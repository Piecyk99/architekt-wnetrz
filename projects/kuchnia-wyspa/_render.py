#!/usr/bin/env python3
"""One-shot Gemini render kuchni z wyspą (v2.2) — uruchom lokalnie z kluczem w env, zapisuje PNG.

    export GEMINI_API_KEY=...   # z aistudio.google.com/apikey
    cd projects/kuchnia-wyspa
    python3 _render.py                    # wszystkie widoki
    python3 _render.py 01-hero-od-wejscia # jeden widok
"""
import os, sys, json, base64, urllib.request, urllib.error, pathlib

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    sys.exit("GEMINI_API_KEY env var required (aistudio.google.com/apikey)")

MODEL = "gemini-3.1-flash-image-preview"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

STYLE = """Materials per the accepted palette: handleless matte beige/cashmere lower
fronts with milled grip, cream cabinet interiors, upper cabinets and the fridge
tower in dark matte walnut woodgrain reaching the ceiling, light travertine-look
laminate worktops (38 mm), dark stone-look backsplash panel behind the hob only,
remaining walls warm beige paint. The island front facing the entry is a dark
fluted (reeded) wood panel. Black matte faucet, black granite sink, warm
under-cabinet LED 3000K, black surface-mounted ceiling spots. No people.
Architectural Digest editorial aesthetic, warm evening-daylight mix."""

GEOMETRY = """Compact open kitchen in a Polish apartment, about 2.55 x 2.40 m, ceiling
2.48 m, open on one side to a corridor. WINDOW WALL: a high window (86 x 82 cm)
reaching the ceiling, sill at 166 cm above the floor — the sill stays as a deep
useful ledge; below the window a base run with a single-bowl black granite sink
(60 cm) directly under the window and a slim 45 cm dishwasher beside it; NO
upper cabinets on this wall. INDUCTION WALL (perpendicular, to the left when
entering): a 195 cm base run with a flush induction hob and a built-in oven
below it, upper cabinets to the ceiling with an integrated hood and LED under
them. FRIDGE: on the wall opposite the induction wall, in the corner nearest the
window — a dark walnut tall enclosure about 95 cm wide reaching the ceiling: a
freestanding fridge (60 cm wide, 190 cm tall) with a cabinet above it and a
narrow pantry unit beside it, closed off by a short partition wall on the entry
side. ISLAND: a peninsula about 118 x 65 cm, worktop at 88 cm, perpendicular to
the induction wall at its open end, leaving exactly a 60 cm gap between the
island end and the fridge enclosure / partition wall — a deliberately narrow
pass-through. Aisle between island and the sink run about 135 cm."""

CONSTRAINTS = """STRICT CONSTRAINTS: do not move or resize the window (it reaches the
ceiling, sill at 166 cm); NO upper cabinets on the window wall; do not enlarge
the room; island about 118 x 65 with exactly a 60 cm gap to the fridge
enclosure — nothing larger; fridge tower stays in the corner nearest the
window; nothing beyond the listed cabinets and appliances."""

PROMPTS = {
    "01-hero-od-wejscia": {
        "aspectRatio": "16:9",
        "imageSize": "2K",
        "text": f"""Architectural interior photograph. {GEOMETRY}
{STYLE}
Camera at the corridor entry next to the partition wall, eye level 160 cm,
24 mm lens, f/8, looking across the island toward the high window and the sink
run, the dark fridge tower catching the right edge of the frame.
{CONSTRAINTS}""",
    },
    "02-sciana-indukcji": {
        "aspectRatio": "4:5",
        "imageSize": "2K",
        "text": f"""Architectural interior photograph. {GEOMETRY}
{STYLE}
Camera at the window wall looking back along the induction run: handleless
beige base cabinets with the flush hob and oven below, dark walnut uppers to
the ceiling with the integrated hood, LED glow on the worktop, the fluted
island front visible in the foreground.
{CONSTRAINTS}""",
    },
    "03-wieza-lodowki-i-przejscie": {
        "aspectRatio": "4:5",
        "imageSize": "2K",
        "text": f"""Architectural interior photograph. {GEOMETRY}
{STYLE}
Camera in the working aisle looking toward the fridge corner: the dark walnut
fridge tower to the ceiling beside the short partition wall, the narrow 60 cm
pass-through between the island end and the tower, the sink run with the high
window on the left.
{CONSTRAINTS}""",
    },
}

def render(name, spec):
    body = {
        "contents": [{"parts": [{"text": spec["text"]}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": spec["aspectRatio"], "imageSize": spec["imageSize"]},
        },
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        print(f"[{name}] HTTP {e.code}: {e.read().decode()[:300]}")
        return
    parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
    for p in parts:
        blob = p.get("inlineData") or p.get("inline_data")
        if blob:
            out = pathlib.Path("renders"); out.mkdir(exist_ok=True)
            path = out / f"{name}.png"
            path.write_bytes(base64.b64decode(blob["data"]))
            print(f"[{name}] OK -> {path}")
            return
    print(f"[{name}] brak obrazu w odpowiedzi: {json.dumps(data)[:300]}")

if __name__ == "__main__":
    wanted = sys.argv[1:] or list(PROMPTS)
    for n in wanted:
        if n not in PROMPTS:
            print(f"nieznany widok: {n} (dostępne: {', '.join(PROMPTS)})"); continue
        render(n, PROMPTS[n])
