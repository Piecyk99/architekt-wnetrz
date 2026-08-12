#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Schemat techniczny kuchni U + ramię L, v3.0 — rzut + elewacje (PDF, wektor)."""
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = sys.argv[1] if len(sys.argv) > 1 else "kuchnia-wyspa-schemat.pdf"
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVS-B", FD + "DejaVuSans-Bold.ttf"))

PW, PH = landscape(A4)
INK = colors.HexColor("#1a1a1a")
WALL = colors.HexColor("#3a3a3a")
FILL = colors.HexColor("#efe9df")
TALL = colors.HexColor("#b39473")
WOOD = colors.HexColor("#8a6a4a")
DIMC = colors.HexColor("#a05252")
GREY = colors.HexColor("#8a8a8a")
BLAT = colors.HexColor("#d8cbb4")

c = canvas.Canvas(OUT, pagesize=(PW, PH))
c.setTitle("Kuchnia U + ramię L — schemat v3.0")


class V:
    def __init__(self, ox, oy, scale):
        self.ox, self.oy, self.s = ox, oy, scale

    def xy(self, x, y):
        return self.ox + x * self.s, self.oy - y * self.s

    def rect(self, x, y, w, h, fill=None, stroke=INK, lw=0.8, dash=None):
        X, Y = self.xy(x, y + h)
        c.saveState()
        if dash: c.setDash(*dash)
        c.setLineWidth(lw); c.setStrokeColor(stroke)
        if fill:
            c.setFillColor(fill); c.rect(X, Y, w * self.s, h * self.s, stroke=1, fill=1)
        else:
            c.rect(X, Y, w * self.s, h * self.s, stroke=1, fill=0)
        c.restoreState()

    def line(self, x1, y1, x2, y2, lw=0.8, col=INK, dash=None):
        c.saveState()
        if dash: c.setDash(*dash)
        c.setLineWidth(lw); c.setStrokeColor(col)
        a, b = self.xy(x1, y1); d, e = self.xy(x2, y2)
        c.line(a, b, d, e); c.restoreState()

    def text(self, x, y, s, size=6.5, bold=False, col=INK, angle=0, center=False):
        X, Y = self.xy(x, y)
        c.saveState(); c.setFillColor(col)
        c.setFont("DVS-B" if bold else "DVS", size)
        c.translate(X, Y)
        if angle: c.rotate(angle)
        (c.drawCentredString if center else c.drawString)(0, 0, s)
        c.restoreState()

    def dimh(self, x1, x2, y, label, off=0, size=6.2):
        yy = y + off
        self.line(x1, yy, x2, yy, 0.5, DIMC)
        for xx in (x1, x2):
            self.line(xx, yy - 2.5, xx, yy + 2.5, 0.5, DIMC)
        self.text((x1 + x2) / 2, yy + 1.5, label, size, col=DIMC, center=True)

    def dimv(self, y1, y2, x, label, off=0, size=6.2):
        xx = x + off
        self.line(xx, y1, xx, y2, 0.5, DIMC)
        for yy in (y1, y2):
            self.line(xx - 2.5, yy, xx + 2.5, yy, 0.5, DIMC)
        X, Y = self.xy(xx, (y1 + y2) / 2)
        c.saveState(); c.setFillColor(DIMC); c.setFont("DVS", size)
        c.translate(X - 2, Y); c.rotate(90); c.drawCentredString(0, 0, label)
        c.restoreState()


def header(title, sub):
    c.setFillColor(WOOD); c.setFont("DVS-B", 13)
    c.drawString(15 * mm, PH - 14 * mm, title)
    c.setFillColor(GREY); c.setFont("DVS", 7.5)
    c.drawString(15 * mm, PH - 19 * mm, sub)
    c.setFont("DVS", 6.5)
    c.drawString(15 * mm, 8 * mm, "Kuchnia U + ramię L — schemat koncepcyjny v3.0 · 2026-08-12 · wymiary w cm · "
                 "wartości [~] do weryfikacji pomiarem — NIE do produkcji formatek")
    c.drawRightString(PW - 15 * mm, 8 * mm, f"str. {c.getPageNumber()}")
    c.setStrokeColor(WOOD); c.setLineWidth(1)
    c.line(15 * mm, PH - 21 * mm, PW - 15 * mm, PH - 21 * mm)


