#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Schemat techniczny kuchni U + ramię L, v3.13 — rzut + elewacje (PDF, wektor)."""
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
RED = colors.HexColor("#a83232")
GREY = colors.HexColor("#8a8a8a")
BLAT = colors.HexColor("#d8cbb4")

c = canvas.Canvas(OUT, pagesize=(PW, PH))
c.setTitle("Kuchnia U + ramię L — schemat v3.13")


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
    c.drawString(15 * mm, 8 * mm, "Kuchnia U + ramię L — schemat koncepcyjny v3.13 · 2026-08-13 · wymiary w cm · "
                 "wartości [~] do weryfikacji pomiarem — NIE do produkcji formatek")
    c.drawRightString(PW - 15 * mm, 8 * mm, f"str. {c.getPageNumber()}")
    c.setStrokeColor(WOOD); c.setLineWidth(1)
    c.line(15 * mm, PH - 21 * mm, PW - 15 * mm, PH - 21 * mm)


# ================= STRONA 1: RZUT Z GÓRY =================
# Układ współrzędnych: origin = wewn. narożnik A/B (przy pilastrze), x -> ściana C (wschód), y -> korytarz (południe)
header("RZUT Z GÓRY — kuchnia w U z ramieniem L (v3.13)",
       "skala ~1:14 · patrzysz od korytarza na okno · A = indukcja (lewa), B = okno (góra), C = lodówka (prawa)")
s = (PH - 40 * mm) / 370.0          # zakres rzutu w pionie: -22 .. 342 (otwór do salonu za kuchnią)
v = V(62 * mm, PH - 35 * mm, s)

CX = 254.6          # x wewn. lica ściany C
AEND = 195.0        # koniec ciągu A / linia południowa [P]
DOOR1, DOOR2 = 195.0, 322.0   # otwór do salonu (127) zaraz za linią
SCY1, SCY2 = 188.5, 197.5     # ścianka wzdłuż C
ARM_L, ARM_D = 117.6, 50.0    # ramię L

# ściany
v.rect(-8, -8, CX + 16, 8, fill=WALL)                       # B
v.rect(CX, -8, 8, 240, fill=WALL)                           # C
v.rect(-8, 0, 8, DOOR1, fill=WALL)                          # A do otworu
v.rect(-8, DOOR2, 8, 20, fill=WALL)                         # A za otworem (fragment)
v.rect(0, 0, 15.5, 67, fill=WALL)                           # pilaster
v.text(18, 8, "pilaster ~15,5×67 [~] (wewnątrz wymiaru 195)", 4.8, col=GREY)
# otwór do salonu
v.line(-8, DOOR1, -8, DOOR2, 0.8, GREY, dash=([3, 3], 0))
v.line(0, DOOR1, 0, DOOR2, 0.8, GREY, dash=([3, 3], 0))
v.text(-14, (DOOR1 + DOOR2) / 2 + 30, "OTWÓR DO SALONU 127 [P]", 5.4, angle=90, col=GREY)
# ścianka
v.rect(CX - 77, SCY1, 77, 9, fill=WALL)
v.text(CX - 74, SCY1 - 4, "ścianka — wysięg ~77 [~], na 188,5 [P]", 4.8, col=GREY)
# okno
ox1, ox2 = 15.5 + 59.7, 15.5 + 59.7 + 85.6   # okno od strony pilastra [P] (korekta v3.5)
v.rect(ox1, -8, ox2 - ox1, 8, fill=colors.white)
v.line(ox1, -4, ox2, -4, 0.8, INK)
v.text((ox1 + ox2) / 2, 7, "OKNO 85,6 — pod sufit, parapet ~166,4", 4.8, center=True, col=GREY)

