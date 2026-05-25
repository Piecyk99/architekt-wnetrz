import type { Env } from "../env.js";
import { streamChat, type ChatMessage, type ContentBlock } from "../lib/claude.js";
import type { MessageRow, ProjectRow, RoomRow } from "../lib/db.js";
import { error, id, json, now } from "../lib/http.js";

const MAX_HISTORY = 40;

interface SendBody {
  text: string;
  roomId?: string | null;
  imageUrls?: string[];
}

export async function listMessages(
  projectId: string,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const { results } = await env.DB.prepare(
    `SELECT * FROM messages WHERE project_id = ? ORDER BY created_at ASC LIMIT 500`,
  )
    .bind(projectId)
    .all<MessageRow>();
  return json({ messages: results }, 200, cors);
}

async function projectContext(env: Env, projectId: string): Promise<string> {
  const project = await env.DB.prepare(`SELECT * FROM projects WHERE id = ?`)
    .bind(projectId)
    .first<ProjectRow>();
  if (!project) return "";

  const { results: rooms } = await env.DB.prepare(
    `SELECT * FROM rooms WHERE project_id = ? ORDER BY created_at`,
  )
    .bind(projectId)
    .all<RoomRow>();

  const { results: decisions } = await env.DB.prepare(
    `SELECT phase, category, key, value FROM decisions
     WHERE project_id = ? ORDER BY phase, created_at`,
  )
    .bind(projectId)
    .all<{ phase: number; category: string; key: string; value: string }>();

  const lines: string[] = [];
  lines.push(`<project>`);
  lines.push(`Nazwa: ${project.name}`);
  if (project.description) lines.push(`Opis: ${project.description}`);
  if (project.total_area) lines.push(`Powierzchnia: ${project.total_area} m²`);
  if (project.style) lines.push(`Styl: ${project.style}`);
  if (project.budget_gr > 0) lines.push(`Budżet: ${(project.budget_gr / 100).toFixed(0)} PLN`);
  if (rooms.length) {
    lines.push(`Pomieszczenia:`);
    for (const r of rooms) {
      const meta = [r.area ? `${r.area} m²` : null, r.dimensions, `faza ${r.current_phase}/9`]
        .filter(Boolean)
        .join(", ");
      lines.push(`  - ${r.name} (${meta})`);
    }
  }
  if (decisions.length) {
    lines.push(`Zapisane decyzje:`);
    for (const d of decisions) {
      lines.push(`  - [faza ${d.phase}/${d.category}] ${d.key}: ${d.value}`);
    }
  }
  lines.push(`</project>`);
  return lines.join("\n");
}

function makeUserContent(text: string, imageUrls?: string[]): string | ContentBlock[] {
  if (!imageUrls || imageUrls.length === 0) return text;
  const blocks: ContentBlock[] = [];
  for (const url of imageUrls) {
    blocks.push({ type: "image", source: { type: "url", url } });
  }
  blocks.push({ type: "text", text });
  return blocks;
}

