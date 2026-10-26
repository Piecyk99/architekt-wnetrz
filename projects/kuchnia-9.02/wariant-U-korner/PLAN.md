# Kuchnia 9.02 — wariant U „Korner DIY" (alternatywa dla teczki Castorama)

> **Zlecenie inwestora (2026-10-26):** na podstawie teczki Castoramy nr `1556_DM_17_10_2026_2358451` (17.10.2026, projektant: salon Bytom) i rzutu mieszkania zrobić tę samą kuchnię do **samodzielnego wykonania z materiałów Korner (płyty, korner.pl)** — oddział Piekary Śląskie / KornerGo: wizualizacje, szafki, lista zakupów.
>
> **To NIE jest dokumentacja produkcyjna.** Lista formatek do cięcia powstanie dopiero po pomiarach kontrolnych z pkt 12 i w formacie e-Rozkroju KornerGo (`skills/zabudowa-na-wymiar/references/formatki.md`). Wartości `[~]` i `[?]` wymagają weryfikacji na miejscu.

Pliki w tym folderze:

| Plik | Co to jest |
|---|---|
| `model.py` | jedno źródło geometrii (mm) + automatyczne kontrole progów + szacunek materiałów; generuje `index.html` i `3d/model.json` |
| `index.html` | strona z interaktywnym modelem 3D (obrót, widoki, fronty on/off, numery szafek) + rozpiska i zakupy — artefakt |
| `technical/01–04` | rzut + elewacje D/A/B (SVG + PNG, generator `technical/gen.py`) |
| `renders/01–06` | widoki z modelu 3D (kadry jak w teczce Castoramy: od wejścia, od przejścia, z góry, korpusy bez frontów, okno, makieta z numerami) |
| `render.mjs` | eksport PNG (Playwright): `node render.mjs svg` / `node render.mjs 3d` |

Poprzedni wariant tej kuchni (v4 — L + słupek + wyspa): `../PLAN.md`. Obowiązują te same dane pomieszczenia i decyzje inwestora co do materiałów (orzech + beż/piasek + jasny kamień).

---

## 0. Analiza teczki Castoramy — co z niej bierzemy, co trzeba zmienić

**Zawartość teczki (15 stron):** 4 wizualizacje + widok z góry, lista zakupów 26 + 11 pozycji (**10 632,04 zł**, 426,76 kg), weryfikacja zawartości (AGD, zlew, bateria, oświetlenie — **nie** wycenione), strony informacyjne (akcesoria montażowe, łączenie blatów, punkty instalacyjne). **Brak rzutu z wymiarami** — „Pomiar dostarczył: Klient"; rysunki „mają charakter poglądowy i nie stanowią projektu wykonawczego" (s. 14).

**Rekonstrukcja układu z listy zakupów + wizualizacji:**

| Ściana | Castorama (GoodHome Caraway / Garcinia / Levanna) |
|---|---|
| D (lewa) | szuflady 60 (Soto 1 + 2 głębokie, antracyt) · piekarnikowa 60 + płyta · nad nimi 2 × wisząca wysoka 60 (orzech Levanna) z okapem podszafkowym · półki otwarte przy kominie |
| A (okno) | zlewowa 80 (2 × front 40) · zmywarka 45 (front 45) · listwy narożne 5,9 × 71,5 (2 szt.) |
| B (prawa) | narożna 100 (front 45 + panel maskujący) · cargo 15 (Pebre 150) · lodówka wolnostojąca · nad nimi 2 × wisząca wysoka 60 |
| Materiały | fronty dolne **sandstone mat**, górne **orzech włoski**, blat laminat **Neutral silk stone 38 × 620**, panel ścienny kompakt **Neutral silk stone/marble gold 3 mm × 3 szt.**, cokół sandstone 15 cm |

**Weryfikacja z rzutem 9.02 (2450 × 1910 [P], komin 370 × 630 [P] od podłogi do sufitu):**

| # | Problem w teczce | Matematyka | Rozwiązanie w wariancie U |
|---|---|---|---|
| 1 | Ściana z oknem się nie mieści | ciąg D (lico ~600) + listwa 59 + zlew 800 + zmywarka 450 + listwa 59 + ciąg B (~600) = **~2568 mm** > **2450 [P]** (bez listew narożnych: równe 2450 → drzwi kolidują) | zlew **750** + zmywarka 450 + blendy **44 / 50** między licami 578 ↔ 1872 = 1294 ✓ |
| 2 | Płyta grzewcza tuż przy kominie (wiz. 1–3, widok z góry) | próg ≥300 mm od ściany bocznej / wysokiej zabudowy | płyta **355** od komina i **323** od końca ciągu (D3 330 między kominem a płytą) |
| 3 | Komin w modelu tylko nad blatem (szafki dolne wchodzą w lewy narożnik) | komin 370 × 630 idzie do podłogi [P] | ciąg D zaczyna się za kominem (y = 650), narożnik zamknięty blendami 72 + 44, martwe pole pod blatem |
| 4 | Moduły tylko w szerokościach 15/40/60/80/100 | — | formatki Korner na wymiar: 300 / 330 / 600 / 750 / 1050 / 150 |
| 5 | 3 panele ścienne po 3 m | obwód nad blatem: A 2080 + komin 630 + 370 + D 1268 + B 1218 = **5,6 mb** | **2 panele** (A + lico komina; D + B + bok komina) |

