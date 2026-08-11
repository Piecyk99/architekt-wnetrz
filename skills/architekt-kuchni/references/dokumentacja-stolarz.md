# Dokumentacja projektu — szablon 15 punktów

Pełny projekt kuchni oddawany użytkownikowi (i dalej stolarzowi) ma **zawsze** tę strukturę. Przy węższym zleceniu (np. tylko układ) wykonaj punkty, które mają sens, i wypisz, które pominięto i dlaczego.

Konwencje:
- Numeracja szafek **od lewej do prawej, ściana po ścianie**: `D` dolne, `G` górne/wiszące, `S` słupki/wysoka zabudowa (D1, D2…, G1…, S1…). Ta sama konwencja co w istniejących projektach repo (garderoba: S-1, S-2).
- Jednostki: mm w rozpisce, cm w opisie, m w opisie pomieszczenia.
- Każda wartość ma status `[P]` / `[~]` / `[?]` (patrz analiza-pomieszczenia.md).

---

## Szablon

### 1. Podsumowanie pomieszczenia
2–4 zdania: wymiary, wysokość, okna/drzwi, instalacje, elementy konstrukcyjne, stan (deweloperski/remont).

### 2. Znane wymiary
Tabela wymiarów `[P]` — tylko potwierdzone, ze źródłem.

### 3. Wymiary wymagające potwierdzenia
Tabela `[~]`/`[?]` — wartość robocza, podstawa szacunku, dlaczego ważny.

### 4. Przeszkody architektoniczne
Rejestr elementów stałych (gzymsy, słupy, kominy, uskoki, piony, kratki) + konsekwencja projektowa każdego.

### 5. Proponowany układ kuchni
Nazwa układu + uzasadnienie wyboru (z tabeli porównawczej wariantów) + rzut ASCII z góry ze strefami i trójkątem roboczym.

### 6. Rozpisanie zabudowy ściana po ścianie
Dla każdej ściany: elewacja ASCII z numeracją szafek i wymiarami (wzór jak Faza 5a architekt-wnetrz).

```
ŚCIANA B (3200 [P])
┌──────┬──────┬──────┬──────────┬──────┐  ← blenda górna do sufitu 10-30
│ G1   │ G2   │ okap │ G3       │ S1   │
│ 600  │ 600  │ 600  │ 800      │ 600  │
├──────┴──────┴──────┴──────────┤lodów-│
│      blat (gr. wg standardów) │ka    │
├──────┬──────┬──────┬──────────┤      │
│ D1   │ D2 zl│ D3 zm│ D4 płyta │      │
│ 600  │ 800  │ 600  │ 600      │      │
└──────┴──────┴──────┴──────────┴──────┘
 blenda 30→                      ←blenda 40 (docinana)
```

### 7. Kolejność szafek od lewej do prawej
Lista: `D1 (600, cargo) → D2 (800, zlew) → …` — jedna linia na ścianę.

### 8. Orientacyjne szerokości modułów
Tabela: Nr | Typ | Szer × Wys × Głęb | Front | Wnętrze (półki/szuflady/cargo) | Uwagi. Szerokości ze statusem — moduły przy ścianach oznaczone „docięcie blendy na miejscu".

### 9. Rozmieszczenie AGD
Tabela: urządzenie | szafka/pozycja | szerokość korpusu | światło zabudowy/nisza (wg standardy-meble.md — **rozróżniaj korpus 600 od niszy 560, nigdy nie łącz w jedno "otwór"**) | wymagania (prąd/woda/wentylacja) | uwagi o otwieraniu.

### 10. Zalecenia instalacyjne
Co przenieść/dodać PRZED montażem: gniazda, wypusty, podejścia, trasa okapu. Odwołanie do instalacje-elektryka.md.

### 11. Lista ryzyk
Tabela: ryzyko | prawdopodobieństwo | skutek | mitygacja (np. „krzywizna ściany B > 15 mm → węższa blenda D4 → docięcie na miejscu").

### 12. Lista pomiarów dla stolarza
Tabela z technologia-wykonania.md §7, dopasowana do projektu. **Obowiązkowa formuła zamykająca:** „Projekt do weryfikacji pomiarem na miejscu przed produkcją mebli."

### 13. Prompt do realistycznej wizualizacji
Pełny prompt EN wg prompty-wizualizacyjne.md §2.

### 14. Prompt do naniesienia projektu na zdjęcie pomieszczenia
Pełny prompt EN wg prompty-wizualizacyjne.md §3 (+ wskazanie, które zdjęcie jest referencją).

### 15. Alternatywna wersja układu (opcjonalna)
Drugi wariant z tabeli porównawczej: rzut ASCII + 3–5 zdań (czym się różni, kiedy go wybrać). Jeśli przestrzeń wymusiła jeden układ — napisz to wprost z uzasadnieniem.

---

## Czego ta dokumentacja NIE obiecuje

- To **nie jest dokumentacja produkcyjna** (lista formatek do cięcia) — tę wykonuje się dopiero po pomiarach kontrolnych. Jeśli użytkownik poprosi o formatki przy danych `[~]`/`[?]` — odmów i wyjaśnij, czego brakuje.
- Ceny wyłącznie jako widełki orientacyjne, do potwierdzenia u dostawcy (Korner-first — płyty, korner.pl; alternatywy wg dostawcy.md).
