# Kuchnia w U z ramieniem L (półwysep) — projekt zabudowy na wymiar (v3.12)

Projekt wykonany skillem **architekt-kuchni** na podstawie: zdjęć pomieszczenia (stan remontowy, obrys blatu wyklejony taśmą), dwóch rzutów odręcznych inwestora z wymiarami i adnotacjami (Z=zlew, zm=zmywarka, L=lodówka, ⊠=indukcja) oraz czterech tur odpowiedzi inwestora. Wykonanie: **samodzielne (inwestor)**, materiały: **Korner (płyty, korner.pl) — oddział Piekary Śląskie / KornerGo**.

> **To NIE jest dokumentacja produkcyjna.** Lista formatek powstanie po pomiarach kontrolnych (pkt 12). Wartości `[P]` = potwierdzone, `[~]` = robocze, `[?]` = do potwierdzenia.

> **Relacja do `projects/kuchnia-9.02`:** ta sama kuchnia po przebudowie ścian — plan 9.02 v4 zarchiwizowany; obowiązuje paleta materiałów zaakceptowana 2026-07-28 (pkt 10).

## Historia wersji (decyzje inwestora)

- **v3.3a (2026-08-12):** korekta nazewnictwa — otwór 127 za ramieniem prowadzi do **SALONU** (zgodnie ze szkicem „salon"); „sypialnia" pojawiła się z wcześniejszej wiadomości inwestora i była błędna — sypialnia jest na końcu mieszkania, poza strefą kuchni.

- v1–v2.2: model pomieszczenia, decyzje bazowe (górne tylko nad indukcją, zlew pod oknem + zmywarka 45, lodówka wolnostojąca 60×65×190 przy ściance 77, indukcja Bosch PXE601DC1E, wycięcie 56×49 `[P]`, sufit 247,8 `[P]`, okno pod sufit 85,6×81,7 `[P]`, przejście 60 `[P]`).
- v2.3–v2.6: iteracje pozycji lodówki/ścianki/wyspy — **zastąpione przez v3.0**.
- **v3.0 (2026-08-12, rzut dzienny inwestora):** „wyspa" = **ramię blatu w L** (przedłużenie ciągu indukcji w stronę lodówki), nie osobna bryła. **127 = szerokość otworu do salonu** w ścianie A za ramieniem (wcześniej błędnie wiązane z wyspą). Kuchnia = **U (A+B+C) + ramię L**, otwarta na korytarz.
- **v3.1 (2026-08-12, adnotacja inwestora na rzucie v3.0):** **195 liczone OD ŚCIANY B** (pilaster 67 wewnątrz tego wymiaru, nie przed nim) i **ramię kończy się NAPRZECIWKO ścianki** — kontrola krzyżowa: koniec ciągu A na 195 od B ≈ ścianka na 188,5+9 od B po stronie C → **obie wyznaczają tę samą linię wschód–zachód = południową granicę kuchni**. Otwór do salonu (127) zaczyna się zaraz za tą linią. Głębokość kuchni od okna ≈ 195, nie 262.
- **v3.3 (2026-08-12, weryfikacja całości po uwadze inwestora o cargo):** **cargo przy pilastrze usunięte — wysuw kolidował z ciągiem A** (strefa 0→600 od ściany A na ciągu okna = martwe pole narożne, bez frontów). Nowy układ B: martwe pole | cargo 15 (600→750) | **zlew 80 pod oknem (750→1550)** | **zmywarka 45 po wschodniej stronie zlewu (1550→2000)**. Dodane ryzyka: blenda dystansowa ~7 między lodówką a ścianką (wysięg 77 > lico zabudowy 70 — drzwi >90°); kierunek ew. drzwi w otworze do salonu vs ramię `[?]`.
- **v3.4–v3.5 (2026-08-12):** blat **910** `[P]` (wzrost 182); okap **recyrkulacyjny z filtrem węglowym** `[P]` (zakup inwestora — kratka nie warunkuje okapu); **ramię gł. 50** `[P]` (strefa przy zlewie ~85; decyzja po analizie komfortu 65 vs 50).
- **v3.6 (2026-08-12, foto pomalowanego pomieszczenia + odpowiedź inwestora):** **gzyms/belka 15,5 pod sufitem, po całym obwodzie `[P]`**. Górne szafki **400 gł.** (propozycja inwestora) z wycięciem 160×(Hg+5) w bokach — front przed gzymsem, jedna płaszczyzna do sufitu; wieniec 240, listwa montażowa pod gzymsem. Wycięcia obejmują też **słupek C2 i nadstawkę C4**. **Korekta GA1: 305 → 245** (pilaster wystaje 155, nie 15 — błąd w v3.2). Otwarte: **Hg** oraz **sprzeczność gzyms vs okno do sufitu (11b)**. Detal: `kuchnia-wyspa-detal-gzyms.pdf`.
- **v3.12 (2026-08-13, pytanie inwestora „a miejsce na widelce?"):** **luka funkcjonalna wykryta i naprawiona** — po przebudowie DA1 na narożną ślepą (v3.10) w całej kuchni nie został ani jeden front szufladowy, a plan funkcjonalny wciąż przypisywał sztućce do nieistniejącej „DA1 45". **Front ramienia (600) podzielony: drzwi 300 (dostęp do martwego pola pod ramieniem) + 3 szuflady 300 z wkładem na sztućce.** Do kontroli dodany **K9 — funkcje obowiązkowe** (sztućce ≥250, kosz segregacji ≥450, przyprawy ≥100), żeby przebudowa modułu nie kasowała po cichu funkcji kuchni. Zaktualizowany plan funkcjonalny (pkt 5a) — usunięte wiersze opisujące moduły, których już nie ma.
- **v3.11 (2026-08-13, uruchomienie automatycznej kontroli geometrii `_kontrola.py`):** dodany skrypt z 8 kontrolami; **regresja potwierdza wykrycie 5/5 błędów z historii projektu**. Kontrola wykryła **nowy błąd: front DC1 ma 345 mm, a nie 450** (pas 0→600 lica zasłonięty korpusem zmywarki) → **cargo narożne obiecane inwestorowi 2026-08-13 NIE mieści się** (magic corner wymaga ≥450); zamiast niego **2 szuflady wewnętrzne ~300**. Poprawiono też ramię 1180 → **1176**, żeby przejście miało pełne 600, a nie 596. Protokół weryfikacji trafił do skilla: `skills/zabudowa-na-wymiar/references/protokol-weryfikacji.md`.
- **v3.10 (2026-08-13, odzysk martwych pól — pytanie inwestora „czy nie da się tego uzupełnić na garnki"):** **DA1 przebudowana na narożną ślepą**: korpus 850×405 sięga aż do ściany B i przejmuje róg, który był martwym polem ciągu okna → **248 l użytecznej przestrzeni tuż przy indukcji**. Sprawdzone: **cargo narożne tam NIE wejdzie** — maksymalny front to 240 mm (szersze drzwi uderzają w korpus ciągu okna, zapas 13 mm), a magic corner/Le Mans wymagają ≥450. **DC1 dostaje cargo narożne (magic corner)** `[P]` — front 450 spełnia minimum. Pod ramieniem bez zmian (dostęp bokiem przez RL1, ~202 l na garnki i blachy). Schemat: `kuchnia-wyspa-schemat-v3.10.pdf`.
- **v3.9 (2026-08-13, decyzja inwestora — wariant A z pkt 9a):** strefa gotowania przesunięta na północ: **DA1 180 (670→850)**, **DA2 indukcja+piekarnik 600 (850→1450)** — front piekarnika kończy się na linii ramienia, otwiera się w pełni. Górne przeliczone: **GA1 670 | GA2 180 | GA3 okap 600 (850→1450) | GA4 500** = 1950. Strefa 1450→1950 pod blatem ramienia = **ślepy narożnik bez frontu**, dostęp bokiem przez RL1. Schemat: `kuchnia-wyspa-schemat-v3.9.pdf`.
- **v3.8 (2026-08-12, weryfikacja rzutu po uwadze inwestora „ta wizualizacja jest jakby zła"):** wykryta **kolizja ramię ↔ ciąg A** — ramię zajmuje pas y 145–195, więc front ciągu A jest dostępny tylko na 85 cm zamiast zakładanych 135; **27 z 60 cm frontu piekarnika (DA2) zasłonięte**. Poprawione też **RL1+RL2 (118) → RL1 narożna ślepa 58 dostępne** (ramię zaczyna się za frontem ciągu A — wcześniej narożnik liczony dwa razy) i **blat ramienia 1180 → 545**. Warianty rozwiązania: pkt 9a. Schemat: `kuchnia-wyspa-schemat-v3.8.pdf`.
- **v3.7a (2026-08-12, kontrola zgodności rzut ↔ rozpiska):** poprawiona **numeracja i szerokości górnych na ścianie A** — okap to **GA3 (600, nad DA2 = 1120→1720)**, a nie GA2; GA2 = zwykła 450 nad DA1; dodana blenda górna 230 przy narożniku ramienia. (W v3.6 zapisałem okap zaraz za GA1, co przesuwałoby go nad szuflady zamiast nad indukcję — schemat v3.5 miał to od początku dobrze.)
- **v3.7 (2026-08-12, korekta po uwadze inwestora „ten gzyms idzie pionowo"):** element 15,5 ze zdjęcia to **PIONOWY PILASTER na całą wysokość**, a nie belka/gzyms pod sufitem — mój błąd w odczycie zdjęcia. **Odwołane z v3.6:** wycięcia 160×(Hg+5) w bokach GA2/GA3/GC1/GC2/C2/C4, wieniec 240, listwa „pod gzymsem", pytanie o Hg oraz sprzeczność „gzyms vs okno do sufitu" (pkt 11b — usunięty; okno idzie do sufitu bez przeszkód). **W mocy zostaje:** górne 400 gł. (uzasadnienie: GA1 na licu pilastra = 245) oraz korekta GA1 305 → 245. Otwarte: **długość uskoku wzdłuż ściany** (pkt 11.11). Detal: `kuchnia-wyspa-detal-pilaster.pdf` (zastępuje odwołany `kuchnia-wyspa-detal-gzyms.pdf`).
- **v3.2 (2026-08-12, uwagi inwestora do schematu v3.1):** (1) **OKNO po stronie indukcji, nie lodówki** — rozkład ściany B od lewej (od pilastra): **59,7 + okno 85,6 + 94,7 do ściany C** (kontrola: suma 240 ≈ 238,9 ✓); zlew przesuwa się pod okno bliżej pilastra, zmywarka między pilastrem a zlewem. (2) **Górne szafki także nad niskim ciągiem na ścianie C** (GC1–GC2 do sufitu) — decyzja inwestora. (3) Narożnik A/B domknięty (przerwa na rzucie v3.1 była strefą pilastra — wypełniona blendą, moduły stykają się). (4) Dodany **plan funkcjonalny** (co w której szafce), w tym szafka na umyte naczynia przy zlewie.

---

## 1. Podsumowanie pomieszczenia

Aneks kuchenny ~254,6 × ~262+ cm (sufit **247,8** `[P]`), otwarty od południa na korytarz. Ściana **A** (zachód) — ciąg z indukcją; przy narożniku z B **pilaster/uskok ~15,5 gł. × 67** `[~]`; za końcem ciągu **otwór do salonu szer. 127** `[P]`. Ściana **B** (północ) — **okno pod sam sufit** (wnęka 85,6 × 81,7, parapet ~166,1 `[P]`), zlew pod oknem. Ściana **C** (wschód) — niski ciąg, słupek, lodówka; **ścianka gr. ~9 `[~]`, wysięg ~77 w głąb** na 188,5 `[P]` od narożnika z B; za ścianką korytarz i wyjście. Podejścia wody/odpływu nisko na B `[~]`. Stan: remont (wylewka; posadzka docelowa zmieni wymiary pionowe).

## 2. Wymiary — statusy

| Wymiar | Wartość | Status | Źródło |
|---|---|---|---|
| Ściana B (okno) | 238,9 | `[P]` | rzut inwestora |
| Szerokość A↔C | 254,6 | `[P]` | rzut (kontrola: 238,9+15,5=254,4 ✓) |
| **Ciąg A: OD ŚCIANY B do końca zabudowy (linia ścianki)** | **195** | `[P]` | rzut + adnotacja inwestora (v3.1); pilaster 67 wewnątrz wymiaru |
| Pilaster przy A/B: dł. × gł. | **67 × 15,5** | `[P]` | rzut + potwierdzenie inwestora na rzucie 2026-08-12; PIONOWY, na całą wysokość; strefa modułowa ciągu A = 195−67 = ~128 |
| **Otwór do salonu (ściana A, za linią ramienia)** | **127** | `[P]` | rzut + opis inwestora; od ~195 do ~322 od B |
| Kontrola linii południowej | 195 (koniec A) ≈ 188,5+9 (ścianka po C) | ✓ | ramię i ścianka naprzeciwko siebie, jedna linia |
| Narożnik B/C → ścianka (wzdłuż C) | 188,5 | `[P]` | rzut |
| Okno: **od pilastra / szerokość / od ściany C** | **59,7 / 85,6 / 94,7** (wys. 81,7, pod sufit) | `[P]` | pomiar inwestora + korekta strony v3.2 (59,7+85,6+94,7 = 240 ≈ 238,9 ✓) |
| Parapet (wyliczony) | ~166,1 | `[~]` | 247,8 − 81,7 |
| Wnęka okienna → ściana C (strona lodówki, „gdzie szafki do sufitu") | 94,7 | `[P]` | pomiar inwestora; = prawy odcinek ściany B |
| Ścianka: wysięg w głąb / grubość | ~77 / ~9 | `[~]` | „77 = wymiar małej ścianki"; do pomiaru łańcuchowego |
| Sufit | 247,8 | `[P]` | pomiar (kontrola po posadzce!) |
| Lodówka (wolnostojąca) | 60 × 65 × 190 | `[P]` | inwestor |
| Indukcja Bosch PXE601DC1E | 57,2 × 51,2 × 5,6; **wycięcie 56 × 49** | `[P]` | inwestor |
| **Przejście ramię ↔ ścianka** | **~60 (reguła nadrzędna)** | `[P]` | decyzja inwestora |
| Ramię L: długość od ściany A / **głębokość** | ~118 `[~]` (177,6 − 60) / **500 `[P]`** | `[P]` gł. | głębokość 50 — decyzja inwestora 2026-08-12 (strefa przy zlewie ~85); długość: docięcie na montażu wg reguły 60 |
| **Wysokość blatu** | **910** | `[P]` | wzrost inwestora 182 (siatka: 180+ → 910); korpus 720 + blat 38 + cokół ~150 |

## 3. Geometria — rzut

Orientacja: **stoisz w korytarzu (południe) i patrzysz na okno (północ)**. A = lewa (indukcja), B = góra (okno), C = prawa (lodówka).

```
            ściana B — OKNO pod sufit (238,9 [P])
            ←59,7→═══ okno 85,6 ═══←──94,7──→
   ▓pilaster│crg│ ZMYW │  ZLEW 80  │DB3│ DC1+GC1-2│
   ▓15,5×67 │15 │  45  │ pod oknem │~39│ narożna  │
   │(blenda)└───┴──────┴───────────┴───┤ niska +  │ ściana C
 1 │┌───────┐                          │ GÓRNE 947│ (188,5 do
 9 ││DA1 45 │      WNĘTRZE U           ├──────────┤  ścianki [P])
 5 ││DA2 60 │   (przy zlewie ~85,      │SŁUPEK ~28│
 [P]│⊠INDUK.│    przy lodówce ~125)    ├──────────┤
   │├───────┴──────────────┐           │ LODÓWKA  │
   ││ RAMIĘ L „wyspa" ~118 │ PRZEJŚCIE │  60×65   │
   ││ (gł. 50 [P], blat L) │  ~60 [P]  │ +nadst.  │
   │└──────────────────────┘    ┌──────┴──────────┤
   ═══ OTWÓR DO SALONU 127 [P]│ścianka ~77      │
   ═══ (zaraz za linią ramienia)└─────────────────┘
   │            ← KORYTARZ (otwarte) →    │wyjście
```

**Linia południowa kuchni** (od zachodu): koniec ciągu A na 195 → ramię L (południowa krawędź w tej linii) → przejście ~60 → czubek ścianki → ścianka → ściana C. **Ramię kończy się naprzeciwko ścianki** `[P]`. Za linią: otwór do salonu (127) i korytarz. Front/rewers ramienia od strony salonu i korytarza: panel ryflowany.

## 4. Ergonomia i przejścia

| Przejście / strefa | Wartość | Próg | Ocena |
|---|---|---|---|
| **Ramię ↔ czubek ścianki (wejście do strefy)** | **~60 `[P]`** | ≥90 | ✗ świadoma decyzja inwestora (jak drzwi „60"; ostrzeżenie niżej) |
| **Front ciągu B ↔ ramię (przy zlewie, dla x<118)** | **~85** (195−60−50) | ≥110 robocze | ~ akceptowalne dla jednej osoby (decyzja: ramię gł. 50 `[P]`); kucanie do szafki pod zlewem swobodne |
| Front B ↔ przestrzeń przy przejściu (x>118) | ~129 | ≥110 | ✓ |
| Front A ↔ front C1/lodówki | ~125–135 | ≥120 | ✓ |
| Otwór do salonu | 127 `[P]` | ≥90 | ✓ (za linią ramienia) |
| Przed lodówką | ~125 | ≥100 | ✓ |

**Trójkąt roboczy:** lodówka (C) → zlew (B, pod oknem) → indukcja (A): boki ~1,3–1,8 m, suma ~4,5 m ✓ (norma 3,6–7,0); ciąg do salonu nie przecina trójkąta (wchodzi się przez przejście 60 obok ramienia).

> ⚠ **Ostrzeżenie (zapisane, decyzja świadoma):** przejście ~60 między ramieniem a ścianką jest poniżej minimum 90 — przechodzi jedna osoba. Reguła 60 jest nadrzędna nad długością ramienia: przy taśmie 127 przejście spada do ~50,6 — **rekomendacja: ramię ≤118**. Ostateczne docięcie blatu na montażu.

## 5. Rozpisanie zabudowy — moduły (mm)

Założenia: korpusy dolne 720 + **cokół ~150 (nóżki 150)**, **blat 910** `[P]` (laminat 38; wzrost 182); głębokość korpusów 560, blat 600 (ramię 650); górne: dół 1480, korpusy ~998 **do sufitu 2478**; fronty bezuchwytowe (frez/gola).

### Ściana A — ciąg z indukcją (1950 `[P]` OD ŚCIANY B; **fronty dolne dostępne tylko 670→1450 = 780**, dalej ślepy narożnik pod ramieniem):

| Nr | Moduł | Szer.×Wys.×Gł. | Front / wnętrze | Uwagi |
|---|---|---|---|---|
| — | blenda przy pilastrze | ~610 | — | zamyka lico ciągu na odcinku 0→610; za nią pracuje korpus DA1 |
| DA1 | **narożna ŚLEPA — odzysk martwego pola (v3.10)** | korpus **850×820×405**, **front 240** (610→850) | drzwi + 1 półka | **korpus sięga aż do ściany B i przejmuje róg, który wcześniej był martwym polem ciągu B** → **248 l na garnki, tuż przy indukcji**. Front max 240: szersze drzwi uderzyłyby w korpus ciągu okna (zapas 13 mm) — dlatego **żadne cargo narożne tu nie wejdzie** (magic corner / Le Mans wymagają otwarcia ≥450). Zawias przy stronie południowej; sięg w ślepą część 600 |
| DA2 | **indukcja + piekarnik** | 600×820×560 | front piekarnika + szuflada | **850→1450 — front kończy się dokładnie na linii ramienia, piekarnik otwiera się w pełni ✓**; wycięcie 560×490 `[P]`; nisza 560×590–600; górna szuflada płytsza (płyta 5,6) |
| — | **ślepy narożnik pod ramieniem** | 1450→1950 × 560 | **bez frontu** | przestrzeń pod blatem ramienia; dostęp bokiem przez RL1 (korpus bez boku zachodniego) |
| GA1 | górna (nad strefą pilastra) | ~670×998×**245** | drzwi, półki | **korekta v3.6:** korpus wisi na LICU PILASTRA (155+245=400 → front równo z GA2/GA3). Poprzednie 305 było błędem (pilaster wystaje 155, nie 15). Dół 1480, do sufitu |
| GA2 | górna wąska | **180**×998×**400** | półki / przyprawy | nad DA1 (670→850) |
| GA3 | **okap w zabudowie** | 600×998×**400** | front uchylny | **nad DA2 = 850→1450, wyśrodkowany nad indukcją** `[P]`; ≥550 nad płytą ✓; recyrkulacja — kratka `[?]` |
| GA4 | górna | **500**×998×**400** | półki | 1450→1950, nad ramieniem (górne są na 1480, więc ramienia nie dotykają) |

### Ramię L („wyspa" — skręt blatu na końcu ciągu A, **~1180×500 `[P gł.]`**, południowa krawędź w linii 1950):

| Nr | Moduł | Szer.×Wys.×Gł. | Front / wnętrze | Uwagi |
|---|---|---|---|---|
| RL1 | **dolna narożna ŚLEPA + szuflady** | ~1176×820×460 (front 600: drzwi 300 + szuflady 300) | drzwi od północy (wnętrze U) | **korekta v3.8:** korpus ramienia zaczyna się dopiero za frontem ciągu A (x=60) → dostępna szerokość 118−60 = **58**; strefa 0–60 × 145–195 to **ślepy narożnik** pod ramieniem (bez boku zachodniego, dostęp bokiem). Poprzednio RL1+RL2 = 118 → liczyło ten narożnik drugi raz |
| — | **KOLIZJA `[?]`** | — | — | **front ciągu A jest dostępny tylko na odcinku y 60→145 = 85 cm**, a moduły planu sumują się do 135 → **27 z 60 cm frontu DA2 (piekarnik) zasłonięte ramieniem**. Do rozstrzygnięcia przez inwestora — warianty w pkt 9a |
| — | blat ramienia | ~1180×500×38 | — | w L z blatem DA (łączenie frezowane/listwa); wieniec na końcu od przejścia |
| — | panel ryflowany | ~1180×910 | — | rewers: od salonu (południe) i od korytarza |

### Ściana B — okno/zlew (okno 597→1453 od pilastra `[P]`; korekta v3.3 po weryfikacji):

| Nr | Moduł | Szer.×Wys.×Gł. | Front / wnętrze | Uwagi |
|---|---|---|---|---|
| — | narożnik zachodni | ~600 od ściany A | **BEZ FRONTU od strony okna** | strefa za ciągiem A — front/wysuw od tej strony kolidowałby z ciągiem indukcji (błąd cargo z v3.2). **Od v3.10 przestrzeń nie jest już martwa: przejmuje ją korpus DA1 (narożna ślepa, dostęp od ciągu A)**; blat ciągły |
| DB0 | cargo przyprawnik 15 | 150×820×560 | cargo | **600→750 od ściany A** — wysuwa się na wolną przestrzeń wnętrza U ✓ |
| DB1 | **zlew 80** | 800×820×560 | drzwi, kosz segregacji, chemia | **750→1550 — pod oknem (752→1608) ✓**; zlew 1-komora z ociekaczem |
| DB2 | **zmywarka 45** | 450 (światło wnęki 450×820+) | front meblowy | **1550→2000** (wschodnia strona zlewu — przed frontem ~125 wolnego ✓); wcina się ~54 w strefę narożnika z C (martwe pole DC1 maleje do ~546 — dopuszczalne) |
| — | narożnik z C | martwe pole ~546×600 | dostęp z DC1 | róg B/C |
| — | **bez górnych na B** | — | — | okno do sufitu; parapet ~166 użytkowy |

### Ściana C — od narożnika z B do ścianki (1885 `[P]`):

| Nr | Moduł | Szer.×Wys.×Gł. | Front / wnętrze | Uwagi |
|---|---|---|---|---|
| DC1 | narożna ślepa (niska, z blatem) | korpus ~945×820×546, **front 345** | **2 szuflady wewnętrzne ~300** | **korekta v3.11 (kontrola K8):** front ma tylko 345 mm — pas 0→600 lica jest zasłonięty korpusem zmywarki. **Cargo narożne (magic corner) NIE wejdzie** (wymaga ≥450). Szuflady wewnętrzne obsługują część dostępną; narożnik północny ~236 l zostaje na sięg ręką |
| — | blenda | ~47 | — | dopełnienie C1 do 947 `[P]` |
| **GC1** | **górna nad DC1** | ~470×998×**400** | półki + **ociekarka na umyte naczynia** | dół 1480, do sufitu; najbliżej zlewu/zmywarki — decyzja inwestora v3.2 |
| **GC2** | **górna nad DC1** | ~477×998×**400** | naczynia codzienne | do sufitu; front w linii słupka C2 |
| C2 | **słupek cargo/spiżarka** | ~280×2378×580 | cargo wysokie | od 947; do sufitu |
| C3 | **zabudowa lodówki** | ~660 światło (lodówka 600+luzy) | — | lodówka wolnostojąca 60×65×190 `[P]` przy ściance; wentylacja 50 tył+góra |
| C4 | nadstawka nad lodówką | ~660×~528×580 | drzwi | od ~1950 do 2478; kratka wentylacyjna |
| — | ŚCIANKA | na 1885 `[P]` | — | bok zabudowy dosunięty; zawiasy lodówki od strony ścianki, drzwi otwierane ku oknu |

## 5a. Plan funkcjonalny — co w której szafce

Zasada: rozładunek zmywarki jednym obrotem (naczynia ≤ 1 krok od zmywarki), strefa gotowania przy indukcji, zapasy przy lodówce, ciężkie nisko.

| Szafka | Przeznaczenie |
|---|---|
| **GC1 (górna nad DC1)** | **umyte naczynia — ociekarka w szafce** + talerze codzienne (1 krok od zmywarki DB1, za narożnikiem) |
| GC2 (górna nad DC1) | szklanki, kubki, miski codzienne |
| DB0 cargo 15 (za linią ciągu A) | przyprawy w butelkach, oleje, ocet — wysuw na wolną przestrzeń ✓ |
| DB1 zlew 80 | kosze segregacji, chemia, akcesoria zlewu |
| DB2 zmywarka 45 | — |
| narożnik zachodni B | **nie jest już stracony** — przejęty przez korpus DA1 (v3.10), dostęp od ciągu A |
| DC1 narożna (front 345) | 2 szuflady wewnętrzne: sztućce zapasowe, sztućce serwisowe (1 krok od zmywarki); część ślepa północna ~236 l: rzadko używane |
| C2 słupek cargo ~28 | spiżarnia pionowa: przetwory, butelki, suche zapasy |
| C3/C4 lodówka + nadstawka | lodówka; nadstawka: zapasy sezonowe, rzadko używany sprzęt |
| DA1 narożna ślepa (front 240) | **garnki i duże naczynia — 248 l tuż przy indukcji** (v3.10); dostęp drzwiami + sięg w głąb |
| DA2 60 | piekarnik + szuflada na blachy/formy (dolna, płytsza — płyta 5,6 nad nią) |
| GA1 (nad pilastrem, docinana) | zapasy lekkie, rzadko używane |
| GA2 18 | herbaty, kawa, cukier — wąska, nad DA1 |
| GA3 okap 60 | okap; nad nim antresola na rzeczy sezonowe |
| **RL1 ramię — front dzielony (v3.12)** | **SZUFLADY 300: górna = sztućce (wkład), środkowa = przybory i noże, dolna = pojemniki**; DRZWI 300 obok: dostęp bokiem do martwego pola pod ramieniem (~202 l — patelnie, blachy, ciężki sprzęt). Blat ramienia (50) = strefa odstawcza/śniadaniowa |

## 6. Rozpisanie pionowe (sufit 2478 `[P]`)

| Poziom | Wysokość | Uwagi |
|---|---|---|
| Cokół | 0–150 | nóżki 150; kratka wentylacji lodówki w cokole |
| Blat | **910 `[P]`** | wzrost 182 → siatka 910 |
| Dół górnych A / okapu | 1480 | odstęp 600 od blatu; okap–indukcja ≥550 ✓ |
| Parapet okna | ~1661 | nad blatem 910 → ~750 wolnej ściany (fartuch) |
| Lodówka | do 1900 | nadstawka od ~1950 |
| Góra zabudowy | 2478 | górne A, słupek C2, nadstawka C4 — wszystko do sufitu |

## 7. AGD — zestawienie

| Urządzenie | Moduł | Nisza / wymagania |
|---|---|---|
| Indukcja Bosch PXE601DC1E `[P]` | DA2 | wycięcie 560×490 `[P]`; obwód siłowy — puszka na A `[?]` potwierdzić 32A |
| Piekarnik | DA2, pod płytą | nisza 560×590–600; osobny obwód 16A; przegroda od płyty wg karty |
| Okap | GA2 | **recyrkulacyjny z filtrem węglowym `[P]` — zakup inwestora**; ≥550 od indukcji ✓; bez kanału — kratka wentylacyjna nie warunkuje okapu |
| Zmywarka 45 | DB2 | światło 450×820+; przyłącza z DB3 |
| Zlew + bateria | DB3 | podejścia nisko na B `[~]` — przedłużyć w zabudowie; nie nad zmywarką ✓ |
| Lodówka 60×65×190 `[P]` | C3 | wolnostojąca; luzy 20–30 bok, 50 tył/góra; zawiasy od ścianki, otwieranie ku oknu |

## 8. Zalecenia instalacyjne (PRZED montażem)

1. Obwód siłowy do DA2 (potwierdzić 32A) + 16A piekarnik + gniazda: zmywarka, lodówka, 2–3 nad blatem B/A (≥600 od zlewu), zasilanie LED (transformator w GA).
2. Zlokalizować **kratkę wentylacyjną** `[?]` — już tylko dla wentylacji ogólnej (okap recyrkulacyjny `[P]`); kratki nie zabudowywać na głucho.
3. Podejścia wody/odpływu: pozycja `[~]` nisko na B — przedłużenie do DB3 w cokole/za korpusami.
4. Ewentualne gniazdo w ramieniu L — doprowadzenie w podłodze **przed posadzką docelową**.
5. Wymiary pionowe finalnie **po posadzce docelowej**.

## 9a. Kolizja ramię ↔ ciąg A — ROZWIĄZANA wariantem A `[P]` (inwestor, 2026-08-13)

Ramię (gł. 50, południowa krawędź w linii 195) zajmuje pas y 145–195. Front ciągu A jest więc dostępny **tylko na 85 cm** (y 60→145; moduły od 67, bo do 67 sięga pilaster → **78 cm na moduły**). Plan zakładał 135 cm. Skutki: **piekarnik w DA2 (112–172) ma 27 cm frontu za ramieniem**, a blenda 172–195 jest w całości w ślepym narożniku.

Warianty:
- **A) Przesunąć strefę gotowania na północ — WYBRANE `[P]`:** DA1 wąskie **180** przy pilastrze (670–850) + **DA2 600 (850–1450)**. Front piekarnika kończy się dokładnie na linii ramienia → otwiera się w pełni ✓. Okap GA3 przesunięty nad 850–1450. Ramię, przejście 60 i reszta układu bez zmian.
- ~~B) Piekarnik do słupka C2~~ (odrzucone) (zabudowa wysoka, na wysokości oczu — wygodniejsze przy schylaniu): pod płytą tylko szuflady, ciąg A dostaje 78 cm szuflad. Koszt: słupek traci cargo/spiżarkę.
- ~~C) Zmniejszyć głębokość ramienia 50 → 30~~ (odrzucone) — ciąg A odzyskuje 20 cm (dostęp 105). Koszt: ramię przestaje być użytecznym blatem, robi się półka; strefa przy zlewie rośnie do ~105.

## 9. Ryzyka

| Ryzyko | Mitygacja |
|---|---|
| Strefa między zlewem a ramieniem ~85 (po decyzji: ramię gł. 50) | akceptowalna dla jednej osoby; zmywarka poza strefą (przed frontem ~125 ✓) |
| Drzwi lodówki >90° zahaczają o kant ścianki (wysięg 77 > lico zabudowy 70) | **blenda dystansowa ~50–70 mm między lodówką a ścianką** (zawiasy od strony ścianki) |
| Jeśli w otworze do salonu (127) będą drzwi — skrzydło otwierane do kuchni kolidowałoby z ramieniem | wg szkicu przejście otwarte `[~]`; przy montażu drzwi: przesuwne albo otwierane do salonu |
| Przejście 60 w praktyce za ciasne | reguła 60 nadrzędna; ramię docinane (118 → można skrócić); decyzja świadoma inwestora |
| Taśma 127 vs reguła 60 (przejście 50,6) | rozstrzygnąć na montażu; rekomendacja ramię ≤118 |
| Pilaster ≠ 15,5×67 na różnych wysokościach | pomiar w 3 punktach; blendy DA1/DB1 docinane |
| Pozycja indukcji vs puszka siłowa | DA2 pozycjonowany do wypustu; kolejność DA1/DA2 może się zamienić |
| Suma łańcucha C (947+280+660 ≈ 1887 vs 1885) | luzy w blendzie przy C1; pomiar łańcuchowy przed zamówieniem |
| Kratka wentylacyjna w strefie zabudowy | pomiar; kratka rewizyjna w zabudowie |
| **Gzyms/podciąg pod sufitem (foto 2026-08-12, pomalowane pomieszczenie)** — koliduje z pasmem górnych 1480–2478 | 3 pomiary (przebieg po ścianach, wystawanie, dolna krawędź od podłogi) → wybór wariantu: A) wycięcie w bokach (wystawanie ≤ ~6 cm), B) szafki kończone POD gzymsem (korpus niższy, gzyms jako „korona"), C) korpusy pogłębione o wystawanie — front przed gzymsem do sufitu; szczegóły w pkt 11a |
| Posadzka zmieni wysokości | wszystkie pionowe po posadzce |

## 10. Materiały i styl (paleta zaakceptowana 2026-07-28, przeniesiona z 9.02)

Kontekst wykończeń (2026-08-12): ściany **NCS S 2002-Y** (jasny ciepły greige), ścianka przy lodówce **RAL 7016** (antracyt), podłoga **jasny dąb**. Fronty dolne + ramię: **beż/kaszmir CIEPŁY mat, bezuchwytowe** (dobór z próbką przy ścianie 2002-Y!); górne A + słupek C2: **ciemny orzech mat** (intencja „Orzech Royal"); **zabudowa lodówki (nadstawka C4 + bok przy ściance): antracyt mat zbliżony do RAL 7016 — jedna ciemna bryła ze ścianką (korekta 2026-08-12)**; blat: **jasny trawertyn, laminat 38**; panel ryflowany ciemny na froncie ramienia od salonu; fartuch przy indukcji: panel ciemny kamień; bateria+zlew czarne; LED 3000K; cokoły czarne. **Kody dekorów z aktualnej oferty Korner (płyty, korner.pl) `[DO WERYFIKACJI]`** — dobór po próbkach w KornerGo / Piekary Śląskie; Egger poza ofertą korner.pl.

## 11. Lista pomiarów kontrolnych — przed zamówieniem formatek (montaż samodzielny)

1. Ściana A łańcuchowo: pilaster (67×15,5 na 3 wysokościach) → 195 → otwór 127 → reszta muru.
2. Ściana B: 238,9 dołem/górą; przekątne narożników A/B i B/C.
3. Ściana C łańcuchowo: 947 → słupek/lodówka → **ścianka: pozycja 1885, grubość, wysięg (77?)**.
4. Okno: 59,7 / 85,6 / 81,7 + głębokość parapetu.
5. Wysokość podłoga–sufit w 4 punktach **po posadzce docelowej**; wysokość lodówki z zawiasami.
6. **Kratka wentylacyjna: pozycja i wymiar.**
7. Podejścia wody/odpływu (wysokość, rozstaw); zaślepka w podłodze przy niszy `[?]`.
8. Puszka siłowa na A: obwód i dokładna pozycja (ustawia DA2).
9. Obrys taśmy ramienia: długość od ściany (127?) i głębokość (65?) — kontrola reguły 60.
10. ~~Wzrost~~ ✓ blat 910 `[P]` (wzrost 182) — pozycja rozstrzygnięta.
11. **PILASTER 15,5 — element PIONOWY `[P]`** (korekta v3.7 po uwadze inwestora; wcześniej błędnie odczytany ze zdjęcia jako belka pod sufitem). Do pomiaru: **ile centymetrów ma uskok WZDŁUŻ ściany** (67 wg szkicu, czy cała długość ściany?) i **przy której ścianie** — inwestor: „pomniejsza jakby całe pomieszczenie" `[?]`. Kontrola: 254,6 − 238,9 = 15,7 ≈ 15,5, ale ta różnica wychodzi tak samo dla słupa 67 i dla uskoku na całej ścianie — sam rzut tego nie rozstrzyga.

### 11a. Górne szafki 400 i pilaster (v3.7)

Głębokość korpusu górnych: **400** `[P decyzja inwestora]`, front 19 → **419 całkowitej**; cofnięcie od lica blatu 181 (przy 320 byłoby 261). Detal rysunkowy: **`kuchnia-wyspa-detal-pilaster.pdf`**.

Powód 400 (nie standardowych 320): **GA1 wisi na licu pilastra**, więc jej głębokość = 400 − 155 = **245**. Przy korpusach 320 wyszłoby 165 — półka bez sensu. Przy 400 wszystkie fronty ciągu A stoją w jednej płaszczyźnie, bez uskoku.

Reszta modułów górnych (GA2, GA3, GC1, GC2) — pełne 400, montaż standardowy (listwa pod sufitem, wieniec 400, półki ruchome). **Żadnych wycięć w bokach** — patrz historia v3.7.

**Projekt musi zostać zweryfikowany pomiarem na miejscu przed produkcją/cięciem mebli.**

## 12. Montaż samodzielny — podział pracy i kolejność

**Zlecić Korner (płyty, korner.pl)** — KornerGo / e-Rozkrój, oddział Piekary Śląskie: cięcie formatek + oklejanie krawędzi + CNC (puszki 35 pod zawiasy, nawierty); przy pełnej kuchni transport Korner (formatki 2,4 m).
**Samodzielnie:** skręcenie korpusów, zawieszenie górnych (listwa montażowa), blaty (łączenie w L frezem/listwą, wycięcia 560×490 i zlew — wyrzynarka + zabezpieczenie krawędzi silikonem, albo CNC z rozkrojem), cokoły, blendy, AGD (siła — elektryk z uprawnieniami).
**Kolejność:** 1) instalacje + posadzka → pomiar finalny → zamówienie; 2) zabudowa C (C1→C2→C3/C4 przy ściance); 3) ciąg B od narożnika; 4) ciąg A od pilastra; 5) ramię L + kotwienie narożnika; 6) górne A; 7) blaty (B→C1→A→ramię, łączenia, silikon); 8) fronty, regulacja, cokoły z kratką, listwy, AGD.
**Po pomiarach z pkt 11 → przeliczam rozpiskę na listę formatek do e-Rozkroju.**

## 13. Prompt — realistyczna wizualizacja (EN; szkic w `_render.py`)

Zaktualizowany opis geometrii do renderów: U-shaped kitchen ~2,55×2,6 m, ceiling 2,48; window wall with high window (86×82, sill 166) and sink run below; induction wall with uppers to ceiling and integrated hood; low corner run continuing to a tall pantry + freestanding fridge enclosure by a short partition wall; an L-shaped worktop return (~118×65) toward the fridge leaving a 60 cm pass; doorway to bedroom (127) behind the return, fluted dark panel on its back. Pełne prompty: `_render.py` (do aktualizacji po zamknięciu pomiarów).

---
*Decyzje inwestora `[P]`: górne tylko nad indukcją i zabudowa nad lodówką; zlew pod oknem + zmywarka 45; lodówka wolnostojąca przy ściance; przejście 60 (reguła nadrzędna); blat w L (ramię w stronę lodówki); otwór do salonu 127 za ramieniem; paleta wg pkt 10; wykonanie samodzielne; materiały Korner (płyty, korner.pl).*
