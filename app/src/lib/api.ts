import type { Expense, Message, Note, Project, Render, Room, ShoppingItem } from "./types";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8787";
const SECRET = process.env.NEXT_PUBLIC_SHARED_SECRET || "";

function headers(extra: HeadersInit = {}): HeadersInit {
  return {
    Authorization: `Bearer ${SECRET}`,
    ...extra,
  };
}

async function req<T>(path: string, init: RequestInit = {}): Promise<T> {
  const resp = await fetch(`${API_URL}${path}`, {
    ...init,
    headers: { ...headers(init.headers), ...(init.body ? { "Content-Type": "application/json" } : {}) },
  });
  if (!resp.ok) {
    let msg = `${resp.status} ${resp.statusText}`;
    try {
      const j = (await resp.json()) as { error?: string };
      if (j.error) msg = j.error;
    } catch {}
    throw new Error(msg);
  }
  return (await resp.json()) as T;
}

export function mediaUrl(keyOrPath: string): string {
  if (keyOrPath.startsWith("http")) return keyOrPath;
  const cleaned = keyOrPath.startsWith("/") ? keyOrPath : `/${keyOrPath}`;
  return `${API_URL}${cleaned}`;
}

// PROJECTS ----------------------------------------------------------------

export const api = {
  health: () => req<{ ok: boolean }>("/health"),

  listProjects: () => req<{ projects: Project[] }>("/api/projects"),
  createProject: (body: {
    name: string;
    description?: string;
    total_area?: number;
    style?: string;
    budget_gr?: number;
    rooms?: Array<{ name: string; area?: number; dimensions?: string }>;
  }) =>
    req<{ project: Project; rooms: Room[] }>("/api/projects", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  getProject: (id: string) => req<{ project: Project; rooms: Room[] }>(`/api/projects/${id}`),
  updateProject: (id: string, body: Partial<Project>) =>
    req<{ project: Project; rooms: Room[] }>(`/api/projects/${id}`, {
      method: "PUT",
      body: JSON.stringify(body),
    }),
  deleteProject: (id: string) => req<{ ok: true }>(`/api/projects/${id}`, { method: "DELETE" }),

  createRoom: (projectId: string, body: { name: string; area?: number; dimensions?: string }) =>
    req<{ room: Room }>(`/api/projects/${projectId}/rooms`, {
      method: "POST",
      body: JSON.stringify(body),
    }),
  updateRoom: (id: string, body: Partial<Room>) =>
    req<{ room: Room }>(`/api/rooms/${id}`, { method: "PUT", body: JSON.stringify(body) }),
  deleteRoom: (id: string) => req<{ ok: true }>(`/api/rooms/${id}`, { method: "DELETE" }),

  listMessages: (projectId: string) =>
    req<{ messages: Message[] }>(`/api/projects/${projectId}/messages`),

  // streaming SSE — patrz lib/stream.ts

  uploadPhoto: async (projectId: string, file: Blob) => {
    const resp = await fetch(`${API_URL}/api/projects/${projectId}/photos`, {
      method: "POST",
      headers: { Authorization: `Bearer ${SECRET}`, "Content-Type": file.type || "image/jpeg" },
      body: file,
    });
    if (!resp.ok) throw new Error(`upload failed: ${resp.status}`);
    return (await resp.json()) as { key: string; url: string; size: number };
  },

  renderImage: (
    projectId: string,
    body: { prompt: string; type?: string; aspectRatio?: string; resolution?: string; roomId?: string | null; messageId?: string | null; inputImageUrl?: string | null },
  ) =>
    req<{ id: string; key: string; url: string }>(`/api/projects/${projectId}/render`, {
      method: "POST",
      body: JSON.stringify(body),
    }),
  listRenders: (projectId: string) =>
    req<{ renders: Render[] }>(`/api/projects/${projectId}/renders`),

  listExpenses: (projectId: string) =>
    req<{ expenses: Expense[]; totalGr: number }>(`/api/projects/${projectId}/expenses`),
  createExpense: (projectId: string, body: Partial<Expense> & { name: string; amount_gr: number; category: string }) =>
    req<{ id: string }>(`/api/projects/${projectId}/expenses`, {
      method: "POST",
      body: JSON.stringify(body),
    }),
  deleteExpense: (id: string) => req<{ ok: true }>(`/api/expenses/${id}`, { method: "DELETE" }),

  listShopping: (projectId: string) =>
    req<{ items: ShoppingItem[] }>(`/api/projects/${projectId}/shopping`),
  createShopping: (projectId: string, body: Partial<ShoppingItem> & { name: string; supplier: string }) =>
    req<{ id: string }>(`/api/projects/${projectId}/shopping`, {
      method: "POST",
      body: JSON.stringify(body),
    }),
  updateShopping: (id: string, body: Partial<ShoppingItem>) =>
    req<{ ok: true }>(`/api/shopping/${id}`, { method: "PUT", body: JSON.stringify(body) }),
  deleteShopping: (id: string) => req<{ ok: true }>(`/api/shopping/${id}`, { method: "DELETE" }),

  listNotes: (projectId: string) => req<{ notes: Note[] }>(`/api/projects/${projectId}/notes`),
  createNote: (projectId: string, body: { content: string; room_id?: string | null }) =>
    req<{ id: string }>(`/api/projects/${projectId}/notes`, {
      method: "POST",
      body: JSON.stringify(body),
    }),
  deleteNote: (id: string) => req<{ ok: true }>(`/api/notes/${id}`, { method: "DELETE" }),
};

export { API_URL, SECRET };