**Uwaga do wariantu v4 (`../PLAN.md`), wykryta przy tej analizie:** w v4 lewe drzwi D1 (zlew, x 400–800) otwierają się w szczelinę ~30 mm przed bokiem słupka S1 (y = 630) — kolizja. Przy powrocie do v4: blenda ≥50 przy narożniku albo zlewowa z jednym frontem/szufladą.

---

## 1. Podsumowanie pomieszczenia

Kuchnia **9.02, 4,86 m²** (2450 × 1910 mm wewn. [P], wys. ~2490 [~]), remont. Wysokie okno ~920 × 810 do sufitu (parapet 1680 [~] na wylewce). **Komin 370 × 630 w lewym górnym narożniku** [P], od podłogi do sufitu. Krawędź C: otwarte przejście 1740 [P] (lewa część) + odcinek ściany 850 zewn. przy wnęce lodówki [P]. Podejścia wody pod oknem [P], 2 wypusty oświetleniowe [P], puszka elektryczna nisko na ścianie B [P]. Płyta indukcyjna — w projekcie brak gazu (ogrzewanie budynku elektryczne wg deklaracji inwestora; ewentualną instalację gazową w lokalu potwierdzić).

Orientacja: **patrzysz na okno**. A = z oknem, D = lewa (komin), B = prawa, C = krawędź od przejścia.

## 2. Znane wymiary `[P]`

| Wymiar | Wartość | Źródło |
|---|---|---|
| Ściana A wewn. / zewn. | 2450 / 2590 | rzut 9.02 |
| Głębokość (D i B) | 1910 | rzut |
| Komin wzdłuż D × w głąb | 630 × 370 | rzut |
| Ściana D poniżej komina | 1280 | rzut |
| Otwarte przejście (C) | 1740 | rzut |
| Odcinek ściany C przy lodówce | 850 (zewn.) | rzut |
| Lodówka | 600 × 600 × 2020 | deklaracja inwestora |

## 3. Wymiary do potwierdzenia `[~]` / `[?]`

| Wymiar | Wartość robocza | Podstawa | Dlaczego ważny |
|---|---|---|---|
| Wysokość pomieszczenia | 2490 [~] | 1680 + 810 | blenda do sufitu, wys. górnych 960 |
| Parapet | 1680 [~] | na wylewce | po posadzce −10…30 |
| Okno od komina / szer. / do B | 230 / 920 / 930 [~] | adnotacje na zdjęciu | półki R1 (220) muszą zmieścić się przed ościeżem |
| Wysokość blatu | 880 [~] | siatka 165–180 cm wzrostu | 860 / 910 zmienia tylko cokół |
| Kratka wentylacyjna | [?] | nie potwierdzona | okap z wyciągiem vs recyrkulacja |
| Pozycje podejść wody / odpływu | [?] | „pod oknem" | wycięcia w D4 |
| Czy komin czynny / ciepły | [?] | spalinowe nieużywane, wentylacyjne traktować jako czynne | mocowanie R1, płyta obok |

## 4. Przeszkody architektoniczne

| Element | Konsekwencja projektowa |
|---|---|
| **Komin 370 × 630, lewy górny róg** | ciąg D od y = 650 (blenda 20 [~]); w narożniku A/D martwe pole 208 × 578 + 52 × 208 pod blatem (blendy 72 + 44); na licu komina półki R1 (bez głębokiego wiercenia) |
| Okno do sufitu | brak szafek nad oknem; R1 kończy się 10 mm przed ościeżem (x 590 < 600) |
| Odcinek ściany C przy lodówce | lodówka 80 mm od ściany po stronie zawiasu (drzwi ≥90°) |
| Kratka wentylacyjna [?] | do potwierdzenia — do tego czasu okap recyrkulacyjny |
| Podejścia wodne pod oknem | zlew pod oknem (D4) |

## 5. Proponowany układ — **U (jak w teczce), przeliczony na wymiar**

Rzut: `technical/01-rzut-U.png`.