# ciąg B (gł. 60); narożnik zachodni (do x=60) = martwe pole bez frontu (kolizja z ciągiem A)
v.rect(0, 67, 15.5, 18, fill=colors.HexColor("#e3ddd2"))   # pustka za korpusem, poniżej pilastra
v.rect(15.5, 0, 40.5, 85, fill=FILL)                       # DA1 narożna ślepa (korpus do ściany B)
v.line(15.5, 0, 56, 61, 0.4, GREY); v.line(15.5, 61, 56, 0, 0.4, GREY)   # część ślepa
v.rect(56, 0, 4, 61, fill=colors.HexColor("#d8cfc2"))      # BLENDA zamykająca lico części ślepej
v.rect(56, 61, 4, 24, fill=BLAT)                           # DRZWI 240
v.line(56, 61, 60, 61, 0.8, GREY)
v.text(62, 88, "wyżej: blenda zamykająca lico", 4.0, col=GREY)
v.text(62, 93, "ślepej części DA1", 4.0, col=GREY)
v.text(62, 76, "← drzwi 24", 4.2, col=GREY)
v.text(36, 30, "DA1", 5.0, center=True)
v.text(36, 38, "narożna ślepa", 4.4, center=True)
v.text(36, 45, "korpus 85×40,5 = 248 l", 4.2, center=True, col=GREY)
v.text(36, 52, "front 24 · sięg bokiem 60", 4.2, center=True, col=GREY)
segsB = [(60, 15, "crg\n15"), (75, 80, "DB1 ZLEW 80\npod oknem"), (155, 45, "DB2\nZMYW. 45")]
for x0, w, lab in segsB:
    v.rect(x0, 0, w, 60, fill=FILL)
    for i, ln in enumerate(lab.split("\n")):
        v.text(x0 + w / 2, 26 + i * 9, ln, 5.2, center=True)
# C1 + C wysokie
v.rect(CX - 60, 0, 60, 94.7, fill=FILL)
v.rect(CX - 32, 0, 32, 94.7, dash=([2, 2], 0), stroke=GREY)
v.text(CX - 30, 30, "DC1", 5.4, center=True)
v.text(CX - 30, 39, "narożna", 4.8, center=True)
v.text(CX - 30, 48, "(niska, blat)", 4.8, center=True)
v.text(CX - 30, 60, "+ GC1-GC2", 4.8, center=True, col=GREY)
v.text(CX - 30, 69, "górne do sufitu", 4.4, center=True, col=GREY)
v.rect(CX - 70, 94.7, 70, 28, fill=TALL)
v.text(CX - 35, 111, "C2 słupek ~28", 4.8, center=True, col=colors.white)
v.rect(CX - 70, 122.7, 70, 65.8, fill=FILL)
v.text(CX - 35, 148, "C3 LODÓWKA", 5.2, center=True)
v.text(CX - 35, 157, "60×65×200 [P] wolnostojąca", 4.8, center=True, col=GREY)
v.text(CX - 35, 166, "+ nadstawka", 4.8, center=True, col=GREY)

# ciąg A: strefa modułowa od styku z ciągiem B (narożnik domknięty)
v.text(66, 58, "narożnik domknięty — jeden korpus obsługuje ciąg A i róg przy oknie", 4.2, col=GREY)

v.rect(0, 85, 60, 60, fill=FILL)
v.text(30, 107, "DA2 ⊠", 5.0, center=True); v.text(30, 116, "INDUKCJA 60", 4.8, center=True); v.text(30, 125, "piekarnik pod", 4.6, center=True)
v.text(150, 128, "front piekarnika kończy się", 5.0, col=GREY)
v.text(150, 135, "dokładnie na linii ramienia ✓", 5.0, col=GREY)
# ramię L: y = 130..195, x = 0..118 (południowa krawędź w linii 195, naprzeciwko ścianki)
v.rect(0, AEND - ARM_D, 60, ARM_D, fill=colors.HexColor("#e8dcd6"))     # ślepy narożnik pod ramieniem
v.line(0, AEND - ARM_D, 60, AEND, 0.4, GREY); v.line(0, AEND, 60, AEND - ARM_D, 0.4, GREY)
v.rect(60, AEND - ARM_D, ARM_L - 60, ARM_D, fill=FILL)                   # korpus ramienia (dostępny od północy)
v.rect(0, AEND - ARM_D - 2, ARM_L + 2, 2, fill=BLAT)
v.text(30, AEND - 32, "ślepy narożnik", 4.2, center=True, col=GREY)
v.text(30, AEND - 26, "202 l — sięg bokiem", 4.0, center=True, col=GREY)
v.text(30, AEND - 20, "przez drzwi ramienia", 4.0, center=True, col=GREY)
v.text((60 + ARM_L) / 2, AEND - 32, "RAMIĘ L", 5.4, center=True, bold=True)
v.text((60 + ARM_L) / 2, AEND - 24, "drzwi 30 + SZUFLADY 30 (sztućce) · gł. 46", 4.2, center=True, col=GREY)
# linia końca dostępu do ciągu A
v.line(0, AEND - ARM_D, 60, AEND - ARM_D, 0.9, GREY, dash=([3, 2], 0))
v.text(64, AEND - ARM_D - 2, "← koniec frontów ciągu A = początek ramienia (y=145)", 4.6, col=GREY)
v.text(ARM_L / 2, AEND + 7, "rewers: panel ryflowany (salon/korytarz)", 4.6, center=True, col=GREY)

