# Audyt skilli wnętrzarskich (kuchnie / meble na wymiar / architektura wnętrz)

Data: 2026-08-11 · Tryb: read-only (żaden plik skilla nie został zmodyfikowany) · Zakres: `~/.claude/skills/synced/`, `skills/` w repo `architekt-wnetrz` (plugin). Katalogi `/mnt/skills/user` i `/mnt/skills/plugins` nie istnieją w tym środowisku; `/mnt/skills/public|examples` nie zawierają nic wnętrzarskiego.

---

## Podsumowanie — najostrzejsze wnioski

1. **Zły dostawca w 6 miejscach — i to głębiej niż podejrzewasz.** Wszystkie skille wskazują `korner.eu` = **Poli-Eco Tworzywa Sztuczne** (producent listew przypodłogowych PVC, ul. Zwycięzców 7, **Żary**). Właściwa hurtownia płyt/okuć z cięciem CNC to **korner.pl** (Korner Sp. z o.o., centrala **Strzałków k. Radomska**, usługa cięcia online KornerGo). Wniosek: etykieta „Korner (Żary)" w skillach najprawdopodobniej w całości pochodzi z adresu **niewłaściwej firmy** — do weryfikacji jest nie tylko domena, ale i miasto/oddział, z którego realnie zamawiasz.
2. **`meble-architekt` jest strukturalnie zepsuty**: nakazuje czytać `references/korner-katalog.md`, `references/standardy-meble.md`, `references/workflow-zapytania.md` i `references/cloudflare-worker.md` — **żaden z tych plików nie istnieje w jego katalogu** (istnieją tylko w pluginie, do którego ten skill nie należy). Skill działa wyłącznie na tym, co ma w SKILL.md.
3. **`meble-architekt` w części kuchennej jest gorszą, starszą wersją `architekt-kuchni`** — bez protokołu analizy zdjęć, bez statusów wymiarów `[P]/[~]/[?]`, bez twardych progów układów, bez listy pomiarów kontrolnych. Ma jednak unikaty (szafy/garderoby/TV/łazienka meblowo, format listy formatek, plan montażu). Rekomendacja: **rozebrać i usunąć** (szczegóły w §6).
4. **„Kuchnia na wymiar" odpala loterię 3 skilli** — fraza jest w description wszystkich trzech. `architekt-kuchni` ma anty-trigger na `architekt-wnetrz`, ale `architekt-wnetrz` i `meble-architekt` nie wiedzą o `architekt-kuchni` w ogóle. Ryzyko: kuchnię obsłuży płytszy skill.
5. **Duplikat `architekt-kuchni` potwierdzony** (kopia user-level `synced/` vs kopia w pluginie) — treść merytoryczna dziś identyczna, ale sekcja references **już się rozjechała** (inne ścieżki, wersja pluginowa ma dodatkowy akapit fallback, wersja synced ma 5 plików skopiowanych 1:1, 54 KB). Brak mechanizmu synchronizacji = rozjazd merytoryczny to kwestia czasu.
6. **Stałe techniczne się rozjechały**: spiek na blat to wg `meble-architekt` „38–40 mm", a wg `technologia-wykonania.md` i `korner-katalog.md` — poprawnie — „12–20 mm na podkonstrukcji". Orzech Royal to raz Egger **H3702** (korner-katalog), raz **H3734 ST9** (architekt-kuchni SKILL). Nomenklatura Blum jest błędna w dwóch plikach („Legrabox **H**=192" — bok o symbolu H nie istnieje; realnie M≈90,5 / K≈128,5 / C≈193 mm).
7. **Żaden skill nie wyprodukuje listy formatek, po której stolarz potnie bez dopytywania.** `meble-architekt` obiecuje tabelę formatek, ale nigdzie nie ma **metody** jej wyliczenia (odliczenia korpusu, plecy wpuszczane/nakładane, front = światło − fugi, obrzeże per krawędź, słoje per formatka). `architekt-kuchni` uczciwie odmawia formatek bez pomiarów (dobra decyzja), ale metody też nie ma. To jest **największa merytoryczna dziura zestawu**.
8. **Zero dostawców lokalnych.** `dostawcy.md` (13 KB, solidny plik) nie zawiera ani jednego dostawcy śląskiego — brak Daedalus, brak Akces, brak logistyki/kosztów dostawy formatek. Dla użytkownika z Zabrza domyślny dostawca „z Żar" (patrz pkt 1 — być może błędnie przypisane miasto) to 350–400 km.
9. **Wizualizacje są pokryte trzykrotnie, produkcja — wcale.** Logika generacji obrazów (4 ścieżki, zakazane słowa, 5-komponentowy prompt, tabela błędów) jest zduplikowana w 3 skillach w ~90% identycznej treści. Jednocześnie w repo leży działający kod rzutów SVG (`projects/kuchnia-9.02/gen.py`, `_render.py`) **niepodpięty do żadnego skilla**.
10. **Hardcode'y środowiskowe w skillach**: ścieżka `C:/Users/PC/.claude/plugins/...` (Windows konkretnego komputera), placeholder `https://meble-banana.<subdomen>.workers.dev`, model `gemini-3.1-flash-image-preview` — wszystko to wymaga parametryzacji albo się cicho wysypie.

---

## 1. Inwentaryzacja

| # | Skill | Źródło / ścieżka | SKILL.md | Pliki pomocnicze | Uwagi |
|---|---|---|---|---|---|
| 1 | **architekt-kuchni** | user (`~/.claude/skills/synced/architekt-kuchni/`) | 10 431 B | 10 × references: 5 własnych (26,2 KB: analiza-pomieszczenia 5,3 / uklady-kuchni 5,1 / technologia-wykonania 6,1 / dokumentacja-stolarz 4,3 / prompty-wizualizacyjne 5,4) + 5 **skopiowanych 1:1 z pluginu** (54,1 KB: standardy-meble 7,1 / korner-katalog 8,0 / dostawcy 13,4 / instalacje-elektryka 10,7 / style-aesthetics 14,9) | **Aktywny w tej sesji.** Duplikat wpisu #4 |
| 2 | **meble-architekt** | user (`~/.claude/skills/synced/meble-architekt/`) | 16 567 B | **0** — katalog references nie istnieje, mimo że SKILL.md deklaruje 4 pliki | **Aktywny w tej sesji.** Martwe odwołania |
| 3 | **architekt-wnetrz** | plugin (`skills/architekt-wnetrz/` w repo; `.claude-plugin/plugin.json` v1.1.0) | 33 284 B | 9 × references, 90,9 KB (dostawcy 13,4 / instalacje-elektryka 10,7 / korner-katalog 8,0 / oswietlenie-katalog 15,1 / podlogi-sciany-sufity 12,1 / standardy-meble 7,1 / style-aesthetics 14,9 / workflow-zapytania 5,5 / cloudflare-worker 4,1) | **Nieaktywny w tej sesji** (plugin niezainstalowany tutaj) |
| 4 | **architekt-kuchni** (duplikat) | plugin (`skills/architekt-kuchni/` w repo) | 10 885 B | 5 własnych references (26,2 KB) — współdzieli 5 przez `../architekt-wnetrz/references/` | Duplikat wpisu #1 |

**Weryfikacja hipotezy użytkownika:** potwierdzona w 3/4 i skorygowana w 1/4. Istnieją: `architekt-kuchni` ✓, `meble-architekt` ✓, `architekt-wnetrz` (plugin) ✓. Duplikat `architekt-kuchni` istnieje ✓, ale nie jest to „drugi egzemplarz wewnątrz pluginu" — plugin ma **jeden** egzemplarz; duplikatem jest kopia user-level w `synced/`. W sesji z zainstalowanym pluginem będą aktywne **dwa skille o nazwie `architekt-kuchni` naraz** (user + plugin), co jest realnym ryzykiem niedeterministycznego triggera.

### Deklarowane triggery (z description)

| Skill | Triggery | Anty-triggery |
|---|---|---|
| architekt-kuchni | projekt kuchni, zabudowa kuchenna, **kuchnia na wymiar**, analiza zdjęć kuchni, rozpiska szafek, projekt dla stolarza, ergonomia kuchni, strefy kuchenne, trójkąt roboczy, rozmieszczenie AGD, zabudowa lodówki, wyspa kuchenna, półwysep, kuchnia w L/U, prompt do wizualizacji kuchni, kuchnia Kornel, **kuchnia Korner** | „NIE aktywuj do pełnego projektu mieszkania ani innych pomieszczeń — to skill architekt-wnetrz" |
| meble-architekt | projekt mebli, **meble na wymiar**, **kuchnia na wymiar**, **szafa na wymiar**, **garderoba**, **rzuty**, **wizualizacja**, plan budowy, **Korner**, **lista zakupów**, cięcie płyt, formatki; scope: kuchnia, szafa, łazienka, garderoba, TV, biuro, regały | **brak** — nie wie o istnieniu pozostałych dwóch |
| architekt-wnetrz | projekt mieszkania, zaprojektuj pokój, urządzić salon/sypialnię/łazienkę/**kuchnię**, mieszkanie pod klucz, moodboard, oświetlenie, plan elektryczny, gniazdka, podłoga, mikrocement, farby, tapeta, **meble na wymiar**, **kuchnia na wymiar**, **szafa na wymiar**, **garderoba**, **Korner**, **rzuty**, layout, **wizualizacja**, render wnętrza, **lista zakupów**, kosztorys, harmonogram remontu | **brak** — description nie deleguje kuchni do architekt-kuchni (robi to tylko plugin.json, którego model nie widzi przy triggerowaniu) |

---

## 2. Macierz pokrycia (skill × etap pipeline'u)

Legenda: **P** = PEŁNE, **C** = CZĘŚCIOWE, **B** = BRAK. Oceniane wg treści, nie deklaracji.

| Etap | architekt-kuchni | meble-architekt | architekt-wnetrz | Komentarz |
|---|---|---|---|---|
| 1. Analiza zdjęć/szkicu | **P** (protokół per zdjęcie, sklejanie widoków, model ASCII) | **C** („opisz w 2–3 zdaniach co widzisz") | **C** (Faza 0a — tylko rysunki techniczne, brak protokołu zdjęć) | najlepszy fragment całego zestawu jest w architekt-kuchni |
| 2. Pomiary i weryfikacja wymiarów | **P** (`[P]/[~]/[?]`, sprzeczności, 12-pozycyjna lista pomiarów stolarza) | **B** (brak statusów, brak listy pomiarów) | **C** (tabele braków w 0a, bez statusów) | |
| 3. Koncept / układ (L, U, wyspa) | **P** (uklady-kuchni.md: twarde progi, odrzucanie z matematyką, min. 2 warianty) | **C** (brak progów — wyspę „upchnie") | **C** (layout mieszkania ogólny, kuchnia bez progów w SKILL) | |
| 4. Ergonomia i strefy | **P** (strefy, trójkąt 3600–7000, przejścia, otwieranie AGD) | **C** (tylko normy bezpieczeństwa okap/lodówka/zlew) | **C** (Faza 2c: korytarze, trójkąt „max 7 m") | |
| 5. Rzuty techniczne | **C** (ASCII) | **C** (ASCII) | **C** (ASCII) | nikt nie generuje rzutów wymiarowanych (SVG/CAD); gotowy kod `gen.py` leży w `projects/` niepodpięty |
| 6. Elewacje / przekroje | **C** (elewacje ASCII per ściana, pkt 6 szablonu) | **C** (elewacja + 1 przekrój ASCII) | **C** (deleguje wzór do 5a) | |
| 7. Rozpiska korpusów i frontów | **P** (pkt 7–8 szablonu: numeracja D/G/S, tabela modułów) | **P** (tabela modułów M01…) | **C** (powiela wzór meble-architekt w 5a) | poziom ofertowy — OK |
| 8. Lista formatek (cięcie, obrzeże) | **C→B** (świadomie odmawia bez pomiarów — słusznie; ale metody wyliczenia brak) | **C** (format tabeli F01… jest, **metody wyliczenia brak**) | **B** (odsyła do meble-architekt) | **dziura krytyczna** — patrz §5 |
| 9. Okucia / AGD | **P** (standardy-meble: wymiary otworów AGD; korner-katalog: Blum/Hettich/GTV) | **C** (Blum/Hettich w house style, bez katalogu — martwy reference) | **C** (przez references) | brak liczenia okuć per front (ile zawiasów, pozycje) |
| 10. Plan elektryczny / instalacje pod meble | **C** (przez instalacje-elektryka.md + technologia §3) | **C** (jedna linijka w notatkach) | **P** (instalacje-elektryka.md: wysokości, obwody 16/32A, wod-kan, gaz, wentylacja) | |
| 11. Wizualizacja (prompt do generatora) | **P** (najlepsze: geometria, kamera, blok zakazów, kontrola zgodności renderu) | **P** (4 ścieżki, aspect-ratio routing, error handling) | **P** (moodboard + 5–8 renderów) | **potrójna redundancja** |
| 12. Plan montażu | **B** (produktem jest projekt dla stolarza + pomiary, montażu nie rozpisuje) | **C** (Faza 4: szablon kroków, punkty krytyczne) | **C** (harmonogram robót, nie instrukcja montażu) | |
| 13. Lista zakupów u dostawcy | **C** (Korner-first, bez formatu listy) | **P** (Faza 5: formatki/fronty/HDF/okucia/LED + koszt) | **P** (8b–8e: multi-vendor + gotowe wiadomości e-mail) | |
| 14. Kosztorys | **C** (widełki, zero danych cenowych) | **C** (X–Y zł — puste widełki) | **C** (tabela kategorii, przykładowe kwoty bez podstaw) | **nikt nie ma cen referencyjnych** (zł/m² płyty, zł/kpl Legrabox) |
| 15. Harmonogram | **B** | **C** (3 linijki „czas realizacji") | **P** (Gantt ASCII + harmonogram zamawiania T-12…T-1) | |

**Etapy z zerowym lub prawie-zerowym pokryciem w całym zestawie:**
- **metoda wyliczania formatek** (moduł → formatki netto z odliczeniami) — 0/3,
- **plan rozkroju / optymalizacja arkuszy** (2800×2070) — 0/3,
- **specyfikacja wierceń** (system 32, pozycje puszek zawiasów, prowadnic) — 0/3,
- **realne dane cenowe do kosztorysu** — 0/3,
- **rzuty wymiarowane w formacie graficznym** (SVG/PDF) — 0/3 jako część skilla (kod istnieje w `projects/`).

---

## 3. Kolizje i duplikacja

### 3a. Kolizje triggerów

Frazy w konflikcie (dokładne słowa-klucze z description):

| Fraza | Skille | Ryzyko |
|---|---|---|
| **kuchnia na wymiar** | wszystkie 3 | najwyższe — użytkownik piszący dokładnie to, czego dotyczy najgłębszy skill, może dostać dowolny z trzech |
| **Korner** / kuchnia Korner | wszystkie 3 | j.w. |
| meble na wymiar | meble-architekt + architekt-wnetrz | średnie |
| szafa na wymiar, garderoba | meble-architekt + architekt-wnetrz | średnie |
| rzuty, wizualizacja, lista zakupów | meble-architekt + architekt-wnetrz | frazy zbyt generyczne jak na trigger — złapią też intencje spoza domeny mebli |
| urządzić kuchnię / projekt kuchni | architekt-wnetrz + architekt-kuchni | architekt-kuchni ma anty-trigger, architekt-wnetrz nie ma — rozstrzyganie jednostronne |
| łazienka | meble-architekt (scope) + architekt-wnetrz | architekt-kuchni jawnie wyklucza — jedyny, który to robi |

Dodatkowa kolizja instalacyjna: przy zainstalowanym pluginie + skillach user-level w tej samej sesji działają **dwa `architekt-kuchni`** i (jeśli synced zawiera też meble-architekt) trzy skille bijące się o „kuchnia na wymiar".

### 3b. Zduplikowane fragmenty treści

**(1) architekt-kuchni synced vs plugin — diff rzeczywisty** (jedyne różnice w SKILL.md; references własne różnią się analogicznie tylko ścieżką w 1 linii; 5 współdzielonych references skopiowanych **bajt w bajt**):

```diff
- (synced, linia 51/53):  **`references/standardy-meble.md`** (współdzielone — nie duplikuj)
+ (plugin, linia 51/53):  **`../architekt-wnetrz/references/standardy-meble.md`** (współdzielone — nie duplikuj)

- (synced, sekcja references): Przejęte ze skillu architekt-wnetrz (dołączone do tej paczki):
+ (plugin):                    Współdzielone ze skillem architekt-wnetrz (ten sam plugin — nie kopiuj, czytaj stamtąd):
+ (tylko plugin):              Jeśli współdzielony plik jest niedostępny (skill zainstalowany pojedynczo, poza
+                              pluginem) — powiedz to wprost i stosuj wartości z references/uklady-kuchni.md
+                              i references/technologia-wykonania.md, które zawierają minimum krytyczne.
```

Czyli: dziś zgodne merytorycznie, **już rozjechane redakcyjnie** (wersja synced nie ma akapitu fallback). Każda przyszła poprawka wymaga ręcznej podwójnej edycji — to się nie utrzyma.

**(2) House style — 4 kopie, 1 rozjazd twardy:**

| Miejsce | Treść bloku | Rozjazd |
|---|---|---|
| meble-architekt (linie 14–24) | Orzech Royal + kremowy + czarne listwy 12 mm + LED 3000K + Blum/Hettich + cokół 100 | **„Blaty: kamień ciemny matowy lub spiek czarny mat, gr. 38-40mm"** — spiek 38–40 mm nie istnieje na rynku (spieki: 4/12/20 mm) |
| architekt-wnetrz (linie 29–39) | j.w. bez grubości blatu | — |
| architekt-kuchni (linia 13) | j.w. + **„Egger H3734 ST9 Pacific Walnut"** | koliduje z korner-katalog |
| korner-katalog.md / style-aesthetics.md | „Orzech Royal / Orzech Pacific — **Egger H3702** lub odpowiednik"; „spiek 12–20 mm na podkonstrukcji" | koliduje z architekt-kuchni SKILL |

**(3) Blok generacji obrazów — 3 kopie ~90% identyczne:** meble-architekt Faza 3 (≈100 linii) ≈ architekt-wnetrz Faza 7 (≈80 linii) ≈ architekt-kuchni „Generacja obrazów" (10 linii, skompresowana). Identyczne: 4 ścieżki detekcji (MCP → Python → Worker → manual), lista słów zakazanych, 5-komponentowa formuła, tabela błędów (IMAGE_SAFETY/429/FAILED_PRECONDITION/API_KEY_INVALID), kotwice „Architectural Digest / Dezeen". Trzy miejsca do aktualizacji przy każdej zmianie API.

**(4) Struktura briefu mebla:** architekt-wnetrz Faza 5a to skrót Fazy 2 meble-architekt (te same 4 punkty, ta sama kolejność), a 8b mówi wprost „dokładnie jak w skillu meble-architekt".

### 3c. Spójność delegacji (dwustronność)

| Relacja | A → B | B → A | Werdykt |
|---|---|---|---|
| architekt-kuchni → architekt-wnetrz | ✓ (tabela „Relacja z innymi skillami" + anty-trigger) | ✗ — SKILL.md architekt-wnetrz **ani razu nie wymienia architekt-kuchni**; sam obsługuje kuchnie (Faza 5a) i triggeruje się na „kuchnia na wymiar" | **jednostronna** — orchestrator nie wie o specjaliście |
| architekt-wnetrz → meble-architekt | ✓✓ („taka sama jak w skillu meble-architekt", „dokładnie jak w skillu meble-architekt") | ✗ — meble-architekt nie zna nikogo | **jednostronna i wisząca**: meble-architekt nie należy do pluginu, więc u użytkownika pluginu te odwołania wskazują skill, którego może nie być |
| meble-architekt → references | deklaruje 4 pliki | pliki **nie istnieją** w jego katalogu | **martwa** |
| architekt-kuchni ↔ meble-architekt | ✗ / ✗ | | dwa skille o pokrywającym się rdzeniu (kuchnia) wzajemnie o sobie nie wiedzą |

---

## 4. Spójność merytoryczna — twarde sprawdzenie

### 4a. Dostawcy

**Wystąpienia domen:** `korner.eu` — 6× (meble-architekt SKILL:8; architekt-kuchni SKILL:12 ×2 kopie; korner-katalog.md:1 ×2 kopie; architekt-wnetrz SKILL:12). `korner.pl` — **0×**.

Stan faktyczny (zweryfikowany 2026-08-11):
- **korner.eu** = marka Poli-Eco Tworzywa Sztuczne Sp. z o.o., ul. Zwycięzców 7, 68-200 **Żary** — producent **listew przypodłogowych PVC/MDF**, nie hurtownia płyt. To nie jest podmiot, u którego zamawia się formatki.
- **korner.pl** = Korner Sp. z o.o. (zał. 1992), hurtownia akcesoriów meblowych i płyt (Egger itd., okucia GTV/Nomet/Sevroll), centrala **Strzałków** (k. Radomska); **KornerGo** (kornergo.pl) = cięcie formatek, oklejanie, CNC, zamówienia online.
- Konsekwencja ostrzejsza niż sama literówka w domenie: „Korner (**Żary**)" powtarzane we wszystkich skillach niemal na pewno pochodzi z adresu **niewłaściwej firmy** (to Poli-Eco siedzi w Żarach). Do ustalenia z Tobą: z jakiego fizycznie oddziału/kanału zamawiasz — bo być może „Żary → 400 km" to problem, którego w ogóle nie ma, a katalog `korner-katalog.md` opisuje asortyment zgadywany, nie rzeczywisty (marki w nim wymienione — Egger, Kronopol, Pfleiderer, Swiss Krono, Blum, Hettich, GTV — częściowo pokrywają się z ofertą korner.pl: Egger i GTV potwierdzone, Blum/Hettich/Pfleiderer do weryfikacji).
- **Dostawcy śląscy: brak.** W całym zestawie (w tym w `dostawcy.md`, 13,4 KB, ~60 firm od IKEA po Gaggenau) nie występuje ani Daedalus, ani Akces, ani żaden podmiot z okolic Zabrza/GOP. Brak też jakiejkolwiek sekcji o logistyce dostaw formatek (koszt palety, odbiór osobisty vs wysyłka), co przy płytach jest decyzją kosztotwórczą.
- Drobiazg podejrzany: `dostawcy.md` wymienia „**Korner-glazura**" przy płytkach — hurtownia płyt meblowych nie handluje gresem; wygląda na konfabulację.

**Mapa dostawców per skill:** meble-architekt → wyłącznie Korner (+Blum/Hettich w stylu); architekt-kuchni → Korner + współdzielony `dostawcy.md`; architekt-wnetrz → pełna mapa multi-vendor (Leroy/Castorama, IKEA, Westwing/Bonami/JYSK, Tubądzin/Cersanit, RTV Euro/Media Markt/x-kom, Grohe/Hansgrohe/Geberit/Deante/Roca, GoodForm/Flos, Topmet/Klus/Paulmann, Berker/Schneider/Kontakt-Simon, Porta/Pol-Skone, Festfloor/Topciment, polscy projektanci). Ta mapa jest sensowna jakościowo, ale w 100% ogólnopolska/warszawska.

### 4b. Stałe techniczne — tabela zgodności

| Stała | meble-architekt | standardy-meble.md | uklady/technologia (kuchni) | architekt-wnetrz SKILL | Werdykt |
|---|---|---|---|---|---|
| Korpus dolny (h) | 820 z cokołem | 720 + cokół 100 = 820 | — | — | ✓ zgodne, rynek PL OK |
| Głębokość dolnych | 580/600 | 580/600, blat 600–630 | — | — | ✓ |
| Szafka górna | 720 × gł. 320 | 720 (900/1000) × 320 (360–400) | — | — | ✓ |
| Wysokość blatu | pytanie „88/91 cm" | 850–930 wg wzrostu (3 progi) | — | workflow-zapytania: „860/880/910" | ⚠ trzy różne siatki wartości; ujednolicić do 860/880/910 |
| Blat laminowany | 38–40 | 38–40 | technologia: 38 | — | ✓ |
| **Blat spiek** | **38–40 mm** (house style) | — | **12–20 mm na podkonstrukcji** (technologia + korner-katalog) | bez grubości | ✗ **sprzeczne**; rynek: spieki 4/12/20 mm — meble-architekt błędny |
| **Orzech Royal (dekor)** | bez kodu | — | SKILL kuchni: **Egger H3734 ST9** | korner-katalog: **Egger H3702** | ✗ **sprzeczne** — co najmniej jeden kod błędny; zweryfikować z wzornikiem Egger/dostawcy |
| **Szuflady Blum** | „Legrabox **H**=192", „3–5 szuflad Legrabox H" (workflow) | „192 (Legrabox **H**), 134 (M), 90 (N)" | — | — | ✗ wewnętrznie zgodne, **niezgodne z nomenklaturą Blum**: boki Legrabox to N≈66,5 / M≈90,5 / K≈128,5 / C≈193 mm — „H" nie istnieje, „134" nie odpowiada żadnemu |
| Okap od płyty | 650 gaz / 550 indukcja | 650/550 (+ zakaz szafki nad gazem, nad indukcją ≥750) | 650/550 | 650/550 | ✓ 4× zgodne, rynek OK |
| Trójkąt roboczy | — | — | 3600–7000, bok 1200–2700, bez przecinania ciągiem | „max 7 m suma boków" | ✓ zgodne (wersja wnetrz uboższa) |
| Przejścia / wyspa | — | — | ≥1000 TWARDY PRÓG (1100–1200 optimum; strona AGD ≥1200; wyspa = ~3400 w osi) | „min 100 cm, optymalnie 110–120" | ✓ |
| Lodówka wentylacja | 50 mm tył/góra | 50 mm + kratka w cokole | 50 mm + kratka w cokole i wieńcu | 50 mm | ✓ |
| Fugi frontów | 2 mm fuga / 3 mm reveal / 2 mm pod blatem | 2–3 / 3 / 2 | — | — | ✓ |
| Luzy montażowe | — | fuga do ściany 5–15, do sufitu 10–30 | technologia: **szczelina 20–50 na blendę**, światło zabudowy = ściana − 40–60 | — | ⚠ standardy-meble (5–15) vs technologia (20–50) — nie sprzeczne wprost (fuga ≠ blenda), ale mylące bez komentarza |
| **Otwory AGD** | — | piekarnik „otwór **600×600**", lodówka „otwór **600**×1780" | — | — | ⚠ nieprecyzyjne: 600 to szerokość **korpusu**; nisza/światło zabudowy to **560** (piekarnik 560×590–600, lodówka 560×1780). W tabeli „wymiar otworu" ta dwuznaczność może skończyć się błędnym cięciem |
| Płyta korpusowa | 18 mm (+ „dna szuflad 18" w katalogu — nietypowe, zwykle HDF/16) | 18 (16 eko), fronty 19, HDF 3 | 18/19/HDF 3 | — | ✓ z drobiazgiem |

### 4c. Czy stolarz potnie bez dopytywania?

**Nie.** Stan wyjść:
- `dokumentacja-stolarz.md` (architekt-kuchni) daje bardzo dobry poziom **ofertowo-techniczny**: elewacje z modułami i blendami, statusy wymiarów, rozmieszczenie AGD z wymaganiami, lista pomiarów kontrolnych, jawna deklaracja „to NIE jest dokumentacja produkcyjna". To uczciwe i bezpieczne — ale finalnego kroku (po pomiarach → formatki) **nikt w zestawie nie umie zrobić**.
- `meble-architekt` udaje, że umie (tabela `F01 | 580×800 | dekor | ilość | obrzeże`), ale bez reguł: jak z modułu 600×820×580 powstają boki/wieńce/półki/plecy/fronty, jakie odliczenia (plecy wpuszczane 10 mm vs nakładane, front = światło − 3 mm/str., cokół − x), obrzeże per krawędź (którą z 4), kierunek słoja per formatka (zasady są w standardy-meble.md, ale kolumny na to w tabeli formatek nie ma), wiercenia. Stolarz/KornerGo dostanie tabelę, której nie da się zweryfikować ani powtórzyć.

---

## 5. Braki

### BLOKUJĄCE (bez tego skill nie dowozi użytecznego outputu)
1. **meble-architekt: martwe references** — 4 deklarowane pliki nie istnieją w katalogu skilla; skill w praktyce działa bez katalogu materiałów i standardów, które sam nakazuje stosować.
2. **Brak metody moduł → formatki** (odliczenia, plecy, fronty, obrzeże per krawędź, słoje, format tabeli produkcyjnej) — obiecany produkt „lista formatek / cięcie płyt" jest niedowoźny w całym zestawie.
3. **korner.eu → korner.pl/KornerGo** + weryfikacja miasta/oddziału i realnego asortymentu (katalog może opisywać niewłaściwy podmiot).

### ISTOTNE (obniża jakość, wymusza rundy dopytywania)
4. Rozjechane stałe: spiek 38–40 vs 12–20; Egger H3702 vs H3734; nomenklatura Legrabox; siatka wysokości blatu 88/91 vs 850–930 vs 860/880/910; dwuznaczne „otwory" AGD (600 vs nisza 560).
5. Kolizje triggerów (§3a) + dwa aktywne `architekt-kuchni` przy pluginie i synced naraz.
6. Duplikat architekt-kuchni bez mechanizmu synchronizacji (w repo istnieje już `worker/scripts/build-skill.mjs` — jest czym to zautomatyzować).
7. Zero dostawców lokalnych (Śląsk: Daedalus, Akces, hurtownie GOP) i zero logistyki dostaw formatek.
8. Brak cen referencyjnych (zł/m² płyty 18 mm, zł/mb obrzeża, zł/kpl Legrabox/Sensys, zł/mb zabudowy jako sanity check) — kosztorysy to puste widełki „X–Y zł".
9. Hardcode'y: `C:/Users/PC/...` (ścieżka z jednego komputera z Windows), `https://meble-banana.<subdomen>.workers.dev` (placeholder), model `gemini-3.1-flash-image-preview` (do przeglądu przy zmianach API).
10. Brak liczenia okuć per front (liczba zawiasów wg wysokości/wagi frontu, dobór podnośników Aventos wg wagi) — lista zakupów okuć powstaje „na oko".

### NICE-TO-HAVE
11. Rzuty SVG: podpiąć istniejące `projects/kuchnia-9.02/gen.py` / `_render.py` jako `scripts/` skilla zamiast wyłącznie ASCII.
12. Kontrola zgodności renderu (checklist z prompty-wizualizacyjne §5) — rozszerzyć na architekt-wnetrz (dziś tylko kuchnia ją ma).
13. Plan montażu kuchni w architekt-kuchni (dziś BRAK — świadomie, ale checklist „kolejność: słupki → dolne → blat → górne → fronty → cokoły → silikon" kosztuje pół strony).
14. Harmonogram dla projektu samej kuchni (dziś tylko w skali mieszkania).

### Nowe skille?
**Nie tworzyć.** Łazienka, garderoba, oświetlenie i kosztorys nie zasługują na osobne skille — to references/rozdziały w dwóch istniejących rolach (patrz §6). Osobny skill miałby sens dopiero dla **rozkroju/formatek jako narzędzia** (skrypt liczący formatki + arkusze), ale i to lepiej trzymać jako `scripts/` + reference wewnątrz skilla kuchennego, nie jako byt triggerowany opisem.

---

## 6. Rekomendacja docelowej architektury

**Docelowo: 2 skille + jeden wspólny zestaw references. Usunąć 1 skill i 1 kopię.**

```
skills/
├── architekt-wnetrz/          # ORCHESTRATOR pomieszczeń i mieszkania
│   ├── SKILL.md               # fazy 0–8, ale Faza 5a = "deleguj do architekt-kuchni"
│   └── references/            # jedyne źródło współdzielonych plików
│       ├── dostawcy.md        # + sekcja Śląsk + logistyka dostaw
│       ├── standardy-meble.md # po korekcie stałych
│       ├── korner-katalog.md  # po weryfikacji podmiotu (korner.pl/KornerGo)
│       ├── generacja-obrazow.md  # NOWY: 4 ścieżki + prompt formula + błędy (1 kopia zamiast 3)
│       ├── instalacje-elektryka.md, oswietlenie-katalog.md,
│       ├── podlogi-sciany-sufity.md, style-aesthetics.md, workflow-zapytania.md
│       └── cloudflare-worker.md
└── architekt-kuchni/          # SPECJALISTA ZABUDÓW NA WYMIAR (rdzeń = obecny architekt-kuchni)
    ├── SKILL.md               # workflow 11 kroków, rozszerzony scope: kuchnia + szafa/garderoba + TV + łazienka (meblowo)
    ├── references/
    │   ├── analiza-pomieszczenia.md, uklady-kuchni.md, technologia-wykonania.md,
    │   ├── dokumentacja-stolarz.md, prompty-wizualizacyjne.md
    │   ├── zabudowy-inne.md   # NOWY: przeniesione z meble-architekt (szafa/garderoba/TV/łazienka: intake, standardy, plan montażu)
    │   └── formatki.md        # NOWY: metoda moduł→formatki + format tabeli produkcyjnej
    └── scripts/gen.py         # przeniesione/uogólnione z projects/kuchnia-9.02
```

Decyzje i uzasadnienia:

1. **Usunąć `meble-architekt`.** Jego rdzeń kuchenny jest w całości zdominowany przez architekt-kuchni (który ma wszystko to samo plus analizę zdjęć, progi układów i pomiary), a jego references są martwe. Unikaty do przeniesienia przed kasacją: (a) format listy zakupów Korner (Faza 5) → `formatki.md`/dokumentacja-stolarz, (b) plan montażu (Faza 4) → `zabudowy-inne.md`, (c) aspect-ratio routing (3c) → `generacja-obrazow.md`, (d) intake szafa/łazienka/TV → `zabudowy-inne.md` (część już jest w workflow-zapytania.md — scalić, nie dublować). Utrzymywanie go „bo ma szersze meble" mnoży kolizje triggerów przy ~30% unikalnej treści.
2. **Zlikwidować duplikat architekt-kuchni**: źródłem prawdy jest repo (plugin); kopia `synced/` ma być generowana skryptem (rozszerzyć istniejący `worker/scripts/build-skill.mjs` lub prosty rsync w CI), albo nie istnieć wcale, jeśli plugin jest zainstalowany wszędzie tam, gdzie pracujesz. Dwa ręcznie edytowane egzemplarze już się rozjechały redakcyjnie.
3. **Rozłączne triggery** (zasada: orchestrator = pomieszczenia i warstwy wykończeniowe; specjalista = zabudowa meblowa):
   - `architekt-wnetrz` description **traci**: „meble na wymiar, kuchnia na wymiar, szafa na wymiar, garderoba, Korner, rzuty, wizualizacja" (za generyczne / cudze), **zyskuje** anty-trigger: „NIE aktywuj do samej zabudowy meblowej — to skill architekt-kuchni" oraz jawną delegację w Fazie 5a.
   - `architekt-kuchni` **zyskuje** triggery zabudów przejęte po meble-architekt: „meble na wymiar, szafa na wymiar, garderoba, zabudowa TV, formatki, cięcie płyt, lista zakupów Korner" i rozszerza anty-trigger („NIE do wykończeń, oświetlenia, pełnych pomieszczeń").
   - Dwustronność: obie description wymieniają się nazwami — warunek, którego dziś nie spełnia żadna para.
4. **Jedna kopia rzeczy współdzielonych**: house style definiowany **tylko** w `style-aesthetics.md` (SKILL.md-y jedynie wskazują), generacja obrazów **tylko** w `generacja-obrazow.md`, stałe **tylko** w standardy-meble/technologia. SKILL.md architekt-wnetrz (33 KB — za duży) chudnie: przykładowe tabele elektryki z Fazy 6 (duplikat instalacje-elektryka.md), template'y promptów z Fazy 7 i szablon 8b–8e → do references. Cel: SKILL.md < 15 KB, ładowanie szczegółów on-demand.
5. **`formatki.md` + skrypt to warunek sensu całości** — bez tego pipeline kończy się tam, gdzie zaczyna się realna wartość (produkcja). Reguły do spisania z technologiem/stolarzem raz, potem deterministyczne.
6. **Czego NIE robić**: nie wydzielać łazienki/garderoby/oświetlenia/kosztorysu jako skilli (za mało unikalnej wiedzy, kolizje triggerów gwarantowane); nie przepisywać architekt-kuchni (rdzeń — analiza, układy, technologia, dokumentacja, prompty — to najlepsza treść w zestawie i zostaje bez zmian).

---

## Plan naprawczy

Priorytety: P0 = blokujące, P1 = przed następnym realnym projektem, P2 = jakość, P3 = kiedyś. Wysiłek: S ≤ 1 h, M = 2–4 h, L = dzień+.

1. **[P0/S] Korner: domena i podmiot.** Zamień `korner.eu` → `korner.pl` (6 miejsc), zweryfikuj z własnymi zamówieniami oddział/kanał (KornerGo?) i popraw „Żary" wszędzie, gdzie pochodzi z adresu Poli-Eco; przy okazji usuń „Korner-glazura" z dostawcy.md albo udokumentuj skąd to.
2. **[P0/S] Zweryfikuj `korner-katalog.md` z realną ofertą** korner.pl/KornerGo (marki płyt, okucia, dekory, usługi CNC) — plik może opisywać zgadywany asortyment.
3. **[P0/S] Ujednolić stałe:** spiek 12–20 mm (usuń „38–40" z meble-architekt/house-style), jeden zweryfikowany kod Egger dla Orzech Royal, poprawna nomenklatura Legrabox (N/M/K/C z realnymi wysokościami), jedna siatka wysokości blatu (860/880/910), doprecyzowanie „otwór korpusu 600 / nisza 560" w standardy-meble.md.
4. **[P1/M] Napisz `references/formatki.md`** (metoda moduł→formatki: odliczenia, plecy, fronty, obrzeże per krawędź, słoje, format tabeli produkcyjnej + zasada „tylko po pomiarach kontrolnych") i podepnij w dokumentacja-stolarz.md jako krok po pomiarach.
5. **[P1/M] Zlikwiduj `meble-architekt`:** przenieś unikaty (lista zakupów, plan montażu, aspect-ratio routing, intake zabudów) do architekt-kuchni/`zabudowy-inne.md` i `generacja-obrazow.md`, potem usuń skill z synced.
6. **[P1/S] Rozłącz triggery i domknij delegację dwustronnie** (opisy wg §6 pkt 3; anty-triggery w obu skillach).
7. **[P1/S] Jedno źródło architekt-kuchni:** repo jako źródło prawdy, synced generowany skryptem (rozszerz `worker/scripts/build-skill.mjs`) albo usunięty tam, gdzie działa plugin.
8. **[P2/S] Wydziel `generacja-obrazow.md`** i wytnij 2 z 3 kopii logiki generacji; przy okazji usuń hardcoded ścieżkę `C:/Users/PC/...` (parametr/env) i przenieś placeholder workera do konfiguracji.
9. **[P2/S] Dostawcy lokalni:** dodaj do `dostawcy.md` sekcję Śląsk (Daedalus, Akces + zweryfikowane hurtownie/rozkrój w promieniu ~50 km od Zabrza) i akapit o logistyce/kosztach dostawy formatek.
10. **[P2/M] Ceny referencyjne:** tabela widełek (płyta 18 mm zł/m², obrzeże zł/mb, Legrabox/Sensys zł/kpl, blat laminowany/spiek zł/mb, robocizna montażu zł/mb zabudowy) z datą aktualizacji — podstawa pod niepuste kosztorysy.
11. **[P2/S] Okucia per front:** reguły liczby zawiasów (wys./waga frontu), dobór Aventos wg wagi — dopisać do standardy-meble.md.
12. **[P3/M] Podepnij `gen.py`/`_render.py`** jako `scripts/` skilla architekt-kuchni (rzuty/elewacje SVG generowane, ASCII tylko jako podgląd inline).
13. **[P3/S] Plan montażu + mini-harmonogram kuchni** w architekt-kuchni (checklist kolejności + typowe czasy), przeniesione i rozszerzone z meble-architekt Faza 4.
14. **[P3/S] Odśwież parametry generatora** (model `gemini-3.1-flash-image-preview`, limity RPM) w jednym miejscu po wykonaniu pkt 8.

---

## Aktualizacja 2026-08-12 — weryfikacja synced vs repo + usunięcie duplikatu

Weryfikacja kopii skilli na koncie claude.ai (`~/.claude/skills/synced/`) względem `skills/` w repo:

| Skill (konto) | Werdykt | Uzasadnienie |
|---|---|---|
| `architekt-kuchni` | **PRZESTARZAŁY → USUNIĘTY z konta przez użytkownika (2026-08-12)** | wersja sprzed korekty dostawcy: „Korner (Żary, korner.eu)" + kody dekorów z pamięci (Egger H3734/H3702); w repo skill nie istnieje (zastąpiony przez `zabudowa-na-wymiar`); w sesji 2026-08-11/12 zdążył się jeszcze wyzwolić na frazę „projektujemy kuchnię" (loteria triggerów z §1 pkt 4 audytu) — projekt uratowały referencje czytane z repo |
| `zabudowa-na-wymiar` | AKTUALNY | treść = repo; różnice wyłącznie pakowaniowe (przepisane ścieżki `../architekt-wnetrz/references/` → `references/` + skopiowane pliki współdzielone — zgodnie z `skills/README.md`) |
| `architekt-wnetrz` | AKTUALNY (drobny dryf) | SKILL.md identyczny; references: 2-liniowe różnice w `generacja-obrazow.md` i `zapytania-dostawcy.md`, nadmiarowe `formatki.md`/`prompty-wizualizacyjne.md` w paczce — do wyrównania przy najbliższym uploadzie ZIP-a z `build-skills.yml` |

Wniosek: ryzyko nr 4 z audytu (dwa skille kuchenne aktywne naraz) — **zamknięte**.
