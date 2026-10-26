#!/usr/bin/env python3
"""Kuchnia 9.02 — wariant U „Korner DIY" (przeniesienie teczki Castorama 1556_DM_17_10_2026 na wymiary z rzutu).

Jedno źródło geometrii dla rysunków (gen.py), modelu 3D (3d/) i szacunku materiałów.
Układ współrzędnych (mm), widok jak w PLAN.md v4 — „patrzysz na okno":
  x — wzdłuż ściany A (okno), 0 = ściana D (lewa, z kominem), 2450 = ściana B (prawa)
  y — w głąb od ściany A (0) do krawędzi C (1910, otwarte przejście + wnęka lodówki)
  z — wysokość od posadzki docelowej
Każdy element: (id, typ, materiał, x0, x1, y0, y1, z0, z1, etykieta).
Wartości [~] — do pomiaru kontrolnego (PLAN.md pkt 12). To NIE są formatki do cięcia.
"""
import json, os

# --- pomieszczenie (rzut 9.02) ---
W, DEPTH, H = 2450, 1910, 2490          # [P] [P] [~] (po posadzce mniej o 10–30)
PILLAR = (0, 370, 0, 630)               # komin 370×630 [P], podłoga→sufit
WIN = (600, 1520, 1680, H)              # okno x0,x1, parapet, góra [~]
PASSAGE = (0, 1740)                     # otwarte przejście na krawędzi C [P]
STUB = (1740, W)                        # odcinek ściany C (wnęka lodówki 850 zewn.) [P]

# --- wysokości ---
PL, CH, WT = 122, 720, 38               # cokół [~] / korpus dolny / blat → blat 880
Z_CARC, Z_WT, Z_TOP = PL, PL + CH, PL + CH + WT
Z_UP0, UH = 1480, 960                   # dół górnych (600 nad blatem), wys. korpusu górnego
Z_UP1 = Z_UP0 + UH                      # 2440 → blenda do sufitu ~50 [~]
LIP = 20                                # podchwyt frontu górnego (front niżej niż korpus)

# --- głębokości ---
CD, FT = 560, 18                        # korpus dolny / front → lico 578
FACE = CD + FT                          # 578
WTD = 600                               # blat
UD = 332                                # korpus górny → lico 350
SHELF_D = 220                           # regał na kominie
G = 2                                   # fuga orientacyjna (wizualnie)

E = []
def add(id_, typ, mat, x0, x1, y0, y1, z0, z1, label=""):
    E.append(dict(id=id_, type=typ, mat=mat, x0=x0, x1=x1, y0=y0, y1=y1, z0=z0, z1=z1, label=label))

# ================= CIĄG D (lewa ściana, pod kominem) — od przejścia do komina =================
# Numeracja od lewej do prawej patrząc na ścianę: D1 (przy przejściu) → D3 (przy kominie)
D_RUN = [  # (id, y0, y1, opis)
    ("D1", 1580, 1880, "cargo 300"),
    ("D2", 980, 1580, "piekarnik + płyta"),
    ("D3", 650, 980, "szuflady 3×"),
]
for id_, y0, y1, lab in D_RUN:
    add(id_, "carcass", "carcass", 0, CD, y0, y1, Z_CARC, Z_WT, lab)
# fronty D
add("D1-F", "front", "sand", CD, FACE, 1580 + G, 1880 - G, PL + 1, Z_WT - G, "cargo")
add("D2-OV", "appliance", "oven", CD, FACE + 2, 980 + G, 1580 - G, Z_WT - 2 - 595, Z_WT - 2, "piekarnik")
add("D2-F", "front", "sand", CD, FACE, 980 + G, 1580 - G, PL + 1, Z_WT - 2 - 595 - 3, "szuflada niska")
for i, (z0, z1) in enumerate([(663, 840), (393, 660), (123, 390)]):
    add(f"D3-F{i+1}", "front", "sand", CD, FACE, 650 + G, 980 - G, z0, z1, "szuflada")
add("BL1", "filler", "sand", CD, FACE, FACE, 650, PL, Z_WT, "blenda 72")          # róg D/komin
add("BW1", "endpanel", "sand", 0, FACE, 1880, 1898, 0, Z_WT, "bok wykończeniowy")
add("BLAT-D", "worktop", "stone", 0, WTD, 630, 1898, Z_WT, Z_TOP)
add("BLAT-Dn", "worktop", "stone", 370, WTD, 600, 630, Z_WT, Z_TOP)                # wcięcie przy kominie
add("HOB", "appliance", "hob", 40, 560, 985, 1575, Z_TOP, Z_TOP + 6, "płyta indukcyjna 60")

