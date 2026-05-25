/**
 * Endpointy zachowane z workera 1.0 (meble-banana) — używane przez Claude Code skill
 * gdy działa w trybie mobile/web bez D1. Pozwala starym integracjom dalej działać.
 */
import type { Env } from "../env.js";
import { error, json } from "../lib/http.js";
import { generateImage, VALID_RATIOS, VALID_RESOLUTIONS } from "../lib/gemini.js";

export async function legacyGenerate(req: Request, env: Env, cors: HeadersInit): Promise<Response> {
  const body = (await req.json().catch(() => null)) as
    | {
        prompt: string;
        aspectRatio?: string;
        resolution?: string;
        model?: string;
      }
    | null;
  if (!body?.prompt) return error("Missing prompt", 400, cors);
  if (body.aspectRatio && !VALID_RATIOS.has(body.aspectRatio)) {
    return error(`Invalid aspectRatio`, 400, cors);
  }
  if (body.resolution && !VALID_RESOLUTIONS.has(body.resolution)) {
    return error(`Invalid resolution`, 400, cors);
  }
  try {
    const r = await generateImage(env, body);
    return json(
      {
        imageBase64: r.imageBase64,
        mimeType: r.mimeType,
        text: r.text,
        model: body.model ?? env.GEMINI_MODEL,
      },
      200,
      cors,
    );
  } catch (e: any) {
    return error(String(e.message ?? e), 500, cors);
  }
}

export async function legacyEdit(req: Request, env: Env, cors: HeadersInit): Promise<Response> {
  const body = (await req.json().catch(() => null)) as
    | {
        prompt: string;
        imageBase64: string;
        imageMimeType?: string;
        aspectRatio?: string;
        resolution?: string;
        model?: string;
      }
    | null;
  if (!body?.prompt || !body.imageBase64) {
    return error("Missing prompt or imageBase64", 400, cors);
  }
  try {
    const r = await generateImage(env, body);
    return json(
      {
        imageBase64: r.imageBase64,
        mimeType: r.mimeType,
        text: r.text,
        model: body.model ?? env.GEMINI_MODEL,
      },
      200,
      cors,
    );
  } catch (e: any) {
    return error(String(e.message ?? e), 500, cors);
  }
}
