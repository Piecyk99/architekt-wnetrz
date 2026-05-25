/**
 * Architekt Wnętrz — backend Worker
 *
 * Endpoints (wszystkie wymagają Authorization: Bearer <SHARED_SECRET> oprócz /health):
 *
 *   GET  /health
 *
 *   GET  /api/projects
 *   POST /api/projects
 *   GET  /api/projects/:id
 *   PUT  /api/projects/:id
 *   DELETE /api/projects/:id
 *
 *   POST /api/projects/:id/rooms
 *   PUT  /api/rooms/:id
 *   DELETE /api/rooms/:id
 *
 *   GET  /api/projects/:id/messages
 *   POST /api/projects/:id/messages         (SSE streaming odpowiedzi Claude'a)
 *
 *   POST /api/projects/:id/photos           (Content-Type: image/*, raw body)
 *   GET  /media/photos/:projectId/:filename
 *   GET  /media/renders/:projectId/:filename
 *
 *   POST /api/projects/:id/render
 *   GET  /api/projects/:id/renders
 *
 *   GET  /api/projects/:id/expenses
 *   POST /api/projects/:id/expenses
 *   DELETE /api/expenses/:id
 *
 *   GET  /api/projects/:id/shopping
 *   POST /api/projects/:id/shopping
 *   PUT  /api/shopping/:id
 *   DELETE /api/shopping/:id
 *
 *   GET  /api/projects/:id/notes
 *   POST /api/projects/:id/notes
 *   DELETE /api/notes/:id
 *
 *   POST /generate    (legacy — kompatybilność z Claude Code skillem)
 *   POST /edit        (legacy)
 */

import type { Env } from "./env.js";
import { authorized, corsHeaders, error, json } from "./lib/http.js";
import {
  createProject,
  deleteProject,
  getProject,
  listProjects,
  updateProject,
} from "./routes/projects.js";
import { createRoom, deleteRoom, updateRoom } from "./routes/rooms.js";
import { listMessages, sendMessage } from "./routes/messages.js";
import { listRenders, renderImage, serveMedia, uploadPhoto } from "./routes/media.js";
import {
  createExpense,
  createNote,
  createShopping,
  deleteExpense,
  deleteNote,
  deleteShopping,
  listExpenses,
  listNotes,
  listShopping,
  updateShopping,
} from "./routes/finance.js";
import { legacyEdit, legacyGenerate } from "./routes/legacy.js";

interface Route {
  method: string;
  pattern: RegExp;
  handler: (req: Request, env: Env, cors: HeadersInit, params: string[]) => Promise<Response>;
  noAuth?: boolean;
}

