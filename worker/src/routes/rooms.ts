import type { Env } from "../env.js";
import type { RoomRow } from "../lib/db.js";
import { error, id, json, now } from "../lib/http.js";

export async function createRoom(
  projectId: string,
  req: Request,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const body = (await req.json().catch(() => null)) as Partial<RoomRow> | null;
  if (!body?.name) return error("Missing 'name'", 400, cors);

  const project = await env.DB.prepare(`SELECT id FROM projects WHERE id = ?`)
    .bind(projectId)
    .first();
  if (!project) return error("Project not found", 404, cors);

  const roomId = id("rm");
  await env.DB.prepare(
    `INSERT INTO rooms (id, project_id, name, area, dimensions, photo_url, current_phase, created_at)
     VALUES (?, ?, ?, ?, ?, ?, 1, ?)`,
  )
    .bind(
      roomId,
      projectId,
      body.name,
      body.area ?? null,
      body.dimensions ?? null,
      body.photo_url ?? null,
      now(),
    )
    .run();

  const room = await env.DB.prepare(`SELECT * FROM rooms WHERE id = ?`)
    .bind(roomId)
    .first<RoomRow>();
  return json({ room }, 201, cors);
}

export async function updateRoom(
  roomId: string,
  req: Request,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const body = (await req.json().catch(() => null)) as Partial<RoomRow> | null;
  if (!body) return error("Invalid body", 400, cors);

  const fields: string[] = [];
  const values: any[] = [];
  const allowed = ["name", "area", "dimensions", "photo_url", "current_phase"] as const;
  for (const k of allowed) {
    if (k in body && body[k] !== undefined) {
      fields.push(`${k} = ?`);
      values.push((body as any)[k]);
    }
  }
  if (fields.length === 0) return error("No fields to update", 400, cors);
  values.push(roomId);

  const res = await env.DB.prepare(
    `UPDATE rooms SET ${fields.join(", ")} WHERE id = ?`,
  )
    .bind(...values)
    .run();
  if (res.meta.changes === 0) return error("Room not found", 404, cors);

  const room = await env.DB.prepare(`SELECT * FROM rooms WHERE id = ?`)
    .bind(roomId)
    .first<RoomRow>();
  return json({ room }, 200, cors);
}

export async function deleteRoom(roomId: string, env: Env, cors: HeadersInit): Promise<Response> {
  const res = await env.DB.prepare(`DELETE FROM rooms WHERE id = ?`).bind(roomId).run();
  if (res.meta.changes === 0) return error("Room not found", 404, cors);
  return json({ ok: true }, 200, cors);
}
