# 00 — WERDYKT KOMISJI AUDYTOWEJ · `kuchnia-wyspa` v3.12a

**Data:** 2026-08-13 · **Przewodniczący komisji** · scalenie sześciu niezależnych audytów (A1 metrolog, A2 ergonomista, A3 AGD+instalacje, A4 technolog, A5 kompletność/zakupy, A6 adwokat diabła).
**Kontekst:** inwestor Dominik, wzrost 182, montaż samodzielny (pierwszy raz), zakup na firmę, materiał Korner (**Korner nie wierci otworów**), 15 modułów.
**Fakt bazowy:** pomiary łańcuchowe z PLAN pkt 11 **nie zostały wykonane** — dokument sam to deklaruje.
**Zasada:** żadnego wymiaru nie dopisano. Brak danych ⇒ `[BRAK DANYCH]`. Każda pozycja ma agenta-źródło i dowód.

---

## 1. TL;DR — 10 zdań

1. **Nie zamawiaj.** Nie z powodu braku pomiarów (to jest uczciwie zadeklarowane), tylko dlatego, że dokument, z którego się zamawia (`FORMATKI-ROBOCZE.md` / `_formatki.py`), opisuje wersję **v3.5** i nie zawiera ani jednej z trzech napraw, które PLAN opisuje jako kluczowe (DA1 v3.10, DC1 v3.11, RL1 v3.12) — zgłosili A1, A2, A4, A5, A6 (5/6).
2. **`_kontrola.py` PASS 9/9 nie dowodzi niczego o projekcie** — dowodzi wewnętrznej spójności dwuwymiarowego modelu w tym jednym pliku, który różni się od PLAN.md i `_formatki.py` w kilkunastu wymiarach (6/6 agentów doszło do tego niezależnie).
3. **Dwa elementy pionowe są fizycznie niemontowalne:** słupek C2 (2378 + nóżki 150 = 2528 > sufit 2478) i bok wykończeniowy lodówki 2478×680 (przekątna **2569,6 mm > 2478** — nie da się go postawić w tym pomieszczeniu).
4. **Ciąg C nie domyka się** — blenda 47 jest policzona przy korpusie, który już jej nie potrzebuje, a blenda dystansowa lodówki 70×2478 (wymuszona geometrią i już zamówiona) **nie ma miejsca w łańcuchu**: deficyt 2–72 mm zależnie od wariantu.
5. **DA2 nie mieści płyty, piekarnika i szuflady naraz** — prześwit wewnętrzny 704 mm, zajęte 626–636 mm, zostaje 68–86 mm na szufladę o froncie 110 mm (5/6 agentów, rozbieżne rachunki, wszystkie na minus).
6. **Cztery urządzenia nie mają modelu** (piekarnik, okap, zmywarka, zlew), a ich nisze, wycięcia i fronty są już w liście do cięcia — dodatkowo GA3 ma pełne dno (okap nie ma czym zasysać) i brak wylotu recyrkulacji.
7. **Dokument zamawia u Kornera usługę, której Korner nie świadczy** (CNC, puszki 35) — inwestor odbierze ~77 formatek bez ani jednego otworu, bez tego w budżecie i harmonogramie.
8. **Nierozstrzygnięta decyzja gola vs frez blokuje zamówienie wszystkich frontów dolnych** — profil gola zabiera 40–60 mm wysokości każdego frontu, a fronty są już policzone na 716.
9. **Pilaster ma w jednym dokumencie trzy statusy** (`[P]`, `[~]`, `[?]`), a wisi na nim cała ściana A — jeśli uskok 15,5 idzie całą ścianą, przeprojektowaniu podlega ciąg A, wszystkie górne A i blat A.
10. **Największa zbieżność audytu (6/6): głębokość blatu** — 600 (PLAN) vs 635 (rozpiska) vs „ramię 650" (PLAN) vs „65" (prompt renderu); od tej jednej liczby zależą wystawka blatu, strefa robocza przy zlewie, cofnięcie górnych i pozycja wycięcia płyty.

---

## 2. WERDYKT KOŃCOWY

Projekt **nie nadaje się do zamówienia — ani dziś, ani po samym pomiarze**. Pomiar jest warunkiem koniecznym, ale niewystarczającym: nawet gdyby wszystkie jedenaście pomiarów z pkt 11 wykonano jutro i wszystkie potwierdziłyby założenia, do rozkroju poszedłby dokument opisujący wersję v3.5, z trzema szafkami narożnymi o wymiarach sprzed trzech kolejnych napraw, dwoma elementami pionowymi, których nie da się fizycznie postawić w pomieszczeniu, i modułem DA2, w którym nie mieści się to, co zaprojektowano. Rdzeń problemu jest jeden i nazwał go już `protokol-weryfikacji.md` §1: **wymiary żyją równolegle w czterech plikach** (`PLAN.md`, `_kontrola.py`, `_formatki.py`, `_schemat.py`) i rozjechały się w kilkunastu miejscach, a jedyne narzędzie kontrolne czyta piąty, własny model — dlatego wystawia PASS dokumentowi, którego nigdy nie widziało. Kolejność ratunkowa jest sztywna: **(1)** zejść do jednego źródła prawdy — `_formatki.py` i `_schemat.py` mają czytać model z `_kontrola.py`; **(2)** rozstrzygnąć decyzje projektowe z koszyka B (gola/frez, głębokość blatu, wiercenie, zawartość DA2, modele AGD); **(3)** wykonać pomiary z koszyka A **po posadzce docelowej**; **(4)** przeprojektować dziewięć modułów wymienionych w §6; **(5)** dopiero wtedy przeliczyć rozpiskę i zamawiać. Koszt wykonania tego teraz to kilka godzin pracy nad plikami i 0 zł materiału; koszt pominięcia to drugi rozkrój, drugi transport i ok. 2,8 m² płyty korpusowej plus 1,7 m² najdroższego dekoru do kosza — a przy montażu samodzielnym także fronty z fabrycznymi nawiertami, których nie da się poprawić.

---

## 3. TABELA POZYCJI — P0 / P1 / P2

Koszyki: **A** = do rozstrzygnięcia pomiarem · **B** = decyzja projektowa Dominika · **C** = poprawka w dokumencie od ręki.
Kolumna „zgłosili" = liczba niezależnych agentów, którzy trafili w to samo. Wysoka zbieżność = wysoki priorytet.

### P0 — blokuje zamówienie, ryzyko wyrzucenia materiału

