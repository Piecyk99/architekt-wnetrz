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
        "imageSize": "2K",
        "text": """Architectural interior photograph of a compact 6 sqm Polish apartment utility
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
minimalist modern Polish utility room, calm and tactile.""",
    },
    "02-open-reveal": {
        "aspectRatio": "16:9",
        "imageSize": "1K",
        "text": """Architectural interior photograph of a compact 6 sqm Polish apartment utility
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
photograph aesthetic, calm modern Polish utility room.""",
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
