# Audyt niezależny — AGD + INSTALACJE

**Projekt:** kuchnia-wyspa, PLAN.md v3.12a (2026-08-13) + FORMATKI-ROBOCZE.md (R1) + `_formatki.py` + `_kontrola.py`
**Zakres:** wyłącznie AGD (dopasowanie wnęk, luzy, wentylacja, kolizje) oraz instalacje (wod-kan, 230 V, siła, LED, wentylacja).
**Data audytu:** 2026-08-13
**Audytor:** niezależny, bez wglądu w pozostałe raporty.

---

## 0. Baza obliczeniowa (wszystko wyprowadzone z dokumentu, nic dodane)

| Wielkość | Wartość | Źródło |
|---|---|---|
| Blat — górna powierzchnia | 910 | PLAN pkt 2 `[P]` |
| Grubość blatu (laminat) | 38 | PLAN pkt 5, FORMATKI pkt 2 |
| Spód blatu | 910 − 38 = **872** | wyliczenie |
| Cokół / nóżki | 150 | PLAN pkt 5, pkt 6 |
| Korpus dolny — wysokość | 720 | PLAN pkt 5, FORMATKI (boki 560×720) |
| Kontrola pionu | 150 + 720 = 870; 870 + 38 = **908 ≠ 910** | rozjazd 2 mm — patrz [BRAK DANYCH] nr 14 |
| Dno korpusu (płyta 18) — górna powierzchnia | 150 + 18 = **168** | wyliczenie |
| **Prześwit wewnętrzny szafki dolnej** | 872 − 168 = **704 mm** | wyliczenie |
| Głębokość korpusów dolnych | 560 (DA1 405, RL1 460, DC1 546, C2/C4 580) | PLAN pkt 5 |
| Głębokość blatu | **600 wg PLAN pkt 5, 635 wg FORMATKI/`_formatki.py`** | sprzeczność, patrz BŁ-19 |
| Dół szafek górnych / okapu | 1480 | PLAN pkt 6 |
| Sufit | 2478 `[P]` | PLAN pkt 2 |

Urządzenia **podane w dokumencie**: płyta Bosch PXE601DC1E (572 × 512 × 56; wycięcie 560 × 490), lodówka wolnostojąca 600 × 650 × 1900, zmywarka „45", piekarnik (bez modelu), okap recyrkulacyjny (bez modelu), zlew 1-komorowy z ociekaczem (bez modelu). **Modele piekarnika, zmywarki, okapu i zlewu nie istnieją w dokumencie — tam, gdzie potrzebna była liczba, użyłem wartości katalogowych ze skilla (`standardy-meble.md`) i oznaczyłem to jawnie.**

---

## 1. TABELA GŁÓWNA

