import { API_URL, SECRET } from "./api";

export interface StreamEvents {
  onMeta?: (meta: { userMsgId: string; assistantMsgId: string; ts: number }) => void;
  onDelta?: (chunk: string) => void;
  onError?: (msg: string) => void;
  onDone?: () => void;
}

export async function sendMessageStream(
  projectId: string,
  body: { text: string; roomId?: string | null; imageUrls?: string[] },
  events: StreamEvents,
  signal?: AbortSignal,
): Promise<void> {
  const resp = await fetch(`${API_URL}/api/projects/${projectId}/messages`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${SECRET}`,
    },
    body: JSON.stringify(body),
    signal,
  });

  if (!resp.ok || !resp.body) {
    const errText = await resp.text().catch(() => `HTTP ${resp.status}`);
    events.onError?.(errText.slice(0, 500));
    return;
  }

  const reader = resp.body.getReader();
  const dec = new TextDecoder();
  let buffer = "";

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    buffer += dec.decode(value, { stream: true });

    let idx: number;
    while ((idx = buffer.indexOf("\n\n")) !== -1) {
      const block = buffer.slice(0, idx);
      buffer = buffer.slice(idx + 2);

      let event = "message";
      let data = "";
      for (const line of block.split("\n")) {
        if (line.startsWith("event: ")) event = line.slice(7).trim();
        else if (line.startsWith("data: ")) data += line.slice(6);
      }
      if (!data) continue;

      try {
        const parsed = JSON.parse(data);
        if (event === "meta") events.onMeta?.(parsed);
        else if (event === "delta") events.onDelta?.(parsed.text ?? "");
        else if (event === "error") events.onError?.(parsed.message ?? "error");
        else if (event === "done") events.onDone?.();
      } catch {
        // ignore
      }
    }
  }
  events.onDone?.();
}

export interface RenderBlock {
  type: string;
  aspect: string;
  prompt: string;
}

const RENDER_RE = /```render\n([\s\S]*?)```/g;

export function extractRenderBlocks(text: string): RenderBlock[] {
  const out: RenderBlock[] = [];
  let m: RegExpExecArray | null;
  while ((m = RENDER_RE.exec(text)) !== null) {
    const body = m[1];
    const obj: Record<string, string> = {};
    for (const raw of body.split("\n")) {
      const line = raw.trim();
      const idx = line.indexOf(":");
      if (idx === -1) continue;
      const k = line.slice(0, idx).trim();
      const v = line.slice(idx + 1).trim();
      if (k) obj[k] = v;
    }
    if (obj.prompt) {
      out.push({
        type: obj.type || "render",
        aspect: obj.aspect || "16:9",
        prompt: obj.prompt,
      });
    }
  }
  return out;
}

export function stripFenceBlocks(text: string): string {
  return text.replace(/```(render|decision|shopping)\n[\s\S]*?```/g, "").trim();
}
