#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JEDNO ŹRÓDŁO GEOMETRII 3D — importowane przez _widok3d.py i _widok_audyt.py.

Powstało po audycie (werdykt, krok 1: zejść do jednego źródła prawdy).
Wcześniej każdy rysunek miał własną kopię wymiarów — dokładnie ta praktyka
wyprodukowała rozjazd między PLAN.md, _formatki.py, _schemat.py i _kontrola.py.

UWAGA: wymiary pionowe pochodzą z sufitu 2478 zmierzonego PRZED posadzką
docelową (P0-05). Do czasu pomiaru wszystkie wysokości mają status [?].
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

# --- geometria pomieszczenia (mm) ---
CX, CY, H = 2546, 1950, 2478
BLAT_H, COKOL_H, KORPUS_Z, GORNE_Z0 = 910, 150, 870, 1480

# --- korekty WYMUSZONE arytmetyką (nie wymagają decyzji ani pomiaru) ---
# P0-03: 2378 + nóżki 150 = 2528 > sufit 2478. Korpus musi być 2478 − 150 = 2328.
C2_KORPUS_WYS = H - COKOL_H          # 2328 zamiast 2378
KOREKTY_WYMUSZONE = [
    ("P0-03", "słupek C2", "korpus 2378 → 2328 (2478 − 150 nóżek); inaczej przebija sufit o 50 mm"),
    ("P0-04", "bok lodówki", "przekątna 2569,6 > 2478 — bok DZIELONY na dwie formatki (1240 + 1238)"),
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
        ("C2", "wieza", 1946, 945, COKOL_H, 2546, 1225, COKOL_H + C2_KORPUS_WYS, ORZECH),
        ("C3", "wieza", 1946, 1225, 0, 2546, 1885, 1900, ANTRACYT),
        ("C4", "wieza", 1946, 1225, 1900, 2546, 1885, H, ANTRACYT),
        ("scianka", "wieza", 1776, 1885, 0, 2546, 1975, 300, mix(ANTRACYT, 0.06)),

        ("cokol_R", "R", 0, 1450, 0, 1176, 1950, COKOL_H, COKOL),
        ("RL1", "R", 0, 1450, COKOL_H, 1176, 1950, KORPUS_Z, BEZ),
        ("ryfle", "R", 0, 1940, COKOL_H, 1176, 1950, KORPUS_Z, RYFLE),
        ("blat_R", "R", 0, 1450, KORPUS_Z, 1176, 1950, BLAT_H, BLAT),

        ("GA1", "GA", 155, 0, GORNE_Z0, 400, 670, H, ORZECH),
        ("GA2", "GA", 0, 670, GORNE_Z0, 400, 850, H, ORZECH),
        ("GA3", "GA", 0, 850, GORNE_Z0, 400, 1450, H, ORZECH),
        ("GA4", "GA", 0, 1450, GORNE_Z0, 400, 1950, H, ORZECH),
        ("GC", "GC", 2146, 0, GORNE_Z0, 2546, 945, H, ORZECH),
    ]


# --- mapa usterek P0 z audytu (werdykt 00-werdykt.md) ---
USTERKI = {
    "DA1": ["P0-01", "P1 garnek Ø240 > światło 230"],
    "RL1": ["P0-02"],
    "C2":  ["P0-03"],
    "C3":  ["P0-04", "P0-13"],
    "C4":  ["P0-13"],
    "DA2": ["P0-06"],
    "DC1": ["P0-07", "P0-08"],
    "GA3": ["P0-12"],
    "GA1": ["P0-05"], "GA2": ["P0-05"], "GA4": ["P0-05"], "GC": ["P0-05"],
}

OPISY_USTEREK = [
    ("P0-01", "DA1 / DC1 / RL1", "rozpiska wystawia sztywny front 446 — zamiast 240 / 345 / dzielonego 600"),
    ("P0-02", "RL1 ramię", "brak 3 frontów szuflad i 6 den — szuflady na sztućce istnieją tylko w planie"),
    ("P0-03", "C2 słupek", "2378 + 150 nóżek = 2528 > sufit 2478 — KOREKTA WYMUSZONA: korpus 2328"),
    ("P0-04", "bok lodówki", "przekątna 2569,6 > 2478 — nie da się wnieść; KOREKTA: bok dzielony"),
    ("P0-05", "wszystkie górne", "wysokości liczone z sufitu mierzonego przed posadzką; fuga = 0"),
    ("P0-06", "DA2", "płyta + piekarnik + szuflada nie mieszczą się w pionie (zostaje 68–86 mm)"),
    ("P0-07", "ciąg C", "łańcuch nie domyka się: deficyt 2–72 mm (blenda dystansowa bez miejsca)"),
    ("P0-08", "DC1", "cztery różne wymiary w czterech plikach"),
    ("P0-12", "GA3 okap", "pełne dno (brak wlotu), brak wylotu recyrkulacji, front 400 na korpusie 998"),
    ("P0-13", "C3 / C4", "cztery głębokości zabudowy lodówki; luz tylny < 50; nadstawka z pełnym dnem"),
]
