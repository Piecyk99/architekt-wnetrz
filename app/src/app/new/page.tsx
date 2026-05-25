"use client";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { api } from "@/lib/api";
import { Button, Card, Input, Label, Spinner, Textarea } from "@/components/ui";
import { TopBar } from "@/components/TopBar";

const STYLES = [
  "Modern Polish Apartment",
  "Japandi",
  "Scandi",
  "Glamour",
  "Industrial",
  "Boho",
  "Wabi-sabi",
  "Mid-century",
  "Coastal",
  "Inny / opisz w czacie",
];

interface RoomDraft {
  name: string;
  area: string;
  dimensions: string;
}

export default function NewProjectPage() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [totalArea, setTotalArea] = useState("");
  const [style, setStyle] = useState(STYLES[0]);
  const [budget, setBudget] = useState("");
  const [rooms, setRooms] = useState<RoomDraft[]>([{ name: "Salon", area: "", dimensions: "" }]);
  const [submitting, setSubmitting] = useState(false);
  const [err, setErr] = useState<string | null>(null);

  const addRoom = () => setRooms((rs) => [...rs, { name: "", area: "", dimensions: "" }]);
  const removeRoom = (i: number) => setRooms((rs) => rs.filter((_, idx) => idx !== i));
  const updateRoom = (i: number, patch: Partial<RoomDraft>) =>
    setRooms((rs) => rs.map((r, idx) => (idx === i ? { ...r, ...patch } : r)));

  const submit = async () => {
    setErr(null);
    setSubmitting(true);
    try {
      const validRooms = rooms.filter((r) => r.name.trim());
      const out = await api.createProject({
        name: name.trim(),
        description: description.trim() || undefined,
        total_area: totalArea ? Number(totalArea) : undefined,
        style: style === "Inny / opisz w czacie" ? undefined : style,
        budget_gr: budget ? Math.round(Number(budget) * 100) : undefined,
        rooms: validRooms.map((r) => ({
          name: r.name.trim(),
          area: r.area ? Number(r.area) : undefined,
          dimensions: r.dimensions.trim() || undefined,
        })),
      });
      router.push(`/project?id=${out.project.id}`);
    } catch (e: any) {
      setErr(String(e.message ?? e));
      setSubmitting(false);
    }
  };

  return (
    <>
      <TopBar title="Nowy projekt" subtitle={`Krok ${step}/3`} back="/" />
      <main className="mx-auto max-w-2xl px-4 py-4 pb-32">
        {err ? <Card className="mb-3 border-red-200 bg-red-50 text-red-800">{err}</Card> : null}

        {step === 1 ? (
          <Card className="space-y-4">
            <div>
              <Label htmlFor="name">Nazwa projektu *</Label>
              <Input
                id="name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="np. Mieszkanie Lipowa 12"
                autoFocus
              />
            </div>
            <div>
              <Label htmlFor="desc">Opis (opcjonalnie)</Label>
              <Textarea
                id="desc"
                rows={3}
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="np. mieszkanie w bloku z lat 70., 3 pokoje, do generalnego remontu, dla pary z dzieckiem"
              />
            </div>
            <div className="grid grid-cols-2 gap-3">
              <div>
                <Label htmlFor="area">Powierzchnia (m²)</Label>
                <Input
                  id="area"
                  type="number"
                  inputMode="decimal"
                  value={totalArea}
                  onChange={(e) => setTotalArea(e.target.value)}
                  placeholder="60"
                />
              </div>
              <div>
                <Label htmlFor="budget">Budżet (PLN)</Label>
                <Input
                  id="budget"
                  type="number"
                  inputMode="numeric"
                  value={budget}
                  onChange={(e) => setBudget(e.target.value)}
                  placeholder="80000"
                />
              </div>
            </div>
          </Card>
        ) : null}

        {step === 2 ? (
          <Card>
            <Label>Styl</Label>
            <div className="grid grid-cols-2 gap-2">
              {STYLES.map((s) => (
                <button
                  key={s}
                  type="button"
                  onClick={() => setStyle(s)}
                  className={`rounded-xl border px-3 py-3 text-left text-sm transition ${
                    style === s
                      ? "border-walnut-500 bg-walnut-50 dark:bg-walnut-800"
                      : "border-walnut-200 dark:border-walnut-700"
                  }`}
                >
                  {s}
                </button>
              ))}
            </div>
            <p className="mt-3 text-xs text-walnut-500">
              Styl możesz zmienić później w czacie. "Modern Polish Apartment" to default skilla — Orzech Royal + kremowy + czarne uchwyty.
            </p>
          </Card>
        ) : null}

        {step === 3 ? (
          <Card className="space-y-3">
            <Label>Pomieszczenia</Label>
            {rooms.map((r, i) => (
              <div key={i} className="rounded-xl border border-walnut-100 p-3 dark:border-walnut-800">
                <div className="flex items-center gap-2">
                  <Input
                    value={r.name}
                    onChange={(e) => updateRoom(i, { name: e.target.value })}
                    placeholder="np. Salon, Kuchnia, Łazienka"
                    className="flex-1"
                  />
                  {rooms.length > 1 ? (
                    <Button variant="ghost" size="sm" onClick={() => removeRoom(i)} aria-label="Usuń">
                      ✕
                    </Button>
                  ) : null}
                </div>
                <div className="mt-2 grid grid-cols-2 gap-2">
                  <Input
                    type="number"
                    inputMode="decimal"
                    value={r.area}
                    onChange={(e) => updateRoom(i, { area: e.target.value })}
                    placeholder="m²"
                  />
                  <Input
                    value={r.dimensions}
                    onChange={(e) => updateRoom(i, { dimensions: e.target.value })}
                    placeholder="np. 4.5×6 m"
                  />
                </div>
              </div>
            ))}
            <Button variant="secondary" onClick={addRoom} className="w-full">
              + Dodaj pomieszczenie
            </Button>
            <p className="text-xs text-walnut-500">
              Możesz pominąć ten krok jeśli planujesz pojedynczy pokój — dodaj jeden lub zostaw domyślnie.
            </p>
          </Card>
        ) : null}
      </main>

      <footer className="fixed bottom-0 left-0 right-0 border-t border-walnut-100 bg-cream-50/95 backdrop-blur dark:bg-walnut-900/95 dark:border-walnut-800 pb-safe">
        <div className="mx-auto flex max-w-2xl items-center justify-between gap-3 px-4 py-3">
          <Button
            variant="ghost"
            onClick={() => setStep((s) => Math.max(1, s - 1))}
            disabled={step === 1 || submitting}
          >
            Wstecz
          </Button>
          {step < 3 ? (
            <Button onClick={() => setStep((s) => s + 1)} disabled={step === 1 && !name.trim()}>
              Dalej
            </Button>
          ) : (
            <Button onClick={submit} disabled={submitting || !name.trim()}>
              {submitting ? <Spinner /> : "Stwórz projekt"}
            </Button>
          )}
        </div>
      </footer>
    </>
  );
}
