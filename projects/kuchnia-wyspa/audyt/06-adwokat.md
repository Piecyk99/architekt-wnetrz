# 06 — ADWOKAT DIABŁA. Audyt niezależny projektu `kuchnia-wyspa` v3.12a

**Data:** 2026-08-13
**Założenie robocze:** projekt zostaje zamówiony **jutro**, bez poprawek i bez pomiarów kontrolnych z pkt 11.
**Inwestor:** wzrost 182, montuje **sam, pierwszy raz**, kupuje **na firmę**, materiał **Korner — Korner NIE wierci otworów montażowych**.
**Materiał audytu:** `PLAN.md` (v3.12a, całość + historia + ryzyka), `FORMATKI-ROBOCZE.md`, `_kontrola.py`, `_formatki.py`, `_montaz.py`, `_montaz_prosty.py`, `skills/zabudowa-na-wymiar/references/protokol-weryfikacji.md`.
**Uwaga metodyczna:** plik `v1.md` nie istnieje w projekcie. Każdy zarzut poniżej ma cytat, moduł albo wymiar z dokumentu. Tam, gdzie dokument nie zawiera danej — piszę `[BRAK DANYCH]` i traktuję to jako osobny zarzut.

**Uwaga o kosztach:** projekt **nie zawiera żadnej wyceny materiału ani robocizny**. Jedyne kwoty w całym repozytorium to `_montaz.py` („narzędzia ~150–250 zł", „wiertło ~15 zł/szt") i `_montaz_prosty.py` („1–5 zł/otwór — przy tej kuchni ~150–400 zł", „przyrząd do puszek 60–120 zł", „~200 zł"). Dlatego wszystkie kwoty poniżej to `[BRAK DANYCH]`, a zamiast nich podaję **policzalny zakres przeróbki**: konkretne formatki z listy, m² płyty, liczba dodatkowych transportów, dni pracy. **Brak wyceny przy zamówieniu „na firmę" jutro jest samodzielnym zarzutem** (zarzut D1 na końcu).

---

# CZĘŚĆ 1 — 10 scenariuszy porażki

Uporządkowane malejąco wg (prawdopodobieństwo × koszt).

---

## S1. Słupek C2 i bok wykończeniowy lodówki są **fizycznie niemontowalne** — arytmetyka pionu nie domyka się

**Co się stanie.** Dwa najdroższe elementy pionowe kuchni nie dadzą się postawić w pomieszczeniu:

- **Bok wykończeniowy zabudowy lodówki `2478×680`** (FORMATKI-ROBOCZE.md, sekcja 1, ostatnie pozycje; `_formatki.py` `PANELE`). Żeby postawić pionowo płytę o wymiarach h×d w pomieszczeniu o wysokości H, musi zachodzić √(h²+d²) ≤ H. Tutaj: **√(2478² + 680²) = 2569,6 mm > 2478 mm**. Płyta zahacza o sufit przy podnoszeniu z pozycji leżącej — **o 92 mm**. Nie ma sposobu, żeby ją tam ustawić. Nie pomoże ani dwóch ludzi, ani podnoszenie „na skos" — 2569 to już jest przekątna liczona po skosie.
- **Słupek C2:** korpus `2378` (`FORMATKI-ROBOCZE.md` nagłówek: „wysokości korpusów: dolne 720 (nóżki 150), górne 998, **słupek 2378**") + nóżki 150 = **2528 mm**, czyli **50 mm ponad sufit 2478**. A jeśli słupek stoi bez nóżek (na podłodze), to sięga 2378 i do sufitu brakuje **100 mm** — a `PLAN.md` pkt 5 deklaruje „C2 słupek cargo ~280×**2378**×580; od 947; **do sufitu**" i pkt 6 „Góra zabudowy 2478 — górne A, słupek C2, nadstawka C4 — wszystko do sufitu". **Obie interpretacje są sprzeczne z dokumentem.** Dodatkowo skręcony słupek 2378×580 ma przekątną 2447,7 mm — do sufitu 2478 zostaje **30 mm zapasu**, a `_montaz.py` str. 3 każe go składać na podłodze: „C2 słupek: (…) Skręcaj na podłodze, plecy przed postawieniem". Po ułożeniu posadzki docelowej ten zapas spada do kilkunastu milimetrów albo do zera.

**DOWÓD.**
- `FORMATKI-ROBOCZE.md`: `| Bok wykończeniowy zabudowy lodówki (przy ściance, z blendą dystansową) | 2478×680 | 1 | ciemny orzech mat |`
- `FORMATKI-ROBOCZE.md`: `| C2 słupek cargo — bok | 580×2378 | 2 |` oraz nagłówek „słupek 2378"
- `FORMATKI-ROBOCZE.md` sekcja 3: `| Nóżki meblowe 150 + klipsy cokołu | 32 + 16 szt |`
- `PLAN.md` pkt 6: `| Góra zabudowy | 2478 | górne A, słupek C2, nadstawka C4 — wszystko do sufitu |`
- `_kontrola.py` — **cały model jest dwuwymiarowy** (`Modul(nazwa, x0, y0, x1, y1)`), nie zna osi Z, więc nie ma jak tego wykryć. Status **PASS**.

**Prawdopodobieństwo: WYSOKIE.** To nie jest ryzyko losowe — to arytmetyka. Elementy są w liście do wyceny w tej postaci już teraz i nic w łańcuchu (PLAN → formatki → kontrola) tego nie sprawdza.

**KOSZT PO FAKCIE.** Do wyrzucenia: bok wykończeniowy **1,69 m²** orzecha (2478×680) + 2 boki słupka **2,76 m²** korpusu (580×2378×2) + plecy 276×2374 + 2 fronty orzech (276×1300, 276×1070). Razem ok. **1,7 m² frontowego orzecha + 2,8 m² płyty korpusowej** — a orzech to najdroższy dekor w zestawieniu i całkowite zapotrzebowanie na niego wynosi 6,3 m² netto. Do tego **drugi rozkrój + drugi transport** (Korner, formatki 2,4 m) i przestój montażu. Kwota: `[BRAK DANYCH]`.
**KOSZT TERAZ.** Zmiana dwóch liczb: bok lodówki dzielony na dwie części albo skrócony do wysokości pozwalającej na obrót (np. montaż w dwóch segmentach z poziomym łączeniem pod nadstawką C4 — dokument sam ma tam podział na 1950), słupek C2 przeliczony jako `sufit_po_posadzce − 150 (nóżki) − luz montażowy`. Materiał: 0 zł. Czas: godzina. `_formatki.py` jest generatorem — dokument sam mówi: „poprawiamy stałe w `_formatki.py` i lista przeliczy się sama".

---

## S2. Wszystkie wymiary pionowe są zamrożone na suficie zmierzonym **przed posadzką** — i dokument mówi o tym pięć razy, a formatki i tak mają 2478

**Co się stanie.** Sufit `247,8 [P]` zmierzono na wylewce. Po ułożeniu podkładu i podłogi z jasnego dębu wysokość spadnie o grubość układu posadzkowego (`[BRAK DANYCH]` — projekt nigdzie nie podaje grubości podłogi ani podkładu). Wszystkie elementy „do sufitu" będą za wysokie: **górne 998** (GA1–GA4, GC1, GC2 — 12 boków), **słupek C2 2378**, **nadstawka C4 528**, **bok lodówki 2478**, blenda przysufitowa. Efekt: albo szafki nie wchodzą pod sufit, albo trzeba je zawiesić niżej i wtedy nad frontem zostaje szpara, której nie zakryje żadna blenda, bo blendy przysufitowej **nie ma w liście formatek** (patrz S10/D3).

**DOWÓD.** Dokument ostrzega sam przed sobą pięciokrotnie i mimo to zamraża 2478:
- `PLAN.md` pkt 1: „Stan: remont (wylewka; **posadzka docelowa zmieni wymiary pionowe**)."
- `PLAN.md` pkt 2: `| Sufit | 247,8 | [P] | pomiar (**kontrola po posadzce!**) |`
- `PLAN.md` pkt 8.5: „Wymiary pionowe finalnie **po posadzce docelowej**."
- `PLAN.md` pkt 9: `| Posadzka zmieni wysokości | wszystkie pionowe po posadzce |`
- `PLAN.md` pkt 11.5: „Wysokość podłoga–sufit w 4 punktach **po posadzce docelowej**"
- A jednocześnie `FORMATKI-ROBOCZE.md` ma już `GA1 górna — bok | 245×998`, `C2 słupek cargo — bok | 580×2378`, `Bok wykończeniowy … | 2478×680` — wartości gotowe do cięcia.

**Prawdopodobieństwo: WYSOKIE** — przy założeniu „zamawiamy jutro" jest to pewność. Jedyne, co dziś chroni projekt, to zdanie na końcu `FORMATKI-ROBOCZE.md`: „**Pomiar → cięcie → montaż. Nigdy odwrotnie.**" — czyli dyscyplina człowieka, nie konstrukcja dokumentu.

**KOSZT PO FAKCIE.** Do wymiany: **12 boków górnych** (245×998 ×2, 400×998 ×10) + 2 boki słupka + bok lodówki + wszystkie **fronty górne 996** (GA1 2×332, GA2 176, GA4 496, GC1 466, GC2 473 — front orzech). To praktycznie **cała pozycja „ciemny orzech mat" (6,3 m² netto / 7,2 m² z zapasem)** plus część korpusowej. Kwota: `[BRAK DANYCH]`.
**KOSZT TERAZ.** Jeden pomiar w 4 punktach po posadzce (pkt 11.5 — już zapisany, tylko niewykonany) + zmiana stałej wysokości w `_formatki.py`. **0 zł materiału.**

---

## S3. Łańcuch ściany C nie domyka się o **72 mm** — blenda dystansowa lodówki nie ma gdzie stanąć

**Co się stanie.** Zabudowa ściany C nie zmieści się między narożnikiem B/C a ścianką. Konsekwencja praktyczna: albo lodówka wchodzi w linię ścianki i **drzwi nie otworzą się powyżej 90°** (nie wyjmiesz szuflad ani półek — po roku to codzienna udręka), albo trzeba na miejscu ciąć słupek C2 z 280 na ~208 mm, a wtedy **cargo spiżarniane przestaje istnieć** (jest już oznaczone `[DO WERYFIKACJI] — szerokość niestandard.` przy 280).

**DOWÓD — rachunek z dokumentu.**
- `PLAN.md` pkt 5, ściana C: DC1 947 (900 + blenda 47) + C2 słupek 280 + C3 lodówka 660 światła = **1887 mm**, ścianka na **1885 `[P]`**. Dokument sam to zauważa: `PLAN.md` pkt 9 `| Suma łańcucha C (947+280+660 ≈ 1887 vs 1885) | luzy w blendzie przy C1 |` — traktuje to jako 2 mm do wchłonięcia.
- Ale **w tym samym punkcie 9, wiersz wyżej**, jest wymaganie: `| Drzwi lodówki >90° zahaczają o kant ścianki (wysięg 77 > lico zabudowy 70) | blenda dystansowa ~50–70 mm między lodówką a ścianką |`, a `FORMATKI-ROBOCZE.md` sekcja 3 ma pozycję: `| Blenda dystansowa lodówka–ścianka | 1 szt (~70×2478) |`.
- **947 + 280 + 660 + 70 = 1957 vs 1885 → brakuje 72 mm.**
- `_kontrola.py` modeluje ciąg C jako `DC1 (0–945) + C2 (945–1225) + C3 (1225–1885)` = dokładnie 1885 — **blendy dystansowej w modelu nie ma w ogóle**. Kontrola K7 domyka lico i daje **PASS**, bo sprawdza model, a nie listę zakupową.

**Prawdopodobieństwo: WYSOKIE.** Brak 72 mm to nie jest tolerancja — to blisko połowa szerokości cargo. A dochodzi do tego niepomierzony wysięg ścianki (`~77 [~]`, `PLAN.md` pkt 2: „do pomiaru łańcuchowego") — jeśli wysięg jest większy niż 77, deficyt rośnie.

**KOSZT PO FAKCIE.** Przeróbka słupka C2 (2 boki 580×2378, dno/wieniec 244×580 ×2, plecy, 2 fronty) + rezygnacja z cargo spiżarniowego (1 kpl, już zamówionego) albo docinanie zabudowy lodówki na miejscu w kolorze orzech (widoczny element, docinka piłą ręczną = widoczna krawędź bez obrzeża ABS). Kwota: `[BRAK DANYCH]`.
**KOSZT TERAZ.** Pomiar łańcuchowy ściany C (pkt 11.3 — już zapisany) i przeliczenie: `947 + C2 + 660 + 70 = zmierzona odległość`. **0 zł.**

---

## S4. Pilaster ma status `[P]`, którego dokument sam sobie nie przyznaje — jeśli uskok idzie **całą ścianą A**, do wyrzucenia jest pół kuchni

**Co się stanie.** Cała ściana A (najdroższy ciąg: indukcja, piekarnik, okap, 4 szafki górne) jest zaprojektowana wokół założenia, że pilaster ma **67 cm długości i 15,5 cm głębokości**, a za nim ściana się cofa. Jeśli uskok 15,5 biegnie **wzdłuż całej ściany A**, to:
- **DA1** (korpus 405 gł., cofnięty na x=155) i **DA2** (560 gł., przy ścianie) stoją w dwóch różnych płaszczyznach → lico ciągu przestaje być prostą;
- **GA2/GA3/GA4** (400 gł.) muszą zejść do 245 jak GA1 → **okap GA3 o głębokości 245 mm nad płytą indukcyjną 512 mm głęboką jest bezużyteczny**;
- **blat A 1950×635** trzeba przeprojektować.

**DOWÓD — dokument przeczy sam sobie w dwóch miejscach.**
- `PLAN.md` pkt 2: `| Pilaster przy A/B: dł. × gł. | **67 × 15,5** | **[P]** | rzut + potwierdzenie inwestora na rzucie 2026-08-12 |`
- `PLAN.md` pkt 11.11: „Do pomiaru: **ile centymetrów ma uskok WZDŁUŻ ściany** (67 wg szkicu, **czy cała długość ściany?**) i **przy której ścianie** — inwestor: »pomniejsza jakby całe pomieszczenie« `[?]`. Kontrola: 254,6 − 238,9 = 15,7 ≈ 15,5, ale **ta różnica wychodzi tak samo dla słupa 67 i dla uskoku na całej ścianie — sam rzut tego nie rozstrzyga.**"
- Ten sam element ma w jednym dokumencie status `[P]` i `[?]`. A `protokol-weryfikacji.md` pkt 5 stawia regułę wprost: „element ze zdjęcia bez potwierdzonych liczb ma status `[?]`, **nie `[P]`**".
- Historia wersji potwierdza, że ten element już raz wywrócił projekt: **v3.7** — „element 15,5 ze zdjęcia to PIONOWY PILASTER na całą wysokość, a nie belka/gzyms pod sufitem — **mój błąd w odczycie zdjęcia**", odwołujący całą sekcję v3.6.
- Do tego `PLAN.md` pkt 9: `| Pilaster ≠ 15,5×67 na różnych wysokościach | pomiar w 3 punktach |` — czyli głębokość na wysokości blatu vs na wysokości szafek górnych też jest nieznana, a **GA1 wisi na licu pilastra** (pkt 11a: „GA1 wisi na LICU PILASTRA, więc jej głębokość = 400 − 155 = 245").

**Prawdopodobieństwo: ŚREDNIE** dla wariantu „uskok na całej ścianie", **WYSOKIE** dla wariantu „15,5 nie jest stałe na wysokości". Uzasadnienie: ten sam element już raz został błędnie odczytany (v3.7), inwestor opisał go zdaniem jakościowym („pomniejsza jakby całe pomieszczenie"), a rzut go nie rozstrzyga — dokument mówi to wprost.

**KOSZT PO FAKCIE.** Wariant „cała ściana": DA1 (bok 405×720 ×2, dno 814×405, plecy, front, blenda), DA2 (bok 560×720 ×2, dno, plecy, trawers nośny), GA1–GA4 (8 boków, 8 wieńców, 4 plecy, 5 frontów orzech), blenda dolna 610×756, blat A 1950×635. To **większość obu kolorów frontowych plus ok. 1/3 płyty korpusowej** + drugi transport + tygodnie przestoju. Wariant „inna głębokość na wysokości": GA1 (bok 245×998 ×2, wieńce 634×245 ×2, 2 fronty 332×996) — sam korpus GA1 do wymiany. Kwota: `[BRAK DANYCH]`.
**KOSZT TERAZ.** Trzy przyłożenia miary (pkt 11.1 i 11.11 — już zapisane): głębokość pilastra na 30 / 150 / 240 cm od podłogi + długość uskoku wzdłuż ściany. **0 zł, 15 minut.**

---

## S5. Sztućce — naprawione w v3.12, **nie dotarły do listy formatek**. Ten sam błąd, który złapał inwestor, wciąż jest w dokumencie do cięcia

**Co się stanie.** Zamawiasz **3 kpl prowadnic z metalowymi bokami nom. 400** i **1 wkład na sztućce 300** — i nie ma do czego ich włożyć. W liście formatek RL1 występuje jako **zwykła szafka narożna ślepa z jednym frontem 446 i blendą 430** — bez frontów szuflad, bez den szuflad, bez **pionowej przegrody dzielącej korpus 1176 na sekcję drzwi 300 + sekcję szuflad 300**. Prowadnice nie mają do czego się przykręcić.

**DOWÓD — trzy dokumenty, trzy różne RL1.**
- `PLAN.md` v3.12: „**Front ramienia (600) podzielony: drzwi 300 (dostęp do martwego pola pod ramieniem) + 3 szuflady 300 z wkładem na sztućce.**"
- `_kontrola.py`: `Modul("RL1 ramię: drzwi 300 + szuflady 300", 0, 1450, 1176, 1950, lico="N", front=(576, 1176), funkcje=("sztućce", "przybory"))` — **jeden ciągły front 576→1176 = 600 mm**, bez podziału.
- `_formatki.py`: `("RL1 ramię narożna ślepa + szuflady", 1176, 720, 460, "**narozna**", …)` — typ `narozna` generuje w kodzie tylko: `front 446×716` + `blenda ślepa 430×716`. Gałąź `szuflady3` (fronty 236 ×3) **nie jest wywoływana dla żadnego modułu w projekcie**.
- `FORMATKI-ROBOCZE.md` w efekcie zawiera: `| RL1 ramię narożna ślepa + szuflady — front | 446×716 | 1 |` i `| RL1 … — blenda ślepa | 430×716 | 1 |`. **Zero frontów szuflad. Zero den. Zero przegrody.**
- A `FORMATKI-ROBOCZE.md` sekcja 3 jednocześnie zamawia: `| System szuflad z metalowymi bokami, nom. 400 | 3 kpl | RL1 ramię — korpus 300 szer., 460 gł. |` oraz `| Wkład na sztućce 300 | 1 szt |`.

**Dlaczego automat tego nie łapie.** K9 sprawdza funkcję „sztućce ≥ 250 mm" po szerokości **całego frontu modułu** (`naj = max(m.front[1] - m.front[0])` = 600), a nie po szerokości sekcji szufladowej (300). Gdyby szuflady miały 150 mm, K9 nadal dałoby **PASS**. Kontrola nie widzi frontów dzielonych.

**Prawdopodobieństwo: PEWNE** (nie „wysokie" — to stan faktyczny listy w repozytorium na dziś).

**KOSZT PO FAKCIE.** Dodatkowe formatki: 3 fronty szuflad + 3 dna + 1 przegroda pionowa 460×720 + docięcie frontu drzwi z 446 na 300 (front 446 na otwór 300 nie zamknie się — do kosza). **Drugi rozkrój + drugi transport dla ~0,5 m²** — czyli koszt logistyki wielokrotnie przewyższa koszt materiału. Kwota: `[BRAK DANYCH]`.
**KOSZT TERAZ.** Dopisanie typu modułu w `_formatki.py` i przegenerowanie listy. **0 zł, 20 minut.**

**Zarzut nadrzędny:** to jest **dokładnie ten sam błąd**, który inwestor złapał pytaniem „a miejsce na widelce?" (v3.12), i który spowodował dodanie kontroli K9. Poprawka trafiła do PLAN.md i do `_kontrola.py`, **ale nie do dokumentu, z którego się zamawia**. Kontrola K9 raportuje PASS na modelu, który nie odpowiada liście do cięcia — i to jest gorsze niż brak kontroli.

---

## S6. DC1 — jeden moduł, **cztery różne wymiary** w czterech plikach. Zamówiony front nie pasuje do otworu

**Co się stanie.** Zamówisz front `446×716` do otworu, który ma **345 mm**. Front będzie o **101 mm za szeroki** — nie zamknie się, nie da się go powiesić, jest do wyrzucenia. Do tego zamówione **zawiasy 155°** (2 szt) i **szuflady wewnętrzne 450 nom.** będą dobrane do niewłaściwej geometrii.

**DOWÓD — rozjazd w czterech miejscach naraz:**

| źródło | szerokość korpusu | głębokość | front |
|---|---|---|---|
| `PLAN.md` pkt 5 (po korekcie v3.11) | ~945 | 546 | **345** |
| `_kontrola.py` (`Modul("DC1 …", 2000,0,2546,945)`) | 945 (wzdłuż y) | 546 (wzdłuż x) | **345** (`front=(600,945)`) |
| `_formatki.py` (`MODULES`) | **900** | **560** | komentarz: „**front 450**" |
| `FORMATKI-ROBOCZE.md` | bok 560×720, dno 864×560 | **560** | **front 446×716** |

- `PLAN.md` v3.11 mówi wprost: „**Kontrola wykryła nowy błąd: front DC1 ma 345 mm, a nie 450** (pas 0→600 lica zasłonięty korpusem zmywarki) → **cargo narożne obiecane inwestorowi 2026-08-13 NIE mieści się**".
- `FORMATKI-ROBOCZE.md` sekcja 3 nawet **cytuje tę poprawkę**: „cargo narożne NIE mieści się: front DC1 ma **345 mm**… — kontrola K8" — i dwie sekcje wyżej, w tej samej tabeli formatek, ma `front 446×716`.
- Dodatkowo głębokość: bok 560 przy modelowanych 546 → korpus wystaje **14 mm poza lico**, na które równany jest blat C1 947×635.

**Prawdopodobieństwo: PEWNE.** Wymiary są w plikach dziś, w tej postaci.

**KOSZT PO FAKCIE.** Front 446×716 + blenda 430×716 (beż/kaszmir) do kosza, dopłata za drugi rozkrój i transport, ewentualna wymiana zawiasów. Kwota: `[BRAK DANYCH]`.
**KOSZT TERAZ.** Zmiana jednej krotki w `MODULES` w `_formatki.py`. **0 zł, 5 minut.**

**Uwaga:** ten sam mechanizm dotyczy **wysokości korpusów dolnych**. `PLAN.md` pkt 5 tabele podają moduły jako `850×**820**×405`, `600×**820**×560`, `~1176×**820**×460`, `~945×**820**×546` — a nagłówek tego samego punktu i wszystkie formatki mówią **720** („korpusy dolne 720 + cokół ~150"). 820 + 150 + 38 = 1008 mm blatu, nie 910. Jedna z tych liczb jest w dokumencie po to, żeby wprowadzić w błąd.

---

## S7. **Korner nie wierci** — a PLAN i FORMATKI zamawiają u niego CNC. Zamówienie jest niewykonalne w takiej postaci

**Co się stanie.** Składasz zamówienie w KornerGo z pozycją, której dostawca nie realizuje. Płyty przyjadą pocięte i oklejone, **bez ani jednego otworu**: bez puszek Ø35 pod 36 zawiasów, bez rzędów pod konfirmaty, bez nawiertów pod prowadniki, bez otworów pod półki. Montaż stoi do czasu zorganizowania wiercenia gdzie indziej — a płyty leżą już w mieszkaniu.

**DOWÓD — projekt sam sobie przeczy między plikami.**
- `PLAN.md` pkt 12: „**Zlecić Korner** (płyty, korner.pl) — KornerGo / e-Rozkrój, oddział Piekary Śląskie: cięcie formatek + oklejanie krawędzi + **CNC (puszki 35 pod zawiasy, nawierty)**"
- `FORMATKI-ROBOCZE.md` sekcja 4.1: „zamówienie rozkroju z oklejaniem i **CNC (puszki 35 pod zawiasy!)** w KornerGo"
- `_montaz_prosty.py` (linia nagłówkowa) mówi prawdę: „Korner tnie i okleja, ale **NIE WIERCI** — otwory załatwiasz jedną z dwóch dróg poniżej"
- Czyli jedyny plik w projekcie, który zna warunki dostawcy, to jednostronicowa instrukcja PDF — a dwa dokumenty, z których się zamawia, obiecują usługę, której nie ma.

**Prawdopodobieństwo: PEWNE** (warunek dostawcy jest dany).

**KOSZT PO FAKCIE.** Z dokumentu (`_montaz_prosty.py`): usługowe wiercenie **1–5 zł/otwór, ~150–400 zł przy tej kuchni** — plus transport płyt do stolarni i z powrotem, plus opóźnienie. Wariant „sam": przyrząd do puszek 35 z ogranicznikiem **60–120 zł** + wiertło stopniowe ~15 zł, razem **~200 zł** — ale wtedy **początkujący wierci 36 puszek Ø35 na głębokość 12,5 mm we froncie 18 mm**, a `_montaz.py` str. 5 sam nazywa to pułapką nr 4: „Za głęboka puszka 35 = **dziura na wylot we froncie**. Taśma na 12,5 mm." Każda przewiercona puszka = front do wymiany + kolejny transport.
**KOSZT TERAZ.** Wpisanie do PLAN pkt 12 i FORMATKI pkt 4 realnego zakresu usługi Korner + decyzja „droga A czy B" **przed** złożeniem zamówienia. **0 zł.**

---

## S8. Geometria budowlana nigdy nie została zmierzona — blaty 2389 i 1950 mm łączone frezem w narożnikach, których kąta nikt nie zna

**Co się stanie.** Blaty przyjadą jako prostokąty (`Blat B 2389×635`, `Blat A 1950×635`, `Blat C1 947×635`) i mają być łączone **frezem + śrubami łącznikowymi w trzech narożnikach**. Jeśli narożnik A/B albo B/C nie ma 90° (typowe odchylenie w mieszkaniu po przebudowie ścian: 5–20 mm na 2 m), łączenie frezowane **nie zejdzie się** — powstanie klin, którego nie zamaskujesz. Analogicznie przy ścianach: przy odchyleniu 10 mm na 2,4 m blat 2389 dolegnie do ściany w jednym punkcie, a szczelina przy oknie/fartuchu będzie zmienna.

**DOWÓD.**
- `FORMATKI-ROBOCZE.md` sekcja 2: „Łączenia blatów: **3** (narożnik A/B przy pilastrze, narożnik B/C1, A/ramię) — **frez + śruby łącznikowe 3 kpl**, silikon."
- `PLAN.md` pkt 11.2: „Ściana B: 238,9 dołem/górą; **przekątne narożników A/B i B/C**" — pomiar **zapisany, niewykonany**.
- Nigdzie w dokumencie nie ma ani jednej liczby o kątach, pionach czy płaskości. `[BRAK DANYCH]`
- `_kontrola.py` zakłada idealne prostokąty (`Modul(x0,y0,x1,y1)`) i pomieszczenie o kątach prostych. Nic tego nie kwestionuje.
- Do tego dochodzi **blat A wokół pilastra**: pilaster wystaje 155 mm na odcinku 670 mm (`_kontrola.py`: `DA1` ma `x0=155`, `GA1` ma `x0=155`). Blat A jest w liście jako prosty prostokąt **1950×635** — **nie ma nigdzie zapisu, że wymaga wycięcia narożnika 155×670**. Bez tego wycięcia blat po prostu nie wejdzie na miejsce. Pierwszorazowiec ma to wyciąć wyrzynarką w laminacie 38 mm, w kącie wewnętrznym (najtrudniejsze cięcie w całej kuchni, z ryzykiem odprysku laminatu na widocznej krawędzi).

**Prawdopodobieństwo: WYSOKIE.** Pomieszczenie jest po przebudowie ścian (`PLAN.md` pkt 7: „ta sama kuchnia **po przebudowie ścian**"), w stanie remontowym, a przekątnych nikt nie mierzył.

**KOSZT PO FAKCIE.** Blaty laminowane są cięte na wymiar — źle docięty blat 2389×635 to cała formatka. Do tego zniszczone łączenie frezowane wymaga nowego kompletu śrub i nowej krawędzi. Kwota: `[BRAK DANYCH]`.
**KOSZT TERAZ.** Dwie przekątne miarą (pkt 11.2) + dopisanie wycięcia 155×670 do pozycji „Blat A" + rozważenie zamówienia wycięć w CNC zamiast wyrzynarką (dokument sam daje tę alternatywę: „albo CNC przy rozkroju"). **0 zł, pół godziny.**

---

## S9. Kuchnia projektowana pod AGD, którego nie ma — nisza piekarnika ma **10 mm zapasu** przy nieznanym modelu

**Co się stanie.** Formatki DA2 są policzone pod niszę **590 mm**, ale piekarnika jeszcze nie ma. Rachunek: korpus 720 − nisza 590 − trawers nośny 18 = **112 mm** na szufladę pod piekarnikiem, a front szuflady zamówiony na **110 mm**. Jeśli kupiony piekarnik wymaga niszy **600** (bardzo częsty wymóg), zostaje **102 mm** i **front 110 nie wchodzi** — szuflada na blachy przepada, a razem z nią zamówiony komplet prowadnic nom. 500.

To samo dotyczy trzech innych urządzeń:
- **Okap** — niekupiony. `PLAN.md` pkt 7: „recyrkulacyjny z filtrem węglowym `[P]` — **zakup inwestora**"; `_formatki.py`: „konstrukcja wg karty okapu `[?]`"; `FORMATKI-ROBOCZE.md`: „Podnośnik frontu okapu (Aventos HK-S **lub wg okapu**) — **dobór po zakupie okapu**". Korpus GA3 (bok 400×998 ×2, wieniec 564×400 ×2, front uchylny 596×400) jest już w liście do cięcia.
- **Zmywarka** — model `[BRAK DANYCH]`. Front `446×713` zamówiony pod nieznany zawias/wysokość.
- **Zlew** — model `[BRAK DANYCH]`. Wycięcie „wg szablonu z kartonu zlewu" (`_montaz.py` str. 5) — szablonu nie ma, bo zlewu nie ma.

**DOWÓD.** `FORMATKI-ROBOCZE.md`: `| DA2 piekarnik+indukcja — front szuflady dolnej | 596×110 |`, `| DA2 … — trawers nośny piekarnika | 564×560 |`; `_montaz.py` str. 3: „trawers NOŚNY na płask, jego GÓRNA płaszczyzna **600 mm** od górnej krawędzi boku (= nisza 600; **sprawdź kartę piekarnika, bywa 590**)" — dwie różne liczby w dwóch dokumentach tego samego projektu, przy zapasie 10 mm.

**Prawdopodobieństwo: ŚREDNIE-WYSOKIE.** Zapas 10 mm przy nieznanym urządzeniu to loteria; okap i zmywarka to trzy kolejne losowania.

**KOSZT PO FAKCIE.** Front szuflady 596×110, ewentualnie korpus GA3 w całości (jeśli okap wymaga innej konstrukcji — komin, wieniec, wysokość), front zmywarki 446×713. Kwota: `[BRAK DANYCH]`.
**KOSZT TERAZ.** Kupić (albo tylko wybrać i pobrać karty techniczne) piekarnik, okap, zmywarkę i zlew **przed** rozkrojem. **0 zł materiału ponad to, co i tak trzeba kupić.**

---

## S10. Kuchnia będzie ciasna i w połowie pusta — trzy narożniki ślepe, przez które nie przejdzie garnek, i korytarz roboczy **81,5 cm**

**Co się stanie po roku.**

**(a) Garnki nie wejdą tam, gdzie plan je umieścił.** `PLAN.md` pkt 5a: „**DA1 narożna ślepa (front 240)** — garnki i duże naczynia — **248 l tuż przy indukcji**". Front ma **240 mm**, po odjęciu przylgi i zawiasu światło otworu to ok. 220 mm. **Garnek o średnicy 24–28 cm przez ten otwór nie przejdzie.** Ta sama pojemność „odzyskana" w v3.10 jest dostępna wyłącznie na wyciągnięcie ręki w bok, na głębokość 600 mm (dokument: „sięg w ślepą część 600"). To będzie pusta szafka.

**(b) Trzy szafki z ośmiu są martwe.** DA1 (front 240 na korpus 850), RL1 (martwe pole ~202 l — „dostęp bokiem"), DC1 (narożnik północny ~236 l — „zostaje na **sięg ręką**"). Łącznie ok. **686 l pojemności, do której trzeba klękać i sięgać na oślep**. W całej kuchni jest przy tym **6 szuflad**: 3 w RL1 (po 300 mm szerokości), 1 w DA2, 2 wewnętrzne w DC1.

**(c) Korytarz roboczy przy zlewie ma 81,5 cm, nie 85.** `PLAN.md` pkt 4 podaje `~85 (195−60−50)` — rachunek zakłada blat ciągu B o głębokości **600**. `FORMATKI-ROBOCZE.md` zamawia **`Blat B 2389×635`**. Rzeczywisty prześwit między krawędziami blatów: **1450 − 635 = 815 mm**. Poniżej progu roboczego 110 podanego w tej samej tabeli i poniżej wartości, na którą inwestor się zgodził.
Konsekwencja codzienna: przy otwartych drzwiach szafki pod zlewem (front 397 mm wychyłu) i wysuniętej szufladzie RL1 (nominał 400) **suma wysuwów 797 mm przekracza prześwit 815 mm** — dwóch rzeczy naraz otworzyć się nie da. Kucając do zlewu, uderzasz plecami w kant blatu ramienia na wysokości 910 mm.

**(d) Nadwis blatu 56 mm.** Blat 635 na korpusie 560 + front 19 → blat wystaje **56 mm poza lico frontu** (standard 20–30). Okruchy, kolana, i to właśnie te 35 mm zjadły korytarz z (c).

**(e) „Strefa śniadaniowa" nią nie jest.** `PLAN.md` pkt 5a: „Blat ramienia (50) = strefa odstawcza/**śniadaniowa**". Blat 500 mm głęboki stoi na korpusie RL1 z frontem od północy — **nie ma żadnego nadwisu na kolana**. Nie da się przy nim usiąść.

**(f) Trójkąt roboczy przecina bryłę ramienia.** `PLAN.md` pkt 4 podaje boki 1,3–1,8 m i sumę ~4,5 m. Z modelu w `_kontrola.py` wychodzi 1666 + 1216 + 2007 = **4889 mm**, a odcinek lodówka→indukcja przechodzi **przez ramię L** (x 0–1176, y 1450–1950). Realna trasa jest dłuższa o obejście ramienia.

**DOWÓD.** `PLAN.md` pkt 5 (DA1 „front 240", DC1 „front 345", RL1 „dostęp bokiem"), pkt 5a (przypisania funkcji), pkt 4 (tabela przejść), `FORMATKI-ROBOCZE.md` sekcja 2 (blaty 635).

**Prawdopodobieństwo: PEWNE.** To nie jest ryzyko — to policzalna konsekwencja przyjętej geometrii.

**KOSZT PO FAKCIE.** Nie da się naprawić bez przebudowy: skrócenie ramienia = nowy blat ramienia + **nowy panel ryflowany 1176×910 od dostawcy zewnętrznego** + nowy blat A. Zwiększenie liczby szuflad = nowe fronty i korpusy. Praktycznie: **nie naprawia się, żyje się z tym.** Kwota: `[BRAK DANYCH]`.
**KOSZT TERAZ.** Decyzje na papierze: (1) blat 600 zamiast 635 → korytarz wraca do 85 cm; (2) DA1 zamieniona na normalny moduł szufladowy zamiast narożnej ślepej z frontem 240; (3) świadome przyjęcie do wiadomości, że narożniki są magazynem rzeczy rzadkich, a nie garnków — i przeniesienie garnków do modułu z frontem ≥ 450. **0 zł.**

---

## Poza dziesiątką — sześć rzeczy, które też kosztują

**P1. Przejście ma 596 mm, nie 600 — reguła nadrzędna `[P]` jest złamana już na papierze.**
`PLAN.md` v3.11: „Poprawiono też ramię 1180 → **1176**, żeby przejście miało pełne 600, a nie 596." Poprawka nie dotarła do blatów: `Blat A 1950×**635**` + `Blat ramienia **545**×500` = **1180 mm**. Ścianka zaczyna się na 1776 → **przejście 596**. `_kontrola.py` K6 mierzy `SCIANKA[0] − max(m.x1 for m in RAMIE)` = 1776 − 1176 = 600 → **PASS**, bo model zna korpusy, nie blaty. Naprawa teraz: 4 mm docinki na papierze. Naprawa po fakcie: docinka blatu po sklejeniu narożnika.

**P2. Fronty 716 mm są zamówione, zanim zapadła decyzja o systemie uchwytu.**
`PLAN.md` pkt 5: „fronty bezuchwytowe (**frez/gola**)"; `FORMATKI-ROBOCZE.md` sekcja 3: „Listwa gola / frez uchwytowy | ~5 mb | **decyzja technologiczna: profil alu vs frez CNC w płycie**". Profil gola wchodzi pod blat nad frontami i zabiera 40–50 mm ich wysokości. Jeśli padnie na gola, **wszystkie fronty dolne 716 są za wysokie** — to cała pozycja „beż/kaszmir mat 3,3 m² netto" do wyrzucenia.

**P3. Okap nie przykrywa przedniego pola indukcji.**
GA3 ma 400 gł. + 19 front = **419 mm** wysięgu. Płyta Bosch 572×512 na blacie 635 sięga do ok. **562 mm** od ściany. Przednie pole grzejne jest **143 mm poza obrysem okapu** — przy okapie **recyrkulacyjnym** (bez kanału, `PLAN.md` pkt 7) to znaczy, że para z przedniego palnika idzie na szafki i sufit. `_kontrola.py` K4 sprawdza wyłącznie oś wzdłuż ściany (`PLYTA = (864, 1436)` — tylko y), głębokości nie zna → **PASS**.

**P4. Ramię kotwione do posadzki drewnianej.**
`FORMATKI-ROBOCZE.md`: `| Kątowniki montażowe (ramię do posadzki, ścianka) | 8 szt |`; `PLAN.md` pkt 10: podłoga **jasny dąb**. Jeśli to podłoga pływająca, przykręcenie mebla przez nią blokuje jej pracę — po sezonie grzewczym szczeliny albo wybrzuszenie. Typ montażu podłogi: `[BRAK DANYCH]`.

**P5. Cokołu jest za mało o ok. 1,9 mb.**
Zamówione: `| Listwa cokołowa (czarny mat), łącznie ~5 mb |`. Suma widocznych lic z modelu: ciąg A 1450 + ramię (północ) 1176 + bok ramienia 500 + ciąg B 1845 + ciąg C 1885 = **6856 mm ≈ 6,9 mb**. Braknie w trakcie montażu, a dekor „czarny mat" trzeba będzie domawiać osobno (0,8 m² w całym projekcie — minimalne zamówienie płyty to osobny problem).

**P6. Instrukcja montażu opisuje moduły, których nie ma.**
`_montaz.py` str. 3: „**DA1 (3 szuflady)**: NIE wkręcaj prowadników zawiasów…" — DA1 od v3.10 jest narożną ślepą z drzwiami. „**DC1 (narożna ślepa): korpus 900**" — w PLAN 945. „**GÓRNE … (gł. 320)**", „boki 998×**320**", „x = 50/160/270" — a decyzja `[P]` to **400**. `_montaz.py` str. 5 i `FORMATKI-ROBOCZE.md` pkt 4.6: „Ramię: **RL1+RL2**" — RL2 zlikwidowany w v3.8 i nie istnieje w formatkach. **Pierwszorazowiec dostaje instrukcję wiercenia do innej kuchni.** Otwory wywiercone wg złego szablonu = formatka do wymiany.

---

# CZĘŚĆ 2 — Założenia niesprawdzone pomiarem

**Łącznie: 24 założenia.** Rozbicie: **A. geometria budowlana — 12**, **B. instalacje i wentylacja — 4**, **C. dane wejściowe produktów i technologii — 8**.

Kryterium wpisania na listę: założenie ma status roboczy (`[~]`, `[?]`) albo status `[P]` nadany bez pomiaru — i jego fałszywość zmienia listę formatek.

## A. Geometria budowlana (12)

| # | Założenie | Gdzie w dokumencie | Co się zawali, jeśli fałszywe | Jak sprawdzić |
|---|---|---|---|---|
| A1 | Pilaster ma **67 cm długości** wzdłuż ściany A (a nie: uskok biegnie całą ścianą) | pkt 2 status `[P]`, ale pkt 11.11 `[?]`: „67 wg szkicu, **czy cała długość ściany?** … sam rzut tego nie rozstrzyga" | Cała ściana A: DA1, DA2, GA1–GA4, blat A, blenda 610. Okap GA3 przy głębokości 245 przestaje działać | Miara wzdłuż ściany A od narożnika B do końca uskoku |
| A2 | Pilaster ma **15,5 cm głębokości na całej wysokości** | pkt 9: „Pilaster ≠ 15,5×67 **na różnych wysokościach** → pomiar w 3 punktach" | GA1 245 gł. (wisi na licu pilastra, pkt 11a) i blenda dolna 610 — złe wymiary | Trzy pomiary: 30 / 150 / 240 cm od podłogi |
| A3 | Narożnik A/B ma **90°** | pkt 11.2 „przekątne narożników A/B i B/C" — **niewykonane** | Łączenie frezowane blatów A/B nie zejdzie się; klin przy ścianie | Przekątne prostokąta 60×60 cm w narożniku |
| A4 | Narożnik B/C ma **90°** | jw. | Łączenie B/C1 (blat 2389 + 947); DC1 narożna nie dolegnie | jw. |
| A5 | Ściany są **w pionie** na 2478 mm | `[BRAK DANYCH]` — nigdzie ani jednej liczby | Górne 998 do sufitu i słupek 2378 — fronty w jednej płaszczyźnie nie wyjdą; blenda 47 nie wchłonie odchyłki | Poziomica 2 m przy każdej ścianie, góra/dół |
| A6 | **Sufit 2478** jest wysokością docelową | pkt 2 `[P]` z dopiskiem „kontrola po posadzce!", pkt 8.5, pkt 9, pkt 11.5 | Wszystkie elementy pionowe (S2) | Pomiar w 4 punktach **po posadzce** |
| A7 | Grubość układu posadzkowego (podkład + dąb) | `[BRAK DANYCH]` | A6; wysokość blatu 910 przestaje wynikać ze wzrostu 182 | Karta produktu podłogi |
| A8 | Podłoga jest **płaska** (rozrzut mieszczący się w regulacji nóżek 150) | `_montaz.py` str. 5: „Poziomowanie: zawsze od NAJWYŻSZEGO punktu podłogi" — bez liczby | Przy rozrzucie >20–25 mm nóżki nie wyregulują; blat przestaje być poziomy, blaty w L nie zejdą się | Poziomica + klin, 6 punktów |
| A9 | Ścianka ma **wysięg 77 cm** | pkt 2 `[~]`: „»77 = wymiar małej ścianki«; do pomiaru łańcuchowego" | Przejście ramię↔ścianka (dziś 596). Przy 82 → przejście 546 | Pomiar od ściany C do czubka ścianki |
| A10 | Ścianka ma **grubość 9 cm** | pkt 2 `[~]` | Kontrola krzyżowa linii południowej; blenda dystansowa lodówki | Miara |
| A11 | Ścianka stoi na **1885** i wypada naprzeciwko ramienia | pkt 2 `[P]`, ale kontrola krzyżowa daje **188,5 + 9 = 197,5 vs 195 → rozjazd 25 mm** (dokument pisze „≈") | Ramię i ścianka nie będą w jednej linii — widoczny uskok 25 mm w otwartej przestrzeni | Pomiar łańcuchowy C (pkt 11.3) |
| A12 | Długość ściany A / początek otworu 127 | Łańcuch **nie domyka się**: pkt 2 „otwór do salonu: od ~195 do **~322** od B" vs pkt 1 „pomieszczenie ~254,6 × **~262+**" | Jeśli otwór zaczyna się bliżej niż 195, koniec ciągu A / ramię nie ma ściany do przykręcenia | Pomiar łańcuchowy A (pkt 11.1) |

## B. Instalacje i wentylacja (4)

| # | Założenie | Gdzie w dokumencie | Co się zawali | Jak sprawdzić |
|---|---|---|---|---|
| B1 | Podejścia wody i odpływu wypadają **pod DB1 (750–1550)** | pkt 2 `[~]`, pkt 7 „podejścia nisko na B `[~]`", pkt 11.7 — niewykonane | Jeśli wypadają w pasie 155–600, kolidują z korpusem DA1 (narożna ślepa, 248 l „odzyskane" w v3.10) — trzeba przekuwać albo skasować DA1 | Odkrycie ściany B, pomiar wysokości i rozstawu |
| B2 | Puszka siłowa na A pozwala ustawić **DA2 na 850–1450** | pkt 7 „obwód siłowy — puszka na A `[?]` **potwierdzić 32A**", pkt 11.8 | Sprzeczność wewnętrzna: pkt 9 mitygacja brzmi „DA2 **pozycjonowany do wypustu**; kolejność DA1/DA2 może się zamienić" — a v3.9 `[P]` przybija DA2 do 850–1450, bo inaczej **front piekarnika chowa się za ramieniem**. **Mitygacja jest niewykonalna.** Jeśli puszka jest gdzie indziej → kucie po posadzce | Otwarcie puszki, pomiar pozycji, sprawdzenie obwodu i przekroju |
| B3 | Obwód dla indukcji Bosch PXE601DC1E to **32A** | pkt 7 `[?]` „potwierdzić 32A" | Bez odpowiedniego obwodu płyta nie zadziała; przekładanie instalacji po posadzce docelowej | Rozdzielnica + elektryk |
| B4 | Kratka wentylacyjna nie wypada w strefie zabudowy | pkt 8.2 „Zlokalizować kratkę `[?]` … kratki **nie zabudowywać na głucho**", pkt 9, pkt 11.6 | Górne A i C idą do sufitu na całej długości. Kratka za zabudową = zamurowana wentylacja grawitacyjna przy okapie **recyrkulacyjnym** (bez kanału) → wilgoć i zapachy | Znaleźć kratkę, zmierzyć pozycję i wymiar |

## C. Dane wejściowe produktów i technologii (8)

| # | Założenie | Gdzie w dokumencie | Co się zawali | Jak sprawdzić |
|---|---|---|---|---|
| C1 | Piekarnik potrzebuje niszy **590** | `_formatki.py` „nisza 560×590 wg karty" vs `_montaz.py` „= nisza 600; bywa 590" | Przy niszy 600 zostaje 102 mm, a front szuflady ma 110 → szuflada na blachy przepada (S9) | Karta kupionego piekarnika |
| C2 | Okap zmieści się w korpusie GA3 400 gł. | pkt 7 „zakup inwestora", `_formatki.py` „konstrukcja wg karty okapu `[?]`" | Korpus GA3 (bok 400×998 ×2, wieniec ×2, front uchylny) + podnośnik | Karta okapu — **przed rozkrojem** |
| C3 | Zmywarka 45 zmieści się w świetle 450×820+ i przyjmie front 446×713 | pkt 7, model `[BRAK DANYCH]` | Front do wymiany; wnęka bez korpusu bocznego od zachodu (formatki nie mają boku niszy) | Karta zmywarki |
| C4 | Zlew 80 z ociekaczem zmieści się w blacie 635 przy oknie od 752 | pkt 5 DB1, model `[BRAK DANYCH]`; wycięcie „wg szablonu z kartonu zlewu" | Zlew 750–1550 vs okno 752–1608 — margines po stronie zachodniej wynosi **2 mm** | Kupić zlew, wziąć szablon |
| C5 | Lodówka ma **190 cm z zawiasami** | pkt 2 `[P]` 60×65×190, ale pkt 11.5 wymaga: „wysokość lodówki **z zawiasami**" | Nadstawka C4 od 1950; przy wyższej lodówce C4 (bok 580×528 ×2, 2 fronty 327×524) do przeliczenia | Miara na lodówce |
| C6 | Rozkład okna 59,7 / 85,6 / 94,7 | pkt 2 `[P]`, ale suma **240,0 vs ściana 238,9 → rozjazd 11 mm** | Zlew 750–1550 pod oknem 752–1608: **2 mm zapasu od zachodu**. Rozjazd 11 mm zjada go z nawiązką → zlew wystaje poza wnękę okienną | Pomiar łańcuchowy okna (pkt 11.4) |
| C7 | Parapet jest na **166,1** | pkt 2 `[~]` — **wartość wyliczona (247,8 − 81,7), nie mierzona**; zakłada, że okno kończy się dokładnie przy suficie, bez nadproża | Wysokość fartucha, ewentualna kolizja z baterią; głębokość parapetu nad blatem 635 nieznana | Miara od podłogi (po posadzce) |
| C8 | System uchwytu: **frez czy gola** | `FORMATKI-ROBOCZE.md` sekcja 3: „decyzja technologiczna: profil alu vs frez CNC" — **nierozstrzygnięta**, a fronty 716 już policzone | Przy gola wszystkie fronty dolne są za wysokie o 40–50 mm → 3,3 m² frontu do kosza (P2) | Decyzja + karta profilu |

**Podsumowanie Części 2.** Projekt ma **24 nierozstrzygnięte założenia**, z czego **4 mają w dokumencie status `[P]`** mimo braku pomiaru albo mimo niedomkniętej kontroli krzyżowej (A1 pilaster, A6 sufit, A11 pozycja ścianki, C6 rozkład okna). Protokół z `protokol-weryfikacji.md` pkt 4 stawia regułę: „Każdy wymiar musi domknąć się w co najmniej dwóch łańcuchach. **Jeśli łańcuch się nie domyka — pytaj, nie zaokrąglaj.**" W trzech miejscach dokument zaokrągla zamiast pytać: 240 ≈ 238,9 (11 mm), 197,5 ≈ 195 (25 mm), 1887 ≈ 1885 (2 mm, zanim doda się blendę 70 mm).

---

# CZĘŚĆ 3 — Czego nie łapie automat, a raportuje PASS

`_kontrola.py` daje **PASS: 9 kontroli, 0 błędów, 0 uwag** i **5/5 w regresji**. To jest prawda o modelu w tym pliku — i nieprawda o projekcie. Poniżej klasy błędów, przez które PASS przechodzi bez drgnienia.

### 3.1. Model jest **dwuwymiarowy** — nie istnieje oś Z

`class Modul(nazwa, x0, y0, x1, y1)`. Nie ma ani jednej wysokości. Automat **nie może** wykryć:
- słupka C2 wyższego od pomieszczenia (2378 + 150 = 2528 > 2478) — **S1**
- panelu, którego przekątna przekracza wysokość pomieszczenia (2569 > 2478) — **S1**
- sufitu zmierzonego przed posadzką — **S2**
- niszy piekarnika i szuflady 110 mm — **S9**
- odstępu górne↔blat: `PLAN.md` pkt 6 deklaruje **600**, a 1480 − 910 = **570**
- wysokości blatu: 720 + 150 + 38 = **908**, deklarowane **910 `[P]`**
- fałszywej wysokości korpusów w pkt 5 (`×820` zamiast 720)
- kolizji z pilastrem/gzymsem na wysokości szafek górnych
To jest największa dziura, bo **cztery z dziesięciu scenariuszy porażki leżą wyłącznie w pionie**.

### 3.2. Kontrola sprawdza **model, nie listę do cięcia** — a te dwa dokumenty się rozjechały

`protokol-weryfikacji.md` pkt 1 stawia wymóg wprost: „Wymiary modułów **NIE mogą żyć równolegle w trzech miejscach** (PLAN.md, generator schematu, generator formatek) — zawsze się rozjadą. Trzymaj model w jednym pliku." **Projekt tego wymogu nie spełnia.** Dowody rozjazdu, wszystkie przy PASS:

| element | `PLAN.md` | `_kontrola.py` | `_formatki.py` / FORMATKI |
|---|---|---|---|
| DC1 szerokość / front | 945 / 345 | 945 / 345 | **900 / 446** |
| DC1 głębokość | 546 | 546 | **560** |
| RL1 podział frontu | drzwi 300 + 3 szuflady 300 | jeden front 600 | **1 front 446 + blenda 430** |
| RL1 głębokość | 500 | 500 | **460** |
| głębokość blatu | 600 (ramię 650) | — | **635 / 500** |
| wysokość korpusów dolnych | 820 (tabele) / 720 (nagłówek) | — | **720** |
| DA1 3 szuflady? | narożna ślepa | narożna ślepa | narożna ślepa, ale **`_montaz.py`: „DA1 (3 szuflady)"** |
| RL2 | nie istnieje od v3.8 | nie istnieje | **`_montaz.py` i FORMATKI pkt 4.6: „RL1+RL2"** |
| głębokość górnych | 400 `[P]` | 400 | **`_montaz.py`: 320** |

Automat weryfikuje kopię projektu, która nie jest tą, którą się zamawia i wg której się montuje. **To jest gorsze niż brak automatu** — daje pisemne PASS dokumentowi, którego nie czytał.

### 3.3. **Czego nie ma w modelu, tego nie ma w kontroli**

W modelu istnieje 13 brył. Nie istnieją: **blaty**, **blendy jako bryły**, **GC1**, **GC2**, **C4 nadstawka**, **cokoły**, **pilaster jako bryła** (tylko jako `x0=155` u dwóch modułów), **okno**, **parapet**, **kratka wentylacyjna**, **podejścia wod-kan**, **blenda dystansowa lodówki**.

Skutki, wszystkie przy PASS:
- **K6 mierzy korpusy, nie blaty**: `SCIANKA[0] − max(m.x1 for m in RAMIE)` = 600 ✓, a blaty (635 + 545 = 1180) dają przejście **596** — czyli reguła nadrzędna inwestora `[P]` jest już złamana, a test jej broni (**P1**).
- **Blenda dystansowa 70 mm nie istnieje w modelu**, więc łańcuch C domyka się co do milimetra i K7 daje ✓ — mimo że w rzeczywistości brakuje **72 mm** (**S3**).
- **GC1/GC2 nie są sprawdzane przez K5 ani K7.** `PLAN.md` obiecuje „GC2: **front w linii słupka C2**" — przy głębokości 400 na ścianie C front wypada 181 mm przed licem słupka. Obietnica jest niewykonalna, kontrola milczy.
- **Ścianka nie jest modułem**, tylko krotką `SCIANKA = (1776, 1885, 2546, 1975)`. Nie wchodzi do list w K2 i K3 → **żadna kolizja mebla ze ścianką nie zostanie wykryta**.

### 3.4. K3 sprawdza wychył drzwi, ale **nie wysuw** i nie dwa fronty naraz

- Pas kontrolny to `PAS = 50` mm. Szuflada wysuwa się **400–500 mm**, cargo tak samo, drzwi piekarnika opadają ok. 500 mm — **żadna z tych wartości nie jest w kodzie**.
- Nie ma kontroli **jednoczesnego otwarcia dwóch frontów naprzeciw siebie**: DB1 (wychył 397) + szuflada RL1 (wysuw 400) = 797 mm w korytarzu 815 mm (**S10c**).
- `if not m.front or m.typ in ("AGD", "szuflady", "uchylny"): continue` — **drzwi lodówki (typ AGD) nie są sprawdzane w ogóle**, a to jest właśnie znany problem projektu (blenda dystansowa, `PLAN.md` pkt 9: „Drzwi lodówki >90° zahaczają o kant ścianki").
- `if W > 700: continue` — szafka zlewowa DB1 (front 800) jest z kontroli wychyłu wypisana całkowicie.

### 3.5. K9 nie zna **frontów dzielonych** — funkcja może istnieć tylko na papierze

`naj = max((m.front[1] - m.front[0]) for m in kand)` — dla RL1 to **600 mm**, choć sekcja szufladowa ma **300**. Gdyby szuflady zmniejszono do 150 mm, K9 nadal dałoby PASS. Kontrola, którą dodano **specjalnie po to**, żeby przebudowa modułu nie skasowała po cichu sztućców, **nie zauważyła, że sztućców nie ma w liście formatek** (**S5**). To jest najczystszy przykład fałszywego bezpieczeństwa w całym projekcie.

Analogicznie K9 zalicza „kosz segregacji" w DB1, bo front ma 800 mm — nie wiedząc, że w tej samej szafce siedzi syfon zlewu i przyłącza zmywarki (`PLAN.md` pkt 7: „przyłącza z DB3").

### 3.6. K4 zna **jedną oś** okapu

`PLYTA = (864, 1436)` to wyłącznie zakres wzdłuż ściany. Głębokość okapu (419 z frontem) vs głębokość płyty (do ~562 od ściany) nie jest porównywana — przednie pole grzejne zostaje poza obrysem okapu recyrkulacyjnego (**P3**), a K4 daje ✓.

### 3.7. Automat nie zna **statusów wymiarów**

W modelu `[P]`, `[~]` i `[?]` nie istnieją. Geometria jest sprawdzana z dokładnością do milimetra na liczbach, z których **24 są nierozstrzygnięte** (Część 2), w tym cztery z fałszywym statusem `[P]`. **PASS na niepomierzonych danych to precyzja bez dokładności.** Brakuje najprostszej możliwej kontroli — K0: „czy jakikolwiek wymiar użyty w modelu ma status inny niż `[P]` potwierdzony pomiarem? jeśli tak → **FAIL: nie zamawiaj**".

### 3.8. Automat nie sprawdza **kompletności listy zakupowej**

Brakuje w `FORMATKI-ROBOCZE.md`, a nic tego nie zgłasza: fronty i dna szuflad RL1, przegroda pionowa RL1, **blenda przysufitowa** (wymagana przez `_montaz.py` str. 5 „blenda sufitowa" i przez `FORMATKI` pkt 4.7 „blenda górna docinana do sufitu"), **blenda górna 230 przy narożniku ramienia** (`PLAN.md` v3.7a), **fartuch — panel ciemny kamień przy indukcji** (`PLAN.md` pkt 10, powierzchnia ok. 1950×570), listwy przyblatowe, wycięcie 155×670 w blacie A, boki wykończeniowe widocznych korpusów (bok RL1 od strony przejścia jest w liście jako „kremowy (korpus)" — surowy korpus na widoku od salonu w kuchni beż/orzech), 1,9 mb cokołu, zawiasy szerokokątne dla DA1 i RL1 (są tylko 2 szt. 155° dla DC1).

### 3.9. Regresja mierzy **nie to, co się wydaje**

`--regresja` odgrywa **5 błędów, które już zostały naprawione** i pokazuje 5/5. To dowodzi wyłącznie, że te pięć poprawek się nie cofnie. **Nie istnieje ani jeden test dla klas błędów z sekcji 3.1–3.8** — pionu, rozjazdu model↔formatki, kompletności listy, statusów. Komunikat „5/5 historycznych błędów wykrytych automatycznie" czyta się jak certyfikat jakości, a znaczy: „nie powtórzyłem pięciu konkretnych pomyłek". Skrypt sam przyznaje jedno ograniczenie („błąd odczytu zdjęcia … nie jest wykrywalny skryptem") — i nie przyznaje ośmiu pozostałych.

---

# Zarzuty dodatkowe

**D1. Projekt nie ma wyceny.** Ani w `PLAN.md`, ani w `FORMATKI-ROBOCZE.md` nie pada żadna kwota za płytę, obrzeże, blat, okucia, AGD ani usługę rozkroju. `FORMATKI-ROBOCZE.md` jest opisana jako „Wersja **do wyceny** w KornerGo" — czyli wycena jest oczekiwana od dostawcy, a inwestor kupujący **na firmę** ma jutro złożyć zamówienie bez znanej kwoty i bez budżetu odniesienia. Jedyne kwoty w projekcie dotyczą narzędzi (150–250 zł) i wiercenia usługowego (150–400 zł). To uniemożliwia racjonalną decyzję „poprawić teraz czy ryzykować" — czyli podważa sens całego zarządzania ryzykiem w pkt 9.

**D2. Dokument zawiera martwe, sprzeczne zapisy, po których montuje pierwszorazowiec.** `PLAN.md` pkt 9 wciąż zawiera ryzyko „**Gzyms/podciąg pod sufitem** … koliduje z pasmem górnych 1480–2478 → 3 pomiary → wariant A/B/C; szczegóły w **pkt 11a**", mimo że v3.7 to odwołało („Odwołane z v3.6: wycięcia 160×(Hg+5) … wieniec 240 … sprzeczność »gzyms vs okno do sufitu«"), a pkt 11a mówi dziś o czymś zupełnie innym (głębokość górnych i pilaster). Do tego numeracja jest rozsypana: **pkt 9a stoi przed pkt 9**. Osoba montująca dostaje instrukcję z odwołaniami donikąd.

**D3. Prompt do wizualizacji opisuje inną kuchnię.** `PLAN.md` pkt 13: „an L-shaped worktop return (~118×**65**)" — a decyzja `[P]` to głębokość **50** (v3.5). „doorway to **bedroom** (127)" — a v3.3a poprawiło to wprost: „otwór 127 … prowadzi do **SALONU** … »sypialnia« … **była błędna**". Renderowana będzie kuchnia, której nikt nie zamówił.

**D4. Kolejność prac w dokumencie jest dobra, a projekt jej łamie.** `PLAN.md` pkt 12: „**Kolejność:** 1) instalacje + posadzka → pomiar finalny → zamówienie". `FORMATKI-ROBOCZE.md` kończy się zdaniem „**Pomiar → cięcie → montaż. Nigdy odwrotnie.**" Cały ten audyt opisuje, co się stanie, gdy tę jedną regułę się złamie — a **nic w narzędziach projektu jej nie egzekwuje**: `_kontrola.py` da PASS w każdej chwili, na dowolnie niepomierzonych danych.

---

# Werdykt

Projekt jest wewnętrznie niespójny na poziomie, który uniemożliwia zamówienie: **ten sam moduł ma różne wymiary w PLAN.md, `_kontrola.py`, `_formatki.py` i `_montaz.py`**, dwa elementy pionowe są matematycznie niemontowalne, łańcuch ściany C nie domyka się o 72 mm, funkcja naprawiona w v3.12 nie istnieje w liście do cięcia, a dostawca nie świadczy usługi, którą projekt u niego zamawia. Automatyczna kontrola raportuje PASS, ponieważ sprawdza dwuwymiarową kopię projektu, a nie dokument, z którego się zamawia i montuje.

**Nie zamawiaj jutro.** Kolejność ratunkowa: (1) 24 pomiary i decyzje z Części 2 — priorytet A1, A6, A9, B1, B2, C8; (2) zejście do jednego źródła prawdy zgodnie z `protokol-weryfikacji.md` pkt 1 — `_formatki.py` musi czytać model z `_kontrola.py`, a nie mieć własne liczby; (3) dodanie do `_kontrola.py` osi Z i kontroli K0 (status wymiarów) oraz K10 (zgodność modelu z listą formatek); (4) dopiero potem rozkrój.
