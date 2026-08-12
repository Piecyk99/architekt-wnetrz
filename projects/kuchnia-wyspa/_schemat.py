#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Schemat techniczny kuchni z wyspą v2.5 — rzut + elewacje (PDF, wektor)."""
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
WOOD = colors.HexColor("#8a6a4a")
DIMC = colors.HexColor("#a05252")
GREY = colors.HexColor("#8a8a8a")

c = canvas.Canvas(OUT, pagesize=(PW, PH))
c.setTitle("Kuchnia z wyspą — schemat v2.5")


class V:
    """widok w skali: cm -> pt; y rośnie W DÓŁ (jak rzut)"""
    def __init__(self, ox, oy, scale):
        self.ox, self.oy, self.s = ox, oy, scale

    def xy(self, x, y):
        return self.ox + x * self.s, self.oy - y * self.s

    def rect(self, x, y, w, h, fill=None, stroke=INK, lw=0.8, dash=None):
        X, Y = self.xy(x, y + h)
        c.saveState()
        if dash: c.setDash(*dash)
        c.setLineWidth(lw)
        c.setStrokeColor(stroke)
        if fill:
            c.setFillColor(fill)
            c.rect(X, Y, w * self.s, h * self.s, stroke=1, fill=1)
        else:
            c.rect(X, Y, w * self.s, h * self.s, stroke=1, fill=0)
        c.restoreState()

    def line(self, x1, y1, x2, y2, lw=0.8, col=INK, dash=None):
        c.saveState()
        if dash: c.setDash(*dash)
        c.setLineWidth(lw)
        c.setStrokeColor(col)
        a, b = self.xy(x1, y1); d, e = self.xy(x2, y2)
        c.line(a, b, d, e)
        c.restoreState()

    def text(self, x, y, s, size=6.5, bold=False, col=INK, angle=0, center=False):
        X, Y = self.xy(x, y)
        c.saveState()
        c.setFillColor(col)
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
    c.drawString(15 * mm, 8 * mm, "Kuchnia z wyspą — schemat koncepcyjny v2.5 · 2026-08-12 · wymiary w cm · "
                 "wartości robocze [~] do weryfikacji pomiarem — NIE do produkcji formatek")
    c.drawRightString(PW - 15 * mm, 8 * mm, f"str. {c.getPageNumber()}")
    c.setStrokeColor(WOOD); c.setLineWidth(1)
    c.line(15 * mm, PH - 21 * mm, PW - 15 * mm, PH - 21 * mm)


# ================= STRONA 1: RZUT Z GÓRY =================
header("RZUT Z GÓRY — układ v2.5", "skala ~1:15 · orientacja: patrzysz na ścianę A (indukcja); B = okno (prawa), C = lodówka (dół), lewa = korytarz")
s = (PH - 60 * mm) / 275.0
v = V(52 * mm, PH - 30 * mm, s)

AX, JX, JY = 260.0, 193.0, 15.5   # ściana A dł., uskok od x=193, głęb. 15,5
BX, CY = 260.0, 254.6             # x ściany B, y ściany C
# ściany (grubość 8)
v.rect(-8, -8, AX + 16, 8, fill=WALL)                      # A (część lewa, tło)
v.rect(JX, 0, AX - JX + 8, JY, fill=WALL)                  # uskok przy A/B
v.rect(BX, -8, 8, CY + 16, fill=WALL)                      # B
v.rect(-8, CY, AX + 16, 8, fill=WALL)                      # C
v.rect(-8, -8, 8, 120, fill=WALL)                          # lewy filar przy A (fragment)
v.text(-30, 60, "korytarz /", 6.5, col=GREY)
v.text(-30, 68, "wejście →", 6.5, col=GREY)
# okno na B (y od C: 59,7..145,3)
oy1, oy2 = CY - 145.3, CY - 59.7
v.rect(BX, oy1, 8, oy2 - oy1, fill=colors.white)
v.line(BX + 4, oy1, BX + 4, oy2, 0.8, INK)
v.text(BX + 14, (oy1 + oy2) / 2 + 12, "OKNO 85,6", 6.5, angle=90)
v.text(BX + 21, (oy1 + oy2) / 2 + 16, "pod sufit, parapet ~166", 5.2, angle=90, col=GREY)
# ciąg A (od wyspy x=65 do B), głęb. 60
segsA = [(65, 45, "D1\n45"), (110, 60, "D2 INDUKCJA\n60 (piek. pod)"), (170, 90, "D3 narożna\n90 (front 45)")]
for x0, w, lab in segsA:
    v.rect(x0, 0 if x0 + w <= JX else JY, w, 60, fill=FILL)
    for i, ln in enumerate(lab.split("\n")):
        v.text(x0 + w / 2, 22 + i * 8, ln, 5.6, center=True)
