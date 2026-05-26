# Render prompts — pralnia z bojlerem, zabudowa przesuwna

Wygenerowane wg 5-component formula z `skills/architekt-wnetrz/SKILL.md:443`.

## Gdzie wkleić

| Ścieżka                       | Jak                                                                          |
|-------------------------------|------------------------------------------------------------------------------|
| **Gemini AI Studio**          | aistudio.google.com → Image generation → wklej PROMPT_1 → Aspect 16:9 → Run  |
| **Claude.ai (Pro)**           | wklej do nowego czatu z prośbą o image generation                            |
| **Banana MCP (Claude Code)**  | `mcp__nanobanana-mcp__gemini_generate_image` z polem prompt + aspect "16:9" + resolution "2K" |
| **Twój worker (jeśli zdeployowany)** | POST do `/api/generate` z body `{ prompt, aspectRatio: "16:9", resolution: "2K" }` |

**Settings dla obu renderów:** aspect `16:9`, resolution `2K`, model `gemini-3.1-flash-image-preview` (lub `gemini-3.0-flash-image-preview` jeśli niedostępny).

---

## RENDER 1 — Ściana zamknięta (hero shot)

**Cel:** pokazać jak wygląda spójna ściana zabudowy przesuwnej z drzwiami zamkniętymi, widoczna od wejścia do pomieszczenia.

**Aspect:** `16:9`  **Resolution:** `2K`

```
Architectural interior photograph of a compact 6 sqm Polish apartment utility
laundry room, view of the back wall 2.67 meters wide and 2.5 meters tall fully
clad in custom built-in sliding wardrobe doors. Three equal sliding panels each
890 mm wide and 2500 mm tall, full-height vertical, made of matte HPL walnut
royal Egger H3702 finish with horizontal wood grain direction, integrated full
height black matte 12mm L-profile recessed handles on the leading edge of each
panel. Above the panels a 100 mm high top fascia matching the walnut tone with
a continuous aluminum black matte ventilation grille 30 mm slot spanning the
entire 2670 mm width. Below the panels a 100 mm matte black plinth flush with
the floor. Floor is dark engineered oak chevron parquet matching the adjacent
wardrobe room, visible reflecting soft light. Side walls finished in warm
off-white cream lateks paint. Ceiling plasterboard with recessed warm 4000K
neutral LED cove behind the top fascia casting a soft uniform downlight on the
walnut grain. Small Aqara water leak sensor barely visible on floor near right
corner. Captured with Sony A7R IV, 35mm lens at f/8, eye-level perspective from
the doorway, three-point composition with the wall centered, no clutter,
no people, no signage. Architectural Digest editorial spread aesthetic,
minimalist modern Polish utility room, calm and tactile.
```

---

## RENDER 2 — Ściana otwarta (reveal)

**Cel:** pokazać wnętrze: bojler, pralka, suszarka, półki — z dwoma odsuniętymi panelami (panel 1 i 2 przesunięte w prawo, odsłaniają sekcję bojlera + pralki; suszarka pozostaje za panelem 3).

**Aspect:** `16:9`  **Resolution:** `2K`

```
Architectural interior photograph of a compact 6 sqm Polish apartment utility
laundry room, view of the back wall 2.67 meters wide and 2.5 meters tall with
the custom sliding wardrobe partially open. Two of three sliding panels in
matte HPL walnut royal Egger H3702 finish have been slid to the right side of
the wall, stacked behind the third panel, revealing the left two thirds of the
built-in interior. Visible interior compartments lined in cream magnolia
laminate 18mm panels: leftmost section shows a vertical 50 liter white wall
hung electric water heater boiler with red label mounted high at 1300 to 2400
mm above the floor, below it an open vertical niche containing a folded ironing
board and an upright vacuum cleaner standing on the floor. Center section shows
a white front-loading washing machine 60x60x85 cm seated on a 100 mm black
matte plinth, above it four adjustable cream shelves at 340 mm spacing holding
neatly arranged transparent boxes of detergent pods, folded white towels, and
two woven storage baskets. The third sliding panel still closed on the right
hides the dryer section. Floor is dark engineered oak chevron parquet matching
the adjacent wardrobe. Top fascia walnut with continuous black ventilation
slot. Inside the cavity warm neutral 4000K LED cove illuminates shelves
uniformly. Black matte L-profile recessed handles full height on each panel.
Side walls warm off-white cream lateks paint. Captured with Sony A7R IV, 28mm
lens at f/8, slight three-quarter angle from doorway showing depth of the
cabinet, no people, no clutter on floor, tidy and curated. Dezeen feature
photograph aesthetic, calm modern Polish utility room.
```

---

## Po wygenerowaniu

Jeśli wynik nie pasuje, edycja zamiast regeneracji (`mcp__nanobanana-mcp__gemini_edit_image`):

- **"front zbyt jasny"** → dodaj `walnut tone slightly darker, deeper umber chocolate undertone`
- **"za dużo szafek"** → `simplify, fewer items inside, only 3 boxes per shelf`
- **"zła podłoga"** → wymień frazę `dark engineered oak chevron parquet` na konkretny dekor z `references/podlogi-sciany-sufity.md`
- **"za biały bojler"** → `boiler in matte off-white tone blending with the cream interior`
- **"za jasne LED"** → `softer LED, dimmer ambient glow, half intensity`
- **"chcę zamknięty front w nocy"** → dodaj `evening scene, dim 3000K accent uplight from the floor, no overhead light`

## Zakazane słowa (degradują output Gemini)

Per `SKILL.md:468`: NIE używaj `8K`, `masterpiece`, `ultra-realistic`, `high resolution`, `best quality`. Już zostały usunięte z powyższych promptów.