# ================= STRONA 1: RZUT Z GÓRY =================
# Układ współrzędnych: origin = wewn. narożnik A/B (przy pilastrze), x -> ściana C (wschód), y -> korytarz (południe)
header("RZUT Z GÓRY — kuchnia w U z ramieniem L (v3.0)",
       "skala ~1:16 · patrzysz od korytarza na okno · A = indukcja (lewa), B = okno (góra), C = lodówka (prawa)")
s = (PH - 64 * mm) / 300.0
v = V(60 * mm, PH - 27 * mm, s)

CX = 254.6          # x wewn. lica ściany C
AEND = 262.0        # koniec ciągu A (pilaster 67 + 195)
DOOR1, DOOR2 = 262.0, 389.0   # otwór do sypialni w ścianie A (127)
SCY1, SCY2 = 188.5, 197.5     # ścianka: y wzdłuż C
ARM_L, ARM_D = 118.0, 65.0    # ramię L: długość od ściany A, głębokość

# ściany
v.rect(-8, -8, CX + 16, 8, fill=WALL)                       # B (góra)
v.rect(CX, -8, 8, 268, fill=WALL)                           # C (prawa) do ~260
v.rect(-8, 0, 8, DOOR1, fill=WALL)                          # A: od B do otworu
v.rect(-8, DOOR2, 8, 30, fill=WALL)                         # A: za otworem (fragment)
v.rect(0, 0, 15.5, 67, fill=WALL)                           # pilaster 15,5x67 przy A/B
v.text(18, 10, "pilaster ~15,5×67 [~]", 4.8, col=GREY)
# otwór do sypialni
v.line(-8, DOOR1, -8, DOOR2, 0.8, GREY, dash=([3, 3], 0))
v.line(0, DOOR1, 0, DOOR2, 0.8, GREY, dash=([3, 3], 0))
v.text(-14, (DOOR1 + DOOR2) / 2 + 24, "OTWÓR DO SYPIALNI 127 [P]", 5.6, angle=90, col=GREY)
# ścianka przy C
v.rect(CX - 77, SCY1, 77, 9, fill=WALL)
v.text(CX - 74, SCY1 - 4, "ścianka — wysięg ~77 [~], na 188,5 [P] od narożnika", 4.8, col=GREY)
# okno na B (od C: 59,7..145,3)
ox1, ox2 = CX - 145.3, CX - 59.7
v.rect(ox1, -8, ox2 - ox1, 8, fill=colors.white)
v.line(ox1, -4, ox2, -4, 0.8, INK)
v.text((ox1 + ox2) / 2, -12, "OKNO 85,6 (pod sufit, parapet ~166)", 5.4, center=True)

# ciąg B (gł. 60, od pilastra do narożnika z C1)
segsB = [(15.5, 50, "DB1\n~50"), (65.5, 45, "DB2\nZMYW. 45"), (110.5, 80, "DB3 ZLEW 80\npod oknem"), (190.5, 4.1, "")]
for x0, w, lab in segsB:
    v.rect(x0, 0, w, 60, fill=FILL)
    for i, ln in enumerate(lab.split("\n")):
        v.text(x0 + w / 2, 26 + i * 9, ln, 5.2, center=True)
