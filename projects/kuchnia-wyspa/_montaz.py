#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Instrukcja skręcania korpusów — kuchnia v3.5 (PDF, krok po kroku, wektor)."""
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = sys.argv[1] if len(sys.argv) > 1 else "montaz.pdf"
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVS-B", FD + "DejaVuSans-Bold.ttf"))

PW, PH = landscape(A4)
INK = colors.HexColor("#1a1a1a"); WOOD = colors.HexColor("#8a6a4a")
FILL = colors.HexColor("#efe9df"); GREY = colors.HexColor("#8a8a8a")
RED = colors.HexColor("#a05252"); BLU = colors.HexColor("#4a6a8a")
c = canvas.Canvas(OUT, pagesize=(PW, PH)); c.setTitle("Montaż korpusów — kuchnia v3.5")


def header(t, s):
    c.setFillColor(WOOD); c.setFont("DVS-B", 12.5); c.drawString(14*mm, PH-13*mm, t)
    c.setFillColor(GREY); c.setFont("DVS", 7.2); c.drawString(14*mm, PH-18*mm, s)
    c.setFont("DVS", 6.4)
    c.drawString(14*mm, 7*mm, "Kuchnia U + ramię L — instrukcja skręcania korpusów (do listy FORMATKI R1) · 2026-08-12 · montaż samodzielny")
    c.drawRightString(PW-14*mm, 7*mm, f"str. {c.getPageNumber()}")
    c.setStrokeColor(WOOD); c.setLineWidth(1); c.line(14*mm, PH-20*mm, PW-14*mm, PH-20*mm)


def steps(x, y, items, w=88*mm, title=None):
    if title:
        c.setFillColor(INK); c.setFont("DVS-B", 8.6); c.drawString(x, y, title); y -= 5.2*mm
    for i, s in enumerate(items, 1):
        c.setFillColor(RED); c.circle(x+2.2*mm, y+1.0*mm, 2.2*mm, stroke=0, fill=1)
        c.setFillColor(colors.white); c.setFont("DVS-B", 6.4); c.drawCentredString(x+2.2*mm, y-0.6*mm, str(i))
        c.setFillColor(INK); c.setFont("DVS", 7.0)
        # zawijanie
        words, line, yy = s.split(), "", y
        for wd in words:
            if c.stringWidth(line+" "+wd, "DVS", 7.0) > w - 8*mm:
                c.drawString(x+6.5*mm, yy, line.strip()); yy -= 3.4*mm; line = wd
            else:
                line += " " + wd
        c.drawString(x+6.5*mm, yy, line.strip())
        y = yy - 5.4*mm
    return y


def dot(x, y, col=RED, r=1.5):
    c.setFillColor(col); c.circle(x, y, r*mm, stroke=0, fill=1)


def box(x, y, w, h, fill=FILL, lw=0.9):
    c.setStrokeColor(INK); c.setLineWidth(lw); c.setFillColor(fill)
    c.rect(x, y, w, h, stroke=1, fill=1)


def label(x, y, t, col=INK, size=6.4, bold=False, center=False):
    c.setFillColor(col); c.setFont("DVS-B" if bold else "DVS", size)
    (c.drawCentredString if center else c.drawString)(x, y, t)


# ================= STRONA 1: KORPUS DOLNY =================
header("1. KORPUS DOLNY (DA1, DA2, RL1, RL2, DB0, DB1, DC1) — kolejność skręcania",
       "płyta 18 · konfirmaty 7×50 (otwór 4,5 przez bok + nakiełek 7) · plecy HDF nakładane, wkręty 4×16 co ~150 mm · nóżki 150")

# rysunek: widok rozłożony od frontu
X, Y = 22*mm, 52*mm
box(X, Y, 8*mm, 62*mm); label(X+4*mm, Y+64*mm, "bok L", center=True)             # bok lewy
box(X+64*mm, Y, 8*mm, 62*mm); label(X+68*mm, Y+64*mm, "bok P", center=True)      # bok prawy
box(X+10*mm, Y+2*mm, 52*mm, 7*mm); label(X+36*mm, Y+4.2*mm, "DNO", center=True, bold=True)
box(X+10*mm, Y+53*mm, 14*mm, 6*mm); label(X+17*mm, Y+60.5*mm, "trawers", size=5.6, center=True)
box(X+48*mm, Y+53*mm, 14*mm, 6*mm); label(X+55*mm, Y+60.5*mm, "trawers", size=5.6, center=True)
for yy in (Y+5.5*mm,):
    for xx in (X+4*mm, X+68*mm): dot(xx, yy)
