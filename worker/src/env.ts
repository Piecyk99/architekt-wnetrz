export interface Env {
  // Secrets
  ANTHROPIC_API_KEY: string;
  GEMINI_API_KEY: string;
  SHARED_SECRET: string;

  // Vars (wrangler.toml)
  ALLOWED_ORIGINS?: string;
  CLAUDE_MODEL?: string;
  GEMINI_MODEL?: string;

  // Bindings
  DB: D1Database;
  MEDIA: R2Bucket;
}

export const DEFAULTS = {
  CLAUDE_MODEL: "claude-sonnet-4-6",
  GEMINI_MODEL: "gemini-3.1-flash-image-preview",
  ASPECT_RATIO: "16:9",
  RESOLUTION: "2K",
} as const;
