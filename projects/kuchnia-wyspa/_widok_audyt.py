#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MAPA USTEREK — widok przestrzenny z naniesionymi wynikami audytu (P0).

Nie jest to „projekt poprawiony" — poprawić w całości się nie da, dopóki nie ma
pomiarów (koszyk A) i decyzji inwestora (koszyk B). To rysunek diagnostyczny:
pokazuje, GDZIE w przestrzeni siedzą usterki P0 i które korekty są już wymuszone
samą arytmetyką.

Geometria importowana z _model3d.py — jedno źródło (werdykt audytu, krok 1).

    python3 _widok_audyt.py kuchnia-wyspa-mapa-usterek.pdf
"""
import math
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

import _model3d as M

OUT = sys.argv[1] if len(sys.argv) > 1 else "kuchnia-wyspa-mapa-usterek.pdf"
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVS-B", FD + "DejaVuSans-Bold.ttf"))
PW, PH = A4

INK = colors.HexColor("#1a1a1a")
GREY = colors.HexColor("#8a8a8a")
WOOD = colors.HexColor("#8a6a4a")
RED = colors.HexColor("#a02c2c")
RED_L = colors.HexColor("#e8c9c9")
ZIEL = colors.HexColor("#4f7a52")
BG = colors.HexColor("#f5f1ea")

S = 0.0335
OX, OY = 74 * mm, 176 * mm
COS30 = math.cos(math.radians(30))

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Kuchnia — mapa usterek z audytu")


def P(x, y, z):
    return (OX + (x - y) * COS30 * S * mm, OY + (z - (x + y) * 0.5) * S * mm)


def wielokat(pts, kolor, obrys=None, gr=0.35):
    p = c.beginPath()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.setFillColor(kolor)
    c.setStrokeColor(obrys or M.mix(kolor, -0.45))
    c.setLineWidth(gr)
    c.drawPath(p, stroke=1, fill=1)


def rysuj(x0, y0, z0, x1, y1, z1, kolor, alarm=False):
    ob = RED if alarm else None
    gr = 1.1 if alarm else 0.35
    wielokat([P(x0, y0, z1), P(x1, y0, z1), P(x1, y1, z1), P(x0, y1, z1)], M.mix(kolor, 0.20), ob, gr)
    wielokat([P(x1, y0, z0), P(x1, y1, z0), P(x1, y1, z1), P(x1, y0, z1)], M.mix(kolor, -0.10), ob, gr)
    wielokat([P(x0, y1, z0), P(x1, y1, z0), P(x1, y1, z1), P(x0, y1, z1)], M.mix(kolor, -0.24), ob, gr)


def znacznik(x, y, z, txt):
    px, py = P(x, y, z)
    c.setFillColor(RED)
    c.circle(px, py, 3.1 * mm, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("DVS-B", 6.2)
    c.drawCentredString(px, py - 2 * mm, txt)


# ================================ nagłówek ================================
c.setFillColor(WOOD)
c.setFont("DVS-B", 13)
c.drawString(15 * mm, PH - 17 * mm, "MAPA USTEREK — wyniki audytu naniesione na bryłę kuchni")
c.setFillColor(RED)
c.setFont("DVS-B", 7.6)
c.drawString(15 * mm, PH - 22.5 * mm,
             "To NIE jest projekt poprawiony. Czerwone bryły = usterki P0 blokujące zamówienie.")
c.setFillColor(GREY)
c.setFont("DVS", 7.2)
c.drawString(15 * mm, PH - 26.5 * mm,
             "Stan 2026-08-13 (v3.13): sufit zmierzony, lodówka zmierzona, zawiasy rozstrzygnięte — trzy usterki P0 zamknięte.")
c.drawString(15 * mm, PH - 30 * mm,
             "Zostaje 7 usterek P0, koszyk B (decyzje inwestora) oraz dwa pomiary: pilaster i ściana C łańcuchowo.")
c.setStrokeColor(WOOD)
c.setLineWidth(1.1)
c.line(15 * mm, PH - 33 * mm, PW - 15 * mm, PH - 33 * mm)

# ================================ scena ================================
wielokat([P(0, 0, 0), P(M.CX, 0, 0), P(M.CX, M.CY, 0), P(0, M.CY, 0)], M.PODLOGA)
wielokat([P(0, 0, 0), P(M.CX, 0, 0), P(M.CX, 0, M.H), P(0, 0, M.H)], M.SCIANA)
wielokat([P(752, 0, 1661), P(1608, 0, 1661), P(1608, 0, M.H), P(752, 0, M.H)], M.SZKLO)
wielokat([P(0, 0, 0), P(0, M.CY, 0), P(0, M.CY, M.H), P(0, 0, M.H)], M.mix(M.SCIANA, -0.07))

POMIN = {"C3", "C4", "scianka"}          # wieża zasłania wnętrze — pokazana osobno niżej
for uid, grupa, x0, y0, z0, x1, y1, z1, kol in sorted(
        M.bryly(), key=lambda b: (b[2] + b[3], b[4])):
    if uid in POMIN:
        continue
    alarm = uid in M.USTERKI
    if alarm:
        kol = M.mix(RED_L, 0.10) if kol not in (M.COKOL,) else kol
    rysuj(x0, y0, z0, x1, y1, z1, kol, alarm)

# płyta indukcyjna
wielokat([P(60, 864, M.BLAT_H + 2), P(620, 864, M.BLAT_H + 2),
          P(620, 1436, M.BLAT_H + 2), P(60, 1436, M.BLAT_H + 2)], colors.HexColor("#23262a"))
wielokat([P(820, 120, M.BLAT_H + 2), P(1480, 120, M.BLAT_H + 2),
          P(1480, 520, M.BLAT_H + 2), P(820, 520, M.BLAT_H + 2)], colors.HexColor("#2b2b2b"))

# znaczniki na bryłach
znacznik(280, 400, M.KORPUS_Z, "01")      # DA1
znacznik(280, 1150, M.KORPUS_Z, "06")     # DA2
znacznik(600, 1700, M.KORPUS_Z, "02")     # RL1
znacznik(2270, 470, M.KORPUS_Z, "08")     # DC1
znacznik(200, 1150, M.GORA, "12")         # GA3

# ================================ legenda usterek ================================
LY = 103 * mm
c.setFillColor(BG)
c.rect(15 * mm, 20 * mm, PW - 30 * mm, LY - 20 * mm + 4 * mm, stroke=0, fill=1)
c.setFillColor(RED)
c.setFont("DVS-B", 9)
c.drawString(19 * mm, LY - 2 * mm, "USTERKI P0 — blokują zamówienie")
c.setFont("DVS", 7)
y = LY - 8 * mm
for kod, gdzie, opis in M.OPISY_USTEREK:
    c.setFillColor(RED)
    c.setFont("DVS-B", 6.9)
    c.drawString(19 * mm, y, kod)
    c.setFillColor(INK)
    c.setFont("DVS-B", 6.9)
    c.drawString(31 * mm, y, gdzie)
    c.setFillColor(GREY)
    c.setFont("DVS", 6.9)
    c.drawString(66 * mm, y, opis)
    y -= 4.3 * mm

y -= 1 * mm
c.setFillColor(ZIEL)
c.setFont("DVS-B", 8.5)
c.drawString(19 * mm, y, "JUŻ POPRAWIONE NA TYM RYSUNKU (korekty wymuszone arytmetyką, bez decyzji i bez pomiaru)")
y -= 5.5 * mm
for kod, gdzie, opis in M.KOREKTY_WYMUSZONE:
    c.setFillColor(ZIEL)
    c.setFont("DVS-B", 6.9)
    c.drawString(19 * mm, y, kod)
    c.setFillColor(INK)
    c.setFont("DVS-B", 6.9)
    c.drawString(31 * mm, y, gdzie)
    c.setFillColor(GREY)
    c.setFont("DVS", 6.9)
    c.drawString(66 * mm, y, opis)
    y -= 4.3 * mm

y -= 1 * mm
c.setFillColor(WOOD)
c.setFont("DVS-B", 8.5)
c.drawString(19 * mm, y, "CZEGO NIE MA NA RYSUNKU I DLACZEGO")
c.setFillColor(INK)
c.setFont("DVS", 6.9)
for t in ["• lodówka i nadstawka C4 — pominięte na rysunku, bo zasłaniają wnętrze; usterka P0-13 opisana wyżej",
          "• skorygowane głębokości blatu, fronty gola/frez, zawartość DA2 — to koszyk B, czekają na Twoją decyzję",
          "• pilaster i ściana C — jedyne dwa pomiary, których jeszcze brakuje (reszta wysokości już policzona z 2481)"]:
    y -= 4.2 * mm
    c.drawString(19 * mm, y, t)

c.setFillColor(GREY)
c.setFont("DVS", 6.3)
c.drawString(15 * mm, 12 * mm,
             "Geometria z _model3d.py — jedno źródło wspólne z widokiem przestrzennym (werdykt audytu, krok 1). "
             "Kuchnia U + ramię L · 2026-08-13")
c.showPage()
c.save()
print("OK:", OUT)
