#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detal konstrukcyjny: górne szafki 400 przy gzymsie 15,5 biegnącym po całym obwodzie.

    python3 _detal_gzyms.py kuchnia-wyspa-detal-gzyms.pdf
"""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = sys.argv[1] if len(sys.argv) > 1 else "kuchnia-wyspa-detal-gzyms.pdf"
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVS-B", FD + "DejaVuSans-Bold.ttf"))
PW, PH = A4

INK = colors.HexColor("#1a1a1a")
WOOD = colors.HexColor("#8a6a4a")
GREY = colors.HexColor("#8a8a8a")
RED = colors.HexColor("#a05252")
BETON = colors.HexColor("#b9b2a6")
BG = colors.HexColor("#f5f1ea")
FRONT = colors.HexColor("#c9b79c")
KORP = colors.HexColor("#fbf7f0")

# --- geometria (mm rzeczywiste) ---
SUFIT = 2478
DOL_G = 1480
KORPUS_H = SUFIT - DOL_G      # 998
GL = 400                      # głębokość korpusu górnych
FR = 19
GZ = 155                      # wystawanie gzymsu [P]
LUZ = 5
WYC = GZ + LUZ                # 160
NAD = GL - WYC                # 240
HG = 250                      # ZAŁOŻONA wysokość gzymsu [?]

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Detal — górne szafki przy gzymsie 15,5")


def naglowek(tyt, pod):
    c.setFillColor(WOOD)
    c.setFont("DVS-B", 12.5)
    c.drawString(15 * mm, PH - 18 * mm, tyt)
    c.setFillColor(GREY)
    c.setFont("DVS", 7.6)
    c.drawString(15 * mm, PH - 23.5 * mm, pod)
    c.setStrokeColor(WOOD)
    c.setLineWidth(1.1)
    c.line(15 * mm, PH - 26.5 * mm, PW - 15 * mm, PH - 26.5 * mm)


def stopka(txt):
    c.setFillColor(GREY)
    c.setFont("DVS", 6.3)
    c.drawString(15 * mm, 10 * mm, txt)


def _grot(x, y, dx, dy):
    c.line(x, y, x + dx, y + dy)


def dim_h(x1, x2, y, txt, ponad=True, kolor=GREY):
    c.setStrokeColor(kolor)
    c.setLineWidth(0.4)
    c.line(x1, y, x2, y)
    for x, s in ((x1, 1), (x2, -1)):
        _grot(x, y, s * 1.6 * mm, 0.9 * mm)
        _grot(x, y, s * 1.6 * mm, -0.9 * mm)
    c.setFillColor(kolor)
    c.setFont("DVS", 6.3)
    c.drawCentredString((x1 + x2) / 2, y + (1.4 * mm if ponad else -3.1 * mm), txt)


def dim_v(y1, y2, x, txt, kolor=GREY):
    c.setStrokeColor(kolor)
    c.setLineWidth(0.4)
    c.line(x, y1, x, y2)
    for y, s in ((y1, 1), (y2, -1)):
        _grot(x, y, 0.9 * mm, s * 1.6 * mm)
        _grot(x, y, -0.9 * mm, s * 1.6 * mm)
    c.saveState()
    c.translate(x - 1.1 * mm, (y1 + y2) / 2)
    c.rotate(90)
    c.setFillColor(kolor)
    c.setFont("DVS", 6.3)
    c.drawCentredString(0, 0, txt)
    c.restoreState()


def opis(x, y, linie, kolor=INK, bold0=False, rozmiar=6.8):
    """Blok tekstu; zwraca y ostatniej linii."""
    for i, t in enumerate(linie):
        c.setFillColor(kolor if i == 0 else GREY)
        c.setFont("DVS-B" if (i == 0 and bold0) else "DVS", rozmiar)
        c.drawString(x, y - i * 3.6 * mm, t)
    return y - (len(linie) - 1) * 3.6 * mm


def leader(x1, y1, x2, y2, kolor=GREY):
    c.setStrokeColor(kolor)
    c.setLineWidth(0.35)
    c.line(x1, y1, x2, y2)
    c.circle(x2, y2, 0.5 * mm, stroke=0, fill=1)


def kreskuj(x0, y0, x1, y1, krok=1.5 * mm):
    c.saveState()
    p = c.beginPath()
    p.rect(x0, y0, x1 - x0, y1 - y0)
    c.clipPath(p, stroke=0)
    c.setStrokeColor(colors.HexColor("#9a9284"))
    c.setLineWidth(0.35)
    n = int((x1 - x0 + y1 - y0) / krok) + 2
    for i in range(n):
        xx = x0 + i * krok
        c.line(xx, y0, xx - (y1 - y0), y1)
    c.restoreState()


# =====================================================================
# STRONA 1 — przekrój pionowy
# =====================================================================
naglowek("DETAL 1/3 — PRZEKRÓJ GÓRNEJ SZAFKI PRZY GZYMSIE",
         "Gzyms wystaje 155 i biegnie po całym obwodzie. Korpus 400 gł., front przechodzi PRZED gzymsem — "
         "jedna płaszczyzna do sufitu.")

S = 0.145
XW = 74 * mm                    # lico ściany
YS = PH - 46 * mm               # sufit


def X(d):
    return XW + d * S * mm


def Y(h):
    return YS - (SUFIT - h) * S * mm


NL = SUFIT - HG - LUZ           # linia wycięcia

# mur
c.setFillColor(BETON)
c.rect(X(-42), Y(1390), 42 * S * mm, (SUFIT - 1390) * S * mm, stroke=0, fill=1)
# gzyms
c.rect(X(0), Y(SUFIT - HG), GZ * S * mm, HG * S * mm, stroke=0, fill=1)
kreskuj(X(0), Y(SUFIT - HG), X(GZ), Y(SUFIT))
c.setStrokeColor(INK)
c.setLineWidth(0.9)
c.line(X(0), Y(1390), X(0), Y(SUFIT - HG))
c.line(X(0), Y(SUFIT - HG), X(GZ), Y(SUFIT - HG))
c.line(X(GZ), Y(SUFIT - HG), X(GZ), Y(SUFIT))
c.setLineWidth(1.3)
c.line(X(-42), Y(SUFIT), X(GL + FR + 12), Y(SUFIT))

# korpus (przekrój z wycięciem)
c.setFillColor(KORP)
c.setStrokeColor(INK)
c.setLineWidth(0.9)
p = c.beginPath()
p.moveTo(X(0), Y(DOL_G))
for d, h in [(GL, DOL_G), (GL, SUFIT), (WYC, SUFIT), (WYC, NL), (0, NL)]:
    p.lineTo(X(d), Y(h))
p.close()
c.drawPath(p, stroke=1, fill=1)

# elementy
c.setFillColor(WOOD)
c.rect(X(0), Y(DOL_G), GL * S * mm, 18 * S * mm, stroke=0, fill=1)                 # dno
c.rect(X(WYC), Y(SUFIT - 18), NAD * S * mm, 18 * S * mm, stroke=0, fill=1)         # wieniec 240
c.rect(X(WYC), Y(NL - 18), NAD * S * mm, 18 * S * mm, stroke=0, fill=1)            # półka stała
c.setFillColor(colors.HexColor("#d8c8ae"))
c.rect(X(12), Y(1935), 376 * S * mm, 16 * S * mm, stroke=0, fill=1)                # półka ruchoma
c.setFillColor(GREY)
c.rect(X(-3), Y(DOL_G), 3 * S * mm, (NL - DOL_G) * S * mm, stroke=0, fill=1)       # plecy
c.setFillColor(FRONT)
c.setStrokeColor(INK)
c.setLineWidth(0.6)
c.rect(X(GL), Y(DOL_G), FR * S * mm, KORPUS_H * S * mm, stroke=1, fill=1)          # front
c.setFillColor(RED)
c.rect(X(0), Y(NL - 85), 20 * S * mm, 62 * S * mm, stroke=0, fill=1)               # listwa

# --- opisy PO LEWEJ ---
yl = Y(SUFIT - HG / 2) + 3 * mm
opis(15 * mm, yl, ["GZYMS / BELKA", "wystaje 155  [P]", "wysokość Hg = ? DO POMIARU"], RED, bold0=True)
leader(52 * mm, yl - 1 * mm, X(GZ / 2), Y(SUFIT - HG / 2))
yl = Y(NL - 55)
opis(15 * mm, yl, ["LISTWA MONTAŻOWA", "mocowana POD gzymsem,", "nie przy suficie"], RED, bold0=True)
leader(52 * mm, yl - 1 * mm, X(10), Y(NL - 55))
yl = Y(1700)
opis(15 * mm, yl, ["plecy HDF 3", "od dna do linii wycięcia"], GREY, bold0=True)
leader(52 * mm, yl - 1 * mm, X(-1.5), Y(1700))

# --- opisy PO PRAWEJ ---
XR = X(GL + FR) + 12 * mm
yr = Y(SUFIT - 30)
opis(XR, yr, ["wieniec górny 240"], INK, bold0=True)
leader(XR - 2 * mm, yr + 0.8 * mm, X(GL - 60), Y(SUFIT - 9))
yr = Y(NL - 20)
opis(XR, yr, ["półka STAŁA na linii wycięcia", "usztywnia korpus + oparcie", "dla zawieszek"], INK, bold0=True)
leader(XR - 2 * mm, yr + 0.8 * mm, X(GL - 60), Y(NL - 9))
yr = Y(1943)
opis(XR, yr, ["półka ruchoma 380"], INK, bold0=True)
leader(XR - 2 * mm, yr + 0.8 * mm, X(GL - 60), Y(1943))
yr = Y(DOL_G + 60)
opis(XR, yr, ["dno 400"], INK, bold0=True)
leader(XR - 2 * mm, yr + 0.8 * mm, X(GL - 60), Y(DOL_G + 9))
yr = Y(DOL_G - 40)
opis(XR, yr, ["front 19 — jedna płaszczyzna", "od blatu aż do sufitu;", "gzymsu od przodu nie widać"], WOOD, bold0=True)
leader(XR - 2 * mm, yr + 0.8 * mm, X(GL + FR / 2), Y(DOL_G + 200))

c.setFillColor(GREY)
c.setFont("DVS", 6.3)
c.drawString(X(GL + FR + 14), Y(SUFIT) + 1.6 * mm, "SUFIT 2478")
c.drawRightString(X(-70), Y(DOL_G) - 1 * mm, "1480")
c.setFont("DVS-B", 6.3)
c.drawRightString(X(-70), Y(DOL_G) + 3 * mm, "dół górnych")

# wymiary
dim_h(X(0), X(GZ), Y(SUFIT) + 8 * mm, "155")
dim_v(Y(NL), Y(SUFIT), X(-20), "Hg + 5", RED)
dim_v(Y(DOL_G), Y(SUFIT), X(-62), "korpus 998")
dim_h(X(0), X(WYC), Y(DOL_G) - 9 * mm, "wycięcie 160", ponad=False, kolor=RED)
dim_h(X(WYC), X(GL), Y(DOL_G) - 17 * mm, "zostaje 240", ponad=False)
dim_h(X(0), X(GL + FR), Y(DOL_G) - 25 * mm, "419 całkowitej (z frontem)", ponad=False)

# ramka "dlaczego 400"
c.setFillColor(BG)
c.rect(15 * mm, 24 * mm, PW - 30 * mm, 32 * mm, stroke=0, fill=1)
c.setFillColor(RED)
c.setFont("DVS-B", 8.5)
c.drawString(19 * mm, 49 * mm, "DLACZEGO 400, A NIE STANDARDOWE 320")
c.setFillColor(INK)
c.setFont("DVS", 7.4)
for i, t in enumerate([
        "Gzyms zabiera 160 mm głębokości w swoim paśmie. Przy korpusie 320 zostałoby tam tylko 160 mm — górna półka byłaby bezużyteczna.",
        "Przy 400 zostaje 240 mm, czyli półka realnie działa (talerze deserowe, słoiki, rzeczy sezonowe).",
        "Koszt decyzji: front stoi 80 mm bliżej głowy — cofnięcie od lica blatu 181 mm zamiast 261 mm. Przy wzroście 182 cm i dolnej",
        "krawędzi 1480 to jest do przyjęcia; nad indukcją i tak wisi okap, więc pod szafkę się nie pochylasz."]):
    c.drawString(19 * mm, (43.5 - i * 4.4) * mm, t)

stopka("Hg (wysokość gzymsu) przyjęto na rysunku 250 mm — DO POMIARU. Kuchnia U + ramię L · detal gzymsu · 2026-08-12")
c.showPage()

# =====================================================================
# STRONA 2 — formatka boku + tabela Hg
# =====================================================================
naglowek("DETAL 2/3 — FORMATKA BOKU I WYCIĘCIE",
         "Wycinasz TYLKO boki. Wieniec górny zamawiasz węższy (240). Fronty i dno bez zmian.")

FS = 0.135
FX = 30 * mm
FY = PH - 44 * mm


def BX(d):
    return FX + d * FS * mm


def BY(h):
    return FY - (KORPUS_H - h) * FS * mm


c.setFillColor(colors.HexColor("#efe6d6"))
c.setStrokeColor(INK)
c.setLineWidth(1.0)
p = c.beginPath()
p.moveTo(BX(0), BY(0))
for d, h in [(GL, 0), (GL, KORPUS_H - HG - LUZ), (GL - WYC, KORPUS_H - HG - LUZ),
             (GL - WYC, KORPUS_H), (0, KORPUS_H)]:
    p.lineTo(BX(d), BY(h))
p.close()
c.drawPath(p, stroke=1, fill=1)

# strefa wycięcia zaznaczona
c.setStrokeColor(RED)
c.setLineWidth(0.5)
c.setDash(2, 2)
c.rect(BX(GL - WYC), BY(KORPUS_H - HG - LUZ), WYC * FS * mm, (HG + LUZ) * FS * mm, stroke=1, fill=0)
c.setDash()
c.setFillColor(RED)
c.setFont("DVS-B", 7)
c.drawString(BX(GL - WYC) + 2 * mm, BY(KORPUS_H - 45), "WYCIĘCIE")
c.setFillColor(GREY)
c.setFont("DVS", 6.3)
c.drawString(BX(GL - WYC) + 2 * mm, BY(KORPUS_H - 72), "wyrzynarka,")
c.drawString(BX(GL - WYC) + 2 * mm, BY(KORPUS_H - 100), "krawędź surowa")
c.drawString(BX(GL - WYC) + 2 * mm, BY(KORPUS_H - 128), "(niewidoczna)")

dim_h(BX(GL - WYC), BX(GL), BY(KORPUS_H) + 6 * mm, "160", kolor=RED)
dim_v(BY(KORPUS_H - HG - LUZ), BY(KORPUS_H), BX(GL) + 9 * mm, "Hg + 5", RED)
dim_h(BX(0), BX(GL), BY(0) - 8 * mm, "400", ponad=False)
dim_v(BY(0), BY(KORPUS_H), BX(0) - 7 * mm, "998")
c.setFillColor(GREY)
c.setFont("DVS", 6.3)
c.drawRightString(BX(GL), BY(KORPUS_H) + 12 * mm, "TYŁ (ściana) →")
c.drawString(BX(0), BY(KORPUS_H) + 12 * mm, "← PRZÓD (front)")

# opisy po prawej
XO = 112 * mm
yo = PH - 48 * mm
c.setFillColor(WOOD)
c.setFont("DVS-B", 8.5)
c.drawString(XO, yo, "OTWORY W BOKU (jak w instrukcji montażu)")
yo -= 6 * mm
c.setFillColor(INK)
c.setFont("DVS", 7)
for t in ["• konfirmaty dna: oś 9 mm od krawędzi dolnej",
          "• półka stała: oś 9 mm na linii wycięcia",
          "• wieniec 240: oś 9 mm od krawędzi górnej",
          "• puszki 35 pod zawiasy: 22,5 mm od krawędzi przedniej",
          "• zawieszki: przy półce stałej, nie przy wieńcu"]:
    c.drawString(XO, yo, t)
    yo -= 4.6 * mm

yo -= 3 * mm
c.setFillColor(RED)
c.setFont("DVS-B", 8.5)
c.drawString(XO, yo, "TRZY RZECZY, KTÓRE MOŻNA TU ZEPSUĆ")
yo -= 6 * mm
c.setFillColor(INK)
c.setFont("DVS", 7)
for t in ["1. Boki są LUSTRZANE — wycięcie zawsze od strony",
          "     ściany, otwory zawsze od wewnątrz szafki.",
          "2. Wycięcie za ciasne — zawsze +5 mm luzu; ściana",
          "     i gzyms nigdy nie są idealnie równe.",
          "3. Listwa montażowa przykręcona do sufitu zamiast",
          "     pod gzyms — szafki nie da się zawiesić."]:
    c.drawString(XO, yo, t)
    yo -= 4.4 * mm

# tabela Hg
ty = 92 * mm
c.setFillColor(BG)
c.rect(15 * mm, ty - 34 * mm, PW - 30 * mm, 40 * mm, stroke=0, fill=1)
c.setFillColor(WOOD)
c.setFont("DVS-B", 8.5)
c.drawString(19 * mm, ty, "CO WYCHODZI DLA RÓŻNYCH Hg (wycięcie zawsze 160 głębokie)")
kolh = [19, 72, 108, 148]
c.setFillColor(GREY)
c.setFont("DVS-B", 6.6)
for x, t in zip(kolh, ["Hg — wysokość gzymsu", "wycięcie: wysokość", "plecy HDF: wysokość", "pasmo płytkie / pełne"]):
    c.drawString(x * mm, ty - 6 * mm, t)
c.setStrokeColor(GREY)
c.setLineWidth(0.4)
c.line(19 * mm, ty - 8 * mm, PW - 19 * mm, ty - 8 * mm)
c.setFont("DVS", 7)
for i, hg in enumerate([150, 200, 250, 300, 350]):
    yy = ty - (13 + i * 4.6) * mm
    c.setFillColor(INK if hg != HG else RED)
    c.setFont("DVS-B" if hg == HG else "DVS", 7)
    c.drawString(kolh[0] * mm, yy, f"{hg} mm" + ("  — przyjęte na rysunku" if hg == HG else ""))
    c.drawString(kolh[1] * mm, yy, f"{hg + LUZ} mm")
    c.drawString(kolh[2] * mm, yy, f"{KORPUS_H - 18 - hg - LUZ} mm")
    c.drawString(kolh[3] * mm, yy, f"{hg} / {KORPUS_H - hg} mm")

c.setFillColor(RED)
c.setFont("DVS-B", 7.4)
c.drawString(19 * mm, ty - 40 * mm, "Podaj mi Hg, a przeliczam formatki górnych i aktualizuję schemat.")

stopka("Kuchnia U + ramię L · detal gzymsu · 2026-08-12")
c.showPage()

# =====================================================================
# STRONA 3 — konsekwencje w projekcie
# =====================================================================
naglowek("DETAL 3/3 — CO ZMIENIA GZYMS PO CAŁYM OBWODZIE",
         "Dotyczy KAŻDEGO modułu sięgającego sufitu — nie tylko szafek górnych.")

y = PH - 34 * mm
c.setFillColor(RED)
c.setFont("DVS-B", 9)
c.drawString(15 * mm, y, "1. MODUŁY DO KOREKTY")
y -= 6.5 * mm
kol = [15, 56, 76, 99]
c.setFillColor(GREY)
c.setFont("DVS-B", 6.6)
for x, t in zip(kol, ["Moduł", "było", "jest", "zmiana"]):
    c.drawString(x * mm, y, t)
c.setStrokeColor(WOOD)
c.setLineWidth(0.5)
c.line(15 * mm, y - 2 * mm, PW - 15 * mm, y - 2 * mm)
y -= 7 * mm

wiersze = [
    ("GA1 nad pilastrem", "305 gł.", "245 gł.",
     "BŁĄD W PLANIE: pilaster wystaje 155, a nie 15 — korpus wisi na jego licu (155+245=400), front równo z GA2/GA3. "
     "Wycięcia NIE potrzebuje: pilaster i gzyms są w tej samej płaszczyźnie."),
    ("GA2 — okap w zabudowie", "320 gł.", "400 gł.",
     "wycięcie 160 × (Hg+5) w obu bokach; komin/kanał recyrkulacji musi zmieścić się w paśmie 240 — sprawdzić przy zakupie okapu."),
    ("GA3", "320 gł.", "400 gł.", "wycięcie jw."),
    ("GC1 / GC2 — ściana lodówki", "320 gł.", "400 gł.",
     "wycięcie jw.; w GC1 półka stała na linii wycięcia wypada idealnie pod ociekarkę na umyte naczynia ✓"),
    ("C2 — słupek cargo", "580 gł.", "580 gł.",
     "wycięcie 160 × (Hg+5) u góry obu boków; NAJWYŻSZY kosz cargo obniżyć — nie może wjeżdżać w pasmo gzymsu."),
    ("C4 — nadstawka nad lodówką", "580 gł.", "580 gł.",
     "wycięcie jw.; kratkę wentylacyjną zabudowy lodówki przenieść PONIŻEJ gzymsu."),
    ("Dolne, blaty, ramię L", "—", "bez zmian", "gzyms jest pod sufitem i nie dotyka strefy roboczej."),
]
for nz, bylo, jest, zm in wiersze:
    c.setFillColor(INK)
    c.setFont("DVS-B", 6.8)
    c.drawString(kol[0] * mm, y, nz)
    c.setFillColor(GREY)
    c.setFont("DVS", 6.8)
    c.drawString(kol[1] * mm, y, bylo)
    c.setFillColor(RED if jest != "bez zmian" else GREY)
    c.setFont("DVS-B", 6.8)
    c.drawString(kol[2] * mm, y, jest)
    c.setFillColor(INK)
    c.setFont("DVS", 6.6)
    line, yy = "", y
    for wd in zm.split():
        if c.stringWidth(line + " " + wd, "DVS", 6.6) > 94 * mm:
            c.drawString(kol[3] * mm, yy, line.strip())
            yy -= 3.5 * mm
            line = wd
        else:
            line += " " + wd
    c.drawString(kol[3] * mm, yy, line.strip())
    y = yy - 6 * mm

y -= 2 * mm
c.setFillColor(RED)
c.setFont("DVS-B", 9)
c.drawString(15 * mm, y, "2. SPRZECZNOŚĆ DO ROZSTRZYGNIĘCIA — OKNO NA ŚCIANIE B")
y -= 6.5 * mm
c.setFillColor(INK)
c.setFont("DVS", 7.2)
for t, kol_t, b in [
    ("Twoje wymiary: parapet 166 + wnęka okna 81,7 = 247,7 ≈ sufit 247,8 — czyli okno sięga SAMEGO sufitu.", INK, False),
    ("Ale gzyms biegnie „po całości\", więc przechodziłby też nad oknem. Jedno z dwojga:", INK, False),
    ("A)  247,8 mierzone do DOLNEJ KRAWĘDZI GZYMSU → prawdziwy sufit jest wyżej o Hg, a wszystkie moduły", INK, False),
    ("      „do sufitu\" (górne 998, słupek 2378, nadstawka C4) są za krótkie o Hg — trzeba je przeliczyć.", INK, False),
    ("B)  gzyms jest przerwany na odcinku okna (nadproże w licu ściany) → wysokości zostają bez zmian.", INK, False),
    ("Rozstrzyga jedno spojrzenie: stań przy ścianie B i sprawdź, czy gzyms przechodzi nad oknem, czy się na nim urywa.", RED, True),
]:
    c.setFillColor(kol_t)
    c.setFont("DVS-B" if b else "DVS", 7.2)
    c.drawString(15 * mm, y, t)
    y -= 4.6 * mm

y -= 3 * mm
c.setFillColor(RED)
c.setFont("DVS-B", 9)
c.drawString(15 * mm, y, "3. POMIAR, KTÓREGO MI BRAKUJE — 2 MINUTY")
y -= 6.5 * mm
c.setFillColor(INK)
c.setFont("DVS", 7.2)
for t in [
    "Hg = wysokość gzymsu. Zmierz od sufitu do dolnej krawędzi gzymsu (albo od podłogi do dolnej krawędzi —",
    "wtedy Hg = 2478 minus ta wartość). Zmierz w 3 miejscach: ściana A (indukcja), ściana C (lodówka), ściana B przy oknie.",
    "Jeśli wartości różnią się o więcej niż 10 mm — przyjmujemy NAJWIĘKSZĄ; wycięcie musi zmieścić najgorszy przypadek.",
]:
    c.drawString(15 * mm, y, t)
    y -= 4.6 * mm

stopka("Po podaniu Hg → przeliczam formatki górnych (400 / GA1 245) i aktualizuję schemat kuchni. "
       "Kuchnia U + ramię L · detal gzymsu · 2026-08-12")
c.showPage()
c.save()
print("OK:", OUT)
