import type { Env } from "../env.js";

export function corsHeaders(origin: string | null, env: Env): HeadersInit {
  const allowed = (env.ALLOWED_ORIGINS ?? "*")
    .split(",")
    .map((s) => s.trim())
    .filter(Boolean);
  const isAllowed = !!origin && (allowed.includes("*") || allowed.includes(origin));
  return {
    "Access-Control-Allow-Origin": isAllowed ? origin! : allowed[0] ?? "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization, X-Requested-With",
    "Access-Control-Max-Age": "86400",
    "Vary": "Origin",
  };
}

export function json(body: unknown, status = 200, headers: HeadersInit = {}): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", ...headers },
  });
}

export function error(message: string, status = 400, headers: HeadersInit = {}): Response {
  return json({ error: message }, status, headers);
}

export function authorized(req: Request, env: Env): boolean {
  const h = req.headers.get("Authorization") ?? "";
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

export function id(prefix = ""): string {
  const r = crypto.randomUUID().replace(/-/g, "").slice(0, 16);
  return prefix ? `${prefix}_${r}` : r;
}

export function now(): number {
  return Math.floor(Date.now() / 1000);
}