# --- PILASTER: rysowany NA KOŃCU, żeby nie zniknął pod korpusem DA1 ---
PILC = colors.HexColor("#c9b7a3")
v.rect(0, 0, 15.5, 67, fill=PILC, stroke=RED, lw=1.5)
for yy in range(4, 67, 5):                     # szrafura — pilaster to MUR, nie szafka
    v.line(0, yy, 15.5, yy, 0.35, RED)
v.line(8, 67, 13, 276, 0.7, RED)                # odnośnik w wolną strefę pod kuchnią
v.text(10, 282, "PILASTER  15,5 × 67  [~ DO POMIARU]", 5.6, bold=True, col=RED)
v.text(10, 289, "pionowy uskok muru na CAŁĄ wysokość, w narożniku ściany A ze ścianą B (przy oknie)", 4.6, col=RED)
v.text(10, 295, "to on odbiera 15,5 cm głębokości ciągu A; na jego licu wisi GA1, a bok GA2 siada na jego czole", 4.6, col=RED)
v.text(10, 302, "kontrola krzyżowa: 254,6 (ściana B z pilastrem) − 238,9 (bez) = 15,7 ≈ 15,5 ✓ — ale DŁUGOŚĆ 67 jest tylko ze szkicu, nigdy nie zmierzona", 4.6, col=GREY)

# wymiary
v.dimv(0, AEND, 0, "195 [P] (od ściany B)", off=-14, size=5.6)
v.dimv(0, 67, 0, "67", off=-7, size=4.6)
v.dimv(DOOR1, DOOR2, 0, "127 [P]", off=-14, size=5.4)
v.dimh(0, CX, 0, "254,6 [P]", off=-22)
v.dimh(15.5, CX, 0, "238,9 [P] (ściana B)", off=-15, size=5.2)
v.dimv(0, SCY1, CX, "188,5 [P]", off=16)
v.dimv(0, 94.7, CX, "94,7 (C1)", off=8, size=5.2)
v.dimh(ARM_L, CX - 77, SCY1 + 4.5, "PRZEJŚCIE ~60 [P]", off=0, size=5.6)
v.dimh(0, ARM_L, AEND, "ramię ~118 [~]", off=14, size=5.2)
v.dimv(60, AEND - ARM_D, 30, "~85 strefa przy zlewie", off=0, size=4.8)
v.dimh(60, CX - 70, 100, "wnętrze U ~125", off=0, size=5.2)
v.text(30, 240, "← KORYTARZ (otwarte)", 5.6, col=GREY)
# --- LEGENDA ---
LX, LY = 118, 208
v.text(LX, LY, "LEGENDA", 5.4, bold=True, col=WOOD)
v.rect(LX, LY + 4, 14, 10, fill=colors.HexColor("#e8dcd6"))
v.line(LX, LY + 4, LX + 14, LY + 14, 0.4, GREY); v.line(LX, LY + 14, LX + 14, LY + 4, 0.4, GREY)
v.text(LX + 18, LY + 11, "przekreślone na X = CZĘŚĆ ŚLEPA szafki — bez własnego frontu, bo drzwi", 4.6, col=GREY)
v.text(LX + 18, LY + 17, "kolidowałyby z sąsiednim ciągiem. NIE jest stracona: sięgasz tam BOKIEM", 4.6, col=GREY)
v.text(LX + 18, LY + 23, "przez drzwi obok (korpus nie ma boku od tej strony). Blat idzie górą ciągiem.", 4.6, col=GREY)
v.rect(LX, LY + 28, 14, 10, fill=FILL)
v.text(LX + 18, LY + 35, "zwykła szafka z frontem", 4.6, col=GREY)
v.text(LX, LY + 48, "⊠", 6.5, col=INK)
v.text(LX + 18, LY + 47, "płyta indukcyjna w blacie (Bosch PXE601DC1E)", 4.6, col=GREY)
v.line(LX, LY + 54, LX + 14, LY + 54, 0.8, GREY, dash=([2, 2], 0))
v.text(LX + 18, LY + 56, "linia przerywana = szerokość frontu szafki narożnej ślepej", 4.6, col=GREY)
v.text(150, 78, "● woda+odpływ [~] nisko na B", 5.0, col=GREY)
v.text(ARM_L + 8, AEND - 50, "koniec ramienia NAPRZECIWKO ścianki [P]", 4.8, col=DIMC)
c.showPage()

