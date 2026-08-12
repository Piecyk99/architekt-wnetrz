#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Instrukcja skręcania dla początkującego — kuchnia v3.5. Wymiary wiercenia na rysunkach."""
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
c = canvas.Canvas(OUT, pagesize=(PW, PH)); c.setTitle("Montaż dla początkującego — kuchnia v3.5")


def header(t, s):
    c.setFillColor(WOOD); c.setFont("DVS-B", 12); c.drawString(13*mm, PH-12*mm, t)
    c.setFillColor(GREY); c.setFont("DVS", 7.0); c.drawString(13*mm, PH-17*mm, s)
    c.setFont("DVS", 6.2)
    c.drawString(13*mm, 6*mm, "Kuchnia U + ramię L · instrukcja montażu dla początkującego (wymiary wiercenia w mm) · wersja 2 · 2026-08-12")
    c.drawRightString(PW-13*mm, 6*mm, f"str. {c.getPageNumber()}")
    c.setStrokeColor(WOOD); c.setLineWidth(1); c.line(13*mm, PH-19*mm, PW-13*mm, PH-19*mm)


def steps(x, y, items, w, title=None, num=True):
    if title:
        c.setFillColor(INK); c.setFont("DVS-B", 8.4); c.drawString(x, y, title); y -= 5.4*mm
    for i, s in enumerate(items, 1):
        if num:
            c.setFillColor(RED); c.circle(x+2.2*mm, y+1.0*mm, 2.3*mm, stroke=0, fill=1)
            c.setFillColor(colors.white); c.setFont("DVS-B", 6.6); c.drawCentredString(x+2.2*mm, y-0.7*mm, str(i))
        else:
            c.setFillColor(RED); c.setFont("DVS-B", 7.2); c.drawString(x, y, "•")
        c.setFillColor(INK); c.setFont("DVS", 7.0)
        words, line, yy = s.split(), "", y
        for wd in words:
            if c.stringWidth(line+" "+wd, "DVS", 7.0) > w - 8*mm:
                c.drawString(x+6.5*mm, yy, line.strip()); yy -= 3.5*mm; line = wd
            else:
                line += " " + wd
        c.drawString(x+6.5*mm, yy, line.strip())
        y = yy - 5.6*mm
    return y


def dimline(x1, y1, x2, y2, txt, off=0, vert=False):
    c.setStrokeColor(RED); c.setLineWidth(0.5)
    c.line(x1, y1, x2, y2)
    for (px, py) in ((x1, y1), (x2, y2)):
        if vert: c.line(px-1.4*mm, py, px+1.4*mm, py)
        else: c.line(px, py-1.4*mm, px, py+1.4*mm)
    c.setFillColor(RED); c.setFont("DVS-B", 6.4)
    if vert:
        c.saveState(); c.translate(x1-1.6*mm+off, (y1+y2)/2); c.rotate(90); c.drawCentredString(0, 0, txt); c.restoreState()
    else:
        c.drawCentredString((x1+x2)/2, y1+1.8*mm+off, txt)


def hole(x, y, r=1.7, col=RED, cross=True):
    c.setStrokeColor(col); c.setLineWidth(0.9); c.setFillColor(colors.white)
    c.circle(x, y, r*mm, stroke=1, fill=1)
    if cross:
        c.line(x-r*mm*1.4, y, x+r*mm*1.4, y); c.line(x, y-r*mm*1.4, x, y+r*mm*1.4)


# ============ STRONA 1: NARZĘDZIA + ZŁĄCZE KONFIRMATOWE ============
header("1. ZANIM ZACZNIESZ — narzędzia i JEDNO złącze, które musisz zrozumieć",
       "cała kuchnia trzyma się na konfirmatach 7×50 — naucz się tego jednego złącza, reszta to powtarzanie")

steps(13*mm, PH-28*mm, [
    "wkrętarka + zwykła wiertarka",
    "wiertło do konfirmatów (tzw. stopniowe — wierci 4,5 i 7 na raz; kup 2 szt, ~15 zł/szt)",
    "bit do konfirmatów (gniazdo Z2 płaskie szerokie lub imbus 4 — sprawdź łeb kupionych)",
    "wiertło puszkowe 35 mm (tylko jeśli NIE zamówisz otworów pod zawiasy w CNC)",
    "miara zwijana + kątownik stolarski + ołówek + szydło (do punktowania)",
    "poziomica min. 60 cm (masz — leżała na wylewce!)",
    "2 ściski stolarskie (sprężynowe wystarczą)",
    "taśma malarska (ogranicznik głębokości na wiertle) + koc/karton na podłogę",
], 88*mm, title="NARZĘDZIA (całość ~150–250 zł):", num=False)

