#!/usr/bin/env python3
# Rysunki techniczne kuchni 9.02 — wariant U „Korner DIY" (z teczki Castorama, przeliczony na rzut 9.02).
# Geometria wyłącznie z ../model.py. PNG: node ../render.mjs svg (Playwright/Chromium).
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import model as M

S = 0.3
BLUE = "#1a56c4"; WARN = "#c0392b"; WALLC = "#9a9a9a"; GZ = "#b0836a"
FILL = dict(sand="#d8ccb6", walnut="#8a5a3b", carcass="#f3efe8", carcass_up="#e9e6e1", stone="#d9d7d2",
            oven="#2b2d31", hob="#1d1e21", dw="#c9d6e8", sink="#45484d", bowl="#2f3236", tap="#222",
            fridge="#6b7078", hood="#555", splash="#ebe8e2", led="#ffd27a")

def px(mm): return mm * S
def svg_open(w, h, title, sub=""):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
         f'font-family="Arial,Helvetica,sans-serif"><rect width="{w}" height="{h}" fill="white"/>'
         f'<text x="{w/2}" y="24" text-anchor="middle" font-size="16" font-weight="bold" fill="#111">{title}</text>')
    if sub: s += f'<text x="{w/2}" y="42" text-anchor="middle" font-size="11" fill="#555">{sub}</text>'
    return s
