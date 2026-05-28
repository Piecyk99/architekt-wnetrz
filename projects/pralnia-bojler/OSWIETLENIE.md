# Projekt oświetlenia — salon + biuro + garderoba/strefa techniczna

## Context

Pomieszczenie wielofunkcyjne ~4,93 × 4,78 m łączące trzy strefy: salon (kanapa + TV), biuro (biurko w narożu NW) oraz zabudowę przesuwną w niszy ściany północnej (wnęka murowa 266 × **40 cm** głęb. wg rysunku; zabudowa **wystaje 20 cm do pokoju** → 60 cm całkowitej głębokości, bo pralka/suszarka mają 60 cm; wysokość 250 cm) z pralką, suszarką, bojlerem elektrycznym i półkami. Inspiracje: ciemny orzech (front przesuwny), kremowe wnętrze szafy, LED w górnej belce i pionowy LED w ościeżu — czyli ciepły, miękki, "premium" charakter zabudowy. Sufit będzie cały podwieszany GK (potwierdzone), smart-home + serwerownię robi sam właściciel (potwierdzone) — czyli projektujemy pod Shelly/HA: każdy obwód osobno, neutralny w każdej puszce, miejsce na zasilacze 24V w serwerowni. W salonie świadoma rezygnacja z lampy wiszącej — atmosfera buduje się przez wnękę LED po obwodzie + spoty podtynkowe + LED dekoracyjny w zabudowie.

Dokument ma być na tyle konkretny, żeby przekazać go elektrykowi bez tłumaczenia: sekcje, obwody, wysokości, puszki, profile, zasilacze, logika scen.

> **FAZA 0a — weryfikacja względem rysunku (v3, po odpowiedziach inwestora).** Odczyt rzutu + 3 pytania dały następujące ustalenia: (1) **wnęka murowa ma 40 cm**, nie 60 — zabudowa wystaje 20 cm do pokoju, bo pralka/suszarka mają 60 cm głęb. (korekta wymiarowa); (2) **napis „OR" = drzwi przesuwne zabudowy** (potwierdzone) — to NIE okno, więc **nie ma kolizji** z zabudową 250 cm; (3) **wejście jest na ścianie E, obok TV, w środkowej części** (potwierdzone) — przywrócono drzwi na ścianie E, P1 przy wejściu, TV przesunięte na południe od drzwi; (4) **symbol ◯** w rogu rysunku = artefakt/oznaczenie do potwierdzenia w naturze (przyłącza wody/odpływ pralki przyjęto w sekcji prawej); (5) wymiar **„161"** pozostaje do potwierdzenia (nieistotny dla projektu świateł).

---

## 0. Analiza pomieszczenia (geometria + strefy)

### 0.1 Orientacja rzutu (wg odczytu rysunku)