for xx in (X+4*mm, X+68*mm):
    dot(xx, Y+56*mm)
label(X+36*mm, Y-6*mm, "konfirmaty: dno 3/stronę (przez bok), trawersy 2/stronę", size=6.0, col=RED, center=True)
# plecy
c.setStrokeColor(BLU); c.setDash(3, 3); c.rect(X-2*mm, Y-2*mm, 76*mm, 68*mm); c.setDash()
label(X+36*mm, Y+70*mm, "PLECY HDF — nakładane na całość (niebieska linia)", size=6.0, col=BLU, center=True)
# nóżki
for xx in (X+6*mm, X+66*mm):
    c.setFillColor(GREY); c.rect(xx-1.5*mm, Y-9*mm, 3*mm, 6*mm, stroke=0, fill=1)
label(X+36*mm, Y-13*mm, "nóżki 150 — 4 szt, ~50 mm od krawędzi", size=6.0, col=GREY, center=True)

steps(120*mm, PH-32*mm, [
    "Rozłóż formatki na kocu/kartonie. Sprawdź komplet i obrzeża (fronty 1,0 na 4 krawędziach). Krawędzie PRZEDNIE boków i dna muszą być równo — to baza.",
    "Bok lewy + DNO: 3 konfirmaty przez bok w czoło dna (otwór 4,5 przez bok, nakiełek 7 w czole — pomijasz, jeśli rozkrój był z CNC). Dno na wysokości dolnej krawędzi boku.",
    "Bok prawy + dno — tak samo. Korpus stoi już w kształcie U.",
    "Trawersy górne (przedni na płask, tylny na sztorc): po 2 konfirmaty na stronę. W szafce zlewowej DB1 zamiast pleców dajesz DRUGĄ listwę na dole z tyłu.",
    "Zmierz PRZEKĄTNE korpusu — muszą być równe (±1 mm). Skoryguj lekkim dociśnięciem.",
    "Plecy HDF nakładane: zacznij od jednego narożnika, wyrównaj krawędzie i przykręcaj 4×16 co ~150 mm dookoła — plecy USTAWIAJĄ kąt prosty na stałe.",
    "Przykręć nóżki 150 (4 szt, ~50 mm od krawędzi; przednie z klipsami cokołu).",
    "DC1 narożna: to samo + blenda ślepa przykręcona od wewnątrz do boku; DB0 cargo: korpus jw., prowadnice cargo wg instrukcji z opakowania.",
], w=155*mm, title="KROK PO KROKU (każda dolna tak samo):")
c.showPage()

# ================= STRONA 2: SZUFLADY / PIEKARNIK / ZLEW =================
header("2. WARIANTY DOLNYCH: szufladowa DA1 · piekarnikowa DA2 · zlewowa DB1",
       "prowadnice 500 pełny wysuw z dociągiem (Blum/GTV) · nisza piekarnika wg karty (560×590–600) · zlew: silikon na każde cięcie")

X, Y = 20*mm, 40*mm
box(X, Y, 8*mm, 62*mm); box(X+56*mm, Y, 8*mm, 62*mm)
for i, yy in enumerate((Y+8*mm, Y+27*mm, Y+46*mm)):
    c.setStrokeColor(RED); c.setLineWidth(1.4); c.line(X+9*mm, yy, X+55*mm, yy)
    label(X+66*mm, yy-1*mm, f"prowadnica {i+1}", size=5.8, col=RED)
label(X+32*mm, Y+66*mm, "DA1: 3 pary prowadnic — obie strony NA TEJ SAMEJ wysokości", size=6.0, center=True)
label(X+32*mm, Y-5*mm, "wysokości od dna: wg systemu szuflad (rozstaw frontów 236)", size=5.6, col=GREY, center=True)