| ID | problem | zgłosili | dowód | koszyk | działanie |
|---|---|---|---|---|---|
| **P0-01** | Rozpiska formatek to **v3.5**: generator wystawia każdej szafce narożnej sztywny front **446×716 + blenda ślepa 430×716**, niezależnie od faktycznego frontu (DA1 240 / RL1 600 dzielony / DC1 345) | A1, A2, A4, A5, A6 — **5/6** | `_formatki.py` l.69–71 `if typ == "narozna"`; DA1: 446+430 = **876 > 850** korpusu — fizycznie niemożliwe | C | przepisać `MODULES` i gałęzie generatora na v3.12a; do tego czasu **żadna liczba m²/mb w BOM nie jest wiążąca** |
| **P0-02** | RL1: **brak 3 frontów szuflad, 6 den szuflad i pionowej przegrody** — regresja naprawy z v3.12, przy jednoczesnym zamówieniu 3 kpl prowadnic i wkładu na sztućce | A1, A2, A4, A5, A6 — **5/6** | 1176 − (446+430) = **300 mm lica bez żadnej formatki** = dokładnie pas szuflad; FORMATKI §3 zamawia prowadnice nom. 400 ×3 | C | dopisać typ modułu w `_formatki.py`, przegenerować listę |
| **P0-03** | **Słupek C2 nie mieści się w pomieszczeniu:** korpus 2378 + nóżki 150 = **2528 > sufit 2478** | A1, A4, A5, A6 — **4/6** | FORMATKI nagłówek „słupek 2378"; PLAN pkt 6 „do sufitu 2478"; 2478 − 2378 = 100 → wysokość policzona dla cokołu 100, a projekt jeździ na 150 | C + A | korpus **2328** przy nóżkach 150, ostateczna liczba po pomiarze sufitu po posadzce |
| **P0-04** | **Bok wykończeniowy lodówki 2478×680 nie da się postawić:** przekątna √(2478²+680²) = **2569,6 mm > 2478** — element zahacza o sufit w każdej pozycji pośredniej | A4 (częściowo, R04), A6 — **2/6** | `_formatki.py PANELE`; arytmetyka sprawdzona przez komisję | C | podzielić na dwa segmenty z łączeniem poziomym na **1950** (dokument sam ma tam podział pod C4) |
| **P0-05** | Wszystkie formatki pionowe policzone z sufitu **2478 mierzonego przed posadzką docelową**; fuga sufitowa = **0**, blendy przysufitowej nie ma w rozpisce | A1, A2, A4, A6 — **4/6** | 1480 + 998 = 2478 dokładnie; PLAN ostrzega przed tym **5 razy** (pkt 1, 2, 8.5, 9, 11.5); `technologia-wykonania.md` §2 wymaga fugi 10–30 + listwa | A | pomiar 11.5 **po posadzce**, potem cięcie; wprowadzić fugę ~15 mm i blendę docinaną na miejscu |
| **P0-06** | **DA2: płyta + piekarnik + szuflada nie mieszczą się w pionie** | A1, A2, A3, A4, A6 — **5/6** | prześwit wewnętrzny **704** (872 − 150 − 18); zajęte: nisza 590–600 + trawers 18 + korpus płyty pod blatem 18 = **626–636** → zostaje **68–86 mm** na szufladę o froncie **110** | B + A | decyzja: (a) piekarnik + płyta bez szuflady, (b) piekarnik do słupka C2 (wariant B z pkt 9a, odrzucony); rozstrzygnąć **kartą kupionego piekarnika** |
| **P0-07** | **Ciąg C nie domyka się** — blenda 47 policzona do korpusu, który jej nie potrzebuje, a blenda dystansowa lodówki 70×2478 nie ma miejsca w łańcuchu | A1, A4, A6 — **4/6** (A5 twierdzi przeciwnie, patrz §4 S-1) | 945+47+280+660 = **1932**; 900+47+280+660 = **1887**; 947+280+660+**70** = **1957** — wszystko vs 1885 `[P]`; `_kontrola.py` nie zna blendy dystansowej | A + C | pomiar łańcuchowy C (11.3) i przeliczenie: `DC1 + C2 + 660 + 70 = zmierzona odległość` |
| **P0-08** | **DC1 — cztery różne wymiary w czterech plikach** | A1, A4, A5, A6 — **4/6** | PLAN §5: 945×546, front 345 · `_kontrola.py`: 945×546, front 345 · `_formatki.py` l.20: **900×560, „front 450"** · `_schemat.py` l.280: „front 45" · FORMATKI: bok 560×720, front **446** | C | jedna krotka w `MODULES`; front 446 do otworu 345 to **101 mm za dużo** — drzwi się nie otworzą |
| **P0-09** | **Korner NIE wierci**, a PLAN pkt 12 i FORMATKI §4.1 zamawiają u niego CNC (puszki 35 pod zawiasy, nawierty) | A4, A6 — **2/6** | `references/dostawcy.md` w. 86; `_montaz_prosty.py` mówi to wprost i daje dwie drogi (usługa ~150–400 zł albo przyrząd ~200 zł) | B + C | rozstrzygnąć drogę **przed** zamówieniem — zmienia zawartość zamówienia, budżet i harmonogram; usunąć obietnicę CNC z obu dokumentów |
| **P0-10** | **Decyzja „gola vs frez" nierozstrzygnięta**, a wszystkie fronty dolne policzone na **716** | A4, A6 — **2/6** | FORMATKI §3: „Listwa gola / frez uchwytowy — decyzja technologiczna: profil alu vs frez CNC"; profil gola zabiera **40–60 mm** wysokości każdego frontu | B | rozstrzygnąć przed zamówieniem frontów; korpusy mogą jechać wcześniej — na tę decyzję nie reagują |
| **P0-11** | **Cztery urządzenia bez modelu** (piekarnik, okap, zmywarka, zlew), a nisze, wycięcia i fronty już zaprojektowane | A2, A3, A4, A5, A6 — **5/6** | PLAN pkt 7; FORMATKI: GA3 front 596×400, DA2 trawers nośny 564×560, DB2 front 446×713, zlew „wg szablonu" (szablonu nie ma, bo zlewu nie ma) | B | kupić albo wybrać i pobrać **karty techniczne** przed rozkrojem |
| **P0-12** | **GA3 okap: pełne dno (brak wlotu), brak wylotu recyrkulacji, front 400 na korpusie 998** | A1, A3, A4 — **3/6** | FORMATKI: „GA3 — dno/wieniec 564×400, 2 szt" (dno pełne), „front uchylny 596×400"; 998 − 400 = **598 mm lica bez frontu**; nad okapem antresola do sufitu bez kratki | B + C | przeprojektować moduł po zakupie okapu: otwór w dnie, wylot recyrkulacji, drugi front + półka dzieląca, gniazdo |
| **P0-13** | **Zabudowa lodówki C3 nie istnieje jako moduł**; cztery różne głębokości; luz wentylacyjny tylny poniżej 50; C4 ma pełne dno — 50-milimetrowa szczelina nad lodówką jest zamknięta z góry | A3, A4, A6 — **3/6** | PANELE ma tylko `bok 2478×680 — 1 szt` (brak drugiego boku, wieńca, trawersu) → **C4 nie ma na czym stać od zachodu**; głębokości: PLAN pkt 9 = 700, FORMATKI = 680, `_kontrola` = 600, C2/C4 = 580, lodówka = 650 | C + B | domknąć C3 jako pełny moduł i przyjąć **jedną** głębokość zabudowy przed rozkrojem |
| **P0-14** | **Pilaster ma trzy statusy w jednym dokumencie** — a wisi na nim cała ściana A | A1, A5, A6 — **3/6** | `[P]` w PLAN pkt 2, `[~]` w §1 i na rzucie, `[?]` w pkt 11.11: „**sam rzut tego nie rozstrzyga**"; ten sam element już raz wywrócił projekt (v3.7) | A | pomiar głębokości w **3 wysokościach** + długość uskoku wzdłuż ściany; do tego czasu status `[?]` zgodnie z protokołem §5 |
| **P0-15** | **Zerowy luz montażowy w ciągu C i w obu pasmach górnych** — projekt zakłada idealne ściany i sufit | A1, A4, A6 — **3/6** | ciąg C 945+280+660 = 1885 (luz 0); górne A 670+180+600+500 = 1950 (luz 0); górne C 470+477 = 947 (luz 0); blat B 2389 = ściana B 2389; `technologia-wykonania.md` §2: 20–50 mm na styk, odchyłka 5–15 mm/2 m to norma | C + A | wprowadzić blendę docinaną w każdym biegu; blaty krótsze od biegu o dylatację 3–5 mm |
| **P0-16** | **11 pomiarów z PLAN pkt 11 niewykonanych; 24 założenia nierozstrzygnięte, 4 z fałszywym statusem `[P]`** | A1, A6 — **2/6** wprost, pozostali pośrednio | PLAN pkt 11; A6 Część 2 (A1 pilaster, A6 sufit, A11 pozycja ścianki, C6 rozkład okna); protokół §4: „jeśli łańcuch się nie domyka — pytaj, nie zaokrąglaj" — dokument zaokrągla w 3 miejscach (11 mm, 25 mm, 2 mm) | A | pełna lista w `pomiar-laserowy.md` |