# ================= STRONA 2: ELEWACJA A =================
header("ELEWACJA A — ciąg z indukcją (górne do sufitu) + ramię L",
       "skala ~1:15 · widok z wnętrza U, patrzysz na ZACHÓD → okno jest po PRAWEJ · sufit 248,1 [P] · góra zabudowy 246,9 (fuga 1,2 pod blendą) · blat 91 [P]")
s2 = (PH - 62 * mm) / 250.0
e = V(60 * mm, PH - 30 * mm, s2)
H, BL, COK, GD = 248.1, 91.0, 15.0, 148.0   # sufit 248,1 [P] pomiar po posadzce; góra zabudowy 246,9 (fuga 1,2)
e.rect(0, 0, 195, H)
e.rect(0, H - COK, 195, COK, fill=colors.HexColor("#2e2e2e"))
# UWAGA: rysunek jest LUSTRZANY względem osi y planu — patrząc na ścianę A stoisz
# tyłem do ściany C i patrzysz na zachód, więc ściana B (okno, y=0) wypada PO PRAWEJ.
# MX(a, b) przelicza odcinek [a,b] planu na odcinek rysunku.
def MX(a, b):
    return (195 - b, b - a)

for x0, w, lab in [MX(0, 61) + ("blenda\n(pilaster)",), MX(61, 85) + ("DA1\ndrzwi",),
                   MX(85, 145) + ("DA2 piekarnik\npod indukcją",),
                   MX(145, 195) + ("ślepy narożnik\npod ramieniem",)]:
    e.rect(x0, H - BL, w, BL - COK - 4, fill=FILL)
    for i, ln in enumerate(lab.split("\n")):
        e.text(x0 + w / 2, H - BL + 30 + i * 9, ln, 5.2, center=True)
e.rect(0, H - BL - 4, 195, 4, fill=BLAT)
e.line(50, H - BL - 4, 110, H - BL - 4, 2.2, INK)   # DA2 po lustrze: 195-145 .. 195-85
e.text(80, H - BL - 8, "INDUKCJA Bosch PXE601DC1E — wycięcie 56×49 [P]", 4.8, center=True)
for x0, w, lab, rozm in [MX(0, 67) + ("GA1\n245 gł.", 5.6), MX(67, 85) + ("GA2\n18\nbutelki", 4.0),
                         MX(85, 145) + ("GA3 OKAP\nw zabudowie", 5.6), MX(145, 195) + ("GA4", 5.6)]:
    e.rect(x0, 0, w, H - GD, fill=TALL)
    for i, ln in enumerate(lab.split("\n")):
        e.text(x0 + w / 2, (H - GD) / 2 + i * 9, ln, rozm, center=True, col=colors.white)
