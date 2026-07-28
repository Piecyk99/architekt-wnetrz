# Prompty wizualizacyjne — kuchnia wierna geometrii pomieszczenia

Prompty po **angielsku** (Gemini Nano Banana 2). Zakaz generowania wizualizacji przed ukończeniem modelu pomieszczenia (workflow kroki 1–4). Zakazane słowa: `8K`, `masterpiece`, `ultra-realistic`, `high resolution`, `best quality`. Kotwice: „Architectural Digest editorial", „Dezeen feature photograph".

---

## 1. Obowiązkowe składniki każdego promptu

1. **Geometria pomieszczenia** — kształt, wymiary (approx. w m), wysokość, pozycje okien/drzwi/elementów konstrukcyjnych względem ścian.
2. **Pozycja obserwatora/kamery** — skąd patrzy, w którą stronę, wysokość oczu, ogniskowa (np. 24 mm, eye-level 160 cm).
3. **Rzeczywiste proporcje** — wymiary kluczowych elementów, żeby model nie „rozciągał" pomieszczenia.
4. **Elementy stałe do zachowania** — okna (z parapetami), drzwi, gzymsy, słupy, wnęki, kratka wentylacyjna — wypisane wprost.
5. **Zabudowa** — kolejność szafek od lewej do prawej zgodna z rozpiską (D1→Dn, G1→Gn, S), pozycje AGD.
6. **Materiały i kolory** — dekory frontów (nazwa + charakter), blat, ściana nad blatem, uchwyty/bezuchwytowe.
7. **Oświetlenie** — naturalne (skąd) + robocze LED + dekoracyjne, temperatura barwowa.
8. **Styl wnętrza** — zgodny z decyzjami projektu (domyślnie Modern Polish Apartment).
9. **Blok zakazów** (sekcja 4) — zawsze na końcu promptu.

---

## 2. Szablon — realistyczna wizualizacja (render od modelu)

```
Architectural interior photograph of a custom-built kitchen in a Polish apartment.
Room geometry (do not alter): [shape, e.g. 3.2 m x 2.6 m, ceiling 2.65 m]. Window
[dimensions + position, e.g. 120x140 cm on the left wall, 60 cm from the corner,
sill at 85 cm, keep the sill]. Door opening [position, width] on [wall]. Structural
column/pilaster [dimensions] in [corner/position] — keep it visible, cabinetry ends
with a filler panel before it. Ventilation grille near the ceiling on [wall] — keep it.

Cabinetry along [wall(s)], left to right: [D1 600 mm tall larder unit with built-in
fridge, D2 800 mm sink base under the window, D3 600 mm dishwasher, D4 600 mm
induction hob with 600 mm chimney hood above...]. Upper cabinets [heights, to ceiling
with 20 mm scribe filler]. Worktop [material, thickness]. Fronts: [decor, e.g. matte
Royal Walnut woodgrain laminate], [handleless / black slim handles]. Backsplash:
[material]. Under-cabinet LED task lighting 3000K, warm daylight from the window.

Camera: [e.g. standing at the doorway on wall C, looking toward the window wall,
eye level 160 cm, 24 mm lens, f/8]. True-to-scale proportions per the given
dimensions. No people. Architectural Digest editorial aesthetic.

STRICT CONSTRAINTS: do not move or resize windows or doors; do not remove the
column/pilaster, cornice or ventilation grille; do not enlarge the room or raise
the ceiling; do not change the camera position in a way that distorts the layout;
do not add an island, extra cabinets or appliances that are not listed; the kitchen
must fit exactly the geometry described above.
```

## 3. Szablon — naniesienie projektu na zdjęcie pomieszczenia

Preferuj `gemini_edit_image` z `imagePath` = zdjęcie referencyjne pomieszczenia (edycja zachowuje geometrię lepiej niż generacja od zera). Wskaż w dokumentacji, które zdjęcie jest referencją.

```
Using the attached photo of the empty room as the exact base: render the designed
kitchen into this room. Keep the photo's camera position, perspective, lens
distortion, lighting direction and every architectural element exactly as in the
photo — walls, window with sill, door, the floor-to-ceiling pilaster in the corner,
ventilation grille, radiator, floor.

Install along [wall visible on the left of the photo]: [cabinet run left to right
with widths and appliances, matching the design spec]. Fronts [decor/finish],
worktop [material], backsplash [material], [handles], under-cabinet LED 3000K.

STRICT CONSTRAINTS: this is an overlay of furniture onto the existing room — do not
move, resize or remove windows, doors, pilasters, cornices or grilles; do not extend
walls or floor area; do not change the viewpoint; do not add furniture where there is
no space in the photo; every cabinet must respect the visible geometry and
proportions of the room; generate nothing unrelated to the reference photo.
```

## 4. Blok zakazów (dołączaj zawsze, dostosuj listę elementów)

- do not move or resize windows and doors
- do not remove cornices, pilasters, columns or ventilation grilles
- do not enlarge the room, ceiling height or floor area
- do not change perspective in a way that falsifies the layout
- do not add elements where there is no physical space (island, extra runs)
- do not generate a kitchen unrelated to the reference photo / described geometry

## 5. Po wygenerowaniu — kontrola zgodności

Porównaj render z modelem pomieszczenia i rozpiską:

| Sprawdzenie | OK/BŁĄD |
|---|---|
| Okna/drzwi w tej samej pozycji i rozmiarze | |
| Elementy konstrukcyjne zachowane (gzyms/słup/kratka) | |
| Kolejność i liczba szafek zgodna z rozpiską | |
| AGD w zaprojektowanych pozycjach | |
| Proporcje pomieszczenia niezmienione | |
| Materiały/kolory zgodne z decyzjami | |

Błędy → iteruj przez `gemini_edit_image` (wskaż konkretną poprawkę), nie generuj od zera. Render niezgodny z geometrią **nie trafia do dokumentacji**.
