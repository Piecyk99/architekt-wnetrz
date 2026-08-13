# AUDYT 04 — TECHNOLOG PRODUKCJI PŁYTOWEJ

**Projekt:** kuchnia-wyspa v3.12a · **Materiał audytowany:** `FORMATKI-ROBOCZE.md` (R1, generowany przez `_formatki.py`), `PLAN.md` v3.12a, `_montaz.py`, `_montaz_prosty.py`
**Kontekst wykonawczy:** rozkrój + oklejanie: Korner (płyty, korner.pl) / KornerGo — **Korner NIE WIERCI otworów montażowych** (`skills/architekt-wnetrz/references/dostawcy.md`, wiersz 86). Montaż: **samodzielny (inwestor, początkujący)**.
**Normy odniesienia:** `skills/architekt-wnetrz/references/standardy-meble.md`, `skills/zabudowa-na-wymiar/references/technologia-wykonania.md`, `.../formatki.md`.

> **Ocena ogólna:** rozpiska nie nadaje się do wyceny ani do rozkroju w obecnej postaci. Nie z powodu braku pomiarów (to jest uczciwie zadeklarowane w nagłówku), tylko dlatego, że **generator `_formatki.py` zatrzymał się na logice sprzed v3.10–v3.12** i produkuje formatki modułów, których projekt już nie ma, a nie produkuje tych, które ma. Trzy naprawy opisane w historii PLAN jako kluczowe (DA1 narożna ślepa v3.10, front DC1 345 v3.11, podział frontu RL1 v3.12) **nie są odzwierciedlone ani w jednej formatce.**

---

## 1. INWENTARYZACJA

### 1.1 Co rozpiska zawiera

| Grupa | Pozycji | Uwaga |
|---|---|---|
| Moduły dolne (DA1, DA2, DB0, DB1, DB2, DC1, RL1) | 7 | DB2 = sam front, bez korpusu/wnęki |
| Moduły górne (GA1–GA4, GC1, GC2) | 6 | — |
| Wysokie (C2 słupek, C4 nadstawka) | 2 | C3 zabudowa lodówki — **nie występuje jako moduł** |
| Panele / blendy / cokół | 4 | bok lodówki, panel ryflowany, blenda A, listwa cokołowa |
| Blaty | 4 | wymiary brutto, bez rozdzielenia narożników |
| Pozycje okuciowe | 22 | — |
| **Formatek łącznie (wierszy tabeli 1)** | **77** | — |

### 1.2 Kompletność per moduł

Legenda: ✓ jest · ✗ brak · ! jest, ale wymiar/typ błędny