- **Ściana N (góra, 493 cm)** — tu biuro (lewa część) + zabudowa przesuwna (prawa część). Druga kartka potwierdza: „BIURO" lewy-górny, „DRZWI Przesuwne" prawy-górny.
- **Ściana W (lewa, 478 cm)** — kanapa.
- **Ściana E (prawa, 478 cm)** — **wejście** w środkowej części + TV na południe od drzwi (potwierdzone przez inwestora).
- **Ściana S (dół)** — bez oznaczeń.
- **Okna** — brak w obrębie zabudowy (napis „OR" = drzwi przesuwne, nie okno). Instalacje — patrz 0.3.

### 0.2 Wymiary odczytane z rysunku

| Element | Wymiar | Źródło / uwaga |
|---|---|---|
| Ściana N (szerokość) | **493 cm** | wymiar górny |
| Głębokość pokoju (N–S) | **478 cm** | wymiar lewy (pionowy) |
| Biuro — odcinek lica ściany N (lewy) | **197 cm** | wymiar „197" |
| Wnęka pod zabudowę (szerokość) | **266 cm** | wymiar „266" |
| Wnęka pod zabudowę (głębokość murowa) | **40 cm** | wymiar „040" (pionowy) |
| Odcinek N na prawo od wnęki | **~30 cm** | 493 − 197 − 266 |
| Wysokość zabudowy | **250 cm** | podana w zleceniu |

```
                          ŚCIANA PÓŁNOCNA (493 cm)
   ┌──────────────────┲━━━━━━━━━━━━━━━━━━━━━━━━━━━━┱──────┐  ← lico ściany N
   │   biurko 197 cm   ┃ wnęka murowa 266×40 cm    ┃ ~30  │
   │  (strefa biuro)   ┃ zabudowa „OR" = drzwi     ┃      │
   │                   ┃ przesuwne; wystaje 20 cm  ┃      │
   │                   ┃ do pokoju → gł. 60 cm     ┃      │
   │                                                      │
   │ KANAPA                                    ╲ WEJŚCIE  │  ← ściana E, środek
   │ (ściana W)                                  (obok TV)│
   │                                              TV ↓    │
   │                                            (poł. E)  │
   └──────────────────────────────────────────────────────┘
                          ŚCIANA POŁUDNIOWA
       (478 cm głębokość — od północy do południa)
```

Strefy funkcjonalne i orientacyjne wymiary do projektu świateł:
- **Salon (S):** południowa i środkowa część, ~4,9 × 3,3 m. Kanapa pod ścianą W, TV na ścianie E.
- **Biuro (B):** narożnik NW, ~2,0 × 1,5 m, biurko przy ścianie N (lico płaskie, 197 cm).
- **Zabudowa przesuwna (Z):** wnęka murowa N 266 × 40 cm; **zabudowa wystaje 20 cm do pokoju → gł. 60 cm**, wys. 250 cm. W środku: pralka + suszarka (sekcja prawa), bojler + półki + pion gospodarczy (sekcja lewa). Drzwi orzech, 2 panele przesuwne nachodzące na siebie (każdy ~135 cm szer.).
- **Strefa techniczna (T):** wewnątrz zabudowy — pralka 60×60 cm, suszarka 60×60 cm, bojler ~50 l Ø45 wiszący nad podłogą ~150–200 cm, półki, deska do prasowania, odkurzacz pionowy.

### 0.3 Ustalenia FAZA 0a + elementy do potwierdzenia w naturze

Rozstrzygnięte z inwestorem:

1. **„OR" = drzwi przesuwne zabudowy** — nie okno → **brak kolizji**, zabudowa 250 cm stoi bez przeszkód. ✓
2. **Wejście = ściana E, obok TV, środkowa część** → P1 (główny włącznik) przy wejściu na ścianie E; TV przesunięte na południe od drzwi; ścieżka spotów L2 (S5/S6) prowadzi od wejścia w głąb salonu. ✓

Do potwierdzenia w naturze przed wykonaniem (nie blokują projektu świateł):

3. **Symbol ◯** w rogu rysunku — przyjęto, że przyłącza wody + odpływ pralki są w **sekcji prawej** zabudowy; potwierdzić rzeczywiste położenie pionu/odpływu.
4. **Wymiar „161"** — znaczenie nieznane; nieistotny dla rozmieszczenia oświetlenia.
5. **Bojler, przyłącza wody, pion CO, wentylacja** — nie są zaznaczone na rzucie; ich położenie pochodzi ze zdjęć inspiracyjnych i `PLAN.md`. Potwierdzić w naturze (zwłaszcza dostęp serwisowy do bojlera i ewentualny pion CO, którego nie wolno zabudować na głucho).

Wysokość pomieszczenia po podwieszeniu GK: zakładam 260–270 cm (zostawiamy 10–15 cm na profil LED + przeciągnięcie kabli). Zabudowa 250 cm = równa z lub poniżej sufitu, **zostaw 5–10 cm zachowanej szczeliny między górą zabudowy a sufitem** — tam ukryjemy LED kompozycyjne nad belką.

---

## 1. Projekt oświetlenia — per strefa

### A. SALON

Trzy warstwy (zgodnie z zasadą projektową, `references/oswietlenie-katalog.md`):

**A1. Światło ogólne — wnęka LED po obwodzie sufitu**
- Profil aluminiowy **wpuszczany w GK** (typ Topmet VARIO30 lub Klus TIRA), klosz mleczny opal, montaż w ramie podsufitowej tak, żeby LED świecił w sufit (cove lighting) → odbity, miękki, bez świecenia w oczy.
- Obwód po obwodzie strefy salonu (ścina W, S, E + część N na prawo od biura). **Nie ciągnij go nad zabudową** — tam będzie osobny pas (sekcja Z).
- Długość ~12 m. Taśma **24V COB CRI≥90, 14 W/m, 3000K**. Zasilacz: 12 × 14 × 1,2 = ~200 W → wybierz Mean Well HLG-240H-24A (240 W, dimowalny 0–10V / PWM) w serwerowni, dociągnięty przewodem 2×1,5 mm² do końca profilu.
- Ściemnialny — kluczowe. Sterowanie Shelly Dimmer 0–10V lub Shelly RGBW2 / DIM2 24V.

**A2. Światło zadaniowe i punktowe — oczka podtynkowe**
- 6× oczko podtynkowe okrągłe Ø75–85 mm, **GU10 LED 6W 3000K CRI≥90**, np. AQForm Aqlux / Halla Round trim / generic z czarnym pierścieniem.
- Rozmieszczenie (od ściany N do S, środek pokoju): 2× nad strefą stolika kawowego, 2× nad przestrzenią między kanapą a TV, 2× ścieżka komunikacyjna od drzwi do salonu.
- **Nie nad TV** (refleksy w ekranie) i **nie nad środkiem kanapy** (cień na czytaniu — światło spada przez głowę).
- Zostawiamy 60–80 cm od ściany do osi oczka (efekt "wall wash" wymaga dedykowanych opraw — patrz A3, więc tu oczka klasyczne 30° beam).
- Ściemnialne (Shelly Dimmer 2 za włącznikiem).

**A3. Światło akcentowe — LED dekoracyjny w niszy TV (opcjonalnie) lub bias za TV**
- Jeżeli za TV będzie wnęka GK / szafka RTV: profil narożny LED 24V 9,6 W/m 3000K, ~1,5 m, świecący w sufit lub na ścianę za TV (bias light) → redukuje zmęczenie wzroku przy filmie.
- Zasilacz wspólny z A1 (ten sam pas 24V, osobny kanał Shelly RGBW2).
- Alternatywa: bez stałej instalacji, dorzucasz później Hue Play / Govee — wtedy zostaw tylko 1× gniazdko 230V w niszy TV na wysokości 130 cm (osobny wypust, patrz §6).

**A4. Lampka stojąca / podłogowa przy kanapie**
- Nie projektujemy stałego światła punktowego nad kanapą. **Wypust 1× gniazdko 230V przy kanapie** na lampę stojącą (np. IKEA NYMÅNE / SKAFTET z LED 3000K). Sterowanie: smart plug (Shelly Plug S) wpinany w obwód scen.

---

### B. BIURO

Biurko stoi pod ścianą N po lewej od zabudowy (~197 cm długości ściany). Oświetlenie pracy musi być **niezależne od salonu** i mieć **inną temperaturę barwową** — to świadomy zabieg: 4000K do pracy, 3000K obok do relaksu. Działa, bo strefy są wizualnie rozdzielone biurkiem od kanapy (różny kadr widzenia).

**B1. Światło zadaniowe nad biurkiem — profil LED podtynkowy liniowy**
- Profil **wpuszczany w GK** prostopadle do ściany N, długość ~120 cm, świeci w dół (klosz opal). Pozycja: 50–60 cm przed ścianą N (czyli nad środkiem biurka głębokości 60 cm).
- Taśma 24V COB CRI≥95, 19 W/m, **4000K** — neutralna do pracy, bez męczenia oczu.
- Zasilacz osobny: Mean Well LPV-35-24 (35 W) w serwerowni lub w stropie nad biurkiem.
- Ściemnialny (Shelly Dimmer) — czasem chcesz przyciemnić w trakcie video-callu.

**B2. Akcent — taśma LED w półce / nad biurkiem (opcjonalnie)**
- Jeśli nad biurkiem powstaje półka wisząca: profil narożny LED 9,6 W/m 4000K pod półką (jako podświetlenie biurka od dołu półki). Wspólny zasilacz z B1.
- Alternatywa: lampka biurkowa BenQ ScreenBar / IKEA HÅRTE z USB → tylko gniazdko, bez stałej instalacji.

**B3. Włącznik biura — osobny**
- Pojedynczy klawisz/Shelly przy wejściu do strefy biura (na ścianie N obok zabudowy lub na ścianie W blisko biurka). Sterowanie: scena "Praca" (B1 100%, A1 30%, A2 OFF) — wszystko możliwe, bo to Shelly.

**B4. Doświetlenie ogólne biura — z systemu A1/A2**
- Wnęka LED salonu (A1) na fragmencie ściany N przy biurku robi tło. Nie ciągnij osobnej wnęki LED nad biurkiem — to dwa źródła w jednym kadrze (kolizja temperatur 3000K/4000K). Wnęka A1 omija strefę biurka.

---

### C. ZABUDOWA Z DRZWIAMI PRZESUWNYMI

Tu jest najwięcej decyzji. Drzwi przesuwne nachodzą na siebie — w danym momencie połowa zabudowy jest zawsze odsłonięta, połowa zamknięta. Oświetlenie wewnątrz musi włączać się **niezależnie po lewej i po prawej stronie**, żeby nie świecić w zamkniętą połowę. Albo musi reagować na **otwarcie drzwi w konkretnej części** (kontaktrony).

**C1. LED dekoracyjny w górnej belce (nad drzwiami, od zewnątrz)**
- **TAK** — daje efekt z wizualizacji (ciepła poświata nad ciemnym orzechem). Profil LED **narożny aluminiowy** 30×30 mm montowany w szczelinie 5–10 cm między górą zabudowy (250 cm) a sufitem (~260–270 cm), świecący na sufit (nie w dół — wtedy oślepia).
- Długość 266 cm. Taśma 24V COB 9,6 W/m **3000K** CRI≥90.
- Sterowanie osobne: scena "akcent zabudowy" — często chcesz mieć włączoną tylko ją (np. wieczorem, jako jedyne światło w pokoju).
- Ściemnialny.

**C2. LED pionowy w ościeżu zabudowy (po obu stronach niszy)**
- **TAK** — widać to na drugiej wizualizacji (pionowe paski LED w ramie). Profil pionowy wpuszczany w boczne ścianki zabudowy, długość ~240 cm każdy (od podłogi do górnej belki).
- Taśma 24V 9,6 W/m **3000K** CRI≥90, opal mocny (musi mocno rozpraszać, bo widać go z bliska).
- Sterowanie razem z C1 (jeden kanał) lub osobno (gust). Domyślnie: razem.

**C3. Oświetlenie wewnętrzne zabudowy — taśmy LED ukryte**
- Dwie sekcje wewnątrz (lewa: bojler + półki gospodarcze; prawa: pralka + suszarka + półki bielizny). Każda sekcja ma osobną taśmę i osobny kontaktron.
- Profil narożny aluminiowy montowany **w narożu sufitu wnętrza zabudowy** świecący w dół, **wzdłuż przedniej krawędzi** (nie z tyłu — bo półki/sprzęty zacieniają). 
- Taśma 24V COB CRI≥90, **14 W/m, 4000K** — neutralna, do oceny kolorów ręczników/ubrań i do serwisu pralki.
- Długość: lewa sekcja ~130 cm, prawa sekcja ~130 cm. 
- Dodatkowo: pod każdą półką w lewej sekcji (~3 półki) — krótki profil COB 9,6 W/m 4000K, długość ~60 cm. Po włączeniu sekcji świeci się cała kolumna.

**C4. Logika włączania wnętrza zabudowy — kontaktrony NIE PIR**
- W zabudowie z drzwiami przesuwnymi **PIR jest bezużyteczny** — nie widzi otwarcia, widzi ruch w pomieszczeniu (fałszywe wyzwolenia). 
- Zamiast tego: **kontaktron magnetyczny w prowadnicy górnej**, jeden na panel przesuwny.
  - Panel lewy odsłania prawą sekcję → załącza taśmę C3-prawa.
  - Panel prawy odsłania lewą sekcję → załącza taśmę C3-lewa.
- Połączenie: kontaktron → wejście Shelly i4 lub Shelly UNI w stropie nad zabudową → reguła w HA: "panel X otwarty więcej niż 10 cm przez >2 s → włącz taśmę Y, fade-in 500 ms".
- Plus **fizyczny włącznik awaryjny** (klawisz) obok zabudowy — gdyby HA padło lub trzeba zostawić światło na stałe (np. malowanie wnętrza).

**C5. Półki z podświetleniem (jak na wizualizacji)**
- Półki w lewej sekcji + górne półki prawej sekcji (z ręcznikami): pod każdą półką płaski profil LED COB 4000K (parametr jak C3 dolne).
- Łączysz wszystkie półki danej sekcji w **szeregowo-równoległą sieć 24V** zasilaną z tego samego kanału co C3 tej sekcji. Jeden kontaktron włącza całą kolumnę półek + taśmę górną.

---

### D. STREFA TECHNICZNA (pralka, suszarka, bojler)

Większość światła technicznego daje C3 (wewnętrzne taśmy 4000K). Dodatkowo:

**D1. Światło serwisowe przy bojlerze**
- Bojler wisi na ścianie tylnej lewej sekcji, ~150–180 cm nad podłogą. Pod nim: zawory, tróje, przyłącza wodne, gniazdo 230V z bryzgoszczelną pokrywą.
- Dodaj **1× oczko podtynkowe IP44 GU10 LED 6W 4000K CRI≥80** w suficie zabudowy lewej sekcji, oś nad bojlerem (czyli ~30 cm od ściany tylnej). Włączane razem z C3-lewa.
- IP44 z powodu wilgoci od bojlera i mokrych ubrań suszących się obok.

**D2. Bezpieczeństwo wilgoć/temperatura**
- Wszystkie LED w lewej sekcji (technicznej): **klasa min. IP44**, profile zamknięte kloszem.
- Bojler ma swój termik i bezpieczeństwo nadciśnieniowe — światło nie ma wpływu, ale **żaden wypust 230V nie może być nad bojlerem** (skropliny). Gniazdo bojlera: 30 cm sboku, na osobnym obwodzie z B16A + różnicówka 30 mA (patrz §6).
- Pralka i suszarka: gniazda 230V za nimi na osobnych obwodach (B16A każdy + różnicówka). Nie projektujemy nad nimi światła punktowego — wystarczy taśma C3-prawa.

**D3. Dostęp serwisowy**
- Bojler trzeba czasem zdjąć ze ściany (anoda, czyszczenie). Profile LED w lewej sekcji **nie mogą być w osi przyłączy** — przesuń je do przodu (przy krawędzi półek) lub do boku.
- Pralka/suszarka — dostęp przez front, taśma górna nie przeszkadza.

---

## 2. Podział włączników i obwodów

System: **smart-first** — każdy obwód niezależny, sterowany z Shelly w puszce za klawiszem. Klawisze fizyczne dalej działają (kluczowe gdy HA padnie).

### Lista obwodów (kanałów) — to jest **lista zaciskowa dla elektryka**

| # | Nazwa obwodu | Strefa | Napięcie | Moc szczyt. | Sterowanie | Domyślny włącznik |
|---|---|---|---|---|---|---|
| **L1** | Salon — wnęka LED 3000K (A1) | Salon | 24V DC | ~170 W | Shelly RGBW2 / Dim 0–10V | klawisz lewy, ściana W przy drzwiach wejściowych + drugi klawisz przy kanapie |
| **L2** | Salon — spoty sufitowe 3000K (A2) | Salon | 230V | ~36 W (6×6W) | Shelly Dimmer 2 (triak) | klawisz prawy, obok L1 |
| **L3** | Salon — akcent TV / bias (A3) | Salon | 24V DC | ~15 W | Shelly RGBW2 (osobny kanał) | scena, klawisz opc. przy TV |
| **L4** | Biuro — światło zadaniowe 4000K (B1+B2) | Biuro | 24V DC | ~30 W | Shelly Dimmer 0–10V | klawisz osobny, ściana N obok biurka lub na ścianie W przy wejściu w strefę biura |
| **L5** | Zabudowa — LED akcent zewnętrzny 3000K (C1+C2) | Zabudowa | 24V DC | ~70 W (2,7 m C1 + 4,8 m C2 × 9,6 W/m) | Shelly Dimmer 0–10V | klawisz osobny, ściana obok zabudowy (po stronie biura) |
| **L6** | Zabudowa wnętrze LEWA + bojler oczko 4000K (C3-lewa + D1 + półki) | Techn. lewa | 24V DC + 230V (oczko) | ~50 W | Shelly UNI + kontaktron lewy panel | kontaktron + awaryjny klawisz wewnątrz zabudowy |
| **L7** | Zabudowa wnętrze PRAWA 4000K (C3-prawa + półki) | Techn. prawa | 24V DC | ~30 W | Shelly UNI + kontaktron prawy panel | kontaktron + awaryjny klawisz wewnątrz zabudowy |

**Razem: 7 niezależnych kanałów.** To minimum. Wszystkie spinasz scenami w HA.

### Sceny domowe (HA)

| Scena | L1 | L2 | L3 | L4 | L5 | L6 | L7 |
|---|---|---|---|---|---|---|---|
| **Dzień** | OFF | OFF | OFF | OFF | OFF | auto-kontaktron | auto-kontaktron |
| **Praca** | 30% | OFF | OFF | 100% | OFF | auto | auto |
| **Wieczór** | 60% | OFF | 50% | OFF | 70% | auto | auto |
| **Film** | 15% | OFF | 80% (bias) | OFF | 20% | OFF | OFF |
| **Sprzątanie / pranie** | 80% | 100% | OFF | 60% | OFF | 100% (manual) | 100% (manual) |
| **Noc / przejście** | 5% | OFF | OFF | OFF | 10% | OFF | OFF |

### Lokalizacja klawiszy fizycznych (puszek)

```
P1 (przy wejściu, ściana E obok TV, po stronie zawiasu drzwi, h=110 cm):
   ramka 3M lub 4M:
   ├── klawisz 1: L1 Salon wnęka  (krótko ON/OFF, długo dim)
   ├── klawisz 2: L2 Salon spoty  (krótko ON/OFF, długo dim)
   ├── klawisz 3: L5 Zabudowa akcent  (krótko ON/OFF, długo dim)
   └── (klawisz 4: scena "Wieczór" — opcjonalnie)

P2 (przy kanapie, na ścianie W, h=110 cm):
   ramka 2M:
   ├── klawisz 1: L1 Salon wnęka (równoległy do P1, scena via HA)
   └── klawisz 2: scena "Film"

P3 (w strefie biura, ściana N obok biurka lub ściana W, h=110 cm):
   ramka 1M:
   └── klawisz: L4 Biuro (krótko ON/OFF, długo dim)

P4 (wewnątrz zabudowy, ścianka boczna prawej sekcji, h=150 cm — bezpiecznie nad pralką):
   ramka 2M IP44:
   ├── klawisz: L6 awaryjny (override kontaktronu)
   └── klawisz: L7 awaryjny (override kontaktronu)
```

Wszystkie klawisze **na tej samej wysokości 110 cm** (zasada projektowa) i **tej samej serii** — np. Kontakt-Simon 55 czarny mat, Berker R.1 antracyt, lub Schneider Asfora czarny (do wyboru, ważne że konsekwentnie). Klawisze bez podpisów — grupowanie po położeniu.

---

## 3. Konkretne typy oświetlenia — podsumowanie z parametrami

| Typ | Gdzie | Po co | Barwa | Ściemnialne | Strefa |
|---|---|---|---|---|---|
| **Profil LED wpuszczany w GK** (Topmet VARIO30) | Wnęka po obwodzie salonu (A1) | Światło ogólne, miękkie, odbite | 3000K | TAK | Salon |
| **Profil LED wpuszczany w GK** (liniowy 120 cm) | Nad biurkiem (B1) | Światło zadaniowe do pracy | 4000K | TAK | Biuro |
| **Profil LED narożny aluminiowy 30×30** | Górna belka zabudowy (C1), pionowe boki (C2) | Akcent, mood, "premium look" | 3000K | TAK | Zabudowa zewn. |
| **Profil LED narożny w stropie zabudowy** | Wnętrze zabudowy, przy froncie (C3) | Praktyczne światło garderoby/techn. | 4000K | NIE (ON/OFF) | Zabudowa wewn. |
| **Profil LED płaski pod półkami** | Lewa + prawa sekcja, pod każdą półką | Doświetlenie półek | 4000K | NIE | Zabudowa wewn. |
| **Oczka podtynkowe GU10 Ø75–85** | 6× w salonie (A2) | Doświetlenie punktowe, ścieżki | 3000K | TAK (triak) | Salon |
| **Oczko podtynkowe IP44 GU10** | 1× nad bojlerem (D1) | Serwisowe | 4000K | NIE | Techniczna |
| **Bias LED za TV** (opc.) | Wnęka/szafka RTV (A3) | Redukcja zmęczenia wzroku | 3000K (lub RGBW) | TAK | Salon |
| **Kontaktron magnetyczny** | Górna prowadnica drzwi przesuwnych, 2 szt. | Auto-włącznik wnętrza | — | — | Zabudowa |
| **Smart plug 230V** | Lampa stojąca przy kanapie | Wpięcie do scen | — | (lampa LED) | Salon |

### Producenci / modele konkretnie do wpisania w wycenę

- **Profile aluminiowe:** Topmet (PL) — VARIO30 wpuszczany, ANGLE30 narożny, GROOVE14 płaski. Klosz **opal mleczny**.
- **Taśmy LED 24V COB CRI≥90:** LedHouse PL, Klus, lub Paulmann MaxLED 1000. Konkretnie: 14 W/m do A1/B1/C3, 9,6 W/m do C1/C2/A3/półki.
- **Zasilacze:** Mean Well HLG-240H-24A (240W, dimowalny) — wspólny dla A1+A3; LPV-35-24 dla B1; LPV-100-24 dla L5; LPV-60-24 dla L6, dla L7. Wszystkie w **serwerowni** (lub w wnęce sufitowej dostępnej przez klapę rewizyjną GK, jeśli serwerownia daleko).
- **Oczka:** AQForm Aqlux Hermetic Round albo Halla H21 Trim Round — wymiennik GU10. Czarny pierścień. Do D1: AQF Aqlux IP44.
- **Żarówki GU10:** Osram Parathom Dim PAR16 6W 3000K CRI80+, alternatywa Philips MASTER LED ExpertColor CRI97 6W 3000K (premium do salonu).
- **Kontaktrony:** dowolny NC magnetyczny 1A (Satel typu MMK-1, generic Aliexpress — to tylko styk).
- **Shelly:** Shelly Dimmer 2 (triak L2), Shelly RGBW2 24V (L1, L3), Shelly Pro DIM (L4, L5) — albo wszystko na Shelly Pro Dual Cover Shutter / Dimmer w rozdzielnicy, wtedy klawisze są tylko wejściami; do L6/L7 wystarczy Shelly UNI lub Shelly Plus 1 z wejściem dla kontaktronu.

---

## 4. Barwy światła — tablica zbiorcza

| Strefa / sekcja | Kelviny | CRI | Uzasadnienie |
|---|---|---|---|
| Salon — wnęka, spoty, bias | **3000K** | ≥90 (CRI95 do spotów premium) | Ciepłe, relaksujące, spójne z drewnem |
| Biuro — pasek nad biurkiem | **4000K** | ≥90 | Neutralne, skupienie, czytanie dokumentów |
| Zabudowa zewnętrzna (C1+C2) | **3000K** | ≥90 | Akcent ciepły, zgodny z salonem i orzechem |
| Zabudowa wnętrze (C3, półki) | **4000K** | ≥90 | Wierna ocena kolorów ubrań/ręczników, serwis pralki |
| Oczko nad bojlerem (D1) | **4000K** | ≥80 | Praktyczne, neutralne, serwisowe |

**Zasada:** w jednym kadrze widzenia z salonu (siedząc na kanapie) widzisz 3000K (wnęka, spoty, akcent zabudowy). Stojąc przy biurku widzisz 4000K nad sobą + 3000K ogólne — to dwa różne kadry, więc OK. Otwierając zabudowę widzisz 4000K wewnątrz + 3000K w belce nad belką — to też OK, bo wnętrze jest "innym pokojem".

---

## 5. Drzwi przesuwne — analiza dedykowana

Drzwi przesuwne nakładają się — w pozycji "zamknięte do lewej" odsłaniają prawą sekcję, i odwrotnie. To narzuca twarde ograniczenia:

**Co ROBIĆ:**
- **LED w górnej belce (C1)** — ukryty w szczelinie 5–10 cm między górą zabudowy a sufitem GK. Profil narożny, świeci w sufit. Nie koliduje z prowadnicą (prowadnica jest niżej, w samej belce zabudowy).
- **LED pionowy w ościeżu (C2)** — wpuszczany w boczną ściankę zabudowy (poza tor drzwi, czyli "na zewnątrz" toru przesuwu). Widoczny zawsze, niezależnie od pozycji drzwi.
- **LED wewnątrz w stropie zabudowy (C3)** — montaż **przy froncie wnętrza**, ale **tuż za płaszczyzną drzwi** (czyli ~2–3 cm od krawędzi przedniej, tak żeby drzwi przesuwając się nie zahaczały o profil ani klosz).
- **Zasilacze poza zabudową** — w sufitowej wnęce GK z klapą rewizyjną nad zabudową (lub w serwerowni). Nigdy wewnątrz zabudowy (wilgoć od suszarki/bojlera, ciepło, brak przepływu powietrza).
- **Kable LED przez górną belkę zabudowy** — wyprowadź wypust 24V z sufitu GK do zabudowy przez **przepust kablowy w plecach lub w suficie zabudowy**, ukryty z góry. Nigdy przez front ani bok.

**Co BEZWZGLĘDNIE NIE:**
- Brak LED-ów na froncie drzwi przesuwnych (drzwi się ruszają, kable się zerwą).
- Brak światła w torze prowadnicy (kolizja mechaniczna).
- Brak PIR-ów w zabudowie (fałszywe wyzwolenia od ruchu w pokoju).
- Brak gniazd 230V wewnątrz zabudowy w osi otwierania drzwi (kable się ścierają).

**Dostęp serwisowy:**
- Klapa rewizyjna 30×30 cm w suficie GK **bezpośrednio nad zabudową** — dostęp do zasilaczy A1+A3+C1+C2.
- Druga klapa nad biurkiem dla L4.
- Trzecia klapa w salonie (najlepiej w okolicy gdzie nie patrzysz) — rezerwa.
- Profile LED w zabudowie — odkręcane od spodu (śruby do GK / mebla), klosze typu klick.

---

## 6. Praktyczne rozmieszczenie instalacji (wypusty, puszki, zasilanie)

### 6.1 Wypusty 230V (do elektryka — co przygotować w GK / ścianie)

| Wypust | Lokalizacja | Co zasila | Obwód (CB w rozdzielnicy) |
|---|---|---|---|
| W1 | Sufit, centralnie nad osią salonu N-S | Spoty A2 (×6, łączone w stropie) | L2 (B10A) |
| W2 | Sufit, nad biurkiem | Profil B1 — zasilacz 24V w stropie lub w serwerowni | L4 (B10A) |
| W3 | Sufit, nad zabudową | LED C1/C2 (zasilacze obok) | L5 (B10A) |
| W4 | Sufit, w zabudowie (strop wewn.) | LED C3 + D1 oczko | L6, L7 (każdy B10A) |
| W5 | Ściana niszy bojlera, h=160 cm, IP44 z klapą | **Bojler 230V** | osobny obwód B16A + RCD 30 mA |
| W6 | Za pralką, h=120 cm | **Pralka** | osobny obwód B16A + RCD 30 mA |
| W7 | Za suszarką, h=120 cm | **Suszarka** | osobny obwód B16A + RCD 30 mA |
| W8 | Ściana E przy TV, h=130 cm (4-krotne) + h=30 cm (2-krotne) | TV + soundbar + konsola + rezerwa | obwód salon-gniazda B16A + RCD |
| W9 | Ściana W za kanapą, h=30 cm (6-krotne) | Kanapa + lampa stojąca | jak W8 |
| W10 | Biurko (ściana N), h=80 cm (4-krotne + RJ45×2) | Komputer + monitor + ładowarki | osobny obwód biuro-gniazda B16A |
| W11 | Wewnątrz zabudowy lewej, h=30 cm | Rezerwa (odkurzacz pionowy ładujący) | wspólny z W6/W7 lub osobny |

### 6.2 Niskie napięcie (12/24V) — przewody LED

**Cała magistrala 24V:** 2×1,5 mm² (LiYY lub OMY) od zasilaczy do końców profili. Maks. spadek napięcia 5% na 5 m — przy 24V to ok.

Trasy:
- **A1 (12 m wnęka salon):** zasilacz w stropie/serwerowni → 2 wyjścia (środek-lewo, środek-prawo) → po 6 m taśmy każda nogą, żeby zminimalizować spadek napięcia. Albo zasilanie z obu końców (jeszcze lepiej).
- **B1 (1,2 m biuro):** krótko, jeden punkt zasilania.
- **C1+C2 (zabudowa zewn., ~7,5 m razem):** wspólny zasilacz, dwa wyjścia (C1 belka, C2 pion + drugi pion). Łączysz równolegle.
- **C3-lewa + półki + D1:** zasilacz dedykowany, sterowany przekaźnikiem ze Shelly UNI. D1 oczko 230V — osobny przewód 3×1,5 do oczka, ale **załączane logicznie razem** z LED (Shelly UNI ma dwa kanały — jeden 24V, drugi 230V).
- **C3-prawa + półki:** analogicznie.

### 6.3 Puszki — co przygotować

- **P1 (główna, przy drzwiach wejściowych):** głęboka puszka pod 3–4 modułowy klawisz + miejsce na 3× Shelly za nim (L1, L2, L5). Doprowadź **N (neutralny)** — Shelly wymaga.
- **P2 (przy kanapie):** głęboka puszka 2M, Shelly 1× lub i4.
- **P3 (biuro):** puszka 1M, Shelly 1× Dimmer.
- **P4 (wewnątrz zabudowy IP44):** puszka 2M na klawisze awaryjne L6/L7, dodatkowo Shelly UNI dla kontaktronów.
- **Puszki w stropie:** przy każdym zasilaczu LED (klapa rewizyjna).

### 6.4 Sieć — RJ45

Skoro robisz serwerownię, ciągnij Cat6 do każdej istotnej strefy:
- 2× RJ45 za TV (W8)
- 2× RJ45 przy biurku (W10)
- 1× RJ45 w serwerowni do każdej Shelly (opcja, jeśli Shelly LAN, np. Pro Series — Wi-Fi też wystarczy w domu)

### 6.5 Smart vs klasyka — rekomendacja dla Ciebie

Robisz HA, więc:
- **Shelly Pro DM 2PM w rozdzielnicy** (2 kanały dimowane 230V) — do L2 (spoty) + L5 (LED akcent przez konwerter 0–10V → 24V dimowalny). Albo Shelly Pro Dual Cover.
- **Shelly Plus 0–10V Dimmer** w stropie/serwerowni do A1, B1 (sterują zasilaczem dimowalnym 0–10V Mean Well HLG-D).
- **Shelly UNI** wewnątrz zabudowy do L6/L7 + kontaktronów (8 zł kontaktron + Shelly = 80 zł kanał).
- **Klawisze** są wejściami SW do Shelly — żaden klawisz nie steruje bezpośrednio obciążeniem, wszystko przez przekaźniki/dimmer. To pozwala scenom HA przejmować pełną kontrolę.

---

## 7. Wariant 1 (prosty/tani) vs Wariant 2 (premium/smart)

### Wariant 1 — Prosty

- Klasyczne włączniki triakowe (Berker R.1 / Asfora), bez Shelly.
- **L1 wnęka salon 3000K** — taśma 14W/m, 1 zasilacz, 1 ściemniacz triakowy lub LED-PWM 24V z pokrętłem.
- **L2 spoty salon (6 szt.)** — GU10 LED ściemnialne, 1 ściemniacz.
- **L4 biuro** — pasek lub plafon liniowy LED 4000K, klasyczny włącznik (ON/OFF), bez ściemniania.
- **L5 zabudowa akcent (belka + piony)** — 1 ściemniacz, wspólny obwód.
- **L6/L7 wnętrze zabudowy** — **bez kontaktronów**, klasyczne włączniki w środku zabudowy (po jednym klawiszu IP44 w każdej sekcji). Wchodzisz → klikasz → świeci.
- **Bez bias TV (A3).**
- Brak scen, brak HA.

**Plus:** taniej (~3000–4500 zł oświetlenie netto materiał + montaż 2500 zł).  
**Minus:** trzeba pamiętać o klikaniu w garderobie, brak automatyki, brak scen. Mniej "premium" w użytkowaniu.

### Wariant 2 — Premium / smart (rekomendowany dla Ciebie, bo masz HA)

- Wszystko jak w §1–§6 powyżej: 7 kanałów Shelly, kontaktrony, sceny w HA, bias TV, profile premium Topmet, COB CRI≥90, klosze opal.
- Profile aluminiowe wpuszczane (nie natynkowe).
- Mean Well dimowalne 0–10V.
- Klawisze są wejściami logicznymi do scen, nie bezpośrednio do obciążenia.
- Ściemnialność na wszystkim co ma sens (L1, L2, L4, L5, A3).
- Sceny: Dzień / Praca / Wieczór / Film / Sprzątanie / Noc.

**Plus:** życie codzienne dużo wygodniejsze, każde światło ma swoją funkcję, kontaktrony w zabudowie to luksus codzienny.  
**Minus:** drożej (~6000–9000 zł materiał + 4000 zł montaż), więcej czasu na konfigurację HA (ale ty to lubisz).

---

## 8. Rekomendacja końcowa

**Idź w Wariant 2.**

Powód: masz już serwerownię i robisz HA — koszt wejścia w smart-light w tej instalacji jest marginalny (Shelly to 60–150 zł / kanał, kontaktron 8 zł), a zysk codzienny ogromny:
1. **Kontaktrony w zabudowie** to nie gadżet — w realnym życiu jest to różnica między "świecę dwoma latarkami z telefonu szukając proszku" a "otwieram, świeci jak w sklepie, biorę, zamykam, gaśnie". Pralka i bojler są w jednym miejscu — będziesz tam wchodzić codziennie.
2. **Scena "Praca" osobno od "Wieczór"** — to dwie kompletnie różne sytuacje świetlne w jednym pomieszczeniu. Bez scen się w tym pogubisz (biuro 4000K + salon 3000K naraz wymaga osobnych klawiszy *zawsze*).
3. **Wnęka LED 3000K po obwodzie** + bias TV + akcent zabudowy = jedyne 3 źródła które będą włączone wieczorem przez 80% czasu. Reszta (spoty A2, biuro B1) ON tylko sytuacyjnie.
4. **Drzwi przesuwne wręcz wymagają smart-logiki** — pojedyncze klawisze byłyby toporne (musisz dotrzeć do klawisza za drzwiami, których jeszcze nie otworzyłeś). Kontaktron rozwiązuje to elegancko.
5. Stać Cię na to dlatego że **wszystkie 7 kanałów ciągniesz raz, w stropie GK który i tak robisz**. Dokładanie później oznacza zrywanie GK.

Jeden kompromis: **L6/L7 mogą startować jako klasyczne klawisze IP44**, a kontaktrony dorzucisz później (zostaw przewód kontaktronowy zaślepiony w prowadnicy + Shelly UNI w puszce P4 — gotowy do podpięcia). To bezpieczna ścieżka rozwoju, ale jeśli i tak robisz HA — od razu pełna wersja.

**Stylistyka:** dla orzechowej zabudowy + kremowego wnętrza + ciepłego LED 3000K na zewnątrz / 4000K wewnątrz: gama temperatur jest spójna z wizualizacjami które przysłałeś. Nie kombinuj z RGB w salonie (poza biasem TV) — w docelowym wnętrzu z ciemnym drewnem 3000K wygląda dojrzale, RGB-walka kolorów się gryzie.

---

## 9. Lista dla elektryka — to przekazujesz, nic więcej nie trzeba tłumaczyć

```
PRZEWODY DO POŁOŻENIA:
- 7× obwód LED/oświetlenie sygnalizowany w stropie GK (L1–L7), każdy 3×1,5 mm² (L/N/PE) od rozdzielnicy do puszki sterującej
- 3× obwód gniazda dedykowane: bojler (W5), pralka (W6), suszarka (W7), każdy 3×2,5 mm² + RCD 30 mA, B16A
- 2× obwód gniazda salon (W8 + W9), 3×2,5 mm², B16A
- 1× obwód gniazda biuro (W10), 3×2,5 mm², B16A
- Cat6 z serwerowni: 2× za TV, 2× biurko, opc. po jednym do każdej Shelly Pro

WYPUSTY SUFITOWE:
- 6× wypust 230V pod oczka GU10 (salon, rozmieszczenie wg §1.A2)
- 1× wypust 230V pod oczko IP44 GU10 (w stropie zabudowy lewej, nad bojlerem)
- 1× wypust + przepust kabla 24V w stropie nad zabudową (klapa rewizyjna 30×30)
- 1× wypust + klapa rewizyjna w stropie nad biurkiem
- 1× wypust + klapa rewizyjna w stropie centrum salonu (rezerwa)

PROFILE LED (frezowanie w GK):
- 12 m profilu wpuszczanego po obwodzie salonu (omija strefę biurka 197 cm)
- 1,2 m profilu wpuszczanego nad biurkiem, prostopadle do ściany N
- 266 cm profilu narożnego w szczelinie nad zabudową (świeci w sufit)
- 2× 240 cm profilu pionowego wpuszczanego w boczne ścianki zabudowy (po wewnętrznej stronie ramy)
- W zabudowie (po stronie meblarza): profile w stropie wnętrza + pod każdą półką lewej + górnymi półkami prawej sekcji

PUSZKI POGŁĘBIONE (na Shelly):
- P1: 4-modułowa przy drzwiach wejściowych, h=110 cm
- P2: 2-modułowa przy kanapie, h=110 cm
- P3: 1-modułowa w strefie biura, h=110 cm
- P4: 2-modułowa IP44 wewnątrz zabudowy prawej sekcji, h=150 cm
- N (neutralny) DO KAŻDEJ puszki — Shelly wymaga

KONTAKTRONY:
- 2× magnetyczny NC, montaż w górnej prowadnicy drzwi przesuwnych (jeden na panel)
- Przewód 2×0,5 mm² z kontaktronu do puszki P4

UWAGI:
- Wszystkie włączniki na h=110 cm, jedna seria w całym pomieszczeniu
- Klapy rewizyjne w stropie GK nad każdym zasilaczem LED
- Zasilacze LED 24V w serwerowni LUB w stropie (klapa rewizyjna), nigdy w meblu
- Bojler — gniazdo IP44, h=160 cm, z dala od osi pionowej bojlera (skropliny)
- LED w zabudowie — minimum IP44 w lewej sekcji (wilgoć)
```

---

## Verification (jak sprawdzić, że projekt się broni przed wykonaniem)

1. **Krok stołkowy po pomieszczeniu z planem w ręce:** dla każdej z 7 scen z §2 wyobraź sobie wieczór/pracę/film — czy wszystkie potrzebne źródła można odpalić jednym ruchem? Jeśli nie — dodaj klawisz/scenę.
2. **Test kolizji drzwi przesuwnych:** zmierz w meblach (po zamówieniu u Korner / stolarza) gdzie biegnie górna prowadnica drzwi vs. gdzie planujesz LED C1 i C3. Bezpieczny odstęp ≥ 3 cm.
3. **Test ciepła zasilaczy:** każdy zasilacz LED w stropie GK potrzebuje ≥10 cm wolnej przestrzeni wokół. W serwerowni daj im wspólną półkę z wentylacją.
4. **Test obciążenia obwodów:** L1 (170 W) + L5 (70 W) + bias L3 (15 W) = 255 W na ~16 A obwodzie z B16A — OK z dużym zapasem. Pralka + suszarka **muszą** być na osobnych obwodach (do 2 kW każda, plus startowe przeciążenie pralki).
5. **Test scen w HA przed zamknięciem GK:** zanim elektryk zamknie sufit, podepnij prowizorycznie 1 m taśmy do każdego kanału Shelly i przetestuj sceny. Po zamknięciu GK zmiana okablowania jest droga.
6. **Test RA90+ palcem na żywej taśmie:** kup 1 m testowy z drogerii kolorów (Topmet sample), połóż obok wzornika tkanin i drewna z mieszkania — jeśli kolory bije w zielone/żółte, zwracaj i bierz CRI95+ od Klus / Paulmann.

---

> **Uwaga końcowa do elektryka, którą warto przekazać razem z planem:**  
> *„Projekt jest pod smart-home (Shelly w puszkach + zasilacze Mean Well w serwerowni). Każdy obwód oświetleniowy musi być NIEZALEŻNY — nie łącz L1 z L2 ani L4 z L5 w rozdzielnicy. W każdej puszce musi być przewód neutralny (N) — bez tego Shelly nie zadziała. Pralka, suszarka, bojler — każde na własnym obwodzie 16A z różnicówką 30 mA. Wszystkie klawisze na wysokości 110 cm, ta sama seria. Wypusty LED wyprowadzaj z klapami rewizyjnymi w GK — zasilacze muszą być dostępne bez kucia sufitu.”*