e.text(98, H - GD + 8, "LED 3000K pod górnymi", 5, center=True, col=GREY)
e.dimh(0, 195, H, "195 [P] — mierzone od ściany B, czyli od PRAWEJ krawędzi rysunku (pilaster w środku wymiaru)", off=14, size=5.4)
e.dimv(0, H, 0, "248,1 [P]", off=-14)
e.dimv(H - BL, H, 195, "91 [P]", off=12)
e.dimv(H - GD, H - BL - 4, 195, "≥55 okap–indukcja", off=12, size=5)
e.dimv(0, H - GD, 195, "górne 98,9 do 246,9", off=22, size=5)
e.text(0, H + 34, "GA2 (18 szer.) to najwęższa szafka ciągu — zawias od strony okapu; jej bok siada dokładnie na końcu pilastra [pomiar!]", 5.4, col=GREY)
e.text(0, H + 26, "PO LEWEJ blat skręca w ramię L (~118×50, wys. 91) w stronę korytarza; PO PRAWEJ pilaster i narożnik z oknem", 5.4, col=GREY)
c.showPage()

# ================= STRONA 3: ELEWACJA B =================
header("ELEWACJA B — ściana okna (BEZ szafek górnych)",
       "skala ~1:15 · okno pod sam sufit, parapet ~166,4 · OKNO OD STRONY PILASTRA: 59,7 | 85,6 | 94,7 [P] (v3.5) · od prawej: narożnik z C")
e = V(55 * mm, PH - 30 * mm, s2)
W = 238.9
e.rect(0, 0, W, H)
e.rect(0, H - COK, W, COK, fill=colors.HexColor("#2e2e2e"))
for x0, w, lab in [(0, 44.5, "martwe pole\n(za ciągiem A)"), (44.5, 15, "crg\n15"), (59.5, 80, "DB1 ZLEW 80"), (139.5, 45, "DB2\nZMYWARKA 45"), (184.5, 54.4, "narożnik z C\n(front DC1 od C)")]:
    e.rect(x0, H - BL, w, BL - COK - 4, fill=FILL)
    for i, ln in enumerate(lab.split("\n")):
        e.text(x0 + w / 2, H - BL + 30 + i * 9, ln, 5.0, center=True)
e.rect(0, H - BL - 4, W, 4, fill=BLAT)
wx1 = 59.7; wx2 = wx1 + 85.6   # okno od strony pilastra (lewej) [P]
e.rect(wx1, 0, 85.6, H - 166.4, fill=colors.HexColor("#dcebf5"))
e.line(wx1, (H - 166.4) / 2, wx2, (H - 166.4) / 2, 0.5, GREY)
e.line(wx1 + 42.8, 0, wx1 + 42.8, H - 166.4, 0.5, GREY)
e.text(wx1 + 42.8, H - 166.4 + 8, "parapet ~166,4 (głęboki, użytkowy)", 5, center=True, col=GREY)
e.dimh(0, wx1, 0, "59,7", off=-8)
e.dimh(wx1, wx2, 0, "85,6", off=-8)
e.dimh(wx2, W, 0, "94,7", off=-8)
e.dimv(0, H - 166.4, wx1, "81,7", off=-10)
e.dimh(0, W, H, "238,9 [P]", off=14)
e.dimv(0, H, 0, "248,1 [P]", off=-14)
e.text(30, H + 26, "zlew pod oknem ✓ · podejścia wody nisko na tej ścianie [~] — przedłużyć w zabudowie · zero górnych (okno do sufitu)", 5.4, col=GREY)
c.showPage()

# ================= STRONA 4: ELEWACJA C + RAMIĘ =================
header("ELEWACJA C — niski ciąg, słupek, lodówka przy ściance · RAMIĘ L od wnętrza U",
       "skala ~1:15 · patrzysz na WSCHÓD → narożnik z oknem po LEWEJ, ścianka po PRAWEJ · lodówka wolnostojąca 60×65×200 [P]")
