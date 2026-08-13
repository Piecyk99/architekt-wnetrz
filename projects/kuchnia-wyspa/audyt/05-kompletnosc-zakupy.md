# Audyt 05 — KOMPLETNOŚĆ I ZAKUPY

**Projekt:** kuchnia-wyspa v3.12a (U + ramię L) · **Data audytu:** 2026-08-13
**Materiał wejściowy:** `PLAN.md` (v3.12a), `FORMATKI-ROBOCZE.md` (nagłówek: „v3.5 R1"), `_formatki.py`, `_kontrola.py`, `references/formatki.md`, `references/dokumentacja-stolarz.md`, `references/dostawcy.md`
**Zakres:** pokrycie ścian, kompletność modułów, plan funkcjonalny, BOM. **Poza zakresem:** ergonomia, kolizje ruchowe, wycena.

Zasady audytu: zero wymyślonych wymiarów; każdy brak → `[BRAK DANYCH]`; każdy zarzut → cytat lub współrzędna z `_kontrola.py`; arytmetyka wypisana.

---

## 0. Inwentaryzacja

### 0.1 Co jest w projekcie

| Warstwa | Stan |
|---|---|
| Moduły szafkowe | **15** (`_formatki.py::MODULES`): DA1, DA2, RL1, DB0, DB1, DB2, DC1, GA1, GA2, GA3, GA4, GC1, GC2, C2, C4 |
| Elementy nie-szafkowe | C3 (lodówka wolnostojąca — nie jest modułem), 4 panele (`PANELE`), 4 docinki blatu (`BLATY`) |
| Model geometryczny | `_kontrola.py` — 9 kontroli, **PASS, 0 błędów, 0 uwag**; regresja 5/5 |
| Lista formatek | `FORMATKI-ROBOCZE.md` — 86 pozycji, 5 dekorów, tabela okuć 22 pozycje |
| Plan funkcjonalny | `PLAN.md` pkt 5a — 15 wierszy |

### 0.2 Fakt bazowy dla całego audytu

`FORMATKI-ROBOCZE.md` i `_formatki.py` mają nagłówek **„kuchnia v3.5"**. PLAN jest w **v3.12a**. Między tymi wersjami zaszły v3.8–v3.12a: przebudowa DA1 na narożną ślepą z frontem 240, korekta DC1 na front 345, podział frontu RL1 na drzwi 300 + 3 szuflady, korekta ramienia 1180→1176, zmiana dekoru zabudowy lodówki na antracyt.

**`_formatki.py` nie przyjął żadnej z tych zmian.** Dowód — `_formatki.py` linia 20:

```
("DC1 narożna ślepa", 900, 720, 560, "narozna", FR_BEZ, "front 450; martwe pole przy B; docinana blendą 47"),
```

„front 450" to stan sprzed v3.11, którą PLAN opisuje tak: *„kontrola wykryła nowy błąd: front DC1 ma 345 mm, a nie 450"*. Analogicznie DA1 i RL1 są generowane szablonem `"narozna"`, który każdemu narożnikowi wystawia sztywno **front 446×716 + blendę ślepą 430×716** (`_formatki.py` linie 69–71) — niezależnie od tego, że PLAN daje DA1 front **240**, a RL1 front **600 dzielony**.

**Konsekwencja: lista formatek nie opisuje projektu v3.12a.** Wszystkie liczby m² i mb poniżej pochodzą z tej listy, więc dziedziczą ten błąd — zaznaczam to przy każdej pozycji.

---

## 1. POKRYCIE ŚCIAN

Układ współrzędnych za `_kontrola.py`: origin = wewnętrzny narożnik A/B, x → wschód (do ściany C), y → południe (do korytarza). Ściana C na x=2546, linia południowa y=1950, ścianka x1776–2546 / y1885–1975.

### 1.1 Ciąg A — lico x=560, oś y, 0 → 1950

| Odcinek (y) | mm | Co tam jest | Front? | Ocena |
|---|---|---|---|---|
| 0 → 610 | **610** | lico ślepej części DA1 (korpus x155–560, y0–850) | blenda | świadome `[P]` — korpus pracuje za blendą, dostęp przez front 240 |
| 610 → 850 | **240** | DA1 — drzwi | TAK | ✓ |
| 850 → 1450 | **600** | DA2 — piekarnik + indukcja | TAK | ✓ |
| 1450 → 1950 | **500** | ślepy narożnik pod ramieniem (korpus RL1) | brak | świadome `[P]` |

**Arytmetyka:** 610 + 240 + 600 + 500 = **1950** ✓ (= długość ciągu A `[P]`).
**Front użytkowy: 240 + 600 = 840 mm z 1950 = 43 %.**

> **Błąd w PLAN pkt 5, nagłówek ciągu A:** *„fronty dolne dostępne tylko 670→1450 = 780"*. Po v3.10 front DA1 zaczyna się na **610**, nie 670. Poprawnie: 610→1450 = **840**. Nagłówek jest z v3.9 (gdy DA1 = 670–850) i nie został przeliczony.

### 1.2 Ramię RL1 — lico y=1450, oś x, 0 → 1176

| Odcinek (x) | mm | Co tam jest | Front? | Ocena |
|---|---|---|---|---|
| 0 → 576 | **576** | ślepy narożnik pod ramieniem (za licem ciągu A) | blenda | świadome `[P]` v3.8 — od północy stoi tu korpus DA2, front fizycznie niemożliwy |
| 576 → 876 | **300** | drzwi (dostęp bokiem do martwego pola) | TAK | ✓ |
| 876 → 1176 | **300** | 3 szuflady (sztućce / przybory / pojemniki) | TAK | ✓ |

**Arytmetyka:** 576 + 300 + 300 = **1176** ✓.
**Front użytkowy: 600 z 1176 = 51 %.**

### 1.3 Ciąg B — lico y=600, oś x, 155 → 2546

| Odcinek (x) | mm | Co tam jest | Front? | Ocena |
|---|---|---|---|---|
| 155 → 600 | **445** | róg przejęty przez korpus DA1 (v3.10) | brak | świadome `[P]` |
| 600 → 750 | **150** | DB0 cargo przyprawnik | TAK | ✓ |
| 750 → 1550 | **800** | DB1 zlew (okno 752→1608) | TAK | ✓ |
| 1550 → 2000 | **450** | DB2 zmywarka | TAK | ✓ |
| 2000 → 2546 | **546** | róg przejęty przez korpus DC1 | brak | świadome `[P]` |

**Arytmetyka:** 445 + 150 + 800 + 450 + 546 = **2391** = 2546 − 155 ✓ (PLAN podaje ścianę B jako 2389 — różnica 2 mm, do zamknięcia pomiarem 11.2).
**Front użytkowy: 1400 z 2391 = 59 %.**

> **Pustka techniczna 40 mm:** korpus DA1 kończy się na x=560, DB0 zaczyna na x=600. Odcinek x560–600 × y0–600 (40 × 600 mm) nie należy do żadnego modułu. Na licu zakrywa go blenda 155–600, ale **w liście formatek nie ma tej blendy** (patrz §5, poz. B-04).

### 1.4 Ciąg C — lico x=2000 (DC1) / x=1946 (C2, C3), oś y, 0 → 1885

| Odcinek (y) | mm | Co tam jest | Front? | Ocena |
|---|---|---|---|---|
| 0 → 600 | **600** | lico DC1 zasłonięte korpusem zmywarki (DB2 = x1550–2000, y0–600) | brak | świadome `[P]` v3.11 |
| 600 → 945 | **345** | DC1 — drzwi + 2 szuflady wewnętrzne | TAK | ✓ |
| 945 → 1225 | **280** | C2 słupek cargo | TAK | ✓ |
| 1225 → 1885 | **660** | C3 zabudowa lodówki | TAK | ✓ |

**Arytmetyka:** 600 + 345 + 280 + 660 = **1885** ✓.
**Front użytkowy: 1285 z 1885 = 68 %.**

> **Uskok lica 54 mm — nieopisany i niekontrolowany.** DC1 ma lico na x=2000, C2 i C3 na x=1946. Różnica **2000 − 1946 = 54 mm**: słupek i lodówka wystają 54 mm przed front DC1. `_kontrola.py::k5_lico_gornych` sprawdza wspólną płaszczyznę **tylko dla górnych A** (`GORNE_A`) — dolne ciągi nie mają takiej kontroli. PLAN nigdzie tego uskoku nie wymienia; w rzucie pkt 3 lico C jest rysowane jako jedna linia. To albo błąd modelu, albo świadomy uskok, którego nikt nie zapisał. **`[DO ROZSTRZYGNIĘCIA]`**
>
> Skutek praktyczny: drzwi DC1 (345) mogą mieć zawias tylko od północy (od strony zmywarki) — zawias od południa uderzy w wystający o 54 mm bok C2. A zawias od północy oznacza, że otwarte skrzydło staje dokładnie przed frontem zmywarki (y=600, x1655–2000). Patrz §4, poz. Z-02.

### 1.5 Górne

| Ściana | Moduły | Suma | Długość ciągu | Pokrycie |
|---|---|---|---|---|
| A (1480–2478) | GA1 670 + GA2 180 + GA3 600 + GA4 500 | **1950** | 1950 | **100 %** ✓ |
| C (1480–2478) | GC1 470 + GC2 477 | **947** | 947 (nad DC1) | **100 %** ✓ |
| **B (1480–2478)** | **brak** | **0** | 2391 | **0 %** |

### 1.6 Ściana B na wysokości górnych — jedyny realny niezagospodarowany odcinek

PLAN pkt 5 deklaruje: *„bez górnych na B — okno do sufitu; parapet ~166 użytkowy"*. Ale okno zajmuje tylko **856 mm** z 2391 mm ściany B (wnęka 85,6 `[P]`, x752 → 1608). Zostają dwa pasy wolnej ściany na wysokości 1480–2478:

**Pas wschodni (od okna do ściany C):**
- okno kończy się na x = **1608**
- górne GC1/GC2 wiszą na ścianie C i wystają 400 mm → ich bok jest na x = 2546 − 400 = **2146**
- wolne: 2146 − 1608 = **538 mm** szerokości × 998 wysokości × 400 głębokości ≈ **0,21 m³ ≈ 210 l**

**Pas zachodni (od pilastra do okna):**
- okno zaczyna się na x = **752**
- górne GA1/GA2 wiszą na ścianie A i wystają 400 mm → ich bok jest na x = **400**
- wolne: 752 − 400 = **352 mm** × 998 × 400 ≈ 0,14 m³ ≈ 140 l

**Razem 890 mm szerokości ściany B nie ma zabudowy na wysokości pasma górnych.**

Czy to przeoczenie? **Tak — i jest na to dowód w samym PLANie.** Pkt 2, tabela wymiarów:

> „Wnęka okienna → ściana C (strona lodówki, **„gdzie szafki do sufitu"**) | **94,7** | `[P]` | pomiar inwestora; **= prawy odcinek ściany B**"

Inwestor wskazał odcinek **94,7 na ścianie B** jako miejsce „gdzie szafki do sufitu". W projekcie górne do sufitu (GC1 470 + GC2 477 = **947**) stanęły na **ścianie C**, nad DC1 — inny odcinek o mylnie podobnej długości (945 mm wychodzi z rachunku 1885 − 280 − 660). Nigdzie nie ma zapisu decyzji „przenosimy szafki z B na C". Równocześnie pkt 5 stwierdza „bez górnych na B" bez uzasadnienia dla pasa poza oknem. **Wewnętrzna sprzeczność PLANu.**

### 1.7 Podsumowanie pokrycia

| Ciąg | Długość lica | Front użytkowy | Ślepe lico |
|---|---|---|---|
| A | 1950 | 840 | 1110 |
| Ramię | 1176 | 600 | 576 |
| B | 2391 | 1400 | 991 |
| C | 1885 | 1285 | 600 |
| **Razem dolne** | **7402** | **4125 (56 %)** | **3277 (44 %)** |

**44 % lica dolnej zabudowy nie ma frontu.** Każdy odcinek jest udokumentowany jako świadoma decyzja i domknięty blendą (`_kontrola.py::k7` PASS) — to nie jest dziura w rysunku. To jest jednak koszt geometrii: pilaster 67×15,5, ramię gł. 500 wchodzące w pas y145–195 i zmywarka wcinająca się 54 mm w narożnik C zjadają łącznie 3,3 m lica.

**Objętość dostępna tylko „sięgiem w głąb"** (przez otwór węższy niż 350 mm, na głębokość ≥ 570 mm):

| Strefa | Objętość wg PLAN | Otwór | Głębokość sięgu |
|---|---|---|---|
| DA1 narożna | 248 l | 240 mm | 600 mm |
| pod ramieniem (RL1) | 202 l | 300 mm | 576 mm |
| narożnik północny DC1 | 236 l | 345 mm (i tylko gdy szuflady wewn. wysunięte) | ~600 mm |
| **Razem** | **686 l** | | |

686 l — to więcej niż pojemność wszystkich frontowych szuflad w tej kuchni razem wziętych. PLAN przypisuje tym strefom garnki (DA1), patelnie i blachy (pod ramieniem) oraz sztućce serwisowe (DC1) — czyli rzeczy codzienne w magazynie z dostępem przez wąską gardziel. To główny zarzut funkcjonalny tego audytu.

---

## 2. DODAĆ

### D-01. Górna GB1 na ścianie B, pas wschodni — 538×998×400 `[REKOMENDACJA]`

**Miejsce:** ściana B, x 1608 → 2146, wysokość 1480 → 2478 (to samo pasmo co GA i GC).
**Rachunek zmieszczenia:**
- prawa granica: bok GC1 = 2546 − 400 (wysięg górnych) = **2146**
- lewa granica: krawędź wnęki okiennej = **1608** `[P]` (752 + 856)
- 2146 − 1608 = **538 mm**
- kolizje: brak — GA/GC wiszą na innych ścianach, blat pod spodem jest na 910, dół szafki na 1480 (prześwit 570), zmywarka i narożnik DC1 są pod blatem.

**Zastrzeżenie `[BRAK DANYCH]`:** nie wiadomo, w którą stronę i czy w ogóle otwiera się skrzydło okna (PLAN nie zawiera tej informacji; pkt 11.4 każe zmierzyć tylko 59,7 / 85,6 / 81,7 + głębokość parapetu). Jeśli okno otwiera się do wnętrza, szafka flush z krawędzią wnęki zablokuje skrzydło. **Wariant bezpieczny: korpus 450 + blenda 88 przy oknie** (450 + 88 = 538 ✓).

**Uzasadnienie funkcjonalne:** to jedyne miejsce w kuchni oddalone o 1 krok od zmywarki (DB2 = x1550–2000) i jednocześnie od zlewu, na wysokości chwytu 1480–1900. Rozwiązuje dwie luki naraz: (a) brak modułu na drobne AGD (§5), (b) górne półki GC1/GC2 sięgają 2478, czyli powyżej wygodnego zasięgu — dokładając GB1 przenosisz naczynia codzienne na poziom 1480–1800 i zwalniasz górę GC na sezonowe.
**Koszt:** 1 korpus (2 boki 400×998, 2 wieńce, plecy, front, 2 półki), 2 zawieszki, 3 zawiasy, ~0,55 m² płyty korpusowej + 0,54 m² frontu.

### D-02. Kosz segregacji do DB1 — **brak w BOM mimo że jest w planie funkcjonalnym i w kontroli K9**

PLAN pkt 5a: *„DB1 zlew 80 | kosze segregacji, chemia, akcesoria zlewu"*. `_kontrola.py::FUNKCJE_OBOWIAZKOWE` wymaga `"kosz segregacji": 450` i przechodzi, **bo sprawdza tylko szerokość frontu (800 ≥ 450), nie fakt zakupu okucia**. W tabeli okuć `FORMATKI-ROBOCZE.md` §3 **nie ma ani jednej pozycji ze słowem „kosz"**.
**Do dokupienia:** kosz segregacyjny 2-komorowy montowany na drzwiach lub na dnie szafki 800. Ograniczenie: syfon zlewu 1-komorowego z ociekaczem zajmuje środek szafki → **kosz musi być modelem drzwiowym albo dwoma pojemnikami po bokach syfonu**, nie pełnowymiarowym wysuwem 800. Wymiar do doboru po ustaleniu pozycji syfonu (pomiar 11.7).

### D-03. Wkład ociekowy do GC1 — brak w BOM, a szafka jest po nim nazwana

PLAN pkt 5 i 5a: *„GC1 górna nad DC1 | półki + **ociekarka na umyte naczynia**"*. W BOM: brak.
**Problem wymiarowy:** GC1 ma 470 szerokości → światło korpusu 470 − 2×18 = **434 mm**. Katalogowe wkłady ociekowe są „do szafki 500 / 600 / 800" i mają realną szerokość ~460 mm. **434 < 460 → standardowy wkład nie wejdzie.**
**Poprawka bezkosztowa:** GC1 470 → **500**, GC2 477 → **447**. Kontrola: 500 + 447 = **947** ✓ (bez zmiany długości ciągu C). Światło GC1 = 500 − 36 = 464 ≥ 460 ✓.

### D-04. Wieniec/panel boczny ramienia od strony przejścia — ~500×910

PLAN pkt 5, wiersz „blat ramienia": *„w L z blatem DA (łączenie frezowane/listwa); **wieniec na końcu od przejścia**"*. W `PANELE` jest tylko `Panel ryflowany ramienia 1176×910` (ściana południowa, od salonu). Wschodni koniec ramienia (x=1176, y1450–1950) to **odsłonięta bryła w przejściu 600 mm** — bez elementu wykończeniowego pokazuje krawędź korpusu i blat od spodu.
**Do dodania:** panel ~500×910, dekor jak panel ryflowany albo front, obrzeże 1,0 na 3 widocznych krawędziach.

### D-05. Dna szuflad — 6 szt, zero w liście formatek

BOM zamawia **6 kompletów prowadnic** (3 kpl nom. 400 do RL1, 1 kpl nom. 500 do DA2, 2 kpl nom. 450 do DC1) i sam sobie tłumaczy dlaczego:

> „przy metalowych bokach **nie budujesz skrzynki z płyty** — dokupujesz tylko **dno i front**"

W liście formatek nie ma **ani jednego dna szuflady** i tylko **jeden front szuflady** (`DA2 — front szuflady dolnej 596×110`). Brakuje 6 den (płyta lub HDF wg systemu) i 5 frontów (3× RL1, 2× DC1 wewnętrzne). Patrz też §5, poz. F-02.

### D-06. Zaślepki, taśma aluminiowa, klej montażowy, listwy przyblatowe, zaślepki blatu

Nie ma w BOM (szczegóły w tabeli §6): zaślepki do konfirmatów, taśma aluminiowa antyparowa nad zmywarką, klej montażowy, **listwa przyblatowa** (mimo że plan montażu krok 10 mówi „listwy przyblatowe"), zaślepki/listwy końcowe blatu, obrzeże do przyciętych krawędzi blatu.

### D-07. `[OPCJA]` Szuflada cokołowa pod ramieniem — 1176×460, wysokość ~110

Cokół 150 mm na długości 1176 mm to obecnie martwa przestrzeń. Szuflada cokołowa (prowadnica nom. 450 ≤ 460 głębokości korpusu ✓, front 1176×~130) daje **≈ 60 l** płaskiego magazynu na blachy, tacki, formy — czyli dokładnie to, co dziś PLAN wpycha w 202-litrową ślepą strefę pod ramieniem.
Warunek: w tym odcinku cokół przestaje być listwą klipsowaną, front szuflady przejmuje jego rolę — do uzgodnienia z linią cokołu na ciągu A.

---

## 3. UJĄĆ / SCALIĆ

### U-01. Trzy blendy-widma z szablonu `"narozna"` — do usunięcia z zamówienia

`_formatki.py` linie 69–71 dokładają każdemu narożnikowi front 446×716 **i** blendę ślepą 430×716. W liście występują 3 razy (DA1, RL1, DC1) = **6 formatek frontowych, z których ani jedna nie ma poprawnego wymiaru**:

| Element w liście | Wymiar w liście | Wymiar wg PLAN v3.12a | Status |
|---|---|---|---|
| DA1 — front | 446×716 | **236×716** (front 240 − fugi) | zły wymiar |
| DA1 — blenda ślepa | 430×716 | brak — lico 0→610 zamyka osobna `Blenda dolna A 610×756` | **do usunięcia** |
| RL1 — front | 446×716 | front 600 dzielony: drzwi 296×716 + 3 fronty szuflad | zły wymiar i zła liczba |
| RL1 — blenda ślepa | 430×716 | **572×716** (blenda 0→576) | zły wymiar |
| DC1 — front | 446×716 | **341×716** (front 345 − fugi) | zły wymiar |
| DC1 — blenda ślepa | 430×716 | brak — lico 0→600 stoi za korpusem zmywarki, niewidoczne | **do usunięcia** |

### U-02. Panel ryflowany liczony jako płyta Korner — podwójny zakup

`FORMATKI-ROBOCZE.md` poz.: „Panel ryflowany ramienia **(lamele — dostawca zewn.)** | 1176×910 | ciemny orzech mat". Element kupowany u innego dostawcy, a jego **1,07 m² wchodzi do sumy „ciemny orzech mat"** (`_formatki.py::add()` sumuje bezwarunkowo). Zamawiając płytę wg tej tabeli kupisz 1,07 m² orzecha, którego nie użyjesz.

### U-03. Nakładka blatów w dwóch narożnikach — ~1,27 mb nadmiaru

Docinki: A 1950×635, B 2389×635, C1 947×635, ramię 545×500. Blat A biegnie po x0–635 na całej długości y, blat B po y0–635 na całej długości x — **narożnik A/B (635×635) jest w obu**. To samo w narożniku B/C1. Deklarowane łączenia: 3, ale żaden docinek nie jest skrócony o szerokość sąsiada.
**Rachunek:** suma docinków 1950 + 2389 + 947 + 545 = **5831 mm = 5,83 mb**; nadmiar 2 × 635 = **1,27 mb**; netto ≈ **4,56 mb**.
To nie jest błąd krytyczny (nadmiar = zapas na docinanie), ale musi być zadeklarowany jako zapas, a nie ukryty w wymiarach — przy zamówieniu **w każdym narożniku jeden element trzeba skrócić o 635**.

### U-04. C2 słupek — cargo ALBO półki, teraz jest jedno i drugie

BOM okucia: „Cargo spiżarniane wysokie do słupka 280 | 1 kpl | **[DO WERYFIKACJI]** — szerokość niestandard.". Formatki: „C2 słupek cargo — półki | 243×560 | **2**".
- Jeśli cargo: 2 półki są zbędne, a **fronty 276×1300 i 276×1070 montuje się do kosza cargo, nie na zawiasach** — czyli z 36 zawiasów odpada 6.
- Jeśli półki: 2 półki na korpus wysokości 2378 to poziomy co ~790 mm. Do spiżarni potrzeba **5–6 półek**.

Dodatkowo: światło korpusu 280 − 36 = **244 mm**. Cargo spiżarniane w katalogach Rejs/Peka występuje w nominałach 150 / 200 / 300 / 400 — **244 to nie jest nominał**. Ryzyko „produkt nie istnieje" jest realne, a BOM sam to sygnalizuje `[DO WERYFIKACJI]` od v3.5 i nikt tego nie zamknął.

### U-05. GA2 180 — moduł o najgorszym stosunku nakładu do pojemności

Światło 180 − 36 = 144 mm; 2 półki 143×300 → 3 poziomy 144 × 300 × ~320 ≈ **19,5 l użytkowe**. Koszt: 2 boki 400×998, 2 wieńce, plecy, front 176×996, 2 półki, 3 zawiasy, 2 zawieszki — pełny komplet szafki.
**Nie da się scalić z GA1**, bo GA1 ma głębokość **245** (wisi na licu pilastra: 155 + 245 = 400), a GA2 pełne **400** — to dwa różne korpusy, a nie jeden z uskokiem pleców.
**Warunek scalenia istnieje i jest niezamknięty:** PLAN pkt 11.11 `[?]` — *„ile centymetrów ma uskok WZDŁUŻ ściany (67 wg szkicu, czy cała długość ściany?)"*. Jeśli pomiar wykaże, że pilaster idzie całą ścianą A, to GA2 też siada na jego licu (gł. 245) i **GA1 + GA2 scalają się w jeden moduł 850×998×245** — mniej formatek, jeden front dzielony. **Decyzję o GA2 trzymać do pomiaru 11.11.**

### U-06. Zawiasy 155° do DC1 — pozycja znika przy zmianie Z-02

Jeśli DC1 przechodzi na szuflady zewnętrzne (§4, Z-02), odpada „Zawiasy 155° 2 szt" i front drzwiowy.

---

## 4. ZMIENIĆ

### Z-01. RL1: drzwi 300 + szuflady 300 → **3 szuflady 600** `[REKOMENDACJA, z kosztem]`

**Liczba, która to uzasadnia: w całej kuchni nie ma ani jednej szuflady szerszej niż 345 mm.** Zestawienie wszystkich frontów szufladowych v3.12a:

| Szuflada | Szerokość frontu | Głębokość | Przeznaczenie wg 5a |
|---|---|---|---|
| RL1 × 3 | 300 | 460 | sztućce, przybory, pojemniki |
| DA2 × 1 | 596, ale wysokość **110** | 560 | blachy/formy |
| DC1 × 2 (wewnętrzne) | ~300 | 546 | sztućce zapasowe |

Garnki i patelnie idą do 248 l (DA1) i 202 l (pod ramieniem) — obie strefy z dostępem sięgiem na 600 / 576 mm.

**Propozycja:** cały front 600 na ramieniu jako 3 szuflady 600 (światło skrzynki ~530 × 420 mm — mieści garnek 24 cm z pokrywką i patelnię 28 cm rączką w bok).
**Koszt zmiany, wprost:** znika drzwi 300 = **znika jedyny dostęp do 202 l pod ramieniem**. Ta przestrzeń staje się trwale zamknięta.
**Rachunek decyzji:** 3 szuflady 600×460 dają ~120 l w pełnym wysuwie, na wysokości chwytu, przy strefie gotowania. Zamiana: 202 l magazynu z gardzielą 300 mm ↔ 120 l pełnego dostępu. Rekomendacja: zamiana, o ile inwestor nie wskaże konkretnego sprzętu wielkogabarytowego, który ma tam zamieszkać na stałe. **Decyzja inwestora — v3.12 dodało te drzwi celowo, więc jej nie odwracam samodzielnie.**

### Z-02. DC1: drzwi 345 + 2 szuflady wewnętrzne → **3 szuflady zewnętrzne 345×546**

**Powód geometryczny (nowy, nie ma go w PLANie):** uskok lica 54 mm z §1.4 zabiera zawias od strony południowej. Zawias musi być od północy, na y=600. Skrzydło otwarte na 90° zajmuje wtedy pas x1655–2000 w płaszczyźnie y=600 — czyli **stoi dokładnie przed frontem zmywarki** (DB2: x1550–2000, lico y=600). Nie da się mieć otwartej zmywarki i otwartej DC1 jednocześnie. A PLAN pkt 5a przypisuje DC1 właśnie „sztućce (1 krok od zmywarki)" — funkcję używaną w trakcie rozładunku zmywarki.

`_kontrola.py::k3_otwieranie` tego nie łapie: sprawdza pas 50 mm przed licem w stanie zamkniętym oraz wychył skrzydła względem brył — zmywarka jest bryłą **za** płaszczyzną obrotu, więc test przechodzi. Kolizja jest czasowa (dwa fronty otwarte naraz), a takiego testu nie ma.

**Zmiana:** 3 szuflady frontowe 345 szer. × 546 gł. (prowadnica nom. 500 ≤ 546 ✓), bez drzwi. Zero wychyłu skrzydła, zero kolizji ze zmywarką.
**Koszt:** narożnik północny **236 l przestaje być osiągalny w ogóle** (dziś: sięg ręką obok wysuniętych szuflad wewnętrznych). Zysk: 3 szuflady w miejscu, gdzie się rozładowuje zmywarkę.

### Z-03. GC1 470 → 500, GC2 477 → 447

Patrz D-03. 500 + 447 = 947 ✓. Bez tej zmiany pozycja „ociekarka" z pkt 5a jest niewykonalna (światło 434 < ~460).

### Z-04. Zamiana zawartości DB0 ↔ GA2 — bezkosztowa

PLAN 5a: DB0 cargo 150 = *„przyprawy w butelkach, oleje, ocet"*; GA2 180 = *„herbaty, kawa, cukier"*.
**Rachunek odległości:** płyta indukcyjna to `PLYTA = (864, 1436)` na ciągu A (x0–560). DB0 stoi na x600–750, y0–600 → środek (675, 300). Środek płyty (280, 1150). Dystans ≈ √(395² + 850²) ≈ **938 mm**, i to w poprzek wnętrza U. GA2 wisi na y670–850, czyli **bezpośrednio nad północną krawędzią płyty**.
Przyprawy używane przy gotowaniu należą do GA2 (0 kroków), a wysokie butelki oleju i octu — do cargo (cargo 150 jest zaprojektowane pod wysokie butelki, światło 114 mm). Dziś jest odwrotnie.

### Z-05. Wysokość korpusów dolnych: PLAN mówi 820, formatki tną 720

PLAN pkt 5 podaje w kolumnie wymiarów **×820×** dla DA1, DA2, RL1, DB0, DB1, DB2, DC1 (7 wierszy). `_formatki.py` i cała lista formatek używają **720** (boki 405×**720**, 560×**720**, 460×**720** …).
**Kontrola arytmetyczna:** blat 910 `[P]` = cokół 150 + korpus 720 + blat 38 = **908** ✓ (nóżki regulowane domykają 2 mm). Z korpusem 820: 150 + 820 + 38 = **1008** ✗, o 98 mm powyżej decyzji `[P]`.
**Wniosek: 720 jest poprawne, „820" w PLAN pkt 5 to wartość-widmo** (najpewniej katalogowa nisza 720 + 100 cokołu). Do usunięcia z PLANu, bo w dokumencie oddawanym do cięcia dwie różne wysokości korpusu to gotowy błąd wykonawczy.

**Wyjątek, który trzeba obsłużyć osobno:** w wierszu DB2 „820" znaczy co innego — *„światło wnęki 450×820+"*, czyli nisza zmywarki. Ale w tej kuchni nisza pod blatem ma **150 (cokół) + 720 (korpus) = 870 mm**, nie 820. Zmywarki 45 cm regulują się zwykle w zakresie ~815–875, więc 870 jest na górnej granicy. **Do sprawdzenia w karcie konkretnej zmywarki przed zamówieniem frontu 446×713.** Model zmywarki: `[BRAK DANYCH]`.

### Z-06. Głębokości — trzy dokumenty, trzy liczby dla tych samych modułów

| Moduł | PLAN pkt 5 | `_formatki.py` | `_kontrola.py` | Co przyjąć |
|---|---|---|---|---|
| DC1 | gł. **546** | bok **560**, dno 864×560 → korpus **900** szer. | x2000→2546 = **546** gł., y0→945 = **945** szer. | 546 × 945 |
| C2 | gł. **580** | bok 580 | x1946→2546 = **600** | `[DO ROZSTRZYGNIĘCIA]` |
| DA1 | gł. **405** | 405 | x155→560 = **405** ✓ | 405 |
| Ramię | gł. **500** (blat) | korpus **460** | — | korpus 460, blat 500 ✓ |

Do tego blaty: docinki są **635 głębokie** przy korpusach 560 (ciąg A → wysięg **75 mm**), 600 (ciąg B → 35 mm ✓) i 546 (DC1 → wysięg **89 mm**). Typowy wysięg blatu to 20–40 mm. Przy 75–89 mm blat na ciągu A i nad DC1 wystaje przed fronty na tyle, że **zbiera kapiącą wodę na fronty i koliduje z otwieraniem drzwi piekarnika w DA2**. Do przeliczenia po ustaleniu jednej głębokości korpusu na ciąg.

### Z-07. C2 słupek — 2378 + 150 nóżek = 2528 > sufit 2478

`FORMATKI-ROBOCZE.md` nagłówek: *„wysokości korpusów: dolne 720 (nóżki 150), górne 998, **słupek 2378**"*. PLAN pkt 6: *„Góra zabudowy 2478 — górne A, **słupek C2**, nadstawka C4 — wszystko do sufitu"*.
**Rachunek:** 150 + 2378 = **2528 mm**, czyli **50 mm powyżej sufitu 2478 `[P]`**. Korpus 2378 domyka się do sufitu tylko przy cokole **100 mm** (100 + 2378 = 2478 ✓) — a cała reszta kuchni stoi na 150.
**Do wyboru:** (a) słupek 2328 na nóżkach 150 (spójna linia cokołu), (b) słupek 2378 na cokole 100 (uskok w linii cokołu, widoczny). Dziś w dokumencie jest wariant niemożliwy.

### Z-08. Ciąg B: rzut w PLAN pkt 3 pokazuje inny układ niż rozpiska w pkt 5

Rzut ASCII, PLAN pkt 3:

```
▓pilaster│crg│ ZMYW │  ZLEW 80  │DB3│ DC1+GC1-2│
▓15,5×67 │15 │  45  │ pod oknem │~39│ narożna  │
```

Rozpiska, PLAN pkt 5 (v3.3): martwe pole | cargo 15 (600→750) | **zlew 80 (750→1550)** | **zmywarka 45 (1550→2000)**.

Rzut ma **zmywarkę po zachodniej stronie zlewu** (przed nim), rozpiska po wschodniej. To dokładnie ta zamiana, którą v3.3 opisuje jako korektę — rzut jej nie przyjął. Do tego rzut zawiera moduł **`DB3 ~39`**, którego **nie ma w żadnej rozpisce, w `_formatki.py` ani w `_kontrola.py`**. I rzut ma jeszcze **„DA1 45"**, czyli szerokość sprzed v3.9/v3.10.

To nie jest kosmetyka: pkt 7 (AGD) odwołuje się do nieistniejącego DB3 **dwa razy** — *„Zmywarka 45 | DB2 | przyłącza z **DB3**"* oraz *„Zlew + bateria | **DB3**"* — a pkt 8.3 raz: *„przedłużenie do **DB3** w cokole"*. Instalator dostanie polecenie doprowadzenia wody do modułu, który nie istnieje. Poprawnie: **DB1**.

### Z-09. Pkt 7 (AGD): okap przypisany do GA2 zamiast GA3

PLAN pkt 7: *„Okap | **GA2** | recyrkulacyjny…"*. PLAN pkt 5: *„GA3 | **okap w zabudowie** | 600×998×400 | nad DA2 = 850→1450"*. Historia v3.7a naprawiła numerację w pkt 5 (*„okap to GA3 (600, nad DA2), a nie GA2"*), ale **pkt 7 został z GA2**. GA2 to szafka 180 mm — okap 600 się w niej nie mieści.

### Z-10. DA1: korpus wisi 155 mm od ściany na odcinku 180 mm — brak elementu

Pilaster ma 67 cm długości `[P]`, czyli kończy się na y=670. Korpus DA1 to x155→560, y0→**850**. Na odcinku y670→850 ściana A cofa się na x=0, a plecy DA1 zostają na x=155 → **155 mm pustki za plecami na długości 180 mm**. Brak w projekcie klocków dystansowych / listwy przyściennej dla tego odcinka. Bez nich plecy DA1 i mocowanie do ściany nie mają na czym usiąść.

---

## 5. WERYFIKACJA PLANU FUNKCJONALNEGO (PLAN pkt 5a)

### 5.1 Czy każda funkcja ma moduł

| Funkcja (wg zakresu audytu) | Moduł w 5a | Okucie/wkład w BOM | Werdykt |
|---|---|---|---|
| **Sztućce** | RL1, górna szuflada 300 | **Wkład na sztućce 300 — 1 szt ✓** | ✓ OK. K9 wymaga ≥250, front 300 ✓ |
| **Kosz segregacji** | DB1 zlew 80 | **BRAK** | ✗ **funkcja opisana, okucie niekupione** (D-02) |
| **Przyprawy** | DB0 cargo 150 | Cargo 150 ✓ | ~ jest, ale 938 mm od płyty (Z-04) |
| **Naczynia codzienne** | GC1 (talerze + ociekarka), GC2 (szklanki, kubki) | **Ociekarka BRAK**; GC1 470 za wąska na standardowy wkład | ✗ (D-03, Z-03) |
| **Garnki** | DA1 — 248 l | — | ~ przestrzeń jest, dostęp przez 240 mm na 600 mm głębokości |
| **Blachy / formy** | DA2 szuflada dolna (front 596×**110**) + pod ramieniem | prowadnica nom. 500 ✓ | ~ szuflada 110 wys. mieści blachy płasko ✓; reszta w ślepej strefie |
| **Chemia** | DB1 (razem z koszem i syfonem) | — | ~ trzy funkcje w jednej szafce 800 z syfonem w środku |
| **Zapasy suche** | C2 słupek 280 | Cargo spiżarniane `[DO WERYFIKACJI]`, światło 244 mm ≠ nominał katalogowy | ✗ ryzyko braku produktu (U-04) |
| **Sprzęt AGD drobny** (czajnik, toster, mikser) | **BRAK WIERSZA** | — | ✗ **funkcja nieprzypisana** |
| Mikrofalówka | brak | — | `[BRAK DANYCH]` — projekt nigdzie nie mówi, czy inwestor ją ma. Do zapytania. |

**Sprzęt AGD drobny — rozwinięcie.** Nie ma modułu ani nawet wiersza w 5a. Blat, na którym można to postawić, istnieje: narożnik północno-zachodni x155–600 × y0–600 (nad ślepym korpusem DA1) to **445 × 600 mm wolnego blatu**, jedyny odcinek blatu w kuchni nieprzypisany do zlewu, zmywarki ani płyty. Warunek: gniazdo. PLAN pkt 8.1 mówi ogólnie *„2–3 nad blatem B/A (≥600 od zlewu)"* — bez lokalizacji. **Do zapisania w 5a jako „strefa śniadaniowa/AGD drobne" + jedno gniazdo podwójne przypisane do tego narożnika**, inaczej ta decyzja nie przetrwa do etapu elektryki.

### 5.2 Czy 5a opisuje moduły, które nie istnieją

Przeszedłem wszystkie 15 wierszy 5a przeciw `_formatki.py::MODULES`:

- **Wszystkie 15 wierszy 5a wskazują na istniejące moduły** ✓ — v3.12 rzeczywiście wyczyściła wiersze-widma (deklaracja z historii: *„usunięte wiersze opisujące moduły, których już nie ma"* — potwierdzam, jest wykonana).
- **Ale 5a ma 15 wierszy przy 15 modułach + 1 wierszu o narożniku B — a mimo to jednego modułu brakuje.** Wiersze 5a pokrywają: GC1, GC2, DB0, DB1, DB2, narożnik zachodni B, DC1, C2, C3/C4, DA1, DA2, GA1, GA2, GA3, RL1.

> ### ✗ **GA4 (500×998×400) nie ma żadnego przypisania funkcjonalnego.**
> Moduł istnieje w PLAN pkt 5 (*„GA4 | górna | 500×998×400 | półki | 1450→1950, nad ramieniem"*), w `_formatki.py` linia 24, w `_kontrola.py::GORNE_A` i w liście formatek (5 pozycji: boki, wieńce, plecy, front, półki). W planie funkcjonalnym — nie ma go.
> To ~**0,20 m³ ≈ 200 l** zabudowy bez odpowiedzi na pytanie „co tam wchodzi".
>
> **Potwierdzenie z drugiego źródła:** BOM okucia, pozycja „Zawieszki regulowane górnych + listwa montażowa | **10 szt** + 3 mb | **GA1-3, GC1-2**" — GA4 pominięta również tutaj. Górnych jest **6** (GA1, GA2, GA3, GA4, GC1, GC2) → potrzeba **12 zawieszek**, nie 10. GA4 wypada z dokumentu konsekwentnie w dwóch niezależnych miejscach.

**Rekomendacja dla GA4:** to najlepsze miejsce na naczynia rzadkie / zapasy lekkie (nad ramieniem, dół 1480 — nad blatem ramienia, więc podchodzi się do niej bokiem, nie przez strefę roboczą). Alternatywnie: przy zmianie Z-01 i D-01 przenieść tam to, co dziś jest w 248-litrowej ślepej DA1.

### 5.3 Funkcje, których 5a nie obejmuje w ogóle

Bez werdyktu „błąd" — do decyzji inwestora, ale każda z nich potrzebuje miejsca i dziś go nie ma: deski do krojenia (przegroda pionowa), worki/folie/ręcznik papierowy, taca/pieczywo, ładowarki/dokumenty, **środki czystości wysokie (mop, szczotka)** — w kuchni bez pomieszczenia gospodarczego zwykle trafiają do słupka, a C2 (280, światło 244) ich nie pomieści.

---

## 6. TABELA BOM

Kolumna **„jest w dokumencie"** dotyczy `FORMATKI-ROBOCZE.md` (formatki + tabela okuć). Kolumna „ilość wg audytu" to moje przeliczenie z listy formatek R1 — **przed korektami z §3–§4**, chyba że napisano inaczej.

### 6.1 Płyty i formatki

| Poz. | Pozycja | W dokumencie | Ilość w dokumencie | Ilość wg audytu | Uwaga |
|---|---|---|---|---|---|
| P-01 | Płyta korpusowa „kremowy" | **TAK** | 19,9 m² netto / 22,9 z zapasem | ≈ 19,9 (z błędnymi DC1 900×560 i DA1) | do przeliczenia po korektach wymiarów |
| P-02 | HDF biały 3 mm (plecy) | **TAK** | 6,5 / 7,4 m² | 6,5 | 13 pleców; DB1 celowo bez pleców (listwa serwisowa) ✓ |
| P-03 | Front „ciemny orzech mat" | **TAK** | 6,3 / 7,2 m² | **3,20 / 3,7 m²** | −0,34 (fronty C4 → antracyt) −1,69 (bok lodówki → antracyt) −1,07 (panel ryflowany = dostawca zewn., U-02) |
| P-04 | Front „beż/kaszmir mat" | **TAK** | 3,3 / 3,8 m² | do przeliczenia | zawiera 3 błędne fronty i 3 blendy-widma (U-01); po korekcie dojdą fronty szuflad RL1/DC1 |
| P-05 | **Płyta „antracyt mat" (RAL 7016)** | **NIE** | — | **2,20 m² netto / 2,53 z zapasem** | PLAN pkt 10 `[P]`: *„zabudowa lodówki (nadstawka C4 + bok przy ściance): antracyt mat"*. Dekoru **nie ma w tabeli płyt**: C4 fronty 2×(327×524)=0,343 + bok 2478×680=1,685 + blenda dystansowa 70×2478=0,173 |
| P-06 | Płyta „czarny mat" (cokół) | **TAK** | 0,8 / 0,9 m² (5000×150) | **~0,95 m² (6,3 mb)** | patrz A-03 |
| P-07 | **Dna szuflad (6 szt)** | **NIE** | — | 6 szt wg systemu | D-05 |
| P-08 | **Fronty szuflad RL1 (3) i DC1 (2)** | **NIE** | — | 5 szt | D-05 |
| P-09 | **Blenda ślepa ramienia 572×716** | **NIE** (jest widmo 430×716) | — | 1 szt | U-01 |
| P-10 | **Panel boczny ramienia ~500×910** | **NIE** | — | 1 szt | D-04 |
| P-11 | Blenda dystansowa lodówka–ścianka ~70×2478 | **TAK**, ale w tabeli okuć | 1 szt | 1 szt | element płytowy zapisany jako okucie → **nie wchodzi do żadnej sumy m²** |
| P-12 | **Klocki dystansowe za plecami DA1 (155 × 180)** | **NIE** | — | `[do policzenia po pomiarze 11.11]` | Z-10 |
| P-13 | **Fronty — zestawienie zbiorcze (szt + m²)** | **NIE** (brak podsumowania) | — | **21 szt / 6,34 m²** wg listy R1; po korektach **≈ 26–28 szt** | audyt policzył z tabeli formatek |

### 6.2 Obrzeże

| Poz. | Pozycja | W dokumencie | Ilość w dokumencie | Ilość wg audytu | Uwaga |
|---|---|---|---|---|---|
| O-01 | **Obrzeże ABS 1,0 mm (fronty, elementy widoczne)** | **NIE — brak sumy w mb** | kolumna per formatka, zero podsumowania | **≈ 59 mb netto → ~65 mb z zapasem** | policzone z obwodów wszystkich formatek oznaczonych „1,0" |
| O-02 | **Obrzeże ABS 0,4 mm (korpusy, krawędź przednia)** | **NIE — brak sumy w mb** | j.w. | **≈ 52 mb netto → ~58 mb z zapasem** | j.w., pozycje „0,4 przód" |
| O-03 | **Obrzeże do przyciętych krawędzi blatu (38 mm)** | **NIE** | — | ≥ 3 mb (końce docinków + krawędzie przy ścianach) | blaty docinane na miejscu; krawędź laminatu musi być zamknięta |

> Dostawca obrzeży: PLAN i dostawcy.md wskazują **Korner (podłogi, korner.eu)** dla obrzeży ABS/PVC i profili blatowych — **inna firma niż Korner (płyty, korner.pl)**, u którego zamawiany jest rozkrój. Przy zamówieniu z oklejaniem u korner.pl obrzeże jest w usłudze; przy docinkach na miejscu trzeba dokupić rolkę osobno. Nie jest to w dokumencie rozstrzygnięte.

### 6.3 Blaty

| Poz. | Pozycja | W dokumencie | Ilość w dokumencie | Ilość wg audytu | Uwaga |
|---|---|---|---|---|---|
| B-01 | Docinki blatu laminat 38 | **TAK** | 4 szt: 1950×635, 2389×635, 947×635, 545×500 | 4 szt, ale 2 do skrócenia o 635 | U-03; suma 5,83 mb, netto ~4,56 mb |
| B-02 | **Jednostka zakupu (płyta blatowa 4100×635)** | **NIE** | — | **2 szt** | 2389 + 1950 = 4339 > 4100 → nie zmieszczą się w jednej płycie; C1 947 i ramię 545 z odpadów (4100−2389=1711 ✓, 4100−1950=2150 ✓) |
| B-03 | Wycięcia: indukcja 560×490 `[P]`, zlew wg szablonu | **TAK** | 2 | 2 | zlew: model `[BRAK DANYCH]` → szablonu jeszcze nie ma |
| B-04 | Śruby łącznikowe blatu | **TAK** | 3 kpl | 3 kpl ✓ | zgadza się z 3 łączeniami |
| B-05 | **Listwa przyblatowa (profil przyścienny)** | **NIE** | — | **≈ 5,3 mb** (ciąg A 1950 + B 2391 + C1 947) | plan montażu krok 10 wymienia „listwy przyblatowe", BOM ich nie ma; asortyment: korner.eu LB 15/23/37 |
| B-06 | **Listwy/zaślepki końcowe blatu** | **NIE** | — | 2–3 szt (koniec ramienia, koniec przy przejściu) | |
| B-07 | Wysięg blatu vs korpus | — | — | ciąg A **75 mm**, DC1 **89 mm**, ciąg B 35 mm | Z-06 — do przeliczenia |

### 6.4 Okucia

| Poz. | Pozycja | W dokumencie | Ilość w dokumencie | Ilość wg audytu | Uwaga |
|---|---|---|---|---|---|
| K-01 | Zawiasy puszkowe 110° | **TAK** | 36 szt (z zapasem 10 %) | ~32 + zapas ✓ | zgodne; **−6 jeśli C2 idzie na cargo** (U-04) |
| K-02 | Zawiasy 155° (DC1) | **TAK** | 2 szt | 2 lub **0** | znikają przy Z-02 |
| K-03 | Prowadnice metal-box nom. 400 (RL1) | **TAK** | 3 kpl | 3 kpl | nominał ≤ 460 gł. korpusu ✓; `[do potwierdzenia w karcie]` — zapis jest w dokumencie ✓ |
| K-04 | Prowadnice metal-box nom. 500 (DA2) | **TAK** | 1 kpl | 1 kpl | ≤ 560 ✓ |
| K-05 | Prowadnice metal-box nom. 450 (DC1) | **TAK** | 2 kpl | 2 kpl (lub 3 przy Z-02, nom. 500) | ≤ 546 ✓ |
| K-06 | Wkład na sztućce 300 | **TAK** | 1 szt | 1 szt ✓ | funkcja „sztućce" domknięta |
| K-07 | Cargo 150 (DB0) | **TAK** | 1 kpl | 1 kpl ✓ | nominał katalogowy ✓ |
| K-08 | Cargo spiżarniane do słupka 280 | **TAK** `[DO WERYFIKACJI]` | 1 kpl | **ryzyko: światło 244 ≠ nominał** | U-04, nierozstrzygnięte od v3.5 |
| K-09 | **Kosz segregacji** | **NIE** | — | **1 kpl** | D-02 — funkcja jest w 5a i w K9, okucia nie ma |
| K-10 | **Wkład ociekowy do GC1** | **NIE** | — | 1 kpl (po zmianie GC1 → 500) | D-03 |
| K-11 | Podnośnik frontu okapu | **TAK** | 1 kpl | 1 kpl | dobór po zakupie okapu — model okapu `[BRAK DANYCH]` |
| K-12 | Nóżki 150 + klipsy cokołu | **TAK** | 32 + 16 szt („8 szafek dolnych ×4") | **≈ 36 + 14** | korpusów na nóżkach jest **7** (DA1, DA2, RL1, DB0, DB1, DC1, C2), nie 8; ale RL1 (1176), DC1 (945) i DB1 (800) potrzebują po 6, nie 4 → 4+4+6+4+6+6+4 = **34**, +zapas 36 |
| K-13 | Zawieszki górnych + listwa montażowa | **TAK** | 10 szt + 3 mb („GA1-3, GC1-2") | **12 szt** + 2,9 mb ✓ | GA4 pominięta (§5.2) |
| K-14 | Kątowniki montażowe ramienia | **TAK** | 8 szt | 8 szt ✓ | |
| K-15 | Listwa gola / frez uchwytowy | **TAK** `[decyzja technologiczna]` | ~5 mb | **≈ 7,3 mb** | dolne 240+596+600+150+800+446+345 = **3177**; górne 670+180+600+500+470+477+280+280+660 = **4117**; razem **7294 mm**. Brak też profilu (alu/kolor), mocowania i zaślepek końcowych |

### 6.5 Montaż, uszczelnienia, drobnica

| Poz. | Pozycja | W dokumencie | Ilość w dokumencie | Ilość wg audytu | Uwaga |
|---|---|---|---|---|---|
| A-01 | Konfirmaty 7×50 | **TAK** | „1 opak." | **≈ 180 szt** (15 korpusów × ~12) | „1 opakowanie" (50–100 szt) to 2–4× za mało |
| A-02 | Kołki 8×35 | **TAK** | „1 opak." | ≈ 150 szt | j.w. |
| A-03 | Cokół (listwa) | **TAK** | ~5 mb | **≈ 6,3 mb** | ciąg A 1450 + front ramienia 1176 + ciąg B 2391 + ciąg C widoczne 1285 = 6302 mm; +kratka wentylacyjna lodówki |
| A-04 | Wkręty 4×30 / 4×16 | **TAK** | „1 opak. każde" | ≈ 300+ (same plecy HDF) | 13 pleców × ~25 wkrętów |
| A-05 | **Zaślepki do konfirmatów / otworów** | **NIE** | — | ≈ 100 szt w kolorze korpusu | |
| A-06 | Silikon | **TAK** | 1 szt | 2 szt (sanitarny + do blatu) | |
| A-07 | Silikorner (uszczelka cokołu, korner.eu) | **TAK** | 1 szt | 1 szt ✓ | |
| A-08 | **Taśma uszczelniająca pod blat / do zlewu** | **NIE** | — | 1 rolka | |
| A-09 | **Taśma aluminiowa antyparowa nad zmywarką** | **NIE** | — | 1 rolka | standard przy zmywarce pod blatem laminowanym — bez niej para rozwarstwia blat |
| A-10 | **Klej montażowy** | **NIE** | — | 1–2 szt | panele, blendy, listwy |

### 6.6 Oświetlenie

| Poz. | Pozycja | W dokumencie | Ilość w dokumencie | Ilość wg audytu | Uwaga |
|---|---|---|---|---|---|
| L-01 | Taśma LED 3000K | **TAK** | ~3 mb | **2,9 mb** ✓ | GA1-4 (1950) + GC1-2 (947) = 2897 mm ✓ |
| L-02 | Profil alu | **TAK** | ~3 mb | 2,9 mb ✓ | typ (wpuszczany/natynkowy) i kolor `[BRAK DANYCH]` |
| L-03 | Zasilacz 24 V | **TAK** | 1 szt | 1 szt, **moc ≈ 36 W** | dokument nie podaje mocy; wzór z formatki.md: długość × W/m × 1,2 |
| L-04 | **Włącznik / czujnik / przewód / złączki** | **NIE** | — | 1 kpl | PLAN pkt 8.1 przewiduje „zasilanie LED (transformator w GA)", BOM nie ma sterowania |

### 6.7 AGD i sanitarne — poza BOM dokumentu

| Poz. | Pozycja | W dokumencie | Status |
|---|---|---|---|
| G-01 | Indukcja Bosch PXE601DC1E | **TAK** (pkt 7) | `[P]` — wycięcie 560×490 `[P]` ✓ |
| G-02 | Okap recyrkulacyjny | **TAK** (pkt 7) | `[P]` zakup inwestora, **model `[BRAK DANYCH]`** — a GA3 ma już wycięty front uchylny 596×400 i przypisany podnośnik |
| G-03 | Piekarnik | **TAK** (pkt 7) | **model `[BRAK DANYCH]`** — a nisza 560×590–600 i trawers nośny 564×560 są już w formatkach |
| G-04 | Zmywarka 45 | **TAK** (pkt 7) | **model `[BRAK DANYCH]`**; nisza deklarowana 820, realna **870** (Z-05) |
| G-05 | Lodówka 60×65×190 | **TAK** | `[P]` ✓ |
| G-06 | **Zlew 1-komorowy z ociekaczem + bateria** | **wymienione w pkt 7/10, brak w BOM** | model `[BRAK DANYCH]` → brak szablonu wycięcia w blacie B |
| G-07 | **Syfon, wąż, zawory kątowe, przedłużenie odpływu** | **NIE** | pkt 8.3 mówi o przedłużeniu podejść „w cokole/za korpusami" — materiału nie ma w BOM |

---

## 7. Zestawienie liczbowe audytu

| Kategoria | Liczba |
|---|---|
| Modułów szafkowych w projekcie | **15** |
| Ciągów z domkniętym licem (`k7` PASS) | **5 / 5** |
| Niezagospodarowanych odcinków lica dolnego | **0** (wszystkie 6 ślepych odcinków = świadome blendy, 3277 mm = 44 % lica) |
| Niezagospodarowanych odcinków ściany w pasmie górnych | **2** (ściana B: 538 mm i 352 mm) |
| Objętość dostępna tylko sięgiem przez otwór < 350 mm | **686 l** |
| Modułów bez przypisania funkcjonalnego w 5a | **1** (GA4) |
| Funkcji obowiązkowych bez okucia w BOM | **2** (kosz segregacji, ociekarka) |
| Funkcji bez modułu | **1** (sprzęt AGD drobny) |
| Pozycji BOM: **NIE ma w dokumencie** | **19** |
| Pozycji BOM: jest, ale ilość zaniżona/błędna | **9** |
| Formatek do usunięcia (widma) | **2** (blendy ślepe DA1, DC1) |
| Formatek z błędnym wymiarem | **4** (fronty DA1, RL1, DC1; blenda ślepa RL1) |
| Formatek brakujących | **≥ 13** (6 den + 5 frontów szuflad + blenda ramienia + panel boczny ramienia) |
| Odwołania do nieistniejącego modułu DB3 | **3** (pkt 3 rzut, pkt 7 ×2, pkt 8.3) |
| Sprzeczności wymiarowych PLAN ↔ formatki | **4** (wys. korpusu 820/720, gł. DC1 546/560, szer. DC1 945/900, gł. C2 580/600) |

---

## 8. Kolejność działań

1. **Zanim cokolwiek — przeliczyć `_formatki.py` na v3.12a.** Lista formatek opisuje v3.5. Dopóki tego nie ma, żadna liczba m²/mb w BOM nie jest wiążąca.
2. Zamknąć pomiar **11.11 (pilaster)** — od niego zależy GA1/GA2 (U-05) i klocki za DA1 (Z-10).
3. Rozstrzygnąć **uskok lica ciągu C 54 mm** (§1.4) — od niego zależy Z-02.
4. Kupić modele: **piekarnik, zmywarka, okap, zlew** — cztery nisze/wycięcia są już zaprojektowane bez kart.
5. Dopisać do PLANu: **GA4 do 5a**, **strefa AGD drobne**, **dekor antracyt do tabeli płyt**, poprawić **DB3 → DB1** (3 miejsca) i **okap GA2 → GA3**.
6. Dopiero potem zamówienie w KornerGo.

**Projekt nadal wymaga weryfikacji pomiarem na miejscu przed produkcją/cięciem mebli.**
