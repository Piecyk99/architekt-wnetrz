#!/usr/bin/env python3
"""One-shot Gemini render kuchni w U z ramieniem L (v3.2) — uruchom lokalnie z kluczem w env, zapisuje PNG.

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

STYLE = """Materials and finishes: walls painted warm light greige (NCS S 2002-Y);
ONE accent wall and the short partition wall beside the fridge in anthracite
(RAL 7016); light oak plank flooring. Handleless matte warm beige/cashmere lower
fronts with milled grip, upper cabinets and the tall pantry column in dark matte
walnut woodgrain to the ceiling; the fridge enclosure (freestanding fridge with
cabinet above) in matte anthracite matching the RAL 7016 wall — reading as one
dark tower. Light travertine-look laminate worktops (38 mm) at 91 cm height,
dark stone-look backsplash panel behind the hob only. The peninsula back facing
the corridor is a dark fluted (reeded) wood panel. Black matte faucet, black
granite sink, warm under-cabinet LED 3000K, black ceiling spots. No people.
Architectural Digest editorial aesthetic, warm evening-daylight mix."""

GEOMETRY = """U-shaped kitchen nook in a Polish apartment, about 2.55 m wide and 1.95 m
deep, ceiling 2.48 m, open on one side to a corridor. WINDOW WALL: a high window
(86 x 82 cm) reaching the ceiling, positioned closer to the induction side (60 cm
from that corner), sill at 166 cm kept as a deep useful ledge; below along this
wall from the left: a slim spice pull-out, a 45 cm dishwasher with cabinet front,
a single-bowl black granite sink (80 cm cabinet) DIRECTLY under the window, a
small drawer unit, then the corner; NO upper cabinets on this wall. INDUCTION
WALL (perpendicular, left): a shallow wall pilaster at the window corner, then
base cabinets with a flush induction hob and a built-in oven below, upper
cabinets to the ceiling with an integrated hood and warm LED beneath. At the end
of this run the worktop turns 90 degrees into an L-return peninsula (about 118 x
50 cm, worktop 91 cm) reaching toward the fridge side, its back clad in dark
fluted (reeded) wood facing the corridor and the living-room doorway (127 cm opening
in the wall right behind it). FRIDGE WALL (right): low cabinets with worktop
continuing around the corner from the sink run with tall upper cabinets above
reaching the ceiling, then a tall slim pantry pull-out, then a freestanding
fridge (60 cm wide, 190 cm tall) enclosed with a cabinet above it to the
ceiling, ending at a short partition wall; between the peninsula end and that
partition wall there is exactly a 60 cm pass-through into the kitchen."""

CONSTRAINTS = """STRICT CONSTRAINTS: do not move or resize the window (to the ceiling, sill
166 cm, near the induction corner); NO upper cabinets on the window wall; do
not enlarge the room; the peninsula is an L-return of the worktop, about
118 x 50, with exactly a 60 cm gap to the partition wall; the fridge stands by
the partition wall on the right-hand run; nothing beyond the listed cabinets."""

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