# ================= CIĄG A (ściana z oknem) — od komina do narożnika B =================
add("BL2", "filler", "sand", FACE, 622, CD, FACE, PL, Z_WT, "blenda 44")
add("D4", "carcass", "carcass", 622, 1372, 0, CD, Z_CARC, Z_WT, "zlew 750")
add("D4-F1", "front", "sand", 622 + G, 997 - 1, CD, FACE, PL + 1, Z_WT - G, "drzwi")
add("D4-F2", "front", "sand", 997 + 1, 1372 - G, CD, FACE, PL + 1, Z_WT - G, "drzwi")
add("ZM", "appliance", "dw", 1372 + 4, 1822 - 4, 20, CD - 2, PL, Z_WT - 20, "zmywarka 45")
add("ZM-F", "front", "sand", 1372 + G, 1822 - G, CD, FACE, PL + 1, Z_WT - G, "front zmywarki")
add("BD", "carcass", "carcass", 1822, 1840, 0, CD, 0, Z_WT, "bok dystansowy")
add("BL3", "filler", "sand", 1822, 1872, CD, FACE, PL, Z_WT, "blenda 50")
add("BLAT-A", "worktop", "stone", 370, W, 0, WTD, Z_WT, Z_TOP)
add("SINK", "appliance", "sink", 632, 1362, 40, 520, Z_TOP, Z_TOP + 4, "zlewozmywak 1-kom. z ociekaczem")
add("BOWL", "appliance", "bowl", 930, 1330, 80, 480, Z_TOP - 180, Z_TOP + 5)
add("TAP", "appliance", "tap", 1110, 1150, 25, 65, Z_TOP, Z_TOP + 380, "bateria")

# ================= CIĄG B (prawa ściana) — od narożnika A do lodówki =================
XB = W - CD                     # 1890 tył korpusu przy ścianie B
add("D5", "carcass", "carcass", XB, W, 0, 1050, Z_CARC, Z_WT, "narożna ślepa 1050")
add("D5-Z", "front", "sand", XB - FT, XB, 0, 600, PL + 1, Z_WT - G, "zaślepka")
add("D5-F", "front", "sand", XB - FT, XB, 600 + G, 1050 - G, PL + 1, Z_WT - G, "drzwi 450")
add("D6", "carcass", "carcass", XB, W, 1050, 1200, Z_CARC, Z_WT, "cargo 150")
add("D6-F", "front", "sand", XB - FT, XB, 1050 + G, 1200 - G, PL + 1, Z_WT - G, "cargo")
add("BW2", "endpanel", "sand", XB - FT, W, 1200, 1218, 0, Z_WT, "bok wykończeniowy")
add("BLAT-B", "worktop", "stone", W - WTD, W, WTD, 1218, Z_WT, Z_TOP)
add("LOD", "appliance", "fridge", 1800, 2400, 1230, 1830, 0, 2020, "lodówka 60×60×202")

# cokoły (cofnięte 40 za lico)
add("COK-D", "plinth", "sand", FACE - 40 - 18, FACE - 40, FACE - 40, 1880, 0, PL)
add("COK-A", "plinth", "sand", FACE - 40, XB - FT + 40, FACE - 40 - 18, FACE - 40, 0, PL)
add("COK-B", "plinth", "sand", XB - FT + 40, XB - FT + 58, FACE - 40, 1200, 0, PL)

# ================= GÓRA =================
# ściana D: G1 (przy przejściu) → G3 (przy kominie); lico 350
UP_D = [("G1", 1580, 1880, "300"), ("G2", 980, 1580, "okapowa 600"), ("G3", 650, 980, "330")]
for id_, y0, y1, lab in UP_D:
    add(id_, "carcass", "carcass_up", 0, UD, y0, y1, Z_UP0, Z_UP1, lab)
