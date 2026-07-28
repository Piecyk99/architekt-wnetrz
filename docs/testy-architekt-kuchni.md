# Testy skilla `architekt-kuchni`

Scenariusze weryfikujące zachowanie skilla (dry-run względem reguł SKILL.md i references). Każdy test: wejście → wymagane zachowanie → reguła, która je wymusza.

---

## Test 1 — kilka zdjęć + częściowe wymiary

**Wejście:** 3 zdjęcia kuchni z różnych perspektyw + wymiary „ściana z oknem 320 cm, wysokość nie wiem".

**Wymagane zachowanie:**
1. Protokół per zdjęcie (pozycja kamery, ściany, elementy stałe, punkty wspólne) — `analiza-pomieszczenia.md §1`.
2. Sklejenie widoków po punktach wspólnych w JEDEN model (rzut ASCII, ściany A–D) — zdjęcia nie są traktowane jako osobne pomieszczenia — SKILL.md workflow krok 2–3.
3. Tabela wymiarów z podziałem `[P]` (320 cm — podane) / `[~]` (szacunki z proporcji, z podaną podstawą) / `[?]` (wysokość, strefy poza kadrem) — `analiza-pomieszczenia.md §2b`.
4. Lista brakujących pomiarów + max 3–5 pytań krytycznych; analiza kontynuowana na dostępnych danych — SKILL.md zasada 10.

**Wynik dry-run:** PASS — workflow kroków 1–4 jest obowiązkowy i nieprzeskakiwalny; statusy wymiarów wymuszone w każdej tabeli szablonu dokumentacji (`dokumentacja-stolarz.md` pkt 2–3).

---

## Test 2 — pionowy gzyms od podłogi do sufitu w rogu

**Wejście:** zdjęcia pokazują gzyms/pilaster 15×15 cm w rogu ściany zabudowy.

**Wymagane zachowanie:**
1. Gzyms trafia do rejestru elementów stałych z konsekwencją projektową — `analiza-pomieszczenia.md §2c`.
2. Zabudowa kończy się blendą 30–80 mm PRZED gzymsem (nie przycina korpusu wokół, nie ignoruje) — `technologia-wykonania.md §6`.
3. Gzyms wypisany wprost w promptach wizualizacyjnych + w bloku zakazów („do not remove cornices, pilasters") — `prompty-wizualizacyjne.md §1.4, §4`.
4. Pomiar gzymsu na liście pomiarów kontrolnych stolarza — `technologia-wykonania.md §7 poz. 11`.

**Wynik dry-run:** PASS — SKILL.md twarda zasada 2 („Nie ignoruj elementów konstrukcyjnych… Nie usuwaj ich z projektu ani z promptów") + kontrola zgodności renderu (`prompty-wizualizacyjne.md §5`) wyłapuje usunięcie gzymsu przez generator.

---

## Test 3 — kuchnia L + mała wyspa przy przejściu do salonu

**Wejście:** użytkownik chce L z małą wyspą; realna szerokość w osi przejść ~2,9 m.

**Wymagane zachowanie:**
1. Sprawdzenie twardych progów wyspy: ≥1000 mm przejścia z każdej strony roboczej; wyspa robocza wymaga ~3400 mm w osi przejść — `uklady-kuchni.md §2`.
2. Matematyka odrzucenia: 600 (zabudowa) + 1000 + 800 (wyspa) + 1000 = 3400 > 2900 → **wyspa odrzucona z wyliczeniem**, nie „upchnięta" — SKILL.md workflow krok 6, twarda zasada 7.
3. Propozycja alternatywy: półwysep lub barek gł. 300–400 przy przejściu do salonu (próg: przejście obok ≥900) — `uklady-kuchni.md §1`.
4. Odrzucony wariant opisany w pkt 15 dokumentacji (alternatywa/uzasadnienie).

**Wynik dry-run:** PASS — próg jest oznaczony „TWARDY PRÓG" z instrukcją „odrzucasz z matematyką i proponujesz alternatywę".

---

## Checklist jakości (przekrojowo)

| Wymaganie | Mechanizm w skillu | Wynik |
|---|---|---|
| Nie usuwa przeszkód ze zdjęć | zasada 2 + blok zakazów + kontrola zgodności renderu | PASS |
| Nie zmienia wymiarów | statusy `[P]/[~]/[?]`, przy sprzeczności wariant bezpieczniejszy jawnie oznaczony | PASS |
| Odróżnia dane potwierdzone od założeń | obowiązkowe statusy w każdej tabeli (analiza §2b, dokumentacja pkt 2–3) | PASS |
| Użyteczny prompt wizualizacyjny | 9 obowiązkowych składników + 2 szablony + blok zakazów | PASS |
| Logiczna rozpiska szafek | numeracja D/G/S od lewej, ściana po ścianie, elewacje ASCII (dokumentacja pkt 6–8) | PASS |
| Nie zaczyna od wizualizacji | „Zakaz generowania wizualizacji przed analizą geometrii (kroki 1–4)" | PASS |
| Nie obiecuje dokumentacji produkcyjnej bez danych | zasada 8 + `dokumentacja-stolarz.md` „Czego NIE obiecuje" | PASS |

## Walidacja techniczna

- Frontmatter YAML SKILL.md parsowalny (name + description) — sprawdzone.
- `node worker/scripts/build-skill.mjs` — bez regresji (bundluje wyłącznie `skills/architekt-wnetrz`, nowy katalog nie jest widziany) — sprawdzone.
- Brak kolizji wyzwalaczy: architekt-wnetrz obsługuje pełne projekty mieszkań (w tym kuchnię jako fazę), architekt-kuchni — zlecenia stricte kuchenne; rozgraniczenie w obu opisach i w README.

## Ograniczenia testów

Testy to dry-run reguł (statyczna weryfikacja treści skilla), nie uruchomienie na realnych zdjęciach — pełny test end-to-end wymaga sesji Claude z załączonymi zdjęciami pomieszczenia (przykładowe prompty w README).
