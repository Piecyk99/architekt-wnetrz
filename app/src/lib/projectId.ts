"use client";
import { useSearchParams } from "next/navigation";

export function useProjectId(): string | null {
  const params = useSearchParams();
  return params.get("id");
}

export function projectHref(path: string, projectId: string): string {
  const sep = path.includes("?") ? "&" : "?";
  return `${path}${sep}id=${encodeURIComponent(projectId)}`;
}