| Moduł | boki | dno | wieniec/trawersy | plecy | półki | front(y) | Werdykt |
|---|---|---|---|---|---|---|---|
| DA1 narożna ślepa | ✓ | ✓ | ✓ | ✓ | **✗** (PLAN: „drzwi + 1 półka") | **!** 446 zamiast 240 | **niekompletny + błędny** |
| DA2 piekarnik | ✓ | ✓ | ✓ + trawers nośny | ✓ | n/d | **!** front szuflady 110 bez pokrycia w świetle | **błędny** |
| RL1 ramię | ✓ | ✓ | ✓ | ✓ | n/d | **✗** brak 3 frontów szuflad + drzwi 300 | **niekompletny (regresja v3.12)** |
| DB0 cargo 15 | ✓ | ✓ | ✓ | ✓ | n/d | **✗ brak frontu cargo** | **niekompletny** |
| DB1 zlewowa | ✓ | ✓ | ✓ | celowo brak | n/d | ✓ 2×397 | **niekompletny** (brak listew tylnych) |
| DB2 zmywarka 45 | **✗** | **✗** | **✗** | n/d | n/d | ✓ 446×713 | **niekompletny** (wnęka bez boków) |
| DC1 narożna ślepa | ✓ | ✓ | ✓ | ✓ | ✗ | **!** 446 zamiast 345 | **błędny (regresja v3.11)** |
| GA1 górna | ✓ | ✓ ×2 | — | ✓ | **!** 300 gł. przy korpusie 245 | ✓ | **błędny** |
| GA2 wąska | ✓ | ✓ ×2 | — | ✓ | ✓ | ✓ | OK |
| GA3 okap | ✓ | ✓ ×2 | — | ✓ | **✗** | **!** front 400 na korpusie 998 | **niekompletny + błędny** |
| GA4 górna | ✓ | ✓ ×2 | — | ✓ | ✓ | ✓ | OK (brak boku wykończ.) |
| GC1 / GC2 | ✓ | ✓ ×2 | — | ✓ | ✓ | ✓ | OK |
| C2 słupek | ✓ | ✓ ×2 | — | ✓ | ✓ ×2 (za mało) | ✓ 1300+1070 | **błędna wysokość** |
| C4 nadstawka | ✓ | ✓ | ✓ | ✓ | **✗** | ✓ | niekompletny + **zły kolor** |
| **C3 zabudowa lodówki** | **✗ (1 z 2)** | ✗ | ✗ | ✗ | — | — | **MODUŁ NIE ISTNIEJE** |

---

## 2. BRAKI W ROZPISCE

| # | Moduł / miejsce | Brakująca formatka / pozycja | Skutek |
|---|---|---|---|
| K01 | **C3 zabudowa lodówki** | drugi bok pełnej wysokości (zachodni), wieniec górny, trawers, kratka wentylacyjna | C4 (nadstawka 660×528) **nie ma na czym stać od zachodu** — bok C2 kończy się na innej wysokości (patrz B04/B05). Zabudowa lodówki jest w PLAN pkt 5 jako moduł C3, w rozpisce jest wyłącznie „Bok wykończeniowy… 2478×680 — 1 szt" |
| K02 | RL1 ramię | **3 fronty szuflad + front drzwi 300** (v3.12) | Rozpiska = stan sprzed v3.12. Dowód arytmetyczny: front 446 + blenda ślepa 430 = 876; korpus 1176 → **1176 − 876 = 300 mm lica bez żadnej formatki** — dokładnie pas szuflad. Zamówienie tak jak jest = kuchnia bez jednej szuflady, czyli dokładnie luka, którą v3.12 naprawiał |
| K03 | RL1, DA2, DC1 | **dna szuflad — 6 szt** (3+1+2) | Sekcja okuć sama pisze: „przy metalowych bokach… dokupujesz tylko **dno i front**". Ani dna, ani frontów nie ma nigdzie na liście. Szuflady nie zamkną się bez den |
| K04 | DB0 cargo 15 | **front cargo ~146×716**, kolor beż/kaszmir | Cargo 150 mocuje się do frontu meblowego. Bez frontu wyrwa 150 mm w ciągu B |
| K05 | DB2 zmywarka | **bok/panel wnęki od wschodu** + listwa podblatowa mocująca zmywarkę | Wnęka 1550→2000 ma bok tylko od zachodu (bok DB1). Od wschodu jest narożnik z C — nic tam nie stoi. Zmywarka nie ma do czego przykręcić prowadnicy frontu ani blatu |
| K06 | DB1 zlewowa | **listwy tylne** (2× 764×100) | `_montaz.py` s.3: „zamiast pleców dwie listwy 100 na sztorc (góra-tył i dół-tył)". W rozpisce są tylko 2 trawersy górne — brak dolnej listwy tylnej → korpus 800 bez pleców i bez dolnego usztywnienia tyłu |
| K07 | DC1 | **blenda ~47×716** (PLAN pkt 5: „blenda ~47 — dopełnienie C1 do 947") | Ciąg C nie domknie się: 900 + 0 ≠ 947 |
| K08 | Górne (wszystkie) | **blenda / listwa sufitowa** | `FORMATKI` pkt 4.7 obiecuje „blenda górna docinana do sufitu", a rozpiska jej nie zawiera. Norma: fuga do sufitu 10–30 mm + listwa maskująca (standardy-meble.md) |
| K09 | Narożnik GA4 / ramię | **blenda górna 230** (zapisana w PLAN v3.7a) | Element zniknął między wersjami |
| K10 | GA4 | **bok wykończeniowy** (dekor frontu, orzech) | Bok wschodni GA4 kończy ciąg nad ramieniem i jest widoczny z całej kuchni. Rozpiska daje bok **kremowy korpusowy** obok ciemnych frontów |
| K11 | RL1 | **bok wykończeniowy wschodni** (od przejścia 60) | Ten bok stoi w przejściu i jest widoczny z korytarza. Rozpiska: bok kremowy 460×720, obrzeże tylko „0,4 przód" |
| K12 | GA3 okap | **front antresoli ~596×592 + półka dzieląca** | Patrz B08 — 598 mm korpusu bez frontu |
| K13 | C2 słupek | **półka stała usztywniająca** | `_montaz.py` s.3 wprost: „PÓŁKA STAŁA w połowie (rząd na 1190) — usztywnia 2378 wysokości". W rozpisce są 2 półki, obie opisane jak ruchome, bez wskazania stałej |
| K14 | C4 nadstawka | **półka 624×~560** | 660×510 światła bez półki |
| K15 | Zabudowa lodówki / cokół | **kratka wentylacyjna** (cokół + wieniec) | technologia-wykonania §4 i standardy-meble: min 50 mm tył/góra + **kratka w cokole**. W dokumencie tylko wzmianka w kroku montażu, brak pozycji zakupowej |
| K16 | Blat / ściany | **listwy przyblatowe** (profil LB, korner.eu) | PLAN i technologia §2 wymagają zamknięcia styku blat–ściana. Pozycja „Listwa gola / frez uchwytowy ~5 mb" to co innego |
| K17 | Ściana A przy indukcji | **panel fartucha „ciemny kamień"** (PLAN pkt 10) | Nie ma go w żadnym zestawieniu m² |
| K18 | Cała rozpiska | **grubość frontów** | Nagłówek deklaruje tylko „Płyta 18 mm; plecy HDF 3 mm". `_formatki.py` nie ma stałej dla frontu. PLAN pkt 11a liczy geometrię z **frontem 19** (400+19=419). Ryzyko zamówienia frontów 18 i rozjechania się cofnięcia górnych |
| K19 | Cała rozpiska | **kierunek słoja per formatka** | `formatki.md` wymienia to jako obowiązkowy element metody. Dekory drewnopodobne: orzech (fronty górne, C2 1300/1070, bok lodówki 2478, C4 poziome 327×524) — bez oznaczenia Korner potnie pod optymalizację i **fronty nie zgrają się rysunkiem** |
| K20 | Cała rozpiska | **wskazanie krawędzi oklejanych per formatka** | Trawersy i półki mają zapis samo „0,4" — bez informacji która krawędź. Formularz e-Rozkroju wymaga krawędzi, nie samej grubości |
| K21 | Okucia | **kosz segregacji do DB1** | PLAN 5a przypisuje DB1 „kosze segregacji", kontrola K9 wymaga ≥450. Na liście okuć nie ma kosza |
| K22 | Okucia | **złącza korpus–korpus** (EuroScrew M4×35 + tulejka, 2 na złącze) | standardy-meble: „Łączenie korpusów ze sobą: śruba EuroScrew M4×35 + tulejka, 2 na połączenie". Dokument każe skręcać „2 wkrętami 4×30 przez boki" — wkręt 4×30 w płytę wiórową przez 18+18 mm nie trzyma na powtarzalnie |
| K23 | Okucia | **zaślepki konfirmatów** | Cała konstrukcja na konfirmatach; łby będą widoczne w każdym otwartym korpusie |
| K24 | Okucia | **typ kołka/kotwy do ściany + materiał ściany** | technologia §5 wymaga rozpoznania materiału. **PLAN pkt 11 (11 pozycji pomiarowych) nie zawiera pozycji „materiał ściany pod górne"** — pominięcie krytyczne, patrz R05 |
| K25 | Okucia | **moc zasilacza LED** | „zasilacz 24V — 1 szt" bez W. 3 mb × ~9,6 W/m = 29 W → wymagany ≥35 W |
| K26 | Blaty | **liczba i format arkuszy blatu** | 4 pozycje długości, bez przełożenia na blaty handlowe (4100 mm) i bez zaślepek/listew końcowych blatu ramienia |
| K27 | Formatki | **blenda dystansowa lodówka–ścianka ~70×2478** | Pozycja figuruje **w sekcji okuć** (poz. 20), a jest formatką z płyty. W tej sekcji nie trafi do rozkroju ani do zestawienia m² |

**Braki: 27.**

---

## 3. BŁĘDY TECHNOLOGICZNE (z arytmetyką)

### B01 — DA1: front 446 zamiast 240; blenda policzona dwa razy
Rozpiska (w. 13–14): `DA1 — front 446×716` + `DA1 — blenda ślepa 430×716`.
PLAN pkt 5: *„korpus 850×820×405, **front 240** (610→850)… Front max 240: szersze drzwi uderzyłyby w korpus ciągu okna, zapas 13 mm"*.
Arytmetyka lica DA1: **446 + 430 = 876 > 850** — suma frontu i blendy przekracza szerokość korpusu o 26 mm. Fizycznie niemożliwe.
Poprawnie: blenda 610 (osobna pozycja, w. 84) + front 240 → **610 + 240 = 850 ✓**.
Skutek: front 446 **uderzy w korpus ciągu B** (dokładnie ta kolizja, którą v3.10 nazwała po imieniu), a blenda ślepa 430 jest pozycją nadmiarową — blenda dla tego odcinka już istnieje.

### B02 — DC1: front 446 zamiast 345 (regresja wykrycia z v3.11)
Rozpiska (w. 40): `DC1 — front 446×716`.
PLAN pkt 5 / v3.11: *„front ma tylko **345 mm** — pas 0→600 lica jest zasłonięty korpusem zmywarki"* (kontrola K8).
Arytmetyka: **446 + 430 (blenda ślepa) = 876**, korpus 900 → **24 mm lica bez pokrycia**, a jednocześnie front 446 wchodzi 101 mm w strefę zasłoniętą korpusem zmywarki (446 − 345 = 101) → **drzwi nie otworzą się**.
To jest błąd, który własna kontrola projektu (`_kontrola.py`, K8) wykryła 2026-08-13 — generator formatek go nie przejął.

### B03 — RL1: brak pasa szuflad (regresja v3.12)
Patrz K02. Dowód: 1176 − (446 + 430) = **300 mm** — dokładnie szerokość pasa szuflad z v3.12.

### B04 — C2 słupek: wysokość nie domyka się z żadnym cokołem
Rozpiska: `C2 — bok 580×2378`, nagłówek: „dolne 720 (**nóżki 150**)"; poz. cokołu: `5000×150`.
Arytmetyka: **150 (nóżka) + 2378 (korpus) = 2528**, sufit **2478** → słupek **przebija sufit o 50 mm**.
Odwrotnie: 2478 − 2378 = **100** — wysokość 2378 została policzona dla cokołu **100 mm** (wartość „typowa" ze standardy-meble.md), a projekt jeździ na 150.
Poprawnie przy nóżkach 150: korpus **2328**. PLAN pkt 6 („Góra zabudowy 2478 — słupek C2… do sufitu") potwierdza, że intencja to 2478 od podłogi.

### B05 — Zabudowa lodówki: dwa różne układy pionowe stykają się bokiem
`Bok wykończeniowy zabudowy lodówki 2478×680` — wymiar **od podłogi do sufitu, bez cokołu**.
Sąsiadujący od zachodu bok C2: **580×2378 na nóżkach 150 → góra na 2528**.
Różnica **2528 − 2478 = 50 mm** na styku dwóch elementów, które mają tworzyć jedną bryłę. Dodatkowo bok lodówki 680 gł. vs C2 580 gł. → **100 mm uskoku** w płaszczyźnie boku, nieopisane żadną blendą.
Skutek: C4 (nadstawka 660 szer.) opiera się od wschodu na boku 2478, a od zachodu na niczym.

### B06 — GA1: półka głębsza niż korpus
Rozpiska: `GA1 — bok 245×998` (korpus gł. **245**), `GA1 — półki 633×300`.
Arytmetyka: **300 > 245 − 3 (plecy) = 242** → półka jest o **58 mm głębsza niż światło korpusu**.
Źródło: `_formatki.py` w. 76 — głębokość półki górnych zaszyta na sztywno `300`, bez związku z `G`.
Ta sama linia daje pozostałym górnym (gł. 400) półkę 300, czyli **97 mm zmarnowanej głębokości** w każdej szafce (patrz U01).

### B07 — DA2: szuflada pod piekarnikiem nie mieści się w korpusie
Dane: korpus H **720**; dno 18; trawers nośny 18 (`DA2 — trawers nośny piekarnika 564×560`); nisza piekarnika **600** (`_montaz.py` s.3: „górna płaszczyzna trawersu 600 mm od górnej krawędzi boku"); płyta indukcyjna 56 mm wpuszczana w blat 38 → schodzi **56 − 38 = 18 mm** pod wierzch korpusu.
Światło pod trawersem:
- bez uwzględnienia płyty: 720 − 18 (dno) − 18 (trawers) − 600 (nisza) = **84 mm**
- z płytą indukcyjną: 720 − 18 − 18 − 600 − 18 = **66 mm**

Szuflada z metalowym bokiem nom. 500 w najniższym wariancie ma bok ~84 mm i wymaga **≥100 mm światła** (bok + luz nad frontem + prowadnica pod dnem).
Skutek: **szuflada nie wejdzie**, a deklarowany `front szuflady dolnej 596×110` nie ma za sobą żadnej przestrzeni. Do tego kolizja płyty indukcyjnej z górą piekarnika (piekarnik 595 w niszy 600 → 5 mm luzu, a płyta zjada 18).
Dodatkowo `trawers nośny 564×560` to **pełna półka na całą głębokość** — piekarnik pod indukcją wymaga przewietrzenia; nazwa „trawers" i wymiar 560 są sprzeczne.

### B08 — GA3 okap: front zakrywa 40% korpusu
Rozpiska: `GA3 — bok 400×998`, `GA3 — front uchylny 596×400`.
Arytmetyka: **998 − 400 = 598 mm wysokości korpusu bez żadnego frontu**.
PLAN 5a przewiduje nad okapem „antresolę na rzeczy sezonowe" — czyli druga strefa istnieje w planie funkcjonalnym, ale nie ma ani frontu, ani półki dzielącej.
Sprzeczność dodatkowa: `_montaz.py` s.3 mówi „GA3: korpus **bez wieńca dolnego**", rozpiska daje `dno/wieniec 564×400 — 2 szt`.

### B09 — Listwa cokołowa: formatka 5000 mm i za mało metrów
Rozpiska: `Listwa cokołowa (czarny mat), łącznie ~5 mb | 5000×150 | 1 szt`.
(a) **Nie istnieje płyta 5000 mm.** Arkusz to 2800×2070 — cokół musi być rozpisany na odcinki ≤2800 (np. 3× ~1700 lub 2×2500).
(b) Długość: ciąg A **1950** + ciąg B (0→2000) **2000** + ciąg C (947+280+660) **1887** = **5837 mm** i to bez ramienia (1176 + bok 460).
Z ramieniem: **≈7,5 mb**. Zamówione **5 mb** → **niedobór ≥0,8 mb, realnie ~2,5 mb**.

### B10 — Kolor zabudowy lodówki niezgodny z zaakceptowaną paletą
Rozpiska w. 81–82: `C4 — fronty … ciemny orzech mat`, `Bok wykończeniowy zabudowy lodówki … ciemny orzech mat`.
PLAN pkt 10 (paleta zaakceptowana, korekta 2026-08-12): *„zabudowa lodówki (nadstawka C4 + bok przy ściance): **antracyt mat zbliżony do RAL 7016** — jedna ciemna bryła ze ścianką"*.
Skutek: 1,69 m² (bok) + 0,34 m² (fronty C4) = **2,03 m²** doliczone do orzecha zamiast do antracytu; **dekor antracyt nie występuje w tabeli m² w ogóle** → nie zostanie zamówiony.

### B11 — Plecy: deklaracja „nakładane" nie zgadza się z wymiarem
Nagłówek: „plecy HDF 3 mm **nakładane**". `_formatki.py` w. 56: `S−4 × H−4`.
Przykład DA1: korpus 850×720, plecy **846×716**.
- Plecy **nakładane** = gabaryt korpusu, czyli **850×720**.
- Plecy **wpuszczane** = światło + 2× głębokość rowka, czyli ~**820×690** przy rowku 10.

Wymiar S−4/H−4 nie jest ani jednym, ani drugim: zostawia **2 mm luzu na obwodzie**.
Skutek konstrukcyjny: `_montaz.py` s.2 opiera prostokątność korpusu na plecach („Plecy blokują kąt prosty na zawsze") — plecy z 2 mm luzu na każdej krawędzi **nie zablokują niczego**; korpus 1176 (RL1) i 900 (DC1) pozostają miękkie na skos.
Drugi skutek: nakładane plecy dokładają **+3 mm głębokości** każdemu korpusowi (560 → 563) — nieuwzględnione w zestawieniu blatów i w odstępach ergonomicznych PLAN pkt 4.

### B12 — Zawiasy: 36 szt to za mało (rachunek)

| Front | Wys. | szt/front | Razem |
|---|---|---|---|
| DA1 (240) | 716 | 2 | 2 |
| RL1 drzwi (300) | 716 | 2 | 2 |
| DB1 ×2 (397) | 716 | 2 | 4 |
| GA1 ×2 (332) | 996 | 3 | 6 |
| GA2 (176) | 996 | 3 | 3 |
| GA4 (496) | 996 | 3 | 3 |
| GC1 (466) | 996 | 3 | 3 |
| GC2 (473) | 996 | 3 | 3 |
| C2 dolny (276) | **1300** | **4** | 4 |
| C2 górny (276) | **1070** | **4** | 4 |
| C4 ×2 (327) | 524 | 2 | 4 |
| **Razem 110°** | | | **38** |
| DC1 (345) | 716 | 2 (155°) | 2 |

W dokumencie: **36 szt 110°** z adnotacją „w tym zapas ~10%" → **netto ~33**.
**Niedobór 5 szt.** Przyczyna: adnotacja („fronty dolne 2/front, górne ~996 mm 3/front") **nie uwzględnia frontów słupka 1300 i 1070** (dla H>1000 mm producenci wymagają 4 zawiasów) ani frontów C4.

### B13 — Zawieszki górnych: 10 szt na 6 szafek
Rozpiska: „Zawieszki regulowane górnych + listwa montażowa | **10 szt** + 3 mb | **GA1-3, GC1-2**".
Górnych jest **6**: GA1, GA2, GA3, GA4, GC1, GC2. Norma (standardy-meble): 2 wieszaki na szafkę do 60 cm → **6 × 2 = 12 szt**.
Adnotacja pomija **GA4** w ogóle. **Niedobór 2 szt.**
Listwa: 1950 (ciąg A) + 947 (ciąg C) = **2897 mm** → 3 mb bez żadnego zapasu na docinki i bez C4.

### B14 — Nóżki: 32 szt policzone regułą „8 × 4", norma mówi inaczej
standardy-meble: „4 na szafkę 60 cm, **6 na 80 cm+**".

| Moduł | Szer. | Nóżek wg normy |
|---|---|---|
| DA1 | 850 | 6 |
| DA2 | 600 | 4 |
| DB0 | 150 | 2 |
| DB1 | 800 | 6 |
| RL1 | 1176 | 6 |
| DC1 | 900 | 6 |
| C2 | 280 | 4 |
| zabudowa lodówki | 660 | 4 |
| **Razem** | | **38** |

W dokumencie **32**. **Niedobór 6** — a RL1 (1176 mm, ramię kotwione do posadzki) i DC1 (900) to dokładnie te korpusy, które przy 4 nóżkach będą pracować.

### B15 — Obrzeża poniżej standardu skilla
Rozpiska: **1,0 fronty / 0,4 korpusy i półki**.
`technologia-wykonania.md` §1 i `standardy-meble.md`: *„Krawędzie widoczne: zawsze ABS **2 mm**… Front i widoczne krawędzie półek: zawsze ABS **2 mm**; krawędzie ukryte 1 mm"*.
Przy frontach **bezuchwytowych** (decyzja PLAN) użytkownik chwyta front **za krawędź** — obrzeże 1,0 mm w tym miejscu odpryskuje. Obrzeże 0,4 na krawędzi przedniej korpusu pod blatem: standard wymaga 1 mm (wilgoć).

### B16 — Fronty 716/996 zakładają rozstrzygnięcie, którego w dokumencie nie ma
Pozycja okuciowa: „Listwa gola / frez uchwytowy ~5 mb | **decyzja technologiczna: profil alu vs frez CNC w płycie**".
Fronty w rozpisce mają wymiar 716 (= korpus 720 − 4) i 996 (= korpus 998 − 2) — czyli wymiar **frontu pełnego, pod uchwyt nakładany**.
Przy profilu gola listwa zabiera 50–60 mm pod blatem → **każdy front dolny musi być niższy o tę wartość**. Przy frezie uchwytowym trzeba zamówić frezowanie przy rozkroju.
Skutek: **nie da się zamówić ani jednego frontu**, dopóki decyzja nie zapadnie. To nie jest brak pomiaru — to nierozstrzygnięta decyzja projektowa w dokumencie oznaczonym jako „do wyceny".

### B17 — Fugi frontów górnych 1 mm
Korpus górny 998, front 996 → **2 mm na całą wysokość = 1 mm góra + 1 mm dół**.
Norma (standardy-meble, tabela tolerancji): fuga między frontami **2–3 mm**, front–blat 2 mm.
Przy regulacji zawiasu (±2 mm w pionie) i przy własnoręcznym montażu 1 mm oznacza **fronty ocierające o wieniec**.

### B18 — Zero fugi przy suficie
PLAN pkt 6: dół górnych **1480** + korpus **998** = **2478** = sufit **2478**.
Norma: „Zabudowa do sufitu — fuga **10–30 mm + listwa maskująca**". Sufit w remoncie ma odchyłkę 5–15 mm na 2 m.
Skutek: górne wchodzą na styk, bez tolerancji i bez blendy (K08). Przy montażu samodzielnym to gwarantowany problem na ostatniej szafce.

### B19 — PLAN pkt 6: „odstęp 600 od blatu" nie zgadza się z liczbami
1480 (dół górnych) − 910 (blat) = **570 mm**, nie 600.
570 mieści się w normie (500–600) i spełnia okap ≥550 nad indukcją ✓ — **błędny jest opis, nie wymiar**. Ale dokument, w którym kontrola krzyżowa nie wychodzi, przestaje być kontrolą.

### B20 — Blaty: narożniki policzone dwukrotnie, brak luzu montażowego
Rozpiska: Blat A **1950**×635, Blat B **2389**×635, Blat C1 **947**×635, ramię 545×500. Łączenia: 3.
(a) Blat A ma 1950 = **cała długość ciągu A liczona od ściany B**, a blat B ma 2389 = **cała ściana B**. W narożniku A/B oba zajmują ten sam kwadrat **635×635**. To samo w narożniku B/C1. Nadmiar: **2 × 0,40 m² ≈ 0,81 m²** (~1,27 mb blatu). Przy łączeniu narożnym jeden z blatów musi być krótszy o szerokość drugiego: blat A → 1950 − 635 = **1315**, blat C1 → 947 − 635 = **312**.
(b) Blat B **2389** = ściana B **2389** — **zero luzu**. Norma: fuga 5–15 mm na silikon/listwę, dylatacja laminatu 3–5 mm. Blat równy ścianie **nie wejdzie**.
(c) Szerokość 635 vs PLAN pkt 5 („blat 600, ramię 650") — sprzeczność między dokumentami. Przy 635 na korpusie 560 + froncie 19: nawis **635 − 579 = 56 mm** (norma nawisu 20–40, głębokość blatu z wystawką 600–630 — 635 jest o 5 mm poza). Dodatkowo 35 mm więcej wystawki po stronie ciągu B zjada przejście robocze policzone w PLAN pkt 4 jako ~85 cm.

### B21 — C2: fronty nie sumują się do korpusu i nie zgadzają się z PLAN
Rozpiska: `276×1300` + `276×1070` = **2370**; korpus **2378** → 8 mm na trzy fugi (2+4+2).
PLAN v3.12a / `_formatki.py` opis: „front dzielony **1300+1074**" (1300+1074 = 2374 = H−4 ✓).
Rozpiska ma **1070** — rozjazd 4 mm względem własnego opisu, i fuga środkowa 4 mm zamiast normowych 2–3.

### B22 — DC1: dwa różne korpusy w dwóch dokumentach
PLAN pkt 5: `korpus ~945×820×546`. `_formatki.py` MODULES: `("DC1 narożna ślepa", 900, 720, 560)`.
Rozjazd: **45 mm szerokości i 14 mm głębokości**. PLAN sam sobie zaprzecza: 945 (korpus) + 47 (blenda) = **992 ≠ 947**, natomiast 900 + 47 = 947 ✓ — czyli PLAN pkt 5 zawiera nieaktualne 945.

### B23 — Dokument obiecuje wiercenie, którego dostawca nie robi
`FORMATKI-ROBOCZE.md` pkt 4.1: *„zamówienie rozkroju z oklejaniem i **CNC (puszki 35 pod zawiasy!)** w KornerGo"*.
`dostawcy.md` w. 86: *„Korner (płyty, korner.pl) tnie i okleja, ale wg inwestora **NIE wierci otworów montażowych**"*.
`_montaz_prosty.py` w. 25 mówi to samo i daje dwie drogi (usługowe wiercenie MEBsystem/Soma/Komandor ~150–400 zł, albo szablony ~200 zł).
Skutek: **główny dokument zakupowy planuje operację, która nie zostanie wykonana** — inwestor odbierze formatki bez ani jednego otworu, nie mając tego w budżecie ani w harmonogramie. To jedyne miejsce, gdzie ta sprzeczność jest ukryta.

### B24 — Instrukcja montażu opisuje moduły i głębokości, których projekt nie ma

| Miejsce | Zapis w `_montaz.py` | Stan projektu |
|---|---|---|
| s.3, w. 165 | „**DA1 (3 szuflady)**: prowadnice… 30/266/502" | DA1 od v3.10 to **narożna ślepa z drzwiami** — bez szuflad |
| s.3, nagłówek | „górne: boki 998×**320**… x = 50/160/**270** (gł. 320)" | górne mają **400**, a GA1 **245** → wymiar 270 wypada **poza formatkę GA1** |
| s.2, nagłówek | rozstawy dna dla gł. **560** i **460** (RL1) | **brak rozstawu dla DA1 gł. 405** — trzeci otwór na 510 wypada 105 mm poza płytę |
| s.5, w. 226 | „Ramię: **RL1+RL2**" | RL2 nie istnieje od v3.8 |
| s.5 vs FORMATKI 4.7 | „listwa montażowa (**góra** szafek = sufit 2478)" | FORMATKI: „listwa montażowa na **1480** (dół szafek)" — sprzeczne |
| `_montaz_prosty.py` w. 41 | „transport (słupek **2,38 m**)" | najdłuższa formatka to **bok lodówki 2478** |

**Błędy: 24.**

---

## 4. WYMIARY MAKSYMALNE — CIĘCIE I TRANSPORT

Arkusz referencyjny: **2800 × 2070** (płyta i HDF).

| Formatka | Wymiar | Mieści się w arkuszu? | Uwaga |
|---|---|---|---|
| Listwa cokołowa | **5000**×150 | **NIE** | B09 — pozycja niewykonalna |
| Bok wykończeniowy lodówki | **2478**×680 | tak, tylko wzdłuż 2800 | 2478 > 2070 → wymusza orientację; odpad 322 mm |
| Bok C2 słupek | **2378**×580 | tak, tylko wzdłuż 2800 | 2 szt z jednego pasa 2800 niemożliwe (2×580=1160 wszerz — OK, ale kierunek słoja narzucony) |
| Plecy C2 HDF | **2374**×276 | tak, wzdłuż 2800 | — |
| Blat B | **2389**×635 | n/d (blat handlowy 4100) | B20b — brak luzu do ściany |
| Panel ryflowany | 1176×910 | n/d — **dostawca zewnętrzny** | doliczony do m² orzecha (1,07 m²) mimo że Korner go nie dostarcza → zawyżenie zamówienia |

**Transport:** formatki 2378 i 2478 wykluczają odbiór osobisty samochodem osobowym (`dostawcy.md`: „formatki pełnowymiarowe zwykle odpadają"). **Transport Korner jest wymagany, nie opcjonalny** — dokument to wskazuje, ale z zaniżonym wymiarem 2,38 m zamiast 2,478 m.

**Cięcie:** boki 2378/2478 nie mają zapasu na docięcie po pomiarze sufitu. Przy sufitach 2478 [P] mierzonych **przed posadzką docelową** (PLAN pkt 11.5 sam to zastrzega) każdy z tych elementów pojedzie na wymiar, który się zmieni.

---

## 5. UGIĘCIE PÓŁEK

Norma: **max rozpiętość 800 mm dla płyty 18 mm** (standardy-meble.md).

| Półka | Rozpiętość | Ocena |
|---|---|---|
| GA1 633×300 | 633 | ✓ rozpiętość OK — ale **głębokość błędna** (B06) |
| GA2 143×300 | 143 | ✓ |
| GA4 463×300 | 463 | ✓ |
| GC1 433 / GC2 440 | 433 / 440 | ✓ |
| C2 243×560 | 243 | ✓ — ale **2 półki na 2378 wysokości**, brak stałej (K13) |

**Żadna półka istniejąca w rozpisce nie jest zagrożona ugięciem.** Problem jest odwrotny:

| Półka **brakująca** | Rozpiętość, jaką musiałaby mieć | Ocena |
|---|---|---|
| DA1 (PLAN: „drzwi + 1 półka") | **814** | **> 800 — przekroczona norma**. Do tego garnki (PLAN 5a: „garnki i duże naczynia, 248 l"), czyli obciążenie skrajne. Wymaga: podpory środkowej / listwy usztywniającej pod przednią krawędzią / płyty 22 |
| DC1 (2 szuflady + strefa ślepa) | **864** | **> 800** — jw. |
| C4 nadstawka | 624 | ✓ mieści się |
| GA3 antresola | 564 | ✓ mieści się |

**Wniosek:** ryzyko ugięcia dotyczy wyłącznie półek, których w rozpisce nie ma — i obie przekraczają normę. Trzeba je zaprojektować od razu z podparciem, nie dopisać jako „półka 18 mm".

---

## 6. MONTAŻ KORPUSÓW — czy instrukcja podaje konkret

| Pytanie | Odpowiedź dokumentu | Ocena |
|---|---|---|
| Rodzaj złącza | konfirmat 7×50 | ✓ podane, z przekrojem i instruktażem |
| Oś otworu | 9 mm od krawędzi (połowa grubości) | ✓ |
| Ilość na złącze dna | **3** (50 / 280 / 510 od przodu, gł. 560) | ✓ dla 560 i 460; **✗ brak dla 405 (DA1)** i dla górnych 400/245 (B24) |
| Ilość na złącze trawersu | **1 na stronę** (50 od przodu, 50 od tyłu) | ⚠ trawers 100 mm mocowany **jednym** konfirmatem na stronę — obraca się; standard to 2 (albo trawers + kołek) |
| Kołki | „kołki 8×35 — 1 opak." na liście | ✗ **nigdzie nie użyte** w instrukcji — pozycja bez zastosowania |
| Mimośrody | — | ✗ **nie występują**. Konstrukcja wyłącznie na konfirmatach → brak jakiejkolwiek korekty po skręceniu i widoczne łby (K23) |
| Łączenie korpus–korpus | „2 wkręty 4×30 przez boki, pod zawiasami" | ✗ niezgodne z normą (EuroScrew M4×35 + tulejka, 2/złącze — K22) |
| Kontrola prostokątności | „zmierz obie przekątne ±1 mm" + plecy | ⚠ metoda dobra, ale plecy z 2 mm luzem jej nie utrwalą (B11) |

---

## 7. OKUCIA

| Pozycja | Wymóg (norma / projekt) | W dokumencie | Ocena |
|---|---|---|---|
| Zawiasy 110° | **38 szt** (rachunek B12: dolne 2/front, górne 996 → 3, C2 1300 i 1070 → 4, C4 → 2) | 36 szt „w tym zapas ~10%" (netto ~33) | **BŁĄD — niedobór 5 szt**; adnotacja pomija fronty słupka i C4 |
| Zawiasy 155° | 2 szt do DC1 (narożna ślepa) | 2 szt | ✓ — ale front DC1 ma zły wymiar (B02) |
| Zawiasy — front 176×996 (GA2) | 3 szt na front o proporcji 1:5,7 | ujęte w puli | ⚠ RYZYKO paczenia; front tak wąski i wysoki wymaga kontroli po sezonie |
| Prowadnice RL1 | nom. **400** ≤ gł. korpusu 460 | 3 kpl nom. 400 | ✓ nominał OK — **ale brak 3 frontów i 3 den** (K02/K03) |
| Prowadnice DA2 | nom. **500** ≤ gł. 560 | 1 kpl nom. 500 | **BŁĄD** — nominał OK, ale **światło pionowe 66–84 mm < wymaganych ~100** (B07) |
| Prowadnice DC1 | nom. **450** ≤ gł. 546/560 | 2 kpl nom. 450 | ✓ nominał OK; brak den (K03) |
| Obciążenie prowadnic | brak deklaracji (standard 40 kg) | nie podano | **BRAK** — szuflada RL1 na garnki i szuflada DA2 na blachy wymagają deklaracji |
| Dna szuflad | 6 szt (płyta/HDF wg producenta) | — | **BRAK (K03)** — dokument sam pisze, że dno się dokupuje |
| Wkład na sztućce 300 | do szuflady o świetle 300−36 = **264** | 1 szt „300" | ✓ (wkład 300 = do korpusu 300) |
| Kosz segregacji | ≥450 wg kontroli K9, do DB1 800 | — | **BRAK (K21)** — funkcja obowiązkowa wg własnej kontroli projektu |
| Cargo 150 (DB0) | korpus 150 → światło 114 | 1 kpl | ✓ nominał — **brak frontu (K04)** |
| Cargo spiżarniane C2 | korpus **280** → światło **244** | 1 kpl „do słupka 280 [DO WERYFIKACJI]" | **RYZYKO/BŁĄD** — cargo wysokie produkuje się na korpus 300/400/500/600; **244 mm światła nie ma odpowiednika katalogowego**. Realna droga: półki (ale wtedy 2 półki na 2378 to za mało — K13) |
| Podnośnik okapu | front 596×400 ≈ 3,4 kg | 1 kpl (HK-S lub wg okapu) | ✓ dobór właściwy dla tej masy — ale front zakrywa 40% korpusu (B08) |
| Zawieszki górnych | **12 szt** (6 szafek × 2) | 10 szt, adnotacja „GA1-3, GC1-2" | **BŁĄD — niedobór 2**, pominięta GA4 |
| Listwa montażowa | 1950 + 947 = **2897 mm** + zapas | 3 mb | ⚠ zero zapasu; brak mocowania C4 |
| Kotwy do ściany | „kotwy chemiczne w betonie"; **pustak/gazobeton → chemia, GK → tylko w profile** | brak pozycji, brak pomiaru materiału ściany | **BRAK (K24)** — patrz R05 |
| Nóżki | **38 szt** (wg reguły 4/60 cm, 6/80 cm+) | 32 szt („8 szafek × 4") | **BŁĄD — niedobór 6** |
| Klipsy cokołu | ~5,8–7,5 mb cokołu | 16 szt | ⚠ przy 7,5 mb i rozstawie 500 mm potrzeba ~15 na samą linię przednią + narożniki |
| Złącza korpus–korpus | EuroScrew M4×35 + tulejka, 2/złącze (~8 złączy = 16 kpl) | — (tylko „wkręty 4×30") | **BRAK (K22)** |
| Kątowniki ramienia | 8 szt | 8 szt | ✓ ilość — **brak typu kołka do posadzki** i patrz R01 |
| Śruby łącznikowe blatu | 3 kpl (3 łączenia) | 3 kpl | ✓ |
| Zasilacz LED | ≥35 W przy 3 mb / 9,6 W/m | „1 szt, 24 V" | **BRAK mocy (K25)** |
| Zaślepki konfirmatów | ~200 szt | — | **BRAK (K23)** |
| Silikorner + silikon | 1+1 | 1+1 | ✓ |

---

## 8. RYZYKA MONTAŻU SAMODZIELNEGO

| # | Ryzyko | Dlaczego realne w tym projekcie | Mitygacja |
|---|---|---|---|
| R01 | **Kotwienie ramienia przez pływającą podłogę** | RL1 kotwione „8 kątownikami do posadzki" (FORMATKI poz. 22, plan montażu 4.6), a posadzka docelowa kładziona **przed** montażem (PLAN pkt 11.5, 8.5). W mieszkaniu jest **SPC Solid Floor 5 mm i4F Drop-Lock** (`dostawcy.md`) — podłoga pływająca. Przewiercenie jej kątownikiem **blokuje dylatację całej płaszczyzny** → falowanie / rozejście zamków | Kątowniki mocować **do ściany A i do korpusu DA2**, nie do posadzki; jeśli konieczne kotwienie w podłożu — punkt kotwiący **pod podłogą**, wykonany przed jej ułożeniem, z wycięciem w panelu i luzem 5 mm dookoła |
| R02 | **Wiercenie nie ma wykonawcy** | B23 — dokument zakupowy planuje CNC w Kornerze, którego Korner nie robi. Inwestor jest początkujący (`_montaz.py` jest pisany dla początkującego) | Przed zamówieniem rozstrzygnąć: droga A (MEBsystem Gliwice / Soma Chorzów / Komandor Katowice, ~150–400 zł) albo droga B (przyrząd do puszek z ogranicznikiem, ~200 zł). **Decyzja zmienia zawartość zamówienia i budżet** |
| R03 | **Puszki 35 we frontach robione samodzielnie** | 38 puszek × głębokość 12,5 mm w froncie 18/19 mm. Margines błędu **5,5 mm**. Przewiercenie = front na wyrzut, a fronty są w unikalnych dekorach (orzech, kaszmir) | Wymusić drogę A dla samych **frontów** (najdroższe formatki), nawet jeśli korpusy idą drogą B. Standardy: „Fronty: +1 sztuka rezerwa jeśli dekor unikalny" — rezerwy w rozpisce nie ma |
| R04 | **Elementy 2378 i 2478 stawiane w pojedynkę** | Bok słupka 2378×580 (~16 kg) i bok lodówki 2478×680 (~22 kg) — przy suficie 2478 wchodzą **na styk, bez tolerancji** (B18). Podniesienie do pionu w pomieszczeniu o wysokości równej długości elementu jest geometrycznie niemożliwe | Skrócić korpus C2 do **2328** (B04) i przewidzieć **fugę sufitową 10–30 mm z blendą** (K08). To jednocześnie naprawia niemożliwość montażu i błąd wysokości |
| R05 | **Górne wieszane bez rozpoznania ściany** | 6 szafek × ~40–48 kg (obliczenie GA4: 1,94 m² płyty × 11,5 kg/m² ≈ 23 kg własnej + 15–25 kg zawartości) na 2 zawieszki = **20–24 kg na punkt**. Zawieszki to wytrzymają; **kołek w gazobetonie nie** (~15–25 kg na wyrywanie). PLAN pkt 11 nie zawiera pozycji „materiał ściany" (K24) | Dopisać do listy pomiarów jako pozycję **nr 12**; do czasu rozpoznania nie zamawiać kotew. Beton/cegła — kotwa standard; gazobeton/pustak — **kotwa chemiczna**; GK — ruszt albo rezygnacja z górnych |
| R06 | **Korpusy bez korekty po skręceniu** | Wyłącznie konfirmaty (brak mimośrodów), plecy z 2 mm luzem (B11), narożne ślepe DA1 850 i DC1 900 skręcane bez blend prowadzących. Po skręceniu **nie ma jak nic poprawić** — konfirmat drugi raz w tym samym otworze nie trzyma | Plecy w wymiarze gabarytowym (nakładane pełne) — one ustawiają kąt; przekątne mierzone **przed** dokręceniem, nie po |
| R07 | **Fronty zamówione przed decyzją gola/frez** | B16 — decyzja „profil alu vs frez CNC" zmienia wysokość każdego frontu dolnego o 50–60 mm | Nie zamawiać frontów w tej samej turze co korpusy. Korpusy mogą jechać wcześniej — one na tę decyzję nie reagują |
| R08 | **Wycięcia w blacie wyrzynarką** | Zlew „wg szablonu" i indukcja 560×490 w laminacie 38. Blat B 2389 jest **jedyną sztuką** — błąd = ponowny zakup 2,4 mb blatu | Zlecić wycięcia przy rozkroju (CNC) razem z blatem; wariant „wyrzynarka + silikon" trzymać jako awaryjny, nie domyślny |
| R09 | **Zabudowa lodówki bez modułu** | K01/B05 — inwestor odkryje brak drugiego boku dopiero przy stawianiu C4, po dostawie | Domknąć C3 jako pełny moduł przed zamówieniem |
| R10 | **Ciąg C nie domknie się na wymiar** | PLAN pkt 9 sam odnotowuje: 947+280+660 = **1887 vs 1885 [P]** → 2 mm nadmiaru, a blenda 47 (K07) nie istnieje w rozpisce | Blenda DC1 z zapasem szerokości (60–70), docinana na miejscu — zgodnie z technologia §2 („blendy zamawiaj z zapasem") |
| R11 | **Kolejność: fronty przed regulacją poziomu** | Plan montażu (4.10) słusznie daje fronty na końcu ✓, ale krok 4.7 wiesza górne **przed** blatami (4.8) — przy blacie 635 (B20c) front górny może nie zejść się z linią blatu | Blaty na sucho **przed** ostatecznym zawieszeniem górnych |

**Ryzyka: 11.**

---

## 9. ULEPSZENIA

| # | Ulepszenie | Uzasadnienie |
|---|---|---|
| U01 | Półki górnych **370** zamiast zaszytego 300 | Przy korpusie 400 i plecach nakładanych światło to 400 mm. Półka 300 marnuje **97 mm × 5 szafek**. Rozpiętości (433–633) i tak są poniżej normy 800 → grubość 18 wystarcza |
| U02 | Wymiar półek liczony z `G`, nie stałą | `_formatki.py` w. 76: `add(..., S-2*P-1, 300, 2, ...)` — zamiana `300` na `G-20` (jak w gałęzi `slupek`, w. 74) usuwa B06 i U01 jedną poprawką |
| U03 | Zestawienie m² rozbite na **arkusze**, nie tylko m² | 19,9 m² kremowego = 4 arkusze 2800×2070 (5,8 m²/arkusz), ale rozkrój boków 2378/2478 wymusza orientację → realnie 5. Sam m² tego nie pokaże |
| U04 | Panel ryflowany wyjąć z bilansu orzecha | 1,07 m² doliczone do dekoru, którego dostawca zewnętrzny nie zrealizuje z płyty Kornera (sekcja 4) |
| U05 | Marża 15% → rozbić: 10% na płytę korpusową, **+1 szt na front w unikalnym dekorze** | standardy-meble: „Fronty: +1 sztuka rezerwa jeśli dekor unikalny". Ryzyko R03 (samodzielne puszki) czyni tę rezerwę obowiązkową, nie opcjonalną |
| U06 | Trawersy górne na **2 konfirmaty/stronę** albo trawers + kołek | Jeden konfirmat na stronę pozwala trawersowi się obrócić przy dokręcaniu blatu |
| U07 | DA1/DC1: podpora środkowa półki zamiast płyty 22 | Tańsze i mieści się w technologii płytowej: listwa 60×18 pod przednią krawędzią, mocowana konfirmatem w bok — sprowadza rozpiętość 814/864 do 2×~410 |

---

## 10. PODSUMOWANIE LICZBOWE

| Kategoria | Liczba |
|---|---|
| **BŁĄD** | **24** |
| **BRAK** | **27** |
| **RYZYKO** | **11** |
| **ULEPSZENIE** | **7** |

### Trzy pozycje, które blokują zamówienie

1. **B03 / K02 — rozpiska jest sprzed v3.12:** RL1 nie ma frontów szuflad, DA1 i DC1 mają fronty 446 zamiast 240 i 345. Wszystkie trzy naprawy opisane w PLAN jako kluczowe nie zeszły do generatora — zamówienie w tej postaci odtwarza dokładnie te błędy, które projekt już raz wykrył i naprawił.
2. **B04 / B05 / K01 — pion ściany C nie zamyka się:** słupek 2378 na nóżkach 150 daje 2528 przy suficie 2478, bok lodówki ma 2478 od podłogi, a zabudowa lodówki jako moduł nie istnieje — więc nadstawka C4 nie ma podparcia od zachodu.
3. **B23 / R02 — dokument planuje wiercenie, którego dostawca nie wykonuje:** pkt 4.1 obiecuje „CNC (puszki 35) w KornerGo", a Korner nie wierci. Inwestor odbierze ~77 formatek bez ani jednego otworu, mając w instrukcji szczegółowej wymiary wiercenia liczone dla głębokości 320, których projekt nie ma.

### Co trzeba zrobić przed jakąkolwiek wyceną

Poprawki są w **jednym pliku** — `_formatki.py`. Kolejność:
1. `MODULES`: doprowadzić DA1/DC1/RL1 do stanu v3.12 (front DA1 240, front DC1 345, RL1 = drzwi 300 + 3 szuflady 300 + blenda 576), C2 → 2328, DC1 → wymiar zgodny z jednym dokumentem.
2. Gałęzie generatora: półki z `G` (U02), front cargo dla `typ=="cargo"`, drugi front + półka dla `typ=="okap"`, dna szuflad.
3. `PANELE`: cokół rozbić na odcinki ≤2800 i przeliczyć na ≥7,5 mb; blenda dystansowa przenieść z okuć do formatek; dodać boki wykończeniowe GA4 i RL1, blendy DC1/sufitową, moduł C3.
4. Kolory: C4 + bok lodówki → antracyt (nowa pozycja w bilansie m²).
5. Sekcja okuć: zawiasy 38+2, zawieszki 12, nóżki 38, kosz segregacji, złącza korpusowe, zaślepki, moc zasilacza, kotwy po rozpoznaniu ściany.
6. Nagłówek: dopisać grubość frontu 19, wyprostować opis pleców (nakładane = gabaryt), **usunąć obietnicę CNC w KornerGo**.
7. Dopiero potem pomiary z PLAN pkt 11 (+ pozycja 12: materiał ściany pod górne).

*Wymiary, których w dokumentach nie ma i których nie wolno założyć: głębokość niszy piekarnika wg konkretnej karty AGD, masa i wymiar frontu okapu wg konkretnego okapu, nominały prowadnic wg karty producenta, wymiar dna szuflady wg systemu — wszystkie oznaczone w źródle jako `[?]` / `[do potwierdzenia]` i tak pozostają: **[BRAK DANYCH]**.*
