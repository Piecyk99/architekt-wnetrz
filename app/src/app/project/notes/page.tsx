"use client";
import { Suspense, useEffect, useState } from "react";
import { api } from "@/lib/api";
import type { Note } from "@/lib/types";
import { Button, Card, Spinner, Textarea } from "@/components/ui";
import { TopBar } from "@/components/TopBar";
import { projectHref, useProjectId } from "@/lib/projectId";

export default function Wrapper() {
  return (
    <Suspense fallback={<div className="flex h-screen items-center justify-center"><Spinner /></div>}>
      <NotesPage />
    </Suspense>
  );
}

function NotesPage() {
  const id = useProjectId();
  const [notes, setNotes] = useState<Note[] | null>(null);
  const [draft, setDraft] = useState("");

  const load = async () => {
    if (!id) return;
    const d = await api.listNotes(id);
    setNotes(d.notes);
  };
  useEffect(() => {
    load();
  }, [id]);

  const add = async () => {
    if (!id || !draft.trim()) return;
    await api.createNote(id, { content: draft.trim() });
    setDraft("");
    load();
  };

  const remove = async (n: Note) => {
    if (!confirm("Usunąć notatkę?")) return;
    await api.deleteNote(n.id);
    load();
  };

  return (
    <>
      <TopBar title="Notatki" subtitle={`${notes?.length ?? 0} pozycji`} back={id ? projectHref("/project", id) : "/"} />

      <main className="mx-auto max-w-2xl px-3 py-3 space-y-3">
        <Card>
          <Textarea
            rows={3}
            value={draft}
            onChange={(e) => setDraft(e.target.value)}
            placeholder="Pomysł, wymiar do sprawdzenia, link, cytat..."
          />
          <div className="mt-2 flex justify-end">
            <Button onClick={add} disabled={!draft.trim()}>Dodaj</Button>
          </div>
        </Card>

        {notes === null ? (
          <div className="flex justify-center py-8 text-walnut-500">
            <Spinner />
          </div>
        ) : notes.length === 0 ? (
          <p className="py-8 text-center text-walnut-500">Brak notatek.</p>
        ) : (
          <div className="space-y-2">
            {notes.map((n) => (
              <Card key={n.id} className="flex items-start gap-2">
                <p className="flex-1 whitespace-pre-wrap text-sm">{n.content}</p>
                <button onClick={() => remove(n)} className="text-walnut-400 hover:text-red-600" aria-label="Usuń">
                  ✕
                </button>
              </Card>
            ))}
          </div>
        )}
      </main>
    </>
  );
}
