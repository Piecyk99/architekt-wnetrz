# Kuchnia w U z ramieniem L (półwysep) — projekt zabudowy na wymiar (v3.0)

Projekt wykonany skillem **architekt-kuchni** na podstawie: zdjęć pomieszczenia (stan remontowy, obrys blatu wyklejony taśmą), dwóch rzutów odręcznych inwestora z wymiarami i adnotacjami (Z=zlew, zm=zmywarka, L=lodówka, ⊠=indukcja) oraz czterech tur odpowiedzi inwestora. Wykonanie: **samodzielne (inwestor)**, materiały: **Korner (płyty, korner.pl) — oddział Piekary Śląskie / KornerGo**.

> **To NIE jest dokumentacja produkcyjna.** Lista formatek powstanie po pomiarach kontrolnych (pkt 12). Wartości `[P]` = potwierdzone, `[~]` = robocze, `[?]` = do potwierdzenia.

> **Relacja do `projects/kuchnia-9.02`:** ta sama kuchnia po przebudowie ścian — plan 9.02 v4 zarchiwizowany; obowiązuje paleta materiałów zaakceptowana 2026-07-28 (pkt 10).

## Historia wersji (decyzje inwestora)

- v1–v2.2: model pomieszczenia, decyzje bazowe (górne tylko nad indukcją, zlew pod oknem + zmywarka 45, lodówka wolnostojąca 60×65×190 przy ściance 77, indukcja Bosch PXE601DC1E, wycięcie 56×49 `[P]`, sufit 247,8 `[P]`, okno pod sufit 85,6×81,7 `[P]`, przejście 60 `[P]`).
- v2.3–v2.6: iteracje pozycji lodówki/ścianki/wyspy — **zastąpione przez v3.0**.
- **v3.0 (2026-08-12, rzut dzienny inwestora):** „wyspa" = **ramię blatu w L** (przedłużenie ciągu indukcji w stronę lodówki), nie osobna bryła. **127 = szerokość otworu do sypialni** w ścianie A za ramieniem (wcześniej błędnie wiązane z wyspą). Ścianka (wysięg 77 od ściany C) i ramię w jednej linii, między nimi **przejście ~60**. Kuchnia = **U (A+B+C) + ramię L**, otwarta na korytarz.

---

## 1. Podsumowanie pomieszczenia

Aneks kuchenny ~254,6 × ~262+ cm (sufit **247,8** `[P]`), otwarty od południa na korytarz. Ściana **A** (zachód) — ciąg z indukcją; przy narożniku z B **pilaster/uskok ~15,5 gł. × 67** `[~]`; za końcem ciągu **otwór do sypialni szer. 127** `[P]`. Ściana **B** (północ) — **okno pod sam sufit** (wnęka 85,6 × 81,7, parapet ~166,1 `[P]`), zlew pod oknem. Ściana **C** (wschód) — niski ciąg, słupek, lodówka; **ścianka gr. ~9 `[~]`, wysięg ~77 w głąb** na 188,5 `[P]` od narożnika z B; za ścianką korytarz i wyjście. Podejścia wody/odpływu nisko na B `[~]`. Stan: remont (wylewka; posadzka docelowa zmieni wymiary pionowe).

## 2. Wymiary — statusy

