# Lista formatek i okuć — kuchnia (WERSJA ROBOCZA R1 — pion przeliczony 2026-08-13, FRONTY WCIĄŻ BŁĘDNE)

> ## ⛔ TA LISTA MA POTWIERDZONE BŁĘDY — NIE ZAMAWIAĆ
> Poprawione dziś (v3.13): **wysokości pionowe** — górne 989, słupek 2319, nadstawka 419, wykreślony bok obudowy lodówki i blenda dystansowa (lodówka jest wolnostojąca).
> **NIE poprawione — usterki P0 z audytu:**
> - **P0-01:** generator wystawia dla każdej szafki narożnej sztywny **front 446**. Prawidłowe to **DA1 = 240**, **DC1 = 345**, **RL1 = 600 dzielony (drzwi 300 + 3 fronty szuflad 300)**.
> - **P0-02:** RL1 nie ma tu **żadnego frontu szuflady ani dna** — szuflady na sztućce istnieją tylko w PLAN.md.
> - **P0-06 / P0-11 / P0-12:** cztery urządzenia AGD bez modelu — nisze i wycięcia policzone „na oko".
> - **P0-09:** **Korner NIE wierci otworów.** Nawierty trzeba zlecić osobno albo zrobić samemu — patrz pkt 2a.
> Dopóki te punkty nie zostaną naprawione, lista służy **wyłącznie do wyceny orientacyjnej**.

> **NIE DO CIĘCIA.** Wersja do wyceny w KornerGo / oddział Piekary Śląskie. Wymiary finalne po pomiarach łańcuchowych (PLAN pkt 11) — wtedy poprawiamy stałe w `_formatki.py` i lista przeliczy się sama. Blendy i ostatnie moduły w ciągach zawsze docinane na miejscu. Płyta 18 mm; plecy HDF 3 mm nakładane; wysokości korpusów: dolne 720 (nóżki 150), górne **989**, słupek **2319**, nadstawka C4 **419** — przeliczone z sufitu **2481** `[P]` minus fuga 12 (góra zabudowy 2469).

## 1. Formatki

