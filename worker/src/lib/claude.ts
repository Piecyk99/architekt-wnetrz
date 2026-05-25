import type { Env } from "../env.js";
import { DEFAULTS } from "../env.js";
import { SYSTEM_PROMPT_CACHED } from "./skill.js";

const API_URL = "https://api.anthropic.com/v1/messages";
const API_VERSION = "2023-06-01";

export type ContentBlock =
  | { type: "text"; text: string }
  | { type: "image"; source: { type: "base64"; media_type: string; data: string } }
  | { type: "image"; source: { type: "url"; url: string } };

export interface ChatMessage {
  role: "user" | "assistant";
  content: string | ContentBlock[];
}

export interface ChatOptions {
  messages: ChatMessage[];
  model?: string;
  maxTokens?: number;
  temperature?: number;
  extraSystemContext?: string;
}

function systemBlocks(extra?: string) {
  const blocks: Array<{
    type: "text";
    text: string;
    cache_control?: { type: "ephemeral" };
  }> = [
    {
      type: "text",
      text: SYSTEM_PROMPT_CACHED,
      cache_control: { type: "ephemeral" },
    },
  ];
  if (extra && extra.trim()) {
    blocks.push({ type: "text", text: extra });
  }
  return blocks;
}

export async function streamChat(env: Env, opts: ChatOptions): Promise<Response> {
  const body = {
    model: opts.model ?? env.CLAUDE_MODEL ?? DEFAULTS.CLAUDE_MODEL,
    max_tokens: opts.maxTokens ?? 4096,
    temperature: opts.temperature ?? 0.7,
    system: systemBlocks(opts.extraSystemContext),
    messages: opts.messages,
    stream: true,
  };

  const upstream = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": env.ANTHROPIC_API_KEY,
      "anthropic-version": API_VERSION,
      "anthropic-beta": "prompt-caching-2024-07-31",
    },
    body: JSON.stringify(body),
  });

  if (!upstream.ok || !upstream.body) {
    const errText = await upstream.text();
    return new Response(
      `data: ${JSON.stringify({ type: "error", message: `Claude API ${upstream.status}: ${errText.slice(0, 500)}` })}\n\n`,
      {
        status: upstream.status,
        headers: { "Content-Type": "text/event-stream" },
      },
    );
  }

  return new Response(upstream.body, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache, no-transform",
      "X-Accel-Buffering": "no",
    },
  });
}
