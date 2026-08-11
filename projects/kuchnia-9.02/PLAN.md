> **Artefakt historyczny sprzed korekty 2026-08. Zawiera nieaktualne dane dostawcy (Korner Żary) i niezweryfikowane kody dekorów. Nie używać jako źródła.**

# Kuchnia 9.02 — projekt zabudowy na wymiar (wariant v4)

Projekt wykonany skillem **architekt-kuchni** na podstawie: rzutu mieszkania (fragment 9.01–9.03), zdjęcia pomieszczenia z adnotacjami wymiarowymi oraz decyzji inwestora. Wykonanie: **samodzielne**, materiały: **Korner (Żary)**.

> **To NIE jest dokumentacja produkcyjna.** Lista formatek do cięcia powstanie dopiero po pomiarach kontrolnych z pkt 12. Wszystkie wartości `[~]` i `[?]` wymagają weryfikacji na miejscu.

Rysunki techniczne: `technical/01–04` (SVG + PNG, generator: `technical/gen.py`).

---

## 1. Podsumowanie pomieszczenia

Kuchnia **9.02, 4,86 m²** (2450 × 1910 mm wewn., wys. ~2490 `[~]`), stan: remont (świeża wylewka). Wysokie okno ~920×810 pod sam sufit (parapet 1680). **Gzyms/komin ~630×370 w lewym górnym narożniku** (przy ścianie z oknem) `[P]`. Krawędź od przedpokoju/salonu **otwarta na odcinku 1740 (dół-lewo)** `[P]`; przy prawym końcu dolnej krawędzi **wnęka na lodówkę 850** `[P]`. Podejścia wodne pod oknem, 2 wypusty oświetleniowe na suficie, puszka elektryczna nisko na prawej ścianie.

Orientacja w całym projekcie: **patrzysz na okno**. Ściana A = z oknem (góra), D = lewa (z gzymsem), B = prawa, krawędź C = dolna (otwarta + wnęka).

## 2. Znane wymiary `[P]` (z rzutu)

| Wymiar | Wartość |
|---|---|
| Ściana A wewn. / zewn. | 2450 / 2590 |
| Głębokość (ściany D i B) | 1910 |
| Gzyms: wzdłuż ściany D × w głąb | 630 × ~370 |
| Ściana D poniżej gzymsu | 1280 |
| Otwarte przejście (krawędź C, lewa część) | 1740 |
| Wnęka lodówki (krawędź C, prawa część) | 850 |
| Lodówka (deklaracja inwestora) | 600×600×2020 |

## 3. Wymiary orientacyjne `[~]` (ze zdjęcia — adnotacje inwestora)

| Wymiar | Wartość | Kontrola |
|---|---|---|
| Wysokość pomieszczenia | ~2490 | 1680+810 = 2490 ✓ |
| Parapet od podłogi | 1680 | mierzone na wylewce — po posadzce zmaleje o 10–30 |
| Okno wys. / szer. | 810 / ~920 | 600+920+930 = 2450 ✓ |
| Od lewej ściany do okna / od okna do prawej | 600 / 930 | |

## 4. Przeszkody architektoniczne

| Element | Konsekwencja |
|---|---|
| **Gzyms/komin 630×370, lewy górny róg** | zabudowa ściany A zaczyna się ZA nim (blenda 30 docinana); słupek S1 przylega od dołu; **sprawdzić czy komin czynny/ciepły** `[?]` |
| Okno do sufitu | brak szafek nad oknem; górne tylko po prawej stronie okna |
| Wnęka 850 + słupek przy niej | lodówka wchodzi we wnękę; kierunek zawiasów do weryfikacji |
| Kratka wentylacyjna | **pozycja NIEPOTWIERDZONA** `[?]` — do tego czasu okap recyrkulacyjny |
| Podejścia wodne pod oknem | strefa zmywania na ścianie A |

## 5. Układ (v4) — decyzje inwestora

- **Wyspa 1000×500 po lewej** (strona gzymsu), przy wejściu do salonu — inwestor świadomie zaakceptował zwężenie przejścia do **min. 700 mm**. Realnie: przejście **~740**, alejka robocza **~810**.
- **Piekarnik + mikrofala w słupku S1 przy gzymsie** (lewa ściana, do sufitu) — ergonomia (AGD na wysokości).
- Wyspa pełnowymiarowa w środku kuchni odrzucona matematyką: 600+1000+600 = 2200 > 1910.
- Kompromis (zapisany świadomie): kuchnia komfortowa dla **jednej osoby gotującej naraz**.