steps(105*mm, PH-30*mm, [
    "DA1 SZUFLADOWA: korpus jak na str. 1. Prowadnice przykręć PRZED zawieszeniem frontów — odmierz wysokości od dna i użyj kątownika/szablonu; lewa i prawa muszą być idealnie równolegle, inaczej szuflada skrzypi i nie domyka.",
    "Złóż szuflady systemowe (boki+dno+tył wg instrukcji systemu), wsuń na prowadnice, potem wepnij fronty na zaczepy i wyreguluj (regulacja we froncie systemu ±2 mm).",
    "DA2 PIEKARNIKOWA: trawers nośny poziomo tak, by ŚWIATŁO NISZY = wysokość z karty piekarnika (typowo 590–600 od góry korpusu). Piekarnik opiera się na trawersie — 2 konfirmaty/stronę + kątowniki.",
    "W plecach DA2 wytnij otwór na kabel i zostaw szczelinę wentylacyjną z tyłu; nad piekarnikiem NIC nie zabudowuj na styk — luz wg karty.",
    "Szuflada dolna DA2 (front 110): płytsza — sprawdź kolizję z korpusem płyty (Bosch 5,6 pod blatem!): górna krawędź boków szuflady min. 70 mm od blatu.",
    "DB1 ZLEWOWA: bez pleców (2 listwy usztywniające). Po wycięciu otworu w blacie POMALUJ silikonem każdą ciętą krawędź. Syfon i podejścia przechodzą przez tylną ścianę/dno — otwory otwornicą, też silikonowane.",
    "Pod zlewem połóż matę ochronną na dno; kosze segregacji montuj po podłączeniu hydrauliki.",
], w=140*mm, title="RÓŻNICE WZGLĘDEM KORPUSU BAZOWEGO:")
c.showPage()

# ================= STRONA 3: GÓRNE / SŁUPEK / NADSTAWKA =================
header("3. GÓRNE (GA1-3, GC1-2) · SŁUPEK C2 · NADSTAWKA C4",
       "górne 998 do sufitu — zawieszki regulowane + listwa montażowa na 1480 · słupek 2378: przekątna 2448 < sufit 2478 ✓ da się obrócić do pionu")

X, Y = 20*mm, 46*mm
box(X, Y, 8*mm, 56*mm); box(X+46*mm, Y, 8*mm, 56*mm)
box(X+9*mm, Y+50*mm, 36*mm, 5*mm); box(X+9*mm, Y+1*mm, 36*mm, 5*mm)
label(X+27*mm, Y+58*mm, "wieniec górny i DOLNY (pełne)", size=5.8, center=True)
for xx in (X+6*mm, X+48*mm): dot(xx, Y+52*mm, BLU, 1.8)
label(X+27*mm, Y-5*mm, "zawieszki regulowane w górnych narożnikach (niebieskie)", size=5.8, col=BLU, center=True)
c.setStrokeColor(BLU); c.setLineWidth(2); c.line(X-6*mm, Y+62*mm, X+62*mm, Y+62*mm)
label(X+27*mm, Y+65*mm, "listwa montażowa na ścianie — góra na 2478 (sufit), zawieszka łapie od środka", size=5.4, col=BLU, center=True)

steps(105*mm, PH-30*mm, [
    "GÓRNA: korpus jak dolny, ale zamiast trawersów PEŁNY wieniec górny i dolny (2 formatki „dno/wieniec\"). Zawieszki regulowane wkręć w górne narożniki OD WEWNĄTRZ, wytnij w plecach okienka na haki.",
    "Listwę montażową przykręć do ściany poziomo (poziomica!) tak, by góra szafek licowała z sufitem 2478; kołki dobierz do ściany (cegła: kołek 8 + wkręt 6; przy pilastrze wierć bez udaru).",
    "Zawieś szafki, zepnij korpusy ze sobą śrubami dwustronnymi, wyreguluj zawieszkami (docisk + wysokość), szczelinę przy suficie zamyka blenda docinana.",
    "Półki na podpórki 5 mm — otwory co 32 mm (CNC) dają pełną regulację.",
    "SŁUPEK C2: skręcaj NA PODŁODZE w salonie (jest miejsce), plecy przykręć przed postawieniem. Przekątna 2448 < 2478 — obrócisz go do pionu bez zahaczenia o sufit, ale prowadź przy ścianie.",
    "Słupek poziomujesz nóżkami, kotwisz do ściany C 2 kątownikami u góry (kołki), potem cargo/półki.",
    "NADSTAWKA C4: prosta skrzynka 660×528 — skręć, postaw na wysokości ~1950 na wspornikach/łatach przykręconych do ściany, zepnij z bokiem zabudowy i słupkiem. Wywierć kratkę wentylacyjną (szereg otworów 35 lub kratka) w dnie i w froncie górnym.",
    "Bok wykończeniowy zabudowy lodówki (2478×680): pion sprawdź poziomicą, kotwy do ścianki + skręcenie z nadstawką; między bokiem a ścianką blenda dystansowa ~70 (drzwi lodówki >90°).",
], w=140*mm, title="KROK PO KROKU:")
c.showPage()

