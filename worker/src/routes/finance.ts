import type { Env } from "../env.js";
import type { ExpenseRow, NoteRow, ShoppingRow } from "../lib/db.js";
import { error, id, json, now } from "../lib/http.js";

// EXPENSES ---------------------------------------------------------------

export async function listExpenses(
  projectId: string,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const { results } = await env.DB.prepare(
    `SELECT * FROM expenses WHERE project_id = ? ORDER BY spent_at DESC`,
  )
    .bind(projectId)
    .all<ExpenseRow>();
  const sumRow = await env.DB.prepare(
    `SELECT COALESCE(SUM(amount_gr), 0) AS total FROM expenses WHERE project_id = ?`,
  )
    .bind(projectId)
    .first<{ total: number }>();
  return json({ expenses: results, totalGr: sumRow?.total ?? 0 }, 200, cors);
}

export async function createExpense(
  projectId: string,
  req: Request,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const body = (await req.json().catch(() => null)) as Partial<ExpenseRow> | null;
  if (!body?.name || body.amount_gr == null || !body.category) {
    return error("Missing name/amount_gr/category", 400, cors);
  }
  const ts = now();
  const expenseId = id("exp");
  await env.DB.prepare(
    `INSERT INTO expenses (id, project_id, room_id, category, supplier, name, amount_gr, note, spent_at, created_at)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
  )
    .bind(
      expenseId,
      projectId,
      body.room_id ?? null,
      body.category,
      body.supplier ?? null,
      body.name,
      body.amount_gr,
      body.note ?? null,
      body.spent_at ?? ts,
      ts,
    )
    .run();
  return json({ id: expenseId }, 201, cors);
}

export async function deleteExpense(
  expenseId: string,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const res = await env.DB.prepare(`DELETE FROM expenses WHERE id = ?`).bind(expenseId).run();
  if (res.meta.changes === 0) return error("Not found", 404, cors);
  return json({ ok: true }, 200, cors);
}

// SHOPPING ---------------------------------------------------------------

export async function listShopping(
  projectId: string,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const { results } = await env.DB.prepare(
    `SELECT * FROM shopping_items WHERE project_id = ? ORDER BY supplier, created_at`,
  )
    .bind(projectId)
    .all<ShoppingRow>();
  return json({ items: results }, 200, cors);
}

export async function createShopping(
  projectId: string,
  req: Request,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const body = (await req.json().catch(() => null)) as Partial<ShoppingRow> | null;
  if (!body?.name || !body.supplier) return error("Missing name/supplier", 400, cors);
  const itemId = id("shp");
  await env.DB.prepare(
    `INSERT INTO shopping_items (id, project_id, room_id, supplier, name, quantity, unit, price_gr, url, status, created_at)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
  )
    .bind(
      itemId,
      projectId,
      body.room_id ?? null,
      body.supplier,
      body.name,
      body.quantity ?? 1,
      body.unit ?? null,
      body.price_gr ?? null,
      body.url ?? null,
      body.status ?? "todo",
      now(),
    )
    .run();
  return json({ id: itemId }, 201, cors);
}

export async function updateShopping(
  itemId: string,
  req: Request,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const body = (await req.json().catch(() => null)) as Partial<ShoppingRow> | null;
  if (!body) return error("Invalid body", 400, cors);
  const fields: string[] = [];
  const values: any[] = [];
  const allowed = ["supplier", "name", "quantity", "unit", "price_gr", "url", "status"] as const;
  for (const k of allowed) {
    if (k in body && body[k] !== undefined) {
      fields.push(`${k} = ?`);
      values.push((body as any)[k]);
    }
  }
  if (fields.length === 0) return error("Nothing to update", 400, cors);
  values.push(itemId);
  const res = await env.DB.prepare(
    `UPDATE shopping_items SET ${fields.join(", ")} WHERE id = ?`,
  )
    .bind(...values)
    .run();
  if (res.meta.changes === 0) return error("Not found", 404, cors);
  return json({ ok: true }, 200, cors);
}

export async function deleteShopping(
  itemId: string,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const res = await env.DB.prepare(`DELETE FROM shopping_items WHERE id = ?`).bind(itemId).run();
  if (res.meta.changes === 0) return error("Not found", 404, cors);
  return json({ ok: true }, 200, cors);
}

// NOTES ------------------------------------------------------------------

export async function listNotes(
  projectId: string,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const { results } = await env.DB.prepare(
    `SELECT * FROM notes WHERE project_id = ? ORDER BY created_at DESC`,
  )
    .bind(projectId)
    .all<NoteRow>();
  return json({ notes: results }, 200, cors);
}

export async function createNote(
  projectId: string,
  req: Request,
  env: Env,
  cors: HeadersInit,
): Promise<Response> {
  const body = (await req.json().catch(() => null)) as Partial<NoteRow> | null;
  if (!body?.content?.trim()) return error("Missing content", 400, cors);
  const noteId = id("nt");
  await env.DB.prepare(
    `INSERT INTO notes (id, project_id, room_id, content, created_at) VALUES (?, ?, ?, ?, ?)`,
  )
    .bind(noteId, projectId, body.room_id ?? null, body.content, now())
    .run();
  return json({ id: noteId }, 201, cors);
}

export async function deleteNote(noteId: string, env: Env, cors: HeadersInit): Promise<Response> {
  const res = await env.DB.prepare(`DELETE FROM notes WHERE id = ?`).bind(noteId).run();
  if (res.meta.changes === 0) return error("Not found", 404, cors);
  return json({ ok: true }, 200, cors);
}
