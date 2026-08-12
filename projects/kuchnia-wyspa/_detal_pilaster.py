#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detal: pilaster 15,5 (pionowy, na całą wysokość) i górne szafki na ścianie A.

Zastępuje błędny _detal_gzyms.py (interpretacja „belka pod sufitem" — odwołana 2026-08-12).

    python3 _detal_pilaster.py kuchnia-wyspa-detal-pilaster.pdf
"""
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = sys.argv[1] if len(sys.argv) > 1 else "kuchnia-wyspa-detal-pilaster.pdf"
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVS-B", FD + "DejaVuSans-Bold.ttf"))
PW, PH = A4

INK = colors.HexColor("#1a1a1a")
WOOD = colors.HexColor("#8a6a4a")
GREY = colors.HexColor("#8a8a8a")
RED = colors.HexColor("#a05252")
ZIEL = colors.HexColor("#4f7a52")
BETON = colors.HexColor("#b9b2a6")
BG = colors.HexColor("#f5f1ea")
FRONT = colors.HexColor("#c9b79c")
KORP = colors.HexColor("#efe6d6")

# --- geometria ciągu A (mm) ---
A_DL = 1950          # długość ciągu A od ściany B
PIL_DL = 670         # długość pilastra wzdłuż ściany A
PIL_GL = 155         # ile pilaster wystaje ze ściany A  [P]
GL = 400             # głębokość korpusu górnych (decyzja inwestora)
GA1_GL = GL - PIL_GL  # 245 — GA1 wisi na LICU pilastra
FR = 19
GA2_DL = 450         # zwykła nad DA1
GA3_DL = 600         # OKAP nad DA2 (indukcja)
BLENDA_DL = A_DL - PIL_DL - GA2_DL - GA3_DL   # 230

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Detal — pilaster 15,5 i górne szafki")


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
    c.setFont("DVS", 6.4)
    c.drawCentredString((x1 + x2) / 2, y + (1.4 * mm if ponad else -3.2 * mm), txt)


def dim_v(y1, y2, x, txt, kolor=GREY):
    c.setStrokeColor(kolor)
    c.setLineWidth(0.4)
    c.line(x, y1, x, y2)
    for y, s in ((y1, 1), (y2, -1)):
        _grot(x, y, 0.9 * mm, s * 1.6 * mm)
        _grot(x, y, -0.9 * mm, s * 1.6 * mm)
    c.saveState()
    c.translate(x - 1.2 * mm, (y1 + y2) / 2)
    c.rotate(90)
    c.setFillColor(kolor)
    c.setFont("DVS", 6.4)
    c.drawCentredString(0, 0, txt)
    c.restoreState()


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
# STRONA 1 — RZUT Z GÓRY ciągu A (to, o co pytałeś)
# =====================================================================
naglowek("DETAL 1/2 — PILASTER 15,5 W RZUCIE Z GÓRY (ciąg A, szafki górne)",
         "Pilaster jest PIONOWY — słup na całą wysokość, nie belka pod sufitem. Tu patrzysz na ciąg A od góry.")

S = 0.086
X0 = 20 * mm                     # początek ciągu = lico ściany B
YW = PH - 62 * mm                # lico ściany A


def X(d):
    return X0 + d * S * mm


def Y(g):
    return YW - g * S * mm       # g = głębokość w głąb pomieszczenia


# ściana A
c.setFillColor(BETON)
c.rect(X(-60), YW, (A_DL + 120) * S * mm, 55 * S * mm, stroke=0, fill=1)
kreskuj(X(-60), YW, X(A_DL + 60), YW + 55 * S * mm)
c.setStrokeColor(INK)
c.setLineWidth(1.2)
c.line(X(-60), YW, X(A_DL + 60), YW)
c.setFillColor(GREY)
c.setFont("DVS", 6.6)
c.drawString(X(A_DL + 8), YW + 20 * S * mm, "ściana A")

# ściana B (lewa krawędź)
c.setFillColor(BETON)
c.rect(X(-60), Y(700), 60 * S * mm, (700 + 55) * S * mm, stroke=0, fill=1)
kreskuj(X(-60), Y(700), X(0), YW + 55 * S * mm)
c.setStrokeColor(INK)
c.line(X(0), YW, X(0), Y(700))
c.saveState()
c.translate(X(-30), Y(430))
c.rotate(90)
c.setFillColor(GREY)
c.setFont("DVS", 6.6)
c.drawCentredString(0, 0, "ściana B (okno)")
c.restoreState()

# PILASTER
c.setFillColor(colors.HexColor("#a89e8e"))
c.rect(X(0), Y(PIL_GL), PIL_DL * S * mm, PIL_GL * S * mm, stroke=0, fill=1)
kreskuj(X(0), Y(PIL_GL), X(PIL_DL), YW)
c.setStrokeColor(RED)
c.setLineWidth(1.4)
c.rect(X(0), Y(PIL_GL), PIL_DL * S * mm, PIL_GL * S * mm, stroke=1, fill=0)
c.setFillColor(RED)
c.setFont("DVS-B", 7.4)
c.drawCentredString(X(PIL_DL / 2), Y(PIL_GL) + 5.5 * mm, "PILASTER")
c.setFont("DVS", 6.4)
c.drawCentredString(X(PIL_DL / 2), Y(PIL_GL) + 2.2 * mm, "670 × 155, PIONOWY — od podłogi do sufitu")

# szafki górne
c.setStrokeColor(INK)
c.setLineWidth(0.8)
c.setFillColor(KORP)
c.rect(X(0), Y(GL), PIL_DL * S * mm, GA1_GL * S * mm, stroke=1, fill=1)              # GA1
c.rect(X(PIL_DL), Y(GL), GA2_DL * S * mm, GL * S * mm, stroke=1, fill=1)             # GA2
c.rect(X(PIL_DL + GA2_DL), Y(GL), GA3_DL * S * mm, GL * S * mm, stroke=1, fill=1)    # GA3 okap
c.rect(X(PIL_DL + GA2_DL + GA3_DL), Y(GL), BLENDA_DL * S * mm, GL * S * mm, stroke=1, fill=1)  # blenda
# fronty
c.setFillColor(FRONT)
c.rect(X(0), Y(GL + FR), A_DL * S * mm, FR * S * mm, stroke=1, fill=1)

c.setFillColor(INK)
c.setFont("DVS-B", 7)
c.drawCentredString(X(PIL_DL / 2), Y(GL) + 4 * mm, "GA1")
c.setFont("DVS", 6.3)
c.drawCentredString(X(PIL_DL / 2), Y(GL) + 1.4 * mm, "245 gł.")
c.setFillColor(INK)
c.setFont("DVS-B", 7)
c.drawCentredString(X(PIL_DL + GA2_DL / 2), Y(GL) + 9 * mm, "GA2")
c.drawCentredString(X(PIL_DL + GA2_DL + GA3_DL / 2), Y(GL) + 9 * mm, "GA3 — OKAP")
c.drawCentredString(X(PIL_DL + GA2_DL + GA3_DL + BLENDA_DL / 2), Y(GL) + 9 * mm, "blenda")
c.setFont("DVS", 6.3)
c.drawCentredString(X(PIL_DL + GA2_DL / 2), Y(GL) + 6.2 * mm, "400 gł.")
c.drawCentredString(X(PIL_DL + GA2_DL + GA3_DL / 2), Y(GL) + 6.2 * mm, "400 gł.")
c.drawCentredString(X(PIL_DL + GA2_DL + GA3_DL + BLENDA_DL / 2), Y(GL) + 6.2 * mm, "400")

# linia frontów
c.setStrokeColor(ZIEL)
c.setLineWidth(0.7)
c.setDash(3, 2)
c.line(X(-60), Y(GL + FR), X(A_DL + 60), Y(GL + FR))
c.setDash()
c.setFillColor(ZIEL)
c.setFont("DVS-B", 6.8)
c.drawString(X(A_DL + 8), Y(GL + FR) - 4.5 * mm, "linia frontów")
c.setFont("DVS", 6.3)
c.drawString(X(A_DL + 8), Y(GL + FR) - 7.5 * mm, "jedna płaszczyzna,")
c.drawString(X(A_DL + 8), Y(GL + FR) - 10.5 * mm, "bez uskoku")

# wymiary
dim_v(Y(PIL_GL), YW, X(-95), "155")
dim_v(Y(GL), Y(PIL_GL), X(-95), "245")
dim_v(Y(GL + FR), YW, X(-150), "419")
dim_h(X(0), X(PIL_DL), Y(GL) - 8 * mm, "670 (GA1 = szerokość pilastra)", ponad=False)
dim_h(X(PIL_DL), X(PIL_DL + GA2_DL), Y(GL) - 8 * mm, "450", ponad=False)
dim_h(X(PIL_DL + GA2_DL), X(PIL_DL + GA2_DL + GA3_DL), Y(GL) - 8 * mm, "600 (okap nad indukcją)", ponad=False)
dim_h(X(PIL_DL + GA2_DL + GA3_DL), X(A_DL), Y(GL) - 8 * mm, "230", ponad=False)
dim_h(X(0), X(A_DL), Y(GL) - 16 * mm, "1950 = 195 cm ciągu A (od ściany B)", ponad=False)

# ramka wyjaśniająca
c.setFillColor(BG)
c.rect(15 * mm, 86 * mm, PW - 30 * mm, 46 * mm, stroke=0, fill=1)
c.setFillColor(RED)
c.setFont("DVS-B", 9)
c.drawString(19 * mm, 125 * mm, "NA TYM POLEGA CAŁA SZTUCZKA")
c.setFillColor(INK)
c.setFont("DVS", 7.4)
for i, t in enumerate([
        "GA1 nie stoi na ścianie — wisi na LICU PILASTRA. Dlatego ma 245 gł., a nie 400: 155 + 245 = 400.",
        "GA2 i GA3 wiszą na ścianie i mają pełne 400. Efekt: wszystkie fronty w jednej płaszczyźnie, bez uskoku.",
        "",
        "I dlatego Twoje 40 cm to dobry wybór: przy standardowych 320 szafka nad pilastrem miałaby 320 − 155 = 165 mm",
        "głębokości — czyli półkę bez sensu. Przy 400 wychodzi 245 mm i szafka realnie działa.",
        "Koszt: fronty stoją 8 cm bliżej głowy (cofnięcie od lica blatu 181 mm zamiast 261 mm)."]):
    c.setFillColor(RED if i == 3 else INK)
    c.setFont("DVS-B" if i == 3 else "DVS", 7.4)
    c.drawString(19 * mm, (119 - i * 5) * mm, t)

stopka("Wymiary w mm. Pilaster 155 [P] — długość 670 [~] do potwierdzenia pomiarem. "
       "Kuchnia U + ramię L · detal pilastra · 2026-08-12")
c.showPage()

# =====================================================================
# STRONA 2 — korekta
# =====================================================================
naglowek("DETAL 2/2 — KOREKTA PO TWOJEJ UWADZE",
         "Wcześniej odczytałem ten element ze zdjęcia jako belkę pod sufitem. Jest pionowy — poniżej co z tego wynika.")

y = PH - 38 * mm
c.setFillColor(RED)
c.setFont("DVS-B", 9.5)
c.drawString(15 * mm, y, "ODWOŁUJĘ (dotyczyło „gzymsu pod sufitem\" — nie istnieje)")
y -= 7 * mm
c.setFillColor(INK)
c.setFont("DVS", 7.6)
for t in [
    "• wycięcia 160 × (Hg+5) w bokach szafek GA2, GA3, GC1, GC2 — NIEPOTRZEBNE, nic nie wycinasz",
    "• wieniec górny 240 — wraca normalny, pełne 400",
    "• półka stała wymuszona linią wycięcia — może być zwykła, ruchoma",
    "• listwa montażowa „pod gzymsem\" — wraca pod sufit, standardowo",
    "• wycięcia w słupku C2 i nadstawce C4 — niepotrzebne; kratka wentylacyjna wraca na swoje miejsce",
    "• pytanie o wysokość Hg — nieaktualne",
    "• sprzeczność „gzyms vs okno do sufitu\" (pkt 11b planu) — nieaktualna, okno spokojnie idzie do sufitu",
]:
    c.drawString(19 * mm, y, t)
    y -= 5 * mm

y -= 4 * mm
c.setFillColor(ZIEL)
c.setFont("DVS-B", 9.5)
c.drawString(15 * mm, y, "ZOSTAJE W MOCY (to było policzone dobrze)")
y -= 7 * mm
c.setFillColor(INK)
c.setFont("DVS", 7.6)
for t in [
    "• górne szafki 400 gł. — Twoja propozycja; uzasadnienie inne, niż napisałem, ale wniosek ten sam (str. 1)",
    "• GA1 = 245 gł. zamiast 305 — to była realna pomyłka w planie (pilaster wystaje 155, nie 15)",
    "• wszystkie fronty w jednej płaszczyźnie, zabudowa do sufitu 2478",
    "• pilaster 155 × 670 jest w rzucie od początku — to on odpowiada za różnicę 254,6 − 238,9 ≈ 15,5",
]:
    c.drawString(19 * mm, y, t)
    y -= 5 * mm

y -= 4 * mm
c.setFillColor(RED)
c.setFont("DVS-B", 9.5)
c.drawString(15 * mm, y, "JEDNO PYTANIE, KTÓRE MUSZĘ ZADAĆ")
y -= 7 * mm
c.setFillColor(INK)
c.setFont("DVS", 7.6)
for t, b in [
    ("Napisałeś, że ten uskok „pomniejsza jakby całe pomieszczenie\". W rzucie mam go jako słup 155 × 670", False),
    ("przy narożniku ścian A i B — czyli lokalnie, na 67 cm. Ale jeśli te 15,5 idzie wzdłuż CAŁEJ ściany", False),
    ("(np. cała ściana A albo cała C), to zmienia się głębokość zabudowy na tej ścianie i trzeba przeliczyć moduły.", False),
    ("", False),
    ("Zmierz jedną rzecz: ile centymetrów ma uskok WZDŁUŻ ściany (67 cm czy cała długość?) i przy której ścianie.", True),
]:
    c.setFillColor(RED if b else INK)
    c.setFont("DVS-B" if b else "DVS", 7.6)
    c.drawString(19 * mm, y, t)
    y -= 5 * mm

y -= 4 * mm
c.setFillColor(BG)
c.rect(15 * mm, y - 26 * mm, PW - 30 * mm, 30 * mm, stroke=0, fill=1)
c.setFillColor(WOOD)
c.setFont("DVS-B", 8.5)
c.drawString(19 * mm, y - 3 * mm, "KONTROLA Z TWOICH WŁASNYCH WYMIARÓW")
c.setFillColor(INK)
c.setFont("DVS", 7.4)
for i, t in enumerate([
        "254,6 (szerokość A↔C)  −  238,9 (długość ściany B)  =  15,7  ≈  15,5",
        "To dokładnie ten pilaster. Gdyby uskok szedł wzdłuż całej ściany, ta różnica i tak wyszłaby ta sama —",
        "dlatego sam rzut tego nie rozstrzyga i potrzebuję od Ciebie długości uskoku."]):
    c.drawString(19 * mm, y - (9 + i * 5) * mm, t)

stopka("Kuchnia U + ramię L · detal pilastra · korekta 2026-08-12")
c.showPage()
c.save()
print("OK:", OUT)
