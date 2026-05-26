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
    "02-open-reveal": {
        "aspectRatio": "16:9",
        "imageSize": "1K",
        "text": """Architectural photo of a 6 sqm Polish utility laundry room. Back wall 2.67 m
wide × 2.5 m tall with built-in sliding wardrobe FULLY OPEN, all three matte
walnut HPL panels stacked behind each other revealing the entire cavity.
Interior lined in cream magnolia laminate, divided into THREE 890 mm sections:

LEFT: vertical white cylindrical electric WATER HEATER BOILER, 55 cm dia
× 120 cm tall, wall-hung on a visible bracket, bottom at 1.3 m / top at 2.4 m
above floor, small red warning label, hot/cold pipes on top. Below an open
niche with folded ironing board leaning vertically + upright cordless vacuum
on floor.

CENTER: white front-loading clothes DRYER 60×60×85 cm with condensation tank
on top, on black matte plinth. Above: 4 cream shelves with folded towels and
woven baskets.

RIGHT (far right, flush with side wall): white front-loading WASHING MACHINE
60×60×85 cm with prominent round glass door, on matching black plinth. Above:
shelves with detergent boxes and linens.

Dark engineered oak chevron parquet floor. SOLID walnut top fascia, NO
ventilation grille, NO slot, completely smooth. Warm 4000K LED cove inside
illuminates shelves. Black matte recessed handles on the stacked panels.
Cream warm-white side walls. Sony A7R IV, 28mm f/8, eye-level from doorway.
No people, tidy. Dezeen editorial aesthetic.""",
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