def rect(x, y, w, h, fill="#eee", stroke="#333", sw=1, dash=None, op=1):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} fill-opacity="{op}"/>'
def line(x1, y1, x2, y2, stroke="#333", sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def txt(x, y, s, size=10, anchor="middle", fill="#111", bold=False, rot=None):
    w = ' font-weight="bold"' if bold else ''
    r = f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot is not None else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" fill="{fill}"{w}{r}>{s}</text>'
def dim_h(x1, x2, y, label, color=BLUE, size=10):
    return (line(x1, y - 4, x1, y + 4, color) + line(x2, y - 4, x2, y + 4, color) + line(x1, y, x2, y, color)
            + txt((x1 + x2) / 2, y - 3, label, size, fill=color, bold=True))
def dim_v(x, y1, y2, label, color=BLUE, side=1, size=10):
    return (line(x - 4, y1, x + 4, y1, color) + line(x - 4, y2, x + 4, y2, color) + line(x, y1, x, y2, color)
            + txt(x - 6 * side, (y1 + y2) / 2, label, size, fill=color, bold=True, rot=-90))
def hatch(x, y, w, h, color=GZ, label=""):
    pid = f"h{int(x)}{int(y)}"
    s = (f'<defs><pattern id="{pid}" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<line x1="0" y1="0" x2="0" y2="8" stroke="{color}" stroke-width="2"/></pattern></defs>'
         + rect(x, y, w, h, f"url(#{pid})", "#555", 1))
    return s + (txt(x + w / 2, y + h / 2, label, 10, fill="#333", bold=True) if label else "")

EL = {e["id"]: e for e in M.E}
def save(name, svg):
    with open(os.path.join(HERE, name + ".svg"), "w") as f: f.write(svg + "</svg>")

# ======================================================================
# 1. RZUT Z GÓRY
# ======================================================================
def rzut():
    mx, my = 110, 125
    Wp, Hp = int(px(M.W) + 2 * mx), int(px(M.DEPTH) + my + 330)
    X = lambda v: mx + px(v); Y = lambda v: my + px(v)
    s = svg_open(Wp, Hp, "RZUT Z GÓRY — kuchnia 9.02, wariant U „Korner DIY” (z teczki Castorama)",
                 "2450 × 1910 [P] · patrzysz na okno · blat h=880 · wymiary mm · do weryfikacji pomiarem")
    t = 22  # ściany
    s += rect(X(0) - t, Y(0) - t, px(M.W) + 2 * t, t, WALLC, "#555")            # A
    s += rect(X(0) - t, Y(0) - t, t, px(M.DEPTH) + t, WALLC, "#555")            # D
    s += rect(X(M.W), Y(0) - t, t, px(M.DEPTH) + t + 30, WALLC, "#555")         # B
    s += rect(X(M.STUB[0]), Y(M.DEPTH), px(M.STUB[1] - M.STUB[0]) + t, 30, WALLC, "#555")
    s += rect(X(M.WIN[0]), Y(0) - t, px(M.WIN[1] - M.WIN[0]), t, "white", BLUE, 1.5)
    s += txt(X((M.WIN[0] + M.WIN[1]) / 2), Y(0) - 7, "OKNO ~920 · parapet 1680", 9, fill=BLUE, bold=True)
    # blaty
    for k in ("BLAT-A", "BLAT-D", "BLAT-Dn", "BLAT-B"):
        e = EL[k]; s += rect(X(e["x0"]), Y(e["y0"]), px(e["x1"] - e["x0"]), px(e["y1"] - e["y0"]), "#ecebe8", "#999", 0.8)
    # korpusy dolne + fronty
    for e in M.E:
        if e["type"] == "carcass" and e["mat"] == "carcass":
            s += rect(X(e["x0"]), Y(e["y0"]), px(e["x1"] - e["x0"]), px(e["y1"] - e["y0"]), "#f3efe8", "#333", 1.1, op=0.85)
        if e["type"] in ("front", "filler", "endpanel") and e["mat"] == "sand":
            s += rect(X(e["x0"]), Y(e["y0"]), px(e["x1"] - e["x0"]), px(e["y1"] - e["y0"]), FILL["sand"], "#6b5d45", 0.8)
    s += hatch(X(0), Y(0), px(370), px(630), label="KOMIN")
    s += txt(X(185), Y(400), "370×630 [P]", 9, fill="#333")
    # górne (przerywane)
    for e in M.E:
        if e["type"] == "carcass" and e["mat"] == "carcass_up":
            s += rect(X(e["x0"]), Y(e["y0"]), px(e["x1"] - e["x0"]), px(e["y1"] - e["y0"]), "none", FILL["walnut"], 1.2, dash="5,3")
    e = EL["R1-B1"]; s += rect(X(370), Y(0), px(220), px(630), "none", FILL["walnut"], 1.2, dash="2,2")
    s += txt(X(480), Y(80), "R1 półki", 8, fill=FILL["walnut"], bold=True)
    # AGD
    h = EL["HOB"]; s += rect(X(h["x0"]), Y(h["y0"]), px(h["x1"] - h["x0"]), px(h["y1"] - h["y0"]), "#333", "#111", 1, op=0.85)
    for cy in (1130, 1430):
        for cx in (180, 420):
            s += f'<circle cx="{X(cx):.1f}" cy="{Y(cy):.1f}" r="{px(95):.1f}" fill="none" stroke="#bbb" stroke-width="1"/>'
    sk = EL["SINK"]; s += rect(X(sk["x0"]), Y(sk["y0"]), px(sk["x1"] - sk["x0"]), px(sk["y1"] - sk["y0"]), "#555", "#222", 1, op=0.75)
    b = EL["BOWL"]; s += rect(X(b["x0"]), Y(b["y0"]), px(b["x1"] - b["x0"]), px(b["y1"] - b["y0"]), "#2a2c30", "#111", 1)
    for i in range(6): s += line(X(660 + i * 40), Y(90), X(660 + i * 40), Y(470), "#999", 1)
    l = EL["LOD"]; s += rect(X(l["x0"]), Y(l["y0"]), px(l["x1"] - l["x0"]), px(l["y1"] - l["y0"]), "#c9d6e8", "#333", 1.2)
    s += txt(X(2100), Y(1510), "LODÓWKA", 10, bold=True) + txt(X(2100), Y(1580), "60×60×202 (wolnostojąca)", 8)
    # pola otwierania (kontrola kolizji)
    s += rect(X(1376), Y(578), px(442), px(600), "none", WARN, 1, dash="4,3")
    s += txt(X(1597), Y(900), "otwarta zmywarka", 8, fill=WARN)
    hx, hy, r = X(1800), Y(1830), px(600)
    s += f'<path d="M {hx:.1f} {hy - r:.1f} A {r:.1f} {r:.1f} 0 0 0 {hx - r:.1f} {hy:.1f}" fill="none" stroke="{WARN}" stroke-width="1" stroke-dasharray="4,3"/>'
    s += line(hx, hy, hx - r, hy, WARN, 1, "4,3")
    s += txt(X(1430), Y(1800), "drzwi lodówki (zawias od ściany C)", 8, fill=WARN)
    s += rect(X(578), Y(985), px(520), px(590), "none", WARN, 1, dash="4,3")
    s += txt(X(840), Y(1300), "otwarty piekarnik", 8, fill=WARN)
    # etykiety modułów
    lab = {"D1": (290, 1730, "D1 cargo 300"), "D2": (300, 1290, "D2 piekarnik+płyta 600"), "D3": (290, 815, "D3 szuflady 330"),
           "D4": (997, 545, "D4 zlew 750"), "ZM": (1597, 545, "ZM 450"), "D5": (2170, 760, "D5 narożna 1050"),
           "D6": (2170, 1125, "D6 cargo 150")}
    for k, (x, y, t_) in lab.items(): s += txt(X(x), Y(y), t_, 9, bold=True, fill="#fff" if k == "D2" else "#111")
    s += txt(X(2170), Y(300), "martwy narożnik (dostęp przez D5)", 8, fill="#666")
    s += txt(X(490), Y(450), "martwe pole", 7, fill="#666")
    s += txt(X(300), Y(1889) + 3, "BW1", 7) + txt(X(2160), Y(1209) + 3, "BW2", 7)
    # wymiary
    s += dim_h(X(0), X(M.W), Y(0) - 50, "2450 [P]")
    s += dim_h(X(0), X(370), Y(0) - 32, "370") + dim_h(X(370), X(600), Y(0) - 32, "230")
    s += dim_h(X(600), X(1520), Y(0) - 32, "okno ~920") + dim_h(X(1520), X(M.W), Y(0) - 32, "~930")
    s += dim_v(X(0) - 55, Y(0), Y(630), "630 [P]") + dim_v(X(0) - 55, Y(630), Y(1910), "1280 [P]")
    s += dim_v(X(M.W) + 58, Y(0), Y(1910), "1910 [P]", side=-1)
    yb = Y(1910) + 70
    chain = [(0, 578, "578"), (578, 622, "44"), (622, 1372, "D4 750"), (1372, 1822, "ZM 450"), (1822, 1872, "50"), (1872, 2450, "578")]
    for a, b_, t_ in chain: s += dim_h(X(a), X(b_), yb, t_, size=9)
    s += txt(X(1225), yb + 18, "ściana A — łańcuch wymiarowy na wys. blatu (lica frontów)", 9, fill=BLUE)
    s += dim_h(X(578), X(1872), Y(1350), "przejście 1294 ✓ (≥1200)", "#0a7d33")
    s += dim_h(X(578), X(1800), Y(1700), "do lodówki 1222 ✓", "#0a7d33")
    yc = Y(0) + 30
    chainD = [(630, 650, ""), (650, 980, "330"), (980, 1580, "600"), (1580, 1880, "300"), (1880, 1898, "")]
    for a, b_, t_ in chainD:
        if t_: s += dim_v(X(640), Y(a), Y(b_), t_, side=-1, size=9)
    s += line(X(0), Y(1910), X(1740), Y(1910), WARN, 2, "8,5")
    s += txt(X(870), Y(1910) + 36, "otwarte przejście 1740 [P] → przedpokój / salon", 10, fill="#555")
    # legenda
    ly = Y(1910) + 120
    s += rect(mx, ly, 14, 10, FILL["sand"], "#6b5d45") + txt(mx + 20, ly + 9, "fronty dolne — piaskowy mat", 9, "start")
    s += rect(mx + 210, ly, 14, 10, "none", FILL["walnut"], 1.2, "5,3") + txt(mx + 230, ly + 9, "górne — orzech (rzut przerywany)", 9, "start")
    s += line(mx + 440, ly + 5, mx + 470, ly + 5, WARN, 1, "4,3") + txt(mx + 476, ly + 9, "pola otwierania AGD", 9, "start")
    s += txt(Wp / 2, ly + 34, "Kolejność (od lewej, patrząc na ścianę): D: D1 → D2 → D3 | A: D4 → ZM | B: D5 → D6 → lodówka", 10, bold=True)
    s += txt(Wp / 2, ly + 52, "Płyta 355 od komina i 323 od końca ciągu (próg ≥300) · trójkąt 1300/1521/1418, suma 4239 · zlew nie nad zmywarką", 9, fill="#0a7d33")
    s += txt(Wp / 2, ly + 70, "Projekt koncepcyjno-techniczny — NIE dokumentacja produkcyjna. Formatki dopiero po pomiarach kontrolnych (PLAN.md pkt 12).", 9, fill=WARN)
    save("01-rzut-U", s)

# ======================================================================
# 2–4. ELEWACJE — wspólny rysownik
# ======================================================================
def elevation(name, title, u_of, items, extra, length, notes):
    mx, top = 90, 70
    Wp, Hp = int(px(length) + 2 * mx + 40), int(px(M.H) + top + 190)
    U = lambda v: mx + px(v); Z = lambda z: top + px(M.H - z)
    s = svg_open(Wp, Hp, title, "widok od środka kuchni · wymiary mm · [~] do pomiaru")
    s += rect(U(0), Z(M.H), px(length), px(M.H), "#fbfaf8", "#888", 1)
    s += line(U(0) - 20, Z(0), U(length) + 20, Z(0), "#333", 2)
    for e in items:
        u0, u1 = sorted(u_of(e))
        col = FILL.get(e["mat"], "#ddd")
        dash = "4,3" if e["type"] == "carcass" else None
        fill = "none" if e["type"] == "carcass" else col
        op = 0.9 if e["type"] != "splash" else 1
        s += rect(U(u0), Z(e["z1"]), px(u1 - u0), px(e["z1"] - e["z0"]), fill, "#333" if e["type"] != "splash" else "#bbb", 0.9, dash, op)
        if e["type"] == "front" and e["mat"] == "sand" and e["z1"] > 800:
            s += rect(U(u0), Z(e["z1"]), px(u1 - u0), 3, "#3a3a3a", "none", 0)  # profil uchwytowy
        if e.get("label") and e["type"] in ("front", "appliance") and px(u1 - u0) > 30 and e["id"] not in ("BOWL", "TAP", "SINK"):
            s += txt(U((u0 + u1) / 2), Z((e["z0"] + e["z1"]) / 2), "LODÓWKA" if e["id"] == "LOD" else e["id"].split("-")[0], 10, fill="#fff" if e["mat"] in ("walnut", "oven", "fridge", "hob") else "#111", bold=True)
    s = extra(s, U, Z)
    for z, lab in ((M.Z_CARC, "122"), (M.Z_WT, "842"), (M.Z_TOP, "880 blat"), (M.Z_UP0, "1480"), (M.Z_UP1, "2440"), (M.H, "2490 [~]")):
        s += line(U(length) + 8, Z(z), U(length) + 18, Z(z), BLUE) + txt(U(length) + 22, Z(z) + 4, lab, 9, "start", BLUE)
    y = Z(0) + 40
    for i, n in enumerate(notes):
        s += txt(Wp / 2, y + i * 16, n, 10 if i == 0 else 9, fill="#111" if i == 0 else "#444", bold=(i == 0))
    return s, U, Z

def chain(s, U, Z, segs, y_off=18):
    y = Z(0) + y_off
    for a, b, t in segs: s += dim_h(U(a), U(b), y, t, size=9)
    return s

# --- ściana D: patrząc na ścianę, lewo = przejście (y=1910), prawo = ściana A (y=0); u = 1910 - y
def el_D():
    items = [e for e in M.E if e["x0"] <= 0 and e["type"] in ("carcass", "front", "endpanel", "splash", "filler", "appliance")
             and e["id"] not in ("HOB",)] + [EL[k] for k in ("D1-F", "D2-F", "D2-OV", "D3-F1", "D3-F2", "D3-F3", "G1-F", "G2-F", "G2-OK", "G3-F", "BLG1", "TOP-D", "BL1", "COK-D")]
    items = list({e["id"]: e for e in items}.values())
    order = {"splash": 0, "carcass": 1}
    items.sort(key=lambda e: order.get(e["type"], 2))
    def extra(s, U, Z):
        s += hatch(U(1910 - 630), Z(M.H), px(630), px(M.H), label="KOMIN")
        s += rect(U(1910 - 1898), Z(M.Z_TOP), px(1898 - 630), px(M.WT), FILL["stone"], "#666")
        s += rect(U(1910 - 1575), Z(M.Z_TOP + 6), px(590), 3, "#111", "none")
        return s
    s, U, Z = elevation("D", "ELEWACJA ŚCIANY D (lewa, pod kominem) — płyta + piekarnik, okap w G2",
                        lambda e: (1910 - e["y0"], 1910 - e["y1"]), items, extra, 1910,
                        ["D1 cargo 300 → D2 piekarnik + indukcja 600 → D3 szuflady 330 → blenda 72 → KOMIN",
                         "Góra: G1 300 → G2 okapowa 600 (okap do zabudowy, front na szufladzie okapu) → G3 330 → blenda 20 · orzech, podchwyt 20 mm",
                         "Płyta: 355 od komina, 323 od końca ciągu — próg ≥300 ✓ · okap 580 nad płytą (≥550) ✓"])
    s = chain(s, U, Z, [(1910 - 1898, 1910 - 1880, ""), (30, 330, "D1 300"), (330, 930, "D2 600"), (930, 1260, "D3 330"),
                        (1260, 1280, ""), (1280, 1910, "komin 630")])
    save("02-elewacja-D", s)

# --- ściana A: lewo = ściana D (x=0), prawo = ściana B; u = x
def el_A():
    ids = ["PAN-A", "PAN-K", "COK-A", "BL2", "D4", "D4-F1", "D4-F2", "ZM-F", "BL3", "SINK", "TAP"] + [f"R1-P{k}" for k in range(5)] + ["R1-B1", "TOP-R"]
    items = [EL[k] for k in ids]
    def extra(s, U, Z):
        s += hatch(U(0), Z(M.H), px(370), px(M.H), label="KOMIN")
        s += rect(U(600), Z(M.H), px(920), px(M.H - 1680), "#dcebfa", BLUE, 1.5)
        s += line(U(1060), Z(M.H), U(1060), Z(1680), BLUE, 0.8) + txt(U(1060), Z(2100), "OKNO ~920 × 810", 10, fill=BLUE, bold=True)
        s += rect(U(590), Z(1680), px(940), 4, "#888", "none")
        s += hatch(U(370), Z(M.Z_WT), px(208), px(M.Z_WT), "#bbb", "")       # róg (ciąg D w przekroju)
        s += hatch(U(1872), Z(M.Z_WT), px(578), px(M.Z_WT), "#bbb", "ciąg B")
        s += hatch(U(2100), Z(M.Z_UP1), px(350), px(M.UH + 20), "#c9a98f", "G4")
        s += rect(U(370), Z(M.Z_TOP), px(2080), px(M.WT), FILL["stone"], "#666")
        return s
    s, U, Z = elevation("A", "ELEWACJA ŚCIANY A (okno) — zlew pod oknem, zmywarka obok",
                        lambda e: (e["x0"], e["x1"]), items, extra, 2450,
                        ["KOMIN + półki R1 (orzech, na licu komina) → blenda 44 → D4 zlew 750 (2 drzwi) → ZM 450 → blenda 50 → narożnik (ciąg B)",
                         "Nad blatem panel ścienny 880–1480 · brak szafek nad oknem (okno do sufitu) · ścianę między oknem a G4 zostawiamy wolną jak w teczce",
                         "Komora zlewu nad prawą częścią D4 (bateria ~70 mm na prawo od osi okna), ociekacz w stronę narożnika · zlew NIE nad zmywarką ✓"])
    s = chain(s, U, Z, [(0, 370, "komin 370"), (370, 578, "208"), (578, 622, "44"), (622, 1372, "D4 750"), (1372, 1822, "ZM 450"),
                        (1822, 1872, "50"), (1872, 2450, "ciąg B 578")])
    save("03-elewacja-A", s)

# --- ściana B: lewo = ściana A (y=0), prawo = ściana C (y=1910); u = y
def el_B():
    ids = ["PAN-B", "COK-B", "D5", "D6", "D5-F", "D6-F", "BW2", "LOD", "G4", "G5", "G4-F", "G5-F", "BLG2", "BWG2", "TOP-B"]
    items = [EL[k] for k in ids]
    def extra(s, U, Z):
        s += hatch(U(0), Z(M.Z_WT), px(578), px(M.Z_WT), "#bbb", "ciąg A (za nim zaślepka D5)")
        s += rect(U(0), Z(M.Z_TOP), px(1218), px(M.WT), FILL["stone"], "#666")
        s += hatch(U(1910), Z(M.H), 22, px(M.H), "#999", "")
        return s
    s, U, Z = elevation("B", "ELEWACJA ŚCIANY B (prawa) — narożnik, cargo, lodówka",
                        lambda e: (e["y0"], e["y1"]), items, extra, 1910,
                        ["narożnik (zaślepka D5) → D5 drzwi 450 → D6 cargo 150 → bok BW2 → szczelina 12 → LODÓWKA 600 → szczelina 80 (zawias)",
                         "Góra: blenda 20 → G4 590 → G5 590 → bok BWG2 · orzech do sufitu jak na ścianie D",
                         "Lodówka wolnostojąca 600×600×2020: 50 mm z tyłu, 80 mm od ściany C po stronie zawiasu — drzwi otwierają się ≥90° ✓"])
    s = chain(s, U, Z, [(0, 600, "narożnik 600"), (600, 1050, "D5 450"), (1050, 1200, "D6 150"), (1200, 1230, ""),
                        (1230, 1830, "lodówka 600"), (1830, 1910, "80")])
    save("04-elewacja-B", s)

if __name__ == "__main__":
    rzut(); el_D(); el_A(); el_B()
    print("ok")
