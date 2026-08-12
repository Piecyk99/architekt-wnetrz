#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Montaż PROSTY — 1 strona, wariant 'wszystko wywiercone w CNC' (jak IKEA)."""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = sys.argv[1] if len(sys.argv) > 1 else "prosty.pdf"
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVS-B", FD + "DejaVuSans-Bold.ttf"))
PW, PH = A4
INK = colors.HexColor("#1a1a1a"); WOOD = colors.HexColor("#8a6a4a")
GREY = colors.HexColor("#8a8a8a"); RED = colors.HexColor("#a05252")
BG = colors.HexColor("#f5f1ea")
c = canvas.Canvas(OUT, pagesize=A4); c.setTitle("Montaż prosty — 1 strona")

c.setFillColor(WOOD); c.setFont("DVS-B", 15)
c.drawString(16*mm, PH-20*mm, "MONTAŻ NA NAJPROŚCIEJ — jedna strona")
c.setFillColor(GREY); c.setFont("DVS", 8)
c.drawString(16*mm, PH-26*mm, "Korner tnie i okleja, ale NIE WIERCI — otwory załatwiasz jedną z dwóch dróg poniżej, a potem skręcasz jak mebel z IKEA.")
c.setStrokeColor(WOOD); c.setLineWidth(1.2); c.line(16*mm, PH-29*mm, PW-16*mm, PH-29*mm)

c.setFillColor(RED); c.setFont("DVS-B", 9.5)
c.drawString(16*mm, PH-37*mm, "OTWORY — DWIE DROGI (wybierz jedną):")
c.setFillColor(INK); c.setFont("DVS", 8.4)
for i, t in enumerate([
    "A)  USŁUGOWO: po odbiorze rozkroju zawozisz fronty i boki do lokalnej stolarni z CNC/wiertarką wielowrzecionową",
    "     (szukaj: \u201eusługowe wiercenie płyt / rozwiert Śląsk\u201d; dajesz im str. 2 i 4 instrukcji szczegółowej jako plan wierceń;",
    "     koszt zwykle 1\u20135 zł/otwór — przy tej kuchni ~150\u2013400 zł). Wtedy Ty nie wiercisz NIC.",
    "B)  SAM Z SZABLONAMI (~200 zł): wiertło stopniowe do konfirmatów (~15 zł) + przyrząd do puszek 35",
    "     z ogranicznikiem głębokości (Wolfcraft/GTV, 60\u2013120 zł) + kątownik i szydło. Szablon pilnuje 22,5 i głębokości",
    "     12,5 za Ciebie — wiercenie przestaje być loterią. Wymiary: str. 2 i 4 instrukcji szczegółowej.",
]):
    c.drawString(20*mm, PH-43*mm - i*5*mm, t)
c.setFillColor(GREY); c.setFont("DVS", 7.6)
c.drawString(20*mm, PH-76*mm, "Przy zamówieniu w KornerGo zaznacz za to: oklejanie krawędzi (fronty 1,0 / korpusy 0,4) + transport (słupek 2,38 m).")