### P1 — poprawić przed cięciem: tanio teraz, drogo później

| ID | problem | zgłosili | dowód | koszyk | działanie |
|---|---|---|---|---|---|
| **P1-01** | **Głębokość blatu: 600 (PLAN) vs 635 (rozpiska) vs „ramię 650" vs „65" w prompcie** — najwyższa zbieżność w całym audycie | A1, A2, A3, A4, A5, A6 — **6/6** | PLAN §5 „blat 600 (ramię 650)"; `_formatki.py BLATY` 635; PLAN pkt 13 „~118×65"; wystawka przy 635: **56 mm** (norma 20–40), przy DC1 **70–89 mm** | B | przyjąć **blat 600, ramię 500** jako jedyne `[P]` i poprawić we wszystkich plikach; 635 wykracza też poza standard 600–630 |
| **P1-02** | **Korpusy dolne: 720 w nagłówkach, 820 we wszystkich tabelach PLAN §5** (6–7 wierszy) | A1, A2, A3, A5, A6 — **5/6** | 820 + 150 + 38 = **1008 ≠ 910**; 720 + 150 + 38 = 908 ✓ (2 mm do wybrania nóżką) | C | wykreślić „820" z tabel PLAN §5; wyjątek: w wierszu DB2 „820" znaczy światło wnęki zmywarki — realne światło to **870**, do sprawdzenia w karcie |
| **P1-03** | **Ramię 1176 (model) vs 1180 (PLAN §5 ×3, blaty) → przejście 596, poniżej reguły nadrzędnej `[P]` 600** | A1, A2, A5, A6 — **4/6** | blat A 635 + blat ramienia 545 = **1180** → 1776 − 1180 = **596**; K6 mierzy korpus (1176), nie blat, więc daje PASS | C | zamienić wszystkie 1180 na 1176; blat ramienia **541**, nie 545. Sama różnica 4 mm jest ergonomicznie nieistotna — istotne jest, że poprawka opisana w historii jako wykonana nie istnieje w dokumencie |
| **P1-04** | **Blaty: narożniki policzone dwa razy (~1113–1270 mm nadmiaru); brak wycięcia 155×670 pod pilaster w blacie A; brak dylatacji** | A1, A2, A4, A5, A6 — **5/6** | blat A (1950×635) ∩ blat B = 480×635; blat B ∩ blat C1 = 635×635; blat A jest w rozpisce jako **prosty prostokąt 1950×635**, a pilaster zajmuje x 0→155, y 0→670 | C + A | w każdym narożniku skrócić jeden element o 635; dopisać wycięcie 155×670 ze statusem „po pomiarze pilastra"; rozważyć wycięcia w CNC zamiast wyrzynarką |
| **P1-05** | **Otwarta zmywarka blokuje jedyny front DC1** — nakładka 345×345 mm | A2, A3, A5 — **3/6** | DB2 (1550–2000, lico y=600) × ćwiartka wychyłu DC1 (front 345, lico x=2000, y 600–945); PLAN §5a każe trzymać w DC1 „sztućce, 1 krok od zmywarki" | B | wariant A5/Z-02: DC1 na 3 szuflady zewnętrzne (zero wychyłu); wariant A2/E37: przesunięcie ciągu B o 150 na zachód (odblokowuje też magic corner) |
| **P1-06** | **Otwarty piekarnik blokuje szuflady RL1** — nakładka 243×400 mm; kolizja przy tej geometrii nieusuwalna | A2 — **1/6** | drzwi DA2 opadają ~540 mm na szerokości y 850–1450; szuflady RL1 wysuwają się z y=1450 na 400 na szerokości x 876–1176 | C | do zapisania w PLAN pkt 9 jako ograniczenie użytkowe („piekarnik otwarty = ramię niedostępne"), nie do udawania, że go nie ma |
| **P1-07** | **Otwarta lodówka zamyka jedyne wejście do kuchni** — z 600 mm zostaje 170 (model) albo 70 (przy realnej gł. 650+50) | A2 — **1/6** (A3 potwierdza kąt otwarcia, nie drożność) | C3 (1946–2546, y 1225–1885), ŚCIANKA (1776–2546), RL1 do x=1176; skrzydło 600 przy 90° sięga do x≈1346 | C | zapisać w PLAN pkt 9 jako świadomą konsekwencję decyzji „przejście 60"; skrzydło **otwiera się** do ~112° po zamontowaniu blendy 70 (A3) — pod warunkiem P0-07 |
| **P1-08** | **Kosz segregacji: funkcja obowiązkowa bez okucia i bez realnego światła** | A1, A2, A3, A5 — **4/6** | DB1 ma 2 skrzydła po **397 < 450**; K9 przepuszcza, bo mierzy szerokość modułu (800), nie skrzydła; w BOM nie ma ani jednej pozycji ze słowem „kosz" | C + B | dopisać kosz do BOM; wybrać wersję drzwiową albo dwa pojemniki obok syfonu (wymiar po pomiarze 11.7) |
| **P1-09** | **DA1 „garnki i duże naczynia — 248 l"** — funkcja nie przechodzi przez otwór; liczba 248 l to objętość brutto | A1, A2, A6 — **3/6** (A5 hedguje) | front 240 → światło ≤ ~230; walec Ø240 nie przejdzie przez szczelinę 230 w **żadnej** orientacji; netto wg A1 = **215 l**, wg A2 = 238 l | C | zmienić przypisanie na „naczynia i sprzęt rzadko używany, wsuwane pojedynczo"; poprawić 248 → wartość netto; garnki przenieść (patrz P2-02) |
| **P1-10** | **GA4 nie ma przypisania funkcjonalnego i wypada z listy okuć** | A1, A5 — **2/6** | PLAN §5a nie ma wiersza GA4; FORMATKI: „Zawieszki … 10 szt — **GA1-3, GC1-2**" — górnych jest 6, potrzeba 12 | C | dopisać GA4 do §5a i do okuć |
| **P1-11** | **Okucia i listwy zaniżone w każdej pozycji** | A1, A4, A5 (+A2, A3 częściowo) — **5/6** | zawiasy: **38** potrzebne vs 36 zamówione „w tym zapas 10%" (netto ~33) · zawieszki **12** vs 10 · nóżki **34–38** vs 32 („8 szafek ×4" — dolnych jest 6–7) · cokół **6,3–7,5 mb** vs 5 mb, a **formatka 5000×150 nie istnieje** (arkusz 2800×2070) · konfirmaty „1 opak." vs ~180 szt | C | przeliczyć BOM z modelu, nie ręcznie; cokół rozbić na odcinki ≤2800 |
| **P1-12** | **Dekor antracyt (PLAN §10) nie występuje w bilansie płyt; rozpiska daje orzech** | A4, A5 — **2/6** | PLAN pkt 10 `[P]`: „C4 + bok przy ściance: antracyt mat ~RAL 7016"; FORMATKI: „ciemny orzech mat"; ~**2,2 m²** nie zostanie zamówione | C | nowa pozycja w tabeli m²: C4 fronty 0,34 + bok 1,69 + blenda dystansowa 0,17 |
| **P1-13** | **Moduł DB3 nie istnieje, a jest przywoływany 3×; rzut ASCII w pkt 3 pokazuje inny układ niż rozpiska** | A3, A5 — **2/6** | pkt 7 „Zlew + bateria \| DB3", „przyłącza z DB3"; pkt 8.3 „przedłużenie do DB3"; rzut: zmywarka **na zachód** od zlewu (v3.3 mówi wschód) i „DA1 45" sprzed v3.9 | C | DB3 → **DB1** w trzech miejscach; przerysować rzut ASCII albo go usunąć — instalator dostaje polecenie doprowadzenia wody do modułu, którego nie ma |
| **P1-14** | **Okap w pkt 7 przypisany do GA2 (180 mm)** — ogon naprawy v3.7a | A1, A3, A5 — **3/6** | PLAN pkt 7 tabela AGD: „Okap \| GA2"; PLAN §5, `_kontrola.py`, `_schemat.py`: GA3 600 | C | GA2 → GA3 |
| **P1-15** | **Instalacje: brak liczb wod-kan, brak gniazd okapu / rezerwy przy zlewie / punktu poboru dla LED; 2–3 gniazda blatowe wobec ~10 wg referencji; kratka wentylacyjna nieznana, a pasmo 1480–2478 zabudowane na głucho** | A3 — **1/6** (A6 potwierdza kratkę jako założenie B4) | PLAN pkt 8.1–8.3, 11.6, 11.7; `instalacje-elektryka.md` „8–12 gniazd"; blat łącznie 6,46 mb | A + C | **gate: nie zamawiać górnych przed pomiarem kratki**; rozpisać czystą listę obwodów dla elektryka |
| **P1-16** | **Dokument podaje zabezpieczenia (32A, 16A) wbrew twardej zasadzie skilla, przy nieznanej mocy płyty** | A3 — **1/6** | PLAN pkt 7 ×2 i pkt 8.1; `instalacje-elektryka.md`: „nie podawaj zabezpieczeń… dobiera uprawniony elektryk” | C | usunąć liczby, zostawić listę obwodów wydzielonych |
| **P1-17** | **„DA2 pozycjonowany do wypustu; kolejność DA1/DA2 może się zamienić" unieważnia wariant A `[P]`** | A3, A6 — **2/6** | PLAN pkt 9 (mitygacja) vs pkt 9a (wariant A `[P]`: front piekarnika kończy się dokładnie na 1450); przesunięcie DA2 przywraca kolizję z v3.8 i wywala K4 | A + C | pomiar 11.8 (pozycja puszki) rozstrzyga; mitygacja z pkt 9 jest **niewykonalna** i trzeba ją skreślić |
| **P1-18** | **Półki GA1 633×300 w korpusie o głębokości 245** | A1, A2, A4 — **3/6** | `_formatki.py` l.76 hardkoduje głębokość półki 300 dla każdej górnej; 300 > 245 − 3 (plecy) | C | jedna poprawka: `300` → `G-20` (jak w gałęzi `slupek`) — usuwa też 97 mm nieużytku w pięciu pozostałych górnych |
| **P1-19** | **Półki, których w rozpisce nie ma, przekraczają normę ugięcia:** DA1 **814**, DC1 **864** przy limicie 800 mm dla płyty 18 | A4 — **1/6** | `standardy-meble.md`: max rozpiętość 800 dla 18 mm; DA1 ma trzymać garnki | C | zaprojektować od razu z podporą środkową (listwa 60×18 pod przednią krawędzią), nie dopisywać jako „półka 18 mm" |
| **P1-20** | **Ramię kotwione 8 kątownikami do posadzki, a posadzka jest pływająca (SPC)** | A4, A6 — **2/6** | FORMATKI poz. 22 + plan montażu 4.6; PLAN pkt 10 „jasny dąb”; typ montażu podłogi `[BRAK DANYCH]` | A + B | kotwić do ściany A i do korpusu DA2; jeśli konieczne w podłożu — punkt kotwiący **pod** podłogą, wykonany przed jej ułożeniem |
| **P1-21** | **Trawersy górne 564×100 leżą dokładnie pod wycięciem płyty w DA2; ta sama gałąź generatora wstawia trawersy w DB1 pod komorę zlewu** | A3 — **1/6** | `_formatki.py` l.54 dodaje trawersy **każdemu** modułowi dolnemu; wycięcie 560×490 musi leżeć nad korpusem 560 | C | wyjątek w generatorze dla typów `piekarnik` i `zlew` |
| **P1-22** | **Ergonomia: brak strefy przygotowania (150 mm blatu między zlewem a płytą), strefa robocza przy zlewie 850/815 mm, realnych frontów szufladowych 300 mm z 2735 mm** | A2, A6 — **2/6** (A5 potwierdza liczbowo: 686 l dostępne tylko sięgiem) | `uklady-kuchni.md` §3: prep min 600, opt 900–1200; 1450 − 600 = 850, przy blacie 635 = 815 | B | przypisać strefę przygotowania do blatu ramienia (757×500 wolne spod GA4) i zapisać to w §5a; patrz też P2-02 |
| **P1-23** | **Uskok lica ciągu C 54 mm nieopisany i niekontrolowany** (DC1 lico x=2000, C2/C3 lico x=1946) | A5 — **1/6** | `_kontrola.py` CIAG_C; K5 sprawdza wspólną płaszczyznę tylko dla górnych A; rzut w pkt 3 rysuje lico C jako jedną linię | A + C | rozstrzygnąć: błąd modelu czy świadomy uskok; decyduje o stronie zawiasu DC1 (patrz P1-05) |
| **P1-24** | **Plecy S−4 × H−4 są ani nakładane, ani wpuszczane — 2 mm luzu na obwodzie** | A4 — **1/6** | nagłówek FORMATKI „plecy HDF 3 mm **nakładane**”; `_montaz.py` opiera prostokątność korpusów właśnie na plecach („Plecy blokują kąt prosty na zawsze") | C | plecy w wymiarze gabarytowym; uwzględnić +3 mm głębokości korpusu w blatach i przejściach |
| **P1-25** | **Obrzeża 1,0 / 0,4 poniżej standardu (ABS 2 mm na widoczne), przy frontach bezuchwytowych chwytanych za krawędź** | A4 — **1/6** | FORMATKI: „1,0 fronty / 0,4 korpusy”; `technologia-wykonania.md` §1 i `standardy-meble.md`: ABS **2 mm** na krawędzie widoczne | C | podnieść do 2 mm na frontach i 1 mm na przedniej krawędzi korpusów pod blatem |
| **P1-26** | **Projekt nie zawiera żadnej wyceny, a zakup idzie na firmę** | A6 — **1/6** | jedyne kwoty w repo: narzędzia 150–250 zł i wiercenie 150–400 zł (`_montaz*.py`) | B | wycena w KornerGo przed decyzją — bez niej nie da się racjonalnie ważyć „poprawić teraz czy ryzykować" |
| **P1-27** | **Strona zawiasu nieokreślona dla większości frontów** (DC1, RL1, DB1, C2, C4, wszystkie górne) | A2 — **1/6** | PLAN §5 kolumna „Front / wnętrze" bez wpisów; określone tylko DA1 i lodówka | C | uzupełnić kolumnę „strona zawiasu" przed zamówieniem; krytyczne: RL1 drzwi 300 (zawias wschodni) i DC1 (y=945 + zawias 155°) |
| **P1-28** | **Pustka 155×180 za plecami DA1** (odcinek y 670→850, gdzie kończy się pilaster) bez żadnego elementu dystansowego | A1, A5 — **2/6** | `_schemat.py` l.131 rysuje ją; PLAN nie opisuje; plecy DA1 nie mają na czym usiąść | A + C | klocki dystansowe / listwa przyścienna, wymiar po pomiarze 11.11 |
| **P1-29** | **Wymiar 947 użyty jako dwa prostopadłe wymiary; inwestor wskazał odcinek 94,7 na ścianie B jako „gdzie szafki do sufitu", a projekt postawił je na ścianie C** | A1, A5 — **2/6** | PLAN pkt 2 („Wnęka okienna → ściana C = 94,7 … = prawy odcinek ściany B") vs ciąg C 947 i blat C1 947; nigdzie nie ma zapisu decyzji o przeniesieniu | A + B | rozdzielić oba wymiary niezależnym pomiarem; zapytać inwestora, czy górne miały być na B (patrz P2-04) |

