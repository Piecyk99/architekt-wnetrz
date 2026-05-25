import type { Env } from "../env.js";

export interface ProjectRow {
  id: string;
  name: string;
  description: string | null;
  total_area: number | null;
  style: string | null;
  budget_gr: number;
  status: string;
  created_at: number;
  updated_at: number;
}

export interface RoomRow {
  id: string;
  project_id: string;
  name: string;
  area: number | null;
  dimensions: string | null;
  photo_url: string | null;
  current_phase: number;
  created_at: number;
}

export interface MessageRow {
  id: string;
  project_id: string;
  room_id: string | null;
  role: string;
  content: string;
  images: string | null;
  created_at: number;
}

export interface RenderRow {
  id: string;
  project_id: string;
  room_id: string | null;
  message_id: string | null;
  type: string;
  prompt: string;
  image_key: string;
  width: number | null;
  height: number | null;
  created_at: number;
}

export interface ExpenseRow {
  id: string;
  project_id: string;
  room_id: string | null;
  category: string;
  supplier: string | null;
  name: string;
  amount_gr: number;
  note: string | null;
  spent_at: number;
  created_at: number;
}

export interface ShoppingRow {
  id: string;
  project_id: string;
  room_id: string | null;
  supplier: string;
  name: string;
  quantity: number;
  unit: string | null;
  price_gr: number | null;
  url: string | null;
  status: string;
  created_at: number;
}

export interface NoteRow {
  id: string;
  project_id: string;
  room_id: string | null;
  content: string;
  created_at: number;
}

export interface DecisionRow {
  id: string;
  project_id: string;
  room_id: string | null;
  phase: number;
  category: string;
  key: string;
  value: string;
  created_at: number;
}

export const db = (env: Env) => env.DB;
