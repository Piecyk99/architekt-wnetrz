import type { Env } from "../env.js";
import type { ProjectRow, RoomRow } from "../lib/db.js";
import { error, id, json, now } from "../lib/http.js";

export async function listProjects(env: Env, cors: HeadersInit): Promise<Response> {
  const { results } = await env.DB.prepare(
    `SELECT * FROM projects ORDER BY updated_at DESC LIMIT 100`,
  ).all<ProjectRow>();
  return json({ projects: results }, 200, cors);
}

export async function createProject(req: Request, env: Env, cors: HeadersInit): Promise<Response> {
  const body = (await req.json().catch(() => null)) as Partial<ProjectRow> & {
    rooms?: Array<Partial<RoomRow>>;
  } | null;
  if (!body || !body.name) return error("Missing 'name'", 400, cors);

  const ts = now();
  const projectId = id("prj");
  await env.DB.prepare(
    `INSERT INTO projects (id, name, description, total_area, style, budget_gr, status, created_at, updated_at)
     VALUES (?, ?, ?, ?, ?, ?, 'active', ?, ?)`,
  )
    .bind(
      projectId,
      body.name,
      body.description ?? null,
      body.total_area ?? null,
      body.style ?? null,
      body.budget_gr ?? 0,
      ts,
      ts,
    )
    .run();

  if (Array.isArray(body.rooms) && body.rooms.length > 0) {
    const stmt = env.DB.prepare(
      `INSERT INTO rooms (id, project_id, name, area, dimensions, photo_url, current_phase, created_at)
       VALUES (?, ?, ?, ?, ?, ?, 1, ?)`,
    );
    const batch = body.rooms
      .filter((r) => r.name)
      .map((r) =>
        stmt.bind(
          id("rm"),
          projectId,
          r.name!,
          r.area ?? null,
          r.dimensions ?? null,
          r.photo_url ?? null,
          ts,
        ),
      );
    if (batch.length > 0) await env.DB.batch(batch);
  }

  const project = await env.DB.prepare(`SELECT * FROM projects WHERE id = ?`)
    .bind(projectId)
    .first<ProjectRow>();
  const { results: rooms } = await env.DB.prepare(
    `SELECT * FROM rooms WHERE project_id = ? ORDER BY created_at`,
  )
    .bind(projectId)
    .all<RoomRow>();

  return json({ project, rooms }, 201, cors);
}

export async function getProject(projectId: string, env: Env, cors: HeadersInit): Promise<Response> {
  const project = await env.DB.prepare(`SELECT * FROM projects WHERE id = ?`)
    .bind(projectId)
    .first<ProjectRow>();
  if (!project) return error("Project not found", 404, cors);

  const { results: rooms } = await env.DB.prepare(
    `SELECT * FROM rooms WHERE project_id = ? ORDER BY created_at`,
  )
    .bind(projectId)
    .all<RoomRow>();

  return json({ project, rooms }, 200, cors);
}

export async function updateProject(
  projectId: string,
  req: Request,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const body = (await req.json().catch(() => null)) as Partial<ProjectRow> | null;
  if (!body) return error("Invalid body", 400, cors);

  const fields: string[] = [];
  const values: any[] = [];
  const allowed = ["name", "description", "total_area", "style", "budget_gr", "status"] as const;
  for (const k of allowed) {
    if (k in body && body[k] !== undefined) {
      fields.push(`${k} = ?`);
      values.push((body as any)[k]);
    }
  }
  if (fields.length === 0) return error("No fields to update", 400, cors);

  fields.push("updated_at = ?");
  values.push(now());
  values.push(projectId);

  const res = await env.DB.prepare(
    `UPDATE projects SET ${fields.join(", ")} WHERE id = ?`,
  )
    .bind(...values)
    .run();
  if (res.meta.changes === 0) return error("Project not found", 404, cors);

  return getProject(projectId, env, cors);
}

export async function deleteProject(
  projectId: string,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const res = await env.DB.prepare(`DELETE FROM projects WHERE id = ?`).bind(projectId).run();
  if (res.meta.changes === 0) return error("Project not found", 404, cors);
  return json({ ok: true }, 200, cors);
}