| Wymiar | Wartość | Status | Źródło |
|---|---|---|---|
| Ściana B (okno) | 238,9 | `[P]` | rzut inwestora |
| Szerokość A↔C | 254,6 | `[P]` | rzut (kontrola: 238,9+15,5=254,4 ✓) |
| Ciąg A (od pilastra do ramienia) | 195 | `[P]` | rzut |
| Pilaster przy A/B: dł. × gł. | 67 × ~15,5 | `[~]` | rzut |
| **Otwór do sypialni (ściana A, za ramieniem)** | **127** | `[P]` | rzut + opis inwestora (v3.0) |
| Narożnik B/C → ścianka (wzdłuż C) | 188,5 | `[P]` | rzut |
| Okno: od C / szerokość / wysokość | 59,7 / 85,6 / 81,7 (pod sufit) | `[P]` | pomiar inwestora |
| Parapet (wyliczony) | ~166,1 | `[~]` | 247,8 − 81,7 |
| Wnęka okienna → szafki do sufitu na C | 94,7 | `[P]` | pomiar inwestora |
| Ścianka: wysięg w głąb / grubość | ~77 / ~9 | `[~]` | „77 = wymiar małej ścianki"; do pomiaru łańcuchowego |
| Sufit | 247,8 | `[P]` | pomiar (kontrola po posadzce!) |
| Lodówka (wolnostojąca) | 60 × 65 × 190 | `[P]` | inwestor |
| Indukcja Bosch PXE601DC1E | 57,2 × 51,2 × 5,6; **wycięcie 56 × 49** | `[P]` | inwestor |
| **Przejście ramię ↔ ścianka** | **~60 (reguła nadrzędna)** | `[P]` | decyzja inwestora |
| Ramię L: długość od ściany A | ~118 `[~]` (177,6 − 60); taśma ~127 → przejście ~50,6 | `[~]` | docięcie na montażu wg reguły 60 |
| Wysokość blatu | 880 | `[~]` | wzrost użytkownika `[?]` (siatka 860/880/910) |

## 3. Geometria — rzut

Orientacja: **stoisz w korytarzu (południe) i patrzysz na okno (północ)**. A = lewa (indukcja), B = góra (okno), C = prawa (lodówka).

```
            ściana B — OKNO pod sufit (238,9 [P])
   ▓pilaster──────────════ okno 85,6 ════──────────┐
   ▓15,5×67│ DB1 │ ZMYWARKA │  ZLEW 80  │bl│ DC1   │
   │       │ ~50 │    45    │ pod oknem │  │narożna│
   │┌──────┴─────┴──────────┴───────────┴──┤ (C1   │ ściana C
  A││DA1 45                                │ 94,7) │ (188,5 do
   ││DA2 60 ⊠INDUKCJA (piekarnik pod)      ├───────┤  ścianki [P])
  1││DA3 45          WNĘTRZE U             │SŁUPEK │
  9││DA4 45         (aleja ~135)           │  ~28  │
  5││                                      ├───────┤
   │└─────┬────────────────┐               │LODÓWKA│
   │ RAMIĘ L „wyspa" ~118  │  PRZEJŚCIE    │60×65  │
   │ (gł. 65, blat ciągły) │   ~60 [P]     │+nadst.│
   ├───────────────────────┘        ┌──────┴───────┤
   ═ OTWÓR DO SYPIALNI 127 [P]      │ścianka ~77   │
   ═ (za ramieniem)                 └──────────────┘
   │            ← KORYTARZ (otwarte) →     │wyjście
```

Ramię L i ścianka leżą **w jednej linii wschód–zachód**; przerwa między nimi (~60) to wejście do strefy roboczej. Za ramieniem, w ścianie A — otwór do sypialni (127). Front ramienia od strony sypialni/korytarza: panel ryflowany.

## 4. Ergonomia i przejścia

