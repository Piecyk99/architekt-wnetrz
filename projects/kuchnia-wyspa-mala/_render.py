#!/usr/bin/env python3
"""Render kitchen W3 visualizations via Gemini Nano Banana 2."""
import os, sys, json, base64, urllib.request, urllib.error, pathlib

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    sys.exit("GEMINI_API_KEY env var required (source .env.local)")

MODEL = "gemini-3.1-flash-image-preview"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# Wspólny opis kuchni W3 (style A - Modern Polish) - reużywany we wszystkich promptach
BASE_KITCHEN = """
Compact 4.86 sqm Polish apartment kitchen, interior dimensions 259 cm wide
along the window wall and 191 cm deep. Ceiling height 250 cm. Layout
shape: L-shape along the long window wall and the short right wall, plus
a longitudinal peninsula running along the bottom wall.

ALONG THE WINDOW WALL (259 cm long): from left to right — induction
hob 60 cm built into the worktop, then 90 cm of clear worktop with two
drawers below, then a stainless steel single-bowl undermount sink 50 cm
positioned exactly under a window, then a fully integrated 45 cm
dishwasher with matching cabinet front. Above the worktop: a built-in
extractor hood concealed inside a matching cabinet over the induction
hob, with upper cabinets to the right of the window going to the ceiling.

WINDOW: centered above the sink, single window approximately 110 cm wide
and 125 cm tall with white frame, daylight streaming in.

ALONG THE RIGHT WALL (191 cm long): a full-height built-in column
unit, two 60 cm modules side by side reaching ceiling. Left module is a
built-in fridge/freezer 60x60x202 cm fully integrated with matching wood
front. Right module: a 60 cm built-in oven at eye level (top of oven
around 180 cm from floor), 38 cm built-in microwave above the oven, a
60 cm tall pull-out larder drawer below the oven, and a small cabinet
above the microwave going to ceiling. To the right of the columns, a
71 cm wide section with 4 cm thick worktop, 3 drawers below and upper
cabinets above, used as a coffee / breakfast station with espresso
machine, kettle and toaster on the worktop.

PENINSULA (along the bottom wall, 174 cm long, 40 cm deep cabinet body
with worktop overhanging 25 cm toward the hallway side to form a bar).
From the kitchen side: three drawers full length. From the hallway side:
the overhanging worktop forms a breakfast bar, with two bar stools tucked
underneath. The peninsula creates a clear walkway of approximately 151 cm
between itself and the window-wall worktop — comfortable for two people.

MATERIALS (style A — Modern Polish Apartment):
- Cabinet fronts: matte Egger H3734 ST9 Pacific Royal Walnut, a warm
  medium-dark walnut with natural horizontal wood grain.
- Worktop and full backsplash: black matte sintered stone (Laminam Calce
  Nero or similar), 12 mm thick worktop with the same material running
  up the wall behind the worktop as a continuous full-height backsplash
  to the upper cabinets.
- Sink: stainless steel undermount, deep single bowl.
- Tapware: matte black tall pull-out spray faucet.
- Plinth: matte black aluminium 100 mm high.
- Handles: NO knobs — integrated full-height matte black 12 mm L-profile
  recessed handles along the top edge of every drawer and door (gola
  system).
- Appliances: fully integrated where possible (fridge, dishwasher, oven,
  microwave behind walnut fronts), hob is induction with seamless black
  glass surface, dishwasher front matches the walnut cabinets exactly.
- Wall not covered by cabinets: warm cream off-white matte paint.
- Floor: light honey oak engineered hardwood planks 14 cm wide running
  parallel to the long walls, matte lacquer, light warm tone.
- Lighting: warm 3000K LED strip recessed under all upper cabinets
  illuminating the worktop, one warm pendant light low over the
  peninsula bar.
- Small details: an espresso machine, a kettle, a wooden cutting board
  on the worktop next to the induction hob, a small herb plant on the
  windowsill, a folded linen tea towel on the oven handle. No clutter.
"""

PROMPTS = {
    "01-main-view-from-doorway": {
        "aspectRatio": "16:9",
        "imageSize": "2K",
        "text": f"""Architectural interior photograph of a modern Polish kitchen, view from
the doorway entering from the hallway. The viewer stands in the doorway
looking into the kitchen with the window-wall (long worktop with induction,
sink and dishwasher) running across the back of the frame, the right wall
(full-height column with fridge and oven) on the right, and the peninsula
visible in the immediate foreground on the right side as it ends near the
doorway. The image must clearly show the L-shape composition: peninsula
foreground right, induction-sink-dishwasher run across the back under a
bright window, and the full-height column on the right wall.
{BASE_KITCHEN}

Captured with Sony A7R IV, 24mm lens at f/8, shoulder-height perspective
from the doorway, three-point composition. Soft daylight through the
window creating a warm side-lit atmosphere. Architectural Digest editorial
spread aesthetic, calm, tactile, no people, no clutter, no signage.
""",
    },
    "02-worktop-window-zone": {
        "aspectRatio": "3:2",
        "imageSize": "2K",
        "text": f"""Architectural interior photograph of a modern Polish kitchen, FRONTAL
EYE-LEVEL view of the window wall. The camera looks straight at the
window wall from inside the kitchen, perpendicular to it. The image
should show: induction hob on the left, 90 cm of clear black sintered
worktop in the middle-left, stainless undermount sink directly under the
window in the centre, fully integrated dishwasher on the right, upper
cabinets above the worktop going to ceiling with a built-in extractor
hood centred over the induction hob, warm cream walls visible around the
window, light honey oak floor in the lower edge of the frame, peninsula
just visible at the bottom of the frame as a foreground hint of walnut
wood. Window centred with daylight pouring through.
{BASE_KITCHEN}

Sony A7R IV, 35mm f/8, frontal eye-level composition, perfectly symmetric
about the window. Bright natural daylight, soft shadows. Editorial
aesthetic, Dezeen magazine spread, calm and minimal, no people.
""",
    },
    "03-column-and-peninsula": {
        "aspectRatio": "3:4",
        "imageSize": "2K",
        "text": f"""Architectural interior photograph of a modern Polish kitchen, VERTICAL
CLOSE-UP view of the right wall column unit and the right end of the
peninsula. The viewer stands toward the left side of the kitchen, camera
turned to the right, capturing the full-height walnut column from floor
to ceiling: integrated fridge on the left module, oven at eye level with
microwave above it and pull-out larder drawer below it on the right
module, small upper cabinets at ceiling level, then to the right a 71 cm
worktop section with coffee station (espresso machine, kettle, toaster
arranged), upper cabinet above. In the foreground bottom right, the end
of the walnut peninsula visible with two black bar stools tucked under
the overhanging bar.
{BASE_KITCHEN}

Sony A7R IV, 28mm f/8, vertical portrait composition, eye-level. Warm
daylight from the left (the window) plus 3000K LED warm wash from
under-cabinet strips. Architectural Digest aesthetic, vertical magazine
spread, calm, tactile walnut grain and matte black contrasts.
""",
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
    print(f"  -> {out} ({len(png) // 1024} KB)", flush=True)
