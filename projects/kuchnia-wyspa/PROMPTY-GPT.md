# Pakiet do wizualizacji w GPT / Gemini — kuchnia v3.5 (kolory 2026-08-12)

## Jak użyć (3 kroki)

1. Otwórz ChatGPT (tryb tworzenia obrazów) albo gemini.google.com.
2. **Dołącz jako obraz stronę 1 schematu** (`kuchnia-wyspa-schemat-v3.5.pdf` → zrzut ekranu rzutu) — model będzie trzymał się geometrii o niebo lepiej.
3. Wklej PROMPT 1 (główny widok). Po wygenerowaniu poprawiaj JEDNYM zdaniem naraz: „Keep everything exactly the same, only change/fix: …". Nie przepisuj całego promptu od nowa.

Zasada: jeśli model przekłamie geometrię (doda szafki nad oknem, zgubi ramię) — dopisz na końcu promptu: "Follow the attached floor plan exactly."

---

## PROMPT 1 — widok główny od korytarza (16:9)

```
Architectural interior photograph of a small U-shaped kitchen nook in a Polish
apartment, about 2.55 m wide and 1.95 m deep, ceiling 2.48 m, open to a corridor
in the foreground. Attached floor plan shows the exact layout — follow it.

FINISHES: walls painted warm light greige (NCS S 2002-Y); the short partition
wall beside the fridge is anthracite (RAL 7016); light oak plank flooring.

BACK WALL (window wall): a high window (86x82 cm) reaching the ceiling, sill at
166 cm kept as a deep useful shelf; below it a run of handleless matte warm
beige/cashmere base cabinets with a black granite sink (80 cm) directly under
the window, a slim 45 cm dishwasher with cabinet front to its right, a narrow
spice pull-out to its left; NO upper cabinets on this wall; light
travertine-look laminate worktop at 91 cm.

LEFT WALL (induction wall): a shallow wall pilaster at the window corner, then
beige base cabinets with a flush induction hob and built-in oven below, dark
matte walnut upper cabinets reaching the ceiling with an integrated hood and
warm LED strip beneath. At the end of this run the worktop turns 90 degrees
into an L-return peninsula (118 x 50 cm, top at 91 cm) reaching toward the
fridge side; its back, facing the camera, is clad in a dark fluted (reeded)
wood panel; behind the peninsula a 127 cm doorway to the living room.

RIGHT WALL (fridge wall): low beige cabinets with the travertine worktop
continuing around the corner, dark walnut upper cabinets above them to the
ceiling, then a slim dark walnut pantry column, then a freestanding fridge
(60 cm, 190 cm tall) enclosed in MATTE ANTHRACITE panels with an anthracite
cabinet above to the ceiling — the anthracite enclosure visually merges with
the RAL 7016 partition wall next to it into one dark tower. A 60 cm
pass-through separates the peninsula end from that partition wall.

Dark stone-look backsplash only behind the hob; black matte faucet; black
ceiling spots; warm evening-daylight mix; no people. Camera at the corridor
entry, eye level 160 cm, 24 mm lens. Architectural Digest editorial aesthetic.

STRICT: do not move or resize the window (it reaches the ceiling); no upper
cabinets on the window wall; do not enlarge the room; peninsula exactly
118 x 50 with a 60 cm gap to the partition wall; nothing beyond the listed
cabinets and appliances.
```

## PROMPT 2 — strefa gotowania (4:5, pion)

```
Same kitchen as before (follow the attached floor plan). Camera standing at the
window wall, looking back along the induction run: handleless warm beige base
cabinets with flush induction hob and oven below, dark matte walnut uppers to
the ceiling with integrated hood, warm LED glow on the light travertine
worktop (91 cm), dark stone backsplash behind the hob, walls in warm light
greige, light oak floor, the dark fluted peninsula panel visible at the left
edge, the anthracite fridge tower far right. Vertical 4:5 frame, eye level
160 cm, 35 mm lens, warm evening light. No people. Architectural Digest style.
STRICT: same constraints as before.
```

## PROMPT 3 — ciemna wieża lodówki i przejście (4:5, pion)

```
Same kitchen (follow the attached floor plan). Camera inside the kitchen
looking at the fridge corner: the matte anthracite fridge enclosure with
cabinet above reaching the ceiling, visually merging with the anthracite
(RAL 7016) partition wall beside it into one dark monolith; to its left the
slim dark walnut pantry column and walnut uppers over low beige cabinets; the
60 cm pass-through between the beige peninsula end (dark fluted back panel)
and the partition wall; light oak floor, greige walls, warm LED accents.
Vertical 4:5, 35 mm lens. No people. Architectural Digest style.
STRICT: same constraints as before.
```

---

## Opis słowny (gdyby GPT wolał po polsku / do wklejenia z rzutem)

Kuchnia w U, otwarta na korytarz, ~2,55 × 1,95 m, sufit 2,48. Ściany jasny ciepły greige (NCS S 2002-Y), ścianka przy lodówce antracyt RAL 7016, podłoga jasny dąb. Na wprost: okno pod sam sufit (parapet 166), pod nim zlew czarny granit 80 w beżowych bezuchwytowych szafkach, obok zmywarka 45, blat jasny trawertyn na 91. Po lewej: ciąg z indukcją i piekarnikiem, nad nim ciemnoorzechowe górne do sufitu z okapem i LED-em; na końcu ciągu blat skręca w ramię 118×50 z ryflowanym ciemnym panelem od strony wejścia; za ramieniem otwór 127 do salonu. Po prawej: niskie szafki z blatem, nad nimi orzechowe górne do sufitu, dalej wąski słupek orzechowy i lodówka w antracytowej zabudowie do sufitu, zlewająca się ze ścianką 7016; między ramieniem a ścianką przejście 60. Czarna bateria, czarne spoty, ciepłe światło.
