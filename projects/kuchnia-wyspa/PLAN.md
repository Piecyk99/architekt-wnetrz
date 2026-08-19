# Kuchnia w U z ramieniem L (półwysep) — projekt zabudowy na wymiar (v3.15)

Projekt wykonany skillem **architekt-kuchni** na podstawie: zdjęć pomieszczenia (stan remontowy, obrys blatu wyklejony taśmą), dwóch rzutów odręcznych inwestora z wymiarami i adnotacjami (Z=zlew, zm=zmywarka, L=lodówka, ⊠=indukcja) oraz czterech tur odpowiedzi inwestora. Wykonanie: **samodzielne (inwestor)**, materiały: **Korner (płyty, korner.pl) — oddział Piekary Śląskie / KornerGo**.

> **To NIE jest dokumentacja produkcyjna.** Lista formatek powstanie po pomiarach kontrolnych (pkt 12). Wartości `[P]` = potwierdzone, `[~]` = robocze, `[?]` = do potwierdzenia.

> **Relacja do `projects/kuchnia-9.02`:** ta sama kuchnia po przebudowie ścian — plan 9.02 v4 zarchiwizowany; obowiązuje paleta materiałów zaakceptowana 2026-07-28 (pkt 10).

## Historia wersji (decyzje inwestora)

- **v3.15 (2026-08-13, decyzja inwestora — blat 600):** **szerokość blatu 600** `[P]` zamiast 635. Poprawione w rozpisce (wszystkie trzy blaty proste) i w modelu 3D (`blat_B` 635 → 600). Rachunek wysięgu nad licem frontu: **ciąg A 21 · ciąg B 21 · DC1 35 · ramię 21 mm** — całość w normie 20–40. Poprzednie 635 dawało **56 mm na ciągu A i 70 nad DC1**, co audyt zgłosił w 05 §304 jako blat zbierający kapiącą wodę na fronty. **Decyzja odsłoniła blokera:** audytowy błąd **M18** (ciąg B — 560 czy 600) przestaje być kosmetyczny, bo **przy korpusie 600 blat 600 fizycznie nie działa** (front 19 mm przed blatem). Wpisane do ryzyk z policzonym skutkiem ubocznym: przy 560 drzwi DA1 mogą urosnąć **240 → ~280**.

