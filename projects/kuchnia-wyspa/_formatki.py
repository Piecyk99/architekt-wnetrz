#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator listy formatek i okuć — kuchnia v3.5. Po pomiarach: popraw wymiary w MODULES i uruchom ponownie.
   python3 _formatki.py  ->  FORMATKI-ROBOCZE.md
"""
P = 18      # grubość płyty
HDF = 3
KORPUS = "kremowy (korpus)"
FR_BEZ = "beż/kaszmir mat (front)"
FR_ORZ = "ciemny orzech mat (front/panel)"

# (nazwa, szer, wys, gł, typ, front_kolor, uwagi)
MODULES = [
    ("DA1 narożna ślepa", 850, 720, 405, "narozna", FR_BEZ, "korpus od ściany B do 850, gł. 405 (za pilastrem); FRONT 240 (610→850), zawias przy stronie południowej — szerszy uderzyłby w korpus ciągu okna; 1 półka; sięg w ślepą część 600"),
    ("DA2 piekarnik+indukcja", 600, 720, 560, "piekarnik", FR_BEZ, "850→1450 — front kończy się na linii ramienia; nisza 560×590 wg karty; szuflada dolna wewn."),
    ("RL1 ramię narożna ślepa", 1140, 720, 460, "narozna", FR_BEZ, "front 580 (otwierany od północy); martwe pole ~560 pod ramieniem przy ścianie A — bez boku zachodniego, dostęp bokiem"),
    ("DB0 cargo 15", 150, 720, 560, "cargo", FR_BEZ, "cargo 150 (Rejs/Peka); róg na zachód od niego obsługuje już DA1"),
    ("DB1 zlewowa", 800, 720, 560, "zlew", FR_BEZ, "bez pleców pełnych (listwa serwisowa); 2 drzwi"),
    ("DB2 zmywarka 45", 450, 0, 0, "front-agd", FR_BEZ, "tylko front 446×~713 wg karty zmywarki"),
    ("DC1 narożna ślepa", 900, 720, 560, "narozna", FR_BEZ, "front 450; martwe pole przy B; docinana blendą 47"),
    ("GA1 górna", 670, 998, 245, "drzwi2g", FR_ORZ, "wisi na LICU pilastra (155+245=400) — front równo z GA2/GA3"),
    ("GA2 górna wąska", 180, 998, 400, "drzwi1g", FR_ORZ, "nad DA1 (670→850); przyprawy"),
    ("GA3 okap", 600, 998, 400, "okap", FR_ORZ, "nad DA2 = 850→1450, wyśrodkowany nad indukcją; konstrukcja wg karty okapu [?]"),
    ("GA4 górna", 500, 998, 400, "drzwi1g", FR_ORZ, "1450→1950, nad ramieniem"),
    ("GC1 górna (ociekarka)", 470, 998, 400, "drzwi1g", FR_ORZ, "ociekarka w szafce"),
    ("GC2 górna", 477, 998, 400, "drzwi1g", FR_ORZ, ""),
    ("C2 słupek cargo", 280, 2378, 580, "slupek", FR_ORZ, "cargo 250/300 [DO WERYFIKACJI] lub półki; front dzielony 1300+1074"),
    ("C4 nadstawka lodówki", 660, 528, 580, "drzwi2n", FR_ORZ, "nad lodówką (od ~1950); kratka went."),
]

PANELE = [
    ("Bok wykończeniowy zabudowy lodówki (przy ściance, z blendą dystansową)", 2478, 680, 1, FR_ORZ),
    ("Panel ryflowany ramienia (lamele — dostawca zewn.)", 1180, 910, 1, FR_ORZ),
    ("Blenda dolna A przy pilastrze (~610 do frontu DA1)", 610, 756, 1, FR_BEZ),
    ("Listwa cokołowa (czarny mat), łącznie ~5 mb", 5000, 150, 1, "czarny mat"),
]

BLATY = [
    ("Blat A (ciąg indukcji)", 1950, 635), ("Blat B (ciąg okna)", 2389, 635),
    ("Blat C1 (niski ciąg)", 947, 635), ("Blat ramienia (docinka na wschód od blatu A)", 545, 500),
]

rows, m2 = [], {}
def add(el, w, h, qty, kolor, obrz):
    rows.append((el, f"{w}×{h}", qty, kolor, obrz))
    m2[kolor] = m2.get(kolor, 0) + (w * h * qty) / 1e6

for (nm, S, H, G, typ, fk, uw) in MODULES:
    if typ == "front-agd":
        add(f"{nm} — front", S - 4, 713, 1, fk, "1,0 mm — 4 krawędzie"); continue
    add(f"{nm} — bok", G, H, 2, KORPUS, "0,4 mm przód")
    add(f"{nm} — dno" + ("/wieniec" if H > 900 else ""), S - 2 * P, G, 2 if H > 900 else 1, KORPUS, "0,4 przód")
    if H <= 900:
        add(f"{nm} — trawersy górne", S - 2 * P, 100, 2, KORPUS, "0,4")
    if typ not in ("zlew",):
        add(f"{nm} — plecy HDF", S - 4, H - 4, 1, "HDF biały", "—")
    if typ in ("drzwi1", "drzwi1g"):
        add(f"{nm} — front", S - 4, (996 if H > 900 else 716), 1, fk, "1,0 — 4 krawędzie")
    if typ in ("drzwi2", "drzwi2g", "zlew"):
        add(f"{nm} — fronty", (S - 6) // 2, (996 if H > 900 else 716), 2, fk, "1,0 — 4 krawędzie")
    if typ == "drzwi2n":
        add(f"{nm} — fronty", (S - 6) // 2, H - 4, 2, fk, "1,0 — 4 krawędzie")
    if typ == "szuflady3":
        add(f"{nm} — fronty szuflad", S - 4, 236, 3, fk, "1,0 — 4 krawędzie")
        add(f"{nm} — półki wewn. brak (szuflady)", 0, 0, 0, KORPUS, "—")
    if typ == "piekarnik":
        add(f"{nm} — front szuflady dolnej", S - 4, 110, 1, fk, "1,0")
        add(f"{nm} — trawers nośny piekarnika", S - 2 * P, 560, 1, KORPUS, "0,4")
    if typ == "narozna":
        add(f"{nm} — front", 446, 716, 1, fk, "1,0 — 4 krawędzie")
        add(f"{nm} — blenda ślepa", 430, 716, 1, fk, "1,0 przód")
    if typ == "slupek":
        add(f"{nm} — fronty", S - 4, 1300, 1, fk, "1,0"); add(f"{nm} — front górny", S - 4, 1070, 1, fk, "1,0")
        add(f"{nm} — półki", S - 2 * P - 1, G - 20, 2, KORPUS, "0,4")
    if typ in ("drzwi1g", "drzwi2g"):
        add(f"{nm} — półki", S - 2 * P - 1, 300, 2, KORPUS, "0,4")
    if typ == "okap":
        add(f"{nm} — front uchylny (wg okapu)", S - 4, 400, 1, fk, "1,0 [~]")

for (nm, w, h, q, k) in PANELE:
    add(nm, w, h, q, k, "1,0 widoczne")

out = ["# Lista formatek i okuć — kuchnia v3.5 (WERSJA ROBOCZA R1)\n",
       "> **NIE DO CIĘCIA.** Wersja do wyceny w KornerGo / oddział Piekary Śląskie. Wymiary finalne po pomiarach łańcuchowych (PLAN pkt 11) — wtedy poprawiamy stałe w `_formatki.py` i lista przeliczy się sama. Blendy i ostatnie moduły w ciągach zawsze docinane na miejscu. Płyta 18 mm; plecy HDF 3 mm nakładane; wysokości korpusów: dolne 720 (nóżki 150), górne 998, słupek 2378.\n",
       "## 1. Formatki\n",
       "| Element | Wymiar (mm) | szt | Płyta/kolor | Obrzeże ABS |", "|---|---|---|---|---|"]
for r in rows:
    if r[2] == 0: continue
    out.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |")

out += ["\n**Szacunek płyt (z zapasem +15% na rozkrój):**\n", "| Kolor | m² netto | m² z zapasem |", "|---|---|---|"]
for k, v in sorted(m2.items(), key=lambda x: -x[1]):
    out.append(f"| {k} | {v:.1f} | {v*1.15:.1f} |")

out += ["""
## 2. Blaty (laminat 38 mm, dekor jasny trawertyn [DO WERYFIKACJI w Korner])