```
                    ściana A (okno 600–1520)
   ┌──────────┬─────┬══════════════════════┬───────────┬──────────┐
   │▓▓ KOMIN ▓│martw│  D4 ZLEW 750         │  ZM 450   │  narożnik│
   │▓ 370×630 ▓│pole │  (komora z prawej)  │           │  (D5)    │
   │▓▓▓▓▓▓▓▓▓▓├─────┴─BL2 44──────────────┴───BL3 50──┤──────────┤
 D ├──BL1 72──┤                                        │ D5 450   │ B
   │ D3  330  │        przejście 1294 ✓                │ (narożna │
   │ szuflady │                                        │  1050)   │
   ├──────────┤                                        ├──────────┤
   │ D2  600  │  ◄ piekarnik                           │ D6 150   │
   │ PŁYTA    │                                        ├─BW2──────┤
   ├──────────┤        lico D ↔ lodówka 1222 ✓         │ LODÓWKA  │
   │ D1  300  │                                        │ 60×60    │
   │ cargo    │                                        │ (zawias ↓)│
   └──BW1─────┘- - - - przejście 1740 - - - - - ┌──────┴──────────┘
                                                └─ ściana C 850
```

**Trójkąt roboczy** (zlew ↔ płyta ↔ lodówka): 1300 / 1521 / 1418 mm, suma **4239** ✓ (3600–7000, żaden bok <1200). **Przejście między ramionami U: 1294** ✓ (twardy próg ≥1200). Lico D ↔ front lodówki: **1222** ✓.

**Ciąg pracy (od prawej do lewej):** lodówka → blat roboczy B + narożnik + nad zmywarką (~1,1 m frontu blatu) → zlew → ociekacz / narożnik → płyta. Ciągły blat między zlewem a płytą jest krótki (narożnik + D3 ≈ 0,36 m²) — świadomy kompromis U w 4,9 m²; główne przygotowanie po prawej stronie zlewu.

### Warianty i ocena (krok 6–8)

| Kryterium | **A: U wg teczki, płyta na D (WYBRANY)** | B: U z płytą na ścianie B | C: v4 — L + słupek + wyspa (`../PLAN.md`) |
|---|---|---|---|
| Ergonomia | trójkąt 4239, wszystkie boki ≥1200 | **odrzucony:** płyta na B (y 600–1200) stoi 30 mm od lodówki (próg ≥300) albo nad narożnikiem, przed którym nie da się stanąć | dobra dla 1 osoby, AGD w słupku na wysokości oczu |
| Najwęższe przejście | 1222 (do lodówki) | — | ~740 (przy wyspie, zaakceptowane) |
| Przechowywanie | 6 dolnych + 5 górnych + R1 | — | więcej w słupku S1 |
| Wykonalność DIY | prosta: same szafki dolne/wiszące, 1 narożnik ślepy | — | trudniejsza: słupek do sufitu, wyspa, zabudowa komina |
| Zgodność z teczką | **pełna (układ, styl, funkcje)** | — | inny układ |
| Werdykt | **wybrany** — to jest kuchnia z teczki, poprawiona tak, żeby się zmieściła | odrzucony matematyką | alternatywa (pkt 15) |

## 6. Rozpisanie zabudowy ściana po ścianie (mm)

Wysokości: cokół **122** [~] · korpus **720** · blat **38** → blat **880** · panel ścienny 880–1480 · górne: korpus **960** (1480–2440), front **980** (podchwyt 20 mm w dół — zamiast uchwytu) · blenda do sufitu ~50 [~]. Głębokości: korpus dolny **560** + front 18 = lico **578**, blat **600**; górne **332** + 18 = **350**; półki R1 **220**.

**Ściana D (lewa) — patrząc na ścianę, od lewej (przejście) do prawej (komin):**
`BW1 18 | D1 cargo 300 | D2 piekarnik + płyta 600 | D3 szuflady 330 | blenda 20 [~] | KOMIN 630`
Góra: `BWG1 18 | G1 300 | G2 okapowa 600 | G3 330 | BLG1 20 | KOMIN` → `technical/02-elewacja-D.png`

**Ściana A (okno) — od lewej (komin) do prawej:**
`KOMIN 370 | martwe pole 208 | BL2 44 | D4 zlew 750 | ZM 450 | BL3 50 | narożnik (ciąg B) 578`
Góra: `R1 półki 220 na licu komina | OKNO (bez szafek) | ściana wolna | (G4 na ścianie B)` → `technical/03-elewacja-A.png`

**Ściana B (prawa) — od lewej (narożnik z A) do prawej (ściana C):**
`D5 narożna 1050 (zaślepka 600 + drzwi 450) | D6 cargo 150 | BW2 18 | szczelina 12 | LODÓWKA 600 | szczelina 80`
Góra: `BLG2 20 | G4 590 | G5 590 | BWG2 18` → `technical/04-elewacja-B.png`

## 7. Kolejność szafek

