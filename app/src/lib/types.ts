export interface Project {
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

export interface Room {
  id: string;
  project_id: string;
  name: string;
  area: number | null;
  dimensions: string | null;
  photo_url: string | null;
  current_phase: number;
  created_at: number;
}

export interface Message {
  id: string;
  project_id: string;
  room_id: string | null;
  role: "user" | "assistant";
  content: string;
  images: string | null;
  created_at: number;
}

export interface Render {
  id: string;
  project_id: string;
  room_id: string | null;
  message_id: string | null;
  type: string;
  prompt: string;
  image_key: string;
  url: string;
  created_at: number;
}

export interface Expense {
  id: string;
  project_id: string;
  room_id: string | null;
  category: string;
  supplier: string | null;
  name: string;
  amount_gr: number;
  note: string | null;
  spent_at: number;
}

export interface ShoppingItem {
  id: string;
  project_id: string;
  room_id: string | null;
  supplier: string;
  name: string;
  quantity: number;
  unit: string | null;
  price_gr: number | null;
  url: string | null;
  status: "todo" | "ordered" | "delivered" | "done";
}

export interface Note {
  id: string;
  project_id: string;
  room_id: string | null;
  content: string;
  created_at: number;
}
