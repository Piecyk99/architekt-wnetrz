# Kuchnia 9.02 — analiza techniczna i plan układu (ETAP 1)

Projekt kuchni w pomieszczeniu **4,86 m²** z zaznaczoną przez inwestora intencją wyspy i lodówki w układzie L. Dokument zawiera **wyłącznie analizę techniczną i plan układu** — wizualizacje (ETAP 2) będą tworzone dopiero po akceptacji tego dokumentu.

> Wszystkie wymiary niepewne są oznaczone **[do pomiaru na miejscu]**. Nie należy zamawiać zabudowy ani sprzętu na podstawie tego dokumentu bez weryfikacji wymiarów na obiekcie.

---

## Spis treści

1. [Odczyt wymiarów i analiza geometrii](#1-odczyt-wymiarów-i-analiza-geometrii)
2. [Ograniczenia i możliwości — założenia funkcjonalne](#2-ograniczenia-i-możliwości--założenia-funkcjonalne)
3. [Trzy warianty układu](#3-trzy-warianty-układu)
4. [Wybór najlepszego wariantu](#4-wybór-najlepszego-wariantu)
5. [Szczegółowy plan techniczny (W3)](#5-szczegółowy-plan-techniczny-w3)
6. [AGD i instalacje](#6-agd-i-instalacje)
7. [Materiały i styl — 3 kierunki](#7-materiały-i-styl--3-kierunki)
8. [Błędy do uniknięcia](#8-błędy-do-uniknięcia)
9. [Lista dodatkowych pomiarów do wykonania na miejscu](#9-lista-dodatkowych-pomiarów-do-wykonania-na-miejscu)

---

## 1. Odczyt wymiarów i analiza geometrii

### 1.1 Wymiary odczytane z rzutu i szkicu

| # | Wymiar | Wartość | Źródło | Pewność |
|---|---|---|---|---|
| 1 | Powierzchnia kuchni (etykieta) | **4,86 m²** | rzut, opis pokoju | Pewne |
| 2 | Długość ściany z oknem (górna) — zewn. | **259 cm** | rzut, wymiar główny | Pewne |
| 3 | Długość ściany z oknem — wewn. | **245 cm** | rzut, wymiar wewn. | Pewne |
| 4 | Głębokość kuchni (oś krótsza) | **191 cm** | rzut, wymiar boczny | Pewne |
| 5 | Uskok w lewym górnym narożniku | **63 cm** | rzut | Pewne (geometria), funkcja niepewna |
| 6 | Wymiar w lewym dolnym narożniku | **128 cm** | rzut | Pewne |
| 7 | Długość ściany dolnej (z wejściem) | **174 cm** | rzut | Pewne |
| 8 | Szerokość wnęki dla lodówki (zazn. „L 85") | **85 cm** | rzut, adnotacja użytkownika | Pewne (zaznaczenie) |
| 9 | Lodówka (wymiary deklarowane) | **60 × 60 × 202 cm** | adnotacja użytkownika | Pewne (deklaracja) |
| 10 | Wysokość pomieszczenia | **h ≈ 250 cm** | szkic odręczny | **[do pomiaru na miejscu]** |
| 11 | Kratka wentylacyjna | ściana górna, prawa strona | szkic odręczny | **[do potwierdzenia]** |
| 12 | Okno: szerokość | brak danych | — | **[do pomiaru na miejscu]** |
| 13 | Okno: wysokość | brak danych | — | **[do pomiaru na miejscu]** |
| 14 | Okno: wysokość parapetu | brak danych | — | **[do pomiaru na miejscu]** |
| 15 | Okno: odległość od lewego/prawego narożnika | brak danych | — | **[do pomiaru na miejscu]** |
| 16 | Pion wod-kan: lokalizacja | brak danych | — | **[do pomiaru na miejscu]** |
| 17 | Przyłącze gazu (istniejące) | brak danych | — | **[do pomiaru na miejscu]** — przy wyborze indukcji do zaślepienia |
| 18 | Lokalizacja istniejących gniazdek | brak danych | — | **[do pomiaru na miejscu]** |
| 19 | Grubość ścian działowych | brak danych | — | **[do pomiaru na miejscu]** |

Weryfikacja arytmetyczna pól: 2,59 × 1,91 = 4,95 m². Pole etykietowane 4,86 m² jest niższe o ~0,09 m² — różnica wynika z uskoku 63 × 128 cm (0,08 m²). To potwierdza, że uskok znajduje się **wewnątrz pomieszczenia kuchni**, a nie jest wycinką poza nią.

### 1.2 Geometria pomieszczenia

```
                                              ┌── kratka went. (szkic)
                                              │
            ┌─OKNO────────────────────────────┴───┐
            │                                    │
    63 cm   │                                    │
   ┌────────┘                                    │ 191 cm
   │ (uskok / pion?)                             │ głębokość
   │                                             │
   │128 cm                                       │
   │                                             │
   └──────WEJŚCIE z PRZEDPOKOJU──────────────────┘
              174 cm (ściana dolna)
              <───────── 259 cm długość ──────────>
```

- **Ściana górna** (długa, 259 cm): jedyna ściana z oknem. Tu naturalne miejsce na **zlew + płytę + okap**.
- **Ściana prawa** (krótka, 191 cm): pełna, bez okna, bez drzwi → kandydat na **wysoką zabudowę** (lodówka + piekarnik w słupku).
- **Ściana dolna** (długa, 174 cm między uskokami): od strony przedpokoju, częściowo otwarta. **Tu user proponuje wyspę** — ale to półwyspa najwyżej, nie pełna wyspa.
- **Ściana lewa** (krótka, ~191 cm) z uskokiem 63 × 128 cm w narożniku: prawdopodobnie pion instalacyjny lub zabudowa sąsiedniego pomieszczenia → ograniczenie głębokości szafki w tym narożniku.

### 1.3 Potencjalne kolizje

| Kolizja | Opis | Działanie |
|---|---|---|
| K1 | Lodówka 202 cm vs okno | Lodówka przy prawej krawędzi ściany z oknem może zachodzić na ościeżnicę / parapet | **Lodówka odsunięta na ścianę prawą** (W3) |
| K2 | Wyspa vs szerokość 191 cm | Pełna wyspa wymaga min. 210 cm przy układzie z jednym przejściem | **Rezygnacja z wyspy** na rzecz półwyspy |
| K3 | Uskok 63 × 128 cm w lewym dolnym narożniku | Niemożliwe ustawienie standardowej szafki 60 cm w tym miejscu | Dopasowanie szafki narożnej lub maskownicy |
| K4 | Okap nad indukcją vs kratka wentylacyjna | Kratka jest na ścianie górnej — okap z odprowadzeniem realny | Wymaga doprowadzenia kanału — **[do potwierdzenia]** |
| K5 | Otwór drzwiowy z przedpokoju | Niejasne, gdzie zaczyna/kończy się ściana dolna (174 cm między uskokami) | **[do pomiaru]** czy ściana 174 cm jest pełna, czy zawiera otwór |

---

## 2. Ograniczenia i możliwości — założenia funkcjonalne

### 2.1 Założenia inwestora

- Kuchnia **nowoczesna, praktyczna, pojemna**.
- Sprzęt: lodówka 60×60×202, **płyta indukcyjna** (potwierdzone), zmywarka, piekarnik, okap.
- Intencja wyspy + lodówki w wyznaczonych miejscach.

### 2.2 Krytyczna ocena intencji „WYSPA"

**Werdykt: pełna wyspa nie ma sensu w tym pomieszczeniu.**

Geometryczne minimum wyspy w typowych standardach polskiej kuchni:

| Element | Minimum | Komfortowo |
|---|---|---|
| Zabudowa robocza wzdłuż ściany | 60 cm | 60 cm |
| Przejście między zabudową a wyspą | 90 cm | 100–120 cm |
| Wyspa (głębokość) | 60 cm | 90 cm (z barem) |
| Przejście za wyspą (jeśli druga strona też używana) | 90 cm | 100 cm |
| **Razem (układ dwustronny)** | **300 cm** | **360+ cm** |
| **Razem (układ jednostronny — wyspa przy ścianie)** | **210 cm** | **240 cm** |

Mamy: **191 cm**. Nawet wariant „wyspa przy ścianie z jednym przejściem 90 cm" mieści się tylko siłowo (191 – 60 – 60 = **71 cm przejścia** — poniżej minimum 90 cm, blokuje otwarcie zmywarki, blokuje dwie osoby w kuchni).

**Realne alternatywy bliskie intencji „wyspy":**

| Forma | Co to | Werdykt |
|---|---|---|
| **Pełna wyspa** | Wolnostojąca bryła 60×120, dostęp ze wszystkich stron | ❌ Niemożliwa |
| **Mini-wyspa wzdłużna** | 60×120 ustawiona równolegle do dłuższej ściany, przejście ~70 cm z obu stron | ⚠ Niefunkcjonalne — przejścia za wąskie |
| **Półwyspa prostopadła** | Przedłużenie ściany dolnej w głąb kuchni, 60×80–100 cm, z 1 stroną przy ścianie | ✅ Realne, sensowne |
| **Półwyspa wzdłużna z barem** | Niska zabudowa 30–40 cm głębokości wzdłuż ściany dolnej + blat barowy 30 cm wystający w stronę przedpokoju | ✅ Najlepsze dla małej kuchni |
| **Wyspa-stół** (np. IKEA-typ) | Konstrukcja na nogach, pełni rolę stołu, nie zabudowy | ⚠ Możliwe, ale wąsko |
| **Brak wyspy** | Stół jadalny w sąsiednim pokoju, pełen ciąg L lub U w kuchni | ✅ Maksymalna ergonomia |

### 2.3 Krytyczna ocena intencji „LODÓWKA przy ścianie z oknem"

**Werdykt: zaznaczone miejsce (prawa strona ściany górnej z oknem) jest słabe.**

Powody:
- Słupek 202 cm zasłoni krawędź okna i utrudni jego obsługę.
- Strata blatu pod oknem — najjaśniejsze, najwartościowsze miejsce robocze.
- Lodówka „L" w wnęce 85 cm marnuje 25 cm głębokości na luzy techniczne, które w 4,86 m² są na wagę złota.

**Lepsza lokalizacja: ściana prawa (krótka, 191 cm)** — pełen słupek lodówka + piekarnik bez ingerencji w okno, ze stałą głębokością 60 cm.

### 2.4 Lokalizacje sprzętów — rekomendacje (do W3)

| Sprzęt | Rekomendacja | Uzasadnienie |
|---|---|---|
| **Zlew** | Pod oknem, na ścianie górnej | Klasyka, najjaśniejsze miejsce, naturalne odprowadzenie pary; warunek: pion wod-kan w pobliżu **[do pomiaru]** |
| **Płyta indukcyjna** | Ściana górna, na lewo od zlewu | Min. 40 cm od ścianki bocznej, min. 60 cm strefa blatu od zlewu |
| **Piekarnik** | Słupek na ścianie prawej, pod lodówką lub obok | Zabudowa kompaktowa, ergonomia (na wysokości oczu) |
| **Lodówka** | Słupek na ścianie prawej (zamiast intencji usera) | Zwalnia ścianę z oknem, pełna głębokość 60 cm |
| **Zmywarka** | 45 cm, obok zlewu (po prawej lub lewej) | Wspólny pion, ergonomia załadunku |
| **Okap** | Nad indukcją, do zabudowy lub teleskopowy | Zależy od trasy do kratki went. **[do potwierdzenia]** |
| **Małe AGD** | Półwyspa lub fragment blatu po prawej (strefa śniadaniowa) | Wydzielona strefa, łatwy dostęp |

### 2.5 Inne decyzje funkcjonalne

- **Zabudowa do sufitu**: TAK. Przy h≈250 cm: dolne 85 cm + górne 90 cm + 35 cm nadstawka (rezerwa) = pełna kolumna pojemności.
- **Cokoły**: 10 cm, w kolorze frontów lub czarne.
- **Maskownica górna**: domknięta do sufitu, koniec kurzu i poprawia estetykę.
- **Układ**: **L** + półwyspa (efektywnie U-light) jest dla tej geometrii optymalny.

---

## 3. Trzy warianty układu

### Wariant 1 — „Blisko intencji usera"

**Idea**: zachować WYSPĘ w okolicy ściany dolnej + LODÓWKĘ przy prawej krawędzi ściany górnej, jak na zaznaczeniu.

| Element | Lokalizacja / wymiar |
|---|---|
| Lodówka | Ściana górna, prawy koniec; wnęka 85 cm × 60 cm (jak zaznaczone) |
| Zlew | Ściana górna, środek (pod oknem) |
| Płyta indukcyjna | Ściana górna, lewy fragment |
| Piekarnik | Pod płytą indukcyjną (zabudowa dolna) |
| Zmywarka 45 cm | Obok zlewu, po lewej |
| „Wyspa" | Ściana dolna, w osi pomieszczenia — siłowa wyspa 60 × 100 cm |
| Przejście wyspa ↔ ściana górna | **71 cm** (191 – 60 – 60) |
| Blat roboczy główny | Między zlewem a płytą (lewa część ściany górnej) — ~80 cm |
| Zabudowa wysoka | Tylko słupek lodówki |

**Ergonomia ruchu**: trójkąt zlew-płyta-lodówka mały, ale przejście 71 cm dyskwalifikuje. Otwarta zmywarka zablokuje przejście całkowicie. Dwie osoby się nie miną.

**Przechowywanie**: średnie. Brak słupka z piekarnikiem ogranicza pojemność.

**Plusy**: zachowuje intencję wizualną „wyspy".
**Minusy**: przejście 71 cm — poniżej minimum; lodówka 202 cm zasłania okno; piekarnik w zabudowie dolnej (mniej ergonomiczny niż w słupku).
**Trudność wykonania**: średnia. Wymaga zaślepienia gazu i pewności co do wod-kan pod oknem.

### Wariant 2 — „Korekta wyspy → półwyspa"

**Idea**: utrzymać prostokątną bryłę w okolicy dolnej ściany, ale jako **półwyspę** prostopadłą do dolnej ściany, oraz **lodówkę przeniesioną do słupka na ścianie prawej**.

| Element | Lokalizacja / wymiar |
|---|---|
| Lodówka | Ściana prawa, słupek 60 × 60 × 202 |
| Piekarnik | Słupek na ścianie prawej, nad lub pod lodówką (np. piekarnik na wysokości oczu, pod lodówką szuflada cargo na zapasy) |
| Zlew | Ściana górna, pod oknem (środek) |
| Płyta indukcyjna | Ściana górna, lewa strona |
| Zmywarka 45 cm | Obok zlewu |
| Półwyspa | Prostopadła do ściany dolnej, 60 × 100 cm; jedna strona przy ścianie, druga otwarta z barem 25 cm wystającym ku przedpokojowi |
| Przejście półwyspa ↔ ściana górna | ~131 cm — komfortowo |
| Blat roboczy główny | Cała lewa część ściany górnej, ~100 cm |

**Ergonomia ruchu**: trójkąt komfortowy. Półwyspa nie blokuje ciągu. Zmywarka otwiera się swobodnie.

**Przechowywanie**: dobre. Słupek lodówka + piekarnik + szuflady półwyspy.

**Plusy**: realny kompromis z intencją wyspy, zachowane przejścia, pełna ściana z oknem na strefę roboczą.
**Minusy**: półwyspa zwęża strefę wejścia z przedpokoju o 60 cm — sprawdzić czy nie utrudnia ruchu w korytarzu **[do pomiaru długości przedpokoju]**.
**Trudność wykonania**: średnia. Wymaga przesunięcia lub doprowadzenia instalacji elektrycznej do słupka lodówki.

### Wariant 3 — „Optymalny" (rekomendowany)

**Idea**: L po lewej i górze + **niski blat barowy / mała półwyspa wzdłużna** wzdłuż ściany dolnej (zamiast prostopadłej). Maksymalizacja blatu roboczego, otwarcie kuchni na przedpokój.

| Element | Lokalizacja / wymiar |
|---|---|
| Lodówka | Ściana prawa, słupek 60 × 60 × 202 cm |
| Piekarnik | Ściana prawa, słupek obok / nad lodówką (kompaktowa kolumna AGD) |
| Mikrofala (opcja) | W słupku nad piekarnikiem |
| Zlew (1 komora 50 cm + ociekacz) | Ściana górna, pod oknem |
| Płyta indukcyjna 60 cm | Ściana górna, lewa strona (min. 40 cm od narożnika z uskokiem) |
| Okap | Nad indukcją, do zabudowy w nadstawce górnej |
| Zmywarka 45 cm | Po prawej stronie zlewu (bliżej słupka prawego) |
| Szafka pod zlewem | Specjalna 60 cm z wycięciem pod syfon, segregacja na odpady |
| Półwyspa | Wzdłużna 30–40 cm głęb. × 174 cm dług. przy ścianie dolnej; blat wystający 25 cm jako bar (siedzisko od strony przedpokoju, jeśli geometria pozwala) **[do pomiaru]** |
| Przejście półwyspa ↔ ściana górna | ~151–161 cm — komfortowo, kuchnia dwuosobowa |
| Górna zabudowa | Pełna do sufitu na ścianie górnej (poza oknem) i na ścianie prawej (nad słupkiem) |
| Strefa lewa (uskok) | Półsłupek 40–60 cm głębokości pod uskok 63 cm — schowek na zapasy / drobny sprzęt |

**Ergonomia ruchu**: trójkąt zlew–lodówka–płyta zwarty (boki ~120–150 cm), główny blat roboczy 90–100 cm między zlewem a płytą. Bar po stronie przedpokoju umożliwia szybkie śniadanie / kawę bez zajmowania blatu kuchennego.

**Przechowywanie**: bardzo dobre. Pełna zabudowa do sufitu + półwyspa wzdłużna z szufladami od strony kuchni + słupek AGD z miejscem na zapasy.

**Plusy**: maksymalna ergonomia, najpojemniejszy, zachowuje sens „wyspy" (bar przy przedpokoju), wszystkie przejścia powyżej minimum.
**Minusy**: półwyspa wzdłużna mniej „wyspista" wizualnie niż prostopadła; wymaga sprawdzenia czy ściana dolna jest pełna (174 cm) — jeśli zawiera otwór drzwiowy, część półwyspy musi być cofnięta.
**Trudność wykonania**: średnia–wysoka. Wymaga doprowadzenia instalacji do słupka lodówki (zwykle bez problemu z najbliższego pionu w przedpokoju) i precyzyjnego dopasowania półwyspy do długości 174 cm.

### 3.1 Porównanie wariantów

| Kryterium | W1 (intencja) | W2 (korekta) | W3 (optymalny) |
|---|---|---|---|
| Przejście min. | 71 cm ❌ | 131 cm ✅ | 151–161 cm ✅✅ |
| Trójkąt roboczy | OK, ale ciasny | OK | OK, optymalny |
| Strefa robocza (blat) | ~80 cm | ~100 cm | ~90–100 cm + bar |
| Pojemność (przechowywanie) | Średnia | Dobra | Bardzo dobra |
| Wykorzystanie okna | Słabe (lodówka zasłania) | Dobre (zlew pod oknem) | Dobre (zlew pod oknem) |
| Lodówka 202 cm | Konflikt z oknem | OK (słupek prawy) | OK (słupek prawy) |
| Otwartość na przedpokój | Zamknięta | Średnia | Otwarta (bar) |
| Trudność wykonania | Średnia | Średnia | Średnia–wysoka |
| Wierność intencji wyspy | ✅ (siłowo) | ⚠ Półwyspa prostopadła | ⚠ Bar wzdłużny |

---

## 4. Wybór najlepszego wariantu

**Rekomendacja: Wariant 3 (W3)** — układ L + półwyspa wzdłużna z barem.

### 4.1 Uzasadnienie

1. **Przejścia ergonomiczne** — przejście 151–161 cm pozwala dwóm osobom funkcjonować, otworzyć zmywarkę nie blokując ciągu, sprzątać podłogę bez przesuwania mebli.
2. **Trójkąt roboczy zwarty** — zlew–płyta–lodówka w ramach ścian L, każdy bok ~120–150 cm (norma: 120–270 cm sumy boków, każdy bok ≥120 cm).
3. **Okno wykorzystane** — zlew pod oknem, naturalne światło na główną strefę roboczą, parapet nadal dostępny.
4. **Lodówka 202 cm bez konfliktu** — słupek na ścianie prawej (pełnej, bez okna) eliminuje problem zasłaniania okna i daje pełną głębokość 60 cm.
5. **Pojemność maksymalna** — zabudowa do sufitu na 2 ścianach + półwyspa = w 4,86 m² odzyskanie pojemności porównywalnej z kuchnią 8 m² bez zabudowy do sufitu.
6. **Półwyspa zachowuje sens wyspy** — bar od strony przedpokoju służy do szybkiego śniadania i wizualnie otwiera kuchnię, nie blokując komunikacji.
7. **Realne wykonanie** — wszystkie wymiary mieszczą się w standardach modułów producentów (60 cm dla AGD, 80 cm dla blatów, 30 cm dla baru).

### 4.2 Warunki realizacji (do potwierdzenia przed startem)

- ✅ Wod-kan dostępny w okolicy ściany górnej **[do pomiaru]**.
- ✅ Wentylacja do kratki w ścianie górnej **[do potwierdzenia]**.
- ✅ Ściana dolna 174 cm jest pełna (nie ma otworu drzwiowego w środku) **[do pomiaru]**.
- ✅ Uskok 63 × 128 cm to zabudowa (pion), nie wnęka możliwa do wykorzystania **[do potwierdzenia]**.
- ✅ Wysokość pomieszczenia h ≈ 250 cm **[do pomiaru]**.

---

## 5. Szczegółowy plan techniczny (W3)

### 5.1 Rzut z góry (schemat tekstowy)

```
                                         OKNO
                              ┌──────────────────────────┐
                              │   ZL  ZM  BR             │
   ┌──── 63 cm uskok ─────────┤  zlew zmyw blat robo     │  Ściana PRAWA (191):
   │                          │                          │  SŁUPEK
   │  S1: półsłupek 60 cm     │      PŁYTA INDUKCJA      │  ┌─────────┐
   │  (wykorzystanie uskoku)  │                          │  │  PIEKARN│
   │                          │   ────  Szafka pod ──    │  │   MIKR  │
   │                          │       indukcją           │  │─────────│
   │ S2: szafka narożna       │                          │  │  LODOW  │
   │   górna z półkami        └──────────────────────────┘  │  60x60  │
   │                                                          │  x202  │
   │       Półwyspa wzdłużna 30–40 × 174 cm                  └────────┘
   │       (od strony kuchni: szuflady; od strony             ▲
   │       przedpokoju: bar 25 cm + 2 hokery)                 │
   └─────────────────────────────────────────────────────────┘
                          WEJŚCIE z PRZEDPOKOJU
```

### 5.2 Szerokości przejść (W3)

| Przejście | Wymiar | Status |
|---|---|---|
| Półwyspa → ściana górna (główne) | 151–161 cm | ✅ komfortowo |
| Półwyspa → ściana prawa (przy lodówce) | ~131 cm | ✅ komfortowo |
| Ściana lewa (uskok) → ściana górna | brak — to ten sam ciąg L | — |
| Otwór wejściowy z przedpokoju | **[do pomiaru]** | min. 80 cm wymagane |

### 5.3 Rozpiska szafek dolnych (ściana górna, długość 245 cm wewn.)

| # | Szer. | Gł. | Wys. | Funkcja | Typ |
|---|---|---|---|---|---|
| D1 | 60 cm | 60 cm | 82 cm (+10 cm cokół + 4 cm blat = 96 cm wysokość całkowita) | Szafka pod płytą indukcyjną | Frontowa szuflada płaska + szuflada wewnętrzna na garnki |
| D2 | 90 cm | 60 cm | 82 cm | Blat roboczy główny | 2 szuflady (1 płaska na sztućce + 1 głęboka na garnki) |
| D3 | 60 cm | 60 cm | 82 cm | Pod zlewem | Drzwiczki + segregacja odpadów na wysuwie, wycięcie pod syfon |
| D4 | 45 cm | 60 cm | 82 cm | Zmywarka | Zmywarka 45 cm w zabudowie z frontem |
| D5 | (do uzupełnienia) | 60 cm | 82 cm | Wąska szuflada/cargo na przyprawy | Dopełnienie ściany górnej do 245 cm |

> Suma D1–D5 = 60 + 90 + 60 + 45 + reszta. Dopasować pod fizyczną długość ściany **[po pomiarze]**.

### 5.4 Rozpiska szafek górnych (ściana górna, nad blatem, nad/obok okna)

| # | Szer. | Wys. | Gł. | Otwieranie | Funkcja |
|---|---|---|---|---|---|
| G1 | 60 cm | 90 cm + 35 cm nadstawka | 35 cm | Uchylne do góry z servodrive | Nad płytą — zabudowa okapu w środku, półki po bokach |
| G2 | 90 cm | 90 cm + 35 cm nadstawka | 35 cm | Lewo+prawo otwierane / podnoszone | Naczynia codzienne, szkło |
| G3 | (nad oknem) | tylko nadstawka 35 cm | 35 cm | Uchylne | Zapasy rzadko używane (dostęp ze schodka) — TYLKO jeśli okno + nadproże na to pozwalają **[do pomiaru]** |
| G4 | brak nad zlewem (okno) | — | — | — | — |

### 5.5 Wysoka zabudowa — ściana prawa (191 cm długości)

Pełen słupek lodówka + piekarnik + mikrofala, długość 120 cm (2× moduł 60 cm), pozostałe ~71 cm na ścianie prawej obok słupka na blat roboczy + szafki dolne 60 cm.

| # | Szer. | Gł. | Wys. | Funkcja |
|---|---|---|---|---|
| W1 (słupek lewy) | 60 cm | 60 cm | 230 cm (do nadstawki) | Lodówka 60×60×202 w zabudowie + 28 cm szafka nad nią pod sufit |
| W2 (słupek prawy) | 60 cm | 60 cm | 230 cm | Od dołu: szuflada cargo 60 cm wys. + piekarnik 60 cm + mikrofala 38 cm + szafka 60 cm pod sufit |
| W3 (dolna obok słupków) | reszta ~71 cm | 60 cm | 82 cm | Szafki dolne — szuflady na bieliznę kuchenną / drobne AGD; blat nad nią ciąg dalszy strefy roboczej |
| W4 (górna obok słupków) | reszta ~71 cm | 35 cm | 90 + 35 cm | Szafka górna na naczynia |

### 5.6 Półwyspa (ściana dolna, 174 cm)

| Parametr | Wartość |
|---|---|
| Długość | **174 cm** (pełna ściana dolna między uskokami) |
| Głębokość zabudowy (od kuchni) | **40 cm** (kompromis między pojemnością a komunikacją) |
| Głębokość blatu (z barem) | **65 cm** (40 cm zabudowy + 25 cm bar od strony przedpokoju) |
| Wysokość | 90 cm (zabudowa 82 + 4 cm blat + ewentualnie podwyższenie baru o 0 cm — bar na wysokości blatu, hokery na 65 cm) |
| Przechowywanie od strony kuchni | 3× szuflada (przepasy, garnki, akcesoria) lub 1× drzwiczki + 2 szuflady |
| Siedzenie | 2 hokery na blacie 65 cm wystającym 25 cm |
| Min. odległość od ściany górnej | **151 cm** (191 – 40) ✅ |
| Min. odległość od ściany prawej (słupek) | **120 cm** (174 – 60 – ?) **[do dopracowania]** |

**Warunek krytyczny**: ściana dolna musi być pełna 174 cm (bez otworu drzwiowego w środku) **[do pomiaru]**. Jeśli zawiera otwór, półwyspę trzeba skrócić lub zrezygnować.

### 5.7 Ściana lewa + uskok

Uskok 63 × 128 cm w lewym dolnym narożniku (jeśli pion instalacyjny):
- Obudowa płytą meblową w kolorze frontów, bez szafki.

Jeśli to wnęka:
- Półsłupek 40–60 cm głębokości × 63 cm szerokości × pełna wysokość 230 cm → spiżarnia / schowek na drobny sprzęt (mikser, robot kuchenny). **[do potwierdzenia funkcji uskoku]**.

### 5.8 Blaty

| Odcinek | Długość | Głębokość | Funkcja |
|---|---|---|---|
| Ściana górna | 245 cm | 60 cm | Strefa indukcji (lewa) + główny blat roboczy (środek, ~90 cm między płytą a zlewem) + zlew + zmywarka |
| Ściana prawa | ~71 cm | 60 cm | Blat dodatkowy / strefa małego AGD (kawiarka, czajnik) |
| Półwyspa | 174 cm | 65 cm | Bar śniadaniowy + powierzchnia rozładunku zakupów |

**Główna strefa robocza**: między zlewem a płytą indukcyjną — **min. 90 cm**, optymalnie 100 cm. Tutaj odbywa się krojenie, miksowanie, przygotowanie.

---

## 6. AGD i instalacje

### 6.1 AGD — specyfikacja

| Sprzęt | Typ | Wymiary | Odstępy / uwagi |
|---|---|---|---|
| **Lodówka** | Wolnostojąca w zabudowie (lub do zabudowy) | 60 × 60 × 202 cm | Min. 5 cm odstępu od ścian bocznych dla wolnostojącej; szafka nad: 28 cm do sufitu (po doliczeniu nadstawki) |
| **Płyta indukcyjna** | Do zabudowy, 60 cm, 4 pola | 60 × 52 cm | Min. 40 cm od narożnika ściany, min. 60 cm blatu z każdej strony (zlew po prawej, ściana po lewej); zasilanie 1× 400V 16A lub 230V 16A (zależnie od modelu) |
| **Piekarnik** | Do zabudowy, 60 cm, klasa A+ | 60 × 60 × 60 cm | W słupku na wysokości oczu (top piekarnika ~155 cm od podłogi); własne zabezpieczenie 16A |
| **Mikrofalówka** (opcja) | Do zabudowy, 38 cm | 60 × 38 × 38 cm | W słupku nad piekarnikiem; jeśli nie, można dać tu szafkę |
| **Okap** | Do zabudowy w nadstawce górnej, teleskopowy / wysuwany | 60 cm szer. | Wysokość nad indukcją: 65–75 cm; wydajność min. 600 m³/h; odprowadzenie do kratki went. **[do potwierdzenia trasy]** lub recyrkulacja z filtrem węglowym |
| **Zlewozmywak** | 1 komora 50 cm + ociekacz, podwieszany lub wpuszczany w blat | 78 × 44 cm typowo | Bateria z wyciąganą wylewką; przyłącze wody Z+C, odpływ |
| **Zmywarka** | Do zabudowy, 45 cm, klasa A++ | 45 × 60 × 82 cm | Wspólny pion z zlewem; gniazdko za szafką |
| **Małe AGD** (kawiarka, toster, czajnik) | Strefa śniadaniowa | — | Na blacie ściany prawej, własne gniazdko sekwencyjne (potrójne nad blatem) |

### 6.2 Instalacje elektryczne

| Punkt | Lokalizacja | Typ |
|---|---|---|
| Lodówka | Za słupkiem na ścianie prawej, ~50 cm od podłogi | Gniazdko 230V 10A z bolcem |
| Piekarnik | Za słupkiem, w okolicy piekarnika | Gniazdko 230V 16A (osobny obwód, B16 w rozdzielnicy) |
| Mikrofalówka | Za słupkiem, w okolicy mikrofali | Gniazdko 230V 10A |
| Płyta indukcyjna | Za szafką D1, dół, ~10 cm od podłogi | Wypust 5×2,5 mm² (3-fazowy) lub 3×2,5 mm² zależnie od modelu, **osobny obwód**, B16 |
| Zmywarka | Za szafką sąsiednią (nie za zmywarką!) | Gniazdko 230V 10A |
| Okap | Nad nadstawką górną, ukryte | Gniazdko 230V 10A |
| Nad blatem (ściana górna) | 3× gniazdko 230V w listwie podszafkowej | Sekwencyjne, dla małego AGD |
| Nad blatem (ściana prawa) | 2× gniazdko 230V | Strefa śniadaniowa |
| Włącznik światła głównego | Przy wejściu z przedpokoju | Standard |
| Włącznik LED podszafkowego | Przy wejściu lub czujnik ruchu | Osobny |
| Sterowanie LED dekoracyjnego (jeśli) | Pilot/aplikacja | Opcja |

### 6.3 Instalacje wod-kan

- **Doprowadzenie wody**: Z (ciepła) + Z (zimna) pod zlewem, pod blatem.
- **Odpływ**: pod zlewem, ⌀50 mm z kolanem; zmywarka podłączona do tego samego syfonu.
- **Lokalizacja pionu wod-kan**: **[do pomiaru na miejscu]** — krytyczne dla potwierdzenia zlewu pod oknem. Jeśli pion w innej ścianie, koszt przekładki dochodzi.

### 6.4 Wentylacja

- Kratka wentylacji grawitacyjnej zaznaczona na szkicu — ściana górna, prawa strona **[do potwierdzenia]**.
- Okap: docelowo z odprowadzeniem do kratki (kanał spiro/prostokątny w nadstawce górnej, przykryty maskownicą). Alternatywa: okap recyrkulacyjny z filtrem węglowym (mniej skuteczny przy intensywnym gotowaniu, ale brak konieczności prowadzenia kanału).
- Wentylacja grawitacyjna **musi pozostać drożna** (kratka osobna, niezamurowana) — nakaz prawa budowlanego.

### 6.5 Oświetlenie

| Warstwa | Typ | Lokalizacja |
|---|---|---|
| **Główne (ogólne)** | LED sufitowy, np. plafoniera lub 2× spot wbudowany 3000 K, sumarycznie ~1500 lm | Sufit, oś kuchni |
| **Robocze (zadaniowe)** | Taśma LED podszafkowa 4000 K, IP44, w aluminiowym profilu | Pod każdą szafką górną G1, G2 nad blatem; pod szafkami nad blatem prawym |
| **Dekoracyjne** (opcjonalnie) | Taśma LED w cokole lub w maskownicy nad nadstawką, 3000 K | Wzdłuż całej zabudowy |
| **Bar (półwyspa)** | Lampa wisząca lub 2× spot kierunkowy nad blatem barowym | Sufit, nad osią półwyspy |

---

## 7. Materiały i styl — 3 kierunki

> Pełna specyfikacja materiałów i wizualizacje powstaną w **ETAPIE 2**. Poniżej trzy kierunki do wyboru przez inwestora.

### Kierunek A — Modern Polish Apartment (domyślny stylu repo)

| Element | Materiał |
|---|---|
| Fronty | Egger H3734 ST9 **Pacific Walnut (Orzech Royal)** 18 mm + kremowy mat (np. RAL 9001) frontów słupka — kontrast |
| Blat | **Spiek czarny mat** 12 mm (np. Laminam Calce Nero) lub konglomerat ciemny grafit |
| Ściana nad blatem | Spiek w bryle z blatem (do nadstawki górnej) — ciemny grafit/czarny mat |
| Cokoły | Czarne aluminiowe 100 mm |
| Uchwyty | **Listwowe czarne mat** w górnej krawędzi frontów (gola lub nakładka) |
| Oświetlenie | LED 3000 K (ciepłe białe), spoty czarne mat |
| Charakter | Ciepłe drewno + ciemny kamień + czerń — elegancja, ponadczasowość |

**Zalety praktyczne**: ciemny blat nie pokazuje kawy, herbaty, sosów; orzech maskuje drobne odpryski; spiek odporny na temperaturę i zarysowania (można kroić bezpośrednio, ale nie zaleca się).

### Kierunek B — Japandi Minimal

| Element | Materiał |
|---|---|
| Fronty | Matowy off-white (np. Senosan M1 0202 OW lub fronty MDF lakierowane) + jasny dąb naturalny (akcent słupka) |
| Blat | Konglomerat / spiek w odcieniu kości słoniowej / off-white z drobnym żyłowaniem |
| Ściana nad blatem | Płytka mała formatu (10×10) biała mat lub mikrocement off-white |
| Cokoły | W kolorze frontów lub białe |
| Uchwyty | **Bezuchwyt** — gola aluminiowa biała mat lub push-to-open |
| Oświetlenie | LED 3000 K, lampa wisząca papierowa nad barem |
| Charakter | Skandynawsko-japoński spokój, jasność, ascezia, „kuchnia która znika" |

**Zalety praktyczne**: optycznie powiększa małą kuchnię, idealne dla 4,86 m²; bezuchwytowe fronty łatwiejsze do czyszczenia; jasne kolory + duże okno = jasna codzienność.

### Kierunek C — Industrial Cichy

| Element | Materiał |
|---|---|
| Fronty | Grafit mat (np. RAL 7016) + dąb naturalny (słupek, akcent półwyspy) |
| Blat | Imitacja betonu (spiek lub laminat grub.) — szary mat |
| Ściana nad blatem | Cegła ręcznie formowana (np. Vandersanden, szara) lub mikrocement |
| Cokoły | Czarne aluminiowe |
| Uchwyty | **Metalowe czarne**, prostokątne 128 mm, klasyczne |
| Oświetlenie | LED 4000 K (chłodno-białe), lampa nad barem typu fabrycznego |
| Charakter | Loft cichy, męski, z dyscypliną; drewno łagodzi |

**Zalety praktyczne**: cegła i beton wybaczają zabrudzenia, lakier mat „nie boi się" odcisków, drewniany akcent równoważy chłód.

---

## 8. Błędy do uniknięcia

1. **Wciskanie pełnej wyspy w 191 cm** — przejście 71 cm zablokuje dwie osoby, otwartą zmywarkę i normalny komfort. Zamiast tego: półwyspa (W3).
2. **Lodówka 202 cm zasłaniająca okno** — strata światła, parapetu i wartościowego blatu pod oknem. Zamiast tego: słupek lodówki na ścianie prawej.
3. **Zlew daleko od pionu wod-kan** — przekuwanie ścian i prowadzenie odpływu w spadku kosztuje 2000–5000 zł, a może powodować awarie. **Sprawdzić pion przed projektem mebli**.
4. **Płyta indukcyjna w narożniku ściany** — odstęp < 40 cm od ścianki uniemożliwia używanie tylnych pól, garnki uderzają o ścianę.
5. **Gniazdka tuż nad płytą indukcyjną** — zakaz przepisowy, ryzyko pożaru. Gniazdka na blat min. 50 cm w bok od strefy gotowania.
6. **Okap recyrkulacyjny bez sprawdzenia, czy kratka wentylacyjna jest drożna** — jeśli zatkana, kuchnia będzie się parować i pojawi się grzyb. **Wykonać próbę przepływu powietrza**.
7. **Brak zabudowy do sufitu w małej kuchni** — strata 30–40% potencjalnej pojemności i kurz na maskownicach.
8. **Szafki narożne bez systemu „magic corner"** — martwy róg traci 60 cm głębokości. W tej kuchni narożnik L jest pojedynczy (lewy dolny — uskok eliminuje typowy narożnik), ale prawy dolny (zlew–lodówka) musi być rozwiązany świadomie.
9. **Zmywarka wciśnięta pod blat narożny** — drzwi zmywarki nie otworzą się przy szafce narożnej. Sprawdzić luzy techniczne.
10. **Bar półwyspy ustawiony „w przelocie" z przedpokoju** — jeśli przedpokój jest wąski, hokery zablokują komunikację. **[Do pomiaru długości przedpokoju i pozycji półwyspy względem ciągu przedpokoju]**.
11. **Frontów połysk wysoki w małej kuchni** — każdy odcisk widoczny. Lepiej mat lub super-mat (anti-fingerprint).
12. **Cokół drewniany w kuchni** — woda + drewno = problem. Cokół zawsze laminowany/aluminiowy.
13. **Pominięcie wentylacji okapu** — okap recyrkulacyjny wymaga wymiany filtrów co 6 miesięcy. Z odprowadzeniem do kanału — sprawdzić, czy pion ma rezerwę przepustowości (w blokach często nie ma).
14. **Brak przewidzianego miejsca na kosz na śmieci segregowane** — w kuchni 4,86 m² musi być w szafce pod zlewem na wysuwie, inaczej skończy w przedpokoju.

---

## 9. Lista dodatkowych pomiarów do wykonania na miejscu

> **Wykonać przed zamówieniem mebli i AGD.** Każdy z poniższych pomiarów może zmienić wymiary modułów.

### 9.1 Pomieszczenie

- [ ] **Wysokość pomieszczenia** — w 4 narożnikach (sprawdzenie skosów sufitu); deklarowane h ≈ 250 cm.
- [ ] **Dokładna długość każdej ściany** — taśmą laserową na poziomie 90 cm (wysokość blatu), nie patrząc na rzut.
- [ ] **Grubość ścian** (w otworze drzwiowym łatwo zmierzyć) — wpływa na wymiary zabudowy w narożnikach.
- [ ] **Sprawdzenie pionowości ścian** — poziomicą laserową, ewentualne odchylenia powyżej 1 cm wymagają korekty mebli.
- [ ] **Sprawdzenie poziomu podłogi** — różnica > 5 mm wymaga korekty cokołów.

### 9.2 Okno

- [ ] **Szerokość okna** (od ościeżnicy do ościeżnicy).
- [ ] **Wysokość okna**.
- [ ] **Wysokość parapetu od podłogi** (kluczowe — typowy parapet 85–90 cm, blat 86–90 cm; konflikt jeśli okno niżej).
- [ ] **Odległość okna od lewego i prawego narożnika ściany górnej**.
- [ ] **Głębokość parapetu wewnętrznego** (czy nachodzi na blat, czy się kończy w licu ściany).
- [ ] **Typ okna** — rozwierne, uchylne, rozwierno-uchylne (wpływa na okap nad zlewem — czy wymaga przesunięcia).

### 9.3 Otwory i drzwi

- [ ] **Szerokość, wysokość i lokalizacja otworu wejściowego z przedpokoju** — pełna ściana dolna czy przejście?
- [ ] **Czy istniejące drzwi do kuchni** — jeśli tak, jak się otwierają (do kuchni / od kuchni / przesuwne).
- [ ] **Długość przedpokoju** — krytyczna dla decyzji o barze na półwyspie (czy hokery zablokują komunikację).
- [ ] **Wysokość nadproża nad oknem i nad otworem wejściowym**.

### 9.4 Uskok 63 × 128 cm

- [ ] **Czy jest to pion instalacyjny czy wnęka** — pukanie, sprawdzenie dokumentacji budowy.
- [ ] **Co przebiega w pionie** — wod-kan, wentylacja, gaz? Decyzja o zabudowie / odsłonięciu rewizji.

### 9.5 Instalacje

- [ ] **Lokalizacja pionu wod-kan** — kluczowe dla zlewu pod oknem; jeśli pion daleko, kalkulacja kosztu przekładki.
- [ ] **Średnica i typ odpływu** (PCV 50 mm typowo).
- [ ] **Lokalizacja przyłącza gazu** — przy wyborze indukcji do zaślepienia przez uprawnionego instalatora gazowego (atest, protokół próby szczelności).
- [ ] **Lokalizacja kratki wentylacyjnej** — pozycja na ścianie (szkic sugeruje ścianę górną, prawa strona).
- [ ] **Przepustowość pionu wentylacyjnego** — próba przepływu (kartka papieru przy kratce).
- [ ] **Lokalizacja istniejących gniazdek i włączników** — schemat instalacji elektrycznej (zdjęcie rozdzielnicy i tablicy).
- [ ] **Średnica i typ przewodów** w istniejącej instalacji — czy wytrzyma indukcję 7,4 kW (3,5 mm² lub większy), czy konieczna wymiana.
- [ ] **Pomiar oporności izolacji** istniejącej instalacji — jeśli stara, kalkulacja remontu elektryki.

### 9.6 Inne

- [ ] **Wysokość cokołu / listwy przypodłogowej** w pomieszczeniu sąsiednim — dla ciągłości stylu.
- [ ] **Typ podłogi** w kuchni — jeśli planowana wymiana, kolejność prac (najpierw podłoga, potem meble bez podcinania).
- [ ] **Stan ścian** — równość, ślady wilgoci, konieczność szpachlowania / malowania przed montażem mebli.

---

## Status projektu

| Etap | Status |
|---|---|
| **ETAP 1 — Analiza techniczna i plan układu** | ✅ Zakończony tym dokumentem |
| **ETAP 2 — Wizualizacje i moodboard** | ⏸ Czeka na akceptację ETAP 1 i wybór kierunku stylistycznego (A/B/C) |
| **ETAP 3 — Specyfikacja modułów i kosztorys** | ⏸ Czeka na pomiar uzupełniający na miejscu |

---

**Kolejny krok**: 
1. Wykonać pomiary z sekcji 9 na miejscu.
2. Wybrać wariant układu (rekomendacja: **W3**).
3. Wybrać kierunek stylistyczny (A / B / C).
4. Zgłoszenie do ETAPU 2 — koncepcja wizualna + moodboard.
