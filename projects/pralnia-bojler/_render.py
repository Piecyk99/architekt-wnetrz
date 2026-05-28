#!/usr/bin/env python3
"""One-shot Gemini render — runs locally with API key from env, outputs PNG."""
import os, sys, json, base64, urllib.request, urllib.error, pathlib

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    sys.exit("GEMINI_API_KEY env var required")

MODEL = "gemini-3.1-flash-image-preview"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

PROMPTS = {
    "01-closed-wall": {
        "aspectRatio": "16:9",
        "imageSize": "1K",
        "text": """Architectural interior photograph of a compact 6 sqm Polish apartment utility
laundry room, view of the back wall 2.67 meters wide and 2.5 meters tall fully
clad in custom built-in sliding wardrobe doors. Three equal sliding panels each
890 mm wide and 2500 mm tall, full-height vertical, made of matte HPL in
Egger H3734 ST9 Orzech Pacific Royal Walnut finish, a warm medium-dark walnut
with prominent natural grain, horizontal wood grain direction, integrated full
height black matte 12mm L-profile recessed handles on the leading edge of each
panel. Above the panels a clean solid 100 mm high top fascia matching the
walnut tone, completely smooth and uninterrupted, NO ventilation grille, NO
slot, NO openings, just continuous walnut HPL matching the panels below.
Below the panels a 100 mm matte black plinth flush with the floor. Floor is
LIGHT HONEY OAK 3-layer engineered hardwood by Barlinek decor "dąb Almond",
matte lacquer finish, laid as straight long planks 14 cm wide running
parallel to the side walls perpendicular to the back wall, light warm honey
blonde tone with soft natural grain, NOT chevron, NOT dark. Side walls
finished in warm off-white cream
lateks paint. Ceiling plasterboard with recessed warm 4000K neutral LED cove
behind the top fascia casting a soft uniform downlight on the walnut grain.
Small Aqara water leak sensor barely visible on floor near right corner.
Captured with Sony A7R IV, 35mm lens at f/8, eye-level perspective from the
doorway, three-point composition with the wall centered, no clutter, no
people, no signage. Architectural Digest editorial spread aesthetic,
minimalist modern Polish utility room, calm and tactile.""",
    },
    "02-open-laundry-day": {
        "aspectRatio": "16:9",
        "imageSize": "1K",
        "text": """Architectural photo of a 6 sqm Polish utility laundry room. Back wall
2.67 m wide × 2.5 m tall built-in sliding wardrobe in matte HPL Egger H3734
Orzech Pacific Royal Walnut finish, warm medium-dark walnut with natural
grain, with 3-track top-hung sliding mechanism. The two right panels have
slid LEFT and are now STACKED behind the leftmost panel, all three walnut
panels grouped on the LEFT THIRD of the wall (890 mm wide stack covering the
bojler section). The RIGHT TWO THIRDS of the wall (1780 mm) is now OPEN,
revealing the interior of the built-in.

Visible interior (right two thirds), lined in cream magnolia 18 mm laminate:

MIDDLE SECTION (centered around 1335 mm from left wall): white front-loading
clothes DRYER 60×60×85 cm with condensation water tank visible on top, seated
on a 100 mm black matte plinth. Above the dryer four cream adjustable shelves
at 340 mm spacing holding folded white towels, transparent boxes of laundry
pods, two woven storage baskets.

RIGHT SECTION (flush with right side wall): white front-loading WASHING
MACHINE 60×60×85 cm with prominent round glass door and digital control
panel, on matching black plinth. Above it matching cream shelves with neatly
folded linens and a small basket of pegs.

LEFT THIRD: stack of three walnut HPL panels visible edge-on, full height
2500 mm, showing three vertical aligned black matte recessed handles, casting
shadow over the hidden bojler section behind. The panels look slightly
overlapped showing slim depth between tracks.

Floor: LIGHT HONEY OAK 3-layer engineered hardwood Barlinek dąb Almond,
matte lacquer, straight long planks 14 cm wide running parallel to the side
walls, light warm honey blonde tone, NOT chevron, NOT dark — bright clean
floor that contrasts gently with the medium-dark walnut walls. Top fascia:
SOLID clean walnut 100 mm tall, NO ventilation grille, NO slot, completely
smooth. Inside the cavity warm 4000K LED cove illuminates shelves uniformly.
Cream warm-white side walls. Sony A7R IV, 28mm f/8, eye-level from doorway.
No people, tidy. Dezeen editorial aesthetic, daily-use laundry day scene.""",
    },
    "04-salon-evening-lighting": {
        "aspectRatio": "16:9",
        "imageSize": "1K",
        "text": """Architectural interior photograph of a modern Polish apartment living room
~5 × 5 m, evening atmosphere, ALL ARTIFICIAL LIGHTING ON, view from the
sofa area toward the north wall where a built-in sliding wardrobe in matte
HPL Egger H3734 Orzech Pacific Royal Walnut (warm medium-dark walnut with
prominent horizontal grain) occupies the right two-thirds of the back wall,
266 cm wide × 250 cm tall, built ~60 cm deep so it protrudes ~20 cm proud
of the surrounding wall face (the masonry niche behind it is only 40 cm
deep, so the cabinet box steps forward into the room), with the office
desk to its LEFT on the flush part of the wall. Two large
sliding panels CLOSED, integrated full-height black matte L-profile recessed
handles. Floor: LIGHT HONEY OAK Barlinek dąb Almond, straight planks
parallel to the side walls, matte lacquer. Walls cream warm-white.

LIGHTING (this is the hero of the shot):
1) Recessed perimeter cove LED in 3000K warm white running along the ceiling
edges of the entire living-room ceiling, hidden in a 15 mm slot of the
plasterboard, casting a soft uniform glow upward onto a slightly raised
ceiling plane — creating a halo effect around the whole room (this is L1).
2) Six small recessed downlight spots (Ø80 mm, GU10 3000K warm white,
trim flush with ceiling) distributed across the ceiling: two over the coffee
table, two over the central seating area, two near the entry walking path.
Each spot casts a soft focused pool of warm light on the floor (this is L2).
3) Above the built-in walnut wardrobe, in the 8 cm gap between the top of
the wardrobe (250 cm) and the ceiling (~270 cm), a hidden 3000K LED strip
washes the ceiling with a soft warm glow that haloes the dark walnut wood
from above (this is the L5 cove accent). Two slim vertical 3000K LED strips
also glow softly along the left and right edges of the wardrobe frame
(L5 piony), framing the walnut panels with light.
4) Behind the TV on the opposite side wall, a subtle 3000K bias light glows
softly outward, reducing eye strain (L3).

Foreground: a low-back sage-green linen sofa, light oak coffee table with
a single ceramic vase. Background right: a 65-inch TV on the east wall,
dark screen reflecting subtle ambient light. The office desk visible
peripherally on the left, switched OFF (no work light) to keep the warm
3000K mood consistent. Overall warm, layered, intimate lighting design —
NO single overhead pendant — the entire atmosphere comes from cove + spots
+ wardrobe accent + bias. Captured Sony A7R IV, 24mm f/4 1/30s ISO 800,
eye-level seated perspective. Architectural Digest editorial spread, modern
Polish apartment, calm intimate evening, no people.""",
    },
    "05-zabudowa-led-glow": {
        "aspectRatio": "16:9",
        "imageSize": "1K",
        "text": """Architectural close-up photograph of a custom built-in sliding wardrobe
266 cm wide × 250 cm tall, matte HPL Egger H3734 Orzech Pacific Royal
Walnut, warm medium-dark walnut with prominent horizontal grain, two large
sliding panels CLOSED, full-height black matte L-profile recessed handles
on the leading edges. The wardrobe is set into a wall niche in a Polish
modern living room. The room is in DIM ambient evening light (the rest of
the room lighting is dimmed to ~10%), so the wardrobe LED accents are
the hero subjects:

1) Top accent: in the 8 cm gap between the top of the wardrobe and the
plasterboard ceiling, a hidden 3000K warm-white LED strip washes the
ceiling above the wardrobe with a soft elegant glow — creating a glowing
halo that backlights the dark walnut from above.
2) Vertical accents: two slim 3000K warm-white LED strips, ~240 cm tall,
recessed into the left and right vertical edges of the wardrobe frame
(in the side jambs), glowing softly downward — framing the walnut panels
with two vertical lines of warm light.
3) The walnut wood grain is gently illuminated by these accents, showing
its natural texture and warmth. No spots, no overhead light, no pendants —
just the cove + verticals.

Floor: LIGHT HONEY OAK Barlinek dąb Almond, planks parallel to side walls,
catching warm reflections from the LED glow. Walls cream warm-white,
visible just enough to read the volume of the room. To the lower-left
edge of the frame a corner of a sage-green linen sofa is visible (out of
focus). Sony A7R IV, 35mm f/2.8 1/15s ISO 1600, eye-level perspective,
camera slightly off-axis to show depth. Architectural Digest editorial,
moody premium hero shot, no people, perfectly tidy.""",
    },
    "03-open-bojler-service": {
        "aspectRatio": "16:9",
        "imageSize": "1K",
        "text": """Architectural photo of a 6 sqm Polish utility laundry room. Back wall
2.67 m wide × 2.5 m tall built-in sliding wardrobe in matte HPL Egger H3734
Orzech Pacific Royal Walnut finish, warm medium-dark walnut with natural
grain, with 3-track top-hung sliding mechanism. The two left panels have slid RIGHT and
are now STACKED behind the rightmost panel, all three walnut panels grouped
on the RIGHT THIRD of the wall (890 mm wide stack covering the washing
machine section). The LEFT TWO THIRDS of the wall (1780 mm) is now OPEN,
revealing the interior of the built-in.

Visible interior (left two thirds), lined in cream magnolia 18 mm laminate:

LEFT SECTION (flush with left side wall): vertical white cylindrical
electric WATER HEATER BOILER 55 cm diameter × 120 cm tall, clearly wall-hung
on the back wall on a visible black metal mounting bracket, its bottom edge
at 1280 mm above floor and top at 2400 mm, small red warning label, hot and
cold copper pipes coming out of the top. Below the boiler: open niche
containing a folded ironing board leaning vertically and an upright cordless
vacuum cleaner standing on the floor.

MIDDLE SECTION (centered): white front-loading clothes DRYER 60×60×85 cm
with condensation tank on top, seated on a 100 mm black matte plinth. Above
the dryer four cream adjustable shelves with folded towels, transparent
detergent pod boxes, woven baskets.

RIGHT THIRD: stack of three walnut HPL panels visible edge-on, full height
2500 mm, three aligned black matte recessed handles, hiding the washing
machine behind.

Floor: LIGHT HONEY OAK 3-layer engineered hardwood Barlinek dąb Almond,
matte lacquer, straight long planks 14 cm wide running parallel to the side
walls, light warm honey blonde tone, NOT chevron, NOT dark. Top fascia:
SOLID clean walnut 100 mm, NO ventilation grille. Warm 4000K LED cove inside
illuminates the boiler area and shelves. Cream warm-white side walls. Sony
A7R IV, 28mm f/8, eye-level from doorway. No people, tidy. Architectural
Digest aesthetic, annual boiler service scene.""",
    },
}

