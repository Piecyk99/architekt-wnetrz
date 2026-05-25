-- Architekt Wnętrz — schema D1
-- Wszystkie kwoty w groszach (PLN * 100) żeby uniknąć floatów.

CREATE TABLE IF NOT EXISTS projects (
  id           TEXT PRIMARY KEY,
  name         TEXT NOT NULL,
  description  TEXT,
  total_area   REAL,
  style        TEXT,
  budget_gr    INTEGER DEFAULT 0,
  status       TEXT NOT NULL DEFAULT 'active',
  created_at   INTEGER NOT NULL,
  updated_at   INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS rooms (
  id            TEXT PRIMARY KEY,
  project_id    TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  name          TEXT NOT NULL,
  area          REAL,
  dimensions    TEXT,
  photo_url     TEXT,
  current_phase INTEGER DEFAULT 1,
  created_at    INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_rooms_project ON rooms(project_id);

CREATE TABLE IF NOT EXISTS messages (
  id          TEXT PRIMARY KEY,
  project_id  TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  room_id     TEXT REFERENCES rooms(id) ON DELETE SET NULL,
  role        TEXT NOT NULL,
  content     TEXT NOT NULL,
  images      TEXT,
  created_at  INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_messages_project ON messages(project_id, created_at);

CREATE TABLE IF NOT EXISTS decisions (
  id          TEXT PRIMARY KEY,
  project_id  TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  room_id     TEXT REFERENCES rooms(id) ON DELETE SET NULL,
  phase       INTEGER NOT NULL,
  category    TEXT NOT NULL,
  key         TEXT NOT NULL,
  value       TEXT NOT NULL,
  created_at  INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_decisions_project ON decisions(project_id, phase);

CREATE TABLE IF NOT EXISTS renders (
  id          TEXT PRIMARY KEY,
  project_id  TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  room_id     TEXT REFERENCES rooms(id) ON DELETE SET NULL,
  message_id  TEXT REFERENCES messages(id) ON DELETE SET NULL,
  type        TEXT NOT NULL,
  prompt      TEXT NOT NULL,
  image_key   TEXT NOT NULL,
  width       INTEGER,
  height      INTEGER,
  created_at  INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_renders_project ON renders(project_id, created_at);

CREATE TABLE IF NOT EXISTS expenses (
  id          TEXT PRIMARY KEY,
  project_id  TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  room_id     TEXT REFERENCES rooms(id) ON DELETE SET NULL,
  category    TEXT NOT NULL,
  supplier    TEXT,
  name        TEXT NOT NULL,
  amount_gr   INTEGER NOT NULL,
  note        TEXT,
  spent_at    INTEGER NOT NULL,
  created_at  INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_expenses_project ON expenses(project_id);

CREATE TABLE IF NOT EXISTS shopping_items (
  id          TEXT PRIMARY KEY,
  project_id  TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  room_id     TEXT REFERENCES rooms(id) ON DELETE SET NULL,
  supplier    TEXT NOT NULL,
  name        TEXT NOT NULL,
  quantity    INTEGER NOT NULL DEFAULT 1,
  unit        TEXT,
  price_gr    INTEGER,
  url         TEXT,
  status      TEXT NOT NULL DEFAULT 'todo',
  created_at  INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_shopping_project ON shopping_items(project_id, supplier);

CREATE TABLE IF NOT EXISTS notes (
  id          TEXT PRIMARY KEY,
  project_id  TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  room_id     TEXT REFERENCES rooms(id) ON DELETE SET NULL,
  content     TEXT NOT NULL,
  created_at  INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_notes_project ON notes(project_id);