| Przejście / strefa | Wartość | Próg | Ocena |
|---|---|---|---|
| **Ramię ↔ czubek ścianki (wejście do strefy)** | **~60 `[P]`** | ≥90 | ✗ świadoma decyzja inwestora (jak drzwi „60"; ostrzeżenie niżej) |
| Wnętrze U: front B ↔ ramię | ~137 | ≥120 | ✓ |
| Front A ↔ front C1/lodówki | ~125–135 | ≥120 | ✓ |
| Otwór do sypialni | 127 `[P]` | ≥90 | ✓ (ramię go nie zawęża — jest obok, nie naprzeciw) |
| Przed zmywarką (front otwarty) | ~137 | ≥110 | ✓ |
| Przed lodówką | ~125 | ≥100 | ✓ |

**Trójkąt roboczy:** lodówka (C) → zlew (B, pod oknem) → indukcja (A): boki ~1,3–1,8 m, suma ~4,5 m ✓ (norma 3,6–7,0); ciąg do sypialni nie przecina trójkąta (wchodzi się przez przejście 60 obok ramienia).

> ⚠ **Ostrzeżenie (zapisane, decyzja świadoma):** przejście ~60 między ramieniem a ścianką jest poniżej minimum 90 — przechodzi jedna osoba. Reguła 60 jest nadrzędna nad długością ramienia: przy taśmie 127 przejście spada do ~50,6 — **rekomendacja: ramię ≤118**. Ostateczne docięcie blatu na montażu.

## 5. Rozpisanie zabudowy — moduły (mm)

Założenia: korpusy dolne 720 + cokół 100, **blat 880** `[~]` (laminat 38); głębokość korpusów 560, blat 600 (ramię 650); górne: dół 1480, korpusy ~998 **do sufitu 2478**; fronty bezuchwytowe (frez/gola).

### Ściana A — ciąg z indukcją (1950 `[P]`, od pilastra):

| Nr | Moduł | Szer.×Wys.×Gł. | Front / wnętrze | Uwagi |
|---|---|---|---|---|
| DA1 | dolna szuflady | 450×820×560 | 3 szuflady | przy pilastrze; blenda styku `[~]` |
| DA2 | **indukcja + piekarnik** | 600×820×560 | front piekarnika + szuflada dolna | wycięcie blatu 560×490 `[P]`; nisza piekarnika 560×590–600; górna szuflada płytsza (płyta 5,6 pod blatem) |
| DA3 | dolna szuflady | 450×820×560 | 3 szuflady | |
| DA4 | dolna narożna ramienia | 450×820×560 | drzwi | łączy się z ramieniem (wspólny blat, wieniec) |
| GA1 | górna | 450×998×320 | drzwi, półki | dół 1480, do sufitu |
| GA2 | **okap w zabudowie** | 600×998×320 | front uchylny | okap wg modelu `[?]`; ≥550 nad indukcją ✓; recyrkulacja do potwierdzenia kratki `[?]` |
| GA3+GA4 | górne | 450+450×998×320 | półki | LED 3000K pod całością |

### Ramię L („wyspa" — przedłużenie blatu, ~1180×650 `[~]`):

| Nr | Moduł | Szer.×Wys.×Gł. | Front / wnętrze | Uwagi |
|---|---|---|---|---|
| RL1 | dolna ramienia | ~530×820×560 | drzwi/szuflady od wnętrza U | podział korpusów do optymalizacji przy formatkach |
| — | blat ramienia | ~1180×650×38 | — | ciągły z blatem DA (łączenie frezowane/listwa); wieniec boczny na końcu |
| — | panel ryflowany | ~1180×880 | — | od strony sypialni/korytarza (południe) |

### Ściana B — okno/zlew (światło między pilastrem a narożnikiem ~1790 `[~]`):

| Nr | Moduł | Szer.×Wys.×Gł. | Front / wnętrze | Uwagi |
|---|---|---|---|---|
| DB1 | dolna | ~500×820×560 | szuflady | docinana blendą do pilastra |
| DB2 | **zmywarka 45** | 450 (światło wnęki 450×820+) | front meblowy | obok zlewu ✓; woda+odpływ z DB3 |
| DB3 | **zlew 80** | 800×820×560 | drzwi, kosz segregacji | **pod oknem** (okno 1093→1949 od pilastra; zlew ~1105→1905 ✓); zlew 1-komora z ociekaczem |
| — | blenda | ~40 | — | przy narożniku z C |
| — | **bez górnych** | — | — | okno do sufitu; parapet ~166 użytkowy |

### Ściana C — od narożnika z B do ścianki (1885 `[P]`):

| Nr | Moduł | Szer.×Wys.×Gł. | Front / wnętrze | Uwagi |
|---|---|---|---|---|
| DC1 | narożna ślepa (niska, z blatem) | ~900 (front 450) ×820×560 | półki/karuzela `[?]` | martwe pole w rogu z B; blat w L ciągły z DB |
| — | blenda | ~47 | — | dopełnienie C1 do 947 `[P]` |
| C2 | **słupek cargo/spiżarka** | ~280×2378×580 | cargo wysokie | od 947; do sufitu |
| C3 | **zabudowa lodówki** | ~660 światło (lodówka 600+luzy) | — | lodówka wolnostojąca 60×65×190 `[P]` przy ściance; wentylacja 50 tył+góra |
| C4 | nadstawka nad lodówką | ~660×~528×580 | drzwi | od ~1950 do 2478; kratka wentylacyjna |
| — | ŚCIANKA | na 1885 `[P]` | — | bok zabudowy dosunięty; zawiasy lodówki od strony ścianki, drzwi otwierane ku oknu |

## 6. Rozpisanie pionowe (sufit 2478 `[P]`)

| Poziom | Wysokość | Uwagi |
|---|---|---|
| Cokół | 0–100 | kratka wentylacji lodówki w cokole |
| Blat | 880 `[~]` | siatka 860/880/910 wg wzrostu `[?]` |
| Dół górnych A / okapu | 1480 | odstęp 600 od blatu; okap–indukcja ≥550 ✓ |
| Parapet okna | ~1661 | nad blatem ~780 wolnej ściany (fartuch) |
| Lodówka | do 1900 | nadstawka od ~1950 |
| Góra zabudowy | 2478 | górne A, słupek C2, nadstawka C4 — wszystko do sufitu |

## 7. AGD — zestawienie

| Urządzenie | Moduł | Nisza / wymagania |
|---|---|---|
| Indukcja Bosch PXE601DC1E `[P]` | DA2 | wycięcie 560×490 `[P]`; obwód siłowy — puszka na A `[?]` potwierdzić 32A |
| Piekarnik | DA2, pod płytą | nisza 560×590–600; osobny obwód 16A; przegroda od płyty wg karty |
| Okap | GA2 | ≥550 od indukcji; recyrkulacja do czasu potwierdzenia kratki `[?]` |
| Zmywarka 45 | DB2 | światło 450×820+; przyłącza z DB3 |
| Zlew + bateria | DB3 | podejścia nisko na B `[~]` — przedłużyć w zabudowie; nie nad zmywarką ✓ |
| Lodówka 60×65×190 `[P]` | C3 | wolnostojąca; luzy 20–30 bok, 50 tył/góra; zawiasy od ścianki, otwieranie ku oknu |

## 8. Zalecenia instalacyjne (PRZED montażem)

1. Obwód siłowy do DA2 (potwierdzić 32A) + 16A piekarnik + gniazda: zmywarka, lodówka, 2–3 nad blatem B/A (≥600 od zlewu), zasilanie LED (transformator w GA).
2. Zlokalizować **kratkę wentylacyjną** `[?]` — decyduje o okapie (wyrzut vs recyrkulacja).
3. Podejścia wody/odpływu: pozycja `[~]` nisko na B — przedłużenie do DB3 w cokole/za korpusami.
4. Ewentualne gniazdo w ramieniu L — doprowadzenie w podłodze **przed posadzką docelową**.
5. Wymiary pionowe finalnie **po posadzce docelowej**.

## 9. Ryzyka

| Ryzyko | Mitygacja |
|---|---|
| Przejście 60 w praktyce za ciasne | reguła 60 nadrzędna; ramię docinane (118 → można skrócić); decyzja świadoma inwestora |
| Taśma 127 vs reguła 60 (przejście 50,6) | rozstrzygnąć na montażu; rekomendacja ramię ≤118 |
| Pilaster ≠ 15,5×67 na różnych wysokościach | pomiar w 3 punktach; blendy DA1/DB1 docinane |
| Pozycja indukcji vs puszka siłowa | DA2 pozycjonowany do wypustu; kolejność DA1/DA2 może się zamienić |
| Suma łańcucha C (947+280+660 ≈ 1887 vs 1885) | luzy w blendzie przy C1; pomiar łańcuchowy przed zamówieniem |
| Kratka wentylacyjna w strefie zabudowy | pomiar; kratka rewizyjna w zabudowie |
| Posadzka zmieni wysokości | wszystkie pionowe po posadzce |

## 10. Materiały i styl (paleta zaakceptowana 2026-07-28, przeniesiona z 9.02)

Fronty dolne + ramię: **beż/kaszmir mat, bezuchwytowe**; górne A + słupek C2 + nadstawka C4: **ciemny orzech mat** (intencja „Orzech Royal"); blat: **jasny trawertyn, laminat 38**; panel ryflowany ciemny na froncie ramienia od sypialni; fartuch przy indukcji: panel ciemny kamień; bateria+zlew czarne; LED 3000K; cokoły czarne. **Kody dekorów z aktualnej oferty Korner (płyty, korner.pl) `[DO WERYFIKACJI]`** — dobór po próbkach w KornerGo / Piekary Śląskie; Egger poza ofertą korner.pl.

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
10. Wzrost głównego użytkownika → blat 860/880/910.

**Projekt musi zostać zweryfikowany pomiarem na miejscu przed produkcją/cięciem mebli.**

## 12. Montaż samodzielny — podział pracy i kolejność

**Zlecić Korner (płyty, korner.pl)** — KornerGo / e-Rozkrój, oddział Piekary Śląskie: cięcie formatek + oklejanie krawędzi + CNC (puszki 35 pod zawiasy, nawierty); przy pełnej kuchni transport Korner (formatki 2,4 m).
**Samodzielnie:** skręcenie korpusów, zawieszenie górnych (listwa montażowa), blaty (łączenie w L frezem/listwą, wycięcia 560×490 i zlew — wyrzynarka + zabezpieczenie krawędzi silikonem, albo CNC z rozkrojem), cokoły, blendy, AGD (siła — elektryk z uprawnieniami).
**Kolejność:** 1) instalacje + posadzka → pomiar finalny → zamówienie; 2) zabudowa C (C1→C2→C3/C4 przy ściance); 3) ciąg B od narożnika; 4) ciąg A od pilastra; 5) ramię L + kotwienie narożnika; 6) górne A; 7) blaty (B→C1→A→ramię, łączenia, silikon); 8) fronty, regulacja, cokoły z kratką, listwy, AGD.
**Po pomiarach z pkt 11 → przeliczam rozpiskę na listę formatek do e-Rozkroju.**

## 13. Prompt — realistyczna wizualizacja (EN; szkic w `_render.py`)

Zaktualizowany opis geometrii do renderów: U-shaped kitchen ~2,55×2,6 m, ceiling 2,48; window wall with high window (86×82, sill 166) and sink run below; induction wall with uppers to ceiling and integrated hood; low corner run continuing to a tall pantry + freestanding fridge enclosure by a short partition wall; an L-shaped worktop return (~118×65) toward the fridge leaving a 60 cm pass; doorway to bedroom (127) behind the return, fluted dark panel on its back. Pełne prompty: `_render.py` (do aktualizacji po zamknięciu pomiarów).

---
*Decyzje inwestora `[P]`: górne tylko nad indukcją i zabudowa nad lodówką; zlew pod oknem + zmywarka 45; lodówka wolnostojąca przy ściance; przejście 60 (reguła nadrzędna); blat w L (ramię w stronę lodówki); otwór do sypialni 127 za ramieniem; paleta wg pkt 10; wykonanie samodzielne; materiały Korner (płyty, korner.pl).*
