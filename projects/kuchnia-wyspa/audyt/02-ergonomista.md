# Audyt 02 — ERGONOMIA UŻYTKOWANIA

Projekt: **kuchnia-wyspa v3.12a** (kuchnia w U + ramię L)
Data audytu: 2026-08-13
Rola: ergonomista. Praca niezależna — nie widziałem raportów pozostałych audytorów.
Kontekst użytkownika przyjęty z zadania: **wzrost 182 cm, gotuje jedna osoba, wykonanie samodzielne**.

---

## 0. Inwentaryzacja wczytanych plików

| # | Plik | Rozmiar / zakres | Co z niego wziąłem |
|---|---|---|---|
| 1 | `projects/kuchnia-wyspa/PLAN.md` | 265 linii, v3.12a | historia decyzji, tabela wymiarów (pkt 2), rzut ASCII (pkt 3), tabela przejść (pkt 4), rozpiska modułów (pkt 5), plan funkcjonalny (pkt 5a), rozpisanie pionowe (pkt 6), AGD (pkt 7), ryzyka (pkt 9), pkt 9a, pkt 11a |
| 2 | `projects/kuchnia-wyspa/FORMATKI-ROBOCZE.md` | 146 linii, nagłówek **„kuchnia v3.5 (WERSJA ROBOCZA R1)"** | formatki, wymiary blatów, lista okuć, plan montażu |
| 3 | `projects/kuchnia-wyspa/_kontrola.py` | 393 linie | **model geometryczny — jedyne źródło współrzędnych w mm**; 9 kontroli K1–K9; uruchomiony: `PASS — 9 kontroli, 0 błędów, 0 uwag`; `--regresja`: 5/5 |
| 4 | `projects/kuchnia-wyspa/_schemat.py` | 322 linie | opisy na rysunku (m.in. „≥55 okap–indukcja", „ramię L ~118×50, wys. 91") |
| 5 | `skills/zabudowa-na-wymiar/SKILL.md` | 113 linii | twarde zasady bezpieczeństwa (pkt 4–7 sekcji „Twarde zasady") |
| 6 | `skills/zabudowa-na-wymiar/references/uklady-kuchni.md` | 74 linie | **główne źródło norm**: progi układów, strefy §3, komunikacja §4 |
| 7 | `skills/zabudowa-na-wymiar/references/protokol-weryfikacji.md` | — | zakres kontroli K1–K9, zasada „jedno źródło prawdy" |
| 8 | `skills/zabudowa-na-wymiar/references/analiza-pomieszczenia.md` | — | statusy `[P]/[~]/[?]` |
| 9 | `skills/zabudowa-na-wymiar/references/technologia-wykonania.md` | — | blendy, szczeliny, pomiary kontrolne |
| 10 | `skills/zabudowa-na-wymiar/references/dokumentacja-stolarz.md` | — | wymagana zawartość dokumentacji |
| 11 | `skills/zabudowa-na-wymiar/references/formatki.md` | — | „lista formatek WYŁĄCZNIE po pomiarach kontrolnych" |
| 12 | `skills/zabudowa-na-wymiar/references/zabudowy-inne.md` | — | (poza zakresem kuchni) |
| 13 | `skills/architekt-wnetrz/references/standardy-meble.md` | — | **siatka wysokości blatu, odstępy blat–górne, nisze AGD, strefy bezpieczeństwa, wysokości boków szuflad Blum** |

**Pliku `v1.md` nie ma — potwierdzam.** Nie odwoływałem się do niego.
Pliki `_formatki.py`, `_montaz*.py`, `_render.py`, `_widok3d.py`, `_detal_pilaster.py`, `PROMPTY-GPT.md` oraz PDF-y są w katalogu, ale poza zakresem ergonomicznym — nie analizowałem ich treści.

### 0a. Układ współrzędnych użyty w całym raporcie

Za `_kontrola.py` (linie 17–18): **origin = wewnętrzny narożnik ścian A/B; x → na wschód (do ściany C), y → na południe (do korytarza), wszystko w mm.**

Moduły z modelu (dosłownie z `_kontrola.py`, linie 51–78):

| Moduł | x0,y0 → x1,y1 | lico | front (od–do) | szer. frontu |
|---|---|---|---|---|
| DA1 narożna ślepa | 155,0 → 560,850 | E (x=560) | 610–850 | **240** |
| DA2 indukcja+piekarnik | 0,850 → 560,1450 | E | 850–1450 | 600 |
| RL1 ramię (drzwi 300 + szuflady 300) | 0,1450 → 1176,1950 | N (y=1450) | 576–1176 | 600 |
| DB0 cargo 15 | 600,0 → 750,600 | S (y=600) | 600–750 | 150 |
| DB1 zlew 80 | 750,0 → 1550,600 | S | 750–1550 | 800 |
| DB2 zmywarka 45 | 1550,0 → 2000,600 | S | 1550–2000 | 450 |
| DC1 narożna ślepa | 2000,0 → 2546,945 | W (x=2000) | 600–945 | **345** |
| C2 słupek cargo | 1946,945 → 2546,1225 | W | 945–1225 | 280 |
| C3 lodówka | 1946,1225 → 2546,1885 | W | 1225–1885 | 660 |
| GA1–GA4 (górne) | x 0/155 → 400, y 0→1950 | E | — | 670/180/600/500 |
| ŚCIANKA | 1776,1885 → 2546,1975 | — | — | — |
| PŁYTA (wycięcie) | y 864 → 1436 | — | — | 572 |

Pozostałe stałe: `SCIANA_C_X = 2546`, `LINIA_POLUDNIOWA = 1950`, `PROG_PRZEJSCIA = 600`, blat **910** `[P]`, dół górnych **1480**, sufit/góra zabudowy **2478**.

### 0b. Źródła norm użyte w raporcie

1. **`uklady-kuchni.md`** — normy własne projektu; progi opisane tam jako **TWARDY PRÓG** traktuję jako nieprzekraczalne (tak stanowi §wstęp tego pliku).
2. **`standardy-meble.md`** — siatka wysokości, odstępy, nisze AGD, strefy bezpieczeństwa.
3. **`SKILL.md` §Twarde zasady** — bezpieczeństwo płyty, lodówki, zmywarki.
4. Tam, gdzie oba pliki milczą (zasięg pionowy, podjazd na kolana przy barku, natężenie oświetlenia), podaję wartość jako **[praktyka]** albo **[antropometria]** i oznaczam to jawnie — nie udaję, że to norma projektu.

---

## 1. Co policzyłem sam (podstawa liczbowa zarzutów)

Wszystko poniżej wyliczone z modelu `_kontrola.py`, nie przepisane z PLAN.md.

**Trójkąt roboczy** (punkty: środek wycięcia płyty, środek modułu zlewowego, środek lica lodówki):

| Wariant | zlew–płyta | zlew–lodówka | płyta–lodówka | SUMA |
|---|---|---|---|---|
| komora zlewu w środku modułu (1150) | **1206** | 1486 | 1700 | **4392** |
| komora dosunięta na wschód (1325) | 1335 | 1400 | 1700 | 4436 |
| komora dosunięta na zachód (950) | **1073** | 1602 | 1700 | 4375 |
| komora w środku + realna głębokość lodówki 650+50 | 1206 | 1435 | 1603 | 4244 |

**Przejścia i strefy:**

| Wielkość | Wyliczenie | Wynik |
|---|---|---|
| przejście ramię ↔ ścianka | 1776 − 1176 | **600** |
| to samo przy ramieniu 1180 (PLAN §5 / FORMATKI) | 1776 − 1180 | **596** |
| strefa robocza front B ↔ ramię (blat 600) | 1450 − 600 | **850** |
| strefa robocza front B ↔ ramię (blat 635 wg FORMATKI) | 1450 − 635 | **815** |
| odległość lic frontów B ↔ RL1 | 1490 − 560 | 930 |
| korytarz front A ↔ front C2/C3 | 1946 − 600 | 1346 |
| korytarz front A ↔ lodówka przy realnej gł. 700 | 1846 − 600 | 1246 |
| przed otwartą zmywarką (do ścianki) | 1885 − 600 | 1285 |
| blat odstawczy na północ od płyty | 864 − 600 | 264 |
| blat odstawczy na południe od płyty | 1950 − 1436 | 514 |
| wolna głębokość blatu przed górnymi (400+19) | 600 − 419 / 635 − 419 | **181 / 216** |
| prześwit blat → dół górnych | 1480 − 910 | **570** |
| pas nad pewnym chwytem dla 182 cm | 2478 − ~2020 | **458** |

**Kolizje policzone (w rzucie):**

| Para | Nakładka |
|---|---|
| opuszczone drzwi piekarnika DA2 × wysunięta szuflada RL1 (400) | **243 × 400 mm** |
| otwarta zmywarka DB2 (front ~780) × ćwiartka wychyłu drzwi DC1 | **345 × 345 mm** |
| otwarte drzwi lodówki 90° × przejście 600 | zostaje **170 mm** (model) / **70 mm** (realna gł. lodówki) |

---

## 2. LISTA ZARZUTÓW

Format: `[KATEGORIA] tytuł | norma/zalecenie | w projekcie | dowód | konsekwencja | rekomendacja`

---

### 2.1. Strefy funkcjonalne (zapasy → przechowywanie → zmywanie → przygotowanie → gotowanie)

**[E01] [BŁĄD] Strefa PRZYGOTOWANIA fizycznie nie istnieje — między zlewem a płytą jest 150 mm blatu**
- **norma/zalecenie:** `uklady-kuchni.md` §3 pkt 4: *„Przygotowanie — główny blat roboczy: **min 600, optymalnie 900–1200** ciągłego blatu między zlewem a płytą"*.
- **w projekcie:** **150 mm** ciągłego, prostego blatu po stronie płyty (odcinek x 600→750, i to nad wysuwem cargo DB0). Dalej zaczyna się narożnik ślepy A/B. Po drugiej stronie zlewu: **450 mm** (x 1550→2000) — i ten odcinek leży nad zmywarką.
- **dowód:** `_kontrola.py`: `DB1 zlew 80 (750,0,1550,600)`, `DB0 cargo 15 (600,0,750,600)`, lico ciągu A na x=560, blat A do x=600. Między licem A a zachodnią krawędzią zlewu: 750 − 600 = 150. PLAN §5a nie przypisuje żadnemu modułowi funkcji „przygotowanie".
- **konsekwencja:** deficyt **450 mm wobec minimum 600** i **750–1050 mm wobec optimum**. Deska do krojenia 250×400 nie ma gdzie stanąć między zlewem a płytą. Realnie cały preparat przenosi się albo na narożnik A/B (nieosiągalny — E02), albo na ramię za plecami (obrót 180° od zlewu), albo na blat nad zmywarką (znika, gdy zmywarka jest otwarta). To nie jest niedoróbka detalu — to brak jednej z pięciu stref w rozpisce.
- **rekomendacja:** (1) jawnie przypisać strefę przygotowania do **blatu ramienia** (x 419→1176 wolne spod GA4, gł. 500, długość 757 mm ≥ 600 ✓) i wpisać ją do PLAN §5a; (2) doprowadzić tam gniazdo (PLAN pkt 8.4 ma je jako „ewentualne" — zmienić na wymagane); (3) doświetlić (E39); (4) zaakceptować, że przygotowanie wymaga obrotu 180° od zlewu — przy jednym gotującym to koszt akceptowalny, ale **musi być napisane**, a nie ukryte.

**[E02] [RYZYKO] Narożnik A/B jest blatem tylko na papierze — leży poza zasięgiem ręki z każdej pozycji roboczej**
- **norma/zalecenie:** [antropometria] funkcjonalny zasięg poziomy (chwyt, bez odrywania stóp, przy pochyleniu tułowia) ≈ **650–700 mm** od krawędzi blatu.
- **w projekcie:** stojąc przy zlewie (x≈1150, y≈950) środek narożnika A/B (x≈300, y≈300) leży **1042 mm** od barku; stojąc przy płycie (x≈900, y≈1150) — **1040 mm**.
- **dowód:** blat A `x 0→600, y 0→1950` × blat B `y 0→600, x 155→2546` — obszar wspólny 445×600 w rogu; `_kontrola.py` BLENDY: `"ciąg B": [(155,600), ...]` — ten odcinek lica nie ma frontu, bo *„front/wysuw od tej strony kolidowałby z ciągiem indukcji"* (PLAN §5, ciąg B).
- **konsekwencja:** ~0,27 m² blatu, które w kalkulacji „mamy blat wokół całego U" wygląda jak powierzchnia robocza, w praktyce jest parkingiem na czajnik. Powiększa to deficyt z E01 — realny blat roboczy jest jeszcze mniejszy, niż wychodzi z metrażu.
- **rekomendacja:** nie liczyć narożnika do bilansu blatu roboczego; zaplanować go świadomie jako miejsce postojowe AGD drobnego (czajnik/toster) i doprowadzić tam gniazdo — inaczej te urządzenia zajmą 450 mm blatu nad zmywarką, czyli jedyny użyteczny odcinek prep.

**[E03] [BŁĄD] Ociekarka w GC1 wisi nad suchym blatem DC1, ~1,2 m od zlewu**
- **norma/zalecenie:** [praktyka] ociekarka wewnątrzszafkowa montowana **nad komorą zlewu** (woda kapie do zlewu). `standardy-meble.md` §Zlewy: *„NIE NAD ZMYWARKĄ — wyciek = zalanie"* — ta sama logika dotyczy blatu laminowanego.
- **w projekcie:** GC1 (ociekarka) wisi nad DC1, czyli nad ciągiem C w narożniku B/C, w odległości ok. **1,2 m** od komory zlewu i nad **blatem laminowanym 38 mm z łączeniem w rogu B/C**.
- **dowód:** PLAN §5 ściana C: *„**GC1** | **górna nad DC1** | ~470×998×**400** | półki + **ociekarka na umyte naczynia**"*; PLAN §5a: *„GC1 … umyte naczynia — ociekarka w szafce … (1 krok od zmywarki DB1, za narożnikiem)"* (błąd też w oznaczeniu: DB1 to zlew, zmywarka to DB2).
- **konsekwencja:** woda z talerzy kapie na blat laminowany dokładnie nad łączeniem blatów B/C1 (FORMATKI §2: *„Łączenia blatów: 3 (narożnik A/B przy pilastrze, **narożnik B/C1**, A/ramię)"*). Laminat 38 + fuga frezowana + stała wilgoć = spęcznienie krawędzi w ciągu 1–2 sezonów. Dodatkowo trasa „mokry talerz z komory zlewu → GC1" prowadzi **nad otwartą zmywarką**.
- **rekomendacja:** albo tacka ociekowa z odprowadzeniem, albo (lepiej) przenieść ociekarkę **nad zlew nie da się — nad ciągiem B nie ma górnych** → zamienić ociekarkę na **ociekacz wbudowany w blat zlewu po zachodniej stronie komory** (patrz E14: ten odcinek blatu i tak jest bezużyteczny) i zostawić GC1 wyłącznie na suche talerze.

**[E04] [BRAK] Funkcje wymuszone kontrolą K9 nie mają odpowiedników w liście okuć**
- **norma/zalecenie:** `_kontrola.py` `FUNKCJE_OBOWIAZKOWE = {"sztućce": 250, "kosz segregacji": 450, "przyprawy": 100}`.
- **w projekcie:** K9 przechodzi (kosz przypisany do DB1 800), ale w FORMATKI §3 „Okucia — lista zakupowa" **nie ma pozycji „kosz segregacji"** ani „ociekarka". Są: zawiasy, 3 systemy szuflad, wkład na sztućce 300, cargo 150, cargo spiżarniane, podnośnik okapu, nóżki, szuflady wewn. DC1, zawieszki, złączki, gola, kątowniki, LED, blenda dystansowa, silikon.
- **dowód:** FORMATKI-ROBOCZE.md §3, cała tabela — brak wiersza z koszem.
- **konsekwencja:** funkcja, którą skrypt kontroluje jako obowiązkową, nie zostanie kupiona. Kosz w szafce zlewowej z syfonem wymaga wersji z wycięciem pod syfon albo montażu na drzwiach — dobór ma wpływ na to, czy w DB1 zostanie miejsce na chemię.
- **rekomendacja:** dopisać do listy okuć: kosz segregacji ≥450 (z wycięciem pod syfon), ociekarka/ociekacz, wkład na przyprawy do DB0. Rozszerzyć K9 o kontrolę „funkcja ma moduł **i** ma okucie na liście zakupowej".

**[E05] [ULEPSZENIE] Sekwencja stref i ekonomia ruchu — jedyny mocny punkt układu, warto go nie zepsuć przy poprawkach**
- **norma/zalecenie:** `uklady-kuchni.md` §3: zapasy → przechowywanie → zmywanie → przygotowanie → gotowanie.
- **w projekcie:** idąc od ścianki: lodówka C3 (y 1225–1885) → spiżarka C2 (945–1225) → naczynia DC1+GC1/GC2 (0–945) → zmywarka DB2 (x 1550–2000) → zlew DB1 (750–1550) → [przygotowanie: brak] → płyta+piekarnik DA2 (y 850–1450). **Kolejność jest poprawna.**
- **dowód:** `_kontrola.py` CIAG_C / CIAG_B / CIAG_A, PLAN §5a.
- **konsekwencja (policzona):** przejścia między stanowiskami — zlew→płyta **292 mm (obrót w miejscu, 0 kroków)**, zlew→lodówka 656 mm (1 krok), płyta→lodówka 724 mm (~1,1 kroku), zmywarka→GC1/GC2 ~425 mm, zmywarka→sztućce RL1 764 mm + obrót 180°. Żadna para stref nie jest dalej niż ~1,2 kroku.
- **rekomendacja:** każdą poprawkę z tego raportu (zwłaszcza E37/E38 — przesunięcie ciągu B o 150) sprawdzić ponownie pod kątem odległości zlew↔płyta; to jedyny parametr, którego nie wolno pogorszyć.

---

### 2.2. Trójkąt roboczy

**[E06] [BŁĄD] PLAN podaje nieprawdziwe wymiary trójkąta roboczego**
- **norma/zalecenie:** `uklady-kuchni.md` §3: *„Trójkąt roboczy zlew–płyta–lodówka: suma boków 3600–7000 mm, **żaden bok <1200 ani >2700**"*.
- **w projekcie (deklarowane):** PLAN §4: *„**Trójkąt roboczy:** lodówka (C) → zlew (B, pod oknem) → indukcja (A): boki **~1,3–1,8 m, suma ~4,5 m** ✓ (norma 3,6–7,0)"*.
- **w projekcie (policzone z modelu):** boki **1206 / 1486 / 1700 mm**, suma **4392 mm**.
- **dowód:** punkty: płyta = środek wycięcia (x = 50 + 490/2 = 295, y = (864+1436)/2 = 1150); zlew = środek modułu DB1 (1150, 300); lodówka = środek lica C3 (1946, 1555).
- **konsekwencja:** deklarowany najkrótszy bok 1,3 m nie istnieje — realny to **1,21 m**, czyli **6 mm nad twardym minimum 1200**. Zapis „~1,3–1,8" ukrywa fakt, że projekt stoi na granicy progu. Suma jest zawyżona o 108 mm.
- **rekomendacja:** wpisać do PLAN §4 policzone wartości z podaniem punktów pomiarowych; dodać do `_kontrola.py` kontrolę **K10 — trójkąt roboczy** (boki 1200–2700, suma 3600–7000), liczoną z modelu, żeby liczba nie mogła znowu rozjechać się z rysunkiem.

**[E07] [BŁĄD] Pozycja komory w module zlewowym 800 jest nieokreślona, a decyduje o zgodności z dwoma progami naraz**
- **norma/zalecenie:** `uklady-kuchni.md` §3: *„Zlew: **≥450 od rogu** (żeby stać przodem)"* + próg boku trójkąta ≥1200.
- **w projekcie:** DB1 to moduł 800 z opisem *„zlew 1-komora z ociekaczem"* (PLAN §5) — **nigdzie nie napisano, po której stronie jest komora, a po której ociekacz**. FORMATKI §2: *„zlew wg szablonu w blacie B"*, bez pozycji.
- **dowód:** PLAN §5 ciąg B, wiersz DB1; FORMATKI-ROBOCZE.md §2.
- **konsekwencja (policzona):** komora w środku modułu (x 950–1450) → odległość od lica ciągu A (x=600) = **350 < 450, deficyt 100**, bok trójkąta zlew–płyta = 1206. Komora dosunięta na **zachód** (750–1150) → bok trójkąta spada do **1073 mm, poniżej twardego minimum 1200 o 127 mm**, a odległość od rogu do 150. Komora dosunięta na **wschód** (1100–1550) → 500 od rogu ✓, bok trójkąta 1335 ✓, a dodatkowo komora wychodzi poza pas zwężony przez ramię (E08). Jeden nieopisany szczegół przenosi projekt z „narusza dwa progi" do „spełnia oba".
- **rekomendacja:** wpisać do PLAN i FORMATKI jako `[P]`: **komora dosunięta do wschodniej krawędzi modułu (x ≈ 1100–1550), ociekacz po stronie zachodniej (x 750–1100)**. Uzasadnienie: (a) 500 mm od rogu ✓; (b) bok trójkąta 1335 ✓; (c) komora sąsiaduje ze zmywarką → załadunek bez kroku; (d) ociekacz ląduje nad odcinkiem blatu, który i tak jest bezużyteczny (E14); (e) komora zostaje pod oknem (752–1608) ✓; (f) blat za plecami komory ma pełne 1285, a nie 850 (E08).

---

### 2.3. Ciągi komunikacyjne i przejścia w U

**[E08] [BŁĄD — NARUSZONY TWARDY PRÓG] Strefa robocza między frontem ciągu B a ramieniem: 850 mm (albo 815)**
- **norma/zalecenie:** trzy progi z `uklady-kuchni.md`, wszystkie naruszone:
  - §1: *„**U** | trzy ściany, między ramionami **≥1200 (TWARDY PRÓG)**"*;
  - §1: *„**Półwysep** | jak L + wolna przestrzeń **≥1000** wokół półwyspu od strony roboczej"*;
  - §4: *„Przejście robocze przy jednym rzędzie (nikt nie przechodzi za plecami) | **minimum 1050** | optimum 1200"*.
- **w projekcie:** **850 mm** przy blacie 600 (PLAN §5) albo **815 mm** przy blacie 635 (FORMATKI §2).
- **dowód:** `_kontrola.py`: `RL1 (0,1450,1176,1950)` — północna krawędź ramienia na y=1450; ciąg B: `DB1 (750,0,1550,600)` — lico/blat na y=600. 1450 − 600 = 850. FORMATKI §2: *„Blat B (ciąg okna) | **2389×635**"* → 1450 − 635 = **815**. PLAN §4 sam to przyznaje: *„Front ciągu B ↔ ramię (przy zlewie, dla x<118) | **~85** (195−60−50) | **≥110 robocze** | ~ akceptowalne dla jednej osoby"*.
- **konsekwencja:** deficyt **350 mm wobec twardego progu 1200**, **150 mm wobec progu półwyspu 1000**, **200 mm wobec minimum przejścia roboczego 1050** (przy blacie 635: 385 / 185 / 235). PLAN ocenił to „~ akceptowalne" wobec własnego progu „≥110" — czyli wpisał ocenę pozytywną do wiersza, który jest o 250 mm poniżej progu podanego w tym samym wierszu. Praktycznie: kucając do szafki pod zlewem opierasz plecy o krawędź blatu ramienia; **nie da się jednocześnie otworzyć drzwi szafki zlewowej i wysunąć szuflady RL1 przy sobie stojąc** (E11).
- **łagodzące (uczciwie):** zwężenie dotyczy tylko odcinka x 750→1176, czyli **426 z 800 mm** modułu zlewowego (53%). Reszta zlewu (x 1176→1550) i cała zmywarka mają za plecami 1285 mm ✓. Dlatego rekomendacja E07 (komora na wschód) częściowo neutralizuje ten zarzut — komora znajdzie się w szerokiej części.
- **rekomendacja:** (1) ustalić głębokość blatu jako **600** (E12) — odzyskuje 35 mm; (2) komora zlewu na wschód (E07) — przenosi stanowisko robocze do pasa 1285; (3) **skrócić ramię z 1176 do ≤1000** — wtedy pas 850 kończy się na x=1000, cały moduł zlewowy od 1000 wzwyż ma 1285, a przejście przy ściance rośnie z 600 do 776. Koszt: 176 mm blatu ramienia, którego i tak w bilansie roboczym prawie nie ma (blat ramienia poza obrysem ciągu A to tylko odcinek x 600→1176). **To jest najtańsza pojedyncza poprawka w całym projekcie.**

**[E09] [RYZYKO] Przejście 600 mm — decyzja świadoma, ale konsekwencje nie są w dokumencie policzone**
- **norma/zalecenie:** `uklady-kuchni.md` §4: *„Przejście komunikacyjne (bez pracy, np. obok barku) | minimum **900** | optimum 1000+"*; §1 (barek przy przejściu do salonu): *„przejście obok **≥900 (TWARDY PRÓG)**"*.
- **w projekcie:** **600 mm** — `PROG_PRZEJSCIA = 600` w `_kontrola.py` (linia 30, komentarz: *„decyzja inwestora [P] — reguła nadrzędna"*), 1776 − 1176 = 600.
- **dowód:** PLAN §4: *„Ramię ↔ czubek ścianki | ~60 [P] | ≥90 | ✗ świadoma decyzja inwestora"*; PLAN §2, wiersz „Przejście ramię ↔ ścianka".
- **konsekwencja — czego PLAN nie pisze:** deficyt 300 mm wobec twardego progu. Przy 600 mm: (a) **nie przejdziesz z tacą/garnkiem trzymanym z boku** — potrzeba ~750 mm; (b) **nie wniesiesz przez to przejście lodówki ani zmywarki** — lodówka 600 szer. + opakowanie/uchwyty nie przechodzi bokiem przez otwór 600, co ma znaczenie przy montażu samodzielnym **i przy przyszłej wymianie AGD** (trzeba będzie zdjąć blat ramienia); (c) skręcając w przejście obcierasz się o narożnik blatu ramienia na wysokości uda (blat 910, wysokość biodra dla 182 cm ≈ 1050); (d) przy otwartej lodówce przejście zanika całkowicie (E10).
- **rekomendacja:** (1) zaokrąglić/sfazować **narożnik południowo-wschodni blatu ramienia promieniem ≥30–50 mm** — koszt zerowy przy docinaniu blatu, eliminuje najczęstszy uraz; (2) zapisać w PLAN pkt 9 ryzyko „wymiana AGD wymaga demontażu blatu ramienia"; (3) rozważyć E08.3 (ramię ≤1000 → przejście 776) — inwestor decydował o 600 jako o minimum, nie jako o wartości docelowej.

**[E10] [BŁĄD] Otwarte drzwi lodówki zamykają jedyne wejście do kuchni**
- **norma/zalecenie:** `SKILL.md` §Twarde zasady pkt 6 (o zmywarce, ta sama logika): *„otwarty front nie może **blokować przejścia** ani drzwi"*; `uklady-kuchni.md` §4: *„Drzwi lodówki | otwarcie ≥90°, do wyjęcia szuflad ~110°"*.
- **w projekcie:** drzwi 600 mm, zawias przy ściance (y=1885), otwierane ku oknu. Przy 90° skrzydło leży wzdłuż y≈1885 i sięga od x=1946 do **x=1346**. Przejście to pas **x 1176→1776**.
- **dowód:** `_kontrola.py`: `C3 lodówka (1946,1225,2546,1885)`, `SCIANKA = (1776,1885,2546,1975)`, `RL1 … 1176`. PLAN §5: *„zawiasy lodówki od strony ścianki, drzwi otwierane ku oknu"*.
- **konsekwencja (policzona):** światło przejścia przy otwartych drzwiach spada z 600 do **170 mm** (model) lub **70 mm** (przy realnej głębokości lodówki 650 + 50 wentylacji = 700 → lico na x=1846). Czyli: **przy otwartej lodówce nie wejdziesz do kuchni ani z niej nie wyjdziesz**. Dla jednej gotującej osoby to nie jest katastrofa, ale: (a) skrzydło otwiera się **w poprzek jedynej trasy komunikacyjnej** — kto wchodzi, dostaje drzwiami; (b) nie da się wnieść zakupów do lodówki „przez przejście" — trzeba wejść, zamknąć za sobą trasę, wypakować.
- **dodatkowo:** kontrola **K3 tego nie sprawdza** — `_kontrola.py` linia 206: `if not m.front or m.typ in ("AGD", "szuflady", "uchylny"): continue`. Lodówka ma `typ="AGD"`, więc jej wychył **nigdy nie był weryfikowany automatycznie**. Model dodatkowo zakłada C3 o głębokości 600 (x 1946→2546), podczas gdy PLAN §2 podaje lodówkę **60×65×190** + PLAN §7 *„luzy 20–30 bok, 50 tył/góra"* → potrzeba **700**. Model zaniża wysięg lodówki o **100 mm**.
- **rekomendacja:** (1) poprawić model: `C3` na `x0=1846` i dopisać do K3 obsługę AGD (drzwi lodówki jako skrzydło 600 z zawiasem, front zmywarki jako klapa opadająca ~780); (2) zaakceptować blokadę przejścia jako świadomą konsekwencję decyzji „przejście 600" i **zapisać ją w PLAN pkt 9** — dziś jej tam nie ma; (3) blenda dystansowa 70 mm jest już na liście (FORMATKI §3: *„Blenda dystansowa lodówka–ścianka | 1 szt (~70×2478)"*) i po jej uwzględnieniu skrzydło otwiera się do **~112°** ✓ (policzone: narożnik ścianki 1776,1885 względem przeniesionej osi zawiasu 1846,1815 → kolizja dopiero przy 112,6°) — to spełnia wymóg ~110° na wyjęcie szuflad. **Ten element projektu jest policzony dobrze i nie należy go ruszać.**

**[E11] [RYZYKO] Fronty naprzeciwko siebie: 930 mm między licami — nie da się pracować przy obu naraz**
- **norma/zalecenie:** `uklady-kuchni.md` §4: *„Szuflady naprzeciwko siebie (układ II/U) | **nie otwierają się jednocześnie przy <1200** | optimum 1300+"*.
- **w projekcie:** **930 mm** między licem frontów ciągu B (y=560) a licem frontu RL1 (y=1490, korpus 460 pod blatem 500).
- **dowód:** `_kontrola.py` `DB1 … (750,0,1550,600)`, korpus 560 wg PLAN §5 (*„głębokość korpusów 560"*); `RL1 … ~1176×820×**460**` (PLAN §5) przy blacie ramienia 500.
- **konsekwencja:** wysunięta szuflada RL1 (nominał 400 wg PLAN v3.12a) + otwarte skrzydło szafki zlewowej (front 397 wg FORMATKI) = 797 mm z dostępnych 930 → **zostaje 133 mm**, czyli fizycznie się mijają, ale **nie ma gdzie stanąć**. Norma na stanowisko człowieka między otwartymi frontami to ≥600 → deficyt **467 mm**. Praktycznie: żeby sięgnąć po sztućce, musisz najpierw zamknąć szafkę pod zlewem.
- **rekomendacja:** przenieść funkcje o wysokiej częstotliwości użycia poza tę parę: sztućce do szuflad RL1 zostają (nie ma alternatywy), ale **kosz segregacji i chemia w DB1 powinny być na wysuwie, nie za skrzydłami** — wysuw nie zajmuje ćwiartki wychyłu, tylko pas prosty, i można go obsłużyć stojąc bokiem.

**[E12] [BŁĄD] Głębokość blatu w dwóch wersjach: 600 (PLAN) vs 635 (FORMATKI) — różnica przenosi się wprost na przejście robocze**
- **norma/zalecenie:** `standardy-meble.md`: *„Głębokość blatu (z wystawką): **600-630**"*.
- **w projekcie:** PLAN §5: *„głębokość korpusów 560, **blat 600** (ramię 650)"*. FORMATKI §2: *„Blat A | **1950×635**; Blat B | **2389×635**; Blat C1 | **947×635**"*.
- **dowód:** oba cytaty wyżej; 635 wykracza też o 5 mm poza pasmo 600–630 ze `standardy-meble.md`.
- **konsekwencja:** strefa robocza przy zlewie to **850 albo 815** (E08), odstawcze przy płycie to 49 albo 84 mm przed wycięciem (E22), a wolna głębokość blatu przed górnymi 181 albo 216 (E16). **Trzy kluczowe liczby ergonomiczne mają po dwie wartości.** Do tego PLAN §5 podaje trzecią sprzeczność: *„ramię 650"* — przy głębokości ramienia potwierdzonej jako **500 `[P]`** (PLAN §2, decyzja z v3.5) i blacie ramienia 545×**500** w FORMATKI. Prompt renderu (PLAN pkt 13) niesie czwartą: *„L-shaped worktop return (~118×**65**)"*.
- **rekomendacja:** przyjąć **blat 600, ramię 500** jako jedyne `[P]`, wykreślić „(ramię 650)" z PLAN §5 i „65" z pkt 13, poprawić FORMATKI §2 na 600. Wpisać głębokości blatów do `_kontrola.py` jako stałe i dodać kontrolę zgodności PLAN↔FORMATKI↔model (to dokładnie przypadek opisany w `protokol-weryfikacji.md` §1: *„Wymiary modułów NIE mogą żyć równolegle w trzech miejscach … zawsze się rozjadą"*).

**[E13] [BŁĄD] Długość ramienia 1176 vs 1180 — w wersji z dokumentu przejście ma 596, czyli poniżej progu inwestora**
- **norma/zalecenie:** `PROG_PRZEJSCIA = 600` — *„decyzja inwestora [P] — reguła nadrzędna"*; K6 raportuje FAIL przy `p < 599`.
- **w projekcie:** model 1176 → przejście **600** ✓. PLAN §5 nagłówek ramienia: *„~**1180**×500 `[P gł.]`"*, wiersz blatu: *„blat ramienia | ~**1180**×500×38"*, panel: *„panel ryflowany | ~**1180**×910"*. FORMATKI §2: blat A 635 + blat ramienia 545 = **1180** → przejście **596**.
- **dowód:** cytaty wyżej + `_kontrola.py` `RL1 … 1176`. Historia PLAN v3.11 jawnie mówi: *„Poprawiono też ramię 1180 → **1176**, żeby przejście miało pełne 600, a nie 596"* — poprawka **nie została wprowadzona w §5 ani w FORMATKI**.
- **konsekwencja:** jeżeli stolarz/rozkrój pójdzie za dokumentem, a nie za skryptem, przejście wyjdzie 596 i K6 dałoby FAIL. Ergonomicznie 4 mm nic nie zmieniają — **poważny jest fakt, że poprawka opisana w historii jako wykonana nie istnieje w treści dokumentu.** To ten sam mechanizm, który wcześniej w tym projekcie wyprodukował okap nad szufladami.
- **rekomendacja:** zamienić wszystkie wystąpienia 1180 na 1176 (PLAN §5 ×3, FORMATKI §2, panel ryflowany w FORMATKI §1 ma już 1176 — czyli plik jest wewnętrznie sprzeczny sam ze sobą). Docelowo: rozpiska generowana z modelu, nie pisana ręcznie.

**[E14] [BŁĄD] Blat odstawczy po zachodniej stronie zlewu: 150 mm**
- **norma/zalecenie:** `uklady-kuchni.md` §3: *„Odstawcze: ≥300 blatu z obu stron płyty …, **≥300 przy lodówce**"*; dla zlewu praktyka i §3 pkt 4 wymagają blatu odstawczego po **obu** stronach komory (min. 400 po stronie brudnej).
- **w projekcie:** zachód **150 mm** (x 600→750, nad wysuwem cargo), wschód **450 mm** (x 1550→2000, nad zmywarką).
- **dowód:** `_kontrola.py`: `DB0 (600,0,750,600)`, `DB1 (750,...)`, `DB2 (1550,0,2000,600)`, `DC1 (2000,...)`.
- **konsekwencja:** brudne naczynia nie mają gdzie czekać po stronie zachodniej (deficyt 250 wobec 400), a jedyny sensowny odcinek 450 mm **znika, gdy zmywarka jest otwarta** — front opada na wysokość ~100 mm i zajmuje pas x 1550→2000 na całej głębokości do y≈1380. Czyli przy rozładunku zmywarki nie masz blatu odstawczego w ogóle.
- **rekomendacja:** ociekacz wbudowany po zachodniej stronie komory (E07) zamienia te bezużyteczne 150 mm w funkcję; blat nad zmywarką zostaje jako odkładczy, a rozładunek zmywarki obsługuje blat DC1 (x 2000→2546, y 600→945) — **ten fragment trzeba jawnie opisać w PLAN §5a jako strefę odkładczą przy zmywarce**, dziś nie ma go w planie funkcjonalnym.

---

### 2.4. Blat roboczy — podsumowanie liczbowe

| Odcinek | Norma (`uklady-kuchni.md` §3) | W projekcie | Ocena |
|---|---|---|---|
| ciągły blat zlew ↔ płyta | min 600 / opt 900–1200 | **150** (prosty) | ✗ deficyt 450 / 750–1050 |
| odstawczy zachód od zlewu | ≥400 [praktyka] | **150** | ✗ deficyt 250 |
| odstawczy wschód od zlewu | ≥400 [praktyka] | **450** (znika przy otwartej zmywarce) | ~ warunkowo |
| odstawczy północ od płyty | ≥300 | **264** do lica B, dalej narożnik nieosiągalny | ~ na granicy |
| odstawczy południe od płyty | ≥300 | **514** (blat ramienia) | ✓ |
| największy wolny ciągły blat w kuchni | — | **757 mm × 500** (ramię, x 419→1176 spod GA4) | jedyny ≥600 |
| efektywna głębokość robocza pod górnymi | 400–450 [praktyka] | **181** (blat 600) / **216** (635) | ✗ deficyt 220–270 |

**[E15] [RYZYKO] Blat odstawczy na północ od płyty: 264 mm do lica ciągu B**
- **norma/zalecenie:** `uklady-kuchni.md` §3: *„Odstawcze: **≥300** blatu z obu stron płyty"*.
- **w projekcie:** 864 − 600 = **264 mm** własnego blatu; dalej zaczyna się narożnik wspólny z ciągiem B, który jest poza zasięgiem (E02).
- **dowód:** `PLYTA = (864, 1436)` w `_kontrola.py`; lico/blat ciągu B na y=600.
- **konsekwencja:** deficyt **36 mm** wobec progu, jeżeli liczyć tylko blat „własny". Formalnie norma jest spełniona (blat biegnie dalej, nieprzerwanie, aż do y=0), więc **nie klasyfikuję tego jako BŁĄD** — ale praktycznie odstawiając gorący garnek z północnego pola płyty masz 26 cm, potem róg. Przy 182 cm i pracy przodem do ściany A jest to ruch „przez ciało".
- **rekomendacja:** ustawić w tym rogu stały element (pojemnik na narzędzia / listwa na noże na ścianie), żeby nie kusiło do odstawiania tam garnków; strefa odstawcza dla płyty to **wyłącznie południe (514 mm, blat ramienia)** — zapisać to w PLAN §5a.

**[E16] [RYZYKO] Górne 400 mm nad blatem 600 — wolna głębokość robocza 181 mm**
- **norma/zalecenie:** `standardy-meble.md`: *„Głębokość [górnych]: **320** (standard) lub **360-400** (głębokie)"* — 400 jest górną granicą pasma, więc formalnie dopuszczalne.
- **w projekcie:** korpus 400 + front 19 = **419** od ściany; blat 600 (albo 635) → wolne **181** (albo 216). W kuchni standardowej (górne 320 nad blatem 600) jest 280 → projekt jest o **~100 mm gorszy od standardu**.
- **dowód:** PLAN §11a: *„Głębokość korpusu górnych: **400** `[P decyzja inwestora]`, front 19 → **419** całkowitej; cofnięcie od lica blatu **181**"* — liczba jest w dokumencie, ale bez oceny skutku.
- **konsekwencja:** przy wzroście 182 cm (wysokość barku ≈ 1490, wysokość oczu ≈ 1700) dolna, przednia krawędź szafki na 1480 leży 220 mm poniżej oczu i tylko 181 mm za krawędzią blatu — **przy sięganiu do tylnej części blatu uderzasz w nią czołem/ramieniem**. Cały pas blatu x 0→419 na ścianie A (czyli 70% jego głębokości) jest w praktyce półką na sprzęt, nie powierzchnią roboczą. Uzasadnienie decyzji (PLAN §11a: *„GA1 wisi na licu pilastra, więc jej głębokość = 400 − 155 = 245"*) jest sensowne — ale cenę płaci cały ciąg A, żeby ratować jedną szafkę.
- **rekomendacja:** rozważyć **GA1 245 gł. + GA2–GA4 na 320** i zaakceptować uskok 80 mm w licu górnych **tylko na styku GA1/GA2** (K5 by to zgłosiła — trzeba by ją poluzować do „wspólne lico w obrębie grupy"). Zysk: 80 mm wolnego blatu na całej ścianie z płytą. Alternatywa mniejszym kosztem: zostawić 400, ale **na ścianie B (zlew, bez górnych) świadomie zaplanować całą pracę wymagającą głębokości** — co i tak wychodzi z E01.

**[E17] [BRAK] Blat A nie ma wycięcia pod pilaster**
- **norma/zalecenie:** `technologia-wykonania.md` §6: *„Blenda przy gzymsie/słupie … zakończ zabudowę blendą 30–80 mm PRZED elementem; nie przycinaj korpusu wokół gzymsu"*.
- **w projekcie:** pilaster zajmuje x 0→155, y 0→670 (pion, na całą wysokość, `[P]` v3.7). Korpusy to respektują (`DA1` od x=155, `GA1` od x=155). **Blat A w FORMATKI §2 to prostokąt 1950×635** — bez wycięcia 155×670.
- **dowód:** FORMATKI §2: *„Blat A (ciąg indukcji) | **1950×635** | docinany na miejscu"*; PLAN §2: *„Pilaster przy A/B: dł. × gł. | **67 × 15,5** … PIONOWY, na całą wysokość"*.
- **konsekwencja:** albo blat trzeba wyciąć na miejscu (wyrzynarką, w laminacie 38, w widocznym miejscu, przy montażu samodzielnym — trudne), albo blat kończy się na y=670 i potrzebny jest drugi kawałek. Ergonomicznie: na odcinku przy pilastrze blat ma **480 mm** głębokości zamiast 635 — to jest dokładnie ten róg, w którym miałaby stanąć strefa przygotowania (E01).
- **rekomendacja:** dopisać do FORMATKI §2 wycięcie **155×670 w narożniku północno-zachodnim blatu A** ze statusem „po pomiarze pilastra w 3 punktach" (PLAN pkt 11.11) i zapisać, że na tym odcinku blat ma 480 gł.

---

### 2.5. Bezpieczeństwo płyty

**[E18] [ZGODNE — z podaniem liczb] Odstępy poziome płyty są prawidłowe**
- **norma:** `SKILL.md` §Twarde zasady pkt 4: *„płyta **≥300 mm od ściany bocznej i wysokiej zabudowy**"*; `uklady-kuchni.md` §4: *„płyta grzewcza nie przy przejściu/drzwiach (rączki garnków), nie pod oknem z firaną"*.
- **w projekcie:** płyta y 864→1436 na ścianie A. Do ściany B (y=0): **864 mm** ✓ (zapas 564). Do najbliższej wysokiej zabudowy (słupek C2 na x=1946): **>1300** ✓. Do okna (ściana B, x 752→1608): najkrótsza odległość **864 mm** ✓ — okno jest na innej ścianie, firanka/skrzydło nie zachodzą nad płytę. Do otworu do salonu (ściana A, y 1950→3220): **514 mm** ✓. Do przejścia 600 (x 1176→1776, y ~1885): **>1000** ✓.
- **dowód:** `PLYTA = (864, 1436)`, `SCIANKA = (1776,1885,...)`, PLAN §2 (okno 59,7/85,6/94,7 od pilastra).
- **wniosek:** to jest policzone dobrze i **nie należy tego ruszać** przy poprawkach E08/E37.

**[E19] [RYZYKO] Okap 419 mm głęboki nad płytą 512 mm głęboką — 93 mm frontu płyty poza okapem**
- **norma/zalecenie:** [praktyka] okap powinien przykrywać **całą głębokość płyty**; przy recyrkulacji (brak ciągu kanałowego) niedomiar jest odczuwalny mocniej niż przy wyciągu.
- **w projekcie:** GA3 = korpus 400 + front 19 = **419** od ściany. Płyta Bosch PXE601DC1E ma szkło **512** gł.; przy wycięciu 490 odsuniętym 50 od ściany szkło zajmuje x 39→551. Poza obrysem okapu zostaje **x 419→551 = 132 mm** (26% głębokości płyty), w tym cały przedni pas pól grzejnych.
- **dowód:** PLAN §5: *„GA3 | **okap w zabudowie** | 600×998×**400** | front uchylny"*; PLAN §2: *„Indukcja Bosch PXE601DC1E | **57,2 × 51,2** × 5,6; wycięcie 56 × 49"*.
- **konsekwencja:** para z przednich pól omija okap. Przy recyrkulacji z filtrem węglowym `[P]` — tłuszcz osiada na froncie GA3/GA4 i na suficie nad ramieniem.
- **rekomendacja:** dobrać **okap teleskopowy wysuwany** (wysuw 250–300 wyrównuje obrys do 670) zamiast okapu z frontem uchylnym; FORMATKI §3 ma już pozycję *„Podnośnik frontu okapu (Aventos HK-S lub wg okapu) | 1 kpl | dobór po zakupie okapu"* — decyzja jest jeszcze otwarta, więc zmiana nic nie kosztuje. Jeżeli okap zostanie podszafkowy stały — przesunąć płytę maksymalnie do tyłu w granicach karty Bosch.

**[E20] [RYZYKO] Okap 570 mm nad płytą — 20 mm zapasu nad twardym minimum, przy użytkowniku 182 cm**
- **norma/zalecenie:** `standardy-meble.md` §Strefy bezpieczeństwa: *„Okap od indukcji: **min 550mm**"*; *„Szafka nad płytą gazową: zakaz …, **nad indukcją min 750mm**"*. `uklady-kuchni.md`/`SKILL.md`: to samo 550.
- **w projekcie:** **570 mm** (1480 − 910). PLAN §6 deklaruje: *„Dół górnych A / okapu | 1480 | **odstęp 600 od blatu**; okap–indukcja ≥550 ✓"* — **1480 − 910 = 570, nie 600**. `_schemat.py` linia 240 rysuje etykietę *„≥55 okap–indukcja"*.
- **dowód:** cytaty wyżej.
- **konsekwencja:** (a) błąd arytmetyczny w PLAN §6 (30 mm) — wartość realna 570 nadal mieści się w normie `standardy-meble.md` *„Odstęp od blatu do dolnej krawędzi górnych: **500-600**"* ✓, więc skutek jest dokumentacyjny, nie konstrukcyjny; (b) **zapas nad twardym minimum to 20 mm**, a PLAN pkt 8.5 i pkt 11.5 wymagają przemierzenia wysokości **po posadzce docelowej** — jeżeli blat zostanie ustawiony na 910 od **nowej** posadzki, a listwa górnych na 1480 od nowej posadzki, relacja się zachowa ✓; jeżeli którakolwiek z tych wysokości zostanie odmierzona od wylewki, odstęp spada poniżej 550; (c) przy 182 cm dolna krawędź okapu na 1480 z wysięgiem do 419 jest **poniżej wysokości oczu o 220 mm** — pochylając się nad tylnym polem grzejnym uderzasz w nią głową.
- **rekomendacja:** poprawić PLAN §6 na 570; dopisać do listy pomiarów pkt 11 jawną instrukcję: **„blat 910 i listwa górnych 1480 — obie od posadzki DOCELOWEJ, jedno odbicie poziomu na ścianie"**; przy wyborze okapu preferować model o niskiej obudowie, żeby zejść z 1480 nie było potrzeby.

**[E21] [RYZYKO] Południowa krawędź wycięcia płyty leży 14 mm od linii, w której zaczyna się blat opisany jako „śniadaniowy"**
- **norma/zalecenie:** [praktyka] miejsca siedzącego / strefy socjalnej nie planuje się w zasięgu rączek garnków; między płytą a strefą przebywania min. 400 mm blatu.
- **w projekcie:** wycięcie kończy się na y=1436, blat ramienia zaczyna się na y=1450 → **14 mm**. Blat ramienia jest w PLAN §5a opisany jako *„strefa odstawcza/**śniadaniowa**"*.
- **dowód:** `PLYTA = (864, **1436**)`, `RL1 (0,**1450**,1176,1950)`; PLAN §5a wiersz RL1.
- **konsekwencja:** południowe pole grzejne styka się bezpośrednio ze strefą, przy której ma się jeść. Formalnie 514 mm blatu odstawczego na południe ✓ (E15) — ale to ten sam blat, który pełni funkcję śniadaniową. Nie da się mieć obu naraz.
- **rekomendacja:** skreślić „śniadaniowa" z PLAN §5a (i tak jest niewykonalna — patrz E22) i zostawić opis „strefa odstawcza przy płycie i piekarniku + główny blat przygotowania".

**[E22] [BŁĄD] Funkcja „śniadaniowa" przypisana blatowi bez podjazdu na kolana**
- **norma/zalecenie:** [praktyka] miejsce siedzące przy blacie: nadwieszenie blatu **≥250 mm** (przy wysokości 900+ raczej 300), szerokość **≥600 mm/osobę**, wysokość siedziska 650–700 przy blacie 910.
- **w projekcie:** nadwieszenie **0 mm** — południowe lico ramienia zamyka **panel ryflowany 1176×910** licujący z krawędzią blatu; RL1 to pełny korpus 0→1176 × 1450→1950.
- **dowód:** PLAN §5 ramię: *„panel ryflowany | ~1180×910 | rewers: od salonu (południe) i od korytarza"*; FORMATKI §1: *„Panel ryflowany ramienia (lamele) | **1176×910**"*; `_kontrola.py` `RL1 (0,1450,1176,1950)`.
- **konsekwencja:** przy blacie nie da się usiąść — kolana uderzają w panel. Funkcja „śniadaniowa" z planu funkcjonalnego jest niewykonalna, a to **dokładnie ten sam typ błędu, który wykryła kontrola K9 w v3.12** (plan funkcjonalny opisujący coś, czego w konstrukcji nie ma).
- **rekomendacja:** albo (a) skreślić funkcję (rekomendowane — patrz E21 i E23, ramię jest cenniejsze jako blat roboczy i jako schowek), albo (b) wysunąć blat ramienia o 300 na południe i cofnąć panel — ale to zjada 300 z otworu do salonu i z korytarza, więc realnie odpada.

---

### 2.6. Wysokość robocza vs wzrost 182 cm

**[E23] [ZGODNE z zastrzeżeniem] Blat 910 — zgodny z własną siatką projektu, ale 182 cm to dolny skraj pasma**
- **norma/zalecenie:** `standardy-meble.md`: *„Wysokość blatu od podłogi — **JEDYNA obowiązująca siatka**: osoba do 165cm → 860; 165-180cm → 880; **180+cm → 910**"*.
- **w projekcie:** **910** `[P]`, uzasadnione w PLAN §2: *„wzrost inwestora 182 (siatka: 180+ → 910)"*.
- **ocena:** **formalnie zgodne ✓.** Nie podnoszę tego do rangi błędu — siatka projektu jest jednoznaczna. Zastrzeżenia liczbowe, które trzeba znać:
  - pasmo „180+" obejmuje 180–200 cm; przy 182 cm użytkownik jest na jego początku, więc 910 jest dla niego wartością bezpieczną (nie za wysoką).
  - **strefa zmywania pracuje niżej niż blat:** dno komory zlewu leży ~180–200 mm poniżej blatu → efektywna wysokość pracy przy zmywaniu **710–730 mm**, co przy wysokości łokcia ~1130 dla 182 cm oznacza pochylenie tułowia. To jest normalne w każdej kuchni jednopoziomowej, ale warto to wiedzieć przed decyzją o głębokości komory.
- **rekomendacja:** przy zakupie zlewu wybrać komorę **płytszą (150–170 zamiast 200)** — to jedyny bezkosztowy sposób podniesienia efektywnej wysokości strefy zmywania o 30–50 mm. Nie zmieniać blatu 910.

**[E24] [BŁĄD] Sprzeczność wysokości korpusów w dokumentacji: 720 vs 820 — 50 mm rozbieżności w wysokości blatu**
- **norma/zalecenie:** `standardy-meble.md`: *„Wysokość korpusu: **720** (bez cokołu i blatu); **Cokół: 100** (typowy) — całość **820** do góry korpusu"*.
- **w projekcie — trzy różne wersje:**
  - PLAN §5 nagłówek: *„korpusy dolne **720** + **cokół ~150 (nóżki 150)**, blat **910** `[P]` (laminat 38)"* → 150+720+38 = **908**;
  - PLAN §5 tabele modułów: **wszystkie** dolne opisane jako `×820×` (DA1 850×**820**×405, DA2 600×**820**×560, RL1 1176×**820**×460, DB0 150×**820**×560, DB1 800×**820**×560, DC1 945×**820**×546) — czyli wartość ze `standardy-meble.md` **dla cokołu 100**, nie dla nóżek 150; przy cokole 100 blat wypada na **858**;
  - FORMATKI nagłówek: *„wysokości korpusów: dolne **720** (nóżki **150**)"*, wszystkie boki 720 ✓.
- **dowód:** cytaty wyżej.
- **konsekwencja:** liczba „820" w tabeli modułów, czytana wprost, daje blat **858** zamiast 910 — **52 mm różnicy**, czyli powrót do wysokości dla osoby 165–180 cm. Dla użytkownika 182 cm oznaczałoby to pracę o pół pasma siatki za nisko. Dodatkowo: 720 + 150 + 38 = **908, nie 910** — brakujące 2 mm trzeba wybrać regulacją nóżek (zakres 100–150 wg `standardy-meble.md`, więc nóżka pracuje **na końcu zakresu**, bez rezerwy w dół przy nierównej podłodze).
- **rekomendacja:** (1) wykreślić „820" z tabel PLAN §5 i wpisać **720**; (2) zapisać jawnie bilans pionowy: `nóżki 152 + korpus 720 + blat 38 = 910`, ewentualnie `nóżki 150 + korpus 720 + blat 40 = 910`; (3) **dobrać nóżki o zakresie 150–200**, żeby przy poziomowaniu od najwyższego punktu podłogi (FORMATKI §4 pkt 3) była rezerwa w górę.

**[E25] [RYZYKO] Sięg do najwyższej półki 2478 — 458 mm ponad pewny chwyt użytkownika 182 cm**
- **norma/zalecenie:** [antropometria] dla wzrostu 182 cm: wysokość barku ≈ **1490**, zasięg czubkami palców w górę ≈ **2180**, **pewny chwyt** (uchwycenie i wyjęcie przedmiotu obiema rękami) ≈ **2000–2030**. [praktyka] najwyższa półka użytkowa bez stołka ≤ **1900–2000**.
- **w projekcie:** górne **1480 → 2478** (korpus 998), słupek C2 i nadstawka C4 **do 2478**.
- **dowód:** PLAN §6: *„Góra zabudowy | **2478** | górne A, słupek C2, nadstawka C4 — wszystko do sufitu"*; FORMATKI: boki górnych 998, boki C2 **2378**.
- **konsekwencja:** pas **2000→2478 = 458 mm, czyli 46% wysokości korpusu górnego**, wymaga stołka nawet przy 182 cm. Przy 400 mm głębokości i szafce zamykanej **jednym frontem 996 mm** (FORMATKI: fronty górne 996) sięgasz w głąb 400 mm na wysokości 2,3 m, w ciemno, stojąc na stołku, z pełnym skrzydłem otwartym nad głową. Plan funkcjonalny przypisuje tam głównie rzeczy rzadkie ✓ (GA1 *„zapasy lekkie, rzadko używane"*, nad okapem *„antresola na rzeczy sezonowe"*, C4 *„zapasy sezonowe"*) — **ale GC2 dostaje „szklanki, kubki, miski **codzienne**", a GC1 „talerze **codzienne**"**, co jest wykonalne wyłącznie na najniższej półce (1480–1750).
- **rekomendacja:** (1) w GC1/GC2 wymusić rozstaw półek **1480 / 1750 / 2000**, a pas 2000–2478 wydzielić **osobnym frontem (antresola)** — dziś FORMATKI dają w GC1/GC2 po 2 półki i jeden front 996; (2) dla frontów górnych 996 mm rozważyć podnośniki (Aventos) zamiast zawiasów bocznych — skrzydło 996 otwierane na bok przy 400 gł. przesuwa się przez pole widzenia na wysokości twarzy; (3) **dopisać do PLAN pkt 6 wiersz „strefa stołka: 2000–2478"** — dziś rozpisanie pionowe nie rozróżnia stref sięgu.

**[E26] [RYZYKO] Zabudowa do sufitu 2478 cięta przed posadzką docelową**
- **norma/zalecenie:** `technologia-wykonania.md` §2: *„do sufitu: fuga 10–30 mm + listwa/blenda maskująca"*; PLAN pkt 8.5: *„Wymiary pionowe finalnie po posadzce docelowej"*.
- **w projekcie:** FORMATKI już zawiera formatki wyliczone z 2478: górne boki **998**, C2 boki **2378**, bok wykończeniowy lodówki **2478×680**, panel ryflowany 1176×**910**.
- **dowód:** cytaty z FORMATKI §1; PLAN §2: *„Sufit | 247,8 | `[P]` | pomiar (**kontrola po posadzce!**)"*.
- **konsekwencja:** posadzka docelowa (jasny dąb + podkład) podniesie poziom o ~15–20 mm → wysokość w świetle spadnie do ~2458–2463, a formatki 998/2378 są cięte na 2478. Ryzyko jest w PLAN opisane, ale **liczby już przeciekły do listy formatek**, co jest dokładnie tym, przed czym ostrzega `formatki.md`: *„TWARDA REGUŁA: lista formatek powstaje WYŁĄCZNIE po pomiarach kontrolnych"*.
- **rekomendacja:** oznaczyć w FORMATKI wszystkie wymiary pionowe jako `[~ po posadzce]` i **wyzerować je** do czasu pomiaru; blenda górna docinana na miejscu (FORMATKI §4 pkt 7 to przewiduje ✓).

---

### 2.7. Kierunki otwierania — kolizje

**[E27] [BŁĄD] Opuszczone drzwi piekarnika kolidują z wysuniętymi szufladami RL1 — 243 × 400 mm**
- **norma/zalecenie:** `protokol-weryfikacji.md` §6 pyt. 1: *„Czy każdy front ma się gdzie otworzyć?"*; K3 ma to łapać.
- **w projekcie:** drzwi piekarnika opadają z lica x≈579 na ~540 mm do przodu (x≈1119) na całej szerokości y 850→1450. Szuflady RL1 (nominał 400, PLAN v3.12a) wysuwają się z y=1450 na północ do y=1050, na szerokości x 876→1176. **Nakładka 243 × 400 mm.**
- **dowód:** `_kontrola.py`: `DA2 … (0,850,560,1450)`, `RL1 … front=(576,1176)`, `y0=1450`; PLAN v3.12a: *„Nominały: **RL1 3×400**"*; PLAN §5 DA2: *„front piekarnika + szuflada"*.
- **konsekwencja:** przy otwartym piekarniku **nie wysuniesz szuflady ze sztućcami, nożami i przyborami** — czyli dokładnie tego, po co sięgasz w trakcie pieczenia. Ta sama kolizja dotyczy drzwi 300 w RL1 (skrzydło stojące na x≈876 w pasie y 1150–1450 wchodzi w ćwiartkę drzwi piekarnika).
- **dlaczego kontrola tego nie złapała:** `_kontrola.py` linia 206: `if not m.front or m.typ in ("AGD", "szuflady", "uchylny"): continue` — DA2 ma `typ="uchylny"`, RL1 ma szuflady i **model w ogóle nie zna pojęcia wysuwu**; K3 sprawdza tylko pas 50 mm przed licem (linia 182: `PAS = 50`). To jest **luka tej samej klasy co błąd v3.7a, dla którego K3 powstała**.
- **rekomendacja:** (1) rozszerzyć K3 o **wysuw**: każdy moduł dostaje `wysuw` (szuflada = nominał prowadnicy, piekarnik = ~540, zmywarka = ~780, cargo = głębokość korpusu) i sprawdzana jest nakładka prostokątów wysuwu, nie tylko pas 50; (2) w rozwiązaniu docelowym: **przenieść szuflady RL1 na wschodni koniec ramienia** (x 876→1176 jest już wschodnim końcem — kolizja i tak zachodzi, bo drzwi piekarnika mają 600 szerokości), więc realnie: **skrócić ramię do ≤1000** (E08.3) nic tu nie pomoże. Poprawka wykonalna: **zamienić kolejność w RL1 — szuflady na x 576→876 (bliżej ciągu A) też kolidują.** Uczciwy wniosek: przy tej geometrii **kolizja jest nieusuwalna** — piekarnik i front ramienia patrzą na tę samą przestrzeń. Do zapisania w PLAN pkt 9 jako ograniczenie użytkowe („piekarnik otwarty = ramię niedostępne"), a nie do udawania, że go nie ma.

**[E28] [BŁĄD] Otwarta zmywarka blokuje jedyny front szafki narożnej DC1 — nakładka 345 × 345 mm**
- **norma/zalecenie:** `SKILL.md` §Twarde zasady pkt 6: *„**Zmywarka** — otwarty front nie może blokować przejścia ani drzwi; **nie w narożniku bez odstępu na otwarcie sąsiednich szuflad**"*.
- **w projekcie:** DB2 stoi **w samym narożniku** — jej wschodni bok (x=2000) jest tożsamy z płaszczyzną lica DC1. Front zmywarki opadając zajmuje pas x 1550→2000, y 600→~1380. Ćwiartka wychyłu drzwi DC1 (front 345, lico x=2000) to obszar x 1655→2000, y 600→945. **Nakładka 345 × 345 mm.**
- **dowód:** `_kontrola.py`: `DB2 zmywarka 45 (1550,0,2000,600)`, `DC1 narożna ślepa (2000,0,2546,945) lico="W" front=(600,945)`; PLAN §5: *„DB2 … **1550→2000** … wcina się ~54 w strefę narożnika z C"*.
- **konsekwencja:** żeby schować sztućce z rozładowywanej zmywarki do DC1, musisz **najpierw zamknąć zmywarkę**. To jest odwrócenie zasady z PLAN §5a: *„Zasada: rozładunek zmywarki jednym obrotem"*. Dodatkowo: to jest **przyczyna źródłowa** całej sprawy front-345 / brak cargo narożnego z v3.11 — nie „niefortunna szerokość frontu", tylko naruszenie reguły „zmywarka nie w narożniku".
- **rekomendacja:** patrz **E38** — przesunięcie ciągu B o 150 mm na zachód rozwiązuje E28 i E37 jednocześnie.

**[E29] [RYZYKO] DA1 front 240 mm — maksimum jest policzone poprawnie, ale zapas to 10 mm**
- **norma/zalecenie:** `standardy-meble.md` §Szerokości typowe: *„150, 200, **300**, 400, …"* — 240 nie jest wymiarem modułowym; `uklady-kuchni.md` §1 (L): *„narożnik = cargo narożne / carousel; **nie marnuj go**"*.
- **w projekcie:** front **240** (y 610→850), reszta lica zamknięta blendą **610 mm**.
- **dowód:** `_kontrola.py`: `DA1 narożna ślepa (155,0,560,850) lico="E" front=(610,850)`; BLENDY `"ciąg A": [(0,610)]`; PLAN §5: *„Front max 240: szersze drzwi uderzyłyby w korpus ciągu okna (**zapas 13 mm**)"*.
- **weryfikacja własna:** zawias na y=850, skrzydło wychyla się na wschód; skrajny narożnik skrzydła w pozycji zamkniętej leży na y = 850 − W. Lico ciągu B jest na y=600, pierwszy korpus B (DB0) zaczyna się na x=600 → warunek `850 − W > 600` daje **W_max = 250**. Projekt: 240 → **zapas 10 mm**, nie 13. Ograniczenie jest realne, liczba w PLAN o 3 mm optymistyczna.
- **konsekwencja:** **42% lica ciągu A (610 z 1450 mm) to blenda bez dostępu.** Skrzydło 240 przy 90° zajmuje pas x 560→800 na wysokości y≈850, czyli staje w korytarzu przed piekarnikiem. Zapas 10 mm nie zniesie krzywizny ściany B (`technologia-wykonania.md` §2: *„odchyłka 5–15 mm na 2 m to norma"*) — **drzwi mogą po prostu nie otworzyć się do końca**.
- **rekomendacja:** (1) zmniejszyć front do **230** i przyjąć zapas 20 mm — strata pojemności zerowa, ryzyko montażowe znika; (2) zamówić zawias **155°** także do DA1 (FORMATKI ma 155° tylko dla DC1) — przy skrzydle stojącym na 155° nie blokuje ono korytarza przed piekarnikiem; (3) zawias **musi** być po stronie południowej (y=850) — PLAN to podaje ✓ i jest to jedyny poprawny wariant (zawias północny zasłoniłby dostęp do części ślepej).

**[E30] [BRAK] Kierunki otwierania nieokreślone dla większości frontów**
- **norma/zalecenie:** `dokumentacja-stolarz.md` §9: tabela AGD ma zawierać *„uwagi o otwieraniu"*; `analiza-pomieszczenia.md`: *„Kierunek otwierania … jeśli nie widać zawiasów/klamki — `[?]`"*.
- **w projekcie — określone:** DA1 (*„Zawias przy stronie południowej"*), lodówka (*„zawiasy od strony ścianki, drzwi otwierane ku oknu"*). **Nieokreślone:** DC1, RL1 (drzwi 300), DB1 (2 skrzydła 397), C2, C4, wszystkie górne GA1–GA4, GC1–GC2.
- **dowód:** PLAN §5, kolumna „Front / wnętrze" — brak wpisów; FORMATKI §3 zamawia 36 zawiasów bez przypisania stron.
- **konsekwencja:** przy montażu samodzielnym i nawiertach CNC zamawianych w KornerGo (**puszki 35 pod zawiasy w rozkroju** — FORMATKI §4 pkt 1) strona zawiasu jest wiercona fabrycznie. Zła strona = front do wyrzucenia. Ergonomicznie krytyczne są dwa przypadki:
  - **RL1 drzwi 300** — dostęp do martwego pola pod ramieniem prowadzi **na zachód**, więc zawias musi być po stronie **wschodniej (x≈876)**; zawias zachodni (x=576) postawi skrzydło dokładnie w torze sięgania.
  - **DC1 front 345** — obie strony kolidują z otwartą zmywarką (E28); zawias przy y=945 stawia skrzydło przy słupku C2, zawias przy y=600 — w pasie zmywarki. Wybór: **y=945 z zawiasem 155°** (jest na liście).
- **rekomendacja:** uzupełnić PLAN §5 o kolumnę „strona zawiasu" dla **każdego** frontu przed zamówieniem CNC; dopisać do `_kontrola.py` pole `zawias` i wymusić w K3, żeby brak wartości był błędem, a nie domyślnym „byle która strona przejdzie".

**[E31] [BRAK] Kontrola K3 z założenia pomija AGD, szuflady i fronty uchylne**
- **norma/zalecenie:** `protokol-weryfikacji.md` tabela: *„K3 | każdy front ma zawias, przy którym się otworzy"*.
- **w projekcie:** `_kontrola.py` linia 206: `if not m.front or m.typ in ("AGD", "szuflady", "uchylny"): continue`. Wyklucza to: **lodówkę C3, zmywarkę DB2, piekarnik DA2, cargo DB0, słupek C2, szuflady RL1 i DC1** — czyli wszystkie fronty, które w tej kuchni realnie kolidują (E10, E27, E28).
- **dowód:** kod wyżej; wynik uruchomienia: `PASS — 9 kontroli, 0 błędów, **0 uwag**`, mimo trzech policzonych wyżej kolizji.
- **konsekwencja:** **skrypt daje PASS kuchni, w której otwarta lodówka blokuje wejście, otwarta zmywarka blokuje jedyną szafkę narożną, a otwarty piekarnik blokuje jedyne szuflady.** Zaufanie do „PASS" jest w tym momencie nieuzasadnione — a `SKILL.md` pkt 12 workflow czyni z tego PASS warunek wysłania rysunku.
- **rekomendacja:** rozszerzyć K3 o pole `wysuw` (patrz E27) i o skrzydła AGD; do czasu poprawki **dopisać w nagłówku `_kontrola.py`, czego skrypt NIE sprawdza** — dziś docstring wymienia 7 klas błędów jako sprawdzane i nie ma ani słowa o wyłączeniach.

---

### 2.8. Dostępność narożników ślepych

**[E32] [BŁĄD] DA1 dostaje w planie funkcjonalnym „garnki i duże naczynia", a przez otwór 240 mm garnek nie przechodzi**
- **norma/zalecenie:** [praktyka] garnek 5 l ma Ø ≈ 240 mm, patelnia 28 cm z rączką ≈ 280 mm + uchwyt; światło otworu = szerokość frontu − luzy ≈ **230 mm**.
- **w projekcie:** front **240 mm**, funkcja: PLAN §5a: *„DA1 narożna ślepa (front 240) | **garnki i duże naczynia — 248 l tuż przy indukcji** (v3.10); dostęp drzwiami + sięg w głąb"*.
- **dowód:** cytat wyżej + `front=(610,850)` w modelu.
- **konsekwencja:** **garnek Ø240 nie przejdzie przez otwór 230.** Zmieszczą się wyłącznie naczynia do ~Ø200 i to wsuwane pod kątem. Pojemność „248 l" (moja weryfikacja: 405 × 850 × 690 = **238 l**) jest prawdziwa geometrycznie i nieprawdziwa użytkowo. To jest **identyczny mechanizm jak luka wykryta w v3.12** („plan funkcjonalny opisywał moduły, których już nie ma") — tylko o poziom niżej: moduł istnieje, funkcja przez niego nie przechodzi.
- **rekomendacja:** (1) zmienić przypisanie DA1 na **„naczynia i sprzęt rzadko używany, wsuwane pojedynczo"**; (2) dodać do `_kontrola.py` kontrolę **K10 — gabaryt vs otwór**: funkcje dostają wymagane światło (`garnki: 300`, `blachy: 400`, `sztućce: 250`), sprawdzane przeciw szerokości frontu — dokładnie tak, jak K8 robi to dla okuć.

**[E33] [RYZYKO] Realna użyteczność DA1: ~40% deklarowanej pojemności**
- **norma/zalecenie:** [antropometria] sięg boczny w głąb szafki dolnej, w klęku, przez otwór 240: pewny chwyt ~350–400 mm, dotknięcie ~600.
- **w projekcie:** PLAN §5 deklaruje *„sięg w ślepą część **600**"*; część ślepa to y 0→610 przy korpusie 405 gł.
- **dowód:** `DA1 (155,0,560,850)`, `front=(610,850)`.
- **konsekwencja:** z 238 l realnie obsłużysz ~90–100 l (strefa y 350→850). Reszta to magazyn typu „raz w roku, na czworakach, po omacku".
- **rekomendacja:** wyposażyć DA1 w **wysuwaną tacę/kosz na dnie** (nawet zwykła szuflada wewnętrzna 200 szer. × 400 gł. na prowadnicy) — to podnosi dostępny procent bez zmiany geometrii; zamówić przy okazji szuflad do DC1.

**[E34] [BŁĄD] Martwe pole pod ramieniem — „ciężki sprzęt" dostępny wyłącznie bokiem, przez otwór 300, na głębokość 576**
- **norma/zalecenie:** [praktyka] przedmioty ciężkie (robot, mikser, garnki żeliwne) muszą mieć dostęp **czołowy**, na wyprost; wyciąganie ciężaru bokiem w klęku z 576 mm to obciążenie kręgosłupa w skręcie.
- **w projekcie:** pole x 0→576, y 1450→1950 (**576 × 500 × ~690 = 199 l**), dostęp **bokiem**, przez drzwi 300 z frontu RL1.
- **dowód:** PLAN §5 ciąg A: *„ślepy narożnik pod ramieniem | 1450→1950 × 560 | **bez frontu** | dostęp bokiem przez RL1"*; PLAN §5a: *„DRZWI 300 obok: dostęp bokiem do martwego pola pod ramieniem (**~202 l — patelnie, blachy, ciężki sprzęt**)"*.
- **konsekwencja:** funkcja „ciężki sprzęt" jest w najgorzej dostępnym punkcie całej kuchni. Do tego pole to jednocześnie ćwiartka, w której stoi otwarte skrzydło RL1 i drzwi piekarnika (E27).
- **rekomendacja — patrz E35 (rozwiązanie istnieje i jest tanie).**

**[E35] [ULEPSZENIE] Martwe pole pod ramieniem można otworzyć od strony korytarza — 199 l w pełni dostępnej przestrzeni za cenę zamiany panelu na fronty**
- **norma/zalecenie:** `uklady-kuchni.md` §1 (L): *„narożnik … **nie marnuj go**"*.
- **w projekcie:** południowe lico ramienia (y=1950, x 0→1176) jest dziś zamknięte **panelem ryflowanym 1176×910**, a za nim leży 199 l martwej przestrzeni. Po południowej stronie jest **wolny korytarz** (PLAN §3: *„Za linią: otwór do salonu (127) i korytarz"*), a nie ściana.
- **dowód:** FORMATKI §1: *„Panel ryflowany ramienia (lamele — dostawca zewn.) | **1176×910** | ciemny orzech mat"*; `_kontrola.py`: `LINIA_POLUDNIOWA = 1950`, `RL1 … y1=1950`; PLAN §5 ramię: *„panel ryflowany | rewers: od salonu (południe) i od korytarza"*.
- **konsekwencja przy dzisiejszym rozwiązaniu:** 199 l dostępne wyłącznie bokiem (E34).
- **rekomendacja:** wykonać panel ryflowany na odcinku **x 0→576 jako dwoje drzwi (albo 2 szuflady)** otwieranych od południa, z tym samym lamelowym licem. Zysk: **199 l w pełni dostępnej przestrzeni czołowej**, głębokość 500 (idealna na garnki i blachy), zero ingerencji w geometrię, zero wpływu na przejście 600 (fronty otwierają się na południe, w korytarz, poza kuchnię). Koszt: podział panelu + 4 zawiasy albo 2 kpl prowadnic, plus przegroda w korpusie RL1 na x=576. **Zastrzeżenia do zapisania:** (a) fronty otwierają się w trakt komunikacyjny korytarza — sprawdzić pole wymachu wobec otworu do salonu 127; (b) po tej zmianie drzwi 300 w RL1 tracą sens → **cały front 600 RL1 można zamienić na 3 szuflady pełnej szerokości 600** (E43) — czyli ta jedna poprawka rozwiązuje też problem braku szuflad na garnki.

**[E36] [RYZYKO] DC1 — 74% objętości poza szufladami, przy jedynym froncie 345 mm**
- **norma/zalecenie:** `_kontrola.py` `MIN_OTWARCIA = {"cargo narożne": 450, "karuzela": 450, "szuflady wewnętrzne": 300}` (K8).
- **w projekcie:** korpus **945 × 546**, front **345**, wnętrze: 2 szuflady wewnętrzne ~300 szer. × 450 gł.
- **dowód:** `DC1 narożna ślepa (2000,0,2546,945) front=(600,945) okucie="szuflady wewnętrzne"`; PLAN §5: *„**korekta v3.11 (kontrola K8):** front ma tylko 345 mm — pas 0→600 lica jest zasłonięty korpusem zmywarki. **Cargo narożne (magic corner) NIE wejdzie** … narożnik północny ~236 l zostaje na sięg ręką"*.
- **konsekwencja (policzona):** szuflady zajmują w rzucie 300 × 450 = 0,135 m² z 0,516 m² rzutu korpusu → **26% wykorzystania, 74% na „sięg ręką"**. PLAN nazywa to uczciwie (236 l na sięg), ale przypisuje tam funkcje „sztućce zapasowe, sztućce serwisowe" — czyli rzeczy, po które sięga się regularnie, do szafki, którą blokuje otwarta zmywarka (E28).
- **rekomendacja:** patrz E37 — przyczyna jest usuwalna.

**[E37] [ULEPSZENIE] Przesunięcie ciągu B o 150 mm na zachód odblokowuje magic corner w DC1 i zdejmuje kolizję ze zmywarką**
- **norma/zalecenie:** `SKILL.md` pkt 6 (zmywarka nie w narożniku) + K8 (cargo narożne ≥450).
- **stan dzisiejszy:** DB0 600–750, DB1 750–1550, DB2 1550–2000, lico DC1 zasłonięte na 0→600, front DC1 = **345**.
- **wariant proponowany:** zrezygnować z **DB0 cargo 150** (przyprawy przenieść do GA2, która wg PLAN §5a i tak trzyma *„herbaty, kawa, cukier"* — funkcja „przyprawy ≥100" z K9 zostaje spełniona przez front GA2 180). Wtedy: **DB1 zlew 800 na 600–1400**, **DB2 zmywarka 1400–1850**, **blenda 1850–2000**.
- **wynik policzony:** lico DC1 zasłonięte tylko na 0→450 → **front DC1 = 945 − 450 = 495 mm ≥ 450 ✓** → **magic corner wchodzi** (K8 spełnione bez obchodzenia). Otwarta zmywarka (x 1400–1850) przestaje leżeć w płaszczyźnie lica DC1 (x=2000) — między nimi 150 mm blendy → **kolizja z E28 znika**. Zysk pojemnościowy: magic corner udostępnia ~60–70% narożnika zamiast 26%.
- **koszty i warunki do sprawdzenia (uczciwie):** (a) zlew przesuwa się na 600–1400 — **komora musi być dosunięta do wschodniej krawędzi (x 950–1400)**, żeby zachować regułę „≥450 od rogu" (950 − 600 = 350 → **za mało; potrzeba zlewu 700 na 700–1400 albo komory na 1050–1400**) — do przeliczenia; (b) komora musi zostać pod oknem (752→1608) ✓; (c) znika cargo przyprawnik — inwestor go chciał, więc to decyzja jego, nie moja; (d) bok trójkąta zlew–płyta się skraca — **sprawdzić, czy nie zejdzie poniżej 1200** (przy komorze 1050–1400, środek 1225, płyta 295/1150 → bok = √(930² + 850²) = **1260 ✓**).
- **rekomendacja:** przedstawić inwestorowi jako wariant „cargo przyprawnik ↔ magic corner + odblokowana szafka narożna przy zmywarce". Wymaga przeliczenia w `_kontrola.py` przed przedstawieniem.

---

### 2.9. Szuflady vs półki

**[E38] [BŁĄD] W całej kuchni nie ma ani jednej szuflady, do której zmieści się garnek**
- **norma/zalecenie:** [praktyka] szuflada na garnki: szerokość korpusu **600–800**, światło ≥520, wysokość boku ≥ K (128,5 wg `standardy-meble.md`); minimum branżowe to jeden blok szufladowy 600 przy strefie gotowania.
- **w projekcie — pełna inwentaryzacja frontów szufladowych:**

| Moduł | Front szufladowy | Szer. wnętrza | Uwaga |
|---|---|---|---|
| RL1 | 3 × **300** | ~230 | wkład na sztućce w górnej |
| DA2 | 1 × 600, **wysokość frontu 110** | ~560 | wg FORMATKI: *„front szuflady dolnej | **596×110**"* — na blachy płasko, nie na garnki; **i tak się nie mieści (E39)** |
| DC1 | 2 × ~300 wewnętrzne, za drzwiami 345 | ~230 | narożnik ślepy |
| **razem realnie użytecznych frontów szufladowych** | **300 mm** | | |

- **dowód:** PLAN v3.12a: *„Nominały: **RL1 3×400, DA2 1×500, DC1 2×450**"*; FORMATKI §3: *„System szuflad … nom. 400 | **3 kpl** | RL1 ramię — **korpus 300 szer.**"*; PLAN §5a: DA1 = *„drzwi + 1 półka"*.
- **konsekwencja:** garnek Ø240 nie mieści się w szufladzie 300 (światło ~230), nie mieści się w DA1 (otwór 240 — E32), nie mieści się w szufladzie DA2 (front 110). **Jedyne miejsce na garnki to martwe pole pod ramieniem, dostępne bokiem (E34).** Suma frontów dolnych bez AGD = 240 + 600 + 600 + 150 + 800 + 345 = **2735 mm**, z czego szufladowych realnie **300 mm = 11%** — przy zaleceniu branżowym ≥50–60% dla dolnej zabudowy.
- **rekomendacja:** **E35 + E43 razem to rozwiązują**: front ramienia od korytarza (576 szer., 500 gł.) na garnki + RL1 600 jako 3 szuflady pełnej szerokości. To jedyna kombinacja w tej geometrii, która daje szufladę o świetle >500.

**[E39] [BŁĄD] Szuflada pod piekarnikiem w DA2 nie mieści się w bilansie pionowym korpusu**
- **norma/zalecenie:** `standardy-meble.md`: piekarnik nisza **560 × 590–600**; korpus dolny **720**; system szuflad z metalowymi bokami wymaga ~**120 mm** światła w pionie (bok najniższy ~84 + prowadnica + luzy).
- **w projekcie:** PLAN §5: *„DA2 | **indukcja + piekarnik** | 600×820×560 | **front piekarnika + szuflada**"*; PLAN §5a: *„DA2 60 | piekarnik + **szuflada na blachy/formy**"*; FORMATKI §1: *„front szuflady dolnej | **596×110**"*; FORMATKI §3: *„System szuflad … **nom. 500** | 1 kpl | DA2 — szuflada pod piekarnikiem, korpus 600 szer., 560 gł."*.
- **bilans policzony:** korpus 720 − 18 (dno) − 18 (trawers nośny piekarnika) − 595 (nisza piekarnika) − ~18 (strefa płyty pod blatem; płyta 56 przy blacie 38 wchodzi 18 w korpus) = **71 mm światła**. Potrzeba ≥120. **Deficyt ~50 mm.** Nawet bez piekarnika na styk: przy niszy 590 zostaje 76.
- **dowód:** liczby wyżej + FORMATKI §1 DA2: *„bok | **560×720**"*, *„trawers nośny piekarnika | 564×560"*, *„dno | 564×560"*.
- **konsekwencja:** zamówiony 1 kpl prowadnic nom. 500 do DA2 nie ma gdzie wejść; front 596×110 nie zamknie 71 mm światła. Praktycznie **kuchnia traci ostatnią szufladę poza RL1** — a to właśnie ta miała trzymać blachy do piekarnika, czyli rzecz używaną przy samym piekarniku.
- **rekomendacja:** (1) przeliczyć bilans pionowy DA2 z **kartą montażową konkretnego piekarnika** (PLAN §7 sam wymaga *„przegroda od płyty wg karty"*, ale nie podaje modelu piekarnika — patrz E40); (2) jeżeli bilans się nie domknie: skreślić szuflady z DA2 i przenieść blachy do **odzyskanego pola pod ramieniem od korytarza (E35)** — leży 500 mm od piekarnika; (3) usunąć z FORMATKI §3 pozycję „nom. 500 — DA2" do czasu rozstrzygnięcia.

**[E40] [BRAK] Piekarnik nie ma modelu ani wymiarów**
- **norma/zalecenie:** `dokumentacja-stolarz.md` §9: tabela AGD musi rozróżniać *„szerokość korpusu 600 od niszy 560, nigdy nie łącz w jedno »otwór«"*.
- **w projekcie:** PLAN §7: *„Piekarnik | DA2, pod płytą | nisza 560×590–600; osobny obwód 16A; przegroda od płyty wg karty"* — **żadnego modelu, żadnych wymiarów urządzenia, brak statusu `[P]/[~]/[?]`**. Indukcja ma model i wymiary `[P]`, lodówka ma `[P]`, zmywarka ma tylko szerokość.
- **dowód:** cytat wyżej; PLAN §2 tabela wymiarów nie zawiera wiersza „piekarnik".
- **konsekwencja:** bez wysokości urządzenia i wymaganego odstępu od spodu płyty **nie da się rozstrzygnąć E39** ani ustalić, na jakiej wysokości znajdzie się dolna krawędź drzwi piekarnika.
- **rekomendacja:** dopisać piekarnik do PLAN §2 i §7 ze statusem `[?]` i wpisać na listę pomiarów/decyzji pkt 11.

**[E41] [RYZYKO] Piekarnik pod płytą — dolna krawędź drzwi ~215–245 mm nad podłogą**
- **norma/zalecenie:** `uklady-kuchni.md` §4: *„Drzwi piekarnika w słupku | wysokość frontu 590–600 **na wys. 700–900 (dolna krawędź)** | uchylne w dół, przestrzeń przed ≥1000"*.
- **w projekcie:** piekarnik pod płytą → dolna krawędź niszy ~**215–245 mm** od podłogi (bilans z E39), czyli **~470–685 mm poniżej dolnej granicy zalecenia**.
- **dowód:** PLAN §9a wariant B: *„~~B) Piekarnik do słupka C2~~ (odrzucone) (**zabudowa wysoka, na wysokości oczu — wygodniejsze przy schylaniu**)"*.
- **konsekwencja:** wyjmowanie gorącej blachy 40×35 z poziomu ~250 mm, na wyprostowanych rękach, przy wzroście 182 cm — pełny skłon z obciążeniem, powtarzany przy każdym pieczeniu. Do tego przestrzeń przed piekarnikiem jest zajęta przez ramię i frontem RL1 (E27). Wariant B został odrzucony świadomie (koszt: słupek traci cargo/spiżarkę) — **nie kwestionuję decyzji**, ale konsekwencja nie jest zapisana w pkt 9 „Ryzyka".
- **rekomendacja:** dopisać do PLAN pkt 9: *„piekarnik pod blatem — dolna krawędź ~24 cm; obsługa wymaga pełnego skłonu; strefa odstawcza dla blach = blat ramienia (514 mm na południe od płyty)"*. Rozważyć piekarnik z **drzwiami chowanymi (slide&hide)** — skraca ramię dźwigni przy wyjmowaniu blachy.

**[E42] [BŁĄD] Oznaczenia wysokości boków szuflad niezgodne z własną referencją projektu**
- **norma/zalecenie:** `standardy-meble.md`: *„Szuflady Blum Legrabox — wysokości boków (nomenklatura Blum): **N ≈ 66,5 / M ≈ 90,5 / K ≈ 128,5 / C ≈ 193 mm** (oznaczenie »H« nie istnieje)"*.
- **w projekcie:** FORMATKI §3: *„System szuflad z metalowymi bokami, nom. 400 | 3 kpl | RL1 ramię … **górna niska (H≈86)** pod wkład na sztućce, **dwie M (≈135)**"*; PLAN v3.12a: *„górna szuflada RL1 niska (**H≈86**) pod wkład na sztućce 300"*.
- **dowód:** cytaty wyżej.
- **konsekwencja:** „H" nie istnieje (referencja mówi to wprost), a „M ≈ 135" jest sprzeczne z M ≈ 90,5 — 135 odpowiada raczej K ≈ 128,5. Zamówione zostaną boki o złej wysokości → podział frontu 716 na trzy szuflady nie zamknie się, a wkład na sztućce (wys. ~50) albo nie wejdzie, albo zmarnuje 40 mm.
- **rekomendacja:** przeliczyć podział frontu RL1: 716 = np. 145 (N/niska) + 2 × 283 (K), fugi 3×2; zamówić boki wg nomenklatury producenta, którego się wybierze (GTV Modern Box / Rejs mają **własne** oznaczenia — nie mieszać ich z Blum), i zapisać w FORMATKI producenta obok nominału. FORMATKI już zawiera właściwe zastrzeżenie (*„Nominały prowadnic [do potwierdzenia w karcie producenta]"*) — rozszerzyć je na wysokości boków.

**[E43] [ULEPSZENIE] Front RL1 600 podzielony 300+300 — po odzyskaniu pola od korytarza podział traci sens**
- **norma/zalecenie:** [praktyka] szuflada 300 obsługuje sztućce i drobiazgi; naczynia i garnki wymagają ≥600.
- **w projekcie:** *„front 600: **drzwi 300 + szuflady 300**"* (PLAN §5, RL1) — drzwi 300 służą wyłącznie dostępowi bokiem do martwego pola (E34).
- **dowód:** `RL1 … front=(576,1176), funkcje=("sztućce","przybory")`; PLAN §5a wiersz RL1.
- **konsekwencja:** jedyny blok szufladowy w kuchni ma 300 mm szerokości, bo połowę frontu zjada dostęp do pola, które i tak jest niedostępny.
- **rekomendacja:** po wykonaniu E35 (fronty od korytarza) **zamienić cały front 600 RL1 na 3 szuflady 600**: górna niska (sztućce, wkład 300 + drugi wkład na przybory), środkowa K (przybory/noże), dolna K/C (**garnki — światło ~520, mieści Ø240 ✓**). To jest jedyna zmiana w całym projekcie, która likwiduje E38.

**[E44] [RYZYKO] Wszystkie górne na półkach 400 mm głębokości**
- **norma/zalecenie:** `standardy-meble.md` §Biblioteka/regał: *„Głębokość: 300 (książki), 350-400"* — przy 400 tylna część półki nad wysokością barku jest poza polem widzenia.
- **w projekcie:** GA1 (245 gł., półki 300 — czyli **półka głębsza niż korpus? 633×300 w FORMATKI to szer.×gł.** ✓ 300 gł. przy korpusie 245 jest błędem formatki, ale to poza moim zakresem), GA2, GA4, GC1, GC2 — wszystkie **korpus 400, półki 300 gł.**, po **2 półki** na korpus 998.
- **dowód:** FORMATKI §1: *„GA2 górna wąska — półki | **143×300**"*, *„GA4 — półki | 463×300"*, *„GC1 — półki | 433×300"*, *„GC2 — półki | 440×300"*, *„GA1 — półki | **633×300**"* przy boku GA1 245×998.
- **konsekwencja:** (a) 2 półki na 998 mm dają rozstaw ~330 mm i **trzy poziomy: 1480 / 1810 / 2140 + wieniec 2478** — poziom 2140 i cała przestrzeń nad nim (338 mm) są w strefie stołka (E25); (b) półka 300 gł. w korpusie 400 zostawia 100 mm nieużytku z tyłu na całej długości; (c) GA1 ma półki 300 przy korpusie 245 — **formatka szersza niż korpus**.
- **rekomendacja:** przejść na **3 półki** w GC1/GC2 z rozstawem 1480/1750/2000/2250 i osobnym frontem antresoli 2000+; poprawić półki GA1 na ≤227 gł.; półki w pozostałych na 380.

---

### 2.10. Pozostałe braki w zakresie ergonomii

**[E45] [BRAK] Brak oświetlenia zadaniowego nad ciągiem B (zlew) i nad ramieniem**
- **norma/zalecenie:** [praktyka / PN-EN 12464-1] powierzchnie robocze w kuchni: **300–500 lx**; oprawa nad każdą strefą roboczą (zmywanie, przygotowanie, gotowanie).
- **w projekcie:** FORMATKI §3: *„Taśma LED 3000K + profil + zasilacz 24V | ~3 mb + 1 szt | **pod GA i GC**"*. Nad ciągiem B **nie ma górnych** (PLAN §5: *„bez górnych na B — okno do sufitu"*), więc **nad zlewem nie ma żadnej oprawy zadaniowej**. Ramię ma LED tylko na odcinku x 0→419 (spod GA4) z 1176.
- **dowód:** cytaty wyżej.
- **konsekwencja:** przy zlewie i przy głównym blacie przygotowania (ramię, po E01) pracujesz we własnym cieniu rzucanym przez oświetlenie sufitowe zza pleców. To najczęstsza skarga po odbiorze kuchni i najdroższa do naprawy po ułożeniu fartucha.
- **rekomendacja:** (1) profil LED **w podcięciu parapetu** albo listwa nad oknem nad zlewem (752→1608); (2) LED na całej długości ramienia — najprościej **w listwie pod blatem ramienia od strony wnętrza U** lub oprawa wisząca; (3) doprowadzić zasilanie razem z gniazdem do ramienia (PLAN pkt 8.4 — przed posadzką!).

**[E46] [BRAK] Ręczność użytkownika nieokreślona**
- **norma/zalecenie:** `uklady-kuchni.md` §3 pkt 3: *„zmywarka ≤900 od zlewu, **po stronie ręki dominującej**"*.
- **w projekcie:** zmywarka po **wschodniej** stronie zlewu (PLAN v3.3: *„zmywarka 45 po wschodniej stronie zlewu"*). Stojąc przodem do okna wschód jest po **prawej** ✓ dla praworęcznego. **Nigdzie nie zapisano, czy inwestor jest praworęczny.**
- **dowód:** PLAN §5, wiersz DB2; brak wzmianki o ręczności w całym PLAN.
- **konsekwencja:** jeśli użytkownik jest leworęczny, ustawienie zmywarka-wschód i ociekacz-zachód (E07) należy odbić — a wtedy komora wraca na zachód i **bok trójkąta spada do 1073 mm, poniżej twardego progu** (E07).
- **rekomendacja:** dopisać do PLAN §2 wiersz „ręczność użytkownika `[?]`" i zadać pytanie **przed** ustaleniem pozycji komory.

**[E47] [RYZYKO] FORMATKI-ROBOCZE.md to wersja v3.5 i jest sprzeczna z PLAN v3.12a — także sama ze sobą**
- **norma/zalecenie:** `protokol-weryfikacji.md` §1: *„Wymiary modułów **NIE mogą żyć równolegle w trzech miejscach** … zawsze się rozjadą. … wypisz obok siebie sumy modułów z PLAN.md i z generatora formatek. **Muszą się zgadzać co do milimetra.**"*
- **w projekcie — wykryte rozjazdy:**

| Element | PLAN v3.12a / model | FORMATKI-ROBOCZE.md | Skutek |
|---|---|---|---|
| front DA1 | **240** + blenda 610 | *„front | **446**×716"* + *„blenda ślepa | **430**×716"* + osobno *„Blenda dolna A przy pilastrze (~610 do frontu DA1) | 610×756"* | front 446 **fizycznie się nie otworzy** (max 250 — E29); trzy elementy lica sumują się do 1486 przy licu 1450 |
| front RL1 | drzwi **300** + szuflady **300** | *„front | **446**×716"* + *„blenda ślepa | 430×716"* | podział z v3.12 w ogóle nie istnieje w formatkach |
| RL2 | usunięty w v3.8 | §4 pkt 6: *„Ramię: **RL1+RL2** skręcone"* | moduł-widmo w planie montażu |
| głębokość blatu | 600 | **635** | E12 |
| długość ramienia | 1176 | 635 + 545 = **1180** | E13 |
| DC1 okucie | 2 szuflady wewnętrzne (v3.11) | §1: front 446 + blenda 430; §3: szuflady wewnętrzne ✓ | §1 i §3 **tego samego pliku** opisują różne moduły |

- **dowód:** wszystkie cytaty z FORMATKI-ROBOCZE.md §1–§4; nagłówek pliku: *„Lista formatek i okuć — kuchnia **v3.5** (WERSJA ROBOCZA R1)"*.
- **konsekwencja:** plik nosi ostrzeżenie *„NIE DO CIĘCIA"* ✓, ale **§3 (okucia) został zaktualizowany do v3.12a, a §1 (formatki) został na v3.5** — czyli jest to dokument, który wygląda na aktualny i nim nie jest. Przy montażu samodzielnym to najbardziej prawdopodobne źródło błędu wykonawczego w całym projekcie: front DA1 446 mm zamawiany z nawiertami CNC, którego nie da się otworzyć.
- **rekomendacja:** **przegenerować FORMATKI z `_formatki.py` zasilanego modelem z `_kontrola.py`** (jedno źródło prawdy) albo — do czasu pomiarów — **usunąć §1 i §2 i zostawić wyłącznie §3 i §4**, zgodnie z regułą z `formatki.md`: *„lista formatek powstaje WYŁĄCZNIE po pomiarach kontrolnych. Nigdy z projektu koncepcyjnego."*

---

## 3. Podsumowanie liczbowe zarzutów

Pozycji łącznie: **47** (E01–E47).

| Kategoria | Liczba | Numery |
|---|---|---|
| **BŁĄD** | **18** | E01, E03, E06, E07, E08, E10, E12, E13, E14, E22, E24, E27, E28, E32, E34, E38, E39, E42 |
| **RYZYKO** | **16** | E02, E09, E11, E15, E16, E19, E20, E21, E25, E26, E29, E33, E36, E41, E44, E47 |
| **BRAK** | **7** | E04, E17, E30, E31, E40, E45, E46 |
| **ULEPSZENIE** | **4** | E05, E35, E37, E43 |
| *ZGODNE (bez zarzutu, opisane z liczbami)* | *2* | *E18 (odstępy poziome płyty), E23 (blat 910)* |

**W tym naruszone TWARDE PROGI z `uklady-kuchni.md`: 2** — E08 (U między ramionami ≥1200 → 850/815) oraz E09 (przejście komunikacyjne / obok barku ≥900 → 600; decyzja świadoma inwestora).

---

## 4. RANKING — 5 najpoważniejszych problemów ergonomicznych

### 1. [E01] Kuchnia nie ma strefy przygotowania — między zlewem a płytą jest 150 mm blatu
Norma własna projektu (`uklady-kuchni.md` §3): **min 600, optymalnie 900–1200 ciągłego blatu**. W projekcie **150 mm** po stronie płyty i 450 mm po stronie zmywarki (znikające przy otwartej zmywarce). To brak jednej z pięciu stref funkcjonalnych, nie detal. Dodatkowo narożnik A/B, który wygląda w metrażu jak blat, leży **1042 mm od barku** z każdej pozycji roboczej — czyli poza zasięgiem. **Naprawa nie wymaga zmiany geometrii:** przypisać strefę przygotowania do blatu ramienia (757 × 500 mm wolne spod GA4), doprowadzić tam gniazdo i światło, zapisać w planie funkcjonalnym. Kosztem jest obrót 180° od zlewu — dla jednej gotującej osoby akceptowalny, ale **musi być świadomy**.

### 2. [E08] Strefa robocza przy zlewie 850 mm (albo 815) — naruszony twardy próg 1200
Trzy progi naruszone jednocześnie: **U ≥1200 (TWARDY PRÓG)**, półwysep ≥1000, przejście robocze ≥1050. W projekcie 1450 − 600 = **850**, a przy głębokości blatu z FORMATKI (635) — **815**. Deficyt **350–385 mm wobec twardego progu**. PLAN §4 wpisuje w tym wierszu ocenę „~ akceptowalne" wobec progu „≥110 robocze" podanego w tym samym wierszu — czyli ocenę pozytywną dla wartości 250 mm poniżej własnego progu. Skutek praktyczny: **przy otwartej szafce zlewowej nie wysuniesz szuflady RL1** (E11: 930 mm między licami, potrzeba ≥1200). **Najtańsza poprawka: skrócić ramię z 1176 do ≤1000** — przejście przy ściance rośnie z 600 do 776, pas 850 kończy się przed komorą zlewu, a traci się 176 mm blatu, którego w bilansie roboczym i tak nie ma.

### 3. [E38 + E32 + E39] W całej kuchni nie ma szuflady na garnki, a moduł, któremu przypisano garnki, ma otwór 240 mm
Realnych frontów szufladowych: **300 mm z 2735 mm frontów dolnych (11%)**. Garnek Ø240 nie przejdzie przez front DA1 (światło ~230 — E32), nie zmieści się w szufladzie RL1 (światło ~230), a szuflada w DA2 **nie mieści się w bilansie pionowym korpusu** (71 mm światła przy wymaganych ~120 — E39). Plan funkcjonalny przypisuje DA1 „garnki i duże naczynia — 248 l" i to jest **ten sam typ luki, który kontrola K9 wykryła w v3.12**: moduł istnieje, funkcja przez niego nie przechodzi. **Rozwiązanie istnieje i jest tanie (E35+E43):** otworzyć martwe pole pod ramieniem od strony korytarza (panel ryflowany → 2 fronty na odcinku x 0→576) — to daje **199 l w pełni dostępnej przestrzeni o głębokości 500** — i wtedy cały front 600 RL1 można zamienić na 3 szuflady pełnej szerokości (światło ~520, mieści Ø240).

### 4. [E27 + E28 + E10 + E31] Trzy blokujące kolizje frontów, których kontrola `_kontrola.py` z założenia nie sprawdza
- **piekarnik × szuflady RL1:** nakładka **243 × 400 mm** — przy otwartym piekarniku nie sięgniesz po sztućce, noże ani przybory;
- **zmywarka × jedyny front DC1:** nakładka **345 × 345 mm** — żeby schować sztućce z rozładowywanej zmywarki, musisz najpierw ją zamknąć (odwrotność zasady „rozładunek jednym obrotem" z PLAN §5a);
- **lodówka × przejście 600:** skrzydło przy 90° zostawia **170 mm** (a przy realnej głębokości lodówki 650+50 → **70 mm**) — otwarta lodówka zamyka jedyne wejście do kuchni.

Wszystkie trzy są niewidoczne dla kontroli: `_kontrola.py` linia 206 wyklucza z testu wychyłu `typ in ("AGD","szuflady","uchylny")`, a model w ogóle nie zna pojęcia wysuwu (K3 bada tylko pas 50 mm przed licem). **Skrypt raportuje `PASS — 0 błędów, 0 uwag` dla kuchni z trzema blokującymi kolizjami** — a `SKILL.md` czyni z tego PASS warunek wysłania rysunku. Model zaniża też głębokość lodówki o 100 mm (600 zamiast 650+50). To jest **luka tej samej klasy, dla której K3 w ogóle powstała** (drzwi piekarnika za ramieniem, v3.7a).

### 5. [E47 + E12 + E13 + E24] Dokumentacja rozjechała się na cztery wymiary krytyczne dla ergonomii
`protokol-weryfikacji.md` §1 wymaga: *„sumy … muszą się zgadzać co do milimetra"*. Nie zgadzają się:
- **głębokość blatu 600 (PLAN) vs 635 (FORMATKI) vs „ramię 650" (PLAN §5) vs „65" (prompt renderu)** → strefa robocza przy zlewie ma dwie wartości (850/815), odstawcze przy płycie dwie (49/84), wolny blat pod górnymi dwie (181/216);
- **ramię 1176 (model) vs 1180 (PLAN §5 ×3, FORMATKI §2)** → przejście 600 albo **596, czyli poniżej progu inwestora**; historia PLAN v3.11 opisuje tę poprawkę jako **wykonaną**, a w treści dokumentu jej nie ma;
- **korpusy dolne 720 (nagłówki) vs 820 (wszystkie tabele modułów PLAN §5)** → blat 908/910 albo **858**, czyli **52 mm i pół pasma siatki wzrostu za nisko dla użytkownika 182 cm**;
- **FORMATKI-ROBOCZE.md to v3.5:** front DA1 **446 mm** (fizycznie nieotwieralny — maksimum to 250), front RL1 446 zamiast podziału 300+300 z v3.12, moduł-widmo RL2 w planie montażu — przy czym §3 tego samego pliku jest już zaktualizowany do v3.12a. Dokument wygląda na aktualny i nim nie jest.

Przy **wykonaniu samodzielnym** i nawiertach CNC zamawianych z rozkrojem to najbardziej prawdopodobne źródło błędu nieodwracalnego: front zamówiony z fabrycznymi puszkami, którego nie da się otworzyć.

---

## 5. Czego NIE oceniałem (granice zakresu)

- Formatki, rozkrój, obrzeża, technologia łączenia blatów — poza zakresem ergonomicznym (wyjątki: gdy wymiar formatki dowodzi zarzutu ergonomicznego — E39, E42, E47).
- Instalacje elektryczne, wodne, wentylacja, obwody — poza zakresem (wyjątki: gniazdo i światło przy strefie przygotowania — E45).
- Materiały, dekory, wycena, dostawcy.
- Pomiary pomieszczenia i ich wiarygodność (`[P]`/`[~]`/`[?]`) — przyjąłem statusy z PLAN §2 bez weryfikacji.
- Zawartość plików PDF i skryptów rysunkowych poza `_kontrola.py` i `_schemat.py`.

**Wszystkie liczby w tym raporcie pochodzą z modelu `_kontrola.py` albo z cytowanych wprost fragmentów PLAN.md / FORMATKI-ROBOCZE.md / referencji skilla. Nic nie zostało oszacowane ani dopowiedziane.**
