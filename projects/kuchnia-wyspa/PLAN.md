# Kuchnia z wyspą — projekt zabudowy na wymiar (koncepcja v1)

Projekt wykonany skillem **architekt-kuchni** na podstawie: **zdjęcia pomieszczenia** (stan remontowy, wyspa wyklejona taśmą na wylewce, adnotacje „wyspa" / „indukcja" / „szafki") oraz **odręcznego rzutu z wymiarami** (adnotacje „wyspa" / „indukcja" / „zlew" / „okno", legenda `oo = woda`, `⊗ = odpływ`). Wykonanie: **samodzielne**, materiały: **Korner (płyty, korner.pl) — oddział Piekary Śląskie / KornerGo**.

> **To NIE jest dokumentacja produkcyjna.** Koncepcja v1 na danych częściowych — wszystkie wartości `[~]` i `[?]` wymagają weryfikacji pomiarem. Szerokości modułów są orientacyjne, do przeliczenia po pomiarach z pkt 12.

> **Relacja do `projects/kuchnia-9.02`:** geometria tego pomieszczenia (≈254,6 × ≈238,9+, okno na ścianie zlewu, brak gzymsu/komina w kadrze) **nie zgadza się** z kuchnią 9.02 (245 × 191, wysokie okno, gzyms 63×37). Traktuję to jako **inne pomieszczenie / nowy projekt**. Jeśli to ta sama kuchnia po zmianach ścian — patrz pytanie Q5; wtedy plan 9.02 v4 zostaje zarchiwizowany jako nieaktualny.

---

## 1. Analiza materiałów źródłowych

### Zdjęcie 1 — pomieszczenie (stan surowy)
- **Pozycja kamery:** z góry (z podestu/drabiny), od strony przejścia/korytarza, w stronę ściany z indukcją i narożnika z niszą.
- **Widoczne:** świeża wylewka; ściana z podtynkową puszką elektryczną (przyszła **indukcja** — prawdopodobnie wypust siłowy `[?]` do potwierdzenia); po prawej uskok ściany i nisza; wyklejony taśmą obrys **wyspy** na podłodze + poziomica wyznaczająca jej krawędź; przejście do pomieszczenia z ułożoną podłogą drewnianą (salon/korytarz) po lewej; stara kuchenka wolnostojąca (tymczasowa) po prawej; przewody elektryczne luzem przy podłodze.
- **Adnotacje na zdjęciu:** „Szafki" (niebieskie, na ścianie indukcji — szafki górne na tej ścianie), „59x52" ołówkiem na ścianie `[?]` — znaczenie nieznane.
- **Na podłodze:** czerwony znacznik przy ścianie indukcji `[?]`; metalowy krążek/zaślepka przy niszy `[?]` (odpływ? gaz? do identyfikacji).
- **Czego NIE widać:** ściana z oknem (za kadrem po prawej), ściana lodówki (za kamerą), sufit, kratka wentylacyjna.

### Zdjęcie 2 — odręczny rzut
- Fragment mieszkania: **łazienka** i **korytarz** po lewej, **wyjście** na dole; kuchnia w prawej części.
- Niebieskim markerem: obrys **wyspy** (prostopadłej do ściany indukcji, przy lewej krawędzi), ciąg wzdłuż ściany górnej (indukcja) i ciąg wzdłuż ściany prawej (**zlew**, na tej ścianie **okno**); u dołu prawego ciągu krótki „hak" w stronę ściany dolnej + znaki `xx` (wg legendy: woda + odpływ w tym rejonie `[~]`).
- Wymiary z rzutu: 254,6 · 238,9 · 195 · 127 · 67 · ~15,5 · 77.

### Kontrole krzyżowe (spójność szkicu)
| Kontrola | Wynik |
|---|---|
| 254,6 − 238,9 = 15,7 ≈ **15,5** (uskok w rejonie narożnika ścian A/B) | ✓ spójne |
| 127 + 67 = 194 ≈ **195** (podział ciągu ściany A: odcinek do uskoku + odcinek przy uskoku) | ✓ spójne — ale patrz sprzeczność S1 |

---

## 2. Model pomieszczenia

Orientacja w całym projekcie: **stoisz w wejściu od korytarza i patrzysz na ścianę z indukcją.**
Ściana **A** = z indukcją (góra rzutu) · ściana **B** = prawa, z oknem i zlewem · krawędź **C** = dolna (lodówka; częściowo otwarta — wejście) · lewa krawędź = otwarta na korytarz (za nią łazienka).

```
              ściana A — indukcja + szafki górne
    ┌─────┬──────────127──────────┬────67─────┐ ← uskok ~15,5 [~]
    │WYSPA│  ciąg dolny + górne   │ (narożnik │
    ├──┐  │  [indukcja + okap]    │  A/B)   ┌─┤
    │  │  └───────195─────────────┴─────────┘ │
    │W │                                  │zmyw│
    │Y │        aleja robocza             │ 45 │
    │S │         ~135 [~]                 ├────┤
    │P │                                  │zlew│═ okno [?pozycja]
    │A │ dł. ~127 [?]                     │    │   (zlew pod oknem)
    ├──┘                                  ├────┤ ściana B: 238,9 [P]
    │    przejście/wejście ~127 [~]       │    │
    │                                ┌────┴────┤
    │  ← otwarte (korytarz)          │ LODÓWKA │ ● woda+odpływ [~]
    └────────────────────────────────┴─────────┘
         ściana C — lodówka z zabudową od góry (nadstawką)
```

### Wymiary — statusy

| Wymiar | Wartość | Status | Źródło |
|---|---|---|---|
| Ściana B (okno/zlew) | 238,9 cm | `[P]` | rzut odręczny |
| Głębokość pomieszczenia po lewej (A↔C) | 254,6 cm | `[P]` | rzut odręczny |
| Ciąg ściany A: wyspa → ściana B | 195 cm | `[P]` | rzut odręczny |
| — w tym odcinek do uskoku / przy uskoku | 127 + 67 cm | `[~]` | rzut; patrz S1 |
| Uskok przy narożniku A/B | ~15,5 cm | `[~]` | rzut (potwierdzone różnicą 254,6−238,9) |
| Wymiar „77" | 77 cm | `[?]` | rzut — **nie wiadomo, czego dotyczy** (Q3) |
| Ściana A łącznie (z wyspą) / ściana C | ? | `[?]` | brak — do pomiaru |
| Wyspa: szerokość × długość | ? × ~127 | `[?]` | taśma na podłodze — do zmierzenia (S1/Q1) |
| Wysokość pomieszczenia | ? | `[?]` | brak |
| Okno na B: pozycja, szerokość, parapet | ? | `[?]` | brak — determinuje pozycję zlewu |
| „59x52" (napis na ścianie) | ? | `[?]` | zdjęcie — znaczenie nieznane (Q4) |

### Sprzeczności / niejednoznaczności

| # | Co | Wersja 1 | Wersja 2 | Przyjmuję | Potwierdzić |
|---|---|---|---|---|---|
| S1 | Znaczenie „127" | odcinek ciągu A między wyspą a uskokiem (127+67≈195 ✓) | długość wyspy w głąb pomieszczenia (proporcje szkicu też ~125) | **wersję 1** (kontrola sumy) — długość wyspy oznaczam osobno `[?]` | pomiar taśmy wyspy: szerokość i długość |
| S2 | Pozycja lodówki na C | przy narożniku B/C (niebieski „hak" na szkicu; „zaczyna się, gdzie kończą się szafki przeciwnej strony" = koniec ciągu przy ścianie B) | wyrównana z wyspą (lewy koniec ciągu A) | **wersję 1** — bezpieczniejsza komunikacyjnie (nie zwęża wejścia) | Q2 |
| S3 | Woda/odpływ | `xx` przy dolnym końcu ściany B (rejon narożnika B/C) | zlew ma być pod oknem (środek B?) | podejścia są nisko na B `[~]`, zlew pod oknem — **podejścia do przedłużenia w zabudowie** | pomiar pozycji podejść + okna |

---

## 3. Decyzje inwestora `[P]` (2026-08-11)

1. **Szafki górne TYLKO na ścianie A** (ściana wyspy i indukcji) **oraz zabudowa nad lodówką na C**. Na ścianie B (okno/zlew) — **żadnych górnych**.
2. **Zlew pod oknem** na ścianie B; **obok zlewu mała zmywarka** (przyjmuję 45 cm).
3. **Lodówka na ścianie C** (naprzeciw indukcji), z tzw. **zabudową od góry** (słupek/nadstawka nad lodówką).
4. **Wyspa** wg obrysu wyklejonego na podłodze — przy lewej krawędzi, prostopadle do ściany A (konstrukcyjnie: **półwysep**, jeśli dostawiona do ściany A — tak wygląda na szkicu i zdjęciu).
5. **Pełna kuchnia** — na tej przestrzeni ma się zmieścić wszystko, co potrzebne (przyjmuję: indukcja, piekarnik, okap, zlew, zmywarka 45, lodówka, przechowywanie).

## 4. Układ i ergonomia (matematyka przejść)

Układ: **L (A+B) + półwysep przy A + słupek lodówki na C** — funkcjonalnie zbliżony do U z otwartym narożnikiem wejściowym.

| Przejście | Wartość | Próg | Ocena |
|---|---|---|---|
| Aleja robocza: wyspa ↔ front ciągu B | ~135 `[~]` (195 − 60 głęb. zabudowy) | ≥100 twardy / 110–120 optimum | ✓ |
| Wyspa (koniec) ↔ ściana C / wejście | ~127 `[~]` (254,6 − ~127 dł. wyspy) | ≥90 komunikacyjne | ✓ |
| Przed otwartą zmywarką | ~135 `[~]` | ≥110 | ✓ |
| Przed lodówką (front ku pomieszczeniu) | ~120+ `[~]` | ≥100 | ✓ |

**Trójkąt roboczy:** lodówka (C, przy narożniku B/C) → zlew (B, pod oknem) → indukcja (A) — boki szacunkowo 1,3–2,2 m, suma ~4,5–5,5 m `[~]` — w normie 3,6–7,0 m, ciąg wejściowy nie przecina trójkąta. Sekwencja stref od wejścia: zapasy (lodówka) → zmywanie (zlew+zmywarka) → przygotowanie (blat B/narożnik) → gotowanie (indukcja) — poprawna.

**Uwaga krytyczna — bilans ściany B (238,9):** narożnik z A (~60 martwego pola) + zmywarka 45 + szafka zlewowa 80 + słupek lodówki na C (~65–70 głębokości wchodzące w światło B) = **~250–255 > 238,9**. Ciąg się **nie spina z zapasem** — do wyboru przy pomiarach: **(a)** szafka zlewowa **60** zamiast 80 (komora pojedyncza — rekomendacja przy małej kuchni), **(b)** zmywarka po drugiej stronie zlewu (bliżej narożnika nic poza martwym polem), **(c)** lodówka odsunięta od narożnika B/C (wariant S2/wersja 2). Decyzja po pomiarze ściany B i pozycji okna.

## 5. Rozpisanie zabudowy ściana po ścianie (koncepcja, mm)

**Ściana A — ciąg 1950 od wyspy do ściany B `[P]`, od lewej:**
`WYSPA/półwysep | D1 450 szuflady | D2 600 INDUKCJA (piekarnik pod płytą) | D3 narożna ślepa ~900 (front ~450, martwe pole w rogu z B)`
450+600+900 = 1950 ✓. Uskok ~155×670 przy prawym końcu: blat wchodzi głębiej w kieszeń lub blenda wyrównująca — do pomiaru.
**Górne na A (do sufitu `[?]` wys.):** `G1 450 | OKAP 600 (nad indukcją, w zabudowie) | G2 ~900` + LED 3000K pod spodem. Odstęp okap–indukcja ≥550.

**Ściana B — 2389 `[P]`, od narożnika z A:**
`martwe pole narożne ~600 (dostęp z D3) | D4 ZMYWARKA 450 | D5 ZLEW 600–800 (pod oknem, pozycja wg okna [?]) | dojście do słupka lodówki — patrz bilans wyżej`
Bez szafek górnych (okno) — decyzja inwestora. Blat na całej długości do zabudowy lodówki.

**Ściana C — od narożnika z B:**
`S1 SŁUPEK LODÓWKI ~650–700 (lodówka + nadstawka nad nią do sufitu, kratka wentylacyjna w cokole i nadstawce)` — reszta ściany C w stronę wejścia **wolna** (komunikacja).
Typ lodówki (do zabudowy 560×1780 nisza / wolnostojąca w obudowie) `[?]` — determinuje szerokość słupka i wentylację.

**WYSPA/półwysep — wymiar wg taśmy `[?]` (roboczo ~1270 × ~650):**
korpusy dolne otwierane od strony alei roboczej lub wejścia `[?]`, blat na wysokości ciągu (880 `[~]` — wzrost użytkownika `[?]`); bez instalacji wodnych; ewentualne **gniazdo w wyspie wymaga doprowadzenia w podłodze — decyzja PRZED posadzką docelową**.

## 6. Rozmieszczenie AGD

| Urządzenie | Pozycja | Nisza / wymagania |
|---|---|---|
| Płyta indukcyjna | D2 (ściana A) | wycięcie blatu 560×490 (4-pol.); wypust siłowy — puszka na ścianie A widoczna na zdjęciu `[?]` potwierdzić 32A |
| Piekarnik | pod płytą w D2 | nisza 560×590–600; osobny obwód 16A; alternatywa: słupek na C obok lodówki — patrz Q2 |
| Okap | nad D2, w G (zabudowany) | ≥550 od indukcji; **recyrkulacja do czasu potwierdzenia kratki wentylacyjnej `[?]`** |
| Zmywarka 45 | D4, obok zlewu | światło wnęki 450×820+; woda+odpływ z D5 |
| Zlew + bateria | D5, pod oknem | podejścia obecnie nisko na B `[~]` — przedłużyć w zabudowie; zlew nie nad zmywarką |
| Lodówka | S1 na C, przy narożniku B/C | otwieranie ≥90° (zawiasy od strony ściany B → blenda dystansowa ≥50); wentylacja 50 tył+góra |

## 7. Zalecenia instalacyjne (PRZED montażem)

1. Potwierdzić charakter puszki na ścianie A (siła 32A dla indukcji); osobny obwód 16A piekarnik; gniazda: zmywarka, lodówka, 2–3 nad blatem A (≥600 od zlewu w poziomie).
2. Zasilanie LED podszafkowego na A (transformator w górnej).
3. Ewentualne gniazdo w wyspie — **decyzja przed wylewką/posadzką docelową**.
4. Zlokalizować kratkę wentylacyjną `[?]` — od tego zależy okap (wyrzut vs recyrkulacja).
5. Podejścia wody/odpływu: potwierdzić pozycję (szkic sugeruje nisko na B przy narożniku z C) i zaplanować przedłużenie do D5 w cokole/za korpusami.
6. Zidentyfikować krążek/zaślepkę w podłodze przy niszy `[?]` (gaz? odpływ?) — nie zabudowywać na głucho.

## 8. Ryzyka

| Ryzyko | Mitygacja |
|---|---|
| Bilans ściany B nie spina się (narożnik+45+80+lodówka > 238,9) | wybór wariantu (a)/(b)/(c) z pkt 4 po pomiarach; zlew 600 zamiast 800 |
| Interpretacja „127" błędna (S1) | zmierzyć taśmę wyspy przed rozpisaniem finalnym |
| Pozycja okna wymusi przesunięcie zlewu | pomiar okna przed rozstawem D4/D5 |
| Uskok 15,5×67 inny niż na szkicu | pomiar w 3 wysokościach; blenda docinana |
| Zawiasy lodówki przy ścianie B | blenda dystansowa 50–70 |
| Posadzka docelowa zmieni wysokości | wymiary pionowe po posadzce |

## 9. Lista pomiarów kontrolnych dla stolarza

1. Ściana A łącznie (z odcinkiem wyspy) i ściana C — dołem i na wys. blatu.
2. Ściana B: 238,9 — kontrola dołem/górą; przekątne narożnika A/B (kąt).
3. Uskok przy A/B: głębokość i długość na 3 wysokościach.
4. **Taśma wyspy: szerokość × długość + odległość od ściany A** (rozstrzyga S1).
5. Okno na B: pozycja od narożników, szerokość, wysokość parapetu (blat pod oknem?).
6. Wysokość podłoga–sufit w 4 punktach **po posadzce docelowej**.
7. Podejścia wody/odpływu: pozycja, wysokości; identyfikacja zaślepki w podłodze.
8. Kratka wentylacyjna: pozycja i wymiar.
9. Puszka elektryczna na A: obwód (32A?); pozycje pozostałych punktów.
10. Światło wejścia do kuchni od korytarza; wyjaśnić wymiar „77" i napis „59x52".

**Projekt musi zostać zweryfikowany pomiarem na miejscu przed produkcją/cięciem mebli.**

## 10. Materiały i styl — propozycja (do akceptacji)

Kontynuacja palety zaakceptowanej w projekcie kuchni 9.02 (jeśli to ten sam inwestor/mieszkanie): fronty dolne beż/kaszmir mat bezuchwytowe, górne + słupek lodówki ciemny orzech mat (intencja „Orzech Royal"), blat jasny trawertyn laminat 38 mm, front wyspy od strony wejścia panel ryflowany ciemny, bateria+zlew czarne, LED 3000K. **Kody dekorów do doboru z aktualnej oferty Korner (płyty, korner.pl) `[DO WERYFIKACJI]`** — bez kodów z pamięci. Alternatywnie: nowa paleta wg inspiracji inwestora.

## 11. Prompt — realistyczna wizualizacja (EN; zaktualizować po pomiarach)

```
Architectural interior photograph of a compact open kitchen in a Polish apartment,
roughly 2.6 x 2.5 m, open on the left to a corridor. Far wall: base cabinets with
an induction hob and built-in oven below, upper cabinets with an integrated hood
above, under-cabinet LED 3000K. A peninsula (~127 x 65 cm, worktop 88 cm) attached
to the far wall at its left end, extending toward the viewer. Right wall: a window
mid-wall with a single-bowl black granite sink below it and a slim 45 cm dishwasher
beside it — NO upper cabinets on this wall. Near-right corner: a tall fridge column
with cabinet above it reaching the ceiling. Handleless matte beige/cashmere lower
fronts, dark matte walnut upper cabinets and fridge column, light travertine-look
laminate worktop, dark fluted wood panel on the peninsula front facing the viewer,
black matte faucet. Fresh renovation, warm daylight from the window. Camera at the
corridor entry, eye level 160 cm, 24 mm lens. No people. Architectural Digest
editorial aesthetic.
STRICT CONSTRAINTS: no upper cabinets on the window wall; do not enlarge the room;
peninsula size as stated; keep the wall recess near the far-right corner; nothing
beyond the listed cabinets.
```

## 12. Prompt — naniesienie na zdjęcie (EN, `gemini_edit_image`; referencja: zdjęcie 1)

```
Using the attached photo of the room under renovation as the exact base: render the
designed kitchen into this room, keeping the camera position, walls, wall recess,
floor and the doorway exactly as photographed. Along the far wall (labeled area):
base cabinets with induction hob and oven, upper cabinets with integrated hood.
Build the peninsula exactly on the taped outline on the floor. Right side: sink run
under the window with a 45 cm dishwasher, no upper cabinets. Near-right: tall fridge
column with top cabinet. Materials: handleless matte beige lower fronts, dark matte
walnut uppers and fridge column, light travertine-look worktop, dark fluted panel
on the peninsula front, black faucet, LED 3000K under uppers.
STRICT: overlay furniture only — do not alter walls, openings or viewpoint; the
peninsula must match the taped outline; no cabinets on the window wall above the
worktop.
```

---

## Pytania krytyczne (Q1–Q5)

1. **Q1 — wyspa:** jaką ma mieć szerokość i długość (wymiar taśmy z podłogi)? Czy dostawiona do ściany A (półwysep), czy wolnostojąca ze szczeliną?
2. **Q2 — lodówka:** przy narożniku B/C (jak przyjąłem), czy wyrównana z wyspą? Lodówka do zabudowy czy wolnostojąca w obudowie? Piekarnik pod indukcją (jak przyjąłem) czy w słupku obok lodówki?
3. **Q3 — wymiar „77" na szkicu:** czego dotyczy (szerokość wejścia? odcinek zabudowy?)?
4. **Q4 — „59x52" na ścianie:** co oznacza?
5. **Q5 — czy to ta sama kuchnia co projekt 9.02** (po zmianach ścian), czy inne mieszkanie? Jeśli ta sama — archiwizuję plan 9.02 v4. Czy paleta materiałów z 9.02 (pkt 10) zostaje?