| Element | Wymiar (mm) | szt | Płyta/kolor | Obrzeże ABS |
|---|---|---|---|---|
| DA1 narożna ślepa — bok | 405×720 | 2 | kremowy (korpus) | 0,4 mm przód |
| DA1 narożna ślepa — dno | 814×405 | 1 | kremowy (korpus) | 0,4 przód |
| DA1 narożna ślepa — trawersy górne | 814×100 | 2 | kremowy (korpus) | 0,4 |
| DA1 narożna ślepa — plecy HDF | 846×716 | 1 | HDF biały | — |
| DA1 narożna ślepa — front | 446×716 | 1 | beż/kaszmir mat (front) | 1,0 — 4 krawędzie |
| DA1 narożna ślepa — blenda ślepa | 430×716 | 1 | beż/kaszmir mat (front) | 1,0 przód |
| DA2 piekarnik+indukcja — bok | 560×720 | 2 | kremowy (korpus) | 0,4 mm przód |
| DA2 piekarnik+indukcja — dno | 564×560 | 1 | kremowy (korpus) | 0,4 przód |
| DA2 piekarnik+indukcja — trawersy górne | 564×100 | 2 | kremowy (korpus) | 0,4 |
| DA2 piekarnik+indukcja — plecy HDF | 596×716 | 1 | HDF biały | — |
| DA2 piekarnik+indukcja — front szuflady dolnej | 596×110 | 1 | beż/kaszmir mat (front) | 1,0 |
| DA2 piekarnik+indukcja — trawers nośny piekarnika | 564×560 | 1 | kremowy (korpus) | 0,4 |
| RL1 ramię narożna ślepa + szuflady — bok | 460×720 | 2 | kremowy (korpus) | 0,4 mm przód |
| RL1 ramię narożna ślepa + szuflady — dno | 1140×460 | 1 | kremowy (korpus) | 0,4 przód |
| RL1 ramię narożna ślepa + szuflady — trawersy górne | 1140×100 | 2 | kremowy (korpus) | 0,4 |
| RL1 ramię narożna ślepa + szuflady — plecy HDF | 1172×716 | 1 | HDF biały | — |
| RL1 ramię narożna ślepa + szuflady — front | 446×716 | 1 | beż/kaszmir mat (front) | 1,0 — 4 krawędzie |
| RL1 ramię narożna ślepa + szuflady — blenda ślepa | 430×716 | 1 | beż/kaszmir mat (front) | 1,0 przód |
| DB0 cargo 15 — bok | 560×720 | 2 | kremowy (korpus) | 0,4 mm przód |
| DB0 cargo 15 — dno | 114×560 | 1 | kremowy (korpus) | 0,4 przód |
| DB0 cargo 15 — trawersy górne | 114×100 | 2 | kremowy (korpus) | 0,4 |
| DB0 cargo 15 — plecy HDF | 146×716 | 1 | HDF biały | — |
| DB1 zlewowa — bok | 560×720 | 2 | kremowy (korpus) | 0,4 mm przód |
| DB1 zlewowa — dno | 764×560 | 1 | kremowy (korpus) | 0,4 przód |
| DB1 zlewowa — trawersy górne | 764×100 | 2 | kremowy (korpus) | 0,4 |
| DB1 zlewowa — fronty | 397×716 | 2 | beż/kaszmir mat (front) | 1,0 — 4 krawędzie |
| DB2 zmywarka 45 — front | 446×713 | 1 | beż/kaszmir mat (front) | 1,0 mm — 4 krawędzie |
| DC1 narożna ślepa — bok | 560×720 | 2 | kremowy (korpus) | 0,4 mm przód |
| DC1 narożna ślepa — dno | 864×560 | 1 | kremowy (korpus) | 0,4 przód |
| DC1 narożna ślepa — trawersy górne | 864×100 | 2 | kremowy (korpus) | 0,4 |
| DC1 narożna ślepa — plecy HDF | 896×716 | 1 | HDF biały | — |
| DC1 narożna ślepa — front | 446×716 | 1 | beż/kaszmir mat (front) | 1,0 — 4 krawędzie |
| DC1 narożna ślepa — blenda ślepa | 430×716 | 1 | beż/kaszmir mat (front) | 1,0 przód |
| GA1 górna — bok | 245×989 | 2 | kremowy (korpus) | 0,4 mm przód |
| GA1 górna — dno/wieniec | 634×245 | 2 | kremowy (korpus) | 0,4 przód |
| GA1 górna — plecy HDF | 666×985 | 1 | HDF biały | — |
| GA1 górna — fronty | 332×996 | 2 | ciemny orzech mat (front/panel) | 1,0 — 4 krawędzie |
| GA1 górna — półki | 633×300 | 2 | kremowy (korpus) | 0,4 |
| GA2 górna wąska — bok | 400×989 | 2 | kremowy (korpus) | 0,4 mm przód |
| GA2 górna wąska — dno/wieniec | 144×400 | 2 | kremowy (korpus) | 0,4 przód |
| GA2 górna wąska — plecy HDF | 176×985 | 1 | HDF biały | — |
| GA2 górna wąska — front | 176×996 | 1 | ciemny orzech mat (front/panel) | 1,0 — 4 krawędzie |
| GA2 górna wąska — półki | 143×300 | 2 | kremowy (korpus) | 0,4 |
| GA3 okap — bok | 400×989 | 2 | kremowy (korpus) | 0,4 mm przód |
| GA3 okap — dno/wieniec | 564×400 | 2 | kremowy (korpus) | 0,4 przód |
| GA3 okap — plecy HDF | 596×985 | 1 | HDF biały | — |
| GA3 okap — front uchylny (wg okapu) | 596×400 | 1 | ciemny orzech mat (front/panel) | 1,0 [~] |
| GA4 górna — bok | 400×989 | 2 | kremowy (korpus) | 0,4 mm przód |
| GA4 górna — dno/wieniec | 464×400 | 2 | kremowy (korpus) | 0,4 przód |
| GA4 górna — plecy HDF | 496×985 | 1 | HDF biały | — |
| GA4 górna — front | 496×996 | 1 | ciemny orzech mat (front/panel) | 1,0 — 4 krawędzie |
| GA4 górna — półki | 463×300 | 2 | kremowy (korpus) | 0,4 |
| GC1 górna (ociekarka) — bok | 400×989 | 2 | kremowy (korpus) | 0,4 mm przód |
| GC1 górna (ociekarka) — dno/wieniec | 434×400 | 2 | kremowy (korpus) | 0,4 przód |
| GC1 górna (ociekarka) — plecy HDF | 466×985 | 1 | HDF biały | — |
| GC1 górna (ociekarka) — front | 466×996 | 1 | ciemny orzech mat (front/panel) | 1,0 — 4 krawędzie |
| GC1 górna (ociekarka) — półki | 433×300 | 2 | kremowy (korpus) | 0,4 |
| GC2 górna — bok | 400×989 | 2 | kremowy (korpus) | 0,4 mm przód |
| GC2 górna — dno/wieniec | 441×400 | 2 | kremowy (korpus) | 0,4 przód |
| GC2 górna — plecy HDF | 473×985 | 1 | HDF biały | — |
| GC2 górna — front | 473×996 | 1 | ciemny orzech mat (front/panel) | 1,0 — 4 krawędzie |
| GC2 górna — półki | 440×300 | 2 | kremowy (korpus) | 0,4 |
| C2 słupek spiżarnia — bok | 580×2319 | 2 | kremowy (korpus) | 0,4 mm przód |
| C2 słupek spiżarnia — dno/wieniec | 244×580 | 2 | kremowy (korpus) | 0,4 przód |
| C2 słupek spiżarnia — plecy HDF | 276×2315 | 1 | HDF biały | — |
| C2 słupek spiżarnia — front dolny (wysuw) | 276×717 | 1 | ciemny orzech mat (front/panel) | 1,0 |
| C2 słupek spiżarnia — front górny (drzwi) | 276×1590 | 1 | ciemny orzech mat (front/panel) | 1,0 |
| C2 słupek spiżarnia — półki | 243×560 | 2 | kremowy (korpus) | 0,4 |
| C4 nadstawka lodówki — bok | 580×419 | 2 | kremowy (korpus) | 0,4 mm przód |
| C4 nadstawka lodówki — dno | 624×580 | 1 | kremowy (korpus) | 0,4 przód |
| C4 nadstawka lodówki — trawersy górne | 624×100 | 2 | kremowy (korpus) | 0,4 |
| C4 nadstawka lodówki — plecy HDF | 656×415 | 1 | HDF biały | — |
| C4 nadstawka lodówki — fronty | 327×415 | 2 | ciemny orzech mat (front/panel) | 1,0 — 4 krawędzie |
| Panel ryflowany ramienia (lamele — dostawca zewn.) | 1176×910 | 1 | ciemny orzech mat (front/panel) | 1,0 widoczne |
| Blenda dolna A przy pilastrze (~610 do frontu DA1) | 610×756 | 1 | beż/kaszmir mat (front) | 1,0 widoczne |
| Listwa cokołowa (czarny mat), łącznie ~5 mb | 5000×150 | 1 | czarny mat | 1,0 widoczne |