Rzut: `technical/01-rzut-z-gory-WA.png`.

## 6. Rozpisanie zabudowy ściana po ścianie (mm)

**Ściana A (2450), od lewej:** `GZYMS 370 | blenda 30 | D1 ZLEW 800 | D2 zmywarka 450 | D3 cargo 240 | D4 narożna ślepa 560`
Zlew pod oknem, przy podejściach wody. Kolejność: `technical/02-elewacja-A-okno.png`.

**Ściana B (1910), od narożnika z A:** `martwe pole narożne 560 (dostęp z D4) | D5 płyta indukcyjna + szuflady 600 | blenda 150 (bok termoizolacyjny) | LODÓWKA we wnęce 850 (+nadstawka ~400 do sufitu)`
`technical/03-elewacja-B-plyta-lodowka.png`.

**Ściana D (lewa):** `GZYMS (od okna 630, z zabudową S2) | S1 słupek 600 do sufitu: szafka góra / MIKROFALA (otwór 400) / PIEKARNIK (otwór 600) / szuflady dół`
**S2 — zabudowa na kominie:** 630×180 gł., od 1490 do sufitu, na licu gzymsu (fronty H3734 jak S1 — jednolita ciemna wieża). **Mocowanie:** kotwy płytkie 40–50 mm bez udaru (ścianka przewodu min ~65–120 mm — brak ryzyka przebicia), kołki do cegły pełnej, w cegłę nie w spoinę + **bok-podpora oparty na blacie D1** przenoszący ciężar (kotwy tylko stabilizują). Lekkie obciążenie (przyprawy, słoiki). Komin: spalinowe nieużywane (całe ogrzewanie w budynku elektryczne — deklaracja inwestora), kanały wentylacyjne traktować jako czynne — stąd zakaz głębokiego wiercenia.
**WYSPA 1000×500**, blat h ~900, luz od S1 ~120–180; szafki wyspy otwierane **od strony salonu**, nadwieszenie blatu na hokery od strony przejścia. `technical/04-elewacja-D-slupek-wyspa.png`.

**Górne:** G2 890 (prawa strona okna, do sufitu) + półka otwarta ~180–200 między gzymsem a oknem; G4 — opcjonalnie nad D5 wg trasy okapu. LED 3000K pod górnymi.

## 7. Kolejność szafek

- A (od lewej): D1 → D2 → D3 → D4
- B (od góry): D4/narożnik → D5 → blenda → lodówka
- D (od okna): gzyms (S2 nad blatem) → S1 → (luz) → wyspa
- Górne: półka → okno → G2

## 8. Orientacyjne szerokości modułów

| Nr | Typ | Szer.×Wys.×Głęb. | Wnętrze | Uwagi |
|---|---|---|---|---|
| D1 | zlewowa | 800×720+100×580 | zlew 1-komora z ociekaczem, kosz | bez pleców / plecy serwisowe |
| D2 | zmywarka | 450 (zabudowa) | front meblowy | przy zlewie |
| D3 | cargo | 240×720+100×580 | cargo przyprawnik | |
| D4 | narożna ślepa | 560 (front ~450) | półki / carousel | blat w narożnik |
| D5 | płyta | 600×720+100×580 | 2 szuflady pod płytą | indukcja 4-pol. (otwór 560×490) |
| S1 | słupek AGD | 600×~2390×580 | mikrofala 400 + piekarnik 600 + szuflady | przy gzymsie, do sufitu |
| S2 | zabudowa na kominie | 630×~1000×180 | płytkie półki | kotwy 40–50 bez udaru + bok na blacie D1 |
| WYSPA | korpusy 2×500 | 1000×~860+blat×500 | półki/szuflady od salonu | blat ~900, nadwieszenie 200–250 |
| G2 | górna | 890×~1000×320 | półki | do sufitu |
| Nadstawka L | nad lodówką | ~590×~400×580 | otwarta/front | kratka wentylacyjna |

Wszystkie moduły przy ścianach: szerokości finalne po pomiarach (blendy docinane).

## 9. Rozmieszczenie AGD

| Urządzenie | Pozycja | Wymagania |
|---|---|---|
| Zlew + bateria | D1, pod oknem | podejścia wody + odpływ 50 (są pod oknem `[P]`) |
| Zmywarka 45 | D2 | woda+odpływ z D1, gniazdo w D3/D1 |
| Płyta indukcyjna | D5 | obwód siłowy 32A `[?]` — do wykonania |
| Piekarnik | S1 (wys. ~800–1400) | gniazdo 16A osobny obwód — nowy punkt na ścianie D |
| Mikrofala | S1 (nad piekarnikiem) | gniazdo 230V w słupku |
| Okap | nad D5 | recyrkulacja do czasu potwierdzenia kratki `[?]` |
| Lodówka | wnęka 850 | gniazdo za/obok, wentylacja 50 tył+góra, kratka w cokole i nadstawce |

