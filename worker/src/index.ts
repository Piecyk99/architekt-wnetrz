/**
 * meble-banana-worker
 * Cloudflare Worker proxy do Gemini Nano Banana API.
 * Pozwala skillowi meble-architekt generować obrazy z dowolnego urządzenia
 * (telefon, web, desktop) bez wystawiania klucza API klientowi.
 *
 * Endpoints:
 *   POST /generate          -> generacja obrazu z promptu
 *   POST /edit              -> edycja istniejącego obrazu (base64 input)
 *   GET  /health            -> ping
 *
 * Bezpieczeństwo:
 *   - GEMINI_API_KEY tylko jako Worker secret (NIE w kodzie)
 *   - Wymaga header `Authorization: Bearer <SHARED_SECRET>` na /generate i /edit
 *   - CORS: zaakceptowany tylko origin claude.ai (+ localhost dla testów)
 */

export interface Env {
  GEMINI_API_KEY: string;       // wrangler secret put GEMINI_API_KEY
  SHARED_SECRET: string;        // wrangler secret put SHARED_SECRET
  ALLOWED_ORIGINS?: string;     // opcjonalnie, comma-separated
}

const GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta/models";
const DEFAULT_MODEL = "gemini-3.1-flash-image-preview";
const DEFAULT_ASPECT = "16:9";
const DEFAULT_RESOLUTION = "2K";

const VALID_RATIOS = new Set([
  "1:1","16:9","9:16","4:3","3:4","2:3","3:2","4:5","5:4","21:9","1:4","4:1","1:8","8:1",
]);
const VALID_RESOLUTIONS = new Set(["512","1K","2K","4K"]);

interface GenerateBody {
  prompt: string;
  aspectRatio?: string;
  resolution?: string;
  model?: string;
}

interface EditBody {
  imageBase64: string;     // surowy base64 (bez data: prefix)
  imageMimeType?: string;  // default image/png
  prompt: string;
  aspectRatio?: string;
  resolution?: string;
  model?: string;
}

function corsHeaders(origin: string | null, allowed: string[]): HeadersInit {
  const isAllowed = origin && allowed.some(a => a === "*" || a === origin);
  return {
    "Access-Control-Allow-Origin": isAllowed ? origin! : allowed[0] ?? "https://claude.ai",
    "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
    "Access-Control-Max-Age": "86400",
  };
}

function json(body: unknown, status: number, extraHeaders: HeadersInit = {}): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json", ...extraHeaders },
  });
}

function authorized(req: Request, env: Env): boolean {
  const h = req.headers.get("Authorization") || "";
  const m = h.match(/^Bearer\s+(.+)$/i);
  if (!m) return false;
  return timingSafeEqual(m[1], env.SHARED_SECRET);
}

function timingSafeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let result = 0;
  for (let i = 0; i < a.length; i++) result |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return result === 0;
}

async function callGemini(
  apiKey: string,
  model: string,
  parts: object[],
  aspectRatio: string,
  resolution: string,
): Promise<{ imageBase64: string; mimeType: string; text: string }> {
  const url = `${GEMINI_BASE}/${model}:generateContent?key=${apiKey}`;
  const body = {
    contents: [{ parts }],
    generationConfig: {
      responseModalities: ["IMAGE"],
      imageConfig: {
        aspectRatio,
        imageSize: resolution,
      },
    },
  };

  const resp = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  if (!resp.ok) {
    const errText = await resp.text();
    throw new Error(`Gemini API ${resp.status}: ${errText}`);
  }

  const data = await resp.json() as any;
  const candidates = data.candidates ?? [];
  if (candidates.length === 0) {
    const reason = data?.promptFeedback?.blockReason ?? "UNKNOWN";
    throw new Error(`No candidates returned. Reason: ${reason}`);
  }
  const respParts = candidates[0]?.content?.parts ?? [];
  let imageBase64 = "";
  let mimeType = "image/png";
  let text = "";
  for (const p of respParts) {
    if (p.inlineData) {
      imageBase64 = p.inlineData.data;
      mimeType = p.inlineData.mimeType ?? "image/png";
    } else if (p.text) {
      text = p.text;
    }
  }
  if (!imageBase64) {
    const finish = candidates[0]?.finishReason ?? "UNKNOWN";
    throw new Error(`No image in response. finishReason: ${finish}`);
  }
  return { imageBase64, mimeType, text };
}