# przekrój złącza: bok (pion) + dno (poziom)
X, Y = 118*mm, 60*mm
box = lambda x, y, w, h, f=FILL: (c.setStrokeColor(INK), c.setLineWidth(1), c.setFillColor(f), c.rect(x, y, w, h, 1, 1))
box(X, Y, 9*mm, 62*mm)                                  # bok (18 mm w skali)
box(X+9*mm, Y+6*mm, 52*mm, 9*mm)                        # dno wchodzące w bok
c.setFillColor(INK); c.setFont("DVS-B", 7.6)
c.drawString(X-1*mm, Y+64*mm, "BOK (przekrój)"); c.drawString(X+30*mm, Y+17*mm, "DNO (przekrój)")
# konfirmat
c.setStrokeColor(RED); c.setLineWidth(2.2)
c.line(X-6*mm, Y+10.5*mm, X+34*mm, Y+10.5*mm)
c.setFillColor(RED); c.setFont("DVS-B", 7.0)
c.drawString(X-6*mm, Y+13*mm, "KONFIRMAT 7×50")
dimline(X+70*mm, Y+6*mm, X+70*mm, Y+15*mm, "18", vert=True)
dimline(X+76*mm, Y+6*mm, X+76*mm, Y+10.5*mm, "9", vert=True)
c.setFillColor(INK); c.setFont("DVS", 6.6)
c.drawString(X+82*mm, Y+9*mm, "← oś otworu ZAWSZE w połowie grubości płyty: 9 mm od krawędzi")

steps(118*mm, Y-8*mm, [
    "Przyłóż dno do boku DOKŁADNIE tak, jak ma być w gotowej szafce (krawędzie przednie równo!). Ściśnij ściskami.",
    "Nawierć wiertłem stopniowym PRZEZ bok w czoło dna — na wylot przez bok (4,5) i ~35 mm w głąb czoła (7). Wiertło stopniowe robi to jednym ruchem.",
    "Wkręć konfirmat wkrętarką na wolnych obrotach; ostatnie pół obrotu ręcznie. Łeb ma się schować równo z płytą — NIE dokręcaj na siłę (pęknie płyta).",
    "Bez nawiercenia konfirmat ROZSADZI płytę — nigdy „na pałę\".",
], 158*mm, title="ZŁĄCZE KROK PO KROKU (ćwicz raz na ścince):")
c.showPage()

# ============ STRONA 2: SZABLON WIERCENIA BOKU + MONTAŻ DOLNEJ ============
header("2. KORPUS DOLNY — szablon wiercenia BOKU (każda dolna szafka tak samo)",
       "bok 720×560 (ramię RL: 720×460 — trzeci otwór dna na 410) · wymiary od krawędzi PRZEDNIEJ (lewa na rysunku) i DOLNEJ")

# bok w skali: 560 szer × 720 wys -> skala 0.16 mm/mm
sc = 0.155*mm
X, Y = 24*mm, 30*mm
W, H = 560*sc, 720*sc
c.setStrokeColor(INK); c.setLineWidth(1.2); c.setFillColor(FILL); c.rect(X, Y, W, H, 1, 1)
c.setFillColor(INK); c.setFont("DVS-B", 8); c.drawCentredString(X+W/2, Y+H+8*mm, "BOK — widok od WEWNĄTRZ szafki")
c.setFont("DVS-B", 6.6); c.setFillColor(BLU)
c.saveState(); c.translate(X-3*mm, Y+H/2); c.rotate(90); c.drawCentredString(0, 0, "KRAWĘDŹ PRZEDNIA (z obrzeżem)"); c.restoreState()
c.setFillColor(GREY); c.drawCentredString(X+W/2, Y-4*mm, "KRAWĘDŹ DOLNA")
# otwory dna: y = 9 od dołu, x = 50/280/510 od przodu
for dx in (50, 280, 510):
    hole(X+dx*sc, Y+9*sc)