## 10. Zalecenia instalacyjne (PRZED montażem)

1. Obwód siłowy 32A do D5 (płyta) + 16A do S1 (piekarnik) + gniazda: mikrofala (S1), zmywarka, lodówka, 2–3 nad blatem A.
2. Zasilanie LED podszafkowego (transformator w G2 lub S1).
3. Ewentualne gniazdo w wyspie (wymaga doprowadzenia w podłodze — decyzja przed wylewką docelową!).
4. Potwierdzić kratkę wentylacyjną; jeśli jest nad B — możliwy okap z wyrzutem (kanał w obudowie).
5. Wymiary pionowe przemierzyć PO położeniu posadzki docelowej.

## 11. Ryzyka

| Ryzyko | Mitygacja |
|---|---|
| Komin czynny/ciepły przy S1 | sprawdzić w administracji; ew. izolacja lub odsunięcie S1 |
| Głębokość gzymsu ≠ 370 na różnych wysokościach | pomiar w 3 punktach; blenda przy D1 docinana |
| Przejście 740 przy krzywych ścianach może spaść <700 | pomiar przed finalną szerokością wyspy (można zwęzić do 900) |
| Kratka wentylacyjna w strefie G2/okapu | pomiar; zabudowa z kratką rewizyjną |
| Zawiasy lodówki | otwieranie od strony blatu; ew. blenda dystansowa |
| Posadzka docelowa zmieni wymiary pionowe | wszystkie wysokości finalne po posadzce |

## 12. Lista pomiarów kontrolnych dla stolarza / przed cięciem formatek

1. Ściana A na wys. 0 / 860 / 2100 (krzywizna) i ściana B j.w.
2. **Gzyms: dokładne 63×37 przy podłodze, na wys. blatu i przy suficie + czy komin czynny**
3. Wysokość podłoga–sufit w 4 punktach **po posadzce docelowej**
4. Przekątne narożnika A/B (kąt prosty?)
5. Okno: szerokość z ościeżami, parapet (wysokość + głębokość)
6. Wnęka lodówki: 850 dołem i górą + głębokość; kierunek zawiasów lodówki
7. Podejścia wody: wysokość, rozstaw, odpływ; zawory
8. **Kratka wentylacyjna: pozycja i wymiar**
9. Pozycje istniejących puszek elektrycznych; możliwość obwodów 32A/16A
10. Światło otwartego przejścia (174?) dołem i górą
11. Poziom podłogi na linii zabudowy A i B oraz pod wyspą

**Projekt musi zostać zweryfikowany pomiarem na miejscu przed produkcją/cięciem mebli.**

## 13. Materiały i styl — wg inspiracji inwestora (2026-07-28)

Inwestor dostarczył zdjęcie referencyjne (mała kuchnia otwarta na salon, półwysep z hokerami) — paleta zmapowana na układ v4 i katalog Korner:

| Element | Materiał / dekor (Korner) | Uwagi |
|---|---|---|
| Fronty dolne A (D1–D4) + B (D5) + korpus wyspy | **beż/kaszmir mat, bezuchwytowe** (Egger U702 ST9 Kaszmir lub zbliżony beż mat) | uchwyt frezowany/gola; korpusy kremowe |
| Górne G2 + słupek S1 (do sufitu) | **Egger H3734 ST9 Orzech Pacific mat** (house style — zgodny 1:1 z inspiracją) | słoje pionowe |
| Zabudowa lodówki (panele wnęki + nadstawka) | **grafit/czarny mat** (Egger U999 ST2 lub grafit) | jak ciemna kolumna na zdjęciu |
| Blat A/B + blat wyspy | **jasny kamień/trawertyn — laminat 38 mm** (Egger dekor jasny kamień beż) | ⚠ odstępstwo od house style (spiek czarny) na wyraźne życzenie inwestora — wg inspiracji |
| Ściana nad blatem przy płycie (B) | panel ciemny kamień/grafit mat (laminat kompaktowy lub spiek) | tylko strefa płyty; reszta ścian farba beż jak salon |
| Front wyspy od strony przejścia/salonu | **panel ryflowany (lamele) ciemny orzech/czarny** | jak na zdjęciu referencyjnym |
| Armatura + zlew | bateria czarna mat, zlew granitowy czarny | zlew pod oknem |
| Oświetlenie | LED 3000K pod G2 i pod nadwieszeniem wyspy; 2× czarny spot natynkowy na suficie (istniejące wypusty) | ciepłe światło jak na zdjęciu |
| Hokery | 2× czarne metalowe, siedzisko ~65 cm | od strony salonu |
| Cokoły | czarny mat (cofnięte optycznie) | kratka wentylacyjna lodówki w cokole |

