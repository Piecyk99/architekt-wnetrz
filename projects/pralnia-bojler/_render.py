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
890 mm wide and 2500 mm tall, full-height vertical, made of matte HPL walnut
royal Egger H3702 finish with horizontal wood grain direction, integrated full
height black matte 12mm L-profile recessed handles on the leading edge of each
panel. Above the panels a clean solid 100 mm high top fascia matching the
walnut tone, completely smooth and uninterrupted, NO ventilation grille, NO
slot, NO openings, just continuous walnut HPL matching the panels below.
Below the panels a 100 mm matte black plinth flush with the floor. Floor is
dark engineered oak chevron parquet matching the adjacent wardrobe room,
visible reflecting soft light. Side walls finished in warm off-white cream
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
2.67 m wide × 2.5 m tall built-in sliding wardrobe in matte walnut HPL with
3-track top-hung sliding mechanism. The two right panels have slid LEFT and
are now STACKED behind the leftmost panel, all three walnut panels grouped
on the LEFT THIRD of the wall (890 mm wide stack covering the bojler
section). The RIGHT TWO THIRDS of the wall (1780 mm) is now OPEN, revealing
the interior of the built-in.

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

Floor: dark engineered oak chevron parquet matching adjacent wardrobe. Top
fascia: SOLID clean walnut 100 mm tall, NO ventilation grille, NO slot,
completely smooth. Inside the cavity warm 4000K LED cove illuminates shelves
uniformly. Cream warm-white side walls. Sony A7R IV, 28mm f/8, eye-level
from doorway. No people, tidy. Dezeen editorial aesthetic, daily-use
laundry day scene.""",
    },
    "03-open-bojler-service": {
        "aspectRatio": "16:9",
        "imageSize": "1K",
        "text": """Architectural photo of a 6 sqm Polish utility laundry room. Back wall
2.67 m wide × 2.5 m tall built-in sliding wardrobe in matte walnut HPL with
3-track top-hung sliding mechanism. The two left panels have slid RIGHT and
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

Floor: dark engineered oak chevron parquet. Top fascia: SOLID clean walnut
100 mm, NO ventilation grille. Warm 4000K LED cove inside illuminates the
boiler area and shelves. Cream warm-white side walls. Sony A7R IV, 28mm f/8,
eye-level from doorway. No people, tidy. Architectural Digest aesthetic,
annual boiler service scene.""",
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