- D (od przejścia): BW1 → D1 → D2 → D3 → BL1 → komin
- A (od komina): R1 (góra) · BL2 → D4 → ZM → BL3 → narożnik
- B (od narożnika): D5 → D6 → BW2 → lodówka
- Górne: G1 → G2 → G3 (D) · R1 (komin) · G4 → G5 (B)

## 8. Moduły — szerokości orientacyjne

| Nr | Typ | Szer × Wys × Gł | Front | Wnętrze / okucia | Uwagi |
|---|---|---|---|---|---|
| D1 | cargo | 300 × 720 × 560 | 1 pełny | cargo 300 | oleje/przyprawy obok płyty |
| D2 | piekarnikowa | 600 × 720 × 560 | szuflada niska ~120 | piekarnik pod blatem, **nisza 560 × 590–600** (korpus 600 ≠ nisza 560) | płyta indukcyjna 60, wycięcie wg karty modelu [?] |
| D3 | szufladowa | 330 × 720 × 560 | 3 szuflady (~180/270/270) | 3 komplety prowadnic pełnego wysuwu | sztućce + garnki płytkie |
| BL1 | blenda narożna | 72 × 720 | piaskowy | — | **docinana na miejscu** (zamów z zapasem 100) |
| BW1 | bok wykończeniowy | 578 × 842 | piaskowy | — | od podłogi do blatu, od strony przejścia |
| BL2 | blenda narożna | 44 × 720 | piaskowy | — | docinana (zapas 80) |
| D4 | zlewowa | 750 × 720 × 560 | 2 drzwi 375 | kosz na segregację; **plecy serwisowe** | zlew 1-komorowy z ociekaczem, komora nad prawą częścią (bateria ~70 mm na prawo od osi okna) |
| ZM | zmywarka 45 | nisza 450 × 820+ | front 450 na drzwiach | — | **BD** bok dystansowy 18 × 560 × 842 (z płyty korpusowej) zamyka niszę od narożnika |
| BL3 | blenda | 50 × 720 | piaskowy | — | luz frontu zmywarki do lica ciągu B |
| D5 | narożna ślepa | 1050 × 720 × 560 | zaślepka 600 + drzwi 450 | 1 półka; opcjonalnie półkosz narożny pod drzwi 450 [DO WERYFIKACJI] | dostęp do martwego narożnika przez drzwi 450 |
| D6 | cargo wąskie | 150 × 720 × 560 | 1 pełny | cargo 150 | odpowiednik Pebre 150 z teczki |
| BW2 | bok wykończeniowy | 578 × 842 | piaskowy | — | przy lodówce |
| G1 | wisząca | 300 × 960 × 332 | drzwi 980 | 2 półki, 3 zawiasy | |
| G2 | okapowa | 600 × 960 × 332 | drzwi ~680 + front szuflady okapu ~300 | okap do zabudowy 60 (teleskopowy) | spód frontu okapu **580** nad płytą (≥550 ✓); recyrkulacja do potwierdzenia kratki |
| G3 | wisząca | 330 × 960 × 332 | drzwi 980 | 2 półki | przy kominie |
| R1 | półki otwarte | 630 × 960 × 220 | — | 2 boki + 5 półek (orzech) | rama skręcona; **wkręty do ściany A** (230 mm między kominem a oknem), w komin tylko **kotwy płytkie 40–50 mm bez udaru** (jak v4) |
| G4, G5 | wiszące | 590 × 960 × 332 | drzwi 980 | 2 półki, 3 zawiasy | ściana B od narożnika |
| BWG1/2, BLG1/2 | boki / blendy górne | 350 × 980 / 20 × 980 | orzech | — | blendy docinane |
| TOP | blendy do sufitu | ~50 [~] × długość ciągu | orzech | — | D, B i nad R1 |
| COK | cokół | 122 [~] × ~3,4 mb | piaskowy | klipsy na nóżki | cofnięty 40 za lico; przy zmywarce przycięty wg karty |

Moduły przy ścianach: **szerokości finalne po pomiarach** (blendy docinane).

## 9. Rozmieszczenie AGD

