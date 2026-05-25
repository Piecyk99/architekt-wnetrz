"use client";
import { Suspense, useEffect, useState } from "react";
import { api } from "@/lib/api";
import type { Expense, Project } from "@/lib/types";
import { Button, Card, Input, Label, Spinner, formatPLN } from "@/components/ui";
import { TopBar } from "@/components/TopBar";
import { projectHref, useProjectId } from "@/lib/projectId";

const CATEGORIES = [
  "wykończenia",
  "meble",
  "oświetlenie",
  "AGD",
  "tekstylia",
  "instalacje",
  "robocizna",
  "inne",
];

export default function Wrapper() {
  return (
    <Suspense fallback={<div className="flex h-screen items-center justify-center"><Spinner /></div>}>
      <BudgetPage />
    </Suspense>
  );
}

function BudgetPage() {
  const id = useProjectId();
  const [project, setProject] = useState<Project | null>(null);
  const [expenses, setExpenses] = useState<Expense[] | null>(null);
  const [totalGr, setTotalGr] = useState(0);
  const [adding, setAdding] = useState(false);
  const [draft, setDraft] = useState({
    name: "",
    category: CATEGORIES[0],
    supplier: "",
    amount: "",
    note: "",
  });

  const load = async () => {
    if (!id) return;
    const [p, e] = await Promise.all([api.getProject(id), api.listExpenses(id)]);
    setProject(p.project);
    setExpenses(e.expenses);
    setTotalGr(e.totalGr);
  };
  useEffect(() => {
    load();
  }, [id]);

  const save = async () => {
    if (!id || !draft.name.trim() || !draft.amount) return;
    await api.createExpense(id, {
      name: draft.name.trim(),
      category: draft.category,
      supplier: draft.supplier.trim() || undefined,
      amount_gr: Math.round(Number(draft.amount) * 100),
      note: draft.note.trim() || undefined,
    });
    setDraft({ name: "", category: CATEGORIES[0], supplier: "", amount: "", note: "" });
    setAdding(false);
    load();
  };

  const remove = async (e: Expense) => {
    if (!confirm(`Usunąć "${e.name}"?`)) return;
    await api.deleteExpense(e.id);
    load();
  };

  const budget = project?.budget_gr ?? 0;
  const remaining = budget - totalGr;
  const percentage = budget > 0 ? Math.min(100, (totalGr / budget) * 100) : 0;

  return (
    <>
      <TopBar
        title="Budżet"
        subtitle={project ? `${formatPLN(totalGr)} / ${budget > 0 ? formatPLN(budget) : "—"}` : ""}
        back={id ? projectHref("/project", id) : "/"}
        right={
          <Button size="sm" onClick={() => setAdding(true)}>
            +
          </Button>
        }
      />

      <main className="mx-auto max-w-2xl px-3 py-3 space-y-3">
        {project ? (
          <Card>
            <div className="flex justify-between text-sm">
              <span className="text-walnut-600 dark:text-cream-200">Wydane</span>
              <span className="font-semibold">{formatPLN(totalGr)}</span>
            </div>
            {budget > 0 ? (
              <>
                <div className="mt-2 h-2 overflow-hidden rounded-full bg-walnut-100 dark:bg-walnut-800">
                  <div
                    className={`h-full ${percentage > 90 ? "bg-red-500" : percentage > 70 ? "bg-amber-500" : "bg-walnut-600"}`}
                    style={{ width: `${percentage}%` }}
                  />
                </div>
                <div className="mt-1 flex justify-between text-xs text-walnut-500">
                  <span>{percentage.toFixed(0)}%</span>
                  <span>{remaining >= 0 ? `Zostało: ${formatPLN(remaining)}` : `Przekroczone o ${formatPLN(-remaining)}`}</span>
                </div>
              </>
            ) : (
              <p className="mt-2 text-xs text-walnut-500">Ustaw budżet projektu żeby widzieć pasek postępu.</p>
            )}
          </Card>
        ) : null}

        {expenses === null ? (
          <div className="flex justify-center py-8 text-walnut-500">
            <Spinner />
          </div>
        ) : expenses.length === 0 && !adding ? (
          <Card className="text-center py-8 text-walnut-500">Brak wydatków.</Card>
        ) : (
          <Card className="space-y-2">
            {expenses.map((e) => (
              <div key={e.id} className="flex items-start justify-between gap-2 border-t border-walnut-100 pt-2 first:border-0 first:pt-0 dark:border-walnut-800">
                <div>
                  <p className="text-sm font-medium">{e.name}</p>
                  <p className="text-xs text-walnut-500">
                    {e.category}
                    {e.supplier ? ` · ${e.supplier}` : ""}
                  </p>
                  {e.note ? <p className="mt-0.5 text-xs italic text-walnut-500">{e.note}</p> : null}
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-sm font-semibold tabular-nums">{formatPLN(e.amount_gr)}</span>
                  <button onClick={() => remove(e)} className="text-walnut-400 hover:text-red-600" aria-label="Usuń">
                    ✕
                  </button>
                </div>
              </div>
            ))}
          </Card>
        )}

        {adding ? (
          <Card className="fixed bottom-20 left-3 right-3 max-w-2xl mx-auto z-30 space-y-2">
            <h3 className="font-semibold">Nowy wydatek</h3>
            <div>
              <Label>Co</Label>
              <Input value={draft.name} onChange={(e) => setDraft({ ...draft, name: e.target.value })} autoFocus placeholder="np. Drzwi wewnętrzne ×3" />
            </div>
            <div className="grid grid-cols-2 gap-2">
              <div>
                <Label>Kategoria</Label>
                <select
                  value={draft.category}
                  onChange={(e) => setDraft({ ...draft, category: e.target.value })}
                  className="w-full rounded-xl border border-walnut-200 bg-white px-3 py-2.5 text-base dark:bg-walnut-900 dark:border-walnut-700 dark:text-cream-50"
                >
                  {CATEGORIES.map((c) => (
                    <option key={c} value={c}>{c}</option>
                  ))}
                </select>
              </div>
              <div>
                <Label>Kwota (PLN)</Label>
                <Input type="number" inputMode="decimal" value={draft.amount} onChange={(e) => setDraft({ ...draft, amount: e.target.value })} />
              </div>
            </div>
            <div>
              <Label>Dostawca (opcjonalnie)</Label>
              <Input value={draft.supplier} onChange={(e) => setDraft({ ...draft, supplier: e.target.value })} />
            </div>
            <div>
              <Label>Notatka (opcjonalnie)</Label>
              <Input value={draft.note} onChange={(e) => setDraft({ ...draft, note: e.target.value })} />
            </div>
            <div className="flex gap-2">
              <Button variant="ghost" onClick={() => setAdding(false)}>Anuluj</Button>
              <Button onClick={save} disabled={!draft.name.trim() || !draft.amount}>Zapisz</Button>
            </div>
          </Card>
        ) : null}
      </main>
    </>
  );
}
