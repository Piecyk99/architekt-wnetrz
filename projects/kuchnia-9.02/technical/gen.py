#!/usr/bin/env python3
# Rysunki techniczne kuchni 9.02 — v3 (ZWERYFIKOWANE z rzutem):
# gzyms/komin 63×37 w LEWYM GÓRNYM narożniku, przejście 174 dół-LEWO, wnęka lodówki 85 dół-PRAWO, barek po LEWEJ
import os
OUT = os.path.dirname(os.path.abspath(__file__))
S = 0.3

def px(mm): return mm * S

def svg_open(w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" font-family="Arial,Helvetica,sans-serif">'
            f'<rect width="{w}" height="{h}" fill="white"/>'
            f'<text x="{w/2}" y="22" text-anchor="middle" font-size="15" font-weight="bold" fill="#111">{title}</text>')

def rect(x, y, w, h, fill="#e8e0d4", stroke="#333", sw=1.2, dash=None, opacity=1):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} opacity="{opacity}"/>'

def line(x1, y1, x2, y2, stroke="#333", sw=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def txt(x, y, s, size=11, anchor="middle", fill="#111", bold=False, rot=None):
    w = ' font-weight="bold"' if bold else ''
    r = f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot is not None else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" fill="{fill}"{w}{r}>{s}</text>'

def dim_h(x1, x2, y, label, color="#1a56c4"):
    return ''.join([line(x1, y-5, x1, y+5, color, 1), line(x2, y-5, x2, y+5, color, 1),
                    line(x1, y, x2, y, color, 1), txt((x1+x2)/2, y-4, label, 11, fill=color, bold=True)])

def dim_v(x, y1, y2, label, color="#1a56c4", side=1):
    return ''.join([line(x-5, y1, x+5, y1, color, 1), line(x-5, y2, x+5, y2, color, 1),
                    line(x, y1, x, y2, color, 1), txt(x - 8*side, (y1+y2)/2, label, 11, fill=color, bold=True, rot=-90)])

WALL = "#9a9a9a"; CAB = "#e8dcc8"; CAB2 = "#d9c9a8"; AGD = "#c9d6e8"; WARN = "#c0392b"; GZ = "#b0836a"

# ============ 1. RZUT Z GÓRY ============
M = 90
RW, RD = 2450, 1910
T = 100
W = int(px(RW) + 2*M + px(T)*2)
H = int(px(RD) + 2*M + px(T)*2 + 340)
ox, oy = M + px(T), 100 + px(T)

def X(mm): return ox + px(mm)
def Y(mm): return oy + px(mm)

e = [svg_open(W, H, "RZUT Z GÓRY v4 — kuchnia 9.02 (2450×1910) — słupek z piekarnikiem przy gzymsie + WYSPA 1000×500 po lewej")]
# walls
e.append(rect(ox-px(T), oy-px(T), px(RW)+2*px(T), px(T), WALL))                  # top wall A (okno)
e.append(rect(ox-px(T), oy-px(T), px(T), px(RD)+px(T), WALL))                    # left wall D
e.append(rect(X(RW), oy-px(T), px(T), px(RD)+2*px(T), WALL))                     # right wall B
e.append(rect(X(1740), Y(RD), px(710)+px(T), px(T), WALL))                       # ścianka dolna przy wnęce (prawa)
# GZYMS/komin 370×630 lewy górny narożnik [P z rzutu]
e.append(rect(X(0), Y(0), px(370), px(630), GZ, "#7a4a2d", 2))
e.append(txt(X(185), Y(340), "GZYMS/", 10, fill="#fff", bold=True))
e.append(txt(X(185), Y(450), "KOMIN", 10, fill="#fff", bold=True))
e.append(txt(X(185), Y(560), "370×630 [P]", 9, fill="#fff"))
# window in top wall (600..1520 od lewej ściany)
e.append(rect(X(600), oy-px(T), px(920), px(T), "#ffffff", "#1a56c4", 2))
e.append(txt(X(1060), oy-px(T)+19, "OKNO ~920 [~]", 10, fill="#1a56c4", bold=True))
# open edge bottom LEFT (0..1740) — czerwone kreskowanie na rzucie
e.append(line(X(0), Y(RD), X(1740), Y(RD), "#c0392b", 2.5, dash="12 6"))
e.append(txt(X(1180), Y(RD)+px(T)+40, "otwarte przejście 174 [P] → PRZEDPOKÓJ / SALON", 11, fill="#555"))
# cabinets wall A: od gzymsu: blenda 30 | D1 ZLEW 800 | D2 zmyw. 450 | D3 cargo 240 | D4 naroż. 560
mods_A = [(370, "", 0), (400, "", 0), (1200, "D1 ZLEW 800", 800), (1650, "D2 zmyw. 450", 450), (1890, "D3|240", 240), (2450, "D4 naroż. 560", 560)]
prev = 0
for end, label, wdt in mods_A:
    if prev >= 370:
        e.append(rect(X(prev), Y(0), px(end-prev), px(600), CAB if wdt else CAB2))
    prev = end
e.append(rect(X(660), Y(80), px(480), px(380), "#fff", "#333", 1))
e.append(txt(X(900), Y(300), "zlew", 9))
prev = 0
for end, label, wdt in mods_A:
    if wdt:
        lab = label.replace('|', ' ')
        e.append(txt(X((prev+end)/2), Y(545), lab, 9 if wdt < 300 else 10, bold=True))
    prev = end
e.append(txt(X(385), Y(300), "blenda 30", 8, rot=-90))
# cabinets wall B (prawa, od narożnika): martwe 560 | D5 płyta 600 | blenda 150 | LODÓWKA
e.append(rect(X(1850), Y(0), px(600), px(600), CAB2))
e.append(rect(X(1850), Y(600), px(600), px(560), CAB))
e.append(rect(X(1850), Y(1160), px(600), px(150), CAB2))
e.append(txt(X(2150), Y(300), "narożnik", 9, rot=-90))
e.append(txt(X(2150), Y(880), "D5 PŁYTA + szuflady", 9, rot=-90))
e.append(txt(X(2150), Y(1245), "blenda 150", 8, rot=-90))
for cy in (760, 990):
    for cx in (2010, 2290):
        e.append(f'<circle cx="{X(cx):.1f}" cy="{Y(cy):.1f}" r="{px(70):.1f}" fill="none" stroke="#333" stroke-width="1"/>')
# fridge in niche bottom-right (wnęka 85 [P])
e.append(rect(X(1820), Y(1310), px(600), px(600), AGD, "#333", 1.5))
e.append(txt(X(2120), Y(1560), "LODÓWKA", 10, bold=True))
e.append(txt(X(2120), Y(1680), "60×60×202", 9))
e.append(txt(X(2120), Y(1230), "wnęka L 85 [P]", 9, fill="#1a56c4"))
# S1: słupek z piekarnikiem przy gzymsie (lewa ściana, do sufitu)
e.append(rect(X(0), Y(630), px(600), px(600), AGD, "#333", 1.5))
e.append(txt(X(300), Y(870), "S1 SŁUPEK 600", 9, bold=True))
e.append(txt(X(300), Y(970), "piekarnik+mikrofala", 8))
e.append(txt(X(300), Y(1070), "do sufitu", 8))
# WYSPA 1000x500 po lewej, przy przejściu do salonu
e.append(rect(X(0), Y(RD-500), px(1000), px(500), CAB2, "#333", 2))
e.append(txt(X(500), Y(RD-290), "WYSPA 1000×500", 10, bold=True))
e.append(txt(X(500), Y(RD-180), "szafki od strony salonu, blat h~900", 8))
e.append(txt(X(500), Y(RD-80), "nadwieszenie na hokery od przejścia", 8))
e.append(dim_h(X(1000), X(1740), Y(RD+330), "przejście ~740 ✓ (min 700 wg decyzji)"))
e.append(dim_v(X(1080), Y(600), Y(RD-500), "alejka 810 ✓", side=-1))
# dims
e.append(dim_h(X(0), X(2450), oy-px(T)-22, "2450 wewn. [P]  (od lewej: 600 | okno ~920 | 930)"))
e.append(dim_v(ox-px(T)-25, Y(0), Y(630), "630 [P] gzyms"))
e.append(dim_v(ox-px(T)-25, Y(630), Y(1910), "1280 [P]"))
e.append(dim_v(X(RW)+px(T)+30, Y(0), Y(1910), "1910 [P]", side=-1))
e.append(dim_h(X(0), X(370), Y(700), "370 [P]", "#7a4a2d"))
# notes
yb = oy+px(RD)+px(T)+px(400)
e.append(txt(W/2, yb+60, "LODÓWKA (prawy dół) → PŁYTA D5 (prawa) → ZLEW D1 (pod oknem) → zmywarka D2 → cargo D3 | PIEKARNIK w słupku S1 przy gzymsie | WYSPA po lewej.", 10))
e.append(txt(W/2, yb+80, "WYSPA 1000×500 wg decyzji: przejście zwężone do ~740 (zaakceptowane min 700). Fronty wyspy od strony salonu — nie kolidują z alejką roboczą 810.", 10.5, fill=WARN, bold=True))
e.append(txt(W/2, yb+100, "Zweryfikowano z rzutem: gzyms 63×37 lewy-górny [P], przejście 174 dół-lewo [P], wnęka L 85 dół-prawo [P]. Pomiar na miejscu przed cięciem formatek!", 10, fill="#555"))
e.append('</svg>')
open(os.path.join(OUT, "01-rzut-z-gory-WA.svg"), "w").write(''.join(e))

# ============ 2. ELEWACJA A — ściana z oknem ============
EW, EH = 2450, 2490
M2 = 90
W2 = int(px(EW) + 2*M2 + 60)
H2 = int(px(EH) + 2*M2 + 130)
ox2, oy2 = M2 + 30, 70
def XA(mm): return ox2 + px(mm)
def YA(mm): return oy2 + px(EH - mm)

e = [svg_open(W2, H2, "ELEWACJA A — ściana z oknem (2450×2490) — gzyms po LEWEJ (370 w głąb)")]
e.append(rect(ox2, oy2, px(EW), px(EH), "#f7f4ee", "#333", 2))
# gzyms: pełna wysokość, 370 od lewej (widok z przodu — zasłania lewy skraj ściany)
e.append(rect(XA(0), YA(2490), px(370), px(2490), GZ, "#7a4a2d", 1.5))
e.append(txt(XA(185), YA(1300), "GZYMS/KOMIN 370 [P] — pełna wysokość [do potwierdzenia]", 9, fill="#fff", rot=-90))
# window 600..1520, sill 1680
e.append(rect(XA(600), YA(2490), px(920), px(810), "#dceafc", "#1a56c4", 2))
e.append(line(XA(560), YA(1680), XA(1560), YA(1680), "#1a56c4", 3))
e.append(txt(XA(1060), YA(2060), "OKNO ~920×810 [~]", 11, fill="#1a56c4", bold=True))
e.append(txt(XA(1060), YA(1600), "parapet 1680 [~]", 10, fill="#1a56c4"))
# base run: gzyms 370 | blenda 30 | D1 zlew 800 | D2 zmywarka 450 | D3 cargo 240 | D4 narożna 560
runs = [(370, 400, "", CAB2), (400, 1200, "D1|ZLEW|800", CAB), (1200, 1650, "D2|zmywarka|450", AGD), (1650, 1890, "D3|cargo|240", CAB), (1890, 2450, "D4|narożna|560", CAB)]
e.append(rect(XA(370), YA(100), px(EW-370), px(100), "#555"))
e.append(txt(XA(500), YA(25), "cokół 100", 9, fill="#fff"))
for x1, x2, label, col in runs:
    e.append(rect(XA(x1), YA(820), px(x2-x1), px(720), col))
    if label:
        for i, p in enumerate(label.split('|')):
            e.append(txt(XA((x1+x2)/2), YA(600-90*i), p, 9.5 if i < 2 else 8.5, bold=(i==1)))
e.append(rect(XA(370), YA(860), px(EW-370), px(40), "#222"))
e.append(txt(XA(2330), YA(890), "blat 38-40, góra ~860", 9, anchor="end", fill="#222"))
e.append(txt(XA(385), YA(500), "blenda 30", 8, rot=-90, fill="#555"))
# uppers: lewa strona okna zajęta przez gzyms (370..600 = tylko 200 -> półka otwarta); G2 900 po prawej
e.append(rect(XA(400), YA(2490), px(180), px(1000), "#efe6d2", "#999", 1))
e.append(txt(XA(490), YA(2280), "półka", 8, rot=-90))
e.append(rect(XA(1520), YA(2490), px(890), px(1000), CAB))
e.append(txt(XA(1965), YA(2000), "G2 890", 10, bold=True))
e.append(txt(XA(1965), YA(1880), "do sufitu", 9))
e.append(line(XA(1520), YA(1485), XA(2410), YA(1485), "#e8a13a", 3))
e.append(txt(XA(1965), YA(1450), "LED 3000K", 9, fill="#b07818"))
# dims
e.append(dim_h(XA(0), XA(2450), oy2-26, "2450 [P]"))
e.append(dim_v(ox2-25, YA(2490), YA(0), "2490 [~] (po posadzce zmierzyć!)"))
e.append(dim_h(XA(0), XA(370), YA(-70), "gzyms 370"))
e.append(dim_h(XA(400), XA(1200), YA(-70), "800"))
e.append(dim_h(XA(1200), XA(1650), YA(-70), "450"))
e.append(dim_h(XA(1650), XA(1890), YA(-70), "240"))
e.append(dim_h(XA(1890), XA(2450), YA(-70), "560"))
e.append(txt(W2/2, H2-16, "Zlew pod oknem przy podejściach wody. Nad oknem i nad gzymsem brak zabudowy. Zabudowa zaczyna się ZA gzymsem (blenda 30 docinana).", 10, fill="#555"))
e.append('</svg>')
open(os.path.join(OUT, "02-elewacja-A-okno.svg"), "w").write(''.join(e))

# ============ 3. ELEWACJA B — ściana PRAWA: płyta + lodówka ============
EW3, EH3 = 1910, 2490
W3 = int(px(EW3) + 2*M2 + 80)
H3 = int(px(EH3) + 2*M2 + 130)
ox3, oy3 = M2 + 40, 70
def XB(mm): return ox3 + px(mm)
def YB(mm): return oy3 + px(EH3 - mm)

# patrząc NA prawą ścianę: ściana z oknem po LEWEJ, wnęka/przedpokój po PRAWEJ
e = [svg_open(W3, H3, "ELEWACJA B — ściana PRAWA: płyta (szuflady pod) + lodówka (1910×2490)")]
e.append(rect(ox3, oy3, px(EW3), px(EH3), "#f7f4ee", "#333", 2))
# od lewej (od okna): narożnik 560 | D5 płyta 600 | blenda 150 | LODÓWKA 600 (wnęka 85)
e.append(rect(XB(0), YB(100), px(1310), px(100), "#555"))
e.append(txt(XB(150), YB(25), "cokół 100", 9, fill="#fff"))
runs3 = [(0, 560, "narożnik|(dostęp z D4)", CAB2), (560, 1160, "D5|600", CAB), (1160, 1310, "blenda|150", CAB2)]
for x1, x2, label, col in runs3:
    e.append(rect(XB(x1), YB(820), px(x2-x1), px(720), col))
    for i, p in enumerate(label.split('|')):
        e.append(txt(XB((x1+x2)/2), YB(640-95*i), p, 9.5 if i == 0 else 8.5, bold=(i==0 and x2-x1 > 200)))
for ymm in (300, 520):
    e.append(line(XB(560), YB(ymm+100), XB(1160), YB(ymm+100), "#999", 1))
e.append(txt(XB(860), YB(330), "szuflady pod płytą", 9))
e.append(rect(XB(0), YB(860), px(1310), px(40), "#222"))
e.append(line(XB(560), YB(905), XB(1160), YB(905), "#c0392b", 4))
e.append(txt(XB(760), YB(950), "płyta indukcyjna (560 od ściany A ✓)", 9, fill=WARN))
# hood
e.append(rect(XB(560), YB(2060), px(600), px(600), "#dcdcdc", "#333", 1.5))
e.append(txt(XB(860), YB(1780), "OKAP 600", 10, bold=True))
e.append(dim_v(XB(480), YB(1460), YB(900), "≥550"))
e.append(txt(XB(860), YB(1550), "[recyrkulacja — kratka went. do potwierdzenia]", 8, fill=WARN))
# fridge: 1310..1910, h 2020 + nadstawka
e.append(rect(XB(1330), YB(2020), px(560), px(2020), AGD, "#333", 1.5))
e.append(txt(XB(1610), YB(1100), "LODÓWKA 60", 10, bold=True, rot=-90))
e.append(txt(XB(1750), YB(1100), "h 202 (wnęka 85)", 8.5, rot=-90))
e.append(rect(XB(1330), YB(2450), px(560), px(400), CAB))
e.append(txt(XB(1610), YB(2230), "nadstawka ~400 [do pomiaru]", 8))
e.append(txt(XB(1610), YB(2070), "wentylacja 50 góra+tył, kratka w cokole/nadstawce", 7.5, fill=WARN))
# thermal note between hob and fridge
e.append(line(XB(1160), YB(100), XB(1160), YB(1540), "#c0392b", 1, dash="4 3"))
e.append(txt(XB(1240), YB(400), "bok termoizolacyjny przy lodówce (blenda 150)", 8, fill=WARN, rot=-90))
# right edge: wall to niche/przedpokój
e.append(txt(ox3+px(EW3)+16, oy3+px(EH3)/2, "dalej: ścianka wnęki / przedpokój", 9, fill="#555", rot=-90))
# dims
e.append(dim_h(XB(0), XB(1910), oy3-26, "1910 [P]"))
e.append(dim_h(XB(0), XB(560), YB(-70), "560"))
e.append(dim_h(XB(560), XB(1160), YB(-70), "600"))
e.append(dim_h(XB(1160), XB(1310), YB(-70), "150"))
e.append(dim_h(XB(1310), XB(1910), YB(-70), "600 (wnęka 85)"))
e.append(txt(W3/2, H3-16, "Płyta z dala od przejścia ✓. Lodówka otwierana od strony blatu (zawias przy ściance wnęki) — sprawdzić kierunek zawiasów!", 10, fill="#555"))
e.append('</svg>')
open(os.path.join(OUT, "03-elewacja-B-plyta-lodowka.svg"), "w").write(''.join(e))

# ============ 4. ELEWACJA D — ściana LEWA: gzyms + słupek piekarnika + wyspa ============
EW4, EH4 = 1910, 2490
W4 = int(px(EW4) + 2*M2 + 80)
H4 = int(px(EH4) + 2*M2 + 130)
ox4, oy4 = M2 + 40, 70
def XD(mm): return ox4 + px(mm)
def YD(mm): return oy4 + px(EH4 - mm)

# patrząc NA lewą ścianę: okno po PRAWEJ, przejście do salonu po LEWEJ
e = [svg_open(W4, H4, "ELEWACJA D — ściana LEWA: gzyms + słupek z piekarnikiem + wyspa (1910×2490)")]
e.append(rect(ox4, oy4, px(EW4), px(EH4), "#f7f4ee", "#333", 2))
# gzyms przy narożniku z oknem (prawa strona elewacji): 630 szer., pełna wysokość
e.append(rect(XD(1280), YD(2490), px(630), px(2490), GZ, "#7a4a2d", 1.5))
e.append(txt(XD(1595), YD(1300), "GZYMS/KOMIN 630 [P] — pełna wysokość [potwierdzić]", 9, fill="#fff", rot=-90))
# S1 słupek 600 przy gzymsie, do sufitu
e.append(rect(XD(680), YD(2490), px(600), px(2390), AGD, "#333", 1.5))
e.append(txt(XD(980), YD(2380), "S1 SŁUPEK 600 do sufitu", 9.5, bold=True))
# mikrofala 400 wys. na ~1500, piekarnik 600 wys. na ~800
e.append(rect(XD(710), YD(1900), px(540), px(400), "#3a3a3a", "#222", 1))
e.append(txt(XD(980), YD(1680), "MIKROFALA (otwór 400)", 8, fill="#fff"))
e.append(rect(XD(710), YD(1450), px(540), px(600), "#3a3a3a", "#222", 1))
e.append(txt(XD(980), YD(1130), "PIEKARNIK (otwór 600)", 8, fill="#fff"))
e.append(txt(XD(980), YD(600), "szuflady dół", 8))
e.append(txt(XD(980), YD(2200), "szafka góra", 8))
# wyspa w przekroju (bok 500 gł.) przy lewej krawędzi (strona przejścia/salonu)
e.append(rect(XD(20), YD(900), px(500), px(800), CAB2, "#333", 1.5))
e.append(rect(XD(0), YD(940), px(560), px(40), "#222"))
e.append(txt(XD(270), YD(500), "WYSPA (przekrój)", 8.5, bold=True))
e.append(txt(XD(270), YD(380), "gł. 500, blat ~900", 8))
e.append(txt(XD(270), YD(1030), "nadwieszenie blatu → hokery od salonu", 7.5, fill="#555"))
# przerwa między wyspą a słupkiem
e.append(dim_h(XD(560), XD(680), YD(-70), "~120 luz"))
e.append(txt(ox4-16, oy4+px(EH4)/2, "krawędź przejścia → salon", 9, fill="#555", rot=-90))
# dims
e.append(dim_h(XD(0), XD(1910), oy4-26, "1910 [P]"))
e.append(dim_h(XD(680), XD(1280), YD(-70), "S1 600"))
e.append(dim_h(XD(1280), XD(1910), YD(-70), "gzyms 630"))
e.append(dim_v(ox4-25, YD(2490), YD(0), "2490 [~]"))
e.append(txt(W4/2, H4-16, "Piekarnik na wysokosci (ergonomia), przy kominie — sprawdzic czy komin czynny/cieply przed montazem [do potwierdzenia].", 10, fill="#555"))
e.append('</svg>')
open(os.path.join(OUT, "04-elewacja-D-slupek-wyspa.svg"), "w").write(''.join(e))
print("OK v4")