# ciąg B: od narożnika w dół: martwe pole 60 / zmywarka 45 / zlew 60
segsB = [(JY, 60, "martwe pole\nnarożne"), (JY + 60, 45, "ZMYWARKA\n45"), (JY + 105, 80, "ZLEW 80\npod oknem"), (JY + 185, 54, "narożnik z C\n~54 (L)")]
for y0, h, lab in segsB:
    v.rect(BX - 60, y0, 60, h, fill=FILL)
    for i, ln in enumerate(lab.split("\n")):
        v.text(BX - 30, y0 + h / 2 - 4 + i * 8, ln, 5.4, center=True)
# ściana C od narożnika B/C: C1 niskie z blatem 94,7 | słupek ~28 | lodówka przy ściance | ścianka na 188,5 [P]
zx2 = BX - 94.7            # koniec C1 = początek zabudowy wysokiej
sc1 = BX - 188.5           # wschodnia krawędź ścianki [P]
v.rect(zx2, CY - 60, 94.7, 60, fill=FILL)                  # C1 niskie szafki z blatem
v.text(BX - 47, CY - 38, "C1 niskie + blat", 5.4, center=True)
v.text(BX - 47, CY - 29, "(L z ciągiem zlewu)", 4.8, center=True, col=GREY)
v.rect(sc1, CY - 70, 66.0, 70, fill=FILL)                  # lodówka przy ściance
v.rect(sc1 + 66.0, CY - 70, zx2 - sc1 - 66.0, 70, fill=FILL)   # słupek od strony C1
v.text(sc1 + 33, CY - 44, "LODÓWKA 60×65", 5.4, center=True)
v.text(sc1 + 33, CY - 34, "wys. 190, przy ściance", 4.6, center=True, col=GREY)
v.text(sc1 + 33, CY - 25, "+ nadstawka do sufitu", 4.6, center=True, col=GREY)
v.text(sc1 + 80, CY - 40, "słupek", 4.8, center=True)
v.text(sc1 + 80, CY - 31, "~28", 4.8, center=True)
v.line(sc1 + 66.0, CY - 70, sc1 + 66.0, CY, 0.5, GREY, dash=([2, 2], 0))
v.rect(sc1 - 9, CY - 77, 9, 77, fill=WALL)                 # ścianka na wprost krawędzi wyspy
v.text(sc1 - 14, CY - 80, "ścianka (w głąb ~77, na wprost krawędzi wyspy)", 5.0, angle=90)
# wyspa
v.rect(0, 0, 65, 118, fill=colors.HexColor("#e2d6c2"))
v.text(32, 55, "WYSPA", 7, bold=True, center=True)
v.text(32, 66, "~65 × ~118", 5.8, center=True)
v.text(32, 75, "front ryflowany od wejścia", 4.8, center=True, col=GREY)
# wymiary
v.dimh(65, BX, 0, "195", off=-16)
v.dimh(JX, BX, JY, "uskok 67 / gł. 15,5", off=-6, size=5)
v.dimv(0, CY, 0, "254,6", off=-16)
v.dimv(JY, CY, BX, "238,9", off=30)
v.dimv(CY - 145.3, CY - 59.7, BX, "okno 85,6", off=16)
v.dimv(CY - 59.7, CY, BX, "59,7", off=16)
v.dimh(zx2, BX, CY, "94,7 (C1)", off=14, size=5.5)
v.dimh(sc1, zx2, CY, "~94 (lodówka+słupek)", off=14, size=5.0)
v.dimh(sc1, BX, CY, "188,5 [P]", off=24, size=5.5)
v.dimv(118, CY - 77, 69.5, "PRZEJŚCIE 60 („drzwi\u201d)", off=0)
v.dimh(65, BX - 60, 130, "aleja ~135", off=0)
v.dimh(0, 65, 118, "~65", off=8, size=5.5)
v.text(150, 100, "● woda+odpływ [~] nisko na B — przedłużyć w zabudowie", 5.2, col=GREY)
c.showPage()

# ================= STRONA 2: ELEWACJA A =================
header("ELEWACJA A — ściana indukcji (jedyne szafki górne, do sufitu)",
       "skala ~1:15 · widok od strony alei roboczej · sufit 247,8 · blat 88 [~wg wzrostu]")
