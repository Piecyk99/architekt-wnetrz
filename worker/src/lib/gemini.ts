import type { Env } from "../env.js";
import { DEFAULTS } from "../env.js";

const GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta/models";

export const VALID_RATIOS = new Set([
  "1:1", "16:9", "9:16", "4:3", "3:4", "2:3", "3:2", "4:5", "5:4", "21:9",
  "1:4", "4:1", "1:8", "8:1",
]);
export const VALID_RESOLUTIONS = new Set(["512", "1K", "2K", "4K"]);

export interface GeminiResult {
  imageBase64: string;
  mimeType: string;
  text: string;
}

export interface GeminiInput {
  prompt: string;
  aspectRatio?: string;
  resolution?: string;
  imageBase64?: string;
  imageMimeType?: string;
  model?: string;
}

export async function generateImage(env: Env, input: GeminiInput): Promise<GeminiResult> {
  const model = input.model ?? env.GEMINI_MODEL ?? DEFAULTS.GEMINI_MODEL;
  const aspectRatio = input.aspectRatio ?? DEFAULTS.ASPECT_RATIO;
  const resolution = input.resolution ?? DEFAULTS.RESOLUTION;

  if (!VALID_RATIOS.has(aspectRatio)) {
    throw new Error(`Invalid aspectRatio: ${aspectRatio}`);
  }
  if (!VALID_RESOLUTIONS.has(resolution)) {
    throw new Error(`Invalid resolution: ${resolution}`);
  }

  const parts: object[] = [{ text: input.prompt }];
  if (input.imageBase64) {
    parts.push({
      inlineData: {
        mimeType: input.imageMimeType ?? "image/png",
        data: input.imageBase64,
      },
    });
  }

  const url = `${GEMINI_BASE}/${model}:generateContent?key=${env.GEMINI_API_KEY}`;
  const body = {
    contents: [{ parts }],
    generationConfig: {
      responseModalities: ["IMAGE"],
      imageConfig: { aspectRatio, imageSize: resolution },
    },
  };

  const resp = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  if (!resp.ok) {
    throw new Error(`Gemini API ${resp.status}: ${(await resp.text()).slice(0, 500)}`);
  }

  const data = (await resp.json()) as any;
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
    throw new Error(`No image in response. finishReason: ${candidates[0]?.finishReason ?? "UNKNOWN"}`);
  }
  return { imageBase64, mimeType, text };
}

export function base64ToBytes(b64: string): Uint8Array {
  const bin = atob(b64);
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return bytes;
}