### P2 — ulepszenia, opcjonalne

| ID | problem | zgłosili | dowód | koszyk | działanie |
|---|---|---|---|---|---|
| **P2-01** | Kontrola nie ma osi Z, nie zna blatów, wysuwów, statusów wymiarów ani listy zakupowej | A1, A2, A3, A6 — **4/6** | patrz §4, rozstrzygnięcie S-3 | C | K0 statusy, K10 pion, K11 blaty w modelu, K12 bilans okuć, K3+wysuw, K9 światło skrzydła zamiast szerokości modułu |
| **P2-02** | **Odzysk 199 l pod ramieniem od strony korytarza** (panel ryflowany x 0→576 jako dwoje drzwi) + cały front 600 RL1 na 3 szuflady pełnej szerokości | A2 (E35/E43), A5 (Z-01) — **2/6** | za panelem 576×500×~690 = 199 l; po południowej stronie jest **wolny korytarz**, nie ściana; szuflada 600 daje światło ~520 → mieści Ø240 | B | jedyna kombinacja w tej geometrii, która likwiduje brak szuflady na garnki; koszt: podział panelu + przegroda w RL1 na x=576 |
| **P2-03** | **Przesunięcie ciągu B o 150 mm na zachód** — front DC1 rośnie z 345 do 495, magic corner wchodzi, kolizja ze zmywarką znika | A2 (E37) — **1/6** | rezygnacja z DB0 cargo 150 (przyprawy do GA2); lico DC1 zasłonięte tylko 0→450 | B | wymaga przeliczenia w `_kontrola.py`; koszt: znika cargo przyprawnik, który inwestor chciał |
| **P2-04** | **Górna GB1 na ścianie B, pas wschodni 538×998×400** — 890 mm ściany B w pasmie górnych stoi puste | A5 (D-01) — **1/6** | okno kończy się na 1608, bok GC1 na 2146 → 538 mm; brak kolizji | B | warunek: kierunek otwierania okna `[BRAK DANYCH]`; wariant bezpieczny — korpus 450 + blenda 88 |
| **P2-05** | **GC1 470 → 500, GC2 477 → 447** — inaczej ociekarka nie wejdzie | A5 (D-03/Z-03) — **1/6** | światło GC1 = 470 − 36 = **434**, katalogowe wkłady ~460; 500 + 447 = 947 ✓ | C | zmiana bezkosztowa, nie rusza długości ciągu |
| **P2-06** | Szuflada cokołowa pod ramieniem 1176×460, ~60 l płaskiego magazynu | A5 (D-07) — **1/6** | cokół 150 na długości 1176 to dziś martwa przestrzeń | B | opcja; front przejmuje rolę cokołu na tym odcinku |
| **P2-07** | **Zamiana zawartości DB0 ↔ GA2** — przyprawy 938 mm od płyty, a GA2 wisi wprost nad nią | A5 (Z-04) — **1/6** | środek DB0 (675, 300) vs środek płyty (280, 1150) | C | bezkosztowa zmiana w §5a |
| **P2-08** | Półki górnych 370 zamiast zaszytego 300 | A2, A4 — **2/6** | `_formatki.py` l.76; 97 mm nieużytku × 5 szafek; rozpiętości 433–633 < 800 | C | ta sama poprawka co P1-18 |
| **P2-09** | **Brak oświetlenia zadaniowego nad zlewem i nad ramieniem** — LED tylko pod GA i GC, a nad ciągiem B nie ma górnych | A2 (E45) — **1/6** | FORMATKI §3 „~3 mb, pod GA i GC"; PLAN §5 „bez górnych na B" | B | profil w podcięciu parapetu + LED na całej długości ramienia; zasilanie razem z gniazdem, **przed posadzką** |
| **P2-10** | Ręczność inwestora nieokreślona, a od niej zależy strona komory zlewu i zmywarki | A2 (E46) — **1/6** | brak wzmianki w całym PLAN | B | jedno pytanie do Dominika przed ustaleniem pozycji komory |
| **P2-11** | **Prompt wizualizacyjny (pkt 13) opisuje inną kuchnię:** ramię „~118×65" przy `[P]` 500, „doorway to **bedroom**" po korekcie v3.3a na SALON | A1, A6 — **2/6** | PLAN pkt 13 | C | przepisać po zamknięciu pomiarów |
| **P2-12** | **Martwe i sprzeczne zapisy w dokumencie, po którym montuje pierwszorazowiec:** wiersz „Gzyms/podciąg" w pkt 9 (odwołany w v3.7), wiersz „KOLIZJA `[?]`" w §5 (rozwiązana w §9a), „RL1+RL2" w planie montażu, „blat ciągły z **DA4**" w `_schemat.py`, „DA1 (3 szuflady)" i „górne gł. 320" w `_montaz.py`, pkt 9a przed pkt 9 | A1, A4, A6 — **3/6** | PLAN pkt 9, §5; `_formatki.py` l.137; `_schemat.py` l.318; `_montaz.py` s.3 i s.5 | C | wyczyścić — pierwszorazowiec dostaje instrukcję wiercenia do innej kuchni |
| **P2-13** | Czujnik zalania, zawory odcinające, rozdzielenie gniazd blatowych na 2 obwody | A3 (I3, I22, I23) — **1/6** | brak w dokumencie | C | tanie pozycje przy montażu samodzielnym |
| **P2-14** | **Scalenie GA1 + GA2 w jeden moduł 850×998×245** — możliwe, jeśli pomiar wykaże, że uskok idzie całą ścianą A | A5 (U-05) — **1/6** | GA2 180 daje **19,5 l użytecznych** przy pełnym komplecie formatek i okuć | A → B | decyzję o GA2 trzymać do pomiaru 11.11 |

