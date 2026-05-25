"use client";
import { useEffect, useState } from "react";
import Link from "next/link";
import { api } from "@/lib/api";
import type { Project } from "@/lib/types";
import { Button, Card, Spinner, formatPLN } from "@/components/ui";
import { TopBar } from "@/components/TopBar";

export default function HomePage() {
  const [projects, setProjects] = useState<Project[] | null>(null);
  const [err, setErr] = useState<string | null>(null);

  useEffect(() => {
    api
      .listProjects()
      .then((d) => setProjects(d.projects))
      .catch((e) => setErr(String(e.message ?? e)));
  }, []);

  return (
    <>
      <TopBar
        title="Architekt Wnętrz"
        subtitle="Twoje projekty"
        right={
          <Link href="/new">
            <Button size="sm">+ Nowy</Button>
          </Link>
        }
      />
      <main className="mx-auto max-w-2xl px-4 py-4 pb-24">
        {err ? (
          <Card className="border-red-200 bg-red-50 text-red-800 dark:bg-red-950 dark:border-red-900 dark:text-red-100">
            <strong>Błąd:</strong> {err}
            <p className="mt-2 text-xs opacity-75">
              Sprawdź czy backend działa pod <code>{process.env.NEXT_PUBLIC_API_URL}</code> i czy SHARED_SECRET się zgadza.
            </p>
          </Card>
        ) : projects === null ? (
          <div className="flex items-center justify-center py-12 text-walnut-500">
            <Spinner />
          </div>
        ) : projects.length === 0 ? (
          <Card className="text-center py-12">
            <h2 className="text-lg font-semibold mb-2">Brak projektów</h2>
            <p className="mb-4 text-walnut-600 dark:text-cream-200">Zacznij od stworzenia pierwszego — np. salon, kuchnia albo całe mieszkanie.</p>
            <Link href="/new">
              <Button>Stwórz pierwszy projekt</Button>
            </Link>
          </Card>
        ) : (
          <ul className="space-y-3">
            {projects.map((p) => (
              <li key={p.id}>
                <Link href={`/project?id=${p.id}`} className="block">
                  <Card className="hover:border-walnut-300 transition">
                    <div className="flex items-start justify-between gap-3">
                      <div className="min-w-0">
                        <h3 className="truncate font-semibold">{p.name}</h3>
                        {p.description ? (
                          <p className="mt-0.5 line-clamp-2 text-sm text-walnut-600 dark:text-cream-200">{p.description}</p>
                        ) : null}
                        <div className="mt-2 flex flex-wrap gap-2 text-xs text-walnut-500">
                          {p.total_area ? <Tag>{p.total_area} m²</Tag> : null}
                          {p.style ? <Tag>{p.style}</Tag> : null}
                          {p.budget_gr > 0 ? <Tag>Budżet: {formatPLN(p.budget_gr)}</Tag> : null}
                        </div>
                      </div>
                      <svg className="h-5 w-5 shrink-0 text-walnut-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <polyline points="9 18 15 12 9 6" />
                      </svg>
                    </div>
                  </Card>
                </Link>
              </li>
            ))}
          </ul>
        )}
      </main>
    </>
  );
}

function Tag({ children }: { children: React.ReactNode }) {
  return (
    <span className="rounded-full bg-walnut-100 px-2 py-0.5 text-walnut-700 dark:bg-walnut-800 dark:text-cream-200">
      {children}
    </span>
  );
}