# narożnik / C1 (gł. 60 od C): od narożnika z B w dół do 94,7
v.rect(CX - 60, 0, 60, 94.7, fill=FILL)
v.text(CX - 30, 40, "DC1", 5.4, center=True)
v.text(CX - 30, 49, "narożna", 4.8, center=True)
v.text(CX - 30, 58, "(niska, blat)", 4.8, center=True)
# C wysokie: słupek + lodówka (gł. 70)
v.rect(CX - 70, 94.7, 70, 28, fill=TALL)
v.text(CX - 35, 111, "C2 słupek ~28", 4.8, center=True, col=colors.white)
v.rect(CX - 70, 122.7, 70, 65.8, fill=FILL)
v.text(CX - 35, 150, "C3 LODÓWKA", 5.2, center=True)
v.text(CX - 35, 159, "60×65×190 [P]", 4.8, center=True, col=GREY)
v.text(CX - 35, 168, "+ nadstawka", 4.8, center=True, col=GREY)

# ciąg A (gł. 60): od pilastra (y=67) do ramienia
segsA = [(67, 45, "DA1|45"), (112, 60, "DA2 ⊠|INDUKCJA 60|piek. pod"), (172, 45, "DA3|45"), (217, 45, "DA4|45")]
for y0, h, lab in segsA:
    v.rect(0, y0, 60, h, fill=FILL)
    parts = lab.split("|")
    for i, ln in enumerate(parts):
        v.text(30, y0 + h / 2 - 3 * (len(parts) - 1) + i * 8, ln, 4.9, center=True)
# ramię L: y = AEND-65 .. AEND, x = 0..118
v.rect(0, AEND - ARM_D, ARM_L, ARM_D, fill=FILL)
v.rect(0, AEND - ARM_D - 2, ARM_L + 2, 2, fill=BLAT)
v.text(ARM_L / 2, AEND - 38, "RAMIĘ L („wyspa”)", 5.6, center=True, bold=True)
v.text(ARM_L / 2, AEND - 28, "blat ciągły z ciągiem A · gł. ~65", 4.8, center=True, col=GREY)
v.text(ARM_L / 2, AEND + 7, "panel ryflowany od strony sypialni", 4.6, center=True, col=GREY)

# wymiary
v.dimv(0, 67, 0, "67", off=-14, size=5.2)
v.dimv(67, AEND, 0, "195 [P]", off=-14)
v.dimv(DOOR1, DOOR2, 0, "127 [P]", off=-14, size=5.4)
v.dimh(0, CX, 0, "254,6 [P]", off=-22)
v.dimh(15.5, CX, 0, "238,9 [P] (ściana B)", off=-15, size=5.2)
v.dimv(0, SCY1, CX, "188,5 [P]", off=16)
v.dimv(0, 94.7, CX, "94,7 (C1)", off=8, size=5.2)
v.dimh(ARM_L, CX - 77, SCY1 + 4.5, "PRZEJŚCIE ~60 [P]", off=0, size=5.6)
v.dimh(0, ARM_L, AEND, "ramię ~118 [~] (reguła 60; taśma 127 → przejście 50,6)", off=14, size=5.0)
v.dimh(60, CX - 70, 140, "wnętrze U ~125–135", off=0, size=5.2)
v.text(30, 300, "← KORYTARZ (otwarte)", 5.6, col=GREY)
v.text(150, 100, "● woda+odpływ [~] nisko na B — przedłużyć w zabudowie", 5.0, col=GREY)
c.showPage()

# ================= STRONA 2: ELEWACJA A =================
header("ELEWACJA A — ciąg z indukcją (górne do sufitu) + ramię L",
       "skala ~1:15 · widok z wnętrza U · sufit 247,8 [P] · blat 88 [~ wg wzrostu] · od lewej: pilaster")
s2 = (PH - 62 * mm) / 250.0
e = V(60 * mm, PH - 30 * mm, s2)
H, BL, COK, GD = 247.8, 88.0, 10.0, 148.0
e.rect(0, 0, 195, H)
e.rect(0, H - COK, 195, COK, fill=colors.HexColor("#2e2e2e"))
for x0, w, lab in [(0, 45, "DA1\nszuflady"), (45, 60, "DA2 piekarnik\npod indukcją"), (105, 45, "DA3\nszuflady"), (150, 45, "DA4\n(ramię)")]:
    e.rect(x0, H - BL, w, BL - COK - 4, fill=FILL)
    for i, ln in enumerate(lab.split("\n")):
        e.text(x0 + w / 2, H - BL + 30 + i * 9, ln, 5.2, center=True)