**Razem: 16 × P0 · 29 × P1 · 14 × P2 = 59 pozycji.**

---

## 4. SPRZECZNOŚCI I ROZSTRZYGNIĘCIA

### S-1. Czy pokrycie ścian domyka się co do milimetra? (A5) czy ciąg C przepełnia się o 2–72 mm? (A1, A6)

**Racja: A1 i A6. A5 zweryfikował nie to, co opisał.**

Rozstrzygnięcie z plików źródłowych:

| co liczono | rachunek | wynik vs 1885 `[P]` |
|---|---|---|
| A5: lico ciągu C (odcinki wzdłuż y) | 600 (lico zasłonięte przez zmywarkę) + 345 (front DC1) + 280 + 660 | **1885 — domyka się** ✓ |
| model `_kontrola.py` (bryły) | DC1 0→945 + C2 945→1225 + C3 1225→1885 | **1885 — domyka się** ✓ |
| PLAN §5 czytany dosłownie | korpus DC1 **945** + blenda **47** + 280 + 660 | **1932 → +47** ✗ |
| `_formatki.py` (korpus 900) | 900 + 47 + 280 + 660 | **1887 → +2** ✗ (PLAN pkt 9 sam to odnotowuje) |
| z blendą dystansową lodówki 70×2478 | 947 + 280 + 660 + **70** | **1957 → +72** ✗ |