**Szacunek płyt (z zapasem +15% na rozkrój):**

| Kolor | m² netto | m² z zapasem |
|---|---|---|
| kremowy (korpus) | 19.7 | 22.6 |
| HDF biały | 6.4 | 7.3 |
| ciemny orzech mat (front/panel) | 4.5 | 5.2 |
| beż/kaszmir mat (front) | 3.3 | 3.8 |
| czarny mat | 0.8 | 0.9 |

## 2. Blaty (laminat 38 mm, **szerokość 600** `[P]` — decyzja inwestora 2026-08-13, dekor jasny trawertyn [DO WERYFIKACJI])

| Blat | Wymiar (mm) | Uwagi |
|---|---|---|
| Blat A (ciąg indukcji) | 1950×600 | docinany na miejscu; wysięg nad licem frontu 21–35 mm |
| Blat B (ciąg okna) | 2389×600 | docinany na miejscu; wysięg nad licem frontu 21–35 mm |
| Blat C1 (niski ciąg) | 947×600 | docinany na miejscu; wysięg nad licem frontu 21–35 mm |
| Blat ramienia (docinka na wschód od blatu A) | 545×500 | docinany na miejscu; wysięg nad licem frontu 21–35 mm |

Łączenia blatów: 3 (narożnik A/B przy pilastrze, narożnik B/C1, A/ramię) — frez + śruby łącznikowe 3 kpl, silikon. Wycięcia: indukcja **560×490** [P] w blacie A, zlew wg szablonu w blacie B — samodzielnie wyrzynarką (krawędzie zabezpieczyć silikonem) albo CNC przy rozkroju.