s2 = (PH - 62 * mm) / 250.0
e = V(70 * mm, PH - 30 * mm, s2)
H, BL, COK, GD = 247.8, 88.0, 10.0, 145.0   # sufit, blat, cokół, dół górnych
e.rect(0, 0, 195, H)                        # obrys ściany (run 195)
e.rect(0, H - COK, 195, COK, fill=colors.HexColor("#2e2e2e"))          # cokół
e.text(197, H - 3, "cokół 10 czarny", 5, col=GREY)
for x0, w, lab in [(0, 45, "D1 szuflady"), (45, 60, "D2 piekarnik\npod indukcją"), (105, 90, "D3 narożna (front 45)")]:
    e.rect(x0, H - BL, w, BL - COK - 4, fill=FILL)
    for i, ln in enumerate(lab.split("\n")):
        e.text(x0 + w / 2, H - BL + 30 + i * 9, ln, 5.6, center=True)
e.rect(0, H - BL - 4, 195, 4, fill=colors.HexColor("#d8cbb4"))         # blat
e.text(197, H - BL, "blat 38 trawertyn [~88]", 5, col=GREY)
e.line(45, H - BL - 4, 105, H - BL - 4, 2.2, INK)                      # indukcja w blacie
e.text(75, H - BL - 8, "INDUKCJA Bosch PXE601DC1E (wycięcie 56×49)", 5, center=True)
for x0, w, lab in [(0, 45, "G1"), (45, 60, "OKAP\nw zabudowie"), (105, 90, "G2")]:
    e.rect(x0, 0, w, H - GD, fill=colors.HexColor("#b39473"))
    for i, ln in enumerate(lab.split("\n")):
        e.text(x0 + w / 2, (H - GD) / 2 + i * 9, ln, 6, center=True, col=colors.white)
e.text(97, H - GD + 8, "LED 3000K pod górnymi", 5, center=True, col=GREY)
e.dimh(0, 195, H, "195", off=14)
e.dimv(0, H, 0, "247,8", off=-14)
e.dimv(H - BL, H, 195, "88", off=14)
e.dimv(H - GD, H - BL - 4, 195, "≥55 (okap–indukcja)", off=14, size=5)
e.dimv(0, H - GD, 195, "górne ~100+blenda", off=26, size=5)
c.showPage()

# ================= STRONA 3: ELEWACJA B =================
header("ELEWACJA B — ściana okna (BEZ szafek górnych)",
       "skala ~1:15 · okno pod sam sufit — parapet ~166 zostaje użytkowy · od lewej: narożnik z A")
e = V(60 * mm, PH - 30 * mm, s2)
W = 238.9
e.rect(0, 0, W, H)
e.rect(0, H - COK, W, COK, fill=colors.HexColor("#2e2e2e"))
for x0, w, lab in [(0, 60, "narożnik\n(martwe pole)"), (60, 45, "ZMYWARKA 45\nfront meblowy"), (105, 80, "ZLEW 80"), (185, 53.9, "narożnik z C\n~54 (L)")]:
    e.rect(x0, H - BL, w, BL - COK - 4, fill=FILL)
    for i, ln in enumerate(lab.split("\n")):
        e.text(x0 + w / 2, H - BL + 30 + i * 9, ln, 5.4, center=True)
e.rect(0, H - BL - 4, W, 4, fill=colors.HexColor("#d8cbb4"))
# okno: od prawej krawędzi (C) 59,7; szer. 85,6; od 166,1 do sufitu — na tej elewacji C jest PO PRAWEJ
wx2 = W - 59.7; wx1 = wx2 - 85.6
e.rect(wx1, 0, 85.6, H - 166.1, fill=colors.HexColor("#dcebf5"))
e.line(wx1, (H - 166.1) / 2, wx1 + 85.6, (H - 166.1) / 2, 0.5, GREY)
e.line(wx1 + 42.8, 0, wx1 + 42.8, H - 166.1, 0.5, GREY)
e.text(wx1 + 42.8, H - 166.1 + 8, "parapet ~166 (głęboki, użytkowy)", 5, center=True, col=GREY)
e.dimh(wx1, wx2, 0, "85,6", off=-8)
e.dimh(wx2, W, 0, "59,7", off=-8)
e.dimv(0, H - 166.1, wx1, "81,7", off=-10)
e.dimh(0, W, H, "238,9", off=14)
e.dimv(0, H, 0, "247,8", off=-14)
e.text(60, H + 22, "zlew pod oknem ✓ (62–142 od C vs okno 59,7–145,3) · podejścia wody przedłużyć w zabudowie", 5.4, col=GREY)
e.text(0, H + 32, "zabudowa lodówki odsunięta od tego narożnika o pas wolny ~94,7 (v2.5) — brak kolizji z oknem", 5.6, col=GREY)
c.showPage()