e.rect(0, H - BL - 4, 195, 4, fill=BLAT)
e.line(45, H - BL - 4, 105, H - BL - 4, 2.2, INK)
e.text(75, H - BL - 8, "INDUKCJA Bosch PXE601DC1E — wycięcie 56×49 [P]", 4.8, center=True)
for x0, w, lab in [(0, 45, "GA1"), (45, 60, "GA2 OKAP\nw zabudowie"), (105, 45, "GA3"), (150, 45, "GA4")]:
    e.rect(x0, 0, w, H - GD, fill=TALL)
    for i, ln in enumerate(lab.split("\n")):
        e.text(x0 + w / 2, (H - GD) / 2 + i * 9, ln, 5.6, center=True, col=colors.white)
e.text(97, H - GD + 8, "LED 3000K pod górnymi", 5, center=True, col=GREY)
e.dimh(0, 195, H, "195 [P]", off=14)
e.dimv(0, H, 0, "247,8", off=-14)
e.dimv(H - BL, H, 195, "88 [~]", off=12)
e.dimv(H - GD, H - BL - 4, 195, "≥55 okap–indukcja", off=12, size=5)
e.dimv(0, H - GD, 195, "górne ~100 do sufitu", off=22, size=5)
e.text(0, H + 26, "za DA4 blat skręca w ramię L (~118×65, wys. 88) — wspólny blat, wieniec na końcu; front ryflowany od sypialni", 5.4, col=GREY)
c.showPage()

# ================= STRONA 3: ELEWACJA B =================
header("ELEWACJA B — ściana okna (BEZ szafek górnych)",
       "skala ~1:15 · okno pod sam sufit, parapet ~166 użytkowy · od lewej: pilaster przy A · od prawej: narożnik z C")
e = V(55 * mm, PH - 30 * mm, s2)
W = 238.9
e.rect(0, 0, W, H)
e.rect(0, H - COK, W, COK, fill=colors.HexColor("#2e2e2e"))
for x0, w, lab in [(0, 50, "DB1 ~50\n(blenda do pilastra)"), (50, 45, "DB2\nZMYWARKA 45"), (95, 80, "DB3 ZLEW 80"), (175, 4, ""), (179, 60, "narożnik z C\n(front DC1 od C)")]:
    e.rect(x0, H - BL, w, BL - COK - 4, fill=FILL)
    for i, ln in enumerate(lab.split("\n")):
        e.text(x0 + w / 2, H - BL + 30 + i * 9, ln, 5.0, center=True)
e.rect(0, H - BL - 4, W, 4, fill=BLAT)
wx2 = W - 59.7; wx1 = wx2 - 85.6
e.rect(wx1, 0, 85.6, H - 166.1, fill=colors.HexColor("#dcebf5"))
e.line(wx1, (H - 166.1) / 2, wx2, (H - 166.1) / 2, 0.5, GREY)
e.line(wx1 + 42.8, 0, wx1 + 42.8, H - 166.1, 0.5, GREY)
e.text(wx1 + 42.8, H - 166.1 + 8, "parapet ~166 (głęboki, użytkowy)", 5, center=True, col=GREY)
e.dimh(wx1, wx2, 0, "85,6", off=-8)
e.dimh(wx2, W, 0, "59,7", off=-8)
e.dimv(0, H - 166.1, wx1, "81,7", off=-10)
e.dimh(0, W, H, "238,9 [P]", off=14)
e.dimv(0, H, 0, "247,8", off=-14)
e.text(30, H + 26, "zlew pod oknem ✓ · podejścia wody nisko na tej ścianie [~] — przedłużyć w zabudowie · zero górnych (okno do sufitu)", 5.4, col=GREY)
c.showPage()