## 2a. STRONY ZAWIASÓW — do zlecenia nawiertów

> **⚠ P0-09 — KORNER NIE WIERCI.** Korner tnie i okleja, ale **nie robi otworów montażowych**
> (`skills/architekt-wnetrz/references/dostawcy.md` w. 86 — informacja od inwestora).
> Nawierty trzeba zlecić **osobno**, u firmy z CNC, albo zrobić samodzielnie przyrządem
> do puszek 35 z ogranicznikiem. **Rozstrzygnąć PRZED zamówieniem rozkroju** — decyzja
> zmienia zawartość zamówienia, budżet i to, czy formatki jadą jeszcze w drugie miejsce.
>
> | droga | co to znaczy | koszt orientacyjny `[?]` |
> |---|---|---|
> | **A — usługa CNC** | wozisz formatki po rozkroju do firmy z wiertarką CNC | ~150–400 zł |
> | **B — samodzielnie** | przyrząd do puszek 35 z ogranicznikiem + wiertło Forstnera | ~200 zł jednorazowo |
>
> Firmy z CNC w okolicy (`dostawcy.md`, wszystkie `[DO POTWIERDZENIA telefonicznie]`):
> **MEBsystem** Gliwice ul. Pszczyńska 206 (~8 km) · **Soma** Chorzów ul. Katowicka 160B ·
> **Komandor Śląsk** Katowice ul. Transportowców 35 · **Daedalus** Ruda Śląska (wiercenie `[?]`).

Strony zawiasów dobrane tak, żeby dwa sąsiadujące skrzydła nie wisiały na wspólnej krawędzi —
otwarte leżą wtedy w jednej płaszczyźnie i zderzają się (kontrola **K10**). Tę tabelę oddajesz
wykonawcy nawiertów niezależnie od tego, którą drogę wybierzesz.

| Moduł | Front (mm) | Oś zawiasu | Dlaczego ta strona |
|---|---|---|---|
| DA1 narożna ślepa | 610–850 | **850** (południe) | szersze otwarcie w stronę ślepego rogu |
| DA2 indukcja+piekarnik | 850–1450 | — | drzwi piekarnika opadają, szuflada się wysuwa |
| RL1 ramię — drzwi 300 | 576–876 | **876** (wschód) | otwarte skrzydło odsłania dojście do martwego pola na zachód |
| RL1 ramię — 3 szuflady | 876–1176 | — | szuflady |
| DB0 cargo 15 | 600–750 | — | cargo wysuwane |
| DB1 zlew 80 | 750–1550 | **750 i 1550** (para) | dwa skrzydła spotykają się w środku |
| DB2 zmywarka 45 | 1550–2000 | — | drzwi AGD, zawias dolny |
| DC1 narożna ślepa | 600–945 | **945** | otwarte skrzydło odsłania dojście do ślepej części przy ścianie B |
| C2 słupek — front DOLNY (150–871) | 945–1225 | **BRAK — wysuw** | drzwi zderzyłyby się ze skrzydłem DC1 (oba w paśmie 155–871) |
| C2 słupek — front GÓRNY (875–2469) | 945–1225 | **945** | powyżej 871 DC1 się kończy — krawędź jest wolna |
| C3 lodówka | 1225–1885 | **1225** (strona słupka) | wariant A `[P]` — zawiasy przełożone; przy ściance skrzydło się nie otwiera |
| GA1 górna | 0–670 | **0 i 670** (para) | dwa skrzydła |
| GA2 wąska 180 | 670–850 | **850** (od okapu) | 670 zajmuje prawe skrzydło GA1 |
| GA3 okap | 850–1450 | — | front uchylny do góry |
| GA4 górna | 1450–1950 | **1950** (zewnętrzna krawędź ciągu) | otwiera się od strony korytarza, nie nad płytę |