e = V(28 * mm, PH - 30 * mm, s2)
ZW = 188.5 + 9.0
e.rect(0, 0, ZW, H)
e.rect(0, H - COK, 94.7, COK, fill=colors.HexColor("#2e2e2e"))
e.rect(0, H - BL, 94.7, BL - COK - 4, fill=FILL)
e.rect(0, H - BL - 4, 94.7, 4, fill=BLAT)
e.text(47, H - 40, "DC1 narożna (front 34,5) + blenda", 5.2, center=True)
e.text(47, H - 30, "blat w L z ciągu okna", 4.8, center=True, col=GREY)
e.rect(0, 0, 47, H - 148, fill=TALL)
e.rect(47, 0, 47.7, H - 148, fill=TALL)
e.text(23.5, (H - 148) / 2, "GC1", 5.6, center=True, col=colors.white)
e.text(23.5, (H - 148) / 2 + 10, "ociekarka/naczynia", 4.4, center=True, col=colors.white)
e.text(71, (H - 148) / 2, "GC2", 5.6, center=True, col=colors.white)
e.text(71, (H - 148) / 2 + 10, "kubki/szkło", 4.4, center=True, col=colors.white)
e.text(47, H - 140, "górne 98,9 (dół 148, góra 246,9) — decyzja inwestora v3.5", 4.4, center=True, col=GREY)
e.rect(94.7, 0, 28, H, fill=TALL)
e.text(108.7, H / 2 - 10, "C2", 5.4, center=True, col=colors.white)
e.text(108.7, H / 2, "~28", 4.8, center=True, col=colors.white)
e.text(108.7, H / 2 + 8, "CARGO", 4.4, center=True, col=colors.white)
e.text(108.7, H / 2 + 15, "(nie drzwi)", 3.8, center=True, col=colors.white)
e.rect(122.7, H - 200, 60, 200, fill=colors.HexColor("#f7f7f7"))   # 60 szer. — DOSUNIĘTA DO SŁUPKA
e.text(185.6, H - 130, "luz 5,8", 3.8, center=True, angle=90, col=GREY)
e.text(152.7, H - 105, "C3 LODÓWKA", 6.2, center=True, bold=True)
e.text(152.7, H - 95, "wolnostojąca 60×65, wys. 200 [P]", 5.0, center=True, col=GREY)
e.line(127, H - 62, 178, H - 62, 0.6, GREY)
e.rect(122.7, 0, 65.8, H - 205, fill=TALL)   # C4: od 205 (lodówka 200 + luz 5 cm) do 246,9
e.text(155.6, (H - 205) / 2, "C4 NADSTAWKA 41,9", 5.2, center=True, col=colors.white)
e.text(155.6, (H - 205) / 2 + 8, "+ kratka went.; podparcie [?]", 4.2, center=True, col=colors.white)
e.rect(188.5, 0, 9, H, fill=WALL)
e.text(201, H - 30, "ścianka [P] — za nią korytarz", 5.0, angle=90, col=GREY)
e.dimv(0, H, 0, "248,1 [P]", off=-14)
e.dimv(H - 200, H, ZW, "200 [P]", off=10)
e.dimv(0, H - 205, ZW, "41,9", off=10)
e.dimh(0, 94.7, H, "94,7 [P]", off=14, size=5.4)
e.dimh(94.7, 188.5, H, "~94 (28+66)", off=14, size=5.2)
e.dimh(0, 188.5, H, "188,5 [P]", off=24, size=5.4)
e.text(0, H + 34, "ZAWIASY LODÓWKI PRZEŁOŻONE NA STRONĘ SŁUPKA (wariant A [P]) — przy ściance skrzydło nie otwiera się wcale; zapas do kantu ścianki 70,8 mm", 5.2, col=GREY)
# ramię L obok
w2 = V(178 * mm, PH - 30 * mm, s2)
IW = 118.0
w2.rect(0, H - BL, IW, BL - COK, fill=FILL)
w2.rect(0, H - BL - 4, IW + 3, 4, fill=BLAT)
w2.rect(0, H - COK, IW, COK, fill=colors.HexColor("#2e2e2e"))
w2.text(IW / 2, H - BL + 34, "RAMIĘ L — widok z wnętrza U", 5.6, center=True, bold=True)
w2.text(IW / 2, H - BL + 46, "RL1: drzwi/szuflady od tej strony", 5.0, center=True, col=GREY)
w2.text(IW / 2, H - BL + 56, "rewers (od salonu): panel ryflowany", 5.0, center=True, col=GREY)
w2.dimh(0, IW, H, "~118 [~] (reguła: przejście 60 do ścianki)", off=14, size=5.0)
w2.dimv(H - BL - 4, H, IW, "91 [P]", off=10)
w2.text(0, H + 34, "blat ciągły z DA4; kotwienie w narożniku L", 5.2, col=GREY)
c.showPage()

c.save()
print("OK:", OUT)