A5 policzył **lico** (co widać z przodu) i model — a te dwa zapisy są tą samą liczbą, bo A5 czytał je z `_kontrola.py`. To nie jest weryfikacja niezależna, tylko powtórzenie tego samego źródła. Fizyczny łańcuch zawiera dwa elementy, których w modelu **nie ma w ogóle**: blendę 47 (dopełnienie korpusu **900** do 947 — nieskasowaną po korekcie korpusu na 945 w v3.11) i blendę dystansową 70 (wymuszoną tym, że wysięg ścianki 770 > lico zabudowy 700, wymaganą przez PLAN pkt 9 i **już zamówioną** w FORMATKI §3). Kontrola K7 daje ✓, bo sprawdza listę odcinków lica, a nie listę zakupową.

Dodatkowo: sama liczba **1885 nie jest zmierzona** — pochodzi z „188,5 `[P]` rzut", a PLAN pkt 11.3 wprost każe zmierzyć ten łańcuch. Kontrola krzyżowa w pkt 2 („195 ≈ 188,5 + 9") rozjeżdża się o **25 mm** i jest oznaczona „✓".

**Wniosek:** ciąg C nie ma zapasu, ma deficyt **2 mm (wariant `_formatki`) do 72 mm (wariant z blendą dystansową)**, a docelowa liczba jest nieznana do czasu pomiaru 11.3. Zaliczyć A5 tę pozycję jako fałszywy alarm bezpieczeństwa — jedyny w całym audycie.

### S-2. Czy przez front DA1 (240) przejdzie garnek Ø240? (A2: nie) czy DA1 to rozwiązany odzysk martwego pola? (narracja v3.10)

**Racja: A2 — i to twarda geometria, nie opinia.**

Walec o średnicy 240 mm ma najmniejszy wymiar sylwetki równy 240 mm **w każdej orientacji** (obrót wokół dowolnej osi nie zmniejsza średnicy). Otwór ma szerokość frontu 240 minus grubość skrzydła w położeniu otwartym i ramię zawiasu — realnie **≤230 mm**. Ø240 nie przejdzie, i nie pomoże wsuwanie pod kątem. PLAN §5a przypisuje temu modułowi „garnki i duże naczynia".

Rozstrzygnięcie jest jednak dwuczłonowe, bo A2 zamyka je jednym słowem „fikcja", a to o pół kroku za daleko:

