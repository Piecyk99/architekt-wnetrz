#!/usr/bin/env python3
"""One-shot Gemini render kuchni 9.02 — uruchom lokalnie z kluczem w env, zapisuje PNG.

    export GEMINI_API_KEY=...   # z aistudio.google.com/apikey
    cd projects/kuchnia-9.02
    python3 _render.py                # wszystkie widoki
    python3 _render.py 01-hero        # jeden widok
"""
import os, sys, json, base64, urllib.request, urllib.error, pathlib

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    sys.exit("GEMINI_API_KEY env var required (aistudio.google.com/apikey)")

MODEL = "gemini-3.1-flash-image-preview"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

STYLE = """Materials per the client's reference: handleless matte beige/cashmere lower
fronts, upper cabinets and both tall units in dark matte walnut woodgrain (Egger
H3734 Royal Walnut) reaching the ceiling, light travertine-look stone worktops,
dark stone backsplash panel behind the hob only, remaining walls warm beige paint.
Black matte faucet, black granite sink, under-cabinet warm LED 3000K, two black
surface-mounted ceiling spots, light honey oak floor. No people. Architectural
Digest editorial aesthetic, warm evening-daylight mix."""

GEOMETRY = """Small custom kitchen in a Polish apartment, 2.45 x 1.91 m, ceiling 2.49 m,
open on one side to the hallway/living room. High window (~92x81 cm) on the far
wall reaching the ceiling, sill at 168 cm — keep it. A floor-to-ceiling chimney
pillar (~37 x 63 cm) in the FAR-LEFT corner, clad from worktop level up in a
shallow dark walnut cabinet (S2) flush with the tall oven column next to it —
together they read as one dark wood tower on the left wall. Along the window
wall, right of the chimney: 80 cm sink base under the window, 45 cm dishwasher,
24 cm spice pull-out, blind corner unit, light stone worktop. Right wall:
induction hob with drawers under and a chimney hood above, then a tall graphite
fridge column (60 cm wide, 202 cm) in a niche with a top cabinet. Left wall below
the chimney: tall dark walnut column with built-in microwave and oven at eye
level. A small island (100 x 50 cm, light stone top at 90 cm) near the open
passage, dark fluted (reeded) wood panel facing the living room, counter overhang
with two black metal bar stools."""

CONSTRAINTS = """STRICT CONSTRAINTS: do not move or resize the window; do not remove the
chimney pillar; do not enlarge the room; island exactly 100x50 at the passage —
nothing larger; no cabinets above the window; nothing beyond the listed cabinets."""

PROMPTS = {
    "01-hero-od-przejscia": {
        "aspectRatio": "16:9",
        "imageSize": "2K",
        "text": f"""Architectural interior photograph. {GEOMETRY}
{STYLE}
Camera at the open passage from the living room, eye level 160 cm, 24 mm lens,
f/8, looking toward the window wall with the island in the foreground.
{CONSTRAINTS}""",
    },
    "02-wieza-i-wyspa": {
        "aspectRatio": "4:5",
        "imageSize": "2K",
        "text": f"""Architectural interior photograph. {GEOMETRY}
{STYLE}
Camera near the fridge column looking LEFT across the room at the dark walnut
tower (chimney cabinet S2 + oven column) and the island with its fluted panel
and bar stools, 35 mm lens, eye level.
{CONSTRAINTS}""",
    },
    "03-strefa-okna": {
        "aspectRatio": "16:9",
        "imageSize": "2K",
        "text": f"""Architectural interior photograph. {GEOMETRY}
{STYLE}
Camera at the island looking at the window wall: sink under the high window,
light stone worktop, LED glow under the upper cabinet right of the window,
the chimney with its dark shallow cabinet on the left edge of frame. 35 mm lens.
{CONSTRAINTS}""",
    },
}

OUT = pathlib.Path(__file__).parent / "renders"
OUT.mkdir(exist_ok=True)

def render(name: str, spec: dict) -> None:
    body = {
        "contents": [{"parts": [{"text": spec["text"]}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": spec["aspectRatio"], "imageSize": spec["imageSize"]},
        },
    }
    req = urllib.request.Request(URL, json.dumps(body).encode(), {"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        print(f"[{name}] HTTP {e.code}: {e.read().decode()[:300]}")
        return
    for part in data.get("candidates", [{}])[0].get("content", {}).get("parts", []):
        if "inlineData" in part:
            path = OUT / f"{name}.png"
            path.write_bytes(base64.b64decode(part["inlineData"]["data"]))
            print(f"[{name}] OK -> {path}")
            return
    print(f"[{name}] brak obrazu w odpowiedzi: {json.dumps(data)[:300]}")

targets = sys.argv[1:] or list(PROMPTS)
for t in targets:
    if t not in PROMPTS:
        print(f"nieznany widok: {t}; dostępne: {', '.join(PROMPTS)}")
        continue
    render(t, PROMPTS[t])