| Blat | Wymiar (mm) | Uwagi |
|---|---|---|""" ]
for (nm, w, h) in BLATY:
    out.append(f"| {nm} | {w}×{h} | docinany na miejscu |")
out += ["""
Łączenia blatów: 3 (narożnik A/B przy pilastrze, narożnik B/C1, A/ramię) — frez + śruby łącznikowe 3 kpl, silikon. Wycięcia: indukcja **560×490** [P] w blacie A, zlew wg szablonu w blacie B — samodzielnie wyrzynarką (krawędzie zabezpieczyć silikonem) albo CNC przy rozkroju.

## 3. Okucia — lista zakupowa (Korner korner.pl: Blum/GTV/Rejs w ofercie)

| Pozycja | Ilość | Uwagi |
|---|---|---|
| Zawiasy puszkowe 110° z prowadnikiem (Blum ClipTop / GTV) | **36 szt** | fronty dolne 2 szt/front, górne ~996 mm 3 szt/front; w tym zapas ~10% |
| Zawiasy 155° (do narożnej DC1) | 2 szt | szeroki kąt przy ślepej |
| Prowadnice szuflad 500 z pełnym wysuwem i dociągiem (Blum Tandembox/GTV Modern Box) | **4 kpl** | DA1 ×3 + DA2 szuflada dolna ×1 |
| Cargo 150 (Rejs/Peka) | 1 kpl | DB0 |
| Cargo spiżarniane wysokie do słupka 280 | 1 kpl | **[DO WERYFIKACJI]** — szerokość niestandard.; alternatywa: półki + drzwi |
| Podnośnik frontu okapu (Aventos HK-S lub wg okapu) | 1 kpl | GA3 — dobór po zakupie okapu |
| Nóżki meblowe 150 + klipsy cokołu | 32 + 16 szt | 8 szafek dolnych ×4 |
| **Cargo narożne (magic corner) do DC1** | 1 kpl | decyzja inwestora 2026-08-13; front 450 ✓ spełnia minimum okucia; ~500–900 zł |
| Zawieszki regulowane górnych + listwa montażowa | 10 szt + 3 mb | GA1-3, GC1-2 |
| Konfirmaty 7×50 + kołki 8×35 + wkręty 4×30/4×16 | 1 opak. każde | montaż korpusów |
| Śruby łącznikowe blatu | 3 kpl | łączenia |
| Listwa gola / frez uchwytowy | ~5 mb | decyzja technologiczna: profil alu vs frez CNC w płycie |
| Kątowniki montażowe (ramię do posadzki, ścianka) | 8 szt | kotwienie ramienia |
| Taśma LED 3000K + profil + zasilacz 24V | ~3 mb + 1 szt | pod GA i GC |
| Blenda dystansowa lodówka–ścianka | 1 szt (~70×2478) | drzwi lodówki >90° |
| Silikon + Silikorner (uszczelka cokołu — Korner korner.eu) | 1+1 | |