add("G1-F", "front", "walnut", UD, UD + FT, 1580 + G, 1880 - G, Z_UP0 - LIP, Z_UP1, "drzwi")
add("G3-F", "front", "walnut", UD, UD + FT, 650 + G, 980 - G, Z_UP0 - LIP, Z_UP1, "drzwi")
add("G2-F", "front", "walnut", UD, UD + FT, 980 + G, 1580 - G, 1760, Z_UP1, "drzwi nad okapem")
add("G2-OK", "front", "walnut", UD, UD + FT, 980 + G, 1580 - G, Z_UP0 - LIP, 1757, "front szuflady okapu")
add("HOOD", "appliance", "hood", 40, UD, 990, 1570, Z_UP0 - 8, Z_UP0, "okap do zabudowy 60")
add("BLG1", "filler", "walnut", UD, UD + FT, 630, 650, Z_UP0 - LIP, Z_UP1, "blenda 20")
add("BWG1", "endpanel", "walnut", 0, UD + FT, 1880, 1898, Z_UP0 - LIP, Z_UP1, "bok wykończeniowy")
add("TOP-D", "filler", "walnut", UD, UD + FT, 630, 1898, Z_UP1, H, "blenda do sufitu")
# regał R1 na licu komina (otwarte półki, orzech)
RX0, RX1 = 370, 370 + SHELF_D
add("R1-B1", "shelf", "walnut", RX0, RX1, 0, 18, Z_UP0, Z_UP1, "regał na kominie")
add("R1-B2", "shelf", "walnut", RX0, RX1, 612, 630, Z_UP0, Z_UP1)
for k, z in enumerate([Z_UP0, 1720, 1960, 2200, Z_UP1 - 18]):
    add(f"R1-P{k}", "shelf", "walnut", RX0, RX1, 18, 612, z, z + 18)
add("TOP-R", "filler", "walnut", RX1 - 18, RX1, 0, 630, Z_UP1, H)
# ściana B: G4 (przy oknie/ścianie A) → G5; lico x = 2100
XU = W - UD
UP_B = [("G4", 20, 610, "590"), ("G5", 610, 1200, "590")]
for id_, y0, y1, lab in UP_B:
    add(id_, "carcass", "carcass_up", XU, W, y0, y1, Z_UP0, Z_UP1, lab)
    add(f"{id_}-F", "front", "walnut", XU - FT, XU, y0 + G, y1 - G, Z_UP0 - LIP, Z_UP1, "drzwi")
add("BLG2", "filler", "walnut", XU - FT, XU, 0, 20, Z_UP0 - LIP, Z_UP1, "blenda 20")
add("BWG2", "endpanel", "walnut", XU - FT, W, 1200, 1218, Z_UP0 - LIP, Z_UP1, "bok wykończeniowy")
add("TOP-B", "filler", "walnut", XU - FT, XU, 0, 1218, Z_UP1, H, "blenda do sufitu")

# panel ścienny między blatem a górnymi
BS = 8
add("PAN-A", "splash", "splash", 370, W, 0, BS, Z_TOP, Z_UP0)
add("PAN-K", "splash", "splash", 370, 370 + BS, 0, 630, Z_TOP, Z_UP0)
add("PAN-Ks", "splash", "splash", 0, 370, 630, 630 + BS, Z_TOP, Z_UP0)
add("PAN-D", "splash", "splash", 0, BS, 630, 1898, Z_TOP, Z_UP0)
add("PAN-B", "splash", "splash", W - BS, W, 0, 1218, Z_TOP, Z_UP0)
# LED pod górnymi i pod regałem
add("LED-D", "led", "led", 260, 300, 650, 1880, Z_UP0 - 4, Z_UP0)
add("LED-B", "led", "led", W - 300, W - 260, 20, 1200, Z_UP0 - 4, Z_UP0)
add("LED-R", "led", "led", RX1 - 70, RX1 - 40, 18, 612, Z_UP0 - 4, Z_UP0)

ROOM = dict(W=W, D=DEPTH, H=H, pillar=PILLAR, window=WIN, passage=PASSAGE, stub=STUB,
            sill_depth=200, z_worktop=Z_TOP, z_up0=Z_UP0, z_up1=Z_UP1)