- **v3.14b (2026-08-13, pytanie inwestora „wszystko mi zrobił w Gliwicach?"):** dodane **`ZAPYTANIE-OFERTOWE.md`** — pełny zakres (płyta 4 dekory + HDF, ~80 formatek, oklejanie, nawierty, 4 blaty, panel ryflowany, transport), **osiem pytań do zadania przez telefon** i porównanie trzech wariantów (wszystko w jednym miejscu / Korner + nawierty usługowo / Korner + wiercę sam). **Nie wiem, czy MEBsystem zrobi całość** — wpis w `dostawcy.md` pochodzi z przeglądu stron www, nikt tam nie dzwonił; deklarowane są cięcie, oklejanie i wiercenie CNC, ale **czy sprzedają płytę, czy obsługują detal i czy mają blaty — nieznane**. Zapisana konsekwencja, o której łatwo zapomnieć: **paleta z pkt 10 jest dobrana pod ofertę Kornera**, więc zmiana dostawcy = ponowny dobór wszystkich czterech dekorów z próbek.

- **v3.14a (2026-08-13, pytanie inwestora o firmę w Gliwicach):** **KOREKTA MOJEGO BŁĘDU — Korner NIE wierci otworów.** Inwestor powiedział mi to na początku projektu, jest to zapisane w `dostawcy.md` w. 86, audyt zgłosił to jako **P0-09** — a ja mimo to napisałem wczoraj w rozpisce „Korner wierci puszki wg strony" i powtórzyłem to w rozmowie. Poprawione w **PLAN pkt 12** i **FORMATKI pkt 2a i 4.1**: rozkrój i oklejanie w KornerGo, **nawierty osobnym zleceniem**. Wpisane obie drogi (usługa CNC ~150–400 zł albo przyrząd do puszek ~200 zł) i tabela firm z CNC w okolicy — **MEBsystem Gliwice, ul. Pszczyńska 206** (to ta z pytania), Soma Chorzów, Komandor Katowice, Daedalus Ruda Śląska. Tabela stron zawiasów z pkt 2a jest potrzebna niezależnie od wybranej drogi — to ona mówi wykonawcy, z której strony wiercić.

- **v3.14 (2026-08-13, decyzja inwestora — LED w cokole dookoła):** dodany **pkt 10a** i detal `kuchnia-wyspa-detal-LED.pdf`. Rozwiązanie: profil alu 16×7 z kloszem **pod dnem korpusu**, cokół **cofnięty 80**. Policzone z modelu: **5471 mm taśmy = 5,47 m**, podzielone na **dwa obwody (3,73 + 1,75 m)**, żeby żaden nie przekroczył 5 m i nie było spadku napięcia; **24 V, zasilacz 100 W**. Trzy warunki: **gniazdo 230 V w ślepym polu pod ramieniem** (dopisane do pkt 8), **taśma IP65** (150 mm nad mytą podłogą) i **cokół na klipsach**. Przy okazji skasowany martwy zapis „kratka wentylacji lodówki w cokole" — lodówka jest wolnostojąca i nie ma przed sobą cokołu; z tego samego powodu linia LED kończy się na słupku C2.

- **v3.13d (2026-08-13, pytanie inwestora „a to cargo jest potrzebne?"):** **KOREKTA WŁASNEGO BŁĘDU.** Dzień wcześniej napisałem, że **C2 nie może mieć drzwi w ogóle**, bo obie jego krawędzie są zajęte. To było za mocne — wniosek pochodził z kontroli K10, która była **płaska i nie znała osi Z**, czyli dokładnie ta ślepota, którą wytknął audyt. Po policzeniu wysokości: skrzydło DC1 kończy się na **871**, więc front C2 **poniżej 871** faktycznie się z nim zderza (zachodzenie 716 mm), ale front **powyżej 875 nie ma z czym kolidować**. Nowy podział C2: **dół 150–871 = wysuw (cargo albo szuflady, obowiązkowo), góra 875–2469 = drzwi na zawiasie 945**. **K10 dostała oś Z** — moduły mają teraz zakres wysokości frontu, a fronty dzielone własne segmenty; kolizja liczy się tylko przy realnym zachodzeniu w pionie. Regresja rozszerzona do **8/8**, w tym nowy przypadek odwrotny: „górny front C2 NIE jest kolizją" — test pilnuje, żeby kontrola nie wróciła do fałszywego alarmu.

- **v3.13c (2026-08-13, pytanie inwestora „jakiego pilastra?"):** **na rzucie pilastra praktycznie nie było widać** — rysowałem go jako prostokąt w kolorze ściany, a potem przykrywał go korpus DA1; jego podpis znikał pod szafką. Skoro inwestor pyta, czym jest element, na którym opiera się cała ściana A, to jest wada rysunku, nie pamięci. Pilaster jest teraz **czerwoną, zaszrafowaną bryłą z odnośnikiem i opisem**. Przy okazji naprawione: **rzut nie mieścił się na stronie** (zakres pionowy to −22…342 przez otwór do salonu, a skala liczyła się z 260 — dolny fragment ściany A uciekał poza kartkę), nachodzące podpisy okna i wymiaru 238,9, oraz **lodówka 60×65×190 → 200 wolnostojąca** na rzucie. **Nazewnictwo:** inwestor nazywa ten element „gzyms" (tak był na jego szkicu), ja od v3.7 „pilaster" — to ta sama rzecz i rysunek powinien mówić oboma słowami.

- **v3.13b (2026-08-13, uwaga inwestora „to nie powinno być na odwrót?"):** **ELEWACJA A była odbita lustrzanie** — miała pilaster i okno po lewej, a powinny być po prawej. Reguła: stojąc we wnętrzu twarzą do ściany zachodniej patrzysz na zachód, więc **północ (okno) jest po Twojej PRAWEJ**, a korytarz i ramię po lewej. Rysunek przeczył własnemu podtytułowi („widok z wnętrza U"). **Sprawdzone rachunkiem wszystkie trzy elewacje: B i C były dobrze, tylko A odbita.** Poprawione; podtytuły elewacji nazywają teraz zwrot wprost („patrzysz na ZACHÓD → okno po PRAWEJ"), żeby rysunek sam się kontrolował. Przy okazji doczyszczona elewacja C, która wciąż pokazywała **lodówkę 190 w niszy 65,8**: teraz **200 wys., 60 szer., dosunięta do słupka, luz 5,8 przy ściance**, nadstawka **41,9**, słupek opisany jako **CARGO (nie drzwi)**, a podpis „zawiasy od strony ścianki" — który był już nieaktualny — zastąpiony wariantem A. Reguła zwrotu elewacji trafiła do skilla (`protokol-weryfikacji.md`, pkt 8).

- **v3.13a (2026-08-13, pytanie inwestora „a ten mały pasek między GA1 a GA3?"):** pasek na elewacji A to **GA2 — szafka 180**, tylko **bez podpisu na rysunku** (mój błąd w rysunku, nie w geometrii). Podpisana. Przy okazji policzone i zapisane: światło wewnętrzne **144**, realny zasięg w głąb ~250 z 400 → zawartość zmieniona z „przypraw" na **butelki ustawiane rzędem** + listwa na przyprawy na drzwiach. Wykryte dwie rzeczy, których wcześniej w dokumencie nie było: **(a)** lewy bok GA2 siada dokładnie na czole pilastra — to najczulszy moduł na pomiar pilastra; **(b) w całym projekcie nie była wybrana ani jedna strona zawiasu**, a nawierty i tak trzeba komuś zlecić. Strony dobrane dla wszystkich skrzydeł i dodana kontrola **K10** (strona wybrana + brak dwóch zawiasów na wspólnej krawędzi). K10 od razu wykazała, że **C2 nie może mieć drzwi** — obie jego krawędzie są zajęte. Regresja: **7/7**.

- **v3.13 (2026-08-13, pomiary inwestora + decyzja o zawiasach):** trzy rzeczy naraz.
  **(1) Sufit zmierzony po ułożeniu posadzki:** 2481 / 2483 / 2485 dalmierzem Bosch GLM 40 → **do zabudowy przyjęte 2481** (najmniejszy), fuga przysufitowa 12 → **góra zabudowy 2469**. *Moja wcześniejsza prognoza była błędna — zapowiadałem, że po podłodze sufit spadnie poniżej 2478; wyszedł wyższy o 3–7 mm.* Przeliczony cały pion (pkt 6): **górne 998 → 989**, **słupek C2 2378 → 2319** (to zamyka usterkę **P0-03** — 2378 + 150 nóżek = 2528 przebijało sufit), **nadstawka C4 519 → 419**. Trzy niezależne łańcuchy ściany C domykają się na 2469.
  **(2) Lodówka:** inwestor ma już własną, **wolnostojącą Beko inox 60 × 65 × 200** `[P]` — nie do zabudowy. Wysokość **200, nie 190** (stąd C4 419). Odpada obudowa lodówki → **P0-04 (bok o przekątnej 2569,6 nie do wniesienia) przestaje istnieć**, z rozkroju znika ~2,2 m² płyty. Nowe otwarte: **czym podeprzeć C4**, skoro nie ma korpusu zabudowy.
  **(3) Zawiasy lodówki — WARIANT A `[P]`:** zawiasy są fabrycznie po stronie ścianki, a ścianka wystaje 770 przy licu lodówki 650 → kant wypada **w osi obrotu**, drzwi nie otwierają się wcale. Inwestor potwierdził, że **drzwi da się przełożyć** → zawiasy idą na stronę słupka C2. Kontrola: kant ścianki **√(120² + 660²) = 670,8 mm** od nowej osi, skrzydło **600** → **zapas 70,8 mm ✓** (warunek: lodówkę dosunąć do słupka, luz boczny 60 po stronie ścianki). Pozycje lodówki i słupka bez zmian, **blenda dystansowa definitywnie odpada** z łańcucha ściany C (P0-07 lżejsze o 70 mm). Warianty B (zamiana lodówki ze słupkiem) i C (odsunięcie o 120 mm) — odrzucone.
  **Wykryty przy okazji błąd w pkt 6:** prześwit nad blatem to **570**, a nie zapisane wcześniej „600" (1480 − 910). Dla okapu 570 ≥ 550 ✓, ale do sprawdzenia w karcie wkładu — część recyrkulacyjnych wymaga 650.

- **v3.3a (2026-08-12):** korekta nazewnictwa — otwór 127 za ramieniem prowadzi do **SALONU** (zgodnie ze szkicem „salon"); „sypialnia" pojawiła się z wcześniejszej wiadomości inwestora i była błędna — sypialnia jest na końcu mieszkania, poza strefą kuchni.

- v1–v2.2: model pomieszczenia, decyzje bazowe (górne tylko nad indukcją, zlew pod oknem + zmywarka 45, lodówka wolnostojąca 60×65×190 przy ściance 77, indukcja Bosch PXE601DC1E, wycięcie 56×49 `[P]`, sufit 247,8 `[P]`, okno pod sufit 85,6×81,7 `[P]`, przejście 60 `[P]`).
- v2.3–v2.6: iteracje pozycji lodówki/ścianki/wyspy — **zastąpione przez v3.0**.
- **v3.0 (2026-08-12, rzut dzienny inwestora):** „wyspa" = **ramię blatu w L** (przedłużenie ciągu indukcji w stronę lodówki), nie osobna bryła. **127 = szerokość otworu do salonu** w ścianie A za ramieniem (wcześniej błędnie wiązane z wyspą). Kuchnia = **U (A+B+C) + ramię L**, otwarta na korytarz.
- **v3.1 (2026-08-12, adnotacja inwestora na rzucie v3.0):** **195 liczone OD ŚCIANY B** (pilaster 67 wewnątrz tego wymiaru, nie przed nim) i **ramię kończy się NAPRZECIWKO ścianki** — kontrola krzyżowa: koniec ciągu A na 195 od B ≈ ścianka na 188,5+9 od B po stronie C → **obie wyznaczają tę samą linię wschód–zachód = południową granicę kuchni**. Otwór do salonu (127) zaczyna się zaraz za tą linią. Głębokość kuchni od okna ≈ 195, nie 262.
- **v3.3 (2026-08-12, weryfikacja całości po uwadze inwestora o cargo):** **cargo przy pilastrze usunięte — wysuw kolidował z ciągiem A** (strefa 0→600 od ściany A na ciągu okna = martwe pole narożne, bez frontów). Nowy układ B: martwe pole | cargo 15 (600→750) | **zlew 80 pod oknem (750→1550)** | **zmywarka 45 po wschodniej stronie zlewu (1550→2000)**. Dodane ryzyka: blenda dystansowa ~7 między lodówką a ścianką (wysięg 77 > lico zabudowy 70 — drzwi >90°); kierunek ew. drzwi w otworze do salonu vs ramię `[?]`.
- **v3.4–v3.5 (2026-08-12):** blat **910** `[P]` (wzrost 182); okap **recyrkulacyjny z filtrem węglowym** `[P]` (zakup inwestora — kratka nie warunkuje okapu); **ramię gł. 50** `[P]` (strefa przy zlewie ~85; decyzja po analizie komfortu 65 vs 50).
- **v3.6 (2026-08-12, foto pomalowanego pomieszczenia + odpowiedź inwestora):** **gzyms/belka 15,5 pod sufitem, po całym obwodzie `[P]`**. Górne szafki **400 gł.** (propozycja inwestora) z wycięciem 160×(Hg+5) w bokach — front przed gzymsem, jedna płaszczyzna do sufitu; wieniec 240, listwa montażowa pod gzymsem. Wycięcia obejmują też **słupek C2 i nadstawkę C4**. **Korekta GA1: 305 → 245** (pilaster wystaje 155, nie 15 — błąd w v3.2). Otwarte: **Hg** oraz **sprzeczność gzyms vs okno do sufitu (11b)**. Detal: `kuchnia-wyspa-detal-gzyms.pdf`.
- **v3.12a (2026-08-13, dobór szuflad):** przyjęty **system z metalowymi bokami** (GTV Modern Box / Rejs / Blum Tandembox) zamiast prowadnic kulkowych — przy montażu samodzielnym odpada budowa skrzynki z płyty (4 formatki i kąt prosty na każdą szufladę), cichy domyk w standardzie. Nominały: **RL1 3×400, DA2 1×500, DC1 2×450** `[do potwierdzenia w karcie producenta — nominał ≤ głębokość korpusu]`; górna szuflada RL1 niska (H≈86) pod wkład na sztućce 300.
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
| **Sufit — POMIAR PO PODŁODZE 2026-08-13** | **2481 / 2483 / 2485 → przyjęte 2481** | `[P]` | dalmierz Bosch GLM 40, 3 punkty, rozrzut 4 mm. **Do zabudowy bierzemy NAJMNIEJSZY.** Poprzednie 247,8 było zaniżone o 3–7 mm |
| **Lodówka (wolnostojąca, Beko inox) — POMIAR 2026-08-13** | **60 szer. × 65 gł. × 200 wys.** | `[P]` | pomiar inwestora; **wysokość 200, nie 190** — nadstawka C4 spada z 519 na **419**; lodówka wystaje **70 mm** przed lico słupka |
| Indukcja Bosch PXE601DC1E | 57,2 × 51,2 × 5,6; **wycięcie 56 × 49** | `[P]` | inwestor |
| **Przejście ramię ↔ ścianka** | **~60 (reguła nadrzędna)** | `[P]` | decyzja inwestora |
| Ramię L: długość od ściany A / **głębokość** | ~118 `[~]` (177,6 − 60) / **500 `[P]`** | `[P]` gł. | głębokość 50 — decyzja inwestora 2026-08-12 (strefa przy zlewie ~85); długość: docięcie na montażu wg reguły 60 |
| **Szerokość blatu** | **600** | `[P]` | decyzja inwestora 2026-08-13. Wysięg nad licem frontu: ciąg A i B **21 mm**, DC1 **35 mm**, ramię **21 mm** — wszystko w normie 20–40. Poprzednie **635 dawało 56 mm na ciągu A i 70 mm nad DC1** — blat zbierałby kapiącą wodę na fronty (audyt 05 §304) |
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

Założenia: korpusy dolne 720 + **cokół ~150 (nóżki 150)**, **blat 910** `[P]` (laminat 38; wzrost 182); głębokość korpusów **560**, **blat 600** `[P decyzja inwestora 2026-08-13]` (ramię: korpus 460 + blat 500); górne: dół 1480, korpusy **989** — **góra zabudowy 2469 = sufit 2481 `[P]` − fuga 12** (fugę zamyka blenda przysufitowa; pkt 6); fronty bezuchwytowe (frez/gola).

### Ściana A — ciąg z indukcją (1950 `[P]` OD ŚCIANY B; **fronty dolne dostępne tylko 670→1450 = 780**, dalej ślepy narożnik pod ramieniem):

| Nr | Moduł | Szer.×Wys.×Gł. | Front / wnętrze | Uwagi |
|---|---|---|---|---|
| — | blenda przy pilastrze | ~610 | — | zamyka lico ciągu na odcinku 0→610; za nią pracuje korpus DA1 |
| DA1 | **narożna ŚLEPA — odzysk martwego pola (v3.10)** | korpus **850×820×405**, **front 240** (610→850) | drzwi + 1 półka | **korpus sięga aż do ściany B i przejmuje róg, który wcześniej był martwym polem ciągu B** → **248 l na garnki, tuż przy indukcji**. Front max 240: szersze drzwi uderzyłyby w korpus ciągu okna (zapas 13 mm) — dlatego **żadne cargo narożne tu nie wejdzie** (magic corner / Le Mans wymagają otwarcia ≥450). Zawias przy stronie południowej; sięg w ślepą część 600 |
| DA2 | **indukcja + piekarnik** | 600×820×560 | front piekarnika + szuflada | **850→1450 — front kończy się dokładnie na linii ramienia, piekarnik otwiera się w pełni ✓**; wycięcie 560×490 `[P]`; nisza 560×590–600; górna szuflada płytsza (płyta 5,6) |
| — | **ślepy narożnik pod ramieniem** | 1450→1950 × 560 | **bez frontu** | przestrzeń pod blatem ramienia; dostęp bokiem przez RL1 (korpus bez boku zachodniego) |
| GA1 | górna (nad strefą pilastra) | ~670×989×**245** | drzwi (para, zawiasy 0 i 670), 2 półki | **korekta v3.6:** korpus wisi na LICU PILASTRA (155+245=400 → front równo z GA2/GA3). Poprzednie 305 było błędem (pilaster wystaje 155, nie 15). Dół 1480, do sufitu |
| GA2 | górna wąska | **180**×989×**400** | 3 półki + listwa na przyprawy na drzwiach | nad DA1 (670→850). **Światło wewnętrzne 144 szer.** Przy 400 gł. sięgasz realnie 250 w głąb → zawartość: **butelki (oliwa, ocet, sosy)** ustawiane rzędem jedna za drugą — rozpoznajesz je po kształcie i wyjmujesz przednią. **Zawias 850 (od strony okapu)** `[P]` — krawędź 670 zajmuje prawe skrzydło GA1, dwa zawiasy na jednej krawędzi = zderzenie (kontrola K10). **Jej lewy bok siada dokładnie na końcu pilastra** — patrz ryzyko poniżej |
| GA3 | **okap w zabudowie** | 600×989×**400** | front uchylny | **nad DA2 = 850→1450, wyśrodkowany nad indukcją** `[P]`; ≥550 nad płytą ✓; recyrkulacja — kratka `[?]` |
| GA4 | górna | **500**×989×**400** | półki | 1450→1950, nad ramieniem (górne są na 1480, więc ramienia nie dotykają) |

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
| **GC1** | **górna nad DC1** | ~470×989×**400** | półki + **ociekarka na umyte naczynia** | dół 1480, do sufitu; najbliżej zlewu/zmywarki — decyzja inwestora v3.2 |
| **GC2** | **górna nad DC1** | ~477×989×**400** | naczynia codzienne | do sufitu; front w linii słupka C2 |
| C2 | **słupek — spiżarnia** | ~280×2319×580 | **front DZIELONY na 871: dół = wysuw (cargo albo szuflady), góra = drzwi z półkami, zawias 945** | od 947; góra 2469. **Dół MUSI być wysuwem**: drzwi na krawędzi 945 zderzyłyby się ze skrzydłem DC1 (oba w paśmie 155–871), a na krawędzi 1225 z drzwiami lodówki. **Góra jest wolna** — DC1 kończy się na 871, więc powyżej 875 drzwi na zawiasie 945 nie mają z czym kolidować (kontrola K10 z osią Z) |
| C3 | **zabudowa lodówki** | ~660 światło (lodówka 600+luzy) | — | lodówka wolnostojąca **60×65×200** `[P]` przy ściance; wentylacja 50 tył+góra; **zawiasy przełożone na stronę słupka C2** `[P]` (wariant A, pkt 9) |
| C4 | nadstawka nad lodówką | ~660×**419**×580 | drzwi | **od 2050 do 2469** (lodówka 2000 + luz 50); kratka wentylacyjna; **podparcie nadstawki `[?]`** — lodówka wolnostojąca nie jest zabudowana, więc C4 musi wisieć na bokach/ścianie, nie stać na lodówce |
| — | ŚCIANKA | na 1885 `[P]` | — | bok zabudowy dosunięty; **zawiasy lodówki NIE przy ściance** — przełożone na stronę słupka C2 (wariant A `[P]`), skrzydło odchyla się od ścianki, zapas 60 mm |

## 5a. Plan funkcjonalny — co w której szafce

Zasada: rozładunek zmywarki jednym obrotem (naczynia ≤ 1 krok od zmywarki), strefa gotowania przy indukcji, zapasy przy lodówce, ciężkie nisko.

**Naczynia stołowe są na ścianie C (GC1 + GC2), nie na ścianie A** — decyzja z v3.2. Dwa powody:
1. **Odległość od zmywarki.** Zmywarka DB2 jest na wschodnim końcu ciągu okna; GC1/GC2 są tuż za narożnikiem = jeden krok. GA1 jest na drugim końcu kuchni, ~2 m dalej.
2. **Głębokość.** GC1/GC2 mają korpus 400 → światło **397 mm**, talerz Ø270 leży swobodnie. GA1 ma korpus **245** (wisi na licu pilastra) → światło **242 mm** — **talerz obiadowy tam po prostu nie wejdzie płasko**.

| Szafka | Przeznaczenie |
|---|---|
| **GC1 (górna nad DC1)** | **umyte naczynia — ociekarka w szafce** + talerze codzienne (1 krok od zmywarki DB1, za narożnikiem) |
| GC2 (górna nad DC1) | szklanki, kubki, miski codzienne |
| DB0 cargo 15 (za linią ciągu A) | **zapas: oleje, ocet, sosy** — cargo wyciąga całą zawartość na raz, więc głębokość nie przeszkadza. Przyprawy w użyciu są w GA2, przy indukcji (DB0 leży za narożnikiem, ~1,5 m od płyty) |
| DB1 zlew 80 | kosze segregacji, chemia, akcesoria zlewu |
| DB2 zmywarka 45 | — |
| narożnik zachodni B | **nie jest już stracony** — przejęty przez korpus DA1 (v3.10), dostęp od ciągu A |
| DC1 narożna (front 345) | 2 szuflady wewnętrzne: sztućce zapasowe, sztućce serwisowe (1 krok od zmywarki); część ślepa północna ~236 l: rzadko używane |
| C2 słupek ~28 (jedyna spiżarnia w tej kuchni) | **DÓŁ (150–871, wysuw):** ciężkie i codzienne — przetwory w słoikach, konserwy, butelki, worki mąki/cukru/ryżu. Wysuw, bo tu sięgasz najczęściej i tu stoi najcięższe. **GÓRA (875–2469, drzwi):** zapas kupowany hurtem i rzeczy rzadkie — makarony, kasze, herbaty, zapasowa chemia. Uwaga: półki mają 244 szer. i 559 gł., więc **realnie użyjesz tylko przedniego ~300 mm** — resztę traktuj jako magazyn na to, co wyjmujesz raz na kwartał |
| C3/C4 lodówka + nadstawka | lodówka; nadstawka: zapasy sezonowe, rzadko używany sprzęt |
| DA1 narożna ślepa (front 240) | **garnki i duże naczynia — 248 l tuż przy indukcji** (v3.10); dostęp drzwiami + sięg w głąb |
| DA2 60 | piekarnik + szuflada na blachy/formy (dolna, płytsza — płyta 5,6 nad nią) |
| GA1 (nad pilastrem, docinana) | **suche zapasy do gotowania: makarony, ryże, kasze, mąka, puszki** — blisko indukcji, a płytkość nie przeszkadza. **NIE naczynia stołowe:** korpus 245 → światło w głąb **242 mm**, a talerz obiadowy ma Ø 260–280 → **nie leży płasko**. Zmieści deserowe Ø200, kubki, miski, szklanki |
| GA2 18 | **przyprawy do gotowania na listwie na wewnętrznej stronie drzwi** (jedyna szafka przy samej indukcji) + wysokie butelki w użyciu, ustawione rzędem. Światło **144 szer.**, realny zasięg ~250 z 400 — drugi rząd w głąb jest bezużyteczny, więc tylko rzeczy rozpoznawalne po sylwetce |
| GA3 okap 60 | okap; nad nim antresola na rzeczy sezonowe |
| **RL1 ramię — front dzielony (v3.12)** | **SZUFLADY 300: górna = sztućce (wkład), środkowa = przybory i noże, dolna = pojemniki**; DRZWI 300 obok: dostęp bokiem do martwego pola pod ramieniem (~202 l — patelnie, blachy, ciężki sprzęt). Blat ramienia (50) = strefa odstawcza/śniadaniowa |

## 6. Rozpisanie pionowe (sufit **2481** `[P]`, pomiar po posadzce 2026-08-13)

**Zasada:** do zabudowy bierzemy **najmniejszy** z trzech pomiarów (2481 / 2483 / 2485), a różnicę zbiera **fuga przysufitowa 12 mm** zamknięta **blendą przysufitową** (listwa 12×19 przykręcana do wieńca po wypoziomowaniu). Bez fugi szafka wyższa niż 2481 nie wejdzie pod strop w najniższym punkcie, a niższa zostawiłaby szczelinę bez czym jej zakryć.

**Góra zabudowy = 2481 − 12 = 2469** — jedna linia dla górnych A/C, słupka C2 i nadstawki C4.

| Poziom | Wysokość | Rachunek / uwagi |
|---|---|---|
| Cokół | 0–150 | nóżki regulowane; **cofnięty 80 od lica frontów** `[P]` — miejsce na profil LED (pkt 10a). ~~kratka wentylacji lodówki~~ **nieaktualne**: lodówka jest wolnostojąca i stoi na podłodze, nie ma cokołu przed sobą |
| Górna krawędź korpusu dolnego | 870 | 150 + 720 |
| **Blat** | **910 `[P]`** | 870 + laminat 38 = **908** → nóżki podkręcić do **152**, żeby wyszło 910 `[ustawienie na montażu]` |
| Dół górnych A / okapu | 1480 | **prześwit nad blatem = 1480 − 910 = 570** (nie 600 — poprzedni zapis był błędny). Okap–indukcja 570 ≥ 550 ✓, ale **sprawdzić w karcie wkładu** — część recyrkulacyjnych wymaga 650 `[?]` |
| **Korpus górnych** | **989** | 2469 − 1480 = 989 (**było 998** — przeliczone po pomiarze sufitu) |
| Parapet okna | ~1664 | 2481 − 817 (okno pod sufit) |
| Lodówka | 0–**2000** `[P]` | wolnostojąca, stoi na podłodze — **nie na cokole** |
| Luz wentylacyjny nad lodówką | 2000–2050 | 50 mm `[P]` wymóg producenta |
| **Nadstawka C4** | **419** | 2469 − 2050 = 419 (**było 519** przy lodówce 1900) |
| **Słupek C2 — korpus** | **2319** | 2469 − 150 nóżek = 2319 (**było 2378**; 2378 + 150 = 2528 > 2481 → przebijało sufit — usterka P0-03) |
| Góra zabudowy | **2469** | górne A/C, słupek C2, nadstawka C4 — jedna linia; nad nią fuga 12 + blenda |

**Kontrola pionu ściany C (od podłogi):** 150 + 2319 = 2469 ✓ · lodówka 2000 + 50 + 419 = 2469 ✓ · górne 1480 + 989 = 2469 ✓ — **trzy niezależne łańcuchy domykają się na tej samej rzędnej.**

## 7. AGD — zestawienie

| Urządzenie | Moduł | Nisza / wymagania |
|---|---|---|
| Indukcja Bosch PXE601DC1E `[P]` | DA2 | wycięcie 560×490 `[P]`; obwód siłowy — puszka na A `[?]` potwierdzić 32A |
| Piekarnik | DA2, pod płytą | nisza 560×590–600; osobny obwód 16A; przegroda od płyty wg karty |
| Okap | GA2 | **recyrkulacyjny z filtrem węglowym `[P]` — zakup inwestora**; ≥550 od indukcji ✓; bez kanału — kratka wentylacyjna nie warunkuje okapu |
| Zmywarka 45 | DB2 | światło 450×820+; przyłącza z DB3 |
| Zlew + bateria | DB3 | podejścia nisko na B `[~]` — przedłużyć w zabudowie; nie nad zmywarką ✓ |
| Lodówka 60×65×200 `[P]` | C3 | wolnostojąca; luzy 20–30 bok, 50 tył/góra; **zawiasy przełożone na stronę słupka C2** `[P]`, otwieranie w głąb kuchni (zapas do ścianki 60 mm) |

## 8. Zalecenia instalacyjne (PRZED montażem)

1. Obwód siłowy do DA2 (potwierdzić 32A) + 16A piekarnik + gniazda: zmywarka, lodówka, 2–3 nad blatem B/A (≥600 od zlewu), zasilanie LED **pod górnymi** (transformator w GA) oraz **GNIAZDO 230 V W ŚLEPYM POLU POD RAMIENIEM** `[P]` — na zasilacz 24 V/100 W do LED w cokole (pkt 10a).
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
| ~~Drzwi lodówki zahaczają o kant ścianki~~ | **ZAMKNIĘTE 2026-08-13 — WARIANT A `[P]`.** Stan wyjściowy: zawiasy fabrycznie **po stronie ścianki**; ścianka wystaje 770, lico lodówki 650 → kant ścianki jest **120 mm PRZED** płaszczyzną drzwi, czyli praktycznie w osi obrotu (odległość zawias→przeszkoda = 0) → drzwi blokują się natychmiast. **Decyzja inwestora („DA SIĘ PRZEŁOŻYĆ"): zawiasy przekładamy na stronę słupka C2 (y = 1225).** Kontrola rachunkiem: oś obrotu w licu lodówki (650 od ściany C) przy słupku (y = 1225); kant ścianki w punkcie (770 od ściany C; y = 1885) → **d = √(120² + 660²) = 670,8 mm** wobec skrzydła **600** → **zapas 70,8 mm ✓**. **Warunek montażowy: lodówkę dosunąć do słupka C2, cały luz boczny (60 mm) zostawić po stronie ścianki** — przesunięcie lodówki o 30 mm ku ściance zjada zapas do 41 mm (nadal działa, ale bez marginesu). Pozycje lodówki i słupka **bez zmian**. Drzwi otwierają się w głąb kuchni, nic nie stoi na drodze. Blenda dystansowa **niepotrzebna** (odpada z łańcucha ściany C → P0-07 lżejsze o 70 mm). ~~B) zamiana lodówki ze słupkiem~~, ~~C) odsunięcie lodówki 120 mm (DC1 spadłaby do frontu 225)~~ — odrzucone. **Robota montażowa: przełożyć zawiasy PRZED wstawieniem lodówki na miejsce** (przy ściance nie ma dostępu z boku) |
| Jeśli w otworze do salonu (127) będą drzwi — skrzydło otwierane do kuchni kolidowałoby z ramieniem | wg szkicu przejście otwarte `[~]`; przy montażu drzwi: przesuwne albo otwierane do salonu |
| Przejście 60 w praktyce za ciasne | reguła 60 nadrzędna; ramię docinane (118 → można skrócić); decyzja świadoma inwestora |
| Taśma 127 vs reguła 60 (przejście 50,6) | rozstrzygnąć na montażu; rekomendacja ramię ≤118 |
| **Głębokość korpusów ciągu B: 560 czy 600?** `[?]` **BLOKUJE** | Audyt **M18 — BŁĄD**: PLAN §5 i rozpiska mówią **560**, a `_kontrola.py`, `_schemat.py` i PLAN §4 („195−60−50") liczą z **600**. Blat 600 rozstrzyga to za nas w jedną stronę: przy korpusie 600 lico wypada na **619**, czyli **front sterczałby 19 mm PRZED blatem** — tak się nie da. **Przy 560 wysięg wychodzi 21 mm ✓.** Skutek uboczny, jeśli potwierdzimy 560: róg korpusu ciągu B cofa się o 40 mm, więc **drzwi DA1 mogą urosnąć z 240 do ~280** (promień swobodny rośnie z 253 na 293 mm). Do potwierdzenia pomiarem/decyzją przed rozkrojem — zmienia front DA1, blendę przy pilastrze i długość odcinka LED na ciągu B |
| Pilaster ≠ 15,5×67 na różnych wysokościach | pomiar w 3 punktach; blendy DA1/DB1 docinane |
| **Z czego jest pilaster? GA1 na nim WISI** `[?]` | GA1 to najcięższa górna szafka (670 szer., suche zapasy) i jej korpus jest przykręcony **do lica pilastra**, nie do ściany nośnej. Jeśli pilaster okaże się **obudową G-K** wokół pionu wentylacyjnego albo rur, nie ma w czym trzymać kołków. **Do sprawdzenia przy pomiarze: zapukać.** Głucho = obudowa → GA1 musi zawisnąć na listwie montażowej zakotwionej w ścianie B i A po bokach, albo oprzeć się na boku GA2. Murowany = bez zmian |
| **Lewy bok GA2 ląduje dokładnie na końcu pilastra (y = 670)** | GA1 jest 245 gł. (wisi na licu pilastra), GA2 jest 400 gł. (wisi na gołej ścianie). Tylne 155 mm boku GA2 dosuwa się do czoła pilastra. Jeśli pilaster ma **mniej niż 670** długości — zostaje szczelina za bokiem (kosmetyczna, niewidoczna). Jeśli **więcej niż 670** — bok GA2 nie wejdzie i trzeba go podciąć. **To najczulszy moduł na pomiar pilastra (pkt 11.11).** Zamawiać bok GA2 dopiero po pomiarze |
| **Zawiasy: sąsiednie skrzydła na jednej krawędzi** | kontrola **K10** wykrywa, że dwa fronty wiszą na tej samej krawędzi **i zachodzą na siebie w pionie** (otwarte leżą w jednej płaszczyźnie i się zderzają). Skutek: **GA2 zawias 850**, nie 670 (670 zajmuje prawe skrzydło GA1). **C2: dół wysuw, góra drzwi na zawiasie 945** — patrz pkt 5. *Korekta z 2026-08-13: pierwsza wersja K10 była płaska i orzekła „C2 nie może mieć drzwi w ogóle". Po dodaniu osi Z okazało się, że dotyczy to tylko dolnego frontu.* |
| Pozycja indukcji vs puszka siłowa | DA2 pozycjonowany do wypustu; kolejność DA1/DA2 może się zamienić |
| Suma łańcucha C (947+280+660 ≈ 1887 vs 1885) | luzy w blendzie przy C1; pomiar łańcuchowy przed zamówieniem |
| Kratka wentylacyjna w strefie zabudowy | pomiar; kratka rewizyjna w zabudowie |
| **Gzyms/podciąg pod sufitem (foto 2026-08-12, pomalowane pomieszczenie)** — koliduje z pasmem górnych 1480–2469 | 3 pomiary (przebieg po ścianach, wystawanie, dolna krawędź od podłogi) → wybór wariantu: A) wycięcie w bokach (wystawanie ≤ ~6 cm), B) szafki kończone POD gzymsem (korpus niższy, gzyms jako „korona"), C) korpusy pogłębione o wystawanie — front przed gzymsem do sufitu; szczegóły w pkt 11a |
| ~~Posadzka zmieni wysokości~~ | **ZAMKNIĘTE 2026-08-13 — podłoga położona i sufit zmierzony: 2481 `[P]`.** *Moja prognoza była błędna: zakładałem, że po posadzce sufit spadnie poniżej 2478, a wyszedł WYŻSZY o 3–7 mm.* Cały pion przeliczony (pkt 6), góra zabudowy **2469** |

## 10a. Oświetlenie LED w cokole — decyzja 2026-08-13 `[P]`

Detal rysunkowy: **`kuchnia-wyspa-detal-LED.pdf`** (przekrój + rozwinięcie obwodów).

**Rozwiązanie:** taśma w **profilu aluminiowym 16×7 z kloszem mlecznym, przykręconym do SPODU dna korpusu przy przedniej krawędzi**, świecąca w dół. Cokół **cofnięty 80 mm** od lica frontów (typowo robi się 50 — 80 daje miejsce na profil i głębszy cień).

**Dlaczego nie na licu cokołu:** taśma pod dnem jest niewidoczna z pozycji stojącej — żeby zobaczyć diody, trzeba mieć oczy poniżej 150 mm nad podłogą. Naklejona na cokole byłaby jasną kreską świecącą w oczy siedzącemu.

**Odcinki (z modelu sprawdzonego kontrolą):**

| odcinek | mm | obwód |
|---|---|---|
| ciąg A — lico indukcji | 1450 | 1 |
| ramię L — front od kuchni | 600 | 1 |
| ramię L — czoło wschodnie | 500 | 1 |
| ramię L — rewers od salonu | 1176 | 1 |
| ciąg B — lico okna | 1400 | 2 |
| ciąg C — lico niskiego ciągu | 345 | 2 |
| **obwód 1** (ciąg A + ramię) | **3726 = 3,73 m** | |
| **obwód 2** (ciąg B + C) | **1745 = 1,75 m** | |
| **RAZEM** | **5471 = 5,47 m** | |

**Rachunek mocy:** 9,6 W/m × 5,47 m = **53 W** → z zapasem 30% = 68 W → **zasilacz 24 V / 100 W**. **24 V, nie 12 V** — przy 12 V koniec obwodu 1 (3,73 m) byłby wyraźnie ciemniejszy. Oba obwody poniżej 5 m, więc zasilanie z jednego końca wystarcza.

**Gdzie kończy się linia:** przy słupku C2. **Lodówka jest wolnostojąca i nie ma cokołu**, więc przed nią taśma się urywa — to narożnik przy ściance, poza polem widzenia z kuchni.

**Trzy warunki, bez których to nie zadziała:**
1. **Gniazdo 230 V w ślepym polu pod ramieniem** — na zasilacz. Dopisane do pkt 8. To jedyne w tej kuchni miejsce suche, wentylowane i dostępne (przez drzwi RL1), a przy tym mniej więcej pośrodku obu obwodów.
2. **Taśma IP65** — leży 150 mm nad podłogą, którą będziesz myć na mokro. Zwykła IP20 tam nie ma czego szukać.
3. **Cokół na klipsach, zdejmowalny** — zasilacz i złączki muszą być dostępne bez demontażu szafek.

**Uczciwie:** światło muskające podłogę pokazuje każdy okruch i każdą nierówność posadzki. To efekt wieczorny, nie oświetlenie robocze — do pracy służy LED pod górnymi szafkami, który jest w projekcie od v3.5.

## 10. Materiały i styl (paleta zaakceptowana 2026-07-28, przeniesiona z 9.02)

Kontekst wykończeń (2026-08-12): ściany **NCS S 2002-Y** (jasny ciepły greige), ścianka przy lodówce **RAL 7016** (antracyt), podłoga **jasny dąb**. Fronty dolne + ramię: **beż/kaszmir CIEPŁY mat, bezuchwytowe** (dobór z próbką przy ścianie 2002-Y!); górne A + słupek C2: **ciemny orzech mat** (intencja „Orzech Royal"); **zabudowa lodówki (nadstawka C4 + bok przy ściance): antracyt mat zbliżony do RAL 7016 — jedna ciemna bryła ze ścianką (korekta 2026-08-12)**; blat: **jasny trawertyn, laminat 38**; panel ryflowany ciemny na froncie ramienia od salonu; fartuch przy indukcji: panel ciemny kamień; bateria+zlew czarne; LED 3000K; cokoły czarne. **Kody dekorów z aktualnej oferty Korner (płyty, korner.pl) `[DO WERYFIKACJI]`** — dobór po próbkach w KornerGo / Piekary Śląskie; Egger poza ofertą korner.pl.

## 11. Lista pomiarów kontrolnych — przed zamówieniem formatek (montaż samodzielny)

1. Ściana A łańcuchowo: pilaster (67×15,5 na 3 wysokościach) → 195 → otwór 127 → reszta muru.
2. Ściana B: 238,9 dołem/górą; przekątne narożników A/B i B/C.
3. Ściana C łańcuchowo: 947 → słupek/lodówka → **ścianka: pozycja 1885, grubość, wysięg (77?)**.
4. Okno: 59,7 / 85,6 / 81,7 + głębokość parapetu.
5. ~~Wysokość podłoga–sufit; wysokość lodówki~~ ✓ **ZROBIONE 2026-08-13:** sufit **2481** `[P]` (3 punkty dalmierzem, min z 2481/2483/2485), lodówka **60×65×200** `[P]`. Opcjonalnie: 4. punkt w narożniku przy lodówce, jeśli montaż wykaże skos.
6. **Kratka wentylacyjna: pozycja i wymiar.**
7. Podejścia wody/odpływu (wysokość, rozstaw); zaślepka w podłodze przy niszy `[?]`.
8. Puszka siłowa na A: obwód i dokładna pozycja (ustawia DA2).
9. Obrys taśmy ramienia: długość od ściany (127?) i głębokość (65?) — kontrola reguły 60.
10. ~~Wzrost~~ ✓ blat 910 `[P]` (wzrost 182) — pozycja rozstrzygnięta.
11. **PILASTER — oprócz wymiarów sprawdź, Z CZEGO JEST:** zapukaj w trzech miejscach. Głuchy dźwięk = obudowa G-K (pion wentylacyjny/rury) → **GA1 nie ma na czym wisieć**, trzeba ją przewiesić na ściany boczne. Pełny = mur, montaż standardowy.
12. **PILASTER 15,5 — element PIONOWY `[P]`** (korekta v3.7 po uwadze inwestora; wcześniej błędnie odczytany ze zdjęcia jako belka pod sufitem). Do pomiaru: **ile centymetrów ma uskok WZDŁUŻ ściany** (67 wg szkicu, czy cała długość ściany?) i **przy której ścianie** — inwestor: „pomniejsza jakby całe pomieszczenie" `[?]`. Kontrola: 254,6 − 238,9 = 15,7 ≈ 15,5, ale ta różnica wychodzi tak samo dla słupa 67 i dla uskoku na całej ścianie — sam rzut tego nie rozstrzyga.

### 11a. Górne szafki 400 i pilaster (v3.7)

Głębokość korpusu górnych: **400** `[P decyzja inwestora]`, front 19 → **419 całkowitej**; cofnięcie od lica blatu 181 (przy 320 byłoby 261). Detal rysunkowy: **`kuchnia-wyspa-detal-pilaster.pdf`**.

Powód 400 (nie standardowych 320): **GA1 wisi na licu pilastra**, więc jej głębokość = 400 − 155 = **245**. Przy korpusach 320 wyszłoby 165 — półka bez sensu. Przy 400 wszystkie fronty ciągu A stoją w jednej płaszczyźnie, bez uskoku.

Reszta modułów górnych (GA2, GA3, GC1, GC2) — pełne 400, montaż standardowy (listwa pod sufitem, wieniec 400, półki ruchome). **Żadnych wycięć w bokach** — patrz historia v3.7.

**Projekt musi zostać zweryfikowany pomiarem na miejscu przed produkcją/cięciem mebli.**

## 12. Montaż samodzielny — podział pracy i kolejność

**Zlecić Korner (płyty, korner.pl)** — KornerGo / e-Rozkrój, oddział Piekary Śląskie: **cięcie formatek + oklejanie krawędzi**; przy pełnej kuchni transport Korner (formatki 2,4 m).

> **⚠ NAWIERTY — OSOBNE ZLECENIE. Korner NIE wierci otworów montażowych** (`dostawcy.md` w. 86; usterka **P0-09** z audytu). Wcześniejszy zapis „+ CNC (puszki 35) w KornerGo" był **błędny** — poprawiony 2026-08-13. Dwie drogi, do rozstrzygnięcia **przed** zamówieniem rozkroju, bo zmieniają zawartość zamówienia i budżet:
>
> | droga | co robisz | koszt orientacyjny `[?]` |
> |---|---|---|
> | **A — usługa CNC** | po rozkroju wieziesz formatki do firmy z wiertarką CNC, oddajesz tabelę stron zawiasów z rozpiski (pkt 2a) | ~150–400 zł |
> | **B — samodzielnie** | przyrząd do puszek 35 z ogranicznikiem + wiertło Forstnera; przy pierwszej kuchni realne, ale każdy błąd jest w widocznym froncie | ~200 zł jednorazowo |
>
> **Firmy z CNC w okolicy** (`skills/architekt-wnetrz/references/dostawcy.md`, wszystkie `[DO POTWIERDZENIA telefonicznie]`):
>
> | firma | adres | od Zabrza | co robi |
> |---|---|---|---|
> | **MEBsystem** | Gliwice, ul. Pszczyńska 206 | ~8 km | cięcie, oklejanie, **wiercenie CNC** · mebsystem.pl |
> | **Daedalus** | Ruda Śląska, ul. Magazynowa 50 | ~10 km | cięcie, oklejanie, frezowanie; **wiercenie `[?]`** · 575 886 996 |
> | **Soma** | Chorzów, ul. Katowicka 160B | ~15 km | cięcie, oklejanie, **wiercenie i frezowanie CNC** · 32 249 76 90; dział CNC 664 011 119 |
> | **Komandor Śląsk** | Katowice, ul. Transportowców 35 | ~25 km | **CNC Homag: otwory pod zawiasy i złącza**, dostawa 24 h |
>
> Wariant trzeci: **całość (płyta + cięcie + oklejanie + wiercenie) w jednej z tych firm** zamiast Kornera — wtedy trzeba porównać cenę samej płyty **oraz przepiąć paletę**, bo dekory z pkt 10 są dobrane pod ofertę korner.pl.
>
> **Gotowe zapytanie do obdzwonienia firm: `ZAPYTANIE-OFERTOWE.md`** — zakres, ilości, osiem pytań i tabela do wypełnienia odpowiedziami.
**Samodzielnie:** skręcenie korpusów, zawieszenie górnych (listwa montażowa), blaty (łączenie w L frezem/listwą, wycięcia 560×490 i zlew — wyrzynarka + zabezpieczenie krawędzi silikonem, albo CNC z rozkrojem), cokoły, blendy, AGD (siła — elektryk z uprawnieniami).
**Kolejność:** 1) instalacje + posadzka → pomiar finalny → zamówienie; 2) zabudowa C (C1→C2→C3/C4 przy ściance); 3) ciąg B od narożnika; 4) ciąg A od pilastra; 5) ramię L + kotwienie narożnika; 6) górne A; 7) blaty (B→C1→A→ramię, łączenia, silikon); 8) fronty, regulacja, cokoły z kratką, listwy, AGD.
**Po pomiarach z pkt 11 → przeliczam rozpiskę na listę formatek do e-Rozkroju.**

## 13. Prompt — realistyczna wizualizacja (EN; szkic w `_render.py`)

Zaktualizowany opis geometrii do renderów: U-shaped kitchen ~2,55×2,6 m, ceiling 2,48; window wall with high window (86×82, sill 166) and sink run below; induction wall with uppers to ceiling and integrated hood; low corner run continuing to a tall pantry + freestanding fridge enclosure by a short partition wall; an L-shaped worktop return (~118×65) toward the fridge leaving a 60 cm pass; doorway to bedroom (127) behind the return, fluted dark panel on its back. Pełne prompty: `_render.py` (do aktualizacji po zamknięciu pomiarów).

---
*Decyzje inwestora `[P]`: górne tylko nad indukcją i zabudowa nad lodówką; zlew pod oknem + zmywarka 45; lodówka wolnostojąca przy ściance; przejście 60 (reguła nadrzędna); blat w L (ramię w stronę lodówki); otwór do salonu 127 za ramieniem; paleta wg pkt 10; wykonanie samodzielne; materiały Korner (płyty, korner.pl).*
