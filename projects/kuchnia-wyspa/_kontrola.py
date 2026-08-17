#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KONTROLA GEOMETRII — automatyczna weryfikacja projektu kuchni przed wysłaniem rysunku.

Sprawdza klasy błędów, które realnie wystąpiły w tym projekcie:
  1. sumy modułów ≠ długość ciągu (dziury / nadmiar)
  2. nakładające się bryły (narożnik policzony dwa razy)
  3. front bez miejsca na otwarcie (drzwi piekarnika za ramieniem)
  4. okap nie nad płytą
  5. górne na jednej ścianie w różnych płaszczyznach frontu
  6. przejścia poniżej progu decyzji inwestora
  7. dziura w licu ciągu (nieopisany fragment = biała przerwa na rzucie)
  8. okucie narożne szersze niż front, brak funkcji obowiązkowej
  9. zawiasy: strona niewybrana albo dwa sąsiednie skrzydła na tej samej krawędzi

Uruchomienie:  python3 _kontrola.py            → raport PASS/FAIL
               python3 _kontrola.py --regresja → dowód, że testy łapią dawne błędy

Układ współrzędnych (mm): origin = wewnętrzny narożnik ścian A/B.
x → na wschód (w stronę ściany C), y → na południe (w stronę korytarza).
"""
import math
import sys

# =============================================================================
# MODEL — jedno źródło prawdy
# =============================================================================
SCIANA_C_X = 2546          # lico wewnętrzne ściany C
LINIA_POLUDNIOWA = 1950    # koniec ciągu A / krawędź ramienia
SCIANKA = (1776, 1885, 2546, 1975)   # x0, y0, x1, y1

PROG_PRZEJSCIA = 600       # decyzja inwestora [P] — reguła nadrzędna
GORA_ZABUDOWY = 2469       # sufit 2481 [P] − fuga 12
# Zakres wysokości frontu wg typu modułu. BEZ TEGO kontrola zawiasów jest płaska
# i wypisuje kolizje między frontami, które nigdy nie spotykają się w pionie.
Z_DOMYSLNE = {
    "dolna":    (150, 871),
    "szuflady": (150, 871),
    "uchylny":  (150, 871),
    "AGD":      (150, 871),
    "górna":    (1480, GORA_ZABUDOWY),
}
FRONT_GR = 19


class Modul:
    def __init__(self, nazwa, x0, y0, x1, y1, lico=None, front=None, typ="dolna", okucie=None,
                 funkcje=(), zawias=None, z=None, segmenty=None):
        self.nazwa, self.typ, self.okucie = nazwa, typ, okucie
        self.zawias = zawias        # współrzędna osi obrotu wzdłuż ciągu, "para" = zawiasy
                                    # na obu końcach frontu, "wysuw" = brak skrzydła, None = NIE WYBRANO
        self.z = z or Z_DOMYSLNE.get(typ, (150, 871))   # zakres wysokości frontu
        self.segmenty = segmenty    # front dzielony: [(z0, z1, zawias), ...]
        self.funkcje = tuple(funkcje)
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.lico = lico            # 'E','W','N','S' — z której strony jest front
        self.front = front          # (od, do) wzdłuż ściany; None = brak frontu (ślepe)

    @property
    def rect(self):
        return (self.x0, self.y0, self.x1, self.y1)

    def plaszczyzna_frontu(self):
        return {"E": self.x1, "W": self.x0, "N": self.y0, "S": self.y1}[self.lico]


# --- ciąg A (indukcja), głębokość 560, lico na x=560 ---------------------------
CIAG_A = [
    Modul("DA1 narożna ślepa", 155, 0, 560, 850, lico="E", front=(610, 850), zawias=850),
    Modul("DA2 indukcja+piekarnik", 0, 850, 560, 1450, lico="E", front=(850, 1450), typ="uchylny"),   # piekarnik opada, szuflada się wysuwa
]
# --- ramię L (razem ze ślepym narożnikiem pod nim) -----------------------------
RAMIE = [
    Modul("RL1 ramię: drzwi 300 + szuflady 300", 0, 1450, 1176, 1950, lico="N",
          front=(576, 1176), funkcje=("sztućce", "przybory"), zawias=876),
]
# --- ciąg B (okno), głębokość 600, lico na y=600 -------------------------------
CIAG_B = [
    Modul("DB0 cargo 15", 600, 0, 750, 600, lico="S", front=(600, 750), typ="szuflady", funkcje=("przyprawy",)),
    Modul("DB1 zlew 80", 750, 0, 1550, 600, lico="S", front=(750, 1550),
          funkcje=("kosz segregacji",), zawias="para"),
    Modul("DB2 zmywarka 45", 1550, 0, 2000, 600, lico="S", front=(1550, 2000), typ="AGD"),
]
# --- ciąg C (lodówka), lico na x=2000 dla DC1 ----------------------------------
CIAG_C = [
    Modul("DC1 narożna ślepa", 2000, 0, 2546, 945, lico="W", front=(600, 945),
          okucie="szuflady wewnętrzne", zawias=945),
    Modul("C2 słupek", 1946, 945, 2546, 1225, lico="W", front=(945, 1225), typ="szuflady",
          z=(150, GORA_ZABUDOWY),
          # DÓŁ: wysuw obowiązkowo — drzwi zderzyłyby się ze skrzydłem DC1 (obie w z 155–871).
          # GÓRA: drzwi dozwolone, zawias 945 — powyżej 871 nie ma z czym kolidować.
          segmenty=[(150, 871, "wysuw"), (875, GORA_ZABUDOWY, 945)]),
    Modul("C3 lodówka", 1946, 1225, 2546, 1885, lico="W", front=(1225, 1885), typ="AGD",
          zawias=1225, z=(0, 2000)),   # wariant A [P] — zawiasy przełożone na stronę słupka
]
# --- górne na ścianie A (dół 1480, do sufitu) ----------------------------------
GORNE_A = [
    Modul("GA1 (na licu pilastra)", 155, 0, 400, 670, lico="E", front=(0, 670), typ="górna",
          zawias="para"),
    Modul("GA2 wąska 180", 0, 670, 400, 850, lico="E", front=(670, 850), typ="górna",
          zawias=850),   # 670 zajęte przez prawe skrzydło GA1
    Modul("GA3 okap", 0, 850, 400, 1450, lico="E", front=(850, 1450), typ="uchylny"),
    Modul("GA4", 0, 1450, 400, 1950, lico="E", front=(1450, 1950), typ="górna", zawias=1950),
]

# blendy zamykające lico tam, gdzie nie ma frontu (muszą domknąć każdy ciąg)
BLENDY = {
    "ciąg A": [(0, 610)],          # lico ślepej części DA1
    "ciąg B": [(155, 600), (2000, 2546)],   # zachód: kolizja z ciągiem A; wschód: narożnik przejęty przez DC1
    "ramię": [(0, 576)],           # ślepy narożnik pod ramieniem
    "ciąg C": [(0, 600)],          # lico DC1 zasłonięte korpusem ciągu B (zmywarka)
    "górne A": [],
}

PLYTA = (864, 1436)      # indukcja Bosch 572 wzdłuż ciągu A, wyśrodkowana w DA2
OKAP = "GA3 okap"

CIAGI = {
    "ciąg A": (CIAG_A, "y", 0, 1450),   # 1450→1950 należy do RL1
    "ramię": (RAMIE, "x", 0, 1176),
    "ciąg B": (CIAG_B, "x", 155, SCIANA_C_X),
    "ciąg C": (CIAG_C, "y", 0, 1885),
    "górne A": (GORNE_A, "y", 0, LINIA_POLUDNIOWA),
}

# =============================================================================
# KONTROLE
# =============================================================================
bledy, ostrzezenia = [], []


def blad(kod, txt):
    bledy.append(f"[{kod}] {txt}")


def ostrz(txt):
    ostrzezenia.append(f"[UWAGA] {txt}")


def zakres(m, os):
    return (m.y0, m.y1) if os == "y" else (m.x0, m.x1)


def k1_sumy():
    """Moduły muszą wypełnić ciąg bez dziur i bez nadmiaru."""
    for nazwa, (mods, os, od, do) in CIAGI.items():
        if nazwa in ("ciąg B", "ciąg C"):
            continue   # ciągi z martwym polem liczone osobno w k7
        odc = sorted(zakres(m, os) for m in mods)
        kursor = od
        for a, b in odc:
            if a > kursor:
                pass   # dziura = miejsce na blendę, sprawdza k7
            kursor = max(kursor, b)
        if kursor != do:
            blad("K1", f"{nazwa}: moduły kończą się na {kursor}, a ciąg ma {do} "
                       f"(różnica {do - kursor} mm)")


def k2_nakladki():
    """Żadne dwie bryły nie mogą zajmować tego samego miejsca w rzucie."""
    wszystkie = [m for grupa in (CIAG_A, RAMIE, CIAG_B, CIAG_C) for m in grupa]
    for i, a in enumerate(wszystkie):
        for b in wszystkie[i + 1:]:
            dx = min(a.x1, b.x1) - max(a.x0, b.x0)
            dy = min(a.y1, b.y1) - max(a.y0, b.y0)
            if dx > 1 and dy > 1:
                blad("K2", f"NAKŁADKA {a.nazwa} × {b.nazwa}: "
                           f"{dx}×{dy} mm liczone dwa razy")


def _dystans_do_rect(px, py, r):
    dx = max(r[0] - px, 0, px - r[2])
    dy = max(r[1] - py, 0, py - r[3])
    return math.hypot(dx, dy)


def _cwiartka(r, lico, plane, zawias, koniec):
    """Skrzydło zatacza ćwiartkę: na zewnątrz lica ORAZ po stronie, w którą sięga skrzydło."""
    x0, y0, x1, y1 = r
    if lico == "E":
        x0 = max(x0, plane)
    elif lico == "W":
        x1 = min(x1, plane)
    elif lico == "S":
        y0 = max(y0, plane)
    else:
        y1 = min(y1, plane)
    if lico in ("E", "W"):          # skrzydło mierzone wzdłuż y
        if koniec > zawias:
            y0 = max(y0, zawias)
        else:
            y1 = min(y1, zawias)
    else:                            # wzdłuż x
        if koniec > zawias:
            x0 = max(x0, zawias)
        else:
            x1 = min(x1, zawias)
    return None if (x1 - x0 <= 1 or y1 - y0 <= 1) else (x0, y0, x1, y1)


def k3_otwieranie():
    """Front musi być (a) niezasłonięty i (b) mieć zawias, przy którym drzwi się otworzą."""
    wszystkie = [m for grupa in (CIAG_A, RAMIE, CIAG_B, CIAG_C) for m in grupa]

    # (a) pas tuż przed licem musi być wolny — dotyczy KAŻDEGO frontu,
    #     także szuflad i drzwi uchylnych piekarnika
    PAS = 50
    for m in wszystkie:
        if not m.front:
            continue
        lico = m.plaszczyzna_frontu()
        if m.lico == "E":
            pas = (lico, m.front[0], lico + PAS, m.front[1])
        elif m.lico == "W":
            pas = (lico - PAS, m.front[0], lico, m.front[1])
        elif m.lico == "S":
            pas = (m.front[0], lico, m.front[1], lico + PAS)
        else:
            pas = (m.front[0], lico - PAS, m.front[1], lico)
        for o in wszystkie:
            if o is m:
                continue
            dx = min(pas[2], o.x1) - max(pas[0], o.x0)
            dy = min(pas[3], o.y1) - max(pas[1], o.y0)
            if dx > 1 and dy > 1:
                blad("K3", f"{m.nazwa}: front zasłonięty przez {o.nazwa} "
                           f"na {max(dx, dy)} mm — nie da się go otworzyć")

    # (b) wychył skrzydła
    for m in wszystkie:
        if not m.front or m.typ in ("AGD", "szuflady", "uchylny"):
            continue
        W = m.front[1] - m.front[0]
        if W > 700:
            continue   # szerokie fronty = drzwi dzielone/szuflady
        lico = m.plaszczyzna_frontu()
        if m.lico == "E":
            zawiasy = [(lico, m.front[0]), (lico, m.front[1])]
        elif m.lico == "W":
            zawiasy = [(lico, m.front[0]), (lico, m.front[1])]
        elif m.lico == "N":
            zawiasy = [(m.front[0], lico), (m.front[1], lico)]
        else:
            zawiasy = [(m.front[0], lico), (m.front[1], lico)]
        ok, maks = False, []
        for (hx, hy), kon in zip(zawiasy, (m.front[1], m.front[0])):
            os_zawias = hy if m.lico in ("E", "W") else hx
            przeszkody = [_cwiartka(o.rect, m.lico, lico, os_zawias, kon)
                          for o in wszystkie if o is not m]
            d = min((_dystans_do_rect(hx, hy, r) for r in przeszkody if r), default=9e9)
            maks.append(d)
            if d >= W:
                ok = True
        if not ok:
            blad("K3", f"{m.nazwa}: front {W} mm nie ma jak się otworzyć "
                       f"(max przy zawiasach: {max(maks):.0f} mm)")
        elif min(maks) < W:
            ostrz(f"{m.nazwa}: zawias tylko po jednej stronie "
                  f"(druga daje {min(maks):.0f} < {W} mm)")


def k4_okap():
    """Okap musi obejmować całą płytę."""
    o = next((m for m in GORNE_A if m.nazwa == OKAP), None)
    if not o:
        return blad("K4", "brak modułu okapu")
    if not (o.front[0] <= PLYTA[0] and o.front[1] >= PLYTA[1]):
        blad("K4", f"okap {o.front} nie obejmuje płyty {PLYTA}")


def k5_lico_gornych():
    """Górne na jednej ścianie muszą mieć wspólną płaszczyznę frontu."""
    plaszczyzny = {m.nazwa: m.plaszczyzna_frontu() for m in GORNE_A}
    if len(set(plaszczyzny.values())) > 1:
        blad("K5", f"górne A w różnych płaszczyznach: {plaszczyzny}")


def k6_przejscia():
    """Przejście ramię ↔ ścianka nie może zejść poniżej decyzji inwestora."""
    p = SCIANKA[0] - max(m.x1 for m in RAMIE)
    if p < PROG_PRZEJSCIA - 1:
        blad("K6", f"przejście {p} mm < próg {PROG_PRZEJSCIA} mm")


def k7_lico_ciagu():
    """Lico każdego ciągu musi być domknięte: front albo blenda. Inaczej dziura."""
    for nazwa, (mods, os, od, do) in CIAGI.items():
        odcinki = [m.front for m in mods if m.front] + BLENDY.get(nazwa, [])
        odcinki = sorted(odcinki)
        kursor, dziury = od, []
        for a, b in odcinki:
            if a > kursor + 1:
                dziury.append((kursor, a))
            kursor = max(kursor, b)
        if kursor < do - 1:
            dziury.append((kursor, do))
        if dziury:
            blad("K7", f"{nazwa}: lico niedomknięte na odcinkach {dziury} "
                       f"— na rysunku wyjdzie biała przerwa")


MIN_OTWARCIA = {"cargo narożne": 450, "karuzela": 450, "szuflady wewnętrzne": 300}


def k8_okucia():
    """Okucie narożne wymaga minimalnej szerokości otwarcia (katalogi Rejs/Kesseböhmer)."""
    for m in [x for g in (CIAG_A, RAMIE, CIAG_B, CIAG_C) for x in g]:
        if not m.okucie or not m.front:
            continue
        W = m.front[1] - m.front[0]
        wym = MIN_OTWARCIA.get(m.okucie, 0)
        if W < wym:
            blad("K8", f"{m.nazwa}: okucie \u201e{m.okucie}\u201d wymaga otwarcia >= {wym} mm, "
                       f"a front ma {W} mm")


FUNKCJE_OBOWIAZKOWE = {"sztućce": 250, "kosz segregacji": 450, "przyprawy": 100}


def k9_funkcje():
    """Przebudowa modułu nie może po cichu skasować funkcji kuchni (np. szuflady na sztućce)."""
    dostepne = {}
    for m in [x for g in (CIAG_A, RAMIE, CIAG_B, CIAG_C) for x in g]:
        for f in m.funkcje:
            dostepne.setdefault(f, []).append(m)
    for f, minim in FUNKCJE_OBOWIAZKOWE.items():
        kand = dostepne.get(f, [])
        if not kand:
            blad("K9", f"brak miejsca na \u201e{f}\u201d — żaden moduł nie ma tej funkcji")
            continue
        naj = max((m.front[1] - m.front[0]) for m in kand if m.front)
        if naj < minim:
            blad("K9", f"\u201e{f}\u201d: najszerszy front {naj} mm, potrzeba >= {minim} mm")



# Moduły, które NIE mają skrzydła na zawiasach bocznych (nie wymagają decyzji):
BEZ_ZAWIASOW = ("szuflady", "AGD", "uchylny")


def _osie(m, os):
    """Zbiór współrzędnych osi obrotu wzdłuż ciągu dla jednego segmentu frontu."""
    if os is None or os == "wysuw":
        return set()
    if os == "para":
        return {m.front[0], m.front[1]}
    return {os}


def _segmenty(m):
    """[(z0, z1, zawias)] — front dzielony albo jeden segment na całą wysokość."""
    return m.segmenty if m.segmenty else [(m.z[0], m.z[1], m.zawias)]


def k10_zawiasy():
    """Strona zawiasu musi być WYBRANA (Korner wierci puszki 35 wg strony)
    i dwa sąsiadujące skrzydła nie mogą wisieć na tej samej krawędzi —
    otwarte jednocześnie leżą w tej samej płaszczyźnie i zderzają się."""
    wszystkie = [x for g in (CIAG_A, RAMIE, CIAG_B, CIAG_C, GORNE_A) for x in g]

    for m in wszystkie:
        if m.front and m.typ not in BEZ_ZAWIASOW and m.zawias is None and not m.segmenty:
            ostrz(f"{m.nazwa}: NIE WYBRANO strony zawiasu — bez tego nie da się "
                  f"zamówić nawiertów CNC (puszki 35)")

    for nazwa, (mods, os, od, do) in CIAGI.items():
        z_frontem = sorted([m for m in mods if m.front], key=lambda m: m.front[0])
        for a, b in zip(z_frontem, z_frontem[1:]):
            if abs(a.front[1] - b.front[0]) > 1:
                continue                      # nie sąsiadują
            krawedz = a.front[1]
            for za0, za1, oa in _segmenty(a):
                for zb0, zb1, ob in _segmenty(b):
                    if krawedz not in _osie(a, oa) or krawedz not in _osie(b, ob):
                        continue
                    wspolne = min(za1, zb1) - max(za0, zb0)
                    if wspolne <= 0:
                        continue              # mijają się w pionie — nie ma kolizji
                    blad("K10", f"{nazwa}: {a.nazwa} i {b.nazwa} mają zawiasy na tej samej "
                                f"krawędzi {krawedz} i zachodzą na siebie w pionie o "
                                f"{wspolne} mm — otwarte skrzydła zderzą się")


KONTROLE = [k1_sumy, k2_nakladki, k3_otwieranie, k4_okap,
            k5_lico_gornych, k6_przejscia, k7_lico_ciagu, k8_okucia, k9_funkcje,
            k10_zawiasy]


def uruchom(naglowek="KONTROLA GEOMETRII — kuchnia U + ramię L"):
    global bledy, ostrzezenia
    bledy, ostrzezenia = [], []
    for k in KONTROLE:
        k()
    print("=" * 78)
    print(naglowek)
    print("=" * 78)
    for o in ostrzezenia:
        print(" ", o)
    if bledy:
        for b in bledy:
            print(" ", b)
        print(f"\n  WYNIK: FAIL — {len(bledy)} błąd(ów). NIE wysyłaj rysunku.")
    else:
        print(f"  WYNIK: PASS — {len(KONTROLE)} kontroli, 0 błędów, "
              f"{len(ostrzezenia)} uwag(i).")
    return not bledy


# =============================================================================
# REGRESJA — dowód, że kontrole łapią błędy, które realnie popełniłem
# =============================================================================
def regresja():
    print("\nREGRESJA — czy kontrole złapałyby błędy z historii projektu?\n")
    wyniki = []

    # (1) v3.6: okap wpisany zaraz za GA1 → wypadał nad szuflady, nie nad płytę
    org = [(m.nazwa, m.front) for m in GORNE_A]
    for m in GORNE_A:
        if m.nazwa == OKAP:
            m.front = (670, 1270)
    bledy.clear(); k4_okap()
    wyniki.append(("v3.6  okap nie nad płytą", bool(bledy), "K4"))
    for m, (n, f) in zip(GORNE_A, org):
        m.front = f

    # (2) v3.2: RL1+RL2 = 118 cm — narożnik liczony dwa razy z ciągiem A
    RAMIE.append(Modul("RL2 (stary podział)", 0, 1450, 650, 1950, lico="N", front=(0, 650)))
    bledy.clear(); k2_nakladki()
    wyniki.append(("v3.2  ramię liczone dwa razy", bool(bledy), "K2"))
    RAMIE.pop()

    # (3) v3.7a: piekarnik 1120–1720, front zasłonięty przez ramię
    stare = (CIAG_A[1].y0, CIAG_A[1].y1, CIAG_A[1].front)
    CIAG_A[1].y0, CIAG_A[1].y1, CIAG_A[1].front = 1120, 1720, (1120, 1720)
    bledy.clear(); k3_otwieranie()
    wyniki.append(("v3.7a piekarnik bez miejsca na drzwi", bool(bledy), "K3"))
    CIAG_A[1].y0, CIAG_A[1].y1, CIAG_A[1].front = stare

    # (4) v3.6: GA1 305 zamiast 245 → uskok w licu górnych
    stary_x1 = GORNE_A[0].x1
    GORNE_A[0].x1 = 155 + 305
    bledy.clear(); k5_lico_gornych()
    wyniki.append(("v3.6  GA1 305 — uskok frontów górnych", bool(bledy), "K5"))
    GORNE_A[0].x1 = stary_x1

    # (5) v3.10: brak blendy na licu ślepej części DA1 → biała przerwa na rzucie
    stare_bl = BLENDY["ciąg A"]
    BLENDY["ciąg A"] = []
    bledy.clear(); k7_lico_ciagu()
    wyniki.append(("v3.10 niedomknięte lico DA1", bool(bledy), "K7"))
    BLENDY["ciąg A"] = stare_bl

    # (6) 2026-08-13: GA2 z zawiasem na krawędzi 670 — zderza się z prawym
    #     skrzydłem GA1 (GA1 ma zawiasy "para", czyli także na 670)
    stary = GORNE_A[1].zawias
    GORNE_A[1].zawias = 670
    bledy.clear(); k10_zawiasy()
    wyniki.append(("v3.13 GA2 zawias na wspólnej krawędzi z GA1", bool(bledy), "K10"))
    GORNE_A[1].zawias = stary

    # (7) 2026-08-13: gdyby C2 dostał DRZWI zamiast cargo — nie ma dla nich strony:
    #     945 zderza się z DC1, 1225 zderza się z drzwiami lodówki (wariant A)
    c2 = CIAG_C[1]
    st_seg = c2.segmenty
    # DÓŁ C2 na drzwiach: obie krawędzie zajęte w tym samym paśmie wysokości
    obie = []
    for proba in (945, 1225):
        c2.segmenty = [(150, 871, proba), (875, GORA_ZABUDOWY, 945)]
        bledy.clear(); k10_zawiasy()
        obie.append(bool(bledy))
    c2.segmenty = st_seg
    wyniki.append(("v3.13 dolny front C2 na drzwiach — obie krawędzie zajęte", all(obie), "K10"))

    # (8) 2026-08-13: kontrola płaska (bez osi Z) wypisywała kolizję GÓRNEGO frontu C2
    #     z drzwiami DC1, choć DC1 kończy się na 871 — fronty nigdy się nie spotykają.
    c2.segmenty = [(150, 871, "wysuw"), (875, GORA_ZABUDOWY, 945)]
    bledy.clear(); k10_zawiasy()
    fałszywy = bool(bledy)
    c2.segmenty = st_seg
    wyniki.append(("v3.13c górny front C2 NIE jest kolizją (oś Z)", not fałszywy, "K10"))

    zlapane = sum(1 for _, z, _ in wyniki if z)
    for opis, z, kod in wyniki:
        print(f"  {'ZŁAPANY ' if z else 'PRZEOCZONY'} {kod:4} {opis}")
    print(f"\n  {zlapane}/{len(wyniki)} historycznych błędów wykrytych automatycznie.")
    print("  (Błąd odczytu zdjęcia — „gzyms" " vs pilaster — nie jest wykrywalny skryptem;")
    print("   dla niego obowiązuje reguła z protokołu: nie projektuj na interpretacji")
    print("   zdjęcia bez dwóch liczb potwierdzonych przez inwestora.)")
    return zlapane == len(wyniki)


if __name__ == "__main__":
    ok = uruchom()
    if "--regresja" in sys.argv:
        ok = regresja() and ok
    sys.exit(0 if ok else 1)