- **Moduł nie jest fikcją.** DA1 850×405 realnie przejmuje róg, który wcześniej był martwym polem ciągu B; K2 potwierdza brak podwójnego liczenia w rzucie. Odzysk przestrzeni jest prawdziwy.
- **Fikcją jest przypisanie funkcji i liczba.** 248 l to objętość brutto po obrysie (850×405×720). A1 policzył netto **215 l** (814×387×684), A2 — 238 l. Obie są niższe od 248; do dokumentu ma wejść netto. Realnie obsłużysz przez otwór 240 na głębokość 600 tylko część tego (A2: ~90–100 l).
- **Trzeci audytor potwierdza niezależnie:** A6 (S10a) doszedł do tego samego wniosku o garnku. A5 opisał to ostrożniej („przestrzeń jest, dostęp przez 240 na 600") — nie zaprzeczył, tylko nie postawił werdyktu.

**Działanie:** DA1 zostaje jako magazyn rzeczy rzadko używanych, wsuwanych pojedynczo; opis w §5a i liczba 248 l do poprawy; garnki przenieść do 3 szuflad 600 na ramieniu (P2-02) — to jedyne miejsce w tej geometrii ze światłem >500.

**Uwaga o precyzji, przy okazji:** A2 podaje maksymalny front DA1 jako 250 mm („zapas 10"), PLAN i A1 — 253,2 mm („zapas 13"). Rachunek rygorystyczny to odległość zawiasu (560, 850) od korpusu DB0: √(40² + 250²) = **253,2** — czyli A1 ma rację, a A2 użył uproszczenia. **Ale obie liczby są nieważne**, bo obie wychodzą z głębokości ciągu B = **600**, a PLAN §5 deklaruje **560**; przy 560 dystans rośnie do √(40² + 290²) = 292,7 i front mógłby mieć ~280. Wniosek „cargo narożne nie wejdzie" zostaje w mocy w każdym wariancie (280 < 450), ale sama liczba 240 nie ma dziś podstawy w dokumencie.

### S-3. Czy `_kontrola.py` PASS 9/9 cokolwiek dowodzi?

> **PASS dowodzi wyłącznie, że dwuwymiarowy model zapisany wewnątrz `_kontrola.py` jest sam ze sobą zgodny — nie dowodzi niczego o projekcie, bo model ten różni się od PLAN.md i od `_formatki.py` w kilkunastu wymiarach, nie zna osi Z, blatów, blend dystansowych, wysuwów szuflad i AGD, mierzy szerokość modułu zamiast światła skrzydła i nie sprawdza statusów wymiarów ani listy zakupowej; PASS na niepomierzonych danych to precyzja bez dokładności.**

Zbieżność **6/6** — każdy agent doszedł do tego niezależnie. Uruchomienie kontrolne komisji potwierdza: `PASS — 9 kontroli, 0 błędów, 0 uwag` oraz `5/5 historycznych błędów`, przy jednoczesnych trzech policzonych kolizjach frontów (P1-05, P1-06, P1-07), dwóch elementach niemontowalnych (P0-03, P0-04) i liście do cięcia opisującej v3.5. Regresja 5/5 znaczy „nie powtórzyłem pięciu konkretnych pomyłek", nie „projekt jest poprawny".

### S-4. DA2 — czy szuflada się mieści? (A6: tak, 112 vs 110) czy nie? (A2, A3, A4: deficyt 24–50 mm)

**Racja: A3 i A4. Rachunek A6 jest niepełny.**

A6 liczy `720 − 590 (nisza) − 18 (trawers) = 112` i porównuje z frontem 110. Pomija dwa człony, które wszyscy pozostali uwzględnili: **dno korpusu 18 mm** i **korpus płyty indukcyjnej schodzący 18 mm pod blat** (56 − 38). Po ich dodaniu zostaje **76 mm** — a system szuflad z metalowymi bokami wymaga ~100–120 mm światła w pionie. A3 doszedł do 68 mm (przy niszy 600), A4 do 66–84, A2 do 71. Wszystkie warianty są na minus; różnice biorą się z tego, czy nisza to 590 czy 600 i czy liczyć trawers.

**Działanie:** decyzja z P0-06, rozstrzygana kartą kupionego piekarnika. Pozycję „System szuflad nom. 500 — DA2" usunąć z BOM do czasu rozstrzygnięcia.

### S-5. Lodówka — czy drzwi się otwierają? (A3: tak, do 112°) czy blokują przejście? (A2: zostaje 170/70 mm)

**Obaj mają rację — mierzą dwie różne rzeczy, i żadne z tych stwierdzeń nie unieważnia drugiego.**

A3 sprawdza, czy skrzydło zdąży się wychylić, zanim uderzy w kant ścianki — z blendą dystansową 70 mm tak, do ~112°, co spełnia wymóg ~110° na wyjęcie szuflad. A2 sprawdza, czy przy otwartym skrzydle da się przejść przez pas x 1176→1776 — nie, zostaje 170 mm (model) albo 70 mm (przy realnej głębokości lodówki 650 + 50 wentylacji). Obie odpowiedzi są poprawne.

**Uwaga krzyżowa:** cała poprawność wyliczenia A3 stoi na blendzie 70, czyli dokładnie na tym elemencie, który wg S-1 **nie ma miejsca w łańcuchu C**. Dwie pozycje ocenione niezależnie jako „policzone dobrze, nie ruszać" (A3/A33) i „brak 72 mm" (A6/S3) to ten sam element. Bez rozstrzygnięcia P0-07 pozytywna ocena A3 jest warunkowa.

### S-6. Trójkąt roboczy — trzy różne wyniki

| źródło | boki | suma |
|---|---|---|
| PLAN pkt 4 | „~1,3–1,8 m" | „~4,5 m" |
| A2 | 1206 / 1486 / 1700 | 4392 |
| A6 | 1216 / 1666 / 2007 | 4889 |
| A1 | 1216 / 1673 / 2017 | 4906 |

**Rozstrzygnięcie:** rozbieżność bierze się z punktów odniesienia (A2 mierzy do środka lica lodówki i środka wycięcia płyty, A1/A6 do innych punktów), a nie z błędu rachunku. Istotne jest to, w czym wszyscy trzej się zgadzają i co jest sprzeczne z dokumentem: **najkrótszy bok wynosi 1206–1216 mm, czyli 6–16 mm nad twardym minimum 1200** — deklarowane „~1,3 m" nie istnieje. Suma mieści się w normie 3600–7000 w każdym wariancie. Liczbę trzeba przeliczyć z modelu **po** ustaleniu głębokości (P1-01) i wpisać do PLAN §4 z podaniem punktów pomiarowych.

### S-7. Bilanse okuć — cztery różne liczby na tę samą pozycję

| pozycja | w dokumencie | A1 | A4 | A5 |
|---|---|---|---|---|
| zawiasy 110° | 36 („w tym zapas 10%") | 38 | 38 (netto ~33 → niedobór 5) | ~32 „zgodne" |
| zawieszki | 10 | 12 | 12 | 12 |
| nóżki | 32 | 36 | 38 | 34–36 |
| cokół | ~5 mb | 6,997 mb | 5,8–7,5 mb | 6,3 mb |

**Rozstrzygnięcie:** A1 i A4 zgadzają się na **38 zawiasach** — A5 policzył bez frontów słupka C2 (1300 i 1070 mm wymagają po 4 zawiasy) i C4. Przy zawieszkach i cokole zgodność jest pełna: **12 zawieszek** (nie 10 — pominięto GA4) i **ponad 6 mb cokołu** (nie 5). Rozrzut nóżek (34–38) zależy od tego, czy liczyć C2/C3 i czy stosować regułę 6 nóżek dla szafek ≥800. **W każdym wariancie każdej z tych pozycji jest za mało** — spór o dokładną liczbę jest bezprzedmiotowy do czasu ustalenia listy modułów; wtedy policzyć z modelu (P2-01, kontrola K12).

### S-8. Czy „luz montażowy 0" to sukces (K7 PASS, A5: „0 niezagospodarowanych odcinków") czy defekt (A1: BRAK)?

**Racja: A1.** K7 sprawdza, czy lico jest domknięte frontem albo blendą — i słusznie daje PASS. Ale ciąg zamykający się **co do zera** wobec wymiaru ściany, który nie został zmierzony, jest ostrzeżeniem, nie sukcesem: `technologia-wykonania.md` §2 wymaga 20–50 mm na styk, a typowa odchyłka ściany to 5–15 mm na 2 m. Ciąg B ma absorpcję tylko po jednej stronie (blenda 445 na zachodzie), ciąg C, górne A i górne C nie mają jej wcale. To pozycja P0-15 — i uzasadnia poprawkę K1 z listy A1 (U7): raportować luz per bieg, żeby „delta 0" przestała się drukować jako sukces.

### S-9. Gdzie który agent przesadził

- **A5** — jedyny fałszywy alarm bezpieczeństwa w audycie: „pokrycie domyka się co do mm" (S-1). Poza tym raport bardzo mocny — A5 jako jedyny znalazł uskok lica 54 mm, brak funkcji dla GA4 i sprzeczność „gdzie szafki do sufitu".
- **A2** — [E08] nazywa 850 mm „naruszeniem TWARDEGO PROGU 1200 dla U". Próg 1200 dotyczy odległości między ramionami U na całej szerokości; tutaj zwężenie obejmuje 426 z 800 mm modułu zlewowego i wynika ze świadomie wybranego półwyspu. A2 sam to uczciwie łagodzi w tym samym punkcie. Właściwa etykieta: naruszony próg półwyspu (1000) i przejścia roboczego (1050) o 150–235 mm. To nadal defekt, ale o klasę niżej niż zapisano.
- **A6** — dramatyzuje przy S9 („nisza 590 → mieści się"), a jednocześnie **zaniża** problem, bo pomija dno i korpus płyty (S-4). W drugą stronę: S1 (przekątna 2569,6) to najlepsza pojedyncza obserwacja całego audytu, której nikt inny nie zrobił.
- **A1** — 44 pozycje „BŁĄD" to liczba zawyżona przez rozdrobnienie: kilkanaście z nich to ta sama przyczyna (gałąź `narozna` w generatorze, rozjazd głębokości). Wartość raportu jest w tabelach, nie w bilansie.
- **A4** — 7,5 mb cokołu policzone hojnie (A5: 6,3, A6: 6,9). Bez znaczenia dla wniosku: zamówione 5 mb nie wystarcza w żadnym rachunku.
- **A3** — najbardziej dyscyplinowany metodycznie raport; jedyny, który w ogóle wszedł w instalacje, wentylację i przekrój pionowy modułów AGD. Bez przesady.

---

## 5. LISTA POMIAROWA — SKRÓT

Pełna checklista terenowa: **`audyt/pomiar-laserowy.md`**.

| # | Co zmierzyć | Dokładność | Rozstrzyga |
|---|---|---|---|
| 1 | **Pilaster: głębokość na 3 wysokościach + długość uskoku wzdłuż ściany A** | ±1 mm / ±5 mm | P0-14, P1-28, P2-14 — całą ścianę A |
| 2 | Ściana A łańcuchowo: pilaster → 1950 → otwór 1270 → reszta muru | ±2 mm | P0-15, ciąg A, kotwienie ramienia |
| 3 | Ściana B: 2389 **dołem, w połowie i górą** + łańcuch okna 597 / 856 / 947 | ±2 mm | P0-15, pozycja zlewu pod oknem (dziś rozjazd 11 mm) |
| 4 | **Ściana C łańcuchowo: 947 → słupek → lodówka → ścianka (pozycja 1885, grubość, wysięg 770)** | ±2 mm | **P0-07** — czy ciąg C w ogóle wejdzie |
| 5 | Przekątne narożników A/B i B/C | ±2 mm | P1-04 — łączenia frezowane blatów |
| 6 | **Wysokość podłoga–sufit w 4–6 punktach, PO POSADZCE DOCELOWEJ** | ±2 mm | **P0-05, P0-03, P0-04** — wszystkie formatki pionowe |
| 7 | Płaskość podłogi (najwyższy i najniższy punkt na trasie zabudowy) | ±1 mm | zakres regulacji nóżek, poziom blatu |
| 8 | Pion ścian A, B, C (góra vs dół) | ±1 mm/m | luzy montażowe, blendy docinane |
| 9 | **Kratka wentylacyjna: pozycja i wymiar** | ±10 / ±5 mm | **gate: nie zamawiać górnych przed tym pomiarem** (P1-15) |
| 10 | Podejścia wody i odpływu: pozycja x, wysokość, rozstaw, średnice | ±5 mm | P1-08, P1-13, DB1 i DB2 |
| 11 | **Puszka siłowa na ścianie A: dokładna pozycja** | ±5 mm | **P1-17** — czy wariant A `[P]` się utrzyma |
| 12 | Materiał ścian A i C pod szafki górne (beton / pustak / gazobeton / GK) | jakościowo | typ kotew; **brak tej pozycji w PLAN pkt 11** |
| 13 | Wysokość lodówki **z nakładkami zawiasów** | ±5 mm | P0-13, szczelina 50 mm pod C4 |
| 14 | Głębokość parapetu + kierunek otwierania okna | ±5 mm | P2-04, kolizja skrzydła z baterią |
| 15 | Grubość układu posadzkowego (podkład + dąb) z karty produktu | ±1 mm | pkt 6, jeśli mierzone przed ułożeniem |

---

## 6. MODUŁY WYMAGAJĄCE PRZEPROJEKTOWANIA

Nie „poprawienia liczby" — przeprojektowania:

| Moduł | Dlaczego |
|---|---|
| **DA1** | front 240 nie przepuszcza przypisanej funkcji; front w rozpisce 446; półka 814 > normy 800; brak elementu dystansowego za plecami (155×180) |
| **DA2** | bilans pionowy nie domyka się (P0-06); trawersy pod wycięciem płyty; plecy pełne bez przepustu i wentylacji niszy |
| **RL1** | podział frontu z v3.12 nie istnieje w formatkach; brak przegrody, den i frontów szuflad; blat 545 daje przejście 596 |
| **DC1** | cztery różne wymiary; front 446 vs otwór 345; blenda 47 podwójnie liczona; uskok lica 54 mm; kolizja z otwartą zmywarką |
| **C2** | 2378 + 150 = 2528 > sufit; cargo o świetle 244 mm nie ma nominału katalogowego; 2 półki na 2378 wysokości; brak półki stałej |
| **C3** | **nie istnieje jako moduł** — brak drugiego boku, wieńca, trawersu; bok 2478×680 niemontowalny; cztery głębokości; wentylacja bez drogi wylotu |
| **C4** | pełne dno zamyka szczelinę wentylacyjną lodówki; brak podparcia od zachodu; brak półki; zły dekor (orzech zamiast antracytu) |
| **GA3** | pełne dno (brak wlotu okapu), brak wylotu recyrkulacji, 598 mm lica bez frontu, brak gniazda, brak modelu okapu |
| **DB1** | *(zmiana wyposażenia, nie geometrii)* skrzydła 397 < 450 wymaganych przez własną kontrolę K9; kosza nie ma w BOM; trawersy kolidują z komorą |

Pozostałe moduły (DB0, DB2, GA1, GA2, GA4, GC1, GC2) wymagają **wyłącznie poprawek liczbowych i uzupełnień** — front cargo dla DB0, głębokość półek dla górnych, szerokości GC1/GC2 pod ociekarkę, przypisanie funkcji dla GA4.

---

## 7. STATYSTYKA AUDYTU

### 7.1 Wkład agentów

| Agent | rola | pozycji surowo | BŁĄD | RYZYKO | BRAK | ULEPSZ. | ZGODNE / poprawne | `[BRAK DANYCH]` |
|---|---|---|---|---|---|---|---|---|
| **A1** | metrolog | 73 (+7 U) | 44 | 16 | 8 | 7 | 5 | 27 |
| **A2** | ergonomista | 47 | 18 | 16 | 7 | 4 | 2 | — |
| **A3** | AGD + instalacje | 53 | 21 | 10 | 18 | 4 | 12 | 18 |
| **A4** | technolog płyty | 69 | 24 | 11 | 27 | 7 | — | — |
| **A5** | kompletność + zakupy | ~51 (D7 / U6 / Z10 / BOM 19 brak + 9 zaniżonych) | — | — | 19 | — | k7 5/5 | — |
| **A6** | adwokat diabła | 53 (10 scenariuszy + 6 „poza dziesiątką" + 24 założenia + 9 luk kontroli + 4 zarzuty) | — | — | — | — | — | 24 |
| **Razem surowo** | | **≈346** | | | | | | |

### 7.2 Po deduplikacji

| Wskaźnik | Wartość |
|---|---|
| Pozycji w werdykcie | **59** (P0 **16** · P1 **29** · P2 **14**) |
| Stopień redukcji | ≈ **5,9 ×** |
| Koszyk **A** (pomiar) | 15 pozycji, w tym 6 blokujących (P0-05, P0-07, P0-14, P0-15, P0-16, P1-15) |
| Koszyk **B** (decyzja Dominika) | 18 pozycji, w tym 6 blokujących (P0-06, P0-09, P0-10, P0-11, P0-12, P0-13) |
| Koszyk **C** (poprawka od ręki) | 34 pozycje, w tym 9 blokujących |
| Pozycji zgłoszonych przez **6/6** agentów | **2** (głębokość blatu 600/635; bezwartościowość PASS 9/9) |
| Pozycji zgłoszonych przez **≥4/6** | **13** — wszystkie w P0 lub na czele P1 |
| Pozycji zgłoszonych przez **1/6**, utrzymanych w werdykcie | **14** — najcenniejsze: przekątna boku lodówki 2569,6 (A6), pełne dno okapu i C4 (A3), uskok lica C 54 mm (A5), kolizja piekarnik × RL1 (A2), półki DA1/DC1 > 800 (A4) |
| Sprzeczności rozstrzygniętych | **9** (S-1…S-9) |
| Fałszywych alarmów bezpieczeństwa | **1** (A5, S-1) |
| Przypadków przesady w klasyfikacji | **2** (A2 „twardy próg 1200"; A1 inflacja bilansu BŁĄD) |
| Modułów do przeprojektowania | **8 z 15** (+1 do zmiany wyposażenia) |
| Modułów bez zastrzeżeń konstrukcyjnych | **0** |

### 7.3 Rozkład P0 po źródle problemu

| Źródło | P0 |
|---|---|
| Rozjazd model ↔ dokument ↔ generator (`protokol-weryfikacji.md` §1 niespełniony) | 5 |
| Brak osi Z / geometria pionowa | 4 |
| Brak danych wejściowych (AGD, dostawca, decyzje technologiczne) | 4 |
| Brak pomiarów / fałszywe statusy `[P]` | 3 |

---

*Werdykt komisji. Podstawa: sześć raportów niezależnych + weryfikacja krzyżowa w `PLAN.md`, `FORMATKI-ROBOCZE.md`, `_formatki.py`, `_kontrola.py`, `_schemat.py`, z uruchomieniem `python3 _kontrola.py --regresja`. Żaden wymiar nie został oszacowany ani dopowiedziany.*