# ================= STRONA 4: ZAWIASY, FRONTY, REGULACJA, KOTWIENIE =================
header("4. ZAWIASY I FRONTY · REGULACJA 3D · COKOŁY I KOTWIENIE RAMIENIA",
       "puszka 35 mm: środek 22,5 od krawędzi frontu (K=5) · prowadnik na boku 37 mm od krawędzi przedniej · dolne 2 zawiasy/front, górne 996 → 3")

X, Y = 20*mm, 44*mm
box(X, Y, 34*mm, 60*mm, FILL)                       # front
c.setFillColor(colors.white); c.circle(X+8*mm, Y+50*mm, 4.6*mm, stroke=1, fill=1)
c.circle(X+8*mm, Y+30*mm, 4.6*mm, stroke=1, fill=1)
c.circle(X+8*mm, Y+10*mm, 4.6*mm, stroke=1, fill=1)
label(X+17*mm, Y+63*mm, "FRONT górny 996 — 3 puszki 35", size=6.0, center=True)
label(X+8*mm, Y+2*mm, "22,5 od krawędzi", size=5.2, col=RED, center=True)
box(X+52*mm, Y, 8*mm, 60*mm)
for yy in (Y+50*mm, Y+30*mm, Y+10*mm):
    dot(X+56*mm, yy, BLU, 1.6)
label(X+56*mm, Y+63*mm, "prowadniki na boku (37 mm)", size=5.6, col=BLU, center=True)
c.setStrokeColor(GREY); c.setDash(2, 2)
for yy in (Y+50*mm, Y+30*mm, Y+10*mm):
    c.line(X+12.6*mm, yy, X+52*mm, yy)
c.setDash()

steps(105*mm, PH-30*mm, [
    "Zawiasy: wciśnij zawias w puszkę 35 we froncie (jeśli rozkrój z CNC — otwory gotowe; jeśli nie: wiertło puszkowe 35, środek 22,5 mm od krawędzi, głębokość 12,5 — użyj ogranicznika!). Prowadniki przykręć na boku w linii 37 mm od przedniej krawędzi.",
    "Wepnij front (klik), zamknij i sprawdź szczeliny: równa 2–3 mm dookoła.",
    "REGULACJA 3D każdego zawiasu: śruba przednia = lewo/prawo (równość szczelin pionowych), śruba tylna/mimośród = docisk do korpusu, prowadnik góra/dół = wysokość. Reguluj od góry frontu do dołu, po jednej śrubie.",
    "Fronty bezuchwytowe: krawędź górna dolnych frontów — profil gola alu wpuszczony pod blat ALBO frez C w płycie (zlecony w CNC) — decyzja przed zamówieniem frontów!",
    "COKÓŁ: listwa 150 czarna na klipsach do przednich nóżek; w cokole pod lodówką wytnij kratkę wentylacyjną. Uszczelka cokołu (Silikorner, korner.eu) od dołu.",
    "KOTWIENIE RAMIENIA: korpusy RL1+RL2 skręcone ze sobą i z DA-ciągiem; w cokole 4 kątowniki do posadzki (wiercenie 8 w wylewkę PRZED ułożeniem posadzki docelowej albo przez posadzkę z tuleją) — ramię nie może „jeździć\".",
    "BLATY na końcu: połóż na sucho, sprawdź przyleganie do ścian (krzywizny → docinka), łączenia w narożach na śruby łącznikowe + silikon, wycięcia posmaruj silikonem, dopiero potem przykręć od spodu przez trawersy (wkręty 4×30 — NIE dłuższe, blat 38!).",
    "Na koniec: LED pod górnymi (taśma w profilu, zasilacz w GA1), panel ryflowany na rewers ramienia (klej montażowy + wkręty od wewnątrz), listwy przyblatowe.",
], w=140*mm, title="KROK PO KROKU:")
c.showPage()
c.save()
print("OK:", OUT)