| Urządzenie | Pozycja | Korpus / nisza | Wymagania | Otwieranie |
|---|---|---|---|---|
| Płyta indukcyjna 60 | blat nad D2 | wycięcie wg karty (typowo 560 × 490) [?] | **puszka przyłączeniowa** pod blatem — parametry obwodu dobiera elektryk z tabliczki znamionowej | — |
| Piekarnik 60 | D2 pod blatem | korpus 600 / **nisza 560 × 590–600** | osobny obwód, przyłącze wg instrukcji modelu — dobiera elektryk | drzwi w dół, przed nimi 1294 ✓ |
| Zmywarka 45 do zabudowy | ZM | nisza 450 × 820+ | woda + odpływ z D4; **gniazdo w D4 lub D5** (nie za zmywarką) | front w dół — blokuje drzwi D5 tylko przy jednoczesnym otwarciu (narożnik = rzadko używany) |
| Okap do zabudowy 60 | G2 | wg karty montażowej | gniazdo w G2 nad okapem; recyrkulacja / wyciąg wg kratki [?] | szuflada okapu wysuwana |
| Lodówka wolnostojąca 60 × 60 × 202 | ściana B, y 1230–1830 | — | gniazdo osobny obwód — za lodówką wysoko lub w D6/D5 (dostęp bez odsuwania); 50 mm z tyłu | **zawias od ściany C**, drzwi otwierają się w stronę przejścia; blat odkładczy B obok ✓ |
| Zlew + bateria | D4 | 750 | ZW + CW + odpływ 50 (pod oknem [P]) | — |

## 10. Zalecenia instalacyjne (przed montażem)

1. **Elektryk:** wydzielone obwody dla płyty, piekarnika, zmywarki i lodówki — przekroje, zabezpieczenia i liczbę faz dobiera uprawniony elektryk na podstawie mocy z tabliczek znamionowych (projekt podaje tylko miejsca).
2. Gniazda nad blatem: 2 × nad D3 / narożnikiem (ściana D), 2 × nad D5 (ściana B); nie nad płytą i nie bliżej niż 600 od zlewu w poziomie (lub z klapką IP44). Na kominie bez puszek (zakaz głębokiego wiercenia).
3. Zasilanie LED: zasilacz w G1 lub G2, przewody za wieńcami górnych; LED pod G1–G3, G4–G5 i pod półką dolną R1 (~3 m, 3000K).
4. Zmywarka: zasilenie wody i odpływ przez D4 (zawory dostępne w D4).
5. Kratka wentylacyjna — potwierdzić; jeśli jest w zasięgu G2/komina → okap z wyciągiem (kanał w G2), inaczej recyrkulacja z filtrem węglowym. **Nie podłączać okapu do kanału grawitacyjnego bez zgody administracji / kominiarza.**
6. Wszystkie wysokości przemierzyć **po posadzce docelowej**.

## 11. Ryzyka

| Ryzyko | Prawdop. | Skutek | Mitygacja |
|---|---|---|---|
| Ściana A krótsza / krzywa na wys. blatu | średnie | brak miejsca na blendy 44/50 | pomiar na 0/880/2200; rezerwa: zlew 700 (blenda 94 → 44) |
| Komin nieprostopadły / 37 cm tylko na dole | średnie | blenda BL1 i R1 nie pasują | pomiar komina w 3 punktach; BL1 i boki R1 docinane |
| Komin ciepły przy G3/R1 | niskie | nagrzewanie frontów | sprawdzić w administracji; ew. szczelina 10 mm + ekran |
| Kolizja zmywarka ↔ drzwi D5 | pewne przy jednoczesnym otwarciu | niewygoda | D5 = przechowywanie rzadkie; świadomy kompromis |
| Kratka wentylacyjna w strefie zabudowy | nieznane | zakaz zabudowy | pomiar; kratka rewizyjna w blendzie TOP |
| Narożniki ≠ 90° | średnie | szczelina na łączeniu blatu | przekątne; łączenie blatu na miejscu, listwa/silikon |
| Dekor piaskowy / orzech niedostępny w Korner | średnie | zmiana koloru | próbki w oddziale przed zamówieniem; ew. inny dostawca [DO WERYFIKACJI] |
| Cięcie bez pomiarów | — | błędne formatki | **zakaz** — formatki dopiero po pkt 12 |

## 12. Pomiary kontrolne (przed e-Rozkrojem)

| # | Pomiar | Gdzie | Dlaczego krytyczny |
|---|---|---|---|
| 1 | Długość ściany A na wys. 0 / 880 / 2200 (najmniejszy wymiar) | A | blendy BL2/BL3, szer. D4 |
| 2 | Długość ścian D (od komina) i B na tych samych wys. | D, B | końce ciągów BW1/BW2, lodówka |
| 3 | Komin: 370 × 630 przy podłodze, na 880, przy suficie; czy czynny/ciepły | róg A/D | BL1, R1, G3 |
| 4 | Wysokość podłoga–sufit w 4 punktach **po posadzce** | cała kuchnia | blenda do sufitu, cokół |
| 5 | Przekątne narożników A/D i A/B | narożniki | łączenie blatu, D5 |
| 6 | Pion ścian (łata 2 m) | D, A, B | blendy, szczeliny |
| 7 | Poziom podłogi na linii cokołu | wszystkie ciągi | nóżki, cokół |
| 8 | Okno: odległość od komina, szerokość z ościeżami, parapet po posadzce, kierunek otwierania skrzydła | A | R1 (220 + 10), zlew |
| 9 | Podejścia wody, odpływ, zawory (wys., rozstaw) | pod oknem | wycięcia w D4, plecy serwisowe |
| 10 | Kratka wentylacyjna — pozycja, wymiar | góra ścian | okap, zakaz zabudowy |
| 11 | Puszki i gniazda (w tym niska na ścianie B) | wszystkie ściany | przeróbki przed montażem |
| 12 | Materiał ścian D i B pod szafki wiszące, ściany A pod R1 | D, B, A | dobór kotew |
| 13 | Nisze z kart montażowych kupionych AGD (piekarnik, zmywarka 45, okap, płyta) | — | D2, ZM, G2, wycięcia w blacie |
| 14 | Lodówka: realne wymiary + kierunek zawiasów (przekładalne?) | — | szczelina 80, BW2 |