export async function sendMessage(
  projectId: string,
  req: Request,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const body = (await req.json().catch(() => null)) as SendBody | null;
  if (!body?.text?.trim()) return error("Missing 'text'", 400, cors);

  const project = await env.DB.prepare(`SELECT id FROM projects WHERE id = ?`)
    .bind(projectId)
    .first();
  if (!project) return error("Project not found", 404, cors);

  const ts = now();
  const userMsgId = id("msg");
  await env.DB.prepare(
    `INSERT INTO messages (id, project_id, room_id, role, content, images, created_at)
     VALUES (?, ?, ?, 'user', ?, ?, ?)`,
  )
    .bind(
      userMsgId,
      projectId,
      body.roomId ?? null,
      body.text,
      body.imageUrls?.length ? JSON.stringify(body.imageUrls) : null,
      ts,
    )
    .run();

  const { results: history } = await env.DB.prepare(
    `SELECT role, content, images FROM messages
     WHERE project_id = ? ORDER BY created_at DESC LIMIT ?`,
  )
    .bind(projectId, MAX_HISTORY)
    .all<{ role: string; content: string; images: string | null }>();

  const messages: ChatMessage[] = history
    .reverse()
    .map((m) => {
      const imgs = m.images ? (JSON.parse(m.images) as string[]) : [];
      return {
        role: m.role as "user" | "assistant",
        content: m.role === "user" && imgs.length ? makeUserContent(m.content, imgs) : m.content,
      };
    });

  const ctx = await projectContext(env, projectId);

  const assistantMsgId = id("msg");
  const claudeResp = await streamChat(env, {
    messages,
    extraSystemContext: ctx,
  });

  if (!claudeResp.body || !claudeResp.ok) {
    return new Response(claudeResp.body, {
      status: claudeResp.status,
      headers: { ...cors, "Content-Type": "text/event-stream" },
    });
  }

  let acc = "";
  const stream = new ReadableStream({
    async start(controller) {
      const enc = new TextEncoder();
      const dec = new TextDecoder();
      const reader = claudeResp.body!.getReader();

      controller.enqueue(
        enc.encode(
          `event: meta\ndata: ${JSON.stringify({ userMsgId, assistantMsgId, ts })}\n\n`,
        ),
      );

      try {
        while (true) {
          const { value, done } = await reader.read();
          if (done) break;
          const chunk = dec.decode(value, { stream: true });
          for (const line of chunk.split("\n")) {
            if (!line.startsWith("data: ")) continue;
            const payload = line.slice(6).trim();
            if (!payload) continue;
            try {
              const evt = JSON.parse(payload);
              if (evt.type === "content_block_delta" && evt.delta?.type === "text_delta") {
                acc += evt.delta.text;
                controller.enqueue(
                  enc.encode(`event: delta\ndata: ${JSON.stringify({ text: evt.delta.text })}\n\n`),
                );
              } else if (evt.type === "message_stop") {
                // saved below
              } else if (evt.type === "error") {
                controller.enqueue(
                  enc.encode(`event: error\ndata: ${JSON.stringify(evt)}\n\n`),
                );
              }
            } catch {
              // ignore parse errors on partial chunks
            }
          }
        }
      } catch (e: any) {
        controller.enqueue(
          enc.encode(`event: error\ndata: ${JSON.stringify({ message: String(e) })}\n\n`),
        );
      }

      try {
        await env.DB.prepare(
          `INSERT INTO messages (id, project_id, room_id, role, content, images, created_at)
           VALUES (?, ?, ?, 'assistant', ?, NULL, ?)`,
        )
          .bind(assistantMsgId, projectId, body.roomId ?? null, acc, now())
          .run();
        await persistInlineBlocks(env, projectId, body.roomId ?? null, assistantMsgId, acc);
      } catch (e: any) {
        controller.enqueue(
          enc.encode(`event: error\ndata: ${JSON.stringify({ message: `persist: ${e}` })}\n\n`),
        );
      }

      controller.enqueue(enc.encode(`event: done\ndata: {}\n\n`));
      controller.close();
    },
  });

  return new Response(stream, {
    headers: {
      ...cors,
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache, no-transform",
      "X-Accel-Buffering": "no",
    },
  });
}

const FENCE_RE = /```(decision|shopping)\n([\s\S]*?)```/g;

function parseFenceBlock(body: string): Record<string, string> {
  const out: Record<string, string> = {};
  for (const raw of body.split("\n")) {
    const line = raw.trim();
    if (!line) continue;
    const idx = line.indexOf(":");
    if (idx === -1) continue;
    const k = line.slice(0, idx).trim();
    const v = line.slice(idx + 1).trim();
    if (k) out[k] = v;
  }
  return out;
}

async function persistInlineBlocks(
  env: Env,
  projectId: string,
  roomId: string | null,
  _messageId: string,
  text: string,
): Promise<void> {
  const stmts: D1PreparedStatement[] = [];
  const ts = now();

  let m: RegExpExecArray | null;
  while ((m = FENCE_RE.exec(text)) !== null) {
    const [, kind, body] = m;
    const data = parseFenceBlock(body);

    if (kind === "decision" && data.key && data.value) {
      stmts.push(
        env.DB.prepare(
          `INSERT INTO decisions (id, project_id, room_id, phase, category, key, value, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
        ).bind(
          id("dec"),
          projectId,
          roomId,
          Number(data.phase) || 1,
          data.category || "other",
          data.key,
          data.value,
          ts,
        ),
      );
    } else if (kind === "shopping" && data.name && data.supplier) {
      const priceGr = data.price ? Math.round(Number(data.price.replace(/[^\d.]/g, "")) * 100) : null;
      stmts.push(
        env.DB.prepare(
          `INSERT INTO shopping_items (id, project_id, room_id, supplier, name, quantity, unit, price_gr, url, status, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'todo', ?)`,
        ).bind(
          id("shp"),
          projectId,
          roomId,
          data.supplier,
          data.name,
          Number(data.quantity) || 1,
          data.unit || null,
          priceGr,
          data.url || null,
          ts,
        ),
      );
    }
  }

  if (stmts.length) await env.DB.batch(stmts);
}
