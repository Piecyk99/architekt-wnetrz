import type { Env } from "../env.js";
import { error, id, json, now } from "../lib/http.js";
import { base64ToBytes, generateImage } from "../lib/gemini.js";
import type { RenderRow } from "../lib/db.js";

const MAX_UPLOAD_BYTES = 8 * 1024 * 1024;

export async function uploadPhoto(
  projectId: string,
  req: Request,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const ct = req.headers.get("Content-Type") ?? "";
  if (!ct.startsWith("image/")) {
    return error("Body must be image/* with Content-Type set", 415, cors);
  }
  const len = Number(req.headers.get("Content-Length") ?? "0");
  if (len > MAX_UPLOAD_BYTES) {
    return error(`Image too large (>${MAX_UPLOAD_BYTES} bytes)`, 413, cors);
  }
  const ext = ct.split("/")[1]?.split("+")[0] ?? "bin";
  const key = `photos/${projectId}/${id("ph")}.${ext}`;
  const bytes = new Uint8Array(await req.arrayBuffer());
  await env.MEDIA.put(key, bytes, { httpMetadata: { contentType: ct } });
  return json({ key, url: `/media/${key}`, size: bytes.byteLength }, 201, cors);
}

export async function serveMedia(key: string, env: Env, cors: HeadersInit): Promise<Response> {
  const obj = await env.MEDIA.get(key);
  if (!obj) return error("Not found", 404, cors);
  const headers = new Headers(cors);
  headers.set("Content-Type", obj.httpMetadata?.contentType ?? "application/octet-stream");
  headers.set("Cache-Control", "public, max-age=31536000, immutable");
  headers.set("Content-Length", obj.size.toString());
  return new Response(obj.body, { headers });
}

interface RenderBody {
  prompt: string;
  type?: string;
  aspectRatio?: string;
  resolution?: string;
  roomId?: string | null;
  messageId?: string | null;
  inputImageUrl?: string | null;
}

export async function renderImage(
  projectId: string,
  req: Request,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const body = (await req.json().catch(() => null)) as RenderBody | null;
  if (!body?.prompt?.trim()) return error("Missing 'prompt'", 400, cors);

  let imageBase64: string | undefined;
  let imageMimeType: string | undefined;
  if (body.inputImageUrl) {
    const key = body.inputImageUrl.replace(/^\/?media\//, "");
    const obj = await env.MEDIA.get(key);
    if (obj) {
      const bytes = new Uint8Array(await obj.arrayBuffer());
      imageBase64 = bytesToBase64(bytes);
      imageMimeType = obj.httpMetadata?.contentType ?? "image/png";
    }
  }

  try {
    const result = await generateImage(env, {
      prompt: body.prompt,
      aspectRatio: body.aspectRatio,
      resolution: body.resolution,
      imageBase64,
      imageMimeType,
    });
    const ext = result.mimeType.split("/")[1] ?? "png";
    const renderId = id("rnd");
    const key = `renders/${projectId}/${renderId}.${ext}`;
    await env.MEDIA.put(key, base64ToBytes(result.imageBase64), {
      httpMetadata: { contentType: result.mimeType },
    });
    await env.DB.prepare(
      `INSERT INTO renders (id, project_id, room_id, message_id, type, prompt, image_key, created_at)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
    )
      .bind(
        renderId,
        projectId,
        body.roomId ?? null,
        body.messageId ?? null,
        body.type ?? "render",
        body.prompt,
        key,
        now(),
      )
      .run();
    return json(
      {
        id: renderId,
        key,
        url: `/media/${key}`,
        mimeType: result.mimeType,
        text: result.text,
      },
      201,
      cors,
    );
  } catch (e: any) {
    return error(String(e.message ?? e), 500, cors);
  }
}

export async function listRenders(
  projectId: string,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const { results } = await env.DB.prepare(
    `SELECT * FROM renders WHERE project_id = ? ORDER BY created_at DESC LIMIT 200`,
  )
    .bind(projectId)
    .all<RenderRow>();
  const renders = results.map((r) => ({ ...r, url: `/media/${r.image_key}` }));
  return json({ renders }, 200, cors);
}

function bytesToBase64(bytes: Uint8Array): string {
  let bin = "";
  for (let i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
  return btoa(bin);
}