y = PH-86*mm
c.setFillColor(RED); c.setFont("DVS-B", 9.5); c.drawString(16*mm, y, "POTEM KAŻDA SZAFKA = 6 RUCHÓW:")
steps = [
    ("1", "Rozłóż części jednej szafki na kocu, sprawdź wymiary z listą formatek. Otwory masz z drogi A albo wiercisz wg szablonów (droga B) — zawsze PRZED skręcaniem, na leżąco."),
    ("2", "Skręć: bok + dno + drugi bok + 2 trawersy (górne: pełny wieniec). Konfirmat w gotowy otwór, wkrętarka na wolnych obrotach, ostatnie pół obrotu ręcznie."),
    ("3", "Przykręć plecy HDF równo z krawędziami: narożnik → wyrównanie → wkręt co ~15 cm. Plecy same ustawiają kąt prosty."),
    ("4", "Dolne: przykręć 4 nóżki (płytki ~5 cm od rogów). Górne: wkręć zawieszki w gotowe otwory."),
    ("5", "Wciśnij zawiasy w gotowe puszki we froncie, przykręć, zatrzaśnij front na prowadniki (klik)."),
    ("6", "Wyreguluj front 3 śrubami zawiasu (przód=lewo/prawo, tył=docisk, prowadnik=góra/dół) do równej szczeliny 2–3 mm."),
]
y -= 8*mm
for n, t in steps:
    c.setFillColor(RED); c.circle(19*mm, y+1.2*mm, 3*mm, stroke=0, fill=1)
    c.setFillColor(colors.white); c.setFont("DVS-B", 8.6); c.drawCentredString(19*mm, y-0.9*mm, n)
    c.setFillColor(INK); c.setFont("DVS", 8.6)
    words, line, yy = t.split(), "", y
    for wd in words:
        if c.stringWidth(line+" "+wd, "DVS", 8.6) > 155*mm:
            c.drawString(25*mm, yy, line.strip()); yy -= 4.2*mm; line = wd
        else:
            line += " " + wd
    c.drawString(25*mm, yy, line.strip())
    y = yy - 7.5*mm

y -= 2*mm
c.setFillColor(RED); c.setFont("DVS-B", 9.5); c.drawString(16*mm, y, "USTAWIANIE (kolejność w kuchni):")
c.setFillColor(INK); c.setFont("DVS", 8.6)
for t in [
    "ściana lodówki → ciąg okna → ciąg indukcji → ramię (przykręć kątownikami do podłogi) → górne na listwie → blaty na końcu",
    "poziomuj nóżkami od NAJWYŻSZEGO punktu podłogi; sąsiednie korpusy skręcaj ze sobą (2 wkręty przez bok, pod zawiasami)",
    "blaty: najpierw przymiarka na sucho, wycięcia (indukcja 56×49, zlew wg szablonu z kartonu) posmaruj silikonem, przykręć od spodu wkrętami MAX 4×30",
]:
    words, line, yy = t.split(), "", y-6*mm
    for wd in words:
        if c.stringWidth(line+" "+wd, "DVS", 8.6) > 168*mm:
            c.drawString(20*mm, yy, "• "+line.strip() if line == t.split()[0] else line.strip()); yy -= 4.2*mm; line = wd
        else:
            line += " " + wd
    c.drawString(20*mm, yy, line.strip()) if line != t else None
    # prostsze: rysuj całość zawijaną
    y = yy - 6*mm

# 3 zasady na dole
c.setFillColor(BG); c.rect(16*mm, 18*mm, PW-32*mm, 26*mm, stroke=0, fill=1)
c.setFillColor(RED); c.setFont("DVS-B", 9.5); c.drawString(20*mm, 38*mm, "TYLKO 3 RZECZY MOGĄ CI TO ZEPSUĆ:")
c.setFillColor(INK); c.setFont("DVS", 8.6)
c.drawString(20*mm, 32*mm, "1. Zamienione boki lewy/prawy — przed skręceniem sprawdź, czy otwory są od WEWNĄTRZ szafki.")
c.drawString(20*mm, 27*mm, "2. Krzywo przykręcone plecy — zawsze od narożnika, po wyrównaniu krawędzi.")
c.drawString(20*mm, 22*mm, "3. Za długie wkręty w blat lub front (max 4×30 w blat, 4×16 w HDF i okucia).")

c.setFillColor(GREY); c.setFont("DVS", 6.4)
c.drawString(16*mm, 12*mm, "Kuchnia U + ramię L · wersja PROSTA (otwory: usługa lub szablony) · szczegóły i wymiary awaryjnie: kuchnia-wyspa-montaz-korpusow.pdf · 2026-08-12")
c.showPage(); c.save()
print("OK:", OUT)