dimline(X, Y-8*mm, X+50*sc, Y-8*mm, "50")
dimline(X, Y-13*mm, X+280*sc, Y-13*mm, "280")
dimline(X, Y-18*mm, X+510*sc, Y-18*mm, "510")
dimline(X+W+5*mm, Y, X+W+5*mm, Y+9*sc, "9", vert=True)
c.setFillColor(RED); c.setFont("DVS", 6.2); c.drawString(X+W+9*mm, Y+1*mm, "← rząd DNA (3 otwory)")
# trawersy: y=711 od dołu (9 od góry), x=50 i 510
for dx in (50, 510):
    hole(X+dx*sc, Y+711*sc)
dimline(X+W+5*mm, Y+711*sc, X+W+5*mm, Y+H, "9", vert=True)
c.setFillColor(RED); c.drawString(X+W+9*mm, Y+H-4*mm, "← trawersy (2 otwory: 50 od przodu i 50 od tyłu)")
# prowadniki zawiasów: x=37, y=102 od góry i 102 od dołu
for dy in (102, 618):
    hole(X+37*sc, Y+dy*sc, col=BLU)
dimline(X, Y+H+3*mm, X+37*sc, Y+H+3*mm, "37")
dimline(X-8*mm, Y+618*sc, X-8*mm, Y+H, "102", vert=True)
c.setFillColor(BLU); c.drawString(X+37*sc+3*mm, Y+610*sc, "prowadniki zawiasów (tylko szafki z drzwiami):")
c.drawString(X+37*sc+3*mm, Y+585*sc, "oś 37 od przodu · 102 od góry i 102 od dołu")

steps(128*mm, PH-28*mm, [
    "Połóż bok wewnętrzną stroną do góry. USTAL, który to lewy, a który prawy (obrzeże przednie!) — podpisz ołówkiem od zewnątrz.",
    "Odmierz i napunktuj szydłem otwory wg rysunku: rząd dna (9 od dołu; 50/280/510 od przodu), trawersy (9 od góry; 50 od przodu i 50 od tyłu).",
    "Szafki z drzwiami: zaznacz też osie prowadników zawiasów (37 od przodu, 102 od góry/dołu) — wkręcisz je PRZED skręceniem korpusu, na leżąco jest 10× łatwiej.",
    "Wywierć rzędy dna i trawersów NA WYLOT wiertłem stopniowym (podłóż ścinkę pod spód — nie wyrwie płyty). Prowadniki zawiasów: tylko wkręty 4×16, bez wiercenia na wylot!",
    "Skręć: bok L + dno (3 konfirmaty) → bok P + dno → trawers przedni na płask (lico z górą, 1 konfirmat/stronę) → trawers tylny na płask przy tylnej krawędzi.",
    "Zmierz obie PRZEKĄTNE (muszą być równe ±1 mm) — skoryguj dociskiem ręką.",
    "Połóż korpus na twarz (przodem do podłogi), przyłóż plecy HDF RÓWNO z krawędziami: wkręt w narożnik, wyrównaj drugi narożnik, wkręt — i dalej co ~150 mm dookoła. Plecy blokują kąt prosty na zawsze.",
    "Postaw, przykręć 4 nóżki 150 (płytki ~50 od krawędzi, wkręty 4×16), klipsy cokołu na przednie nóżki.",
], 150*mm, title="MONTAŻ (30–40 min/szafka na początku):")
c.showPage()

# ============ STRONA 3: WARIANTY ============
header("3. WARIANTY: DA1 szuflady · DA2 piekarnik · DB1 zlew · DC1 narożna · górne GA/GC",
       "górne: boki 998×320, wieniec górny i dolny PEŁNY (zamiast trawersów) — rzędy otworów 9 od góry I 9 od dołu, x = 50/160/270")