# ---------------- kontrole geometrii (twarde progi z uklady-kuchni.md / SKILL.md) ----------------
def checks():
    g = {e["id"]: e for e in E}
    out = []
    aisle = (XB - FT) - FACE
    out.append(("Przejście między ramionami U (lico D ↔ lico B)", aisle, aisle >= 1200))
    fr = g["LOD"]["x0"] - FACE
    out.append(("Lico D ↔ front lodówki", fr, fr >= 1200))
    hob = g["HOB"]
    out.append(("Płyta ↔ lico komina (y=630)", hob["y0"] - PILLAR[3], hob["y0"] - PILLAR[3] >= 300))
    out.append(("Płyta ↔ koniec ciągu D (przejście)", 1898 - hob["y1"], 1898 - hob["y1"] >= 300))
    hood_gap = g["G2-OK"]["z0"] - Z_TOP
    out.append(("Spód okapu/frontu okapu nad płytą", hood_gap, hood_gap >= 550))
    zm = g["ZM-F"]
    out.append(("Zmywarka ↔ lico ciągu B (luz przy narożniku)", (XB - FT) - zm["x1"], (XB - FT) - zm["x1"] >= 40))
    out.append(("Szczelina lodówka ↔ ściana C (zawias)", DEPTH - g["LOD"]["y1"], DEPTH - g["LOD"]["y1"] >= 50))
    out.append(("Wentylacja lodówki z tyłu", W - g["LOD"]["x1"], W - g["LOD"]["x1"] >= 50))
    win_ok = g["R1-B1"]["x1"] <= WIN[0] and g["G4-F"]["x0"] >= WIN[1]
    out.append(("Zabudowa górna nie zachodzi na okno", 0, win_ok))
    import math
    sink = ((g["BOWL"]["x0"] + g["BOWL"]["x1"]) / 2, (g["BOWL"]["y0"] + g["BOWL"]["y1"]) / 2)
    hobc = ((hob["x0"] + hob["x1"]) / 2, (hob["y0"] + hob["y1"]) / 2)
    frc = (g["LOD"]["x0"], (g["LOD"]["y0"] + g["LOD"]["y1"]) / 2)
    sides = [math.dist(sink, hobc), math.dist(hobc, frc), math.dist(frc, sink)]
    out.append(("Trójkąt: najkrótszy bok", round(min(sides)), min(sides) >= 1200))
    out.append(("Trójkąt: suma boków", round(sum(sides)), 3600 <= sum(sides) <= 7000))
    return out

# ---------------- szacunek materiałów (NIE formatki — do budżetu) ----------------
SHEET = 2.8 * 2.07
def estimate():
    carc = front_sand = front_wal = hdf = 0.0
    edge = 0.0   # mb obrzeża (orientacyjnie)
    for e in E:
        w = (e["x1"] - e["x0"]) / 1000; d = (e["y1"] - e["y0"]) / 1000; h = (e["z1"] - e["z0"]) / 1000
        if e["type"] == "carcass" and e["id"] != "BD":
            run_along_x = e["mat"] == "carcass" and e["y0"] == 0 and e["x0"] >= 600 and e["x1"] <= 1900
            width = w if run_along_x else d
            depth = d if run_along_x else w
            up = e["mat"] == "carcass_up"
            shelves = 0 if e["id"] in ("D2", "D3", "D1", "D6", "G2") else 1
            if up: shelves = 2 if e["id"] != "G2" else 1
            carc += 2 * h * depth + (2 if up else 1) * width * depth + (0 if up else 2 * width * 0.1) + shelves * width * (depth - 0.02)
            hdf += width * h
            edge += 2 * h + 2 * width + shelves * width
        elif e["id"] == "BD":
            carc += d * h
        if e["type"] in ("front", "filler", "endpanel", "plinth", "shelf"):
            dims = sorted([w, d, h])[1:]
            a = dims[0] * dims[1]
            if e["mat"] == "sand": front_sand += a
            elif e["mat"] == "walnut": front_wal += a
            edge += 2 * (dims[0] + dims[1])
    return dict(carcass_m2=carc, sand_m2=front_sand, walnut_m2=front_wal, hdf_m2=hdf, edge_mb=edge,
                sheets=dict(carcass=carc * 1.25 / SHEET, sand=front_sand * 1.35 / SHEET,
                            walnut=front_wal * 1.35 / SHEET, hdf=hdf * 1.15 / SHEET))

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(here, "3d"), exist_ok=True)
    data = json.dumps(dict(room=ROOM, elements=E), ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(here, "3d", "model.json"), "w") as f:
        f.write(data)
    # strona z modelem 3D (artefakt) = index.src.html + wstrzyknięty model
    with open(os.path.join(here, "index.src.html")) as f:
        page = f.read()
    assert "/*MODEL*/null" in page
    with open(os.path.join(here, "index.html"), "w") as f:
        f.write(page.replace("/*MODEL*/null", data))
    for name, val, ok in checks():
        print(f"{'OK ' if ok else 'BŁĄD'}  {name}: {val}")
    est = estimate()
    print({k: (round(v, 2) if isinstance(v, float) else {kk: round(vv, 2) for kk, vv in v.items()}) for k, v in est.items()})