| # | urządzenie/instalacja | wymóg (z liczbą) | stan w projekcie | konflikt | kategoria |
|---|---|---|---|---|---|
| **AGD — płyta indukcyjna Bosch PXE601DC1E** ||||||
| A1 | Płyta + piekarnik w jednym module DA2 600 | nisza piekarnika **590–600** (PLAN pkt 5/7) + trawers nośny **18** (FORMATKI) + korpus płyty pod blatem **56 − 38 = 18** = **636 min** | prześwit wewnętrzny DA2 = **704**; pozostaje **704 − 636 = 68 mm** na szufladę i na wymagany prześwit wentylacyjny płyty | FORMATKI deklaruje `DA2 — front szuflady dolnej 596×110` oraz okucie `System szuflad nom. 500, 1 kpl — DA2, szuflada pod piekarnikiem`. **110 > 68.** Nawet przy niszy 590 i bez trawersu: 704 − 590 − 18 = **96 < 110**. Szuflada nie mieści się w pionie | **BŁĄD** |
| A2 | Trawersy górne w szafce z płytą | korpus płyty wystaje **18 mm** pod spód blatu (872 → 854) na całej powierzchni wycięcia 560×490 | `_formatki.py` (linia 54) dodaje **trawersy górne 564×100, 2 szt.** do KAŻDEGO modułu dolnego, w tym DA2. Trawers leży w płaszczyźnie 854–872, dokładnie pod wycięciem | wycięcie 490 gł. w blacie 635 musi leżeć nad korpusem 560 → **zawsze nachodzi na trawers przedni (x 460–560) i tylny (x 0–100)**. Płyta nie osiądzie w blacie | **BŁĄD** |
| A3 | Wycięcie 560 × 490 w blacie | pozycja wycięcia w głąb blatu | **nieokreślona** — dokument podaje tylko wymiar | przy blacie 635: 635 − 490 = 145 mm do rozdzielenia przód/tył; bez tej liczby nie da się zamówić CNC ani sprawdzić kolizji z trawersem, z niszą piekarnika i z osią okapu | **BRAK** |
| A4 | Wycięcie 560 vs korpus DA2 | korpus 600 − 2×18 = **światło 564** | wycięcie **560** | zapas **2 mm na stronę**. Wykonalne tylko CNC przy rozkroju, nie wyrzynarką „na miejscu" jak zakłada PLAN pkt 12 i FORMATKI pkt 2 | **RYZYKO** |
| A5 | Prześwit wentylacyjny pod płytą / przegroda | liczba z karty montażowej Bosch | PLAN pkt 7: „**przegroda od płyty wg karty**" — bez wartości i bez pozycji w FORMATKI | jednocześnie w tej samej przestrzeni zaplanowano szufladę (A1). Nie da się rozstrzygnąć, czy szuflada w ogóle jest dopuszczalna nad piekarnikiem | **BRAK** |
| A6 | Umiejscowienie szuflady w DA2 | jedna, jednoznaczna odpowiedź | PLAN pkt 5: „**górna** szuflada płytsza"; PLAN pkt 5a: „szuflada na blachy/formy (**dolna**, płytsza)"; FORMATKI: „front szuflady **dolnej**" | wariant „dolna" jest fizycznie niemożliwy: front dolny 110 + fuga 3 + front piekarnika 595 = 708, top piekarnika wypadłby na **~868**, a korpus płyty sięga do **854** → nachodzenie 14 mm i zero wentylacji | **BŁĄD** |
| A7 | Odstęp okap – płyta | **≥550** (SKILL pkt 4, standardy-meble) | 1480 − 910 = **570** (a od szkła płyty ~566) | brak — **pozycja poprawna ✓** | — |
| A8 | Odstęp płyty od ściany bocznej / wysokiej zabudowy | **≥300 TWARDY PRÓG** (uklady-kuchni §3) | płyta y 864→1436 (`_kontrola.py`); do ściany B: **864**, do linii ramienia: 1950 − 1436 = **514** | brak — **pozycja poprawna ✓** | — |
| A9 | Moc płyty | model + moc z tabliczki (wymóg `instalacje-elektryka.md`) | **nie ma w dokumencie** | bez tego elektryk nie dobierze obwodu; PLAN mimo to podaje „32A" (patrz I6) | **BRAK** |
| **AGD — piekarnik** ||||||
| A10 | Model piekarnika | wymiary urządzenia + karta niszy | **brak modelu**; PLAN operuje ogólnym „nisza 560 × 590–600" | cała arytmetyka DA2 (A1) stoi na wartości katalogowej, nie na karcie | **BRAK** |
| A11 | Wentylacja niszy piekarnika | piekarnik do zabudowy wymaga otwartego tyłu niszy / szczeliny wentylacyjnej + przepust na przewód | FORMATKI: `DA2 — plecy HDF 596×716` = **pełne plecy, bez wycięcia**; brak pozycji „wycięcie wentylacyjne" i „przepust kablowy" | piekarnik zamknięty od tyłu; brak drogi dla przewodu zasilającego i dla przewodu płyty | **BŁĄD** |
| A12 | Piekarnik vs lodówka | min. jedna szafka rozdzielająca (standardy-meble) | piekarnik na ścianie A, lodówka na C, między nimi cała szerokość kuchni | brak — **poprawne ✓** | — |
| A13 | Przestrzeń przed otwartymi drzwiami piekarnika | ≥1000 (uklady-kuchni §4) | PLAN pkt 4: front A ↔ front C1/lodówki **1250–1350** | brak — **poprawne ✓** | — |
| **AGD — okap recyrkulacyjny** ||||||
| A14 | Przypisanie okapu do modułu | jeden moduł | PLAN pkt 5: **GA3 600** (850→1450); PLAN pkt 7 (tabela AGD): „Okap \| **GA2**" — a GA2 ma **180 mm** szerokości | okap 600 nie wejdzie w moduł 180. Korekta z v3.7a nigdy nie dotarła do pkt 7 | **BŁĄD** |
| A15 | Wlot powietrza do okapu | otwór w dnie szafki okapowej | FORMATKI: `GA3 okap — dno/wieniec 564×400, 2 szt.` = **pełne dno bez otworu** | okap zabudowany w szafce z zamkniętym dnem nie ma czym zasysać | **BŁĄD** |
| A16 | Wylot powietrza (recyrkulacja) | kanał + kratka wylotowa do pomieszczenia — **warunek działania trybu recyrkulacji** | PLAN pkt 5 GA3: „recyrkulacja — kratka `[?]`"; PLAN pkt 5a: „**nad nim antresola na rzeczy sezonowe**"; szafka idzie do sufitu 2478 | powietrze nie ma dokąd wyjść: nad okapem zamknięta antresola, nad nią sufit. Brak kratki wylotowej w FORMATKI (ani w licu frontu, ani w wieńcu) | **BŁĄD** |
| A17 | Front lica GA3 | wysokość frontu górnych = **996** (jak GA1/GA2/GA4) | FORMATKI: `GA3 okap — front uchylny 596×400` — jedyny front tej szafki | 996 − 400 = **596 mm lica bez frontu** = otwarta dziura nad okapem (antresola bez frontu). Kontrola K7 tego nie łapie, bo sprawdza lico w rzucie, nie w elewacji | **BŁĄD** |
| A18 | Oś okapu vs oś płyty w głąb | okap powinien obejmować palniki przednie | okap: korpus 400 + front 19 → środek ~**210** od ściany; płyta: wycięcie 490 w blacie **635**, pozycja nieokreślona → środek między **245** (wycięcie przy licu) a **390** (wycięcie przy ścianie) | rozjazd osi **35–180 mm** do tyłu; nierozstrzygalny, dopóki A3 (pozycja wycięcia) nie jest ustalona | **RYZYKO** |
| A19 | Dostęp do wymiany filtra węglowego | filtr węglowy wymienny — dostęp bez demontażu zabudowy | brak jakiegokolwiek zapisu; jest tylko `Podnośnik frontu okapu (Aventos HK-S lub wg okapu) — dobór po zakupie okapu` | filtr węglowy w recyrkulacji jest materiałem eksploatacyjnym; brak opisanej ścieżki dostępu i brak zapasu miejsca nad korpusem okapu | **BRAK** |
| A20 | Dane okapu | model, wymiary, wydajność m³/h, typ i liczba filtrów, wysokość korpusu | „zakup inwestora" `[P]` — bez żadnej liczby | nie da się zaprojektować GA3 (wysokość korpusu okapu, otwór w dnie, wylot, front uchylny) | **BRAK** |
| **AGD — zmywarka 45** ||||||
| A21 | Światło wnęki | **450 × 820+** (PLAN pkt 7; standardy-meble: urządzenie 446 × 818) | DB2 = 1550→2000 = **450**; wysokość realna 872 | 450 − 446 = **4 mm łącznie (2 mm/stronę)** ✓; 872 − 818 = **54 mm** zakresu nóżek ✓ — **poprawne** | — |
| A22 | Głębokość wnęki vs przyłącza | urządzenie 45 cm: **~555 gł.** (standardy-meble; **dokument nie podaje modelu**) | korpusy ciągu B: **560** | za urządzeniem zostaje **560 − 555 = 5 mm** na wąż dopływowy, odpływowy i przewód. Fizycznie niewykonalne — przyłącza muszą iść bokiem lub w cokole, czego dokument nie opisuje | **RYZYKO** |
| A23 | Osłona parowa pod blatem | wymagana nad zmywarką przy blacie **laminowanym 38** (para rozwarstwia laminat) | **nie ma ani w PLAN, ani w FORMATKI pkt 3 (okucia)** | brak pozycji zakupowej i brak zapisu montażowego (krok 9 planu montażu wymienia tylko „zmywarka") | **RYZYKO** |
| A24 | Front meblowy zmywarki | wymiary z karty urządzenia | FORMATKI: `446 × 713`; wysokość **713 zaszyta na sztywno** w `_formatki.py` linia 50 (`add(..., S-4, 713, ...)`) | sąsiednie fronty dolne mają **716** → 3 mm uskok w linii dolnej; wymiar nie pochodzi z karty zmywarki (brak modelu) | **BRAK** |
| A25 | Otwarte drzwi zmywarki vs front DC1 | SKILL zasada 6: „otwarty front nie może blokować... sąsiednich szuflad" | zmywarka: lico y=600, x 1550→2000; otwarte drzwi 45 cm rzutują ~570–600 mm → zajmują **y 600→~1180, x 1554→1996**. DC1: front **345 mm**, lico x=2000, **y 600→945** — w całości wewnątrz tego rzutu | **kolizja funkcjonalna: nie da się otworzyć DC1 przy otwartej zmywarce.** A plan funkcjonalny 5a przypisuje DC1 „sztućce serwisowe — 1 krok od zmywarki", czyli dokładnie scenariusz jednoczesnego użycia. `_kontrola.py` K3 tego nie wykrywa (sprawdza pas 50 mm i bryły statyczne, nie stan „AGD otwarte") | **BŁĄD** |
| A26 | Przestrzeń przed otwartą zmywarką | **≥1100** (uklady-kuchni §4) | od lica y=600 do ścianki y=1885 → **1285** | brak — **poprawne ✓** | — |
| A27 | Zlew nad zmywarką | zakaz (standardy-meble) | zlew DB1 750→1550, zmywarka DB2 1550→2000 — rozłączne | brak — **poprawne ✓** | — |
| **AGD — lodówka wolnostojąca 600 × 650 × 1900** ||||||
| A28 | Głębokość zabudowy lodówki | jedna liczba | **cztery różne w czterech plikach:** PLAN pkt 9 „lico zabudowy **70**" (=700); FORMATKI/`_formatki.py` bok wykończeniowy **680**; `_kontrola.py` C3 x 1946→2546 = **600**; C4 nadstawka i C2 słupek = **580** | lodówka ma **650** gł. — jest głębsza od modelu kontrolnego (600) i od nadstawki (580); wystaje przed nie o 50 i 70 mm. Nie da się zamówić boku ani nadstawki | **BŁĄD** |
| A29 | Luz wentylacyjny za lodówką | **≥50 mm tył** (SKILL zasada 5, standardy-meble) | przy boku 680: 680 − 650 = **30 mm** < 50. Przy modelu `_kontrola` 600: **−50 mm** (lodówka wystaje). Tylko lico 700 daje 700 − 650 = **50 ✓** | dwa z trzech wariantów głębokości łamią próg wentylacji | **BŁĄD** |
| A30 | Blenda dystansowa lodówka–ścianka | ścianka wysięg **770** (2546 − 1776 wg `_kontrola.py`) − lico zabudowy | PLAN pkt 9 liczy 770 − **700** = 70; FORMATKI zamawia **~70 × 2478**. Przy boku 680: 770 − 680 = **90**. Przy `_kontrola` 600: 770 − 600 = **170** | zamówiona blenda 70 jest prawidłowa **wyłącznie** dla lica 700, którego żaden inny plik nie potwierdza. Przy pozostałych wariantach drzwi lodówki nie otworzą się >90° — czyli awaria, którą blenda miała naprawić | **BŁĄD** |
| A31 | Wentylacja góra lodówki | **≥50 mm** nad urządzeniem + droga odprowadzenia ciepła | 1950 (dół C4) − 1900 (lodówka) = **50 ✓** w liczbie, ale C4 ma `dno 624×580` = **pełne dno** i deklarowaną „kratkę wentylacyjną" bez trasy | 50-milimetrowa szczelina jest zamknięta z góry pełnym dnem nadstawki, z tyłu ścianą, z boków korpusami. „Kratka w C4" wentyluje **wnętrze nadstawki**, a nie pomieszczenie. **Ciepłe powietrze nie ma dokąd wyjść** | **BŁĄD** |
| A32 | Kratki wentylacyjne (cokół + wieniec) | pozycje zakupowe | PLAN pkt 6 i plan montażu krok 10 mówią „cokoły z kratką wentylacyjną lodówki"; **FORMATKI pkt 3 nie zawiera ani jednej kratki** (jest tylko `Listwa cokołowa 5000×150`) | element wymagany przez wentylację lodówki nie jest zamówiony | **BRAK** |
| A33 | Drzwi lodówki | otwarcie ≥90°, do wyjęcia szuflad ~110° | zawiasy od strony ścianki, otwieranie ku oknu; przy 110° koniec skrzydła wypada na ~x 1382 — poza ramieniem (x≤1176), zapas **206 mm** | geometrycznie ✓ **pod warunkiem** poprawnej blendy (A30) | — |
| A34 | Wysokość lodówki z zawiasami | 1900 + nakładka zawiasu ≤ 1950 | ujęte w pomiarach kontrolnych PLAN pkt 11.5 ✓ | brak — pozycja obsłużona | — |
| **AGD — zlew + szafka DB1** ||||||
| A35 | Model i wymiar zlewu | wymiar zewnętrzny + wycięcie w blacie | **brak** — tylko „zlew 1-komora z ociekaczem"; FORMATKI pkt 2: „zlew **wg szablonu**" | nie da się sprawdzić ani wycięcia w blacie 635, ani miejsca pod komorą, ani przejścia szuflad/kosza | **BRAK** |
| A36 | Kosz segregacji — szerokość otwarcia | próg własny projektu **≥450** (`_kontrola.py`, `FUNKCJE_OBOWIAZKOWE`) | DB1 ma **2 fronty po 397** (`_formatki.py`: `(800−6)//2 = 397`). Największe realne otwarcie = **397 < 450** | **kontrola K9 przepuszcza to błędnie**, bo mierzy `front[1]−front[0]` = szerokość **modułu** (800), a nie szerokość pojedynczego skrzydła. Ten sam typ błędu, który K8 wykrył w DC1 — tylko że tu kontrola go nie łapie | **BŁĄD** |
| A37 | Kosz + syfon + chemia w jednej szafce | komora zlewu + syfon zabierają dolną część prześwitu 704 | PLAN 5a: „DB1 zlew 80 \| kosze segregacji, chemia, akcesoria zlewu" — **bez ani jednego wymiaru pionowego** | brak sprawdzenia w pionie: nieznana głębokość komory, nieznana wysokość syfonu, nieznany model kosza. Deklaracja „wszystko w DB1" nie jest niczym poparta | **RYZYKO** |
| A38 | Trawersy górne w szafce zlewowej | komora zlewu wystaje pod blat na całą swoją głębokość | `_formatki.py` linia 54 dodaje `DB1 — trawersy górne 764×100, 2 szt.` (bez wyjątku dla typu „zlew") | trawers przedni w płaszczyźnie 854–872 przecina strefę, w którą opada komora zlewu. Generator wyłącza dla typu „zlew" tylko plecy, trawersów nie | **BŁĄD** |
| A39 | Bateria vs okno | wysięg baterii + kierunek otwierania okna | blat 910 → parapet 1661 = **751 mm** wolnej ściany ✓; **kierunek otwierania okna nie jest nigdzie podany** | jeśli okno otwiera się do wewnątrz, skrzydło może kolidować z baterią i z ociekarką | **BRAK** |
| A40 | Zlew ≥450 od rogu | uklady-kuchni §3 | DB1 750→1550; od narożnika A/B (x=155): **595 ✓**; od narożnika B/C (2546): **996 ✓** | brak — **poprawne ✓** | — |
| **AGD — sprzeczności rozmieszczenia** ||||||
| A41 | Kolejność modułów na ścianie B | jedna wersja | **PLAN pkt 3 (rzut ASCII):** `crg 15 │ ZMYW 45 │ ZLEW 80 │ DB3 ~39 │ DC1` — zmywarka **na zachód** od zlewu. **PLAN pkt 5 (tabela):** DB0 600→750, DB1 zlew 750→1550, DB2 zmywarka 1550→2000 — zmywarka **na wschód** | rzut w dokumencie pokazuje inne rozmieszczenie AGD niż rozpiska i niż `_kontrola.py`. Decyzja v3.3 mówi „wschód" — rzut z pkt 3 jest nieaktualny i wprowadza w błąd na montażu | **BŁĄD** |
| A42 | Moduł „DB3" | moduł musi istnieć w rozpisce | **PLAN pkt 7 (tabela AGD):** „Zlew + bateria \| **DB3**" oraz „Zmywarka 45 \| DB2 \| **przyłącza z DB3**"; rzut pkt 3 pokazuje „DB3 ~39" | **modułu DB3 nie ma w rozpisce pkt 5, nie ma w FORMATKI, nie ma w `_kontrola.py`.** Zlew jest w DB1, a odcinek 2000→2546 to martwe pole przejęte przez DC1. Punkt 7 kieruje przyłącza zmywarki do modułu, który nie istnieje | **BŁĄD** |
| **INSTALACJE — wod-kan** ||||||
| I1 | Podejścia wody i odpływu | pozycja (x, wysokość), rozstaw, średnice: odpływ zlewu **50**, odpływ zmywarki **32** (`instalacje-elektryka.md`) | PLAN pkt 1: „Podejścia wody/odpływu **nisko na B** `[~]`"; pkt 8.3: „pozycja `[~]` — przedłużenie do **DB3** w cokole/za korpusami"; pkt 11.7: do pomiaru | **zero liczb.** Nie wiadomo, czy zlew w pozycji 750→1550 wymaga przeróbki instalacji. Jednocześnie cel przedłużenia (DB3) nie istnieje (A42) | **BRAK** |
| I2 | Punkt zmywarki | własne ZW + odpływ 32; odpływ **nie pod zlewem** (`instalacje-elektryka.md`) | jedyny zapis to „przyłącza z DB3" (pkt 7) | zmywarka 1550→2000 nie ma przypisanego punktu wod-kan. Realna trasa (przez bok DB1 albo w cokole) nie jest opisana, a za urządzeniem zostaje 5 mm (A22) | **BŁĄD** |
| I3 | Dostęp serwisowy do podejść | zawory odcinające dostępne, plecy serwisowe | DB1 bez pleców ✓ (`_formatki.py` pomija plecy dla typu „zlew"); DB2 to wnęka bez pleców ✓ | brak — **poprawne ✓**, ale nie ma zapisu o zaworach odcinających | **ULEPSZENIE** |
| **INSTALACJE — 230 V** ||||||
| I4 | Liczba gniazd nad blatem | „co 60 cm nad blatem, **8–12 gniazd** dla typowej kuchni" (`instalacje-elektryka.md`) | PLAN pkt 8.1: „**2–3** nad blatem B/A" | blat: B 2389 + A 1950 + C1 947 + ramię 1176 = **6,46 mb** → wg referencji ~10 gniazd. Instalację robi się raz; 2–3 to niedoszacowanie o rząd wielkości | **RYZYKO** |
| I5 | Gniazda ≥600 od zlewu (poziomo) | uklady-kuchni §4 | zlew w module 750→1550 | na ścianie B pozostają tylko x ≤ 150 (fizycznie niemożliwe, tam jest korpus ciągu A/DA1 do 600) albo **x ≥ 2150** — czyli martwy narożnik za DC1. **Realnie gniazda blatowe muszą przejść na ścianę A** (wolny fartuch: y 600→864 = 264 mm oraz y 1436→1950 nad ramieniem) — czego dokument nie mówi | **RYZYKO** |
| I6 | Gniazdo okapu | „1× za okapem" (`instalacje-elektryka.md`) | **nie ma na liście** (pkt 8.1 wymienia: zmywarka, lodówka, 2–3 nad blatem, zasilanie LED) | okap w GA3 (1480–2478) bez zasilania | **BRAK** |
| I7 | Gniazdo rezerwowe przy zlewie | „1× za zlewem (osmoza / boiler / rozdrabniacz)" | **nie ma** | rezerwa nie do odtworzenia po montażu blatu i fartucha | **BRAK** |
| I8 | Gniazda zmywarki i lodówki — lokalizacja | „gniazdo w **sąsiedniej** szafce, dostęp bez wysuwania urządzenia" (`technologia-wykonania.md` §3) | PLAN wymienia tylko „gniazda: zmywarka, lodówka" — **bez szafki i bez wysokości** | dla zmywarki sąsiadem jest DB1 (mokra szafka zlewowa) albo DC1 — wybór nierozstrzygnięty; dla lodówki: C2 (cargo pełnowysokościowe) albo C4 | **BRAK** |
| I9 | Gniazdo/puszka za lodówką | luz tylny 50 mm (A29) | brak wskazania | gniazdo na ścianie za lodówką „zjada" luz wentylacyjny i wypycha urządzenie do przodu — a lodówka już teraz nie mieści się w deklarowanych głębokościach (A28) | **RYZYKO** |
| I10 | Kolizje z korpusami i plecami | DA2: piekarnik ~550 gł. w korpusie 560; plecy pełne | brak jakiegokolwiek opisu przepustu | żadna puszka ani gniazdo nie zmieści się za DA2. Przewód płyty i piekarnika musi wyjść bokiem lub w cokole — brak zapisu i brak wycięcia (A11) | **BŁĄD** |
| I11 | Gniazdo w ramieniu RL1 | decyzja **przed** posadzką (ramię kotwione do posadzki kątownikami) | PLAN pkt 8.4: „**Ewentualne** gniazdo w ramieniu L — doprowadzenie w podłodze przed posadzką docelową" | pozycja wciąż otwarta, a jest nieodwracalna. RL1 ma 3 szuflady 460 gł. + drzwi — po montażu nie da się doprowadzić zasilania. Brak daty/gate'u decyzyjnego | **RYZYKO** |
| **INSTALACJE — zasilanie płyty indukcyjnej** ||||||
| I12 | Parametry obwodu siłowego | **twarda zasada `instalacje-elektryka.md`:** „nie podawaj zabezpieczeń, przekrojów kabli ani liczby faz... dobiera uprawniony elektryk" | PLAN pkt 7: „obwód siłowy — puszka na A `[?]` **potwierdzić 32A**"; pkt 7 piekarnik: „**osobny obwód 16A**"; pkt 8.1: „Obwód siłowy do DA2 (**potwierdzić 32A**) + **16A** piekarnik" | dokument podaje wartości zabezpieczeń w trzech miejscach wbrew zasadzie skilla, przy jednoczesnym **braku mocy płyty i modelu piekarnika**. To sugestia liczbowa bez podstawy | **BŁĄD** |
| I13 | Sposób przyłączenia płyty | „podłączenie **na stałe przez puszkę przyłączeniową** (nie gniazdko)" | PLAN mówi „puszka" ✓ | brak — **poprawne ✓** | — |
| I14 | Pozycja puszki siłowej | musi być poza rzutem piekarnika i szuflady | PLAN pkt 11.8: „Puszka siłowa na A: obwód i **dokładna pozycja (ustawia DA2)**"; pkt 9 (ryzyka): „DA2 pozycjonowany do wypustu; **kolejność DA1/DA2 może się zamienić**" | **to unieważnia decyzję `[P]` z pkt 9a (wariant A).** Cały wariant A istnieje po to, żeby front piekarnika kończył się dokładnie na linii ramienia (1450). Przesunięcie DA2 do wypustu przywraca kolizję z v3.8 i wywala kontrolę K4 (okap nad płytą). Sprzeczność między `[P]` a listą ryzyk | **BŁĄD** |
| **INSTALACJE — oświetlenie LED** ||||||
| I15 | Zasilacz LED — lokalizacja | konkretna szafka | PLAN pkt 8.1: „zasilanie LED (**transformator w GA**)" — bez numeru szafki | GA1 ma tylko 245 gł., GA2 ma 180 szer., GA3 to okap. Realnie zostaje GA4 — nierozstrzygnięte | **BRAK** |
| I16 | Zasilanie 230 V zasilacza | gniazdo/puszka na poziomie górnych (1480–2478) | **nie ma na liście gniazd** — pkt 8.1 wymienia „zasilanie LED" jako pozycję, ale bez punktu poboru | zasilacz 24 V (FORMATKI pkt 3) nie ma z czego być zasilany | **BRAK** |
| I17 | Włącznik LED | „włącznik dotykowy pod szafkami górnymi lub na frezie blatu" (`instalacje-elektryka.md`) | **nie ma nigdzie** — ani w PLAN, ani w FORMATKI | brak elementu sterującego | **BRAK** |
| I18 | Długość taśmy LED | pod GA i GC, bez GA3 (okap ma własne światło) | FORMATKI: **~3 mb**. Realnie: (670+180+500) + (470+477) = **2297 mm**; z GA3: 2897 | 3 mb jest OK jako zamówienie z zapasem, ale zapis „pod GA i GC" sugeruje taśmę także pod okapem | **ULEPSZENIE** |
| I19 | Trasa kabla LED | „za wieńcem górnych do transformatora" (`technologia-wykonania.md` §3) | brak opisu przejścia z ciągu A na ciąg C (są rozdzielone oknem — na ścianie B **nie ma górnych**) | taśmy GA i GC nie mają fizycznego połączenia górą; potrzebne albo dwa zasilacze, albo trasa dołem/w fartuchu — nierozstrzygnięte | **BRAK** |
| **INSTALACJE — wentylacja** ||||||
| I20 | Kratka wentylacji grawitacyjnej | pozycja + wymiar; **zakaz zabudowy na głucho** (`technologia-wykonania.md` §4) | PLAN pkt 8.2: „**Zlokalizować** kratkę `[?]`"; pkt 9: „pomiar; kratka rewizyjna w zabudowie"; pkt 11.6: do pomiaru | **pozycja nieznana, a pasmo 1480–2478 jest zabudowane na ścianie A (GA1–GA4) i C (GC1–GC2, C2, C4) — czyli dokładnie tam, gdzie kratka wentylacyjna zwykle jest.** Ryzyko nie jest domknięte żadnym wariantem awaryjnym ani gate'em „nie zamawiaj górnych przed pomiarem kratki" | **RYZYKO** |
| I21 | Okap recyrkulacyjny a wentylacja pomieszczenia | recyrkulacja **nie zastępuje** wentylacji grawitacyjnej | PLAN pkt 8.2 to poprawnie odnotowuje: „już tylko dla wentylacji ogólnej... kratki nie zabudowywać na głucho" | brak — **poprawne ✓** | — |
| I22 | Czujnik zalania pod zlewem / zmywarką | zalecenie `instalacje-elektryka.md` (sekcja smart) | brak | tania pozycja przy montażu samodzielnym; zmywarka i zlew sąsiadują z 5 modułami z płyty wiórowej | **ULEPSZENIE** |
| I23 | Wykaz obwodów wydzielonych | lista bez parametrów: płyta, piekarnik, zmywarka, lodówka, gniazda blatowe (najlepiej 2), oświetlenie | PLAN pkt 8.1 podaje listę, ale zmieszaną z zabezpieczeniami (I12) i bez rozdzielenia gniazd blatowych na 2 obwody | dokument nie ma czystej listy obwodów do przekazania elektrykowi | **ULEPSZENIE** |

---

## 2. Trzy rozwinięcia arytmetyczne (najcięższe pozycje)

### 2.1 DA2 — bilans pionowy (A1, A2, A5, A6, A11)

```
Blat góra                                     910   [P]
Blat 38                                      −38
Spód blatu                                  = 872
Nóżki 150 + dno 18                          −168
PRZEŚWIT WEWNĘTRZNY DA2                     = 704 mm

Zajęte:
  nisza piekarnika (PLAN pkt 5/7)            600   (wariant min. 590)
  trawers nośny piekarnika (FORMATKI)         18
  korpus płyty pod blatem (56 − 38)           18
  RAZEM                                    = 636   (wariant min. 626)

ZOSTAJE na szufladę + prześwit wentylacyjny płyty:
  704 − 636 = 68 mm     (wariant min.: 704 − 626 = 78 mm)

DEKLAROWANE w FORMATKI: front szuflady 596 × 110  →  110 > 68   ✗
Nawet bez trawersu nośnego: 704 − 600 − 18 = 86 < 110            ✗
```
Elewacja się domyka (110 + 3 + 595 = 708 ≈ 715 dostępnego pod blatem), więc **błąd jest niewidoczny na rysunku frontów i widoczny dopiero w przekroju**. Do tego dochodzi trawers przedni 564×100 leżący dokładnie pod wycięciem płyty (A2) oraz pełne plecy HDF bez przepustu (A11).

**Wniosek:** w DA2 mieści się płyta + piekarnik ALBO płyta + szuflada. Nie oba naraz — chyba że karta piekarnika dopuści niszę <520 mm, czego dokument nie wykazuje.

### 2.2 Okap recyrkulacyjny — trzy niezależne braki w jednym module (A14–A17, A19, A20)

```
GA3: 600 × 998 × 400, dół 1480, góra 2478
  wlot:   dno 564×400 PEŁNE (FORMATKI)                    → brak zasysania
  wylot:  nad okapem antresola do sufitu, brak kratki      → brak recyrkulacji
  lico:   front uchylny 596×400; wymagane 996              → 596 mm lica bez frontu
  filtr:  brak opisu dostępu i brak zapasu miejsca         → brak eksploatacji
  model:  brak                                             → brak podstawy do formatek
  gniazdo: brak (I6)                                       → brak zasilania
  przypisanie: pkt 5 = GA3 (600), pkt 7 = GA2 (180)        → sprzeczność w dokumencie
```
Odstęp 570 mm nad płytą jest jedynym poprawnym parametrem tego modułu.

### 2.3 Zabudowa lodówki — cztery głębokości, jedna lodówka (A28–A32)

```
Lodówka:                                     650 gł.  [P]
PLAN pkt 9 „lico zabudowy 70":               700  →  tył 700−650 = 50  ✓ ; blenda 770−700 = 70
FORMATKI bok wykończeniowy 2478×680:         680  →  tył 680−650 = 30  ✗ (<50) ; blenda 770−680 = 90
_kontrola.py C3 (x 1946→2546):               600  →  lodówka wystaje 50 przed model ✗ ; blenda 770−600 = 170
C4 nadstawka / C2 słupek:                    580  →  lodówka wystaje 70 przed nadstawkę

Zamówiona blenda dystansowa: ~70 × 2478  →  poprawna TYLKO dla wariantu 700.
Wentylacja góra: 1950 − 1900 = 50 mm ✓ w liczbie, ale zamknięta pełnym dnem C4 624×580
                 → brak drogi wylotu ciepła; „kratka w C4" wentyluje wnętrze szafki, nie pokój.
Kratki wentylacyjne (cokół + wieniec): 0 szt. na liście zakupowej.
```

---

## 3. [BRAK DANYCH] — czego nie ma w dokumencie, a jest niezbędne do zamówienia i montażu

Kolejność = kolejność potrzebna (co blokuje co).

| # | Brakująca dana | Blokuje |
|---|---|---|
| 1 | **Model + moc [kW] płyty Bosch PXE601DC1E z tabliczki znamionowej** | dobór obwodu przez elektryka; dokument podaje „32A" bez podstawy (I12) |
| 2 | **Karta montażowa płyty: wymagany prześwit pod korpusem płyty i wymóg przegrody** | rozstrzygnięcie, czy szuflada w DA2 jest w ogóle dopuszczalna (A1, A5) |
| 3 | **Pozycja wycięcia 560×490 w głąb blatu** (ile od lica, ile od ściany) | CNC blatu, kolizja z trawersem, oś okapu (A3, A18) |
| 4 | **Model piekarnika + wymiary niszy z karty** | cały bilans pionowy DA2 (A10) |
| 5 | **Model zmywarki 45 + głębokość + wymiary frontu meblowego z karty** | wnęka, przyłącza, front 446×713 (A22, A24) |
| 6 | **Model okapu: wymiary korpusu, wydajność m³/h, typ filtra, sposób i kierunek wylotu recyrkulacji** | konstrukcja GA3 w całości (A14–A20) |
| 7 | **Model zlewu + wymiar wycięcia + głębokość komory + wysokość syfonu** | wycięcie w blacie, zawartość DB1, kosz segregacji (A35, A37) |
| 8 | **Model kosza segregacji** (montowany do drzwi 397 czy do dna) | K9 i realna funkcja segregacji (A36) |
| 9 | **Podejścia wod-kan: pozycja x, wysokość nad podłogą, rozstaw, średnice** | czy zlew i zmywarka wymagają przeróbki instalacji (I1, I2) |
| 10 | **Pozycja i wymiar kratki wentylacji grawitacyjnej** | zamówienie górnych na A i C oraz C2/C4 (I20) — **gate: nie zamawiać górnych przed tym pomiarem** |
| 11 | **Pozycja istniejącej puszki siłowej na ścianie A** | pozycja DA2, a przez nią GA3/okap i kontrola K4 (I14) |
| 12 | **Kierunek otwierania okna (do wewnątrz / uchylne / stałe)** | kolizja skrzydła z baterią i ociekarką (A39) |
| 13 | **Decyzja: gniazdo w ramieniu RL1 tak/nie** | doprowadzenie w podłodze **przed** posadzką — decyzja nieodwracalna (I11) |
| 14 | **Rozstrzygnięcie 150 + 720 + 38 = 908 vs deklarowane 910** | wysokość wnęki zmywarki i regulacja nóżek AGD (baza obliczeniowa) |
| 15 | **Rozstrzygnięcie głębokości blatu: 600 (PLAN pkt 5) czy 635 (FORMATKI)** | wycięcie płyty, wycięcie zlewu, nadwieszenie nad zmywarką i lodówką |
| 16 | **Jedna głębokość zabudowy lodówki** (580/600/680/700) | bok wykończeniowy, nadstawka C4, blenda dystansowa, wentylacja (A28–A30) |
| 17 | **Wysokość lodówki z nakładkami zawiasów** (pkt 11.5 już to zawiera ✓) | szczelina 50 mm pod C4 |
| 18 | **Materiał ścian A i C** (beton / pustak / GK) | kotwy szafek górnych do sufitu — brak w PLAN i w liście pomiarów |

---

## 4. Podsumowanie ilościowe

| Kategoria | Liczba | Pozycje |
|---|---|---|
| **BŁĄD** | **21** | A1, A2, A6, A11, A14, A15, A16, A17, A25, A28, A29, A30, A31, A36, A38, A41, A42, I2, I10, I12, I14 |
| **RYZYKO** | **10** | A4, A18, A22, A23, A37, I4, I5, I9, I11, I20 |
| **BRAK** | **18** | A3, A5, A9, A10, A19, A20, A24, A32, A35, A39, I1, I6, I7, I8, I15, I16, I17, I19 |
| **ULEPSZENIE** | **4** | I3, I18, I22, I23 |
| Pozycje **poprawne** (potwierdzone arytmetycznie) | **12** | A7 (okap 570 ≥ 550), A8 (864 i 514 ≥ 300), A12, A13, A21 (wnęka 450 / 872), A26 (1285 ≥ 1100), A27, A33, A34, A40, I13, I21 |

Do tego **18 pozycji** w wykazie [BRAK DANYCH] (sekcja 3) — częściowo pokrywają się z pozycjami BRAK w tabeli, ale wykaz jest listą zamówieniową: **bez pozycji 1–11 nie wolno zamawiać AGD ani wykonywać instalacji**.

Rozkład po podzakresach:

| Podzakres | BŁĄD | RYZYKO | BRAK | poprawne |
|---|---|---|---|---|
| Płyta indukcyjna + piekarnik (DA2) | 4 | 2 | 4 | 3 |
| Okap recyrkulacyjny (GA3) | 4 | 1 | 2 | 1 |
| Zmywarka (DB2) | 1 | 2 | 1 | 3 |
| Lodówka (C3/C4) | 4 | 1 | 1 | 2 |
| Zlew / DB1 | 2 | 1 | 2 | 1 |
| Sprzeczności rozmieszczenia AGD | 2 | 0 | 0 | 0 |
| Wod-kan | 1 | 0 | 1 | 0 |
| 230 V + siła | 3 | 4 | 4 | 1 |
| LED | 0 | 0 | 4 | 0 |
| Wentylacja pomieszczenia | 0 | 1 | 0 | 1 |

---

## 5. Werdykt

Projekt **nie jest gotowy do zamówienia AGD ani do wykonania instalacji**. Trzy moduły stykające się z urządzeniami — DA2 (płyta + piekarnik), GA3 (okap recyrkulacyjny) i C3/C4 (lodówka) — zawierają błędy, które ujawniają się dopiero w przekroju pionowym, a nie w rzucie. `_kontrola.py` ich nie wykrywa, bo wszystkie 9 kontroli działa **wyłącznie w rzucie 2D i na bryłach statycznych**: nie zna wysokości, nie zna wymiarów urządzeń, nie zna stanu „AGD otwarte" i nie odróżnia szerokości modułu od szerokości skrzydła.

Rekomendowane rozszerzenie kontroli (poza zakresem tego audytu, ale wprost z jego wyników):
- **K10 — bilans pionowy modułu AGD:** suma (nisza + trawersy + korpus urządzenia pod blatem + prześwit z karty) ≤ prześwit wewnętrzny.
- **K11 — stan „AGD otwarte":** drzwi zmywarki/piekarnika jako bryła 570–600 mm przed licem, sprawdzana przeciw frontom sąsiadów (złapałaby A25).
- **K12 — szerokość skrzydła zamiast szerokości modułu** w K8/K9 (złapałaby A36).
- **K13 — jedna głębokość na urządzenie** we wszystkich plikach projektu (złapałaby A28).