steps(13*mm, PH-28*mm, [
    "DA1 (3 szuflady): NIE wkręcaj prowadników zawiasów. Prowadnice szuflad przykręć na leżących bokach PRZED skręceniem: przednia krawędź prowadnicy równo z przednią krawędzią boku, wysokości OSI od dolnej krawędzi boku: 30 / 266 / 502 mm [~ dla frontów 236 — zweryfikuj z instrukcją kupionego systemu, każdy system ma szablon]. Obie strony IDENTYCZNIE — różnica 1 mm = krzywa szuflada.",
    "DA2 (piekarnik): zamiast górnych trawersów — trawers NOŚNY na płask, jego GÓRNA płaszczyzna 600 mm od górnej krawędzi boku (= nisza 600; sprawdź kartę piekarnika, bywa 590). Otwory przez bok: 9 mm poniżej tej linii, 50 i 280 od przodu (2 konfirmaty/stronę). W plecach otwór 60 mm na kabel (otwornica), róg dolny.",
    "DB1 (zlew): BEZ pleców i bez wiercenia rzędów tylnych. Zamiast pleców dwie listwy 100 na sztorc (góra-tył i dół-tył): otwory 9 od tylnej krawędzi, 30 i 80 od góry/dołu. Wycięcia na syfon i podejścia zrobisz na miejscu otwornicą — każde cięcie smarujesz silikonem.",
    "DC1 (narożna ślepa): korpus 900 jak bazowy (rzędy jak na str. 2, gł. 560). Po skręceniu przykręć od środka blendę ślepą 430 do boku od strony martwego pola (wkręty 4×30 przez bok korpusu w blendę, 3 szt). Zawiasy 155° montujesz jak zwykłe — puszka 35 tak samo.",
    "GÓRNE (GA1, GA2, GC1, GC2): jak dolna, ale zamiast trawersów PEŁNY wieniec u góry i u dołu — więc na boku wiercisz DWA pełne rzędy: 9 od dołu i 9 od góry, x = 50/160/270 (gł. 320). Zawieszki regulowane przykręć w górnych narożnikach od wewnątrz PRZED plecami; w plecach wytnij okienka wg instrukcji zawieszek.",
    "Półki górnych: otwory pod podpórki 5 mm — dwa piony na bok: 37 i 283 od przodu, wysokości co 32 mm w środkowej strefie (albo zamów szereg w CNC — grosze).",
    "GA3 (okap): korpus jak górna, ale bez wieńca dolnego (okap teleskopowy wchodzi od dołu) — konstrukcję dopasuj do karty okapu PO zakupie; front uchylny na podnośniku (montaż wg instrukcji podnośnika, 2 wkręty/strona).",
    "C2 słupek: dwa rzędy jak dolna (dno 9 od dołu) + wieniec górny 9 od góry + PÓŁKA STAŁA w połowie (rząd na 1190 od dołu: 50/280/510) — usztywnia 2378 wysokości. Skręcaj na podłodze, plecy przed postawieniem. C4 nadstawka: jak mała górna (rzędy 9 od góry i od dołu, x=50/280/510 przy gł. 580).",
], 268*mm, title="RÓŻNICE WZGLĘDEM KORPUSU BAZOWEGO (str. 2):")
c.showPage()

# ============ STRONA 4: FRONT + ZAWIAS ============
header("4. FRONT — wiercenie puszki 35 i zawieszenie (wymiary na rysunku)",
       "front dolny 716: 2 zawiasy · front górny 996: 3 zawiasy · głębokość puszki 12,5 mm — taśma na wiertle!")

sc = 0.155*mm
X, Y = 30*mm, 30*mm
W, H = 446*sc, 716*sc
c.setStrokeColor(INK); c.setLineWidth(1.2); c.setFillColor(FILL); c.rect(X, Y, W, H, 1, 1)
c.setFillColor(INK); c.setFont("DVS-B", 8); c.drawCentredString(X+W/2, Y+H+8*mm, "FRONT 446×716 — widok od TYŁU (strona zawiasów)")
for dy in (100, 616):
    hole(X+22.5*sc*2.2, Y+dy*sc, r=3.2)   # puszka 35 (przeskalowana wizualnie)
dimline(X, Y-6*mm, X+22.5*sc*2.2, Y-6*mm, "22,5 (środek puszki od krawędzi)")
dimline(X-8*mm, Y+616*sc, X-8*mm, Y+H, "100", vert=True)
dimline(X-14*mm, Y, X-14*mm, Y+100*sc, "100", vert=True)
c.setFillColor(RED); c.setFont("DVS", 6.4)
c.drawString(X+W+4*mm, Y+H-8*mm, "puszka Ø35, głębokość 12,5")
c.drawString(X+W+4*mm, Y+H-13*mm, "front górny 996: trzecia puszka")
c.drawString(X+W+4*mm, Y+H-18*mm, "w środku wysokości (498)")