OUT_DIR = pathlib.Path(__file__).parent / "renders"
OUT_DIR.mkdir(exist_ok=True)


def call_gemini(text: str, aspect: str, size: str) -> bytes:
    body = {
        "contents": [{"parts": [{"text": text}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": aspect, "imageSize": size},
        },
    }
    req = urllib.request.Request(
        URL,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:500]}")

    candidates = data.get("candidates", [])
    if not candidates:
        sys.exit(f"No candidates. blockReason={data.get('promptFeedback', {}).get('blockReason', 'UNKNOWN')}")

    parts = candidates[0].get("content", {}).get("parts", [])
    for p in parts:
        if "inlineData" in p:
            return base64.b64decode(p["inlineData"]["data"])
    sys.exit(f"No image. finishReason={candidates[0].get('finishReason', 'UNKNOWN')}")


only = sys.argv[1] if len(sys.argv) > 1 else None
for name, cfg in PROMPTS.items():
    if only and name != only:
        continue
    print(f"Rendering {name} ({cfg['aspectRatio']}, {cfg['imageSize']})...", flush=True)
    png = call_gemini(cfg["text"], cfg["aspectRatio"], cfg["imageSize"])
    out = OUT_DIR / f"{name}.png"
    out.write_bytes(png)
    print(f"  → {out} ({len(png) // 1024} KB)", flush=True)