function validate(body: { aspectRatio?: string; resolution?: string }): string | null {
  if (body.aspectRatio && !VALID_RATIOS.has(body.aspectRatio)) {
    return `Invalid aspectRatio. Valid: ${[...VALID_RATIOS].join(", ")}`;
  }
  if (body.resolution && !VALID_RESOLUTIONS.has(body.resolution)) {
    return `Invalid resolution. Valid: ${[...VALID_RESOLUTIONS].join(", ")}`;
  }
  return null;
}

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    const origin = req.headers.get("Origin");
    const allowed = (env.ALLOWED_ORIGINS ?? "https://claude.ai,http://localhost").split(",").map(s => s.trim());
    const cors = corsHeaders(origin, allowed);

    if (req.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: cors });
    }

    if (url.pathname === "/health" && req.method === "GET") {
      return json({ ok: true, ts: Date.now() }, 200, cors);
    }

    if (url.pathname === "/generate" && req.method === "POST") {
      if (!authorized(req, env)) {
        return json({ error: "Unauthorized" }, 401, cors);
      }
      let body: GenerateBody;
      try {
        body = await req.json() as GenerateBody;
      } catch {
        return json({ error: "Invalid JSON" }, 400, cors);
      }
      if (!body.prompt || typeof body.prompt !== "string") {
        return json({ error: "Missing prompt" }, 400, cors);
      }
      const validationErr = validate(body);
      if (validationErr) return json({ error: validationErr }, 400, cors);

      try {
        const result = await callGemini(
          env.GEMINI_API_KEY,
          body.model ?? DEFAULT_MODEL,
          [{ text: body.prompt }],
          body.aspectRatio ?? DEFAULT_ASPECT,
          body.resolution ?? DEFAULT_RESOLUTION,
        );
        return json({
          imageBase64: result.imageBase64,
          mimeType: result.mimeType,
          text: result.text,
          model: body.model ?? DEFAULT_MODEL,
          aspectRatio: body.aspectRatio ?? DEFAULT_ASPECT,
          resolution: body.resolution ?? DEFAULT_RESOLUTION,
        }, 200, cors);
      } catch (e: any) {
        return json({ error: e.message ?? String(e) }, 500, cors);
      }
    }

    if (url.pathname === "/edit" && req.method === "POST") {
      if (!authorized(req, env)) {
        return json({ error: "Unauthorized" }, 401, cors);
      }
      let body: EditBody;
      try {
        body = await req.json() as EditBody;
      } catch {
        return json({ error: "Invalid JSON" }, 400, cors);
      }
      if (!body.prompt || !body.imageBase64) {
        return json({ error: "Missing prompt or imageBase64" }, 400, cors);
      }
      const validationErr = validate(body);
      if (validationErr) return json({ error: validationErr }, 400, cors);

      try {
        const result = await callGemini(
          env.GEMINI_API_KEY,
          body.model ?? DEFAULT_MODEL,
          [
            { text: body.prompt },
            {
              inlineData: {
                mimeType: body.imageMimeType ?? "image/png",
                data: body.imageBase64,
              },
            },
          ],
          body.aspectRatio ?? DEFAULT_ASPECT,
          body.resolution ?? DEFAULT_RESOLUTION,
        );
        return json({
          imageBase64: result.imageBase64,
          mimeType: result.mimeType,
          text: result.text,
          model: body.model ?? DEFAULT_MODEL,
        }, 200, cors);
      } catch (e: any) {
        return json({ error: e.message ?? String(e) }, 500, cors);
      }
    }

    return json({ error: "Not found", path: url.pathname }, 404, cors);
  },
};