steps(128*mm, PH-28*mm, [
    "Połóż front zewnętrzną stroną NA KOCU (rysy!). Zaznacz środki puszek: 22,5 mm od bocznej krawędzi (strona zawiasów!), 100 mm od górnej i 100 od dolnej krawędzi (front 996: dodatkowo w połowie).",
    "Owiń wiertło puszkowe 35 taśmą na 12,5 mm od czubka — wierć do taśmy, NIE dalej (front ma 18; przewiercisz = front do kosza). Wierć na wolnych obrotach, wyciągaj wióry.",
    "Włóż zawias w puszkę, dociśnij, ustaw ramię PROSTOPADLE do krawędzi frontu (kątownik), przykręć 2 wkręty puszki.",
    "Zawieś front: ramię zawiasu wciskasz na prowadnik w korpusie aż kliknie (Blum ClipTop — bez narzędzi). Zamknij i obejrzyj szczeliny.",
    "REGULACJA — na każdym zawiasie 3 śruby: PRZEDNIA = lewo/prawo (wyrównanie szczelin pionowych), TYLNA = docisk frontu do korpusu (skrzypienie/odstawanie), na PROWADNIKU = góra/dół. Kręć po ćwierć obrotu i patrz na szczelinę. Cel: równe 2–3 mm wszędzie.",
    "Fronty bezuchwytowe: jeśli profil gola — listwa alu wchodzi POD blat nad frontami dolnych (kupujesz z płytami); jeśli frez — zamawiasz przy CNC. Zdecyduj przed zamówieniem frontów.",
], 150*mm, title="KROK PO KROKU:")
c.showPage()

# ============ STRONA 5: PUŁAPKI + KOLEJNOŚĆ CAŁOŚCI ============
header("5. 10 PUŁAPEK POCZĄTKUJĄCEGO + kolejność montażu całej kuchni",
       "przeczytaj PRZED pierwszą szafką — każda z tych rzeczy kosztuje formatkę albo dzień pracy")

steps(13*mm, PH-28*mm, [
    "Boki L i P to LUSTRZANE odbicia — zawsze sprawdź, po której stronie ma być obrzeże przednie, ZANIM wywiercisz.",
    "Konfirmat bez nawiercenia stopniowym = pęknięta płyta. Zawsze nawiercaj.",
    "Wiercenie na wylot bez ścinki pod spodem = wyrwany tył otworu (widoczny!).",
    "Za głęboka puszka 35 = dziura na wylot we froncie. Taśma na 12,5 mm.",
    "Wkręty do blatu i frontów: MAX 4×30 (blat 38, front 18+puszka). Dłuższy = wystrzeli na wierzch.",
    "Plecy przykręcone krzywo = krzywa cała szafka. Najpierw narożnik, wyrównanie, potem reszta.",
    "Przekątne nie sprawdzone = drzwi nie zejdą się na środku podwójnej szafki.",
    "Prowadnice szuflad różnią się o 2 mm wysokości = szuflada chodzi po skosie i wypada z dociągu.",
    "Poziomowanie: zawsze od NAJWYŻSZEGO punktu podłogi (znajdź poziomicą wzdłuż ścian zanim zaczniesz).",
    "Nie przykręcaj blatów, dopóki WSZYSTKIE korpusy nie stoją poziomo i skręcone ze sobą.",
], 130*mm, title="PUŁAPKI:")

steps(150*mm, PH-28*mm, [
    "Skręć wszystkie korpusy „na sucho\" w salonie (str. 2–3). Ponumeruj je ołówkiem wg planu.",
    "Ściana C: DC1 → słupek C2 → bok zabudowy lodówki + blenda dystansowa → nadstawka C4.",
    "Ciąg B: DB1, wnęka zmywarki, DB0. Poziomowanie nóżkami, skręcanie korpusów ze sobą (2 ściski + 2 wkręty 4×30 przez boki, pod zawiasami — niewidoczne).",
    "Ciąg A: DA1, DA2. Ramię: RL1+RL2, kotwienie 4 kątownikami do posadzki.",
    "Górne: listwa montażowa (góra szafek = sufit 2478), zawieszenie, spięcie, blenda sufitowa.",
    "Blaty: na sucho → docinka do ścian → łączenia naroży (śruby + silikon) → wycięcia (56×49 indukcja [P], zlew wg szablonu z kartonu zlewu) → przykręcenie od spodu.",
    "AGD (elektryk do siły!), fronty + regulacja, cokoły z kratką, LED, panel ryflowany, listwy, silikon.",
], 132*mm, title="KOLEJNOŚĆ CAŁOŚCI:")
c.showPage()
c.save()
print("OK:", OUT)