# ================= STRONA 4: ELEWACJA C + RAMIĘ =================
header("ELEWACJA C — niski ciąg, słupek, lodówka przy ściance · RAMIĘ L od wnętrza U",
       "skala ~1:15 · C: od narożnika z B (lewa) do ścianki (prawa) · lodówka wolnostojąca 60×65×190 [P]")
e = V(28 * mm, PH - 30 * mm, s2)
ZW = 188.5 + 9.0
e.rect(0, 0, ZW, H)
e.rect(0, H - COK, 94.7, COK, fill=colors.HexColor("#2e2e2e"))
e.rect(0, H - BL, 94.7, BL - COK - 4, fill=FILL)
e.rect(0, H - BL - 4, 94.7, 4, fill=BLAT)
e.text(47, H - 40, "DC1 narożna (front 45) + blenda", 5.2, center=True)
e.text(47, H - 30, "blat w L z ciągu okna", 4.8, center=True, col=GREY)
e.text(47, H - 130, "bez wiszących", 5, center=True, col=GREY)
e.rect(94.7, 0, 28, H, fill=TALL)
e.text(108.7, H / 2 - 10, "C2", 5.4, center=True, col=colors.white)
e.text(108.7, H / 2, "słupek ~28", 4.8, center=True, col=colors.white)
e.rect(122.7, H - 190, 65.8, 190, fill=colors.HexColor("#f7f7f7"))
e.text(155.6, H - 100, "C3 LODÓWKA", 6.2, center=True, bold=True)
e.text(155.6, H - 90, "wolnostojąca 60 (wys. 190)", 5.0, center=True, col=GREY)
e.line(128, H - 62, 183, H - 62, 0.6, GREY)
e.rect(122.7, 0, 65.8, H - 192, fill=TALL)
e.text(155.6, (H - 192) / 2, "C4 NADSTAWKA + kratka", 5.2, center=True, col=colors.white)
e.rect(188.5, 0, 9, H, fill=WALL)
e.text(201, H - 30, "ścianka [P] — za nią korytarz", 5.0, angle=90, col=GREY)
e.dimv(0, H, 0, "247,8", off=-14)
e.dimv(H - 190, H, ZW, "190", off=10)
e.dimv(0, H - 192, ZW, "~53", off=10)
e.dimh(0, 94.7, H, "94,7 [P]", off=14, size=5.4)
e.dimh(94.7, 188.5, H, "~94 (28+66)", off=14, size=5.2)
e.dimh(0, 188.5, H, "188,5 [P]", off=24, size=5.4)
e.text(0, H + 34, "zawiasy lodówki od strony ścianki — drzwi otwierają się ku oknu", 5.2, col=GREY)
# ramię L obok
w2 = V(178 * mm, PH - 30 * mm, s2)
IW = 118.0
w2.rect(0, H - BL, IW, BL - COK, fill=FILL)
w2.rect(0, H - BL - 4, IW + 3, 4, fill=BLAT)
w2.rect(0, H - COK, IW, COK, fill=colors.HexColor("#2e2e2e"))
w2.text(IW / 2, H - BL + 34, "RAMIĘ L — widok z wnętrza U", 5.6, center=True, bold=True)
w2.text(IW / 2, H - BL + 46, "RL1: drzwi/szuflady od tej strony", 5.0, center=True, col=GREY)
w2.text(IW / 2, H - BL + 56, "rewers (od sypialni): panel ryflowany", 5.0, center=True, col=GREY)
w2.dimh(0, IW, H, "~118 [~] (reguła: przejście 60 do ścianki)", off=14, size=5.0)
w2.dimv(H - BL - 4, H, IW, "88 [~]", off=10)
w2.text(0, H + 34, "blat ciągły z DA4; kotwienie w narożniku L", 5.2, col=GREY)
c.showPage()

c.save()
print("OK:", OUT)
