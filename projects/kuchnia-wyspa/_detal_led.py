#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DETAL: oświetlenie LED w cokole — przekrój + rozwinięcie obwodów.

Odpowiedź na pytanie inwestora: „pod dolnymi szafkami chcę miejsce na LED dookoła".

Str. 1 — przekrój przez cokół (skala 1:2): gdzie siedzi profil, ile cofnąć cokół,
         czego nie widać z pozycji stojącej.
Str. 2 — rzut z odcinkami, długościami, podziałem na dwa obwody i miejscem zasilacza.

    python3 _detal_led.py kuchnia-wyspa-detal-LED.pdf
"""
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = sys.argv[1] if len(sys.argv) > 1 else "kuchnia-wyspa-detal-LED.pdf"
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVS-B", FD + "DejaVuSans-Bold.ttf"))
PW, PH = landscape(A4)

INK = colors.HexColor("#1a1a1a")
GREY = colors.HexColor("#8a8a8a")
WOOD = colors.HexColor("#8a6a4a")
RED = colors.HexColor("#a02c2c")
DIMC = colors.HexColor("#a02c2c")
FILL = colors.HexColor("#efe9df")
COKOL = colors.HexColor("#2e2e2e")
SWIATLO = colors.HexColor("#f5e2a8")
PROFIL = colors.HexColor("#b9bec3")
POD = colors.HexColor("#d9c3a2")

c = canvas.Canvas(OUT, pagesize=landscape(A4))
c.setTitle("Kuchnia U + ramię L — detal oświetlenia LED w cokole")

# ---------------------------------------------------------------- geometria [mm]
COKOL_H = 150           # wysokość cokołu = nóżki
COKOL_R = 80            # COFNIĘCIE cokołu od lica frontów — decyzja tego detalu
DNO_GR = 18             # grubość dna korpusu
PROF_W, PROF_H = 16, 7  # profil aluminiowy nakładany z kloszem
FRONT_GR = 19

# odcinki cokołu (mm) — z modelu sprawdzonego kontrolą
ODCINKI = [
    ("ciąg A — lico indukcji",       1450, 1),
    ("ramię L — front (od kuchni)",   600, 1),
    ("ramię L — czoło wschodnie",     500, 1),
    ("ramię L — rewers (od salonu)", 1176, 1),
    ("ciąg B — lico okna",           1400, 2),
    ("ciąg C — lico niskiego ciągu",  345, 2),
]
OBW = {1: "OBWÓD 1 — ciąg A + ramię", 2: "OBWÓD 2 — ciąg B + ciąg C"}
W_NA_M = 9.6            # taśma 9,6 W/m (wariant podstawowy)


def naglowek(tytul, sub):
    c.setFillColor(WOOD); c.setFont("DVS-B", 13)
    c.drawString(15 * mm, PH - 14 * mm, tytul)
    c.setFillColor(GREY); c.setFont("DVS", 7.5)
    c.drawString(15 * mm, PH - 19 * mm, sub)
    c.setFont("DVS", 6.5)
    c.drawString(15 * mm, 8 * mm, "Kuchnia U + ramię L — detal LED w cokole · 2026-08-13 · "
                 "wymiary w mm · cofnięcie cokołu 80 to DECYZJA tego detalu, nie standard")
    c.drawRightString(PW - 15 * mm, 8 * mm, f"str. {c.getPageNumber()}")
    c.setStrokeColor(WOOD); c.setLineWidth(1)
    c.line(15 * mm, PH - 21 * mm, PW - 15 * mm, PH - 21 * mm)


# ================================ STRONA 1 — PRZEKRÓJ ================================
naglowek("DETAL LED W COKOLE — przekrój pionowy przez dolną szafkę",
         "skala ok. 1:4,5 · patrzysz z boku · lico frontu po LEWEJ · profil świeci w dół i lekko do przodu")

S = 0.22                      # ok. 1:4,5 — cały detal mieści się w lewej połowie strony
OX, OY = 56 * mm, 96 * mm     # lico frontu na poziomie podłogi
ZCIECIE = 300                 # rysunek ucięty na tej wysokości


def P(x, z):
    """x: w głąb szafki (0 = lico frontu, dodatnie = do tyłu); z: wysokość nad podłogą."""
    return OX + x * S * mm, OY + z * S * mm


def prost(x0, z0, x1, z1, fill, stroke=INK, lw=0.7):
    a, b = P(x0, z0); d, e = P(x1, z1)
    c.setLineWidth(lw); c.setStrokeColor(stroke); c.setFillColor(fill)
    c.rect(a, b, d - a, e - b, stroke=1, fill=1)


def txt(x, z, s, size=6.6, bold=False, col=INK, dx=0, dz=0):
    a, b = P(x, z)
    c.setFillColor(col); c.setFont("DVS-B" if bold else "DVS", size)
    c.drawString(a + dx * mm, b + dz * mm, s)


def wym_pion(x, z0, z1, lab):
    a, b = P(x, z0); _, e = P(x, z1)
    c.setStrokeColor(DIMC); c.setLineWidth(0.5); c.line(a, b, a, e)
    for yy in (b, e):
        c.line(a - 1.4 * mm, yy, a + 1.4 * mm, yy)
    c.saveState(); c.setFillColor(DIMC); c.setFont("DVS", 6.2)
    c.translate(a - 1.1 * mm, (b + e) / 2); c.rotate(90)
    c.drawCentredString(0, 0, lab); c.restoreState()


def wym_poz(z, x0, x1, lab):
    a, b = P(x0, z); d, _ = P(x1, z)
    c.setStrokeColor(DIMC); c.setLineWidth(0.5); c.line(a, b, d, b)
    for xx in (a, d):
        c.line(xx, b - 1.4 * mm, xx, b + 1.4 * mm)
    c.setFillColor(DIMC); c.setFont("DVS", 6.2)
    c.drawCentredString((a + d) / 2, b + 1.1 * mm, lab)


# podłoga
a, b = P(-150, 0); d, _ = P(420, 0)
c.setFillColor(POD); c.rect(a, b - 4 * mm, d - a, 4 * mm, stroke=0, fill=1)
c.setStrokeColor(INK); c.setLineWidth(1.2); c.line(a, b, d, b)
txt(-148, 0, "PODŁOGA (jasny dąb, już ułożona)", 6.0, col=GREY, dz=-3)

# stożek światła spod profilu
c.setFillColor(SWIATLO)
pth = c.beginPath()
pth.moveTo(*P(FRONT_GR + 2, COKOL_H - PROF_H))
pth.lineTo(*P(FRONT_GR + 2 + PROF_W, COKOL_H - PROF_H))
pth.lineTo(*P(180, 0))
pth.lineTo(*P(-150, 0))
pth.close()
c.setStrokeColor(SWIATLO); c.drawPath(pth, stroke=0, fill=1)

# korpus dolny — ucięty na 300
prost(FRONT_GR, COKOL_H, 400, COKOL_H + DNO_GR, FILL)                        # dno korpusu 18
prost(FRONT_GR, COKOL_H + DNO_GR, 400, ZCIECIE, colors.HexColor("#faf8f4"))  # wnętrze
prost(0, COKOL_H - 45, FRONT_GR, ZCIECIE, colors.HexColor("#e6dccb"))        # FRONT 19
c.setStrokeColor(GREY); c.setLineWidth(0.6); c.setDash(2, 2)
c.line(*P(0, ZCIECIE), *P(400, ZCIECIE))
c.setDash()
txt(60, ZCIECIE + 8, "↑ korpus dolny 720 — rysunek ucięty", 6.0, col=GREY)
txt(-148, 250, "FRONT", 7.4, bold=True)
txt(-148, 232, "(bezuchwytowy —", 6.0, col=GREY)
txt(-148, 218, "schodzi 45 poniżej dna)", 6.0, col=GREY)
c.setStrokeColor(GREY); c.setLineWidth(0.5)
c.line(*P(-40, 240), *P(2, 220))

# cokół — COFNIĘTY
prost(COKOL_R, 0, COKOL_R + 18, COKOL_H, COKOL)
txt(COKOL_R + 26, 96, "COKÓŁ 150 (czarny mat)", 6.6, bold=True)
txt(COKOL_R + 26, 78, "cofnięty 80 od lica frontu", 6.0, col=GREY)
txt(COKOL_R + 26, 62, "na klipsach — ZDEJMOWALNY", 6.0, col=GREY)

# nóżka
prost(250, 0, 290, COKOL_H, colors.HexColor("#9aa0a6"))
txt(300, 30, "nóżka 150", 6.0, col=GREY)

# PROFIL LED
prost(FRONT_GR + 2, COKOL_H - PROF_H, FRONT_GR + 2 + PROF_W, COKOL_H, PROFIL, RED, 1.3)
txt(-150, 176, "PROFIL ALU 16×7 + klosz mleczny", 6.8, bold=True, col=RED)
txt(-150, 160, "przykręcony do SPODU dna korpusu", 6.0, col=RED)
c.setStrokeColor(RED); c.setLineWidth(0.7)
c.line(*P(-34, 166), *P(FRONT_GR + 8, COKOL_H - 2))

# wymiary
wym_pion(-70, 0, COKOL_H, "150 cokół")
wym_poz(-30, 0, COKOL_R, "80 — cofnięcie cokołu")
wym_pion(440, COKOL_H, COKOL_H + DNO_GR, "18 dno")

txt(300, 96, "strefa cienia", 6.2, col=GREY)

# ---- kolumna tekstu po prawej ----
TX = 152 * mm
c.setFillColor(WOOD); c.setFont("DVS-B", 9.5)
c.drawString(TX, PH - 32 * mm, "DLACZEGO POD DNEM, A NIE NA COKOLE")
yy = PH - 39 * mm
for t in ["Taśma na SPODZIE dna świeci w dół. Z pozycji stojącej nie zobaczysz",
          "jej nigdy — musiałbyś mieć oczy niżej niż 150 mm nad podłogą.",
          "",
          "Taśma naklejona na LICU cokołu byłaby widoczna jako jasna kreska",
          "i świeciłaby prosto w oczy każdemu, kto siedzi.",
          "",
          "Cofnięcie 80 (zamiast typowych 50) daje miejsce na profil 16 mm",
          "plus palce przy montażu, i pogłębia cień — zabudowa mocniej",
          "„unosi się\" nad podłogą.",
          "",
          "Klosz mleczny obowiązkowo. Bez niego na podłodze widać ciąg",
          "oddzielnych kropek zamiast równej smugi."]:
    c.setFillColor(INK); c.setFont("DVS", 7.2)
    c.drawString(TX, yy, t); yy -= 4.6 * mm

yy -= 3 * mm
c.setFillColor(RED); c.setFont("DVS-B", 9)
c.drawString(TX, yy, "UCZCIWE OSTRZEŻENIE"); yy -= 6 * mm
for t in ["Światło muskające podłogę pokazuje KAŻDY okruch i każdą",
          "nierówność posadzki. To efekt na wieczór, nie oświetlenie robocze —",
          "do pracy służy LED pod górnymi szafkami (już w projekcie)."]:
    c.setFillColor(INK); c.setFont("DVS", 7.2)
    c.drawString(TX, yy, t); yy -= 4.6 * mm

c.showPage()

# ================================ STRONA 2 — ROZWINIĘCIE ================================
naglowek("LED W COKOLE — przebieg, długości, obwody",
         "rzut z góry · grube linie = odcinki taśmy · dwa obwody, każdy poniżej 5 m, żeby nie było spadku napięcia")

S2 = 0.043
BX, BY = 20 * mm, PH - 32 * mm


def R(x, y):
    return BX + x * S2 * mm, BY - y * S2 * mm


def rlinia(x0, y0, x1, y1, col, lw=2.6):
    c.setStrokeColor(col); c.setLineWidth(lw); c.setLineCap(1)
    c.line(*R(x0, y0), *R(x1, y1))


def rtxt(x, y, s, size=6.4, bold=False, col=INK, center=False):
    a, b = R(x, y)
    c.setFillColor(col); c.setFont("DVS-B" if bold else "DVS", size)
    (c.drawCentredString if center else c.drawString)(a, b, s)


# obrys pomieszczenia
c.setStrokeColor(GREY); c.setLineWidth(0.8)
c.rect(*R(0, 0), 2546 * S2 * mm, -1950 * S2 * mm, stroke=1, fill=0)
c.setFillColor(colors.HexColor("#f3f0ea"))
for (x0, y0, x1, y1) in [(0, 0, 600, 1450), (600, 0, 2000, 600), (2000, 0, 2546, 945),
                         (600, 1450, 1176, 1950), (0, 1450, 600, 1950)]:
    a, b = R(x0, y0); d, e = R(x1, y1)
    c.setStrokeColor(colors.HexColor("#d5cec2")); c.setLineWidth(0.5)
    c.rect(a, b, d - a, e - b, stroke=1, fill=1)
rtxt(300, 700, "ciąg A", 6.2, col=GREY, center=True)
rtxt(1300, 300, "ciąg B (okno)", 6.2, col=GREY, center=True)
rtxt(2270, 470, "ciąg C", 6.2, col=GREY, center=True)
rtxt(890, 1700, "ramię L", 6.2, col=GREY, center=True)
rtxt(2250, 1480, "lodówka: BEZ cokołu —", 5.4, col=RED, center=True)
rtxt(2250, 1620, "tu linia się kończy", 5.4, col=RED, center=True)

C1, C2C = colors.HexColor("#c8891f"), colors.HexColor("#3f7d8c")
# obwód 1
rlinia(600, 0, 600, 1450, C1)                 # ciąg A
rlinia(600, 1450, 1176, 1450, C1)             # ramię front
rlinia(1176, 1450, 1176, 1950, C1)            # czoło ramienia
rlinia(0, 1950, 1176, 1950, C1)               # rewers ramienia
# obwód 2
rlinia(600, 600, 2000, 600, C2C)              # ciąg B
rlinia(2000, 600, 2000, 945, C2C)             # ciąg C

# zasilacz
zx, zy = 300, 1700
a, b = R(zx, zy)
c.setFillColor(RED); c.circle(a, b, 2.2 * mm, stroke=0, fill=1)
c.setFillColor(colors.white); c.setFont("DVS-B", 6); c.drawCentredString(a, b - 1.5 * mm, "Z")
rtxt(0, 2080, "Z = ZASILACZ 24 V — w ślepym polu pod ramieniem, dostęp przez drzwi RL1", 6.0, bold=True, col=RED)
rtxt(0, 2200, "tam też schodzą się oba obwody; to jedyne suche i dostępne miejsce w kuchni", 5.6, col=RED)
rtxt(180, 1540, "ślepe pole", 5.4, col=GREY, center=True)
c.setStrokeColor(RED); c.setLineWidth(0.5); c.setDash(2, 2)
c.line(*R(zx, zy), *R(600, 1450))
c.line(*R(zx, zy), *R(600, 600))
c.setDash()

# tabela odcinków
TX, TY = 145 * mm, PH - 32 * mm
c.setFillColor(WOOD); c.setFont("DVS-B", 9)
c.drawString(TX, TY, "ODCINKI TAŚMY")
y = TY - 7 * mm
c.setFont("DVS-B", 6.8); c.setFillColor(GREY)
c.drawString(TX, y, "odcinek"); c.drawRightString(TX + 62 * mm, y, "mm"); c.drawString(TX + 68 * mm, y, "obwód")
y -= 4 * mm
sumy = {1: 0, 2: 0}
for nazwa, dl, ob in ODCINKI:
    sumy[ob] += dl
    c.setFillColor(INK); c.setFont("DVS", 7.0)
    c.drawString(TX, y, nazwa)
    c.drawRightString(TX + 62 * mm, y, f"{dl}")
    c.setFillColor(C1 if ob == 1 else C2C); c.setFont("DVS-B", 7.0)
    c.drawString(TX + 68 * mm, y, str(ob))
    y -= 4.6 * mm

y -= 1.5 * mm
c.setStrokeColor(GREY); c.setLineWidth(0.5); c.line(TX, y + 2 * mm, TX + 80 * mm, y + 2 * mm)
for ob in (1, 2):
    c.setFillColor(C1 if ob == 1 else C2C); c.setFont("DVS-B", 7.2)
    c.drawString(TX, y, OBW[ob])
    c.drawRightString(TX + 62 * mm, y, f"{sumy[ob]} = {sumy[ob]/1000:.2f} m")
    y -= 4.6 * mm
CALK = sum(sumy.values())
c.setFillColor(INK); c.setFont("DVS-B", 8)
c.drawString(TX, y, "RAZEM")
c.drawRightString(TX + 62 * mm, y, f"{CALK} mm = {CALK/1000:.2f} m")
y -= 8 * mm

MOC = CALK / 1000 * W_NA_M
c.setFillColor(WOOD); c.setFont("DVS-B", 9); c.drawString(TX, y, "RACHUNEK MOCY")
y -= 6 * mm
for t in [f"taśma 9,6 W/m × {CALK/1000:.2f} m = {MOC:.0f} W",
          f"zasilacz z zapasem 30% → {MOC*1.3:.0f} W → kupujesz 24 V / 100 W",
          "24 V, nie 12 V — przy 12 V na 3,7 m koniec odcinka byłby wyraźnie ciemniejszy",
          f"oba obwody poniżej 5 m ({sumy[1]/1000:.2f} m i {sumy[2]/1000:.2f} m) → zasilanie z jednego końca wystarczy"]:
    c.setFillColor(INK); c.setFont("DVS", 7.0)
    c.drawString(TX, y, "• " + t)
    y -= 4.6 * mm

y -= 4 * mm
c.setFillColor(WOOD); c.setFont("DVS-B", 9); c.drawString(TX, y, "CO KUPIĆ")
y -= 6 * mm
for t in ["profil alu nakładany 16×7 z kloszem mlecznym — 6 mb (5,47 + zapas na docinki)",
          "taśma 24 V 3000 K IP65, 9,6 W/m — 6 mb (ta sama barwa co pod górnymi)",
          "zasilacz 24 V 100 W + przewód 2×0,75 do obu obwodów",
          "złączki bezlutowe do taśmy IP65 — 8 szt (6 narożników + 2 zapas)",
          "ściemniacz/odbiornik 24 V z pilotem — opcja, jeśli chcesz regulować jasność"]:
    c.setFillColor(INK); c.setFont("DVS", 7.0)
    c.drawString(TX, y, "• " + t)
    y -= 4.6 * mm

y -= 4 * mm
c.setFillColor(RED); c.setFont("DVS-B", 9); c.drawString(TX, y, "TRZY RZECZY, KTÓRE TRZEBA ZROBIĆ TERAZ, NIE POTEM")
y -= 6 * mm
for t in ["GNIAZDO 230 V w ślepym polu pod ramieniem — na zasilacz. Dopisane do listy instalacyjnej.",
          "IP65 obowiązkowo: taśma leży 150 mm nad podłogą, którą będziesz myć na mokro.",
          "Cokół musi być ZDEJMOWALNY (klipsy), bo zasilacz i złączki muszą być dostępne."]:
    c.setFillColor(INK); c.setFont("DVS", 7.0)
    c.drawString(TX, y, "• " + t)
    y -= 4.6 * mm

c.showPage()
c.save()
print("OK:", OUT, f"| razem {CALK} mm, obwody: {sumy[1]} + {sumy[2]}")