const ROUTES: Route[] = [
  { method: "GET", pattern: /^\/health$/, noAuth: true, handler: async (_r, _e, cors) =>
      json({ ok: true, ts: Date.now() }, 200, cors) },

  // Media (no auth — keys use unguessable random IDs; browsers can't send Authorization
  // on <img> requests, so gating here would break chat thumbnails)
  { method: "GET", pattern: /^\/media\/(.+)$/, noAuth: true, handler: async (_r, env, cors, [key]) =>
      serveMedia(decodeURIComponent(key), env, cors) },

  // Projects
  { method: "GET", pattern: /^\/api\/projects$/, handler: async (_r, env, cors) =>
      listProjects(env, cors) },
  { method: "POST", pattern: /^\/api\/projects$/, handler: async (r, env, cors) =>
      createProject(r, env, cors) },
  { method: "GET", pattern: /^\/api\/projects\/([^/]+)$/, handler: async (_r, env, cors, [id]) =>
      getProject(id, env, cors) },
  { method: "PUT", pattern: /^\/api\/projects\/([^/]+)$/, handler: async (r, env, cors, [id]) =>
      updateProject(id, r, env, cors) },
  { method: "DELETE", pattern: /^\/api\/projects\/([^/]+)$/, handler: async (_r, env, cors, [id]) =>
      deleteProject(id, env, cors) },

  // Rooms
  { method: "POST", pattern: /^\/api\/projects\/([^/]+)\/rooms$/, handler: async (r, env, cors, [id]) =>
      createRoom(id, r, env, cors) },
  { method: "PUT", pattern: /^\/api\/rooms\/([^/]+)$/, handler: async (r, env, cors, [id]) =>
      updateRoom(id, r, env, cors) },
  { method: "DELETE", pattern: /^\/api\/rooms\/([^/]+)$/, handler: async (_r, env, cors, [id]) =>
      deleteRoom(id, env, cors) },

  // Messages
  { method: "GET", pattern: /^\/api\/projects\/([^/]+)\/messages$/, handler: async (_r, env, cors, [id]) =>
      listMessages(id, env, cors) },
  { method: "POST", pattern: /^\/api\/projects\/([^/]+)\/messages$/, handler: async (r, env, cors, [id]) =>
      sendMessage(id, r, env, cors) },

  // Photos & renders
  { method: "POST", pattern: /^\/api\/projects\/([^/]+)\/photos$/, handler: async (r, env, cors, [id]) =>
      uploadPhoto(id, r, env, cors) },
  { method: "POST", pattern: /^\/api\/projects\/([^/]+)\/render$/, handler: async (r, env, cors, [id]) =>
      renderImage(id, r, env, cors) },
  { method: "GET", pattern: /^\/api\/projects\/([^/]+)\/renders$/, handler: async (_r, env, cors, [id]) =>
      listRenders(id, env, cors) },

  // Expenses
  { method: "GET", pattern: /^\/api\/projects\/([^/]+)\/expenses$/, handler: async (_r, env, cors, [id]) =>
      listExpenses(id, env, cors) },
  { method: "POST", pattern: /^\/api\/projects\/([^/]+)\/expenses$/, handler: async (r, env, cors, [id]) =>
      createExpense(id, r, env, cors) },
  { method: "DELETE", pattern: /^\/api\/expenses\/([^/]+)$/, handler: async (_r, env, cors, [id]) =>
      deleteExpense(id, env, cors) },

  // Shopping
  { method: "GET", pattern: /^\/api\/projects\/([^/]+)\/shopping$/, handler: async (_r, env, cors, [id]) =>
      listShopping(id, env, cors) },
  { method: "POST", pattern: /^\/api\/projects\/([^/]+)\/shopping$/, handler: async (r, env, cors, [id]) =>
      createShopping(id, r, env, cors) },
  { method: "PUT", pattern: /^\/api\/shopping\/([^/]+)$/, handler: async (r, env, cors, [id]) =>
      updateShopping(id, r, env, cors) },
  { method: "DELETE", pattern: /^\/api\/shopping\/([^/]+)$/, handler: async (_r, env, cors, [id]) =>
      deleteShopping(id, env, cors) },

  // Notes
  { method: "GET", pattern: /^\/api\/projects\/([^/]+)\/notes$/, handler: async (_r, env, cors, [id]) =>
      listNotes(id, env, cors) },
  { method: "POST", pattern: /^\/api\/projects\/([^/]+)\/notes$/, handler: async (r, env, cors, [id]) =>
      createNote(id, r, env, cors) },
  { method: "DELETE", pattern: /^\/api\/notes\/([^/]+)$/, handler: async (_r, env, cors, [id]) =>
      deleteNote(id, env, cors) },

  // Legacy (Claude Code skill compat)
  { method: "POST", pattern: /^\/generate$/, handler: async (r, env, cors) => legacyGenerate(r, env, cors) },
  { method: "POST", pattern: /^\/edit$/, handler: async (r, env, cors) => legacyEdit(r, env, cors) },
];

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    const origin = req.headers.get("Origin");
    const cors = corsHeaders(origin, env);

    if (req.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: cors });
    }

    for (const route of ROUTES) {
      if (route.method !== req.method) continue;
      const m = url.pathname.match(route.pattern);
      if (!m) continue;
      if (!route.noAuth && !authorized(req, env)) {
        return error("Unauthorized", 401, cors);
      }
      try {
        return await route.handler(req, env, cors, m.slice(1));
      } catch (e: any) {
        console.error("Route error:", e);
        return error(`Internal: ${e?.message ?? String(e)}`, 500, cors);
      }
    }

    return error(`Not found: ${req.method} ${url.pathname}`, 404, cors);
  },
};