## 14. Prompt — realistyczna wizualizacja (EN, Gemini)

```
Architectural interior photograph of a small custom kitchen in a Polish apartment,
2.45 x 1.91 m, ceiling 2.49 m. High window (~92x81 cm) on the far wall reaching the
ceiling, sill at 168 cm — keep it. A floor-to-ceiling chimney pillar (~37 x 63 cm)
in the FAR-LEFT corner — keep it visible. Along the window wall, starting right of
the chimney: 80 cm sink base under the window, 45 cm dishwasher, 24 cm spice
pull-out, blind corner unit. Right wall: induction hob with drawers under, chimney
hood above, then a tall fridge (60 cm, 202 cm) in a niche with a top cabinet.
Left wall, below the chimney: a tall column with built-in microwave and oven at eye
level. A small island (100 x 50 cm, worktop at 90 cm) near the open passage to the
living room, its doors facing the living room, counter overhang with two bar stools.
Materials per the client's reference: handleless matte beige/cashmere lower fronts,
upper cabinets and the tall oven column in dark matte walnut woodgrain reaching the
ceiling, the fridge column in matte graphite/black, light travertine-look stone
worktop on the runs and the island, dark stone backsplash panel behind the hob only,
remaining walls warm beige paint. The island front facing the living room is a dark
fluted (reeded) wood panel; light stone island top with an overhang and two black
metal bar stools. Black matte faucet and black granite sink under the window,
under-cabinet LED 3000K, two black surface-mounted ceiling spots, warm daylight
from the window. Camera at the open passage, eye level 160 cm, 24 mm lens. No
people. Architectural Digest editorial aesthetic.
STRICT CONSTRAINTS: do not move or resize the window; do not remove the chimney
pillar; do not enlarge the room; island exactly 100x50 at the passage — nothing
larger; no cabinets above the window; nothing beyond the listed cabinets.
```

## 15. Prompt — naniesienie projektu na zdjęcie pomieszczenia (EN, `gemini_edit_image`)

Referencja: zdjęcie pomieszczenia z adnotacjami (kadr od przejścia w stronę okna).

```
Using the attached photo of the empty room as the exact base: render the designed
kitchen into this room. Keep the photo's camera position, perspective, the high
window with its sill, the chimney pillar in the left corner, wall plumbing stubs
and ceiling wiring points exactly as in the photo. Install: along the window wall
(right of the chimney) — sink base 80 under the window, dishwasher 45, spice
pull-out, blind corner; along the right wall — induction hob with drawers and hood,
tall fridge in the niche; along the left wall below the chimney — tall column with
built-in oven and microwave; small island 100x50 near the passage in the foreground,
doors facing the viewer, two black bar stools. Materials per the client's reference
photo: handleless matte beige lower fronts, dark matte walnut upper cabinets and
tall column, graphite fridge column, light travertine-look worktops, dark stone
panel behind the hob, dark fluted wood panel on the island front facing the viewer,
black faucet and black granite sink, LED 3000K under the upper cabinet right of the
window.
STRICT: overlay furniture only — do not alter walls, window, chimney or viewpoint;
do not widen the room; island no larger than 100x50; nothing where there is no space
in the photo.
```

## 16. Wariant alternatywny (odrzucony, zachowany dla porównania)

**v3 „L + barek":** bez słupka S1 i wyspy — piekarnik pod płytą (D5), przy przejściu tylko barek 700×400 (przejście ~1040). Wybierany, gdyby pomiar wykazał, że przejście 740 jest w praktyce za ciasne albo komin okaże się czynny/ciepły (S1 odpada). Historia wariantów: v1–v2 (błędna orientacja, odrzucone), v3 (barek), **v4 (finalny — wyspa + słupek)**.

---

*Historia decyzji inwestora: „Kornel/Korner" = dostawca Korner Żary; przejście min. 70 cm zaakceptowane; piekarnik po stronie gzymsu; wyspa po lewej przy wejściu do salonu; zabudowa lewej strony do sufitu (S1).*