**Projekt do weryfikacji pomiarem na miejscu przed produkcją mebli.**

## 13. Materiały i styl (wg teczki + decyzji inwestora z v4)

Dekory jako **intencja kolorystyczna** — kody dobrać w KornerGo / oddziale Piekary Śląskie z próbek (w ofercie m.in. Kronospan, Sonae Arauco, Pfleiderer, kolekcje Deep Matt, Time of Oak, Woodstories, Mood Stories, SKIN, Lombardo, PrimeBoard). **Nie podaję kodów z pamięci.**

| Element | Teczka Castoramy | Wariant Korner | Status |
|---|---|---|---|
| Fronty dolne, blendy, boki, cokół | Garcinia / Stevia **sandstone mat** | płyta frontowa **piaskowy beż mat** (supermat np. Deep Matt) + ABS 2 mm | dekor [DO WERYFIKACJI] |
| Uchwyty dolne | frezowane (bezuchwytowe) | **profil uchwytowy aluminiowy na górnej krawędzi frontu** (czarny/grafit) albo Tip-On; frez J w płycie wiórowej odpada (odsłoni rdzeń) | model [DO WERYFIKACJI] |
| Fronty górne, R1, blendy górne | Levanna **orzech włoski** | płyta drewnopodobna **orzech średni/ciemny, słoje pionowe** (Time of Oak / Woodstories) | dekor [DO WERYFIKACJI] |
| Uchwyty górne | push / bez uchwytów | **podchwyt 20 mm** (front niżej niż korpus) — zero okuć | ✓ |
| Korpusy | Caraway biały (dół) / szary (góra) | **jedna płyta korpusowa 18 mm biała lub kremowa** (prostsze zamówienie) | ✓ |
| Blat | laminat Neutral silk stone 38 × 620, 2 × 3 m | **laminat 38 × 600 jasny kamień**, 3 kawałki (2080 + 1298 + 618) | dekor [DO WERYFIKACJI] |
| Panel ścienny | kompakt Neutral silk stone/marble gold 3 mm × **3** | ten sam typ, **2 szt.** — jeśli Korner nie ma paneli ściennych, kup w Castoramie (568 zł/szt. wg teczki) | dostępność [DO WERYFIKACJI] |
| Szuflady | Soto antracyt | systemy szuflad Blum / GTV / Häfele (partnerzy Korner) | model [DO WERYFIKACJI] |
| Oświetlenie | brak w teczce | LED 3000K pod górnymi i R1 | — |

## 14. Lista zakupów

### 14a. Korner (płyty, korner.pl) — oddział Piekary Śląskie / KornerGo

Ilości z `model.py` (szacunek do budżetu, **nie formatki**):

| Pozycja | Ilość | Uwagi |
|---|---|---|
| Płyta korpusowa 18 mm biała/kremowa | **~4 arkusze** 2800 × 2070 (netto ~14,8 m² + 25% na rozkrój) | boki, wieńce, półki, bok BD |
| Płyta frontowa piaskowy mat 18 | **1–2 arkusze** (~3,7 m²) | 11 frontów + 3 blendy + 2 boki + cokół |
| Płyta frontowa orzech 18 | **~2 arkusze** (~4,3 m²) | 5 drzwi górnych + front szuflady okapu (słój pionowy — fronty 980 ustaw wzdłuż długości arkusza) + R1 + boki + blendy |
| HDF 3 mm biały | 1 arkusz (~4,6 m²) | plecy (D4 — plecy serwisowe) |
| Formatowanie + oklejanie ABS | ~120 mb (2 mm fronty i widoczne krawędzie, 1 mm ukryte) | krawędzie przy ścianie bez oklejania |
| Blat laminowany 38 mm, jasny kamień | 4,0 mb (1 × 4100 lub 2 × 3000) | + obrzeże na 2 końce, 2 komplety łączników blatu, wycięcia zlewu i płyty (CNC lub na miejscu) |
| Zawiasy z cichym domykiem 110° + prowadniki | **20** | D4 4 · D5 2 · G1 3 · G2 2 · G3 3 · G4 3 · G5 3 |
| Prowadnice / systemy szuflad | **4 kpl** | D3 × 3 (korpus 330), D2 × 1 |
| Cargo | 300 + 150 | D1, D6 |
| Profil uchwytowy (górna krawędź frontów dolnych) | ~4 mb | lub Tip-On |
| Nóżki regulowane 100–150 + klipsy cokołu | 26 + ~20 | |
| Zawieszki regulowane + szyna montażowa | 10 + ~2,5 m | G1–G5 |
| Złącza (konfirmaty / euro), kołki, zaślepki, kątowniki | kpl | |