# ================= STRONA 4: ELEWACJA C + WYSPA =================
header("ELEWACJA C — zabudowa lodówki (do sufitu) · WYSPA od strony alei",
       "skala ~1:15 · lodówka wolnostojąca 60×65×190, luz serwisowy, wentylacja 50 tył+góra + kratki")
e = V(30 * mm, PH - 30 * mm, s2)
ZW = 188.5 + 9.0   # do ścianki [P] + ścianka (widok: ściana B po LEWEJ)
e.rect(0, 0, ZW, H)
e.rect(0, H - COK, 94.7, COK, fill=colors.HexColor("#2e2e2e"))
e.rect(0, H - BL, 94.7, BL - COK - 4, fill=FILL)                   # C1 niskie
e.rect(0, H - BL - 4, 94.7, 4, fill=colors.HexColor("#d8cbb4"))    # blat C1
e.text(47, H - 40, "C1 — niskie szafki z blatem", 5.6, center=True)
e.text(47, H - 30, "(blat ciągły z ciągu zlewowego)", 5, center=True, col=GREY)
e.text(47, H - 130, "bez wiszących [?]", 5, center=True, col=GREY)
e.rect(94.7, 0, 27.8, H, fill=colors.HexColor("#b39473"))          # słupek do sufitu
e.text(108.6, H / 2 - 10, "SŁUPEK", 5.2, center=True, col=colors.white)
e.text(108.6, H / 2, "~28", 5.2, center=True, col=colors.white)
e.rect(122.5, H - 190, 66, 190, fill=colors.HexColor("#f7f7f7"))   # lodówka przy ściance
e.text(155.5, H - 100, "LODÓWKA", 6.4, center=True, bold=True)
e.text(155.5, H - 90, "wolnostojąca 60 (wys. 190)", 5.2, center=True, col=GREY)
e.line(128.5, H - 62, 182.5, H - 62, 0.6, GREY)
e.rect(122.5, 0, 66, H - 192, fill=colors.HexColor("#b39473"))
e.text(155.5, (H - 192) / 2, "NADSTAWKA + kratka", 5.4, center=True, col=colors.white)
e.rect(188.5, 0, 9, H, fill=WALL)
e.text(201.5, H - 40, "ścianka — na wprost krawędzi wyspy (wystaje ~77)", 5.2, angle=90, col=GREY)
e.dimv(0, H, 0, "247,8", off=-14)
e.dimv(H - 190, H, ZW, "190", off=12)
e.dimv(0, H - 192, ZW, "~55", off=12)
e.dimh(0, 94.7, H, "94,7 (C1)", off=14, size=5.5)
e.dimh(94.7, 188.5, H, "~94 (słupek ~28 + lodówka ~66)", off=14, size=5.2)
e.dimh(0, 188.5, H, "188,5 [P]", off=24, size=5.5)
e.text(0, H + 34, "zawiasy lodówki od strony ścianki — drzwi otwierają się ku oknu (na słupek/C1)", 5.4, col=GREY)
# wyspa obok
w2 = V(150 * mm, PH - 30 * mm, s2)
IW, IH = 118.0, 88.0
w2.rect(0, H - IH, IW, IH - 0, fill=FILL)
w2.rect(0, H - IH - 4, IW + 3, 4, fill=colors.HexColor("#d8cbb4"))
w2.rect(0, H - 10, IW, 10, fill=colors.HexColor("#2e2e2e"))
w2.text(IW / 2, H - IH + 40, "WYSPA — widok z alei roboczej", 6, center=True, bold=True)
w2.text(IW / 2, H - IH + 52, "korpusy otwierane od alei / od wejścia [?]", 5.2, center=True, col=GREY)
w2.text(IW / 2, H - IH + 62, "od strony wejścia: panel ryflowany ciemny", 5.2, center=True, col=GREY)
w2.dimh(0, IW, H, "~118 (reguła: przejście 60)", off=14)
w2.dimv(H - IH - 4, H, IW, "88 [~]", off=12)
w2.text(0, H + 30, "Kotwienie wyspy do posadzki (kątowniki w cokole) — przed posadzką docelową zdecydować o gnieździe.", 5.4, col=GREY)
c.showPage()

c.save()
print("OK:", OUT)