## 3. Okucia — lista zakupowa (Korner korner.pl: Blum/GTV/Rejs w ofercie)

| Pozycja | Ilość | Uwagi |
|---|---|---|
| Zawiasy puszkowe 110° z prowadnikiem (Blum ClipTop / GTV) | **36 szt** | fronty dolne 2 szt/front, górne ~996 mm 3 szt/front; w tym zapas ~10% |
| Zawiasy 155° (do narożnej DC1) | 2 szt | szeroki kąt przy ślepej |
| **System szuflad z metalowymi bokami, nom. 400** (GTV Modern Box / Rejs / Blum Tandembox) | **3 kpl** | RL1 ramię — korpus 300 szer., 460 gł.; górna niska (H≈86) pod wkład na sztućce, dwie M (≈135) |
| **System szuflad z metalowymi bokami, nom. 500** | 1 kpl | DA2 — szuflada pod piekarnikiem, korpus 600 szer., 560 gł. |
| **System szuflad z metalowymi bokami, nom. 450** | 2 kpl | DC1 — szuflady wewnętrzne za drzwiami, ~300 szer., 546 gł. |
| **Wkład na sztućce 300** | 1 szt | do górnej szuflady RL1 |
| — dlaczego metalowe boki, a nie kulkowe: | — | przy metalowych bokach **nie budujesz skrzynki z płyty** (odpadają 4 formatki i problem kątów prostych na szufladę) — dokupujesz tylko dno i front; cichy domyk w standardzie. Nominały prowadnic **[do potwierdzenia w karcie producenta]** — muszą być ≤ głębokości korpusu |
| Cargo 150 (Rejs/Peka) | 1 kpl | DB0 |
| Cargo spiżarniane wysokie do słupka 280 | 1 kpl | **[DO WERYFIKACJI]** — szerokość niestandard.; alternatywa: półki + drzwi |
| Podnośnik frontu okapu (Aventos HK-S lub wg okapu) | 1 kpl | GA3 — dobór po zakupie okapu |
| Nóżki meblowe 150 + klipsy cokołu | 32 + 16 szt | 8 szafek dolnych ×4 |
| **Szuflady wewnętrzne do DC1 (2 szt., szer. ~300)** | 2 szt | cargo narożne NIE mieści się: front DC1 ma 345 mm (zasłonięty korpusem zmywarki), a magic corner wymaga ≥450 — kontrola K8 |
| Zawieszki regulowane górnych + listwa montażowa | 10 szt + 3 mb | GA1-3, GC1-2 |
| Konfirmaty 7×50 + kołki 8×35 + wkręty 4×30/4×16 | 1 opak. każde | montaż korpusów |
| Śruby łącznikowe blatu | 3 kpl | łączenia |
| Listwa gola / frez uchwytowy | ~5 mb | decyzja technologiczna: profil alu vs frez CNC w płycie |
| Kątowniki montażowe (ramię do posadzki, ścianka) | 8 szt | kotwienie ramienia |
| Taśma LED 3000K + profil + zasilacz 24V | ~3 mb + 1 szt | pod GA i GC |
| Silikon + Silikorner (uszczelka cokołu — Korner korner.eu) | 1+1 | |

## 4. Plan montażu — kolejność (montaż samodzielny)

1. **Instalacje + posadzka docelowa** → pomiary łańcuchowe (PLAN pkt 11) → korekta `_formatki.py` → **zamówienie rozkroju z oklejaniem w KornerGo** (transport Korner). **NAWIERTY OSOBNO — Korner ich nie robi**, patrz pkt 2a: usługa CNC albo przyrząd własny.
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