Systemy cokołowe, profile blatowe, uszczelka cokołu — alternatywnie **Korner (podłogi i profile, korner.eu)**, zgodnie z `skills/architekt-wnetrz/references/dostawcy.md`.

### 14b. Poza Korner

| Pozycja | Gdzie | Uwagi |
|---|---|---|
| Panel ścienny 600 × 3000 × 2 | Castorama (jak w teczce) lub odpowiednik | jeśli brak w Korner |
| Płyta indukcyjna 60, piekarnik 60, zmywarka 45 do zabudowy, okap do zabudowy 60 | dowolny sklep AGD | teczka też ich nie zawiera; **nisze z kart montażowych przed e-Rozkrojem** |
| Zlew granit 1-komorowy z ociekaczem (~740 × 480), bateria, syfon, zawory kątowe | Castorama / Leroy / Allegro | zlew musi pasować do szafki 750 |
| LED 3000K: ~3 m profilu + taśma + zasilacz + włącznik | Allegro / Castorama | |
| Silikon sanitarny, listwa przyblatowa, kotwy do ścian | Castorama / Leroy | kotwy wg materiału ścian (pkt 12.12) |

### 14c. Koszt — porównanie (orientacyjnie)

| | Kwota | Co obejmuje |
|---|---|---|
| **Teczka Castoramy** | **10 632 zł** | meble + blat + 3 panele ścienne, bez AGD/zlewu/oświetlenia. Promocja „20% na kupon" do **3.11.2026** przy kuchni ≥10 000 zł (s. 14) — zwrot na kupon, nie rabat |
| Korner — ekonomicznie | **~5,5–7 tys. zł** | płyta laminowana, okucia budżetowe, panel ścienny z Castoramy (2 szt.) |
| Korner — standard | **~8–10 tys. zł** | Blum z domykiem, fronty supermat, lepsze cargo |

Kwoty Korner to **szacunek z cen rynkowych** (np. płyta 18 mm biała w Castoramie 37,98 zł/m² ≈ 220 zł/arkusz; blat 38 × 3000 — 398 zł i panel 568 zł wg teczki), **nie cennik Korner** — ten nie jest jeszcze w `korner-katalog.md`. Najwięcej zmieniają: dekor frontów (supermat vs zwykły laminat) i klasa okuć. Realna kwota = wycena e-Rozkroju po pomiarach. Główna przewaga wariantu Korner to **dopasowanie do 2,45 m** (zestaw z teczki się nie mieści) i swoboda szerokości, a nie gwarantowana oszczędność.

### 14d. Wiadomość do Korner (do skopiowania, po pomiarach)

```
Temat: Wycena formatek + frontów — kuchnia U 2,45 × 1,91 m (samodzielny montaż)

Dzień dobry,

proszę o wycenę rozkroju z oklejaniem i okuć do kuchni w układzie U (11 szafek dolnych/wiszących + półki otwarte):
- płyta korpusowa 18 mm biała/kremowa (~4 arkusze),
- płyta frontowa 18 mm w dekorze piaskowy beż mat (~1–2 arkusze) — proszę o propozycje dekorów supermat,
- płyta frontowa 18 mm orzech, słój pionowy (~2 arkusze) — proszę o dostępne dekory orzecha,
- HDF 3 mm biały (1 arkusz),
- oklejanie ABS 2 mm (fronty) / 1 mm (korpusy), ok. 120 mb,
- blat laminowany 38 mm jasny kamień, 4,0 mb, z wycięciem pod zlew i płytę (jeśli robicie),
- 20 zawiasów z cichym domykiem 110°, 4 komplety prowadnic szuflad, cargo 300 i 150, profil uchwytowy ~4 mb,
- nóżki 26 szt., zawieszki 10 szt., szyna 2,5 m.

Listę formatek prześlę przez e-Rozkrój po pomiarach. Pytanie: czy macie panele ścienne nad blat w dekorze blatu?

Dostawa: transport Korner / odbiór osobisty Piekary Śląskie.

Pozdrawiam,
<imię>
```