## 4. Plan montażu — kolejność (montaż samodzielny)

1. **Instalacje + posadzka docelowa** → pomiary łańcuchowe (PLAN pkt 11) → korekta `_formatki.py` → zamówienie rozkroju z oklejaniem i CNC (puszki 35 pod zawiasy!) w KornerGo, transport Korner.
2. **Skręcenie korpusów** (konfirmaty + kołki; plecy HDF na wkręty) — zacznij od najmniejszych (DB0, GA2) na rozgrzewkę.
3. **Ściana C:** DC1 → słupek C2 → zabudowa lodówki (bok z blendą przy ściance) → nadstawka C4. Poziomowanie od najwyższego punktu podłogi.
4. **Ciąg B:** od narożnika — DB1 (zlew), DB2 (wnęka zmywarki), DB0; skręcanie korpusów ze sobą śrubami.
5. **Ciąg A:** DA1, DA2 (trawers pod piekarnik wg karty).
6. **Ramię:** RL1+RL2 skręcone, ustawione, **kotwienie kątownikami do posadzki**.
7. **Górne:** listwa montażowa na 1480 (dół szafek), zawieszenie GA i GC, blenda górna docinana do sufitu.
8. **Blaty:** B → C1 (łączenie w rogu) → A → ramię (łączenie z A); wycięcia; silikon przy ścianach i oknie.
9. **AGD:** zmywarka, piekarnik, indukcja (elektryk — obwód siłowy!), okap, lodówka (blenda dystansowa przy ściance).
10. **Fronty + regulacja zawiasów**, cokoły z kratką wentylacyjną lodówki, LED, listwy przyblatowe, panel ryflowany na ramię.

**Pomiar → cięcie → montaż. Nigdy odwrotnie.**
"""]
open("FORMATKI-ROBOCZE.md", "w", encoding="utf-8").write("\n".join(out))
print("OK: FORMATKI-ROBOCZE.md")
