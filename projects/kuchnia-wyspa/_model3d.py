#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JEDNO ŹRÓDŁO GEOMETRII 3D — importowane przez _widok3d.py i _widok_audyt.py.

Powstało po audycie (werdykt, krok 1: zejść do jednego źródła prawdy).
Wcześniej każdy rysunek miał własną kopię wymiarów — dokładnie ta praktyka
wyprodukowała rozjazd między PLAN.md, _formatki.py, _schemat.py i _kontrola.py.

AKTUALIZACJA v3.13 (2026-08-13): sufit zmierzony PO ułożeniu posadzki dalmierzem
(2481 / 2483 / 2485) → do zabudowy 2481 (najmniejszy), fuga przysufitowa 12,
GÓRA ZABUDOWY = 2469. To zamyka P0-05 i P0-03. Lodówka wolnostojąca 600×650×2000
stoi na podłodze — bez obudowy, więc P0-04 (bok o przekątnej 2569,6) odpada.
"""
from reportlab.lib import colors

# --- paleta (pkt 10 planu) ---
BEZ      = colors.HexColor("#d9cbb3")
ORZECH   = colors.HexColor("#6b4f35")
ANTRACYT = colors.HexColor("#3a3d40")
BLAT     = colors.HexColor("#e8e0d4")
COKOL    = colors.HexColor("#2a2a2a")
PODLOGA  = colors.HexColor("#d9c3a2")
SCIANA   = colors.HexColor("#e9e5dd")
RYFLE    = colors.HexColor("#4a3a2c")
SZKLO    = colors.HexColor("#eef3f6")
INOX     = colors.HexColor("#b8bcc0")   # lodówka wolnostojąca — nie jest w palecie mebli

# --- geometria pomieszczenia (mm) ---
CX, CY = 2546, 1950
H = 2481                             # [P] pomiar po posadzce: 2481/2483/2485 → najmniejszy
FUGA = 12                            # fuga przysufitowa, zamknięta blendą
GORA = H - FUGA                      # 2469 — jedna linia góry zabudowy
BLAT_H, COKOL_H, KORPUS_Z, GORNE_Z0 = 910, 150, 870, 1480

# --- lodówka wolnostojąca [P]: 600 szer. × 650 gł. × 2000 wys., stoi na podłodze ---
LOD_W, LOD_D, LOD_H = 600, 650, 2000
LOD_LUZ_GORA = 50                    # wymóg wentylacji

# --- korekty WYMUSZONE arytmetyką (nie wymagają decyzji ani pomiaru) ---
C2_KORPUS_WYS = GORA - COKOL_H       # 2319 = 2469 − 150
C4_WYS = GORA - (LOD_H + LOD_LUZ_GORA)   # 419 = 2469 − 2050
GORNE_WYS = GORA - GORNE_Z0          # 989 = 2469 − 1480
KOREKTY_WYMUSZONE = [
    ("P0-05", "sufit", "zmierzony po posadzce: 2481 (min z 2481/2483/2485); fuga 12 → góra zabudowy 2469"),
    ("P0-03", "słupek C2", "korpus 2378 → 2319 (2469 − 150 nóżek); inaczej przebijał sufit o 47 mm"),
    ("P0-04", "obudowa lodówki", "ODPADA — lodówka wolnostojąca 600×650×2000; nie ma boku 2569,6 do wnoszenia"),
    ("—", "górne A i C", "korpus 998 → 989; nadstawka C4 519 → 419 (lodówka 2000, nie 1900)"),
]


def mix(col, f):
    r, g, b = col.red, col.green, col.blue
    if f >= 0:
        return colors.Color(r + (1 - r) * f, g + (1 - g) * f, b + (1 - b) * f)
    return colors.Color(r * (1 + f), g * (1 + f), b * (1 + f))


def bryly():
    """(uid, grupa, x0, y0, z0, x1, y1, z1, kolor)"""
    return [
        ("pilaster", "pilaster", 0, 0, 0, 155, 670, H, mix(SCIANA, -0.14)),

        ("cokol_A", "A", 0, 0, 0, 560, 1450, COKOL_H, COKOL),
        ("DA1", "A", 155, 0, COKOL_H, 560, 850, KORPUS_Z, BEZ),
        ("DA2", "A", 0, 850, COKOL_H, 560, 1450, KORPUS_Z, BEZ),
        ("blat_A", "A", 0, 0, KORPUS_Z, 600, 1450, BLAT_H, BLAT),

        ("cokol_B", "B", 155, 0, 0, 2000, 600, COKOL_H, COKOL),
        ("DB", "B", 155, 0, COKOL_H, 2000, 600, KORPUS_Z, BEZ),
        ("DB2", "B", 1550, 585, COKOL_H, 2000, 600, KORPUS_Z, mix(BEZ, -0.07)),
        ("blat_B", "B", 155, 0, KORPUS_Z, 2546, 635, BLAT_H, BLAT),

        ("cokol_C", "C", 2000, 0, 0, 2546, 945, COKOL_H, COKOL),
        ("DC1", "C", 2000, 0, COKOL_H, 2546, 945, KORPUS_Z, BEZ),
        ("C2", "wieza", 1966, 945, COKOL_H, 2546, 1225, COKOL_H + C2_KORPUS_WYS, ORZECH),
        # C3 = LODÓWKA WOLNOSTOJĄCA (nie mebel): 600×650×2000, dosunięta do słupka,
        # cały luz boczny (60) po stronie ścianki — patrz wariant A zawiasów w PLAN pkt 9.
        ("C3", "wieza", 2546 - LOD_D, 1225, 0, 2546, 1225 + LOD_W, LOD_H, INOX),
        # zawias po stronie słupka (y = 1225, lico x = 1896); kant ścianki (1776, 1885):
        # d = √(120² + 660²) = 670,8 > skrzydło 600  ->  zapas 70,8 mm  [wariant A]
        ("C4", "wieza", 1966, 1225, LOD_H + LOD_LUZ_GORA, 2546, 1885, GORA, ANTRACYT),
        ("scianka", "wieza", 1776, 1885, 0, 2546, 1975, 300, mix(ANTRACYT, 0.06)),

        ("cokol_R", "R", 0, 1450, 0, 1176, 1950, COKOL_H, COKOL),
        ("RL1", "R", 0, 1450, COKOL_H, 1176, 1950, KORPUS_Z, BEZ),
        ("ryfle", "R", 0, 1940, COKOL_H, 1176, 1950, KORPUS_Z, RYFLE),
        ("blat_R", "R", 0, 1450, KORPUS_Z, 1176, 1950, BLAT_H, BLAT),

        ("GA1", "GA", 155, 0, GORNE_Z0, 400, 670, GORA, ORZECH),
        ("GA2", "GA", 0, 670, GORNE_Z0, 400, 850, GORA, ORZECH),
        ("GA3", "GA", 0, 850, GORNE_Z0, 400, 1450, GORA, ORZECH),
        ("GA4", "GA", 0, 1450, GORNE_Z0, 400, 1950, GORA, ORZECH),
        ("GC", "GC", 2146, 0, GORNE_Z0, 2546, 945, GORA, ORZECH),
    ]


# --- mapa usterek P0 z audytu (werdykt 00-werdykt.md) ---
USTERKI = {
    "DA1": ["P0-01", "P1 garnek Ø240 > światło 230"],
    "RL1": ["P0-02"],
    "DA2": ["P0-06"],
    "DC1": ["P0-07", "P0-08"],
    "GA3": ["P0-12"],
    "C4":  ["P0-13"],
}

OPISY_USTEREK = [
    ("P0-01", "DA1 / DC1 / RL1", "rozpiska wystawia sztywny front 446 — zamiast 240 / 345 / dzielonego 600"),
    ("P0-02", "RL1 ramię", "brak 3 frontów szuflad i 6 den — szuflady na sztućce istnieją tylko w planie"),
    ("P0-06", "DA2", "płyta + piekarnik + szuflada nie mieszczą się w pionie (zostaje 68–86 mm)"),
    ("P0-07", "ciąg C", "łańcuch nie domyka się: deficyt 2–72 mm (blenda dystansowa JUŻ odpadła — przeliczyć)"),
    ("P0-08", "DC1", "cztery różne wymiary w czterech plikach"),
    ("P0-12", "GA3 okap", "pełne dno (brak wlotu), brak wylotu recyrkulacji, front 400 na korpusie 989"),
    ("P0-13", "C4 nadstawka", "lodówka wolnostojąca nie jest obudową — czym podeprzeć C4? pełne dno vs wentylacja"),
]