Lista gotowa do złożenia w Korner (płyty, korner.pl — oddział Piekary Śląskie lub KornerGo) **po pomiarach z pkt 12**.

## 15. Prompty do wizualizacji fotorealistycznej

Rendery `renders/01–06` są wierne geometrii (model 3D z `model.py`), ale nie są fotorealistyczne. Do fotorealizmu: **edycja renderu `renders/01-widok-od-wejscia.png` jako obrazu bazowego** (`gemini_edit_image` z `imagePath` albo dowolny model image-to-image) — zachowuje geometrię lepiej niż generacja od zera.

### 15a. Naniesienie materiałów na render (EN, edycja obrazu)

```
Using the attached render as the exact base: turn it into a photorealistic interior
photograph. Keep the camera position, perspective, every cabinet, the window, the
chimney pillar in the far-left corner and all proportions exactly as in the image.
Materials: lower cabinet fronts handleless matte sand-beige laminate with a thin
graphite edge-pull profile on top, upper cabinets and the open shelves on the chimney
in medium-dark walnut woodgrain with vertical grain, reaching the ceiling; light grey
stone-look laminate worktop 38 mm; light grey marble-look compact panel between
worktop and upper cabinets; black induction hob; built-in black oven under the hob;
anthracite granite sink with a black faucet under the window; freestanding graphite
fridge on the right; light oak floor. Warm 3000K LED strip under the upper cabinets,
soft daylight from the high window. Architectural Digest editorial aesthetic, no people.
STRICT: do not move or resize the window; do not remove the chimney pillar; do not add
cabinets, an island or appliances; do not change the room size or the viewpoint.
```

### 15b. Render od zera (EN)

```
Architectural interior photograph of a small U-shaped kitchen in a Polish apartment,
2.45 x 1.91 m, ceiling 2.49 m, open at the front to the hallway. High window (~92x81 cm)
on the far wall reaching the ceiling, sill at 168 cm, 60 cm from the left corner. A
floor-to-ceiling chimney pillar (37 x 63 cm) in the FAR-LEFT corner with open walnut
shelves on its face next to the window. Left run (in front of the chimney, left to right
as seen from the entrance): 30 cm pull-out, 60 cm oven under an induction hob with a
walnut hood cabinet above, 33 cm drawer unit. Far wall: 75 cm sink base with a granite
sink under the window, 45 cm integrated dishwasher. Right run: blind corner unit with a
45 cm door, 15 cm pull-out, then a freestanding graphite fridge 60 cm wide, 202 cm tall.
Upper cabinets on the left and right walls in walnut, 96 cm tall, up to the ceiling; no
cabinets above the window. Fronts: handleless matte sand-beige lower fronts, walnut uppers
with vertical grain, light grey stone worktop and backsplash panel, light oak floor, warm
3000K under-cabinet LED. Camera in the hallway at the open side, eye level 155 cm,
28 mm lens, looking at the window. No people. Architectural Digest editorial aesthetic.
STRICT CONSTRAINTS: do not move or resize the window; do not remove the chimney pillar;
do not enlarge the room; no island, no peninsula, no tall cabinets except the fridge;
nothing beyond the listed cabinets.
```

**Kontrola zgodności po wygenerowaniu** (`prompty-wizualizacyjne.md` §5): okno w tym samym miejscu · komin zachowany · płyta NIE przy kominie (między nimi szuflady) · zlew pod oknem, zmywarka po prawej · lodówka po prawej przy przejściu · brak wyspy. Render niezgodny nie trafia do dokumentacji.

## 16. Kontrola zgodności z materiałami źródłowymi (krok 11)

| Sprawdzenie | Wynik |
|---|---|
| Wymiary pomieszczenia jak w rzucie 9.02 (2450 × 1910, komin 370 × 630, przejście 1740, ściana C 850) | ✓ (`model.py`, `01-rzut-U`) |
| Okno 600–1520 nie zasłonięte, brak szafek nad oknem | ✓ (kontrola automatyczna) |
| Komin zachowany do podłogi, zabudowa kończy się blendami przed nim | ✓ |
| Układ, funkcje i materiały z teczki Castoramy | ✓ — z 4 świadomymi zmianami (pkt 0) |
| Twarde progi: przejście ≥1200, płyta ≥300 od ściany/końca, okap ≥550, lodówka ≥50 od ściany po stronie zawiasu | ✓ — wynik `python3 model.py` |
| Elementy niepotwierdzone (kratka, podejścia, wysokość) | oznaczone `[?]` / `[~]`, w pkt 12 |

---

*Historia: wariant U (2026-10-26) = przeniesienie teczki Castorama 1556_DM_17_10_2026_2358451 na rzut 9.02 do wykonania z płyt Korner (korner.pl). Wariant v4 (L + słupek + wyspa) pozostaje w `../PLAN.md` jako alternatywa.*
