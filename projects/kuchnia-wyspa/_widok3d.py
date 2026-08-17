#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Widok aksonometryczny kuchni — „wizualizacja" rysunkowa w kolorach z palety.

Dwa ujęcia (kuchnia w U — z jednego rogu zawsze coś zasłania):
  str. 1 — od korytarza, od strony lodówki: ciąg z indukcją, okap, zlew
  str. 2 — od korytarza, od strony indukcji: ściana z lodówką, słupek, ramię

Rysowane z tych samych wymiarów co _kontrola.py.

    python3 _widok3d.py kuchnia-wyspa-widok-3D.pdf
"""
import math
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = sys.argv[1] if len(sys.argv) > 1 else "kuchnia-wyspa-widok-3D.pdf"
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVS-B", FD + "DejaVuSans-Bold.ttf"))
PW, PH = A4

import _model3d as M                      # JEDNO ŹRÓDŁO GEOMETRII — patrz _model3d.py

BEZ, ORZECH, ANTRACYT = M.BEZ, M.ORZECH, M.ANTRACYT
BLAT, COKOL, PODLOGA = M.BLAT, M.COKOL, M.PODLOGA
SCIANA, RYFLE, SZKLO, INOX = M.SCIANA, M.RYFLE, M.SZKLO, M.INOX
INK      = colors.HexColor("#1a1a1a")
GREY     = colors.HexColor("#8a8a8a")
WOOD     = colors.HexColor("#8a6a4a")
CIEMNY   = colors.HexColor("#2f3336")
BRAZ     = colors.HexColor("#5a4028")

CX, CY, H = M.CX, M.CY, M.H
GORA = M.GORA                              # 2469 — góra zabudowy (sufit 2481 − fuga 12)
BLAT_H, COKOL_H, KORPUS_Z, GORNE_Z0 = M.BLAT_H, M.COKOL_H, M.KORPUS_Z, M.GORNE_Z0
PARAPET = H - 817                          # okno pod sufit, wys. 817 [P]

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Kuchnia U + ramię L — widok aksonometryczny")

S = 0.042
OX, OY = 86 * mm, 152 * mm
COS30 = math.cos(math.radians(30))
MIRROR = False


def T(x):
    return (CX - x) if MIRROR else x


def PR(tx, y, z):
    return (OX + (tx - y) * COS30 * S * mm, OY + (z - (tx + y) * 0.5) * S * mm)


def P(x, y, z):
    return PR(T(x), y, z)


def mix(col, f):
    r, g, b = col.red, col.green, col.blue
    if f >= 0:
        return colors.Color(r + (1 - r) * f, g + (1 - g) * f, b + (1 - b) * f)
    return colors.Color(r * (1 + f), g * (1 + f), b * (1 + f))


def wielokat(pts, kolor, obrys=True):
    p = c.beginPath()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.setFillColor(kolor)
    if obrys:
        c.setStrokeColor(mix(kolor, -0.45))
        c.setLineWidth(0.35)
    c.drawPath(p, stroke=1 if obrys else 0, fill=1)


def rysuj_bryle(x0, y0, z0, x1, y1, z1, kolor):
    a0, a1 = sorted((T(x0), T(x1)))
    wielokat([PR(a0, y0, z1), PR(a1, y0, z1), PR(a1, y1, z1), PR(a0, y1, z1)], mix(kolor, 0.20))
    wielokat([PR(a1, y0, z0), PR(a1, y1, z0), PR(a1, y1, z1), PR(a1, y0, z1)], mix(kolor, -0.10))
    wielokat([PR(a0, y1, z0), PR(a1, y1, z0), PR(a1, y1, z1), PR(a0, y1, z1)], mix(kolor, -0.24))


def etykieta(x, y, z, txt, dx=0, dy=0, kolor=INK, bold=True, rozm=6.6):
    px, py = P(x, y, z)
    c.setFillColor(kolor)
    c.setFont("DVS-B" if bold else "DVS", rozm)
    c.drawString(px + dx * mm, py + dy * mm, txt)


def zabudowa():
    """Bryły z _model3d.bryly() — bez uid, w formacie (grupa, x0, y0, z0, x1, y1, z1, kolor)."""
    return [b[1:] for b in M.bryly()]


def strona(mirror, tytul, podtytul, opisy, pomin=()):
    global MIRROR
    MIRROR = mirror

    c.setFillColor(WOOD)
    c.setFont("DVS-B", 12.5)
    c.drawString(15 * mm, PH - 18 * mm, tytul)
    c.setFillColor(GREY)
    c.setFont("DVS", 7.4)
    c.drawString(15 * mm, PH - 23.5 * mm, podtytul)
    c.setStrokeColor(WOOD)
    c.setLineWidth(1.1)
    c.line(15 * mm, PH - 26.5 * mm, PW - 15 * mm, PH - 26.5 * mm)

    wielokat([P(0, 0, 0), P(CX, 0, 0), P(CX, CY, 0), P(0, CY, 0)], PODLOGA, obrys=False)
    wielokat([P(0, 0, 0), P(CX, 0, 0), P(CX, 0, H), P(0, 0, H)], SCIANA)
    wielokat([P(752, 0, PARAPET), P(1608, 0, PARAPET), P(1608, 0, H), P(752, 0, H)], SZKLO)
    c.setStrokeColor(colors.HexColor("#9aa4ab"))
    c.setLineWidth(0.6)
    c.line(*P(1180, 0, PARAPET), *P(1180, 0, H))
    bok = CX if mirror else 0
    wielokat([P(bok, 0, 0), P(bok, CY, 0), P(bok, CY, H), P(bok, 0, H)], mix(SCIANA, -0.07))

    widoczne = [b for b in zabudowa() if b[0] not in pomin]
    for nm, x0, y0, z0, x1, y1, z1, kol in sorted(
            widoczne, key=lambda b: (min(T(b[1]), T(b[4])) + b[2], b[3])):
        rysuj_bryle(x0, y0, z0, x1, y1, z1, kol)

    if "A" not in pomin:
        wielokat([P(60, 864, BLAT_H + 2), P(620, 864, BLAT_H + 2),
                  P(620, 1436, BLAT_H + 2), P(60, 1436, BLAT_H + 2)], colors.HexColor("#23262a"))
    wielokat([P(820, 120, BLAT_H + 2), P(1480, 120, BLAT_H + 2),
              P(1480, 520, BLAT_H + 2), P(820, 520, BLAT_H + 2)], colors.HexColor("#2b2b2b"))
    c.setStrokeColor(mix(BEZ, -0.4))
    c.setLineWidth(0.5)
    for zz in (COKOL_H + 240, COKOL_H + 480):
        c.line(*P(576, 1950, zz), *P(1176, 1950, zz))
    c.line(*P(876, 1950, COKOL_H), *P(876, 1950, KORPUS_Z))

    for x, y, z, txt, kw in opisy:
        etykieta(x, y, z, txt, **kw)

    LY = 48 * mm
    c.setFillColor(WOOD)
    c.setFont("DVS-B", 8.5)
    c.drawString(15 * mm, LY + 6 * mm, "MATERIAŁY (paleta zaakceptowana — pkt 10 planu)")
    for i, (kol, opis) in enumerate([
            (BEZ, "fronty dolne — beż/kaszmir CIEPŁY mat, bezuchwytowe"),
            (ORZECH, "górne + słupek — ciemny orzech mat, do sufitu"),
            (ANTRACYT, "nadstawka nad lodówką + ścianka — antracyt ≈ RAL 7016"),
            (INOX, "lodówka WOLNOSTOJĄCA (Beko inox 60×65×200) — nie jest meblem"),
            (BLAT, "blat — jasny trawertyn, laminat 38"),
            (RYFLE, "rewers ramienia — panel ryflowany ciemny (od salonu)"),
            (PODLOGA, "podłoga — jasny dąb · ściany NCS S 2002-Y")]):
        yy = LY - i * 5.3 * mm
        c.setFillColor(kol)
        c.setStrokeColor(mix(kol, -0.4))
        c.setLineWidth(0.4)
        c.rect(15 * mm, yy - 1 * mm, 7 * mm, 4 * mm, stroke=1, fill=1)
        c.setFillColor(INK)
        c.setFont("DVS", 7.2)
        c.drawString(25 * mm, yy, opis)

    c.setFillColor(GREY)
    c.setFont("DVS", 6.3)
    c.drawString(15 * mm, 10 * mm,
                 "Rysunek aksonometryczny (nie perspektywa) · ścianka przy lodówce ścięta do 30 cm, "
                 "żeby nie zasłaniała wnętrza · wymiary z modelu sprawdzonego kontrolą · 2026-08-13")
    c.showPage()


strona(False,
       "WIDOK PRZESTRZENNY 1/2 — strefa gotowania i zmywania",
       "Patrzysz od korytarza, od strony lodówki. Widać fronty ciągu z indukcją i ciągu okna.",
       [(0, 200, GORA + 40, "GA1  670 · gł. 245 (na licu pilastra)", dict(dx=-8, dy=2, kolor=BRAZ)),
        (0, 760, GORA + 40, "GA2  180 — butelki", dict(dx=-16, dy=2, kolor=BRAZ)),
        (0, 1150, GORA + 40, "GA3  600 — OKAP", dict(dx=-19, dy=2, kolor=BRAZ)),
        (0, 1750, GORA + 40, "GA4  500", dict(dx=-4, dy=2, kolor=BRAZ)),
        (300, 1150, BLAT_H + 30, "INDUKCJA 60", dict(dx=-11, dy=0, kolor=colors.white, rozm=6.2)),
        (1150, 300, BLAT_H + 30, "ZLEW pod oknem", dict(dx=-14, dy=2, kolor=colors.white, rozm=6.2)),
        (1780, 600, BLAT_H + 30, "ZMYWARKA 45", dict(dx=-2, dy=-3)),
        (1176, 1950, KORPUS_Z, "RAMIĘ L — szuflady na sztućce", dict(dx=4, dy=-7)),
        (0, 850, 300, "DA1 — narożna ślepa (garnki, dostęp bokiem)", dict(dx=-2, dy=0, kolor=INK, rozm=6.2))],
       pomin=("wieza",))

strona(True,
       "WIDOK PRZESTRZENNY 2/2 — ściana z lodówką",
       "Ten sam pokój, obejście na drugą stronę. Widać fronty ściany z lodówką, słupek i ramię od korytarza.",
       [(2546, 1885, 1450, "LODÓWKA WOLNOSTOJĄCA", dict(dx=12, dy=2, kolor=colors.white, rozm=6.2)),
        (2546, 1885, 1450, "zawiasy od strony słupka", dict(dx=12, dy=-2.4, bold=False, kolor=colors.white, rozm=6.2)),
        (2546, 1225, GORA, "C4 — nadstawka 419", dict(dx=-2, dy=3, kolor=CIEMNY)),
        (2546, 945, GORA, "SŁUPEK / SPIŻARKA 2319", dict(dx=-2, dy=3, kolor=BRAZ)),
        (2546, 700, GORA, "GC1 / GC2 — górne do 2469", dict(dx=-2, dy=6, kolor=BRAZ)),
        (2000, 700, BLAT_H + 30, "DC1 — szuflady wewnętrzne", dict(dx=-6, dy=2)),
        (1150, 300, BLAT_H + 30, "ZLEW pod oknem", dict(dx=-8, dy=2, kolor=colors.white, rozm=6.2)),
        (0, 1950, KORPUS_Z, "RAMIĘ — rewers ryflowany od salonu", dict(dx=-8, dy=-6))],
       pomin=("GA",))

c.save()
print("OK:", OUT)
