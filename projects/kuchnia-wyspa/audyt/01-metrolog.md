# 01 — METROLOG · audyt niezależny projektu `kuchnia-wyspa` v3.12a

**Data:** 2026-08-13 · **Zakres:** wyłącznie liczby (sumy biegów, narożniki, głębokości, pionowe, blaty, fronty, luzy).
**Metoda:** każdy wymiar czytany z pliku źródłowego, nie z pamięci. Brak wymiaru w dokumencie ⇒ `[BRAK DANYCH]`, bez interpolacji.
**Jednostka raportu:** mm (dokument miesza cm i mm — przeliczenia jawne).
**Zasada rozstrzygania:** rozjazd między PLAN.md / `_formatki.py` / `_kontrola.py` traktuję jako BŁĄD niezależnie od tego, która wartość jest „prawdziwa" — projekt nie ma jednego źródła prawdy, mimo że `references/protokol-weryfikacji.md` §1 tego wymaga.

---

## 0. Inwentaryzacja wczytanych plików

| Plik | Rozmiar | Linii | Mtime | Rola |
|---|---|---|---|---|
| `projects/kuchnia-wyspa/PLAN.md` | 32 690 B | 265 | 2026-08-13 08:46 | dokumentacja główna, v3.12a |
| `projects/kuchnia-wyspa/FORMATKI-ROBOCZE.md` | 11 847 B | 146 | 2026-08-13 08:46 | rozpiska formatek (wygenerowana) |
| `projects/kuchnia-wyspa/_formatki.py` | 10 393 B | 146 | 2026-08-13 08:46 | generator formatek — lista `MODULES` |
| `projects/kuchnia-wyspa/_kontrola.py` | 16 032 B | 393 | 2026-08-13 08:41 | model geometryczny + kontrole K1–K9 |
| `projects/kuchnia-wyspa/_schemat.py` | 17 232 B | 322 | 2026-08-13 09:44 | generator rzutu + 4 elewacji |
| `skills/zabudowa-na-wymiar/SKILL.md` | — | 112 | — | reguły twarde (okap ≥550, płyta ≥300 od zabudowy) |
| `skills/zabudowa-na-wymiar/references/protokol-weryfikacji.md` | — | 85 | 2026-08-13 08:43 | protokół (jedno źródło prawdy, K1–K9) |
| `skills/zabudowa-na-wymiar/references/technologia-wykonania.md` | — | 78 | — | luzy montażowe 20–50, fuga sufit 10–30 |
| `skills/zabudowa-na-wymiar/references/formatki.md` | — | 63 | — | metoda formatek ZABLOKOWANA |
| `skills/architekt-wnetrz/references/standardy-meble.md` | — | 186 | — | korpus 720 / cokół 100 / blat 600–630 / tolerancje |
| `skills/zabudowa-na-wymiar/references/{analiza-pomieszczenia, dokumentacja-stolarz, uklady-kuchni, prompty-wizualizacyjne, zabudowy-inne}.md` | — | 107/79/74/93/60 | — | przejrzane, bez wpływu na liczby |

**Uruchomienie kontrolne:** `python3 _kontrola.py --regresja` → `PASS — 9 kontroli, 0 błędów, 0 uwag` oraz `5/5 historycznych błędów wykrytych`.
**Uwaga metrologiczna:** PASS dotyczy wyłącznie modelu zapisanego w `_kontrola.py`. Model ten **nie jest zgodny** z PLAN.md ani z `_formatki.py` w 8 wymiarach (patrz §3). PASS nie jest więc dowodem poprawności projektu — jest dowodem wewnętrznej spójności jednego z trzech rozjeżdżonych zapisów.

**Plik `v1.md` nie istnieje w repo** — potwierdzone `ls`. Zakres N1–N6 zastąpiony orzeczeniami E1–E6 wg §9.

---

## 1. Tabela główna

Legenda kategorii: **BŁĄD** = sprzeczność wewnątrz dokumentacji lub z regułą twardą · **RYZYKO** = liczba domyka się, ale bez zapasu / na niepewnej podstawie · **BRAK** = pozycja wymagana, nieobecna · **ZGODNE** = sprawdzone, bez uwag.

