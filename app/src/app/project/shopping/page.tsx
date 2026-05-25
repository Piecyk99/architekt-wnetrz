"use client";
import { Suspense, useEffect, useMemo, useState } from "react";
import { api } from "@/lib/api";
import type { ShoppingItem } from "@/lib/types";
import { Button, Card, Input, Label, Spinner, formatPLN } from "@/components/ui";
import { TopBar } from "@/components/TopBar";
import { projectHref, useProjectId } from "@/lib/projectId";

const STATUSES: Array<{ key: ShoppingItem["status"]; label: string }> = [
  { key: "todo", label: "Do kupienia" },
  { key: "ordered", label: "Zamówione" },
  { key: "delivered", label: "Dostarczone" },
  { key: "done", label: "Zamknięte" },
];

export default function Wrapper() {
  return (
    <Suspense fallback={<div className="flex h-screen items-center justify-center"><Spinner /></div>}>
      <ShoppingPage />
    </Suspense>
  );
}

function ShoppingPage() {
  const id = useProjectId();
  const [items, setItems] = useState<ShoppingItem[] | null>(null);
  const [adding, setAdding] = useState(false);
  const [draft, setDraft] = useState({ supplier: "Korner", name: "", quantity: "1", price: "" });

  const load = async () => {
    if (!id) return;
    const d = await api.listShopping(id);
    setItems(d.items);
  };
  useEffect(() => {
    load();
  }, [id]);

  const grouped = useMemo(() => {
    const g: Record<string, ShoppingItem[]> = {};
    for (const it of items ?? []) (g[it.supplier] ||= []).push(it);
    return g;
  }, [items]);

  const totalGr = useMemo(
    () => (items ?? []).reduce((s, i) => s + (i.price_gr ?? 0) * i.quantity, 0),
    [items],
  );

  const save = async () => {
    if (!id || !draft.name.trim()) return;
    await api.createShopping(id, {
      supplier: draft.supplier,
      name: draft.name.trim(),
      quantity: Number(draft.quantity) || 1,
      price_gr: draft.price ? Math.round(Number(draft.price) * 100) : null,
    });
    setDraft({ supplier: draft.supplier, name: "", quantity: "1", price: "" });
    setAdding(false);
    load();
  };

  const cycleStatus = async (it: ShoppingItem) => {
    const order: ShoppingItem["status"][] = ["todo", "ordered", "delivered", "done"];
    const next = order[(order.indexOf(it.status) + 1) % order.length];
    await api.updateShopping(it.id, { status: next });
    load();
  };

  const remove = async (it: ShoppingItem) => {
    if (!confirm(`Usunąć "${it.name}"?`)) return;
    await api.deleteShopping(it.id);
    load();
  };

  return (
    <>
      <TopBar
        title="Listy zakupów"
        subtitle={items ? `${items.length} pozycji · ${formatPLN(totalGr)}` : ""}
        back={id ? projectHref("/project", id) : "/"}
        right={
          <Button size="sm" onClick={() => setAdding(true)}>
            +
          </Button>
        }
      />

      <main className="mx-auto max-w-2xl px-3 py-3">
        {items === null ? (
          <div className="flex justify-center py-12 text-walnut-500">
            <Spinner />
          </div>
        ) : items.length === 0 && !adding ? (
          <Card className="text-center py-12 text-walnut-500">
            <p>Brak pozycji. Lista buduje się sama gdy AI w czacie sugeruje produkty.</p>
          </Card>
        ) : (
          <div className="space-y-4">
            {Object.entries(grouped).map(([supplier, list]) => (
              <Card key={supplier} className="space-y-2">
                <h3 className="font-semibold">{supplier}</h3>
                {list.map((it) => (
                  <div key={it.id} className="flex items-start gap-2 border-t border-walnut-100 pt-2 dark:border-walnut-800">
                    <button
                      onClick={() => cycleStatus(it)}
                      className={`mt-0.5 rounded-full px-2 py-0.5 text-xs ${statusColor(it.status)}`}
                      title="Kliknij by zmienić status"
                    >
                      {STATUSES.find((s) => s.key === it.status)?.label}
                    </button>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm">{it.name}</p>
                      <p className="text-xs text-walnut-500">
                        {it.quantity}×{it.unit ? ` ${it.unit}` : ""}
                        {it.price_gr ? ` · ${formatPLN(it.price_gr * it.quantity)}` : ""}
                      </p>
                      {it.url ? (
                        <a href={it.url} target="_blank" rel="noreferrer" className="text-xs text-walnut-600 underline">
                          Link
                        </a>
                      ) : null}
                    </div>
                    <button onClick={() => remove(it)} className="text-walnut-400 hover:text-red-600" aria-label="Usuń">
                      ✕
                    </button>
                  </div>
                ))}
              </Card>
            ))}
          </div>
        )}

        {adding ? (
          <Card className="fixed bottom-20 left-3 right-3 max-w-2xl mx-auto z-30 space-y-2">
            <h3 className="font-semibold">Nowa pozycja</h3>
            <div>
              <Label>Dostawca</Label>
              <Input value={draft.supplier} onChange={(e) => setDraft({ ...draft, supplier: e.target.value })} />
            </div>
            <div>
              <Label>Nazwa</Label>
              <Input value={draft.name} onChange={(e) => setDraft({ ...draft, name: e.target.value })} autoFocus />
            </div>
            <div className="grid grid-cols-2 gap-2">
              <div>
                <Label>Ilość</Label>
                <Input type="number" inputMode="numeric" value={draft.quantity} onChange={(e) => setDraft({ ...draft, quantity: e.target.value })} />
              </div>
              <div>
                <Label>Cena (PLN/szt)</Label>
                <Input type="number" inputMode="decimal" value={draft.price} onChange={(e) => setDraft({ ...draft, price: e.target.value })} />
              </div>
            </div>
            <div className="flex gap-2">
              <Button variant="ghost" onClick={() => setAdding(false)}>
                Anuluj
              </Button>
              <Button onClick={save} disabled={!draft.name.trim()}>
                Zapisz
              </Button>
            </div>
          </Card>
        ) : null}
      </main>
    </>
  );
}

function statusColor(s: ShoppingItem["status"]): string {
  switch (s) {
    case "todo":
      return "bg-walnut-100 text-walnut-800 dark:bg-walnut-800 dark:text-cream-100";
    case "ordered":
      return "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-100";
    case "delivered":
      return "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-100";
    case "done":
      return "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-100";
  }
}
