"use client";
import { Suspense, useEffect, useState } from "react";
import { api } from "@/lib/api";
import type { Render } from "@/lib/types";
import { Spinner } from "@/components/ui";
import { TopBar } from "@/components/TopBar";
import { projectHref, useProjectId } from "@/lib/projectId";

export default function Wrapper() {
  return (
    <Suspense fallback={<div className="flex h-screen items-center justify-center"><Spinner /></div>}>
      <RendersPage />
    </Suspense>
  );
}

function RendersPage() {
  const id = useProjectId();
  const [renders, setRenders] = useState<Render[] | null>(null);
  const [selected, setSelected] = useState<Render | null>(null);

  useEffect(() => {
    if (!id) return;
    api.listRenders(id).then((d) => setRenders(d.renders));
  }, [id]);

  return (
    <>
      <TopBar
        title="Wizualizacje"
        subtitle={`${renders?.length ?? 0} obrazów`}
        back={id ? projectHref("/project", id) : "/"}
      />
      <main className="mx-auto max-w-2xl px-3 py-4">
        {renders === null ? (
          <div className="flex justify-center py-12 text-walnut-500">
            <Spinner />
          </div>
        ) : renders.length === 0 ? (
          <p className="py-12 text-center text-walnut-500">
            Brak wizualizacji. Wróć do czatu i poproś o moodboard lub render.
          </p>
        ) : (
          <div className="grid grid-cols-2 gap-2">
            {renders.map((r) => (
              <button key={r.id} onClick={() => setSelected(r)} className="overflow-hidden rounded-xl">
                <img src={r.url} alt={r.type} className="aspect-video w-full object-cover" />
              </button>
            ))}
          </div>
        )}
      </main>

      {selected ? (
        <div
          className="fixed inset-0 z-40 flex items-center justify-center bg-black/80 p-4"
          onClick={() => setSelected(null)}
        >
          <div className="max-h-full max-w-full">
            <img src={selected.url} alt={selected.type} className="max-h-[85vh] max-w-full rounded-xl" />
            <p className="mt-2 max-h-32 overflow-auto text-xs text-cream-100">{selected.prompt}</p>
          </div>
        </div>
      ) : null}
    </>
  );
}