| ID | moduł / wielkość | wymiar w dokumencie | wymiar wyliczony | delta mm | kategoria | werdykt |
|---|---|---|---|---|---|---|
| M01 | ciąg A — suma modułów dolnych | 1950 `[P]` | 610+240+600+500 = 1950 | 0 | ZGODNE | domyka się |
| M02 | ciąg A — „fronty dolne dostępne tylko **670→1450 = 780**" (PLAN §5 nagłówek) | 780 | front DA1 610→850 + DA2 850→1450 = **840** | +60 | BŁĄD | ogon v3.9: nagłówek nie przeliczony po przebudowie DA1 (v3.10) |
| M03 | górne A — suma | 1950 | 670+180+600+500 = 1950 | 0 | ZGODNE | zgodne w PLAN, `_formatki`, `_kontrola`, `_schemat` |
| M04 | ciąg B — suma vs ściana B | 2389 `[P]` | 445+150+800+450+546 = **2391** | +2 | RYZYKO | model `_kontrola` liczy bieg 155→2546 = 2391 |
| M05 | ściana B — łańcuch okna | 2389 `[P]` | 597+856+947 = **2400** | **+11** | BŁĄD | PLAN pkt 2 oznacza to „✓"; protokół §4 zabrania zaokrąglania niedomkniętego łańcucha |
| M06 | ciąg C wg PLAN §5 (korpus DC1 945 + blenda 47) | 1885 `[P]` | 945+47+280+660 = **1932** | **+47** | BŁĄD | blenda 47 pochodzi z wersji z korpusem 900; po v3.11 (945) nie skasowana |
| M07 | ciąg C wg `_formatki.py` (DC1 900 + blenda 47) | 1885 | 900+47+280+660 = 1887 | +2 | RYZYKO | to wariant opisany w PLAN §9 („947+280+660 ≈ 1887 vs 1885") |
| M08 | ciąg C **z blendą dystansową lodówki** (wymóg PLAN §9 + SKILL.md l.75) | 1885 | 945+280+660+**70** = **1955** | **+70** | BŁĄD | blenda dystansowa nie ma miejsca w biegu — `_kontrola` daje C3 zakres 1225→1885, styk ze ścianką |
| M09 | górne C — suma | 947 `[P]` | 470+477 = 947 | 0 | ZGODNE | — |
| M10 | ramię — lico wg PLAN §5 / `_kontrola` | 1176 | blenda ślepa 576 + drzwi 300 + szuflady 300 = 1176 | 0 | ZGODNE | K7 domyka |
| M11 | ramię — lico wg FORMATKI-ROBOCZE | 1176 | front 446 + blenda ślepa 430 = **876** | **−300** | BŁĄD | w rozpisce brak 300 mm lica = brak frontów szuflad (ogon E5) |
| M12 | ramię — długość, PLAN §5 (nagłówek, wiersz „blat ramienia", wiersz „panel ryflowany") | **~1180**×500 ×3 wystąpienia | korpus RL1 = **1176** (PLAN, `_formatki`, `_kontrola`) | +4 | BŁĄD | ogon E6 nieusunięty w 3 miejscach PLAN.md |
| M13 | przejście ramię ↔ ścianka liczone od **blatu** | 600 `[P]` reguła nadrzędna | 1776 − (635+545) = 1776−1180 = **596** | −4 | BŁĄD | blat definiuje realny prześwit; K6 mierzy korpus (1176), nie blat |
| M14 | ciąg A — lico strefy DA1 wg FORMATKI | 850 | blenda 610 + front 446 + blenda ślepa 430 = **1486** | **+636** | BŁĄD | generator wystawia hardkodowany front 446 dla każdej „narożnej" |
| M15 | DC1 — szerokość frontu | **345** (PLAN §5, §5a, `_kontrola` front (600,945)) | **450** (`_formatki.py` l.20 „front 450"), **446** (FORMATKI), **45 cm** (`_schemat.py` l.280) | +101…+105 | BŁĄD | ogon E4 — poprawka nie zeszła do rozkroju ani do rysunku |
| M16 | DC1 — szerokość korpusu | **945** (PLAN, `_kontrola`) | **900** (`_formatki.py`, FORMATKI dno 864 = 900−36) | −45 | BŁĄD | rozjazd trzech źródeł |
| M17 | DC1 — głębokość korpusu | **546** (PLAN, `_kontrola` x 2000→2546) | **560** (`_formatki`), **600** (`_schemat` `rect(CX-60,0,60,94.7)`) | +14 / +54 | BŁĄD | cztery pliki, trzy wartości |
| M18 | ciąg B — głębokość korpusów | **560** (PLAN §5 założenia + wiersze DB0/DB1, FORMATKI boki 560×720) | **600** (`_kontrola` l.60–65 „głębokość 600", `_schemat` segsB, PLAN §4 „195−60−50") | +40 | BŁĄD | z tej wartości wyliczono front DA1 = 240 i „zapas 13 mm" |
| M19 | DA2 — głębokość na rzucie | 560 (PLAN, `_formatki`, `_kontrola`) | `_schemat.py` l.167 `rect(0,85,60,60)` = **600** | +40 | BŁĄD | na rzucie lico DA2 (600) i DA1 (560) tworzą nieistniejący uskok 40 |
| M20 | C2 / C3 / C4 — głębokość | **580** (PLAN §5, `_formatki`) | **600** (`_kontrola` x 1946→2546), **700** (`_schemat` `rect(CX-70,…,70,…)`) | +20 / +120 | BŁĄD | od tej liczby zależy „zmywarka wcina się ~54" (2000−1946); przy 580 wychodzi 34 |
| M21 | RL1 — głębokość korpusu | **460** (PLAN §5, `_formatki.py`) | **500** (`_kontrola` y 1450→1950, `_schemat` ARM_D) | +40 | BŁĄD | 460 + front 19 + panel 19 = 498 ≈ blat 500 — układ prawdopodobny, ale nigdzie nie zapisany |
| M22 | blat — głębokość ciągów | **600** (PLAN §5 założenia: „blat 600") | **635** (`_formatki.py` BLATY: A, B, C1) | +35 | BŁĄD | 635 wykracza też poza standard 600–630 (standardy-meble.md) |
| M23 | blat ramienia — głębokość | **650** (PLAN §5 założenia: „ramię 650") | **500** (PLAN pkt 2 `[P]`, PLAN §5 wiersz blatu, `_formatki` 545×500, `_schemat` ARM_D) | −150 | BŁĄD | ogon sprzed v3.5 (decyzja „ramię gł. 50 `[P]`") |
| M24 | wystawka blatu przed lico frontu, ciąg A | norma 20–40 | 635 − 560 (korpus) − 19 (front) = **56** | +16…+36 | BŁĄD | przy blacie 600 wychodzi 21 ✓ — potwierdza, że 635 jest wartością błędną |
| M25 | cofnięcie górnych od lica blatu (PLAN §11a) | **181** | blat 635 − (400+19) = **216** | +35 | BŁĄD | 181 = 600−419, czyli §11a liczone na blacie 600, a rozpiska ma 635 |
| M26 | korpusy dolne — wysokość | **820** (PLAN §5 tabele: DA1, DA2, RL1, DB0, DB1, DC1 — 6 wystąpień „×820×") | **720** (PLAN §5 założenia „korpusy dolne 720", `_formatki.py` H=720, FORMATKI boki ×720) | +100 | BŁĄD | 820+150+38 = **1008 ≠ 910**; nawet jako „korpus+cokół" 820 ≠ 720+150 = 870 |
| M27 | wysokość blatu | **910** `[P]` | cokół 150 + korpus 720 + blat 38 = **908** | −2 | RYZYKO | do wyzerowania nóżką (regulacja 100–150); PLAN sam podaje ten łańcuch w pkt 2 |
| M28 | odstęp blat → dolna krawędź górnych | „**600**" (PLAN §6) | 1480 − 910 = **570** | −30 | BŁĄD | 570 mieści się w normie 500–600 ✓, ale liczba w dokumencie jest fałszywa |
| M29 | pasmo górnych | dół 1480, korpus 998, sufit 2478 | 1480 + 998 = 2478 | 0 | ZGODNE | domyka się **co do zera** — patrz M30 |
| M30 | fuga montażowa pod sufitem | technologia-wykonania §2: **10–30 + listwa** | **0** — korpus 998 dochodzi wprost do 2478 | −10…−30 | BRAK | brak fugi i brak formatki blendy górnej (M43) |
| M31 | C2 słupek — wysokość całkowita | korpus **2378** (PLAN §5, FORMATKI bok 580×2378), „do sufitu 2478" | 2378 + cokół 150 = **2528** | **+50** | BŁĄD | 2378 = 2478 − **100**, czyli słupek zakłada cokół 100, a dolne 150 → uskok linii cokołu |
| M32 | C4 nadstawka — wysokość | **528** (PLAN §5: „od ~1950 do 2478"; FORMATKI bok 580×528) | `_schemat.py` l.296 `rect(122.7,0,65.8,H−192)` = **558** (spód 1920) | +30 | BŁĄD | rysunek daje wentylację 20 mm zamiast wymaganych 50 |
| M33 | DA2 — stos pionowy (indukcja + piekarnik + szuflada) | mieści się w korpusie 720 | 910 − 38 (blat) − 18 (indukcja poniżej blatu: 56−38) − 590 (nisza) − 110 (front szuflady) − 150 (cokół) = **4** | 4 mm zapasu | RYZYKO | przy niszy 600 (górna granica „590–600") wychodzi **−6 mm — nie mieści się** |
| M34 | DA2 — pozycja szuflady | „**górna** szuflada płytsza (płyta 5,6)" (PLAN §5) | „**dolna**, płytsza" (PLAN §5a); „szuflada **pod piekarnikiem**" (FORMATKI okucia); „front szuflady **dolnej**" (`_formatki.py`) | — | BŁĄD | sprzeczność 1:3 wewnątrz PLAN.md |
| M35 | lodówka — luz boczny | „luzy **20–30 bok**" (PLAN §7) | światło C4/C3 = 660 − 2×18 = 624; 624 − 600 = **24 łącznie = 12/bok** | −16…−36 | BŁĄD | żeby dotrzymać 20–30/bok korpus musi mieć 676–696, nie 660 |
| M36 | okap — przypisanie do modułu | **GA3** (PLAN §5, §5a, `_kontrola` OKAP, `_schemat` elew. A) | **GA2** (PLAN §7 tabela AGD, wiersz „Okap \| GA2") | — | BŁĄD | ogon E1 — GA2 to szafka 180 na przyprawy |
| M37 | GA1 — półki | korpus gł. **245** | FORMATKI: „GA1 górna — półki 633×**300**" | +55 | BŁĄD | `_formatki.py` l.76 hardkoduje 300 dla każdej górnej — półka nie wejdzie do korpusu 245 |
| M38 | blenda dolna A przy pilastrze — wysokość | fronty dolne **716** (FORMATKI) | FORMATKI: „Blenda dolna A … 610×**756**" (`_formatki.py` PANELE) | +40 | BŁĄD | 756 = 910−150−4, czyli liczone bez korpusu 720; wchodzi w blat |
| M39 | panel ryflowany ramienia — wysokość | **910** (FORMATKI, PLAN §5) | lico pod blatem = 910 − 38 = **872** | +38 | RYZYKO | 910 tylko jeśli panel zachodzi na czoło blatu — nigdzie nie napisane |
| M40 | DB0 cargo 150 — front | wymagany ~146×716 | **brak w rozpisce** (typ `"cargo"` w `_formatki.py` nie generuje frontu) | — | BRAK | cargo bez frontu = szafka bez lica |
| M41 | RL1 — 3 fronty szuflad + front drzwi 300 | wymagane 4 fronty | **brak w rozpisce** (jest tylko front 446 + blenda 430) | — | BRAK | ogon E5 — funkcja jest w planie i w K9, nie ma jej w cięciu |
| M42 | GA3 — front antresoli nad okapem | PLAN §5a: „nad nim antresola na rzeczy sezonowe" | FORMATKI ma tylko „front uchylny 596×**400**"; korpus 998 → **~590 lica bez frontu** | −590 | BRAK | — |
| M43 | blenda górna pod sufit | FORMATKI §4 pkt 7: „blenda górna docinana do sufitu"; PLAN §12 to samo | **brak formatki**, brak wymiaru, brak miejsca (M30) | — | BRAK | — |
| M44 | nóżki meblowe | „32 + 16 szt \| **8 szafek dolnych** ×4" | dolnych korpusów jest **6** (DA1, DA2, RL1, DB0, DB1, DC1; DB2 to wnęka). Wg standardy-meble (6 nóżek ≥800): 6+4+6+4+6+6 = **32** + słupek C2 4 = **36** | +4 | BŁĄD | uzasadnienie („8 szafek") fałszywe; wynik i tak za mały o 4 |
| M45 | zawieszki górnych | „10 szt \| **GA1-3, GC1-2**" | górnych jest **6** (GA1, GA2, GA3, GA4, GC1, GC2) × 2 = **12** | +2 | BŁĄD | **GA4 pominięta** w wyliczeniu okuć |
| M46 | zawiasy puszkowe | „36 szt … w tym zapas ~10%" | DA1 2 + RL1 2 + DB1 4 + DC1 2 + GA1 6 + GA2 3 + GA4 3 + GC1 3 + GC2 3 + C2 6 + C4 4 = **38** | −2 | RYZYKO | zapasu nie ma, jest niedobór |
| M47 | listwa cokołowa | „łącznie ~**5 mb**" (5000×150) | ciąg A 1450 + ramię (N 1176 + E 500) + ciąg B 1986 + ciąg C 1885 = **6997** | **−2000** | BŁĄD | nawet bez ramienia (A+B+C = 5321) 5 mb nie starcza |
| M48 | blaty — nakładki w narożnikach | „Łączenia blatów: **3**" (czyli elementy rozłączne) | narożnik A/B: blat A (x 0–635) ∩ blat B = 480×635; narożnik B/C1: ∩ = 635×635 → nadmiar **478 + 635 = 1113 mm** długości | +1113 | RYZYKO | dla ramienia odjęto zakładkę (545 = 1180−635), dla B i C1 nie — metoda niekonsekwentna |
| M49 | blat ramienia — długość | **545** (FORMATKI) | 1176 − 635 = **541** | +4 | BŁĄD | to jest fizyczna przyczyna przejścia 596 (M13) |
| M50 | blat B — długość | **2389** | bieg 155→2546 = **2391** | −2 | RYZYKO | blat 2 mm krótszy od biegu (przed odjęciem zakładki z M48) |
| M51 | linia południowa — kontrola krzyżowa | „195 ≈ 188,5+9" (PLAN pkt 2, oznaczone ✓) | 1950 vs **1975** | 25 | RYZYKO | 25 mm oznaczone jako ✓; ścianka `[~]`, więc kontrola i tak nierozstrzygająca |
| M52 | szerokość A↔C — kontrola krzyżowa | 2546 `[P]` („238,9+15,5 = 254,4 ✓") | 2389 + 155 = **2544** | −2 | RYZYKO | 2 mm; `_kontrola` przyjmuje 2546 jako twarde, więc ściana B rośnie do 2391 (M04) |
| M53 | GC2 — „front w linii słupka C2" (PLAN §5) | lico wspólne | słupek gł. 580 → lico x=1966; górna gł. 400 → lico x=**2146** | 180 | BŁĄD | fizycznie niewykonalne bez pogłębienia GC1/GC2 do 580 |
| M54 | trójkąt roboczy | „boki ~1,3–1,8 m, suma ~**4,5 m**" (PLAN §4) | lodówka(2256,1555)–zlew(1150,300)–indukcja(280,1150): **1673 / 1216 / 2017**, suma **4906** | +406 | RYZYKO | suma nadal w normie 3600–7000 ✓, ale podane widełki boków (1,3–1,8) są nieprawdziwe |
| M55 | DA1 — „248 l **użytecznej** przestrzeni" (PLAN v3.10, §5, §5a) | 248 l | netto (814 × 387 × 684) = **215 l**; 248 l = 850×405×720 brutto po obrysie | −33 l | BŁĄD | liczba brutto sprzedana jako użyteczna; to samo dotyczy „~202 l" i „~236 l" |
| M56 | ramię — szerokość części ślepej | **560** (PLAN §5a „martwe pole ~560", `_formatki.py` uwagi RL1) | **576** (`_kontrola` front (576,1176) → blenda (0,576)) | 16 | BŁĄD | rozjazd 2 źródeł; z 560 wychodzi front 616, nie 600 |
| M57 | RL1 — „dostępna szerokość 118−60 = **58**" (PLAN §5 wiersz RL1) | 580 | 1176 − 576 = **600** (drzwi 300 + szuflady 300) | +20 | BŁĄD | ogon E2 — opis nie przeliczony po v3.11/v3.12 |
| M58 | ramię na rzucie — podział lica | front 600 / ślepe 576 | `_schemat.py` l.172–174: ślepe **0→600**, front **600→1176 = 576** | odwrócone | BŁĄD | na rzucie w front 576 nie zmieszczą się drzwi 300 + szuflady 300 |
| M59 | kosz segregacji — realne światło (K9) | K9 czyta front DB1 = **800** ≥ 450 ✓ | DB1 ma **2 drzwi po 397** (FORMATKI) → światło jednego skrzydła **397** | −53 | RYZYKO | K9 mierzy szerokość modułu, nie szerokość otwarcia — luka w samej kontroli |
| M60 | pilaster 155×670 — status wymiaru | `[P]` (PLAN pkt 2) | `[~]` (PLAN §1, §3 rzut), `[?]` (PLAN pkt 11.11: „sam rzut tego nie rozstrzyga") | — | BŁĄD | GA1 = 400−155 = 245 wisi na wymiarze o trzech różnych statusach |
| M61 | prompt wizualizacyjny (PLAN §13) | ramię `~118×**65**` | ramię gł. **500** `[P]` od v3.5 | +150 | BŁĄD | ogon sprzed v3.5 |
| M62 | prompt wizualizacyjny (PLAN §13) | „doorway to **bedroom** (127)" | otwór prowadzi do **SALONU** (v3.3a) | — | BŁĄD | ogon jawnie skasowany w v3.3a |
| M63 | pustka za DA1 na odcinku y 670→850 | — | 155 × 180 (korpus 405 gł. od lica pilastra, ściana cofnięta o 155) | — | BRAK | narysowana w `_schemat.py` l.131, nieopisana w PLAN.md i bez formatki wypełniającej |
| M64 | luz montażowy przy ścianie — ciąg C | technologia §2: **20–50 na styk** | 945+280+660 = 1885 = **całość biegu, luz 0** | −20…−50 | BRAK | jedyny bufor to blenda 47, która już jest zajęta przez M06 |
| M65 | luz montażowy — górne A i górne C | 20–50 | A: 670+180+600+500 = 1950 (luz 0) · C: 470+477 = 947 (luz 0) | −20…−50 | BRAK | zabudowa górna od ściany do ściany bez ani jednej blendy docinanej |
| M66 | transport formatek | PLAN §12: „formatki **2,4 m**" | bok lodówki **2478**, blenda dystansowa **2478** | +78 | RYZYKO | dwie formatki ponad deklarowany limit |
| M67 | C2 — podział frontu | komentarz `_formatki.py` l.27: „1300+**1074**" | kod i FORMATKI: 1300 + **1070** | 4 | RYZYKO | rozjazd komentarz/kod w tym samym pliku |
| M68 | „**RL2**" w planie montażu | FORMATKI §4 pkt 6 + `_formatki.py` l.137: „Ramię: **RL1+RL2** skręcone" | RL2 skasowany w v3.8 | — | BŁĄD | ogon E2 |
| M69 | „**DA4**" w opisie blatu ramienia | `_schemat.py` l.318: „blat ciągły z DA4" | moduły ciągu A to DA1, DA2 | — | BŁĄD | moduł nieistniejący |
| M70 | wiersz „**KOLIZJA `[?]`**" w PLAN §5 (ramię) | „27 z 60 cm frontu DA2 zasłonięte … Do rozstrzygnięcia przez inwestora" | PLAN §9a: „ROZWIĄZANA wariantem A `[P]`" | — | BŁĄD | ogon E2 — dwa wzajemnie sprzeczne wiersze w tym samym dokumencie |
| M71 | wiersz ryzyka „**Gzyms/podciąg pod sufitem**" (PLAN §9) | „koliduje z pasmem górnych 1480–2478 … warianty A/B/C, szczegóły w pkt 11a" | v3.7 odwołała gzyms; pkt 11a mówi już tylko o pilastrze i głębokości 400 | — | BŁĄD | ogon E3 |
| M72 | wymiar **947** — podwójne użycie | „Wnęka okienna → ściana C = 94,7" (odcinek ściany B, oś **x**) | ten sam 947 użyty jako długość biegu C i blatu C1 (oś **y**) | — | RYZYKO | dwa prostopadłe wymiary o tej samej wartości bez niezależnego pomiaru; pkt 11.3 tego nie rozdziela |
| M73 | indukcja — odstęp od końca biegu | SKILL.md l.74: płyta ≥300 od zabudowy bocznej | płyta 864→1436, ramię od 1450 → **14** | — | RYZYKO | formalnie nie „ściana boczna" ani „wysoka zabudowa", ale 14 mm od krawędzi blatu roboczego |

**Bilans:** BŁĄD **44** · RYZYKO **16** · BRAK **8** · ZGODNE **5** · razem **73** pozycje. Do tego **7 pozycji ULEPSZENIE** (§11) i **27 pozycji `[BRAK DANYCH]`** (§10).

---

## 2. Arytmetyka jawna — per bieg

### 2.1 Ciąg A (indukcja), oś y od ściany B, długość 1950 `[P]`
```
blenda przy pilastrze   610   (0 → 610)      lico ślepej części DA1
DA1 front               240   (610 → 850)    korpus 850 (0 → 850), gł. 405
DA2 indukcja+piekarnik  600   (850 → 1450)   gł. 560
ślepy narożnik          500   (1450 → 1950)  bez frontu, pod blatem ramienia
                        ----
610 + 240 + 600 + 500 = 1950  vs  ciąg A 1950  ->  0 mm   ✓
```
Kontrola frontów: 610→1450 = **840** dostępnego lica. PLAN §5 nagłówek deklaruje **780** („670→1450") → **+60 mm** (M02).
Kontrola wg rozpiski formatek: 610 (blenda) + 446 (front DA1) + 430 (blenda ślepa) = **1486** na strefę o licu 850 → **+636 mm** (M14).

### 2.2 Górne A, oś y, długość 1950
```
GA1 670 (0→670, gł. 245, na licu pilastra 155+245=400)
GA2 180 (670→850, gł. 400)
GA3 600 (850→1450, gł. 400)  okap
GA4 500 (1450→1950, gł. 400)
670 + 180 + 600 + 500 = 1950  vs  1950  ->  0 mm   ✓
```
Okap vs płyta: GA3 850→1450, środek **1150**; płyta 864→1436 (572 = Bosch PXE601DC1E), środek **1150** → wyśrodkowana, delta **0** ✓.
Luz montażowy w tym biegu: **0** (M65).

### 2.3 Ciąg B (okno), oś x od lica pilastra 155 do ściany C 2546
```
blenda / martwe pole    445   (155 → 600)    strefa przejęta przez korpus DA1
DB0 cargo               150   (600 → 750)
DB1 zlew                800   (750 → 1550)
DB2 zmywarka            450   (1550 → 2000)
martwe pole narożnika C 546   (2000 → 2546)  obsługiwane od DC1
                        ----
445 + 150 + 800 + 450 + 546 = 2391  vs  ściana B 2389 [P]  ->  +2 mm
```
Źródło +2: model przyjmuje `SCIANA_C_X = 2546` i pilaster 155 → 2546−155 = 2391, podczas gdy pomiar to 2389 (2546−2389 = **157**, nie 155).
Elewacja B w `_schemat.py` zamyka to inaczej: 445+150+800+450+**544** = 2389 → martwe pole 544, a PLAN mówi 546 (delta 2).

**Łańcuch okna (osobno):** 597 + 856 + 947 = **2400** vs 2389 → **+11 mm** (M05).
Konsekwencja pozycyjna: okno z lewego łańcucha = 752→1608; z prawego = (2546−947−856)=743→1599. **Niepewność pozycji okna ±9 mm** — a od niej zależy centrowanie zlewu (DB1 750→1550, środek 1150 vs środek okna 1180 → **przesunięcie 30 mm**).

### 2.4 Ciąg C (lodówka), oś y od narożnika z B do ścianki 1885 `[P]`
```
wariant PLAN §5:      945 (DC1) + 47 (blenda) + 280 (C2) + 660 (C3) = 1932   -> +47 mm
wariant _formatki:    900 (DC1) + 47 (blenda) + 280 (C2) + 660 (C3) = 1887   -> +2 mm
wariant _kontrola:    945 + 280 + 660                                = 1885   ->  0 mm  (bez blendy)
wariant z blendą dystansową lodówki (PLAN §9, SKILL l.75):
                      945 + 280 + 660 + 70                           = 1955   -> +70 mm
```
Blenda 47 jest dopełnieniem korpusu **900** do 947. Po korekcie korpusu na 945 (v3.11) nikt jej nie skasował → PLAN.md zawiera obie wersje jednocześnie (M06/M16).
Blenda dystansowa 70×2478 figuruje w rozpisce okuć i jest wymuszona geometrią (ścianka wysięg 770 > lico zabudowy 700), a w łańcuchu C **nie ma dla niej miejsca** (M08).

### 2.5 Górne C, oś y
```
GC1 470 + GC2 477 = 947  vs  bieg C1 947  ->  0 mm   ✓   (luz montażowy 0)
```

### 2.6 Ramię L, oś x od ściany A
```
wg PLAN §5 / _kontrola:  blenda ślepa 576 + drzwi 300 + szuflady 300 = 1176  ->  0 mm  ✓
wg _schemat.py:          ślepe 600 + front 576                       = 1176  ->  podział ODWRÓCONY (M58)
wg FORMATKI:             front 446 + blenda ślepa 430                =  876  -> -300 mm (M11)
wg PLAN §5a/_formatki:   martwe pole 560 -> front 1176-560 = 616, nie 600     (M56, 16 mm)
```
**Przejście:**
```
korpus:  1776 (czubek ścianki) − 1176 (RL1)          = 600   ✓  próg [P] spełniony (K6)
blat:    1776 − (635 blat A + 545 blat ramienia)     = 596   ✗  −4 mm  (M13/M49)
wg PLAN §5 nagłówek (ramię ~1180): 1776 − 1180       = 596   ✗  (M12)
```
To jest dokładnie błąd E6, wciąż obecny w blacie i w trzech miejscach PLAN.md.

---

## 3. Narożniki — czy przestrzeń liczona dwa razy

| Narożnik | Kto przejmuje | Ile realnie zabiera sąsiedni bieg | Martwe / ślepe pole | Ocena |
|---|---|---|---|---|
| **A/B (przy pilastrze)** | korpus DA1 (850×405), sięga do ściany B | ciąg B traci **445 mm** lica (155→600), zamknięte blendą | ślepa część DA1 = 610×405 (bez frontu); **+ nieopisana pustka 155×180 za korpusem** (M63) | brak podwójnego liczenia w rzucie (K2 PASS), ale PLAN opisuje strefę raz jako „narożnik zachodni ~600 od ściany A", a `_kontrola` daje blendę 155→600 = 445 — **dwie liczby na tę samą strefę** |
| **A/ramię** | RL1 (1176×460/500) | ciąg A traci **500 mm** lica (1450→1950) | ślepy narożnik 500 × 576 (lub 560) | **ta sama bryła opisana dwa razy**: jako wiersz ciągu A („ślepy narożnik 1450→1950 × 560, bez frontu") i jako część ślepa RL1 (0→576). K2 tego nie łapie, bo pierwszy zapis nie jest obiektem `Modul`. Rozjazd szerokości 560 vs 576 (M56) |
| **B/C** | korpus DC1 (945×546) | ciąg B traci **546 mm** lica (2000→2546); zmywarka wcina się w strefę C o **54** (2000−1946) lub **34** (przy gł. 580 → 1966) | martwe pole ~546×600 = „~236 l" (brutto) | „54" wyliczone z głębokości 600, a PLAN deklaruje 580 (M20) |
| **A/B — blaty** | — | blat A (635) ∩ blat B = **480×635** | — | **podwójne liczenie materiału 478 mm** (M48) |
| **B/C1 — blaty** | — | blat B (635) ∩ blat C1 = **635×635** | — | **podwójne liczenie materiału 635 mm** (M48) |
| **A/ramię — blaty** | — | zakładka odjęta poprawnie (545 = 1180−635) | — | jedyny narożnik blatowy policzony konsekwentnie — ale od złej długości ramienia (1180) |

Wniosek: klasa błędu E2 („narożnik liczony dwa razy") **została usunięta z korpusów, ale przetrwała w blatach** — i nikt jej tam nie kontroluje (K2 działa tylko na listach `CIAG_*` i `RAMIE`, blaty nie są w modelu).

---

## 4. Głębokości — konfrontacja trzech (czterech) źródeł

| Element | PLAN.md | `_formatki.py` | `_kontrola.py` | `_schemat.py` | werdykt |
|---|---|---|---|---|---|
| DA1 | 405 | 405 | 405 (x 155→560) | 405 | ✓ zgodne |
| DA2 | 560 | 560 | 560 (x 0→560) | **600** | BŁĄD (M19) |
| RL1 (ramię) | **460** | **460** | **500** (y 1450→1950) | **500** | BŁĄD (M21) |
| DB0 / DB1 (ciąg B) | **560** | **560** | **600** (y 0→600) | **600** | BŁĄD (M18) |
| DB2 zmywarka | światło 450×820+ | front 446×713 | 450 (x 1550→2000) | 450 | ✓ |
| DC1 | **546** | **560** | **546** (x 2000→2546) | **600** | BŁĄD (M17) |
| C2 / C3 / C4 | **580** | **580** | **600** (x 1946→2546) | **700** | BŁĄD (M20) |
| GA1 | 245 | 245 | 245 (x 155→400) | 245 (etykieta) | ✓ zgodne — jedyna głębokość spójna po korekcie |
| GA2/GA3/GA4/GC1/GC2 | 400 | 400 | 400 | 400 | ✓ |
| blat ciągów | **600** (§5) / brak w tabelach | **635** | brak (blaty poza modelem) | brak | BŁĄD (M22) |
| blat ramienia | **650** (§5 założenia) / **500** (pkt 2, §5 wiersz) | **500** | brak | 500 (ARM_D) | BŁĄD (M23) |
| słupek C2 | 580 | 580 | 600 | 700 | BŁĄD |

**Sześć z jedenastu głębokości ma co najmniej dwie różne wartości w repo.** Wymóg protokołu §1 („muszą się zgadzać co do milimetra") niespełniony.

Skutki wtórne, które już weszły do wniosków projektowych:
- front DA1 = **240** i „zapas 13 mm" wyliczono na ciągu B o głębokości **600** (odległość zawias(560,850) → korpus DB0 = √(40²+250²) = **253,2**; 253,2 − 240 = 13,2). Przy zadeklarowanych **560** dystans rośnie do √(40²+290²) = **292,7** → front mógłby mieć ~280. Wniosek „cargo narożne nie wejdzie" i tak zostaje w mocy (280 < 450), ale sama liczba 240 jest wyliczona z wymiaru, którego dokument nie deklaruje.
- „strefa przy zlewie ~85" (PLAN §4) = 1950 − **600** − 500. Przy głębokości 560 wychodzi **890**, przy uwzględnieniu frontu 19 — **871**. Deklarowane 850 nie odpowiada żadnej wersji dokumentu.
- „zmywarka wcina się ~54" — z głębokości 600 dla C2/C3. Przy 580 → 34.

---

## 5. Pionowe

```
cokół 150 + korpus 720 + blat 38 = 908   vs  wysokość blatu 910 [P]   ->  -2 mm   (M27)
```
Nóżki 150 mają regulację 100–150, więc 2 mm jest do wybrania — ale dokument podaje ten łańcuch jako domknięty (PLAN pkt 2: „korpus 720 + blat 38 + cokół ~150").

```
PLAN §5 tabele modułów dolnych:  wys. 820  ->  820 + 150 + 38 = 1008   vs 910   ->  +98 mm   (M26)
                                             820 vs 720+150 = 870      ->  -50 mm
```
Sześć wierszy PLAN §5 (DA1, DA2, RL1, DB0, DB1, DC1) niesie wysokość **820** — wartość ze standardu „korpus 720 + cokół **100**". Projekt ma cokół **150**. Żadne odczytanie 820 nie domyka się z blatem 910.

```
dół górnych 1480 - blat 910 = 570        deklarowane w PLAN §6: "odstęp 600"      ->  -30 mm  (M28)
                                          norma standardy-meble: 500-600           ->  ✓
okap 1480 - płyta 910 = 570              wymóg SKILL: >=550 od indukcji            ->  ✓ (+20)
górne: 1480 + 998 = 2478                 sufit 2478 [P]                            ->  0, ale fuga 0 (M30)
słupek C2: 2378 + cokół 150 = 2528       sufit 2478                                ->  +50 mm  (M31)
                                          2378 + 100 = 2478  ->  słupek zakłada cokół 100
nadstawka C4: 1950 + 528 = 2478          ✓  (lodówka 1900 + wentylacja 50 = 1950 ✓)
_schemat C4: spód 1920, wys. 558         wentylacja 20 zamiast 50                  ->  +30 mm  (M32)
parapet: 2478 - 817 = 1661               PLAN ~1661                                ->  0  ✓
fartuch: 1661 - 910 = 751                PLAN "~750"                               ->  ✓
```

**Stos w DA2** (jedyne miejsce, gdzie pion jest naprawdę ciasny):
```
910 (blat) - 38 (grubość blatu) = 872         spód blatu
872 - 18 (indukcja 56 poniżej blatu: 56-38) = 854
854 - 590 (nisza piekarnika, dolna granica) = 264
264 - 110 (front szuflady) = 154              vs  góra cokołu 150  ->  zapas 4 mm
przy niszy 600 (górna granica "590-600"):     ->  -6 mm, NIE MIEŚCI SIĘ
```

---

## 6. Blaty

| Blat | W dokumencie | Bieg do pokrycia | Delta | Uwaga |
|---|---|---|---|---|
| Blat A | 1950 × **635** | ciąg A 1950 | 0 dł. / +35 gł. | głębokość sprzeczna z PLAN §5 („blat 600") i z normą 600–630 |
| Blat B | 2389 × 635 | bieg 155→2546 = 2391 | −2 dł. | nie odjęto zakładki narożnika A/B (480) → przy pełnej długości nadmiar +478 |
| Blat C1 | 947 × 635 | bieg C1 947 | 0 | nie odjęto zakładki narożnika B/C1 (635) → nadmiar +635 |
| Blat ramienia | 545 × 500 | 1176 − 635 = **541** | **+4** | daje przejście **596** zamiast 600 |
| **Suma** | 1950+2389+947+545 = **5831** | — | — | nadmiar zakładek **1113 mm**, niedobór na ramieniu **−4 mm** |

**Wystawka przed lico frontu:**
- ciąg A/B: 635 − 560 − 19 = **56** (norma 20–40) → BŁĄD; przy blacie 600: 600−560−19 = **21** ✓
- ciąg C (DC1 546): 635 − 546 − 19 = **70** → BŁĄD; przy 600: **35** ✓
- ramię: 500 − 460 − 19 (front) − 19 (panel) = **2** → wystawka praktycznie zerowa, blat licuje z panelem

**Łączenia:** 3 zadeklarowane (A/B, B/C1, A/ramię) — zgodne z geometrią.
**Wycięcia:** indukcja 560×490 `[P]` w blacie A ✓ spójne w PLAN pkt 2, §5, §7, FORMATKI, `_schemat`. Pozycja wycięcia w głąb blatu — `[BRAK DANYCH]`. Zlew — „wg szablonu", brak wymiaru.
**Dylatacje blatu od ściany (3–5 mm, technologia §2):** nie przewidziane w żadnym z czterech blatów — długości są równe biegom co do milimetra.

---

## 7. Fronty vs korpusy vs szczeliny (rozpiska formatek)

Generator `_formatki.py` liczy fronty z korpusu: pojedyncze `S−4`, podwójne `(S−6)//2`, wysokość dolnych **716** (korpus 720), górnych **996** (korpus 998).

| Moduł | Korpus | Front(y) w rozpisce | Kontrola | Werdykt |
|---|---|---|---|---|
| DB1 zlew 800 | 800 | 2 × 397×716 | 397·2+6 = 800 ✓ | ✓ fuga 2 mm zgodna z tabelą tolerancji |
| GA1 670 | 670 | 2 × 332×996 | 332·2+6 = 670 ✓ | ✓ |
| GA2 180 / GA4 500 / GC1 470 / GC2 477 | j.w. | 176 / 496 / 466 / 473 × 996 | S−4 ✓ | ✓ |
| C4 660 | 660 | 2 × 327×524 | 327·2+6 = 660 ✓; 524 = 528−4 ✓ | ✓ |
| C2 280 | 280×2378 | 276×1300 + 276×1070 | 1300+1070 = 2370 vs 2378 → 8 mm na 3 fugi ✓ | ✓ (komentarz w kodzie mówi 1074 — M67) |
| DB2 zmywarka | wnęka 450 | 446×713 | ✓ zgodne z kartą 45 cm | ✓ |
| DA2 | 600 | front szuflady 596×110 | ✓ szerokość; wysokość patrz M33 | ~ |
| **DA1** | **850, front ma mieć 240** | **446×716 + blenda ślepa 430×716** | 446+430 = 876 ≠ 850; z blendą 610 razem 1486 vs 850 | **BŁĄD** |
| **RL1** | **1176, front 600 = drzwi 300 + 3 szuflady 300** | **446×716 + blenda 430×716** | brak 4 frontów; 876 vs 1176 | **BŁĄD + BRAK** |
| **DC1** | **945, front ma mieć 345** | **446×716 + blenda 430×716** | front o 101 za szeroki; blenda o 170 za wąska (ma być ~600) | **BŁĄD** |
| **DB0 cargo 150** | 150 | **brak frontu** | wymagany 146×716 | **BRAK** |
| **GA3 okap** | 600×998 | front uchylny 596×400 | ~590 lica antresoli bez frontu | **BRAK** |
| **GA1 półki** | gł. 245 | 633×**300** | półka głębsza od korpusu o 55 | **BŁĄD** |
| **blenda dolna A** | strefa 610 | 610×**756** | fronty w tym samym pasie mają 716 | **BŁĄD** |

Przyczyna trzech ostatnich wierszy „narożnych": w `_formatki.py` gałąź `if typ == "narozna"` (l. 69–71) wystawia **stałe** 446×716 i 430×716 dla DA1, RL1 i DC1 — niezależnie od faktycznej szerokości frontu (240 / 600 / 345) i szerokości korpusu (850 / 1176 / 945). To jeden defekt generatora, który unieważnia rozpiskę dla wszystkich trzech szafek narożnych, czyli dla **całej strefy, w której projekt naprawiał błędy v3.10–v3.12**.

Wysokości frontów szuflad (RL1 ×3, DA2, DC1 ×2): `[BRAK DANYCH]` — poza „górna RL1 niska (H≈86)".

---

## 8. Luzy montażowe i zapas na nierówności

Wymóg: technologia-wykonania §2 — szczelina 20–50 mm przy każdej ścianie, „światło zabudowy = wymiar ściany − 40–60 mm łącznie na blendy"; do sufitu fuga 10–30 mm; standardy-meble — fuga do ściany 5–15 mm.

| Bieg | Zaprojektowany luz | Element docinany | Ocena |
|---|---|---|---|
| Ciąg A (dolne) | **0** — 610+240+600+500 = 1950 dokładnie | blenda 610 przy pilastrze (docinana) | ~ akceptowalne: blenda absorbuje błąd na zachodnim końcu |
| Ciąg B (dolne) | **0** — 445+150+800+450+546 = 2391 | blenda 445 na zachodzie | ~ absorpcja tylko po jednej stronie; wschodni koniec (DC1 do ściany C) na styk |
| Ciąg C (dolne) | **0** — 945+280+660 = 1885 | blenda 47 (już zużyta arytmetycznie, M06) | **BRAK** — plus brak miejsca na blendę dystansową 70 (M08) |
| Ramię | n/d (wolnostojące) | docinane na montażu wg reguły 60 | ✓ jedyny bieg z jawną regułą docinania |
| Górne A | **0** — 670+180+600+500 = 1950 | brak | **BRAK** |
| Górne C | **0** — 470+477 = 947 | brak | **BRAK** |
| Pion — sufit | **0** — 1480+998 = 2478 | „blenda górna" wymieniona w montażu, brak formatki | **BRAK** (M30, M43) |
| Blaty | **0** — długości = długości biegów | „docinany na miejscu" (adnotacja) | ~ deklaracja bez wymiaru zapasu; brak dylatacji 3–5 mm |

Zapas na nierówności ścian jest **przewidziany wyłącznie w ciągach dolnych A i B**. W ciągu C, w obu pasmach górnych i pod sufitem projekt zakłada ściany i sufit idealne — wprost wbrew własnej regule „nie zakładaj, że ściana ma tę samą długość na każdej wysokości".

Do policzenia jako ryzyko materiałowe: przy typowej odchyłce 5–15 mm/2 m ściana B (2389) może dać ±15–20 mm, a przy zerowym luzie ciąg B nie wejdzie. PLAN pkt 11 przewiduje pomiary łańcuchowe — ale rozpiska nie ma gdzie tej korekty przyjąć.

---

## 9. Orzeczenia E1–E6

### E1 — v3.6: okap wpisany nad szuflady zamiast nad płytę
**POPRAWIONE CZĘŚCIOWO.**
Poprawne i spójne w czterech miejscach: PLAN §5 („GA3 okap … nad DA2 = 850→1450, wyśrodkowany nad indukcją `[P]`"), PLAN §5a („GA3 okap 60"), `_formatki.py` l.23, `_kontrola.py` (`OKAP = "GA3 okap"`, K4 PASS), `_schemat.py` elew. A `(85, 60, "GA3 OKAP")`. Arytmetyka: GA3 850→1450 środek 1150; płyta 864→1436 środek 1150 → **delta 0**.
**Ogon:** PLAN §7, tabela AGD, wiersz `| Okap | **GA2** | recyrkulacyjny z filtrem węglowym [P] …` — przypisanie okapu do **GA2**, czyli do szafki 180 mm nad DA1. Dokładnie ten sam błąd, który naprawiała v3.7a, przetrwał w tabeli AGD.

### E2 — v3.8: kolizja ramię ↔ ciąg A, narożnik liczony dwa razy (RL1+RL2)
**POPRAWIONE CZĘŚCIOWO** — najwięcej ogonów ze wszystkich sześciu.
Naprawione: RL1 to jeden moduł 1176 (nie RL1+RL2 = 1180); K2 PASS (brak nakładek brył); strefa gotowania przesunięta (wariant A), front DA2 kończy się na 1450 = linii ramienia.
**Ogony:**
1. PLAN §5, tabela ramienia, wiersz **„KOLIZJA `[?]`"**: „front ciągu A jest dostępny tylko na odcinku y 60→145 = 85 cm … 27 z 60 cm frontu DA2 (piekarnik) zasłonięte ramieniem. **Do rozstrzygnięcia przez inwestora**" — sprzeczny z PLAN §9a („ROZWIĄZANA wariantem A `[P]`"). Liczby w tym wierszu (60→145) opisują nieistniejący układ sprzed v3.9.
2. PLAN §5, wiersz RL1: „dostępna szerokość 118−60 = **58**" → 580, gdy front ma 600 (M57).
3. FORMATKI §4 pkt 6 i `_formatki.py` l.137: „Ramię: **RL1+RL2** skręcone" — moduł RL2 skasowany w v3.8 (M68).
4. `_schemat.py` l.318: „blat ciągły z **DA4**" — moduł nie istnieje (M69).
5. `_schemat.py` l.172–174: podział lica ramienia **odwrócony** (ślepe 600 / front 576) względem PLAN i `_kontrola` (M58).
6. Narożnik nadal liczony dwa razy **w blatach** (M48) — kontrola K2 nie obejmuje blatów.

### E3 — v3.7: pilaster odczytany ze zdjęcia jako gzyms; GA1 305 → 245
**POPRAWIONE CZĘŚCIOWO.**
Naprawione i spójne: GA1 = **245** w PLAN §5, `_formatki.py` l.21 i `_kontrola.py` (x 155→400); K5 PASS (wszystkie górne A w płaszczyźnie x = 400); 155 + 245 = 400 ✓. Wycięcia 160×(Hg+5), wieniec 240 i „listwa pod gzymsem" usunięte z §5/§11a zgodnie z v3.7.
**Ogony:**
1. PLAN §9, tabela ryzyk, wiersz **„Gzyms/podciąg pod sufitem … koliduje z pasmem górnych 1480–2478 … warianty A) wycięcie w bokach, B) szafki POD gzymsem, C) korpusy pogłębione; szczegóły w pkt 11a"** — cały wiersz odwołany przez v3.7, pkt 11a mówi już o czymś innym (M71).
2. `_formatki.py` l.76 nie przyjął zmiany głębokości: GA1 dostaje półkę **300** w korpusie **245** (M37).
3. PLAN §11a liczy „cofnięcie od lica blatu **181**" na blacie 600, a rozpiska ma blat 635 → 216 (M25).
4. Status samego pilastra rozjechany: `[P]` w pkt 2, `[~]` w §1 i na rzucie, `[?]` w pkt 11.11 (M60) — mimo że reguła protokołu §5 wymaga statusu `[?]` do czasu dwóch liczb od inwestora.

### E4 — v3.11: front DC1 345 zamiast 450, cargo narożne nie mieści się
**POPRAWIONE CZĘŚCIOWO** — poprawka nie dotarła do plików produkcyjnych.
Naprawione: PLAN §5 („front 345 … cargo narożne NIE wejdzie"), PLAN §5a, `_kontrola.py` (front (600,945) = 345; `okucie="szuflady wewnętrzne"`, K8 PASS: 345 ≥ 300), FORMATKI §3 okucia („Szuflady wewnętrzne do DC1 (2 szt., ~300) … magic corner wymaga ≥450 — kontrola K8").
**Ogony:**
1. `_formatki.py` l.20: `("DC1 narożna ślepa", 900, 720, 560, "narozna", FR_BEZ, "**front 450**; …")` — szerokość 900, głębokość 560 i komentarz „front 450" (M15/M16/M17).
2. FORMATKI-ROBOCZE.md — wiersze DC1: bok 560×720, dno 864×560, plecy 896×716, **front 446×716**, blenda 430×716. Rozpiska, która idzie do rozkroju, opisuje wersję sprzed v3.11.
3. `_schemat.py` l.280: „DC1 narożna (**front 45**) + blenda" — elewacja C pokazuje 450.
4. PLAN §5 zostawił blendę „~47 — dopełnienie C1 do 947" przy korpusie 945 → 945+47 = 992 ≠ 947, a bieg C rośnie do 1932 (M06).

### E5 — v3.12: zniknięcie szuflad na sztućce
**POPRAWIONE CZĘŚCIOWO.**
Naprawione: PLAN §5 (RL1 „front 600: drzwi 300 + szuflady 300"), PLAN §5a (górna = sztućce z wkładem), `_kontrola.py` (`funkcje=("sztućce","przybory")`, K9 PASS: front 600 ≥ 250), `_formatki.py` l.16 (opis podziału), FORMATKI §3 okucia (3 kpl nom. 400 + wkład na sztućce 300), `_schemat.py` rzut („drzwi 30 + SZUFLADY 30 (sztućce)").
**Ogony:**
1. **FORMATKI-ROBOCZE.md nie zawiera ani jednego frontu szuflady** — RL1 dostaje wyłącznie front 446×716 i blendę 430×716 (M11/M41). Do rozkroju idzie dokument bez szuflad na sztućce; naprawiono opis, nie naprawiono cięcia.
2. Wysokości trzech frontów szuflad: `[BRAK DANYCH]`.
3. K9 kontroluje szerokość **modułu**, nie szerokość otwarcia: „kosz segregacji ≥450" przechodzi na froncie DB1 = 800, choć realne skrzydła mają 397 (M59). Kontrola dodana po E5 ma tę samą klasę luki, którą miała rozpiska.
4. `_schemat.py` rysuje front ramienia jako 576 — za wąski na 300+300 (M58).

### E6 — przejście 596 → 600 (ramię 1180 → 1176)
**POPRAWIONE CZĘŚCIOWO** — poprawione w korpusie, niepoprawione w blacie, czyli w elemencie, który wyznacza realny prześwit.
Naprawione: `_formatki.py` l.16 (RL1 = 1176), panel ryflowany 1176×910, `_kontrola.py` (RL1 x1 = 1176; K6: 1776 − 1176 = 600 ✓), `_schemat.py` rzut ARM_L = 117,6.
**Ogony:**
1. FORMATKI §2: „Blat ramienia … **545**×500" + blat A 635 → 635 + 545 = **1180** → przejście **1776 − 1180 = 596** (M13/M49).
2. PLAN §5, nagłówek sekcji ramienia: „**~1180×500** `[P gł.]`".
3. PLAN §5, wiersz „blat ramienia | **~1180**×500×38".
4. PLAN §5, wiersz „panel ryflowany | **~1180**×910".
5. `_schemat.py` l.309: `IW = 118.0` — elewacja ramienia rysowana na 1180.
6. PLAN pkt 2, §3, §4, §9, §13: konsekwentnie „~118" (= 1180), przy poprawnym wzorze „177,6 − 60" = 117,6.
Podsumowując: liczba 1176 istnieje w **3** miejscach repo, liczba 1180 w **8**.

**Zbiorczo: 0 × POPRAWIONE KOMPLETNIE, 6 × POPRAWIONE CZĘŚCIOWO, 0 × NIEPOPRAWIONE.**
Wspólny wzorzec wszystkich sześciu: korekta trafia do PLAN §5 i do `_kontrola.py`, a nie trafia do (a) tabel pobocznych PLAN (§7, §9, §13), (b) `_formatki.py` / FORMATKI-ROBOCZE.md, (c) `_schemat.py`. Kontrola automatyczna nie wykrywa żadnego z tych ogonów, bo czyta wyłącznie własny model.

---

## 10. `[BRAK DANYCH]`

Pozycje, których w dokumentacji **nie ma** — nie zostały tu oszacowane ani zinterpolowane:

**Wymiary pomieszczenia**
1. Kąty narożników A/B i B/C (przekątne) — pkt 11.2 zapowiada pomiar, brak wartości.
2. Odchyłka pionu i krzywizny ścian — brak.
3. Poziom podłogi na długości zabudowy — brak.
4. Głębokość parapetu — pkt 11.4 zapowiada, brak wartości.
5. Materiał ścian pod górne szafki (kotwy) — brak; technologia §5 wymaga.
6. Pozycja i wymiar kratki wentylacyjnej — `[?]`, brak liczb.
7. Podejścia wody/odpływu: wysokość i rozstaw — `[~]`, brak liczb.
8. Pozycja puszki siłowej na ścianie A — `[?]`.
9. Wysokość otworu do salonu (127 to tylko szerokość).
10. Rzeczywisty wymiar pilastra na trzech wysokościach — `[?]` (pkt 11.11 wprost: „sam rzut tego nie rozstrzyga").
11. Grubość i wysięg ścianki (9 / 77) — `[~]`, a od nich zależy przejście 600 `[P]`.

**Wymiary mebli**
12. Wysokości trzech frontów szuflad RL1 (jest tylko „górna niska H≈86").
13. Wysokości frontów dwóch szuflad wewnętrznych DC1.
14. Grubość frontów dolnych (górne: 19; dolne nigdzie nie podane).
15. Wymiar i wysokość blendy górnej pod sufitem.
16. Wymiar frontu antresoli nad okapem GA3.
17. Wymiar frontu DB0 (cargo 150).
18. Która krawędź RL1 jest bazą przy głębokości 460 w polu 500 (lico N czy tył S).
19. Wysokość korpusu/obudowy okapu wewnątrz GA3 (front uchylny 400 z 998).
20. Wysokość cokołu pod słupkiem C2 (100 wg 2378, 150 wg reszty).
21. Pozycja wycięcia indukcji w głąb blatu (odległość od lica).
22. Wymiar wycięcia zlewu („wg szablonu").

**AGD i okucia**
23. Model piekarnika (jest tylko nisza 560×590–600) — a od tego zależy zapas 4 mm z M33.
24. Model zmywarki, okapu, zlewu, baterii.
25. Nominały prowadnic — oznaczone `[do potwierdzenia w karcie producenta]`.
26. Kąt otwarcia drzwi lodówki wymagany do wyjęcia szuflad (SKILL: ~110°) vs blenda 50–70 zaprojektowana pod >90°.
27. Kody dekorów Korner — `[DO WERYFIKACJI]`.

---

## 11. ULEPSZENIA (nie błędy — propozycje metrologiczne)

- **U1.** Wygenerować PLAN §5 i `_formatki.py MODULES` **z** `_kontrola.py`, zamiast utrzymywać trzy listy. Wszystkie 6 orzeczeń E1–E6 zakończyło się częściowo dokładnie z tego powodu.
- **U2. K10 — kontrola pionowa.** Dziś żadna z 9 kontroli nie dotyka osi Z. Złapałaby M26 (820 vs 720), M31 (słupek 2528 > 2478), M28 (570 vs 600), M33 (stos DA2), M30 (fuga sufitowa 0).
- **U3. K11 — blaty w modelu.** Blaty są poza `Modul`, więc K2 ich nie sprawdza. Złapałaby M48 (zakładki 1113 mm) i M13/M49 (przejście 596 od blatu, nie od korpusu — czyli **sam błąd E6**).
- **U4. K12 — bilans okuć i listew.** Zliczanie zawiasów/nóżek/zawieszek/cokołu z modelu zamiast ręcznie. Złapałaby M44, M45, M46, M47.
- **U5. K6 poprawka:** mierzyć przejście do **najdalej wysuniętego elementu** (blat/panel), nie do korpusu.
- **U6. K9 poprawka:** mierzyć **światło pojedynczego skrzydła / szuflady**, nie szerokość modułu (M59).
- **U7. K1 poprawka:** dopisać wymóg minimalnego luzu montażowego per bieg (20–50), inaczej „delta 0" jest raportowana jako sukces, a jest ostrzeżeniem (M64, M65).

---

*Raport metrologa. Nie ocenia ergonomii, funkcji, estetyki, kosztów ani wykonalności — wyłącznie liczby i ich zgodność między PLAN.md, `_formatki.py`, `_kontrola.py`, `_schemat.py` i regułami skilla.*
