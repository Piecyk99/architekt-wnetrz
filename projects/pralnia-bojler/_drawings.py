#!/usr/bin/env python3
"""Rysunki techniczne projektu oświetlenia — rzut, elewacja, schemat obwodów.

Generuje:
  TECH-01-rzut.pdf / .png            — rzut z gory pomieszczenia z oprawami,
                                       włącznikami, gniazdami, obwodami L1-L7
  TECH-02-elewacja.pdf / .png        — elewacja zabudowy 266x250 (front + wnętrze)
  TECH-03-schemat-obwodow.pdf / .png — schemat blokowy rozdzielnica -> Shelly -> oprawy
  TECH-ALL.pdf                        — wszystko razem (3 strony)

Uruchomienie:  python3 _drawings.py
"""

import pathlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle, Polygon, FancyBboxPatch
from matplotlib.backends.backend_pdf import PdfPages

OUT = pathlib.Path(__file__).parent

# kolor kodow obwodow (uzywane wszedzie konsekwentnie)
CIRCUITS = {
    "L1": ("#d97706", "Salon wnęka LED 3000K"),
    "L2": ("#dc2626", "Salon spoty 3000K"),
    "L3": ("#9333ea", "Bias TV 3000K"),
    "L4": ("#0891b2", "Biuro pasek 4000K"),
    "L5": ("#16a34a", "Zabudowa akcent 3000K"),
    "L6": ("#7c3aed", "Zabudowa wnętrze L 4000K"),
    "L7": ("#ea580c", "Zabudowa wnętrze P 4000K"),
}

WALL_COLOR = "#222"
WALL_LW = 2.4
DIM_COLOR = "#666"
NOTE_COLOR = "#444"
BG = "#fafaf7"


# ---------- pomocnicze symbole ----------
def spot(ax, x, y, circuit="L2", size=6, label=None):
    """Oczko podtynkowe = okrąg + X w środku"""
    color, _ = CIRCUITS[circuit]
    ax.add_patch(Circle((x, y), size, facecolor="white", edgecolor=color, linewidth=1.4, zorder=5))
    ax.plot([x - size * 0.6, x + size * 0.6], [y - size * 0.6, y + size * 0.6],
            color=color, linewidth=1.0, zorder=6)
    ax.plot([x - size * 0.6, x + size * 0.6], [y + size * 0.6, y - size * 0.6],
            color=color, linewidth=1.0, zorder=6)
    if label:
        ax.annotate(label, (x, y), xytext=(0, size + 4), textcoords="offset points",
                    fontsize=6, ha="center", color=color)


def led_strip(ax, xs, ys, circuit, label=None, lw=3, offset=(0, 0)):
    """Tasma LED = pogrubiona linia kropkowana w kolorze obwodu"""
    color, _ = CIRCUITS[circuit]
    ax.plot(xs, ys, color=color, linewidth=lw, linestyle=(0, (4, 2)), zorder=4)
    if label:
        mx = sum(xs) / len(xs) + offset[0]
        my = sum(ys) / len(ys) + offset[1]
        ax.annotate(label, (mx, my), fontsize=6.5, ha="center", color=color,
                    fontweight="bold")


def switch(ax, x, y, name, circuits, side="right"):
    """Wlacznik = kwadracik z numerem + lista obwodow ktore steruje"""
    ax.add_patch(Rectangle((x - 4, y - 4), 8, 8, facecolor="#fff7e6",
                           edgecolor="#b08a4a", linewidth=1.2, zorder=7))
    ax.text(x, y, name, ha="center", va="center", fontsize=6.2, fontweight="bold",
            color="#5a4a2a", zorder=8)
    dx = 12 if side == "right" else -12
    ha = "left" if side == "right" else "right"
    txt = " ".join(circuits)
    ax.annotate(txt, (x + dx, y), fontsize=5.5, ha=ha, va="center", color="#5a4a2a")


def socket(ax, x, y, label="230V", n=1):
    """Gniazdo 230V = pol-okrag"""
    ax.add_patch(patches.Wedge((x, y), 5, 0, 180, facecolor="#e0e7ef",
                               edgecolor="#444", linewidth=0.9, zorder=5))
    ax.text(x, y - 8, f"{label}×{n}" if n > 1 else label, ha="center", va="top",
            fontsize=5, color="#333")


def contactor(ax, x, y, label="K"):
    """Kontaktron = trojkat"""
    pts = [[x, y + 4], [x - 4, y - 3], [x + 4, y - 3]]
    ax.add_patch(Polygon(pts, facecolor="#fde68a", edgecolor="#a16207", linewidth=1.0, zorder=7))
    ax.text(x, y - 8, label, ha="center", va="top", fontsize=5.2, color="#a16207")


def dim_line(ax, x1, y1, x2, y2, text, offset_perp=15, side="above"):
    """Linia wymiarowa z opisem"""
    ax.plot([x1, x2], [y1, y2], color=DIM_COLOR, linewidth=0.6)
    # tick marks
    if x1 == x2:  # vertical
        ax.plot([x1 - 3, x1 + 3], [y1, y1], color=DIM_COLOR, linewidth=0.6)
        ax.plot([x2 - 3, x2 + 3], [y2, y2], color=DIM_COLOR, linewidth=0.6)
        mx, my = x1, (y1 + y2) / 2
        ax.text(mx + (offset_perp if side == "above" else -offset_perp),
                my, text, ha="left" if side == "above" else "right",
                va="center", fontsize=6, color=DIM_COLOR, rotation=90)
    else:  # horizontal
        ax.plot([x1, x1], [y1 - 3, y1 + 3], color=DIM_COLOR, linewidth=0.6)
        ax.plot([x2, x2], [y2 - 3, y2 + 3], color=DIM_COLOR, linewidth=0.6)
        mx, my = (x1 + x2) / 2, y1
        ax.text(mx, my + (offset_perp if side == "above" else -offset_perp),
                text, ha="center", va="bottom" if side == "above" else "top",
                fontsize=6, color=DIM_COLOR)


# ============================================================================
# KARTA 1 — RZUT POMIESZCZENIA Z OŚWIETLENIEM
# ============================================================================

def draw_rzut(ax):
    # pokoj 493 x 478 cm. Skala: 1 cm rzeczywisty = 1 jednostka na osi.
    W, H = 493, 478
    # WNĘKA MUROWA w scianie polnocnej wg rysunku: 266 szer x 40 GŁĘB.
    # Pralka/suszarka maja 60 cm gleb, wiec zabudowa WYSTAJE 20 cm do pokoju.
    NISZA_X = 197
    NISZA_W = 266
    NISZA_D_MUR = 40        # glebokosc wneki murowej (z rysunku: "040")
    ZAB_WYSTAJE = 20        # zabudowa wystaje do pokoju, by zmiescic AGD 60 cm
    ZAB_GL = NISZA_D_MUR + ZAB_WYSTAJE  # 60 cm calkowita glebokosc zabudowy
    ZAB_FRONT = H - ZAB_WYSTAJE          # front zabudowy = 20 cm w glab pokoju

    ax.set_xlim(-40, W + 70)
    ax.set_ylim(-55, H + 95)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_facecolor(BG)

    # ZEWNETRZNY OBWOD SCIAN. Wejscie: sciana E obok TV (srodek) — wg ustalen.
    DRZWI_Y0, DRZWI_W = 195, 90   # otwor drzwi na scianie E (y0..y0+90), srodek ~240
    ax.plot([0, W], [0, 0], color=WALL_COLOR, linewidth=WALL_LW)   # poludniowa (S)
    ax.plot([0, 0], [0, H], color=WALL_COLOR, linewidth=WALL_LW)   # zachodnia (W)
    ax.plot([W, W], [0, DRZWI_Y0], color=WALL_COLOR, linewidth=WALL_LW)        # E dol
    ax.plot([W, W], [DRZWI_Y0 + DRZWI_W, H], color=WALL_COLOR, linewidth=WALL_LW)  # E gora
    # drzwi wejsciowe (otwierane do srodka, luk)
    arc = patches.Arc((W, DRZWI_Y0), 2 * DRZWI_W, 2 * DRZWI_W, angle=0,
                      theta1=90, theta2=180, color="#999", linewidth=0.8)
    ax.add_patch(arc)
    ax.plot([W, W - DRZWI_W], [DRZWI_Y0, DRZWI_Y0], color="#999", linewidth=0.8, linestyle=":")
    ax.text(W - 18, DRZWI_Y0 + DRZWI_W / 2, "WEJŚCIE\n(obok TV)", fontsize=5,
            color="#666", ha="center", va="center", rotation=-90)
    # polnocna sciana z wnęką murowa:
    ax.plot([0, NISZA_X], [H, H], color=WALL_COLOR, linewidth=WALL_LW)
    ax.plot([NISZA_X + NISZA_W, W], [H, H], color=WALL_COLOR, linewidth=WALL_LW)
    # wneka murowa (cofniecie 40 cm w sciane):
    ax.plot([NISZA_X, NISZA_X], [H, H + NISZA_D_MUR], color=WALL_COLOR, linewidth=WALL_LW)
    ax.plot([NISZA_X + NISZA_W, NISZA_X + NISZA_W], [H, H + NISZA_D_MUR], color=WALL_COLOR, linewidth=WALL_LW)
    ax.plot([NISZA_X, NISZA_X + NISZA_W], [H + NISZA_D_MUR, H + NISZA_D_MUR], color=WALL_COLOR, linewidth=WALL_LW)


    # ZABUDOWA — front wystaje 20 cm do pokoju (od ZAB_FRONT do H+NISZA_D_MUR)
    zab_x0, zab_y0 = NISZA_X, ZAB_FRONT
    ax.add_patch(Rectangle((zab_x0, zab_y0), NISZA_W, ZAB_GL,
                           facecolor="#c9a47a", edgecolor="#6b4a2b", linewidth=1.0, alpha=0.5))
    ax.text(zab_x0 + NISZA_W / 2, zab_y0 + ZAB_GL / 2,
            "ZABUDOWA 266×60×250\norzech, drzwi przesuwne",
            ha="center", va="center", fontsize=6, color="#4a2f0f", fontweight="bold")
    # linia pierwotnego lica sciany (zeby pokazac wystawanie)
    ax.plot([NISZA_X, NISZA_X + NISZA_W], [H, H], color="#b00020",
            linewidth=0.7, linestyle=(0, (2, 2)), zorder=3)
    ax.annotate("zabudowa wystaje +20 cm\ndo pokoju (AGD 60 cm > wnęka 40)",
                xy=(zab_x0 + NISZA_W / 2, ZAB_FRONT),
                xytext=(zab_x0 + NISZA_W / 2 + 30, ZAB_FRONT - 42),
                fontsize=5.2, ha="left", color="#b00020",
                arrowprops=dict(arrowstyle="->", color="#b00020", lw=0.6))
    # podzial pol/pol pionowy
    ax.plot([zab_x0 + NISZA_W / 2, zab_x0 + NISZA_W / 2], [zab_y0, zab_y0 + ZAB_GL],
            color="#6b4a2b", linewidth=0.8, linestyle=":")
    # symbole pralka/suszarka po prawej, bojler po lewej
    ax.text(zab_x0 + 60, zab_y0 + ZAB_GL - 9, "bojler\n+ półki", fontsize=5,
            ha="center", color="#4a2f0f")
    ax.text(zab_x0 + NISZA_W - 100, zab_y0 + ZAB_GL - 9, "pralka", fontsize=5,
            ha="center", color="#4a2f0f")
    ax.text(zab_x0 + NISZA_W - 30, zab_y0 + ZAB_GL - 9, "suszarka", fontsize=5,
            ha="center", color="#4a2f0f")
    # strzalki przesuwu drzwi
    ax.annotate("", xy=(zab_x0 + 30, zab_y0 + 8), xytext=(zab_x0 + NISZA_W / 2 - 10, zab_y0 + 8),
                arrowprops=dict(arrowstyle="<->", color="#6b4a2b", lw=0.8))
    ax.annotate("", xy=(zab_x0 + NISZA_W / 2 + 10, zab_y0 + 8), xytext=(zab_x0 + NISZA_W - 30, zab_y0 + 8),
                arrowprops=dict(arrowstyle="<->", color="#6b4a2b", lw=0.8))

    # KONTAKTRONY w gornej prowadnicy drzwi (na froncie zabudowy)
    contactor(ax, zab_x0 + NISZA_W / 4, zab_y0 - 7, "K1→L6")
    contactor(ax, zab_x0 + 3 * NISZA_W / 4, zab_y0 - 7, "K2→L7")

    # MEBLE POMIESZCZENIA
    # biurko - przy scianie polnocnej (plaskie lico), lewa czesc
    bx0, by0, bw, bh = 15, H - 60, NISZA_X - 30, 50
    ax.add_patch(Rectangle((bx0, by0), bw, bh, facecolor="#e8dcc6", edgecolor="#8a6a3a", linewidth=0.8))
    ax.text(bx0 + bw / 2, by0 + bh / 2, "BIURKO 167×50", fontsize=6,
            ha="center", va="center", color="#5a3f1a", fontweight="bold")
    # krzeslo biurowe
    ax.add_patch(Circle((bx0 + bw / 2, by0 - 35), 22, facecolor="#d0d0d0", edgecolor="#666", linewidth=0.7))
    ax.text(bx0 + bw / 2, by0 - 35, "fotel", fontsize=4.5, ha="center", va="center", color="#444")

    # kanapa na scianie zachodniej
    kx0, ky0, kw, kh = 10, 150, 80, 220
    ax.add_patch(Rectangle((kx0, ky0), kw, kh, facecolor="#cfd4b9", edgecolor="#6a7242", linewidth=0.8))
    ax.text(kx0 + kw / 2, ky0 + kh / 2, "KANAPA\n220×80", fontsize=7,
            ha="center", va="center", color="#3a4220", fontweight="bold", rotation=90)
    # stolik kawowy
    ax.add_patch(Rectangle((140, 200), 120, 60, facecolor="#d4c4a6", edgecolor="#8a6a3a", linewidth=0.6))
    ax.text(200, 230, "stolik", fontsize=5.5, ha="center", va="center", color="#5a3f1a")

    # TV na scianie wschodniej, na poludnie od drzwi wejsciowych
    tvx, tvy, tvw, tvh = W - 25, 55, 15, 120
    ax.add_patch(Rectangle((tvx, tvy), tvw, tvh, facecolor="#222", edgecolor="#000", linewidth=0.8))
    ax.text(tvx - 8, tvy + tvh / 2, "TV 65\"", fontsize=6, ha="right", va="center",
            color="#222", fontweight="bold")
    # szafka pod TV
    ax.add_patch(Rectangle((W - 45, 30), 35, 22, facecolor="#e8dcc6", edgecolor="#8a6a3a", linewidth=0.6))

    # OSWIETLENIE - L1 wnęka po obwodzie salonu (pomija strefę biura i zabudowy)
    # obwod: zachod (od y=30 do y=140), poludnie (od x=15 do x=W-15), wschod (od y=30 do y=H-90)
    # i częsc N na prawo od zabudowy (od x=NISZA_X+NISZA_W+15 do x=W-15)
    led_strip(ax, [25, 25], [30, H - 90], "L1", label="L1 wnęka 3000K (cove)")
    led_strip(ax, [25, W - 25], [30, 30], "L1")
    led_strip(ax, [W - 25, W - 25], [30, H - 25], "L1")
    led_strip(ax, [NISZA_X + NISZA_W + 15, W - 25], [H - 25, H - 25], "L1")

    # L2 - spoty salon (6 sztuk)
    spots_pos = [
        (200, 290, "S1"),  # nad stolikiem 1
        (200, 380, "S2"),  # nad stolikiem 2
        (320, 250, "S3"),  # srodek salonu
        (320, 350, "S4"),
        (150, 110, "S5"),  # sciezka do drzwi
        (380, 110, "S6"),
    ]
    for x, y, lbl in spots_pos:
        spot(ax, x, y, circuit="L2", label=lbl)

    # L3 - bias TV (krotki pasek za TV)
    led_strip(ax, [W - 27, W - 27], [tvy + 5, tvy + tvh - 5], "L3", label="L3 bias", offset=(-15, 0), lw=2.4)

    # L4 - pasek nad biurkiem (prostopadle do sciany N, nad srodkiem biurka)
    led_strip(ax, [bx0 + bw / 2, bx0 + bw / 2], [by0 + 8, by0 + bh - 4],
              "L4", lw=3.4)
    ax.annotate("L4 pasek 4000K nad biurkiem", (bx0 + bw / 2, by0 + bh / 2),
                xytext=(0, -3), textcoords="offset points", fontsize=6,
                ha="center", va="top", color=CIRCUITS["L4"][0], fontweight="bold")

    # L5 - akcent zabudowy: belka nad zabudowa (w glebi wneki) + dwa piony po bokach frontu
    led_strip(ax, [NISZA_X + 5, NISZA_X + NISZA_W - 5],
              [H + NISZA_D_MUR + 16, H + NISZA_D_MUR + 16],
              "L5", label="L5 akcent: belka + piony 3000K", lw=2.8)
    # piony - wzdluz bocznych krawedzi zabudowy (od frontu do tylu wneki)
    led_strip(ax, [zab_x0 + 3, zab_x0 + 3], [ZAB_FRONT + 4, H + NISZA_D_MUR - 4], "L5", lw=2.0)
    led_strip(ax, [zab_x0 + NISZA_W - 3, zab_x0 + NISZA_W - 3], [ZAB_FRONT + 4, H + NISZA_D_MUR - 4], "L5", lw=2.0)

    # L6 i L7 - wnetrze zabudowy (tasmy w stropie przy froncie wnetrza)
    led_strip(ax, [zab_x0 + 10, zab_x0 + NISZA_W / 2 - 10],
              [ZAB_FRONT + 10, ZAB_FRONT + 10], "L6", lw=2.0)
    led_strip(ax, [zab_x0 + NISZA_W / 2 + 10, zab_x0 + NISZA_W - 10],
              [ZAB_FRONT + 10, ZAB_FRONT + 10], "L7", lw=2.0)
    # oczko IP44 nad bojlerem (D1) - czesc L6, w glebi przy tylnej scianie
    spot(ax, NISZA_X + 60, H + NISZA_D_MUR - 13, circuit="L6", size=4, label="IP44")

    # WLACZNIKI
    # P1 - przy wejsciu na scianie E (na polnoc od otworu drzwi)
    switch(ax, W - 35, DRZWI_Y0 + DRZWI_W + 18, "P1", ["L1 L2 L5"], side="left")
    # P2 - przy kanapie
    switch(ax, kx0 + kw + 15, ky0 + 30, "P2", ["L1", "scena Film"], side="right")
    # P3 - biuro
    switch(ax, bx0 + bw - 10, by0 - 15, "P3", ["L4"], side="right")
    # P4 - wnetrze zabudowy (manualny override), na froncie prawej sekcji
    switch(ax, zab_x0 + NISZA_W - 20, ZAB_FRONT + 18, "P4", ["L6 L7 manual"], side="left")

    # GNIAZDA 230V - zaznaczone w kluczowych miejscach
    socket(ax, W - 15, 115, "TV", n=4)      # za TV (poludnie sciany E)
    socket(ax, W - 15, 320, "AC", n=2)      # przy wejsciu (odkurzacz/ladowarka)
    socket(ax, 35, 130, "lampa", n=1)
    socket(ax, kx0 + kw + 10, ky0, "AC", n=6)  # za kanapa
    socket(ax, bx0 + 30, by0 + 5, "PC", n=4)  # biurko
    socket(ax, zab_x0 + NISZA_W - 25, zab_y0 + 26, "pralka", n=1)
    socket(ax, zab_x0 + NISZA_W - 70, zab_y0 + 26, "suszarka", n=1)
    socket(ax, zab_x0 + 30, zab_y0 + 26, "bojler IP44", n=1)

    # WYMIARY
    dim_line(ax, 0, H + 88, W, H + 88, "493 cm (ściana N)", offset_perp=8)
    dim_line(ax, -28, 0, -28, H, "478 cm (gł. pokoju)", offset_perp=8, side="above")
    dim_line(ax, NISZA_X, H + NISZA_D_MUR + 40, NISZA_X + NISZA_W, H + NISZA_D_MUR + 40,
             "wnęka / zabudowa 266 cm", offset_perp=6)
    dim_line(ax, 0, H + 58, NISZA_X, H + 58, "biuro 197", offset_perp=6)
    # glebokosc wneki murowej 40 cm (pionowy wymiar przy lewej krawedzi wneki)
    dim_line(ax, NISZA_X - 14, H, NISZA_X - 14, H + NISZA_D_MUR, "wnęka 40", offset_perp=5, side="below")

    # POTWIERDZONE: "OR" z rysunku = drzwi przesuwne zabudowy (NIE okno — brak kolizji)
    ax.text(NISZA_X + NISZA_W / 2, H + NISZA_D_MUR + 28,
            '„OR" = drzwi przesuwne zabudowy (potwierdzone — brak okna)',
            fontsize=5.2, ha="center", color="#2a6a2a")
    # przylacza pralki/odplyw — do potwierdzenia w naturze (sekcja prawa)
    ax.text(NISZA_X + NISZA_W - 20, H + NISZA_D_MUR + 12,
            "przyłącza wody + odpływ pralki\n(do potwierdzenia w naturze)",
            fontsize=4.6, ha="center", va="bottom", color="#888")

    # ROZA KIERUNKOW + skala
    ax.text(W + 38, H, "N", ha="center", va="center", fontsize=10, fontweight="bold")
    ax.annotate("", xy=(W + 38, H - 25), xytext=(W + 38, H + 15),
                arrowprops=dict(arrowstyle="->", color="#000", lw=1.0))
    ax.text(W + 38, H - 40, "skala\n1:50", ha="center", va="top", fontsize=6.5, color="#444")

    # TYTUL
    ax.text(0, -25, "KARTA 1 / 3   ·   RZUT POMIESZCZENIA Z OŚWIETLENIEM (v3)   ·   1:50",
            fontsize=9.5, fontweight="bold", color="#222")


def draw_rzut_legenda(ax):
    """Legenda do karty 1."""
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    ax.set_facecolor(BG)

    y = 95
    ax.text(2, y, "LEGENDA", fontsize=8, fontweight="bold", color="#222")
    y -= 6

    # obwody
    ax.text(2, y, "Obwody (kable w stropie GK):", fontsize=6.5, fontweight="bold", color="#444")
    y -= 5
    for code, (color, name) in CIRCUITS.items():
        ax.plot([3, 9], [y, y], color=color, linewidth=2.5, linestyle=(0, (4, 2)))
        ax.text(11, y, f"{code} — {name}", fontsize=6, color="#333", va="center")
        y -= 4

    y -= 3
    ax.text(2, y, "Symbole:", fontsize=6.5, fontweight="bold", color="#444")
    y -= 5

    # spot
    spot_ax_x, spot_ax_y = 5, y
    ax.add_patch(Circle((spot_ax_x, spot_ax_y), 1.5, facecolor="white",
                        edgecolor="#dc2626", linewidth=1.2))
    ax.plot([spot_ax_x - 0.9, spot_ax_x + 0.9], [spot_ax_y - 0.9, spot_ax_y + 0.9],
            color="#dc2626", linewidth=0.7)
    ax.plot([spot_ax_x - 0.9, spot_ax_x + 0.9], [spot_ax_y + 0.9, spot_ax_y - 0.9],
            color="#dc2626", linewidth=0.7)
    ax.text(11, y, "oczko podtynkowe GU10 (kolor=obwód)", fontsize=6, color="#333", va="center")
    y -= 5

    ax.plot([3, 9], [y, y], color="#16a34a", linewidth=3, linestyle=(0, (4, 2)))
    ax.text(11, y, "taśma LED w profilu aluminiowym", fontsize=6, color="#333", va="center")
    y -= 5

    ax.add_patch(Rectangle((3, y - 1.5), 4, 3, facecolor="#fff7e6",
                           edgecolor="#b08a4a", linewidth=1.0))
    ax.text(5, y, "P", ha="center", va="center", fontsize=5, fontweight="bold", color="#5a4a2a")
    ax.text(11, y, "włącznik klawiszowy (Shelly w puszce), h=110 cm", fontsize=6, color="#333", va="center")
    y -= 5

    ax.add_patch(Polygon([[5, y + 1.2], [3.5, y - 1], [6.5, y - 1]],
                         facecolor="#fde68a", edgecolor="#a16207", linewidth=0.9))
    ax.text(11, y, "kontaktron magnetyczny (w prowadnicy drzwi)", fontsize=6, color="#333", va="center")
    y -= 5

    ax.add_patch(patches.Wedge((5, y), 1.5, 0, 180, facecolor="#e0e7ef",
                               edgecolor="#444", linewidth=0.8))
    ax.text(11, y, "gniazdo 230V (×N = liczba modułów)", fontsize=6, color="#333", va="center")

    # uwagi
    y -= 9
    ax.text(2, y, "Uwagi:", fontsize=6.5, fontweight="bold", color="#444")
    y -= 5
    notes = [
        "• wszystkie włączniki na h=110 cm, ta sama seria (np. Berker R.1 / Kontakt-Simon 55 mat)",
        "• każda puszka z przewodem N (neutralnym) — wymaga Shelly",
        "• zasilacze LED 24V w serwerowni / w klapie rewizyjnej GK, NIE w meblu",
        "• L6 i L7 sterowane automatycznie z kontaktronów K1/K2 + P4 awaryjnie",
        "• pralka, suszarka, bojler — każde na osobnym obwodzie B16A + RCD 30 mA",
        "• rzut schematyczny — dokładne pozycje opraw uzgodnij na budowie z elektrykiem",
    ]
    for n in notes:
        ax.text(2, y, n, fontsize=5.8, color="#333")
        y -= 4


# ============================================================================
# KARTA 2 — ELEWACJA ZABUDOWY
# ============================================================================

def draw_elewacja_front(ax):
    """Front zabudowy 266x250 — drzwi zamknięte z LED w belce + piony."""
    ax.axis("off")
    ax.set_facecolor(BG)
    ax.set_xlim(-40, 310)
    ax.set_ylim(-10, 340)
    W, H = 266, 250
    ox, oy = 0, 10
    # rama zewnetrzna zabudowy
    ax.add_patch(Rectangle((ox, oy), W, H, facecolor="#8b5a2b", edgecolor="#3a1f08",
                           linewidth=1.4))
    # drzwi przesuwne - 2 panele po 135 cm, nachodzące. Rysuje 2 prostokaty.
    panel_w = 135
    # panel prawy (na pierwszym planie, obecnie kryje prawą stronę)
    ax.add_patch(Rectangle((ox + W - panel_w, oy + 5), panel_w, H - 10,
                           facecolor="#6b4a2b", edgecolor="#3a1f08", linewidth=0.8))
    # panel lewy (cofnięty)
    ax.add_patch(Rectangle((ox + 0, oy + 5), panel_w, H - 10,
                           facecolor="#7a5630", edgecolor="#3a1f08", linewidth=0.8))
    # uchwyt L-profile czarny matowy
    ax.add_patch(Rectangle((ox + panel_w - 4, oy + 15), 3, H - 30,
                           facecolor="#111", edgecolor="#000", linewidth=0.4))
    ax.add_patch(Rectangle((ox + W - panel_w - 1, oy + 15), 3, H - 30,
                           facecolor="#111", edgecolor="#000", linewidth=0.4))

    # GORNA BELKA z LED ukrytym (C1 / L5)
    # belka jest częścią mebla wysokości ~10 cm widoczna nad drzwiami
    ax.add_patch(Rectangle((ox, oy + H - 8), W, 8, facecolor="#5a3a18",
                           edgecolor="#3a1f08", linewidth=1.0))
    # strzelisty LED z gory belki w sufit (rysuje "blask")
    for i, x in enumerate(range(int(ox + 10), int(ox + W), 16)):
        ax.add_patch(patches.FancyBboxPatch((x, oy + H + 1), 8, 14,
                                            boxstyle="round,pad=0", linewidth=0,
                                            facecolor="#fbcc7a", alpha=0.45))
    ax.text(ox + W / 2, oy + H + 22, "L5 — LED 3000K w szczelinie 5–10 cm (cove → sufit)",
            ha="center", fontsize=6, color="#b85a00", fontweight="bold")

    # PIONY LED w ramie po bokach (C2 / L5)
    for x in [ox - 2, ox + W - 1]:
        ax.add_patch(Rectangle((x, oy + 10), 3, H - 20, facecolor="#fbcc7a",
                               edgecolor="#d97706", linewidth=0.4, alpha=0.85))
    ax.annotate("L5 piony 240 cm", xy=(ox - 4, oy + H / 2),
                xytext=(-50, 0), textcoords="offset points",
                fontsize=6, color="#b85a00",
                arrowprops=dict(arrowstyle="->", color="#b85a00", lw=0.7))

    # strzalki przesuwu
    ax.annotate("", xy=(ox + 30, oy + H / 2), xytext=(ox + panel_w - 10, oy + H / 2),
                arrowprops=dict(arrowstyle="<->", color="#fff", lw=1.2))
    ax.text(ox + panel_w / 2 - 25, oy + H / 2 + 8, "przesuw", fontsize=5.5,
            color="#fff", ha="center")

    # wymiar W i H
    dim_line(ax, ox, oy - 15, ox + W, oy - 15, "266 cm", offset_perp=4, side="below")
    dim_line(ax, ox + W + 18, oy, ox + W + 18, oy + H, "250 cm", offset_perp=4)

    ax.text(ox + W / 2, oy + H + 50, "FRONT — drzwi zamknięte (LED w belce L5 + piony L5)",
            ha="center", fontsize=8, fontweight="bold", color="#3a1f08")
    ax.text(ox + W / 2, oy + H + 38,
            "głębokość zabudowy 60 cm = wnęka mur. 40 cm + wystaje 20 cm do pokoju (AGD 60 cm)",
            ha="center", fontsize=5.8, color="#b00020")

    # nagłówek karty
    ax.text(-40, 330, "KARTA 2 / 3   ·   ELEWACJA + PRZEKRÓJ ZABUDOWY 266×250 cm (v2)",
            fontsize=10, fontweight="bold", color="#222")


def draw_elewacja_wnetrze(ax):
    """Przekrój przez wnętrze zabudowy (drzwi pominięte) — pralka, suszarka, bojler, LED L6/L7."""
    ax.axis("off")
    ax.set_facecolor(BG)
    ax.set_xlim(-50, 340)
    ax.set_ylim(-30, 290)
    W, H = 266, 250
    ox2 = 320
    # cofnięcie rysunku (niezbyt duzo miejsca)
    # bedzie pod glownym frontem.
    # Faktycznie ulozymy go ponizej.
    ox2, oy2 = 0, -250 + 50  # przesuwam ponizej
    # Lepiej narysuj pod elewacja - czyli zmieniam wymiary i obrazem osi
    # PRZEROBKA: zamiast obok, zrobimy ponizej w osobnym ax (zwrocimy z funkcji)

    # WNETRZE jako przekrój
    ox3, oy3 = 0, 10
    # rama
    ax.add_patch(Rectangle((ox3, oy3), W, H, facecolor="#f5ebd6", edgecolor="#6b4a2b",
                           linewidth=1.4))
    # podzial wewnetrzny - lewa polowa (gospodarcza/bojler), prawa polowa (pralka/suszarka)
    mid = W / 2
    ax.plot([ox3 + mid, ox3 + mid], [oy3, oy3 + H], color="#6b4a2b", linewidth=1.0)
    # cokol
    ax.add_patch(Rectangle((ox3, oy3), W, 10, facecolor="#111", edgecolor="#000", linewidth=0.5))
    # gorna belka wewnetrzna
    ax.add_patch(Rectangle((ox3, oy3 + H - 8), W, 8, facecolor="#d4c4a6",
                           edgecolor="#6b4a2b", linewidth=0.5))

    # LEWA polowa: bojler u gory, polki ponizej
    # bojler ~Ø45 cm na wys ~150-200 cm
    ax.add_patch(patches.FancyBboxPatch((ox3 + 35, oy3 + 150), 50, 90,
                                        boxstyle="round,pad=0,rounding_size=8",
                                        facecolor="white", edgecolor="#666", linewidth=0.8))
    ax.text(ox3 + 60, oy3 + 195, "BOJLER\nelektr.\n~50 l", ha="center", va="center",
            fontsize=5.5, color="#222", fontweight="bold")
    # zawory pod bojlerem
    ax.text(ox3 + 60, oy3 + 135, "↑ zawory + przyłącza wody", fontsize=4.5,
            ha="center", color="#666")
    # polki w lewej kolumnie (poza obszarem bojlera)
    for sy in [10, 50, 90, 240 - 10]:
        ax.plot([ox3 + 5, ox3 + mid - 5], [oy3 + sy, oy3 + sy],
                color="#6b4a2b", linewidth=0.8)
    # tasma LED w stropie wewnetrznym lewej (L6)
    led_strip(ax, [ox3 + 10, ox3 + mid - 10], [oy3 + H - 12, oy3 + H - 12], "L6", lw=2.0)
    # oczko IP44 nad bojlerem (L6)
    spot(ax, ox3 + 60, oy3 + H - 18, circuit="L6", size=4)
    ax.text(ox3 + 60, oy3 + H - 24, "L6 IP44", fontsize=4.5, ha="center", color="#7c3aed")
    # podswietlenie polek lewej
    for sy in [10, 50, 90]:
        ax.plot([ox3 + 8, ox3 + mid - 8], [oy3 + sy + 1, oy3 + sy + 1],
                color="#7c3aed", linewidth=1.0, linestyle=(0, (3, 2)))
    # gniazdo bojlera
    ax.add_patch(patches.Wedge((ox3 + 110, oy3 + 165), 4, 0, 180,
                               facecolor="#e0e7ef", edgecolor="#444", linewidth=0.6))
    ax.text(ox3 + 110, oy3 + 175, "230V IP44", fontsize=4, ha="center", color="#222")

    # PRAWA polowa: polki gora (recznikow), pralka + suszarka na dole
    # polki gorne
    for sy in [240 - 10, 200, 160, 120]:
        ax.plot([ox3 + mid + 5, ox3 + W - 5], [oy3 + sy, oy3 + sy],
                color="#6b4a2b", linewidth=0.8)
    # pralka i suszarka (h ~85, w ~60)
    ax.add_patch(Rectangle((ox3 + mid + 8, oy3 + 12), 55, 85,
                           facecolor="#f5f5f5", edgecolor="#444", linewidth=0.8))
    ax.add_patch(Circle((ox3 + mid + 35, oy3 + 55), 18, facecolor="white",
                        edgecolor="#444", linewidth=0.8))
    ax.text(ox3 + mid + 35, oy3 + 102, "pralka 60×60×85", fontsize=4.5,
            ha="center", color="#222")
    ax.add_patch(Rectangle((ox3 + mid + 70, oy3 + 12), 55, 85,
                           facecolor="#f5f5f5", edgecolor="#444", linewidth=0.8))
    ax.add_patch(Circle((ox3 + mid + 97, oy3 + 55), 18, facecolor="white",
                        edgecolor="#444", linewidth=0.8))
    ax.text(ox3 + mid + 97, oy3 + 102, "suszarka 60×60×85", fontsize=4.5,
            ha="center", color="#222")
    # tasma LED prawej (L7) + podswietlenie gornych polek
    led_strip(ax, [ox3 + mid + 10, ox3 + W - 10], [oy3 + H - 12, oy3 + H - 12], "L7", lw=2.0)
    for sy in [240 - 10, 200, 160, 120]:
        ax.plot([ox3 + mid + 8, ox3 + W - 8], [oy3 + sy + 1, oy3 + sy + 1],
                color="#ea580c", linewidth=1.0, linestyle=(0, (3, 2)))
    # gniazda za pralka i suszarka
    ax.add_patch(patches.Wedge((ox3 + mid + 35, oy3 + 105), 3, 0, 180,
                               facecolor="#e0e7ef", edgecolor="#444", linewidth=0.5))
    ax.add_patch(patches.Wedge((ox3 + mid + 97, oy3 + 105), 3, 0, 180,
                               facecolor="#e0e7ef", edgecolor="#444", linewidth=0.5))

    # P4 wewn awaryjny (na bocznej sciance prawej, h~150)
    switch(ax, ox3 + W - 8, oy3 + 150, "P4", ["L6 L7"], side="left")

    # wymiary wnetrza
    dim_line(ax, ox3, oy3 - 15, ox3 + W, oy3 - 15, "266 cm", offset_perp=4, side="below")
    dim_line(ax, ox3 - 18, oy3, ox3 - 18, oy3 + H, "250 cm", offset_perp=4, side="below")
    # poziomy:
    ax.text(ox3 + W + 30, oy3 + 85, "h pralki/suszarki\n~10 cm cokół + 85 cm",
            fontsize=5.5, color="#444", ha="left", va="center")
    ax.text(ox3 + W + 30, oy3 + 195, "h bojlera ~150–230 cm",
            fontsize=5.5, color="#444", ha="left", va="center")

    ax.text(ox3 + W / 2, oy3 + H + 20, "WNĘTRZE (przekrój, drzwi pominięte)",
            ha="center", fontsize=8, fontweight="bold", color="#3a1f08")


# ============================================================================
# KARTA 3 — SCHEMAT BLOKOWY OBWODÓW
# ============================================================================

def draw_schemat(ax):
    """Rozdzielnica → Shelly → Oprawy. Schemat blokowy."""
    ax.axis("off")
    ax.set_facecolor(BG)
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 140)

    # ROZDZIELNICA
    ax.add_patch(FancyBboxPatch((3, 35), 26, 80, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor="#e0e7ef", edgecolor="#222", linewidth=1.2))
    ax.text(16, 110, "ROZDZIELNICA\n230V AC", ha="center", va="center",
            fontsize=6.2, fontweight="bold", color="#222")
    # bezpieczniki - lista
    breakers = ["B10A L1+L3", "B10A L2", "B10A L4", "B10A L5",
                "B10A L6", "B10A L7", "B16A pralka", "B16A suszarka",
                "B16A bojler", "RCD 30 mA"]
    by = 96
    for b in breakers:
        ax.text(16, by, b, fontsize=4.5, ha="center", color="#333")
        by -= 5

    # SERWEROWNIA (zasilacze + Shelly Pro)
    ax.add_patch(FancyBboxPatch((40, 50), 35, 70, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor="#fff7e6", edgecolor="#b08a4a", linewidth=1.2))
    ax.text(57, 115, "SERWEROWNIA", ha="center", va="center",
            fontsize=6.5, fontweight="bold", color="#5a4a2a")
    items = [
        ("Mean Well HLG-240H-24A dim", "(L1+L3 — 240W)"),
        ("Mean Well LPV-35-24", "(L4 — 35W)"),
        ("Mean Well LPV-100-24", "(L5 — 100W)"),
        ("Mean Well LPV-60-24", "(L6 — 60W)"),
        ("Mean Well LPV-60-24", "(L7 — 60W)"),
        ("Shelly Pro DM 2PM", "(L2 + L5 dim 230V)"),
        ("Shelly Pro Dimmer 0–10V", "(L1, L3, L4)"),
        ("Home Assistant", "(sceny + HA)"),
    ]
    iy = 108
    for nm, det in items:
        ax.text(43, iy, "▪ " + nm, fontsize=4.5, color="#222", fontweight="bold")
        ax.text(43, iy - 3, "  " + det, fontsize=4, color="#666", style="italic")
        iy -= 7

    # PUSZKI KLAWISZOWE (Shelly i4 + przyciski)
    puszki = [
        (90, 110, "P1", "L1+L2+L5 + scena", "drzwi wej., h=110"),
        (90, 90, "P2", "L1 + scena Film", "kanapa, h=110"),
        (90, 70, "P3", "L4 (dim)", "biuro, h=110"),
        (90, 50, "P4 IP44", "L6 L7 awaryjny", "wewn. zab., h=150"),
        (90, 30, "K1, K2", "kontaktrony", "prowadnica drzwi przesuw."),
    ]
    for px, py, nm, ctrl, where in puszki:
        ax.add_patch(FancyBboxPatch((px - 8, py - 4), 16, 8,
                                    boxstyle="round,pad=0.3,rounding_size=1",
                                    facecolor="#fff", edgecolor="#b08a4a", linewidth=1.0))
        ax.text(px, py + 1, nm, ha="center", va="center", fontsize=5.5,
                fontweight="bold", color="#5a4a2a")
        ax.text(px, py - 2, ctrl, ha="center", va="center", fontsize=4, color="#333")
        ax.text(px + 14, py, where, ha="left", va="center", fontsize=4.5,
                color="#666", style="italic")

    # OPRAWY KOŃCOWE
    fixtures = [
        (165, 120, "L1", "Wnęka LED 3000K, 12 m, COB 14W/m, profil wpuszczany"),
        (165, 110, "L2", "6× oczko GU10 6W 3000K CRI≥90, ściemnialne"),
        (165, 100, "L3", "Bias TV 24V 3000K, 1,5 m"),
        (165, 90, "L4", "Pasek nad biurkiem 4000K, 1,2 m, COB CRI≥90"),
        (165, 80, "L5", "Belka 266 cm + 2 piony 240 cm, 3000K"),
        (165, 70, "L6", "Wnętrze L: taśma + podświetlenia półek + IP44 nad bojlerem 4000K"),
        (165, 60, "L7", "Wnętrze P: taśma nad pralką + podświetlenia półek 4000K"),
    ]
    for fx, fy, code, desc in fixtures:
        color, _ = CIRCUITS[code]
        ax.add_patch(Circle((fx - 8, fy), 2.5, facecolor=color, edgecolor="#222", linewidth=0.6))
        ax.text(fx - 8, fy, code, ha="center", va="center", fontsize=4.5,
                fontweight="bold", color="#fff")
        ax.text(fx - 3, fy, desc, ha="left", va="center", fontsize=4.8, color="#222")

    # POLACZENIA - linie z rozdzielnicy do serwerowni do puszek do opraw (schematyczne strzalki)
    # rozdzielnica -> serwerownia
    ax.annotate("", xy=(40, 85), xytext=(29, 85),
                arrowprops=dict(arrowstyle="->", color="#444", lw=1.0))
    ax.text(34, 88, "230V", fontsize=4.5, ha="center", color="#444")

    # serwerownia -> puszki (logika sterowania)
    ax.annotate("", xy=(82, 70), xytext=(75, 75),
                arrowprops=dict(arrowstyle="->", color="#b08a4a", lw=0.8, linestyle="--"))
    ax.text(78, 78, "MQTT / LAN", fontsize=4, ha="center", color="#b08a4a", style="italic")

    # serwerownia -> oprawy (zasilanie 24V dla LED)
    ax.annotate("", xy=(150, 90), xytext=(75, 90),
                arrowprops=dict(arrowstyle="->", color="#d97706", lw=1.0))
    ax.text(112, 93, "24V DC (LiYY 2×1,5)", fontsize=4.5, ha="center", color="#d97706")
    ax.annotate("", xy=(150, 110), xytext=(75, 100),
                arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.0))
    ax.text(112, 106, "230V (oczka L2)", fontsize=4.5, ha="center", color="#dc2626")

    # K1/K2 -> Shelly UNI -> L6/L7
    ax.annotate("", xy=(82, 30), xytext=(57, 50),
                arrowprops=dict(arrowstyle="<-", color="#a16207", lw=0.7))
    ax.text(72, 38, "wejście\nShelly UNI", fontsize=4, ha="center", color="#a16207")

    # SCENY
    ax.add_patch(FancyBboxPatch((5, 5), 145, 22, boxstyle="round,pad=0.5,rounding_size=2",
                                facecolor="#e9f5e9", edgecolor="#2a6a2a", linewidth=1.0))
    ax.text(8, 22, "SCENY HA:", fontsize=6, fontweight="bold", color="#2a6a2a")
    sceny = [
        ("Dzień", "wszystko OFF, kontaktrony AUTO"),
        ("Praca", "L1 30%, L4 100%, reszta OFF"),
        ("Wieczór", "L1 60%, L3 50%, L5 70%"),
        ("Film", "L1 15%, L3 80% bias, L5 20%"),
        ("Sprzątanie", "L1 80%, L2 100%, L4 60%, L6 L7 manual 100%"),
        ("Noc", "L1 5%, L5 10%, reszta OFF"),
    ]
    sx = 32
    sy = 20
    for nm, ds in sceny:
        ax.text(sx, sy, nm, fontsize=4.5, fontweight="bold", color="#2a6a2a")
        ax.text(sx, sy - 2, ds, fontsize=3.8, color="#333")
        sy -= 6
        if sy < 8:
            sx += 60
            sy = 20

    # TYTUL
    ax.text(0, 132, "KARTA 3 / 3   ·   SCHEMAT BLOKOWY OBWODÓW I STEROWANIA",
            fontsize=10, fontweight="bold", color="#222")


# ============================================================================
# GLOWNY RENDER
# ============================================================================

def render():
    # KARTA 1: rzut + legenda obok
    fig1 = plt.figure(figsize=(16.5, 11.7), facecolor=BG)  # A3 landscape
    ax_main = fig1.add_axes([0.04, 0.05, 0.66, 0.92])
    ax_leg = fig1.add_axes([0.72, 0.05, 0.26, 0.92])
    draw_rzut(ax_main)
    draw_rzut_legenda(ax_leg)
    fig1.savefig(OUT / "TECH-01-rzut.pdf", facecolor=BG, dpi=200)
    fig1.savefig(OUT / "TECH-01-rzut.png", facecolor=BG, dpi=150)
    plt.close(fig1)

    # KARTA 2: elewacja (front + przekrój wnętrza, A3 portrait)
    fig2 = plt.figure(figsize=(11.7, 16.5), facecolor=BG)
    ax2a = fig2.add_axes([0.06, 0.50, 0.88, 0.46])
    ax2b = fig2.add_axes([0.06, 0.04, 0.88, 0.42])
    draw_elewacja_front(ax2a)
    draw_elewacja_wnetrze(ax2b)
    fig2.savefig(OUT / "TECH-02-elewacja.pdf", facecolor=BG, dpi=200)
    fig2.savefig(OUT / "TECH-02-elewacja.png", facecolor=BG, dpi=150)
    plt.close(fig2)

    # KARTA 3: schemat
    fig3 = plt.figure(figsize=(16.5, 11.7), facecolor=BG)
    ax3 = fig3.add_axes([0.04, 0.04, 0.92, 0.92])
    draw_schemat(ax3)
    fig3.savefig(OUT / "TECH-03-schemat.pdf", facecolor=BG, dpi=200)
    fig3.savefig(OUT / "TECH-03-schemat.png", facecolor=BG, dpi=150)
    plt.close(fig3)

    # ALL — wszystko razem
    with PdfPages(OUT / "TECH-ALL.pdf") as pdf:
        for fn in [draw_rzut, draw_elewacja_front, draw_schemat]:
            if fn is draw_rzut:
                fig = plt.figure(figsize=(16.5, 11.7), facecolor=BG)
                ax_main = fig.add_axes([0.04, 0.05, 0.66, 0.92])
                ax_leg = fig.add_axes([0.72, 0.05, 0.26, 0.92])
                draw_rzut(ax_main)
                draw_rzut_legenda(ax_leg)
            elif fn is draw_elewacja_front:
                fig = plt.figure(figsize=(11.7, 16.5), facecolor=BG)
                axa = fig.add_axes([0.06, 0.50, 0.88, 0.46])
                axb = fig.add_axes([0.06, 0.04, 0.88, 0.42])
                draw_elewacja_front(axa)
                draw_elewacja_wnetrze(axb)
            else:
                fig = plt.figure(figsize=(16.5, 11.7), facecolor=BG)
                ax = fig.add_axes([0.04, 0.04, 0.92, 0.92])
                draw_schemat(ax)
            pdf.savefig(fig, facecolor=BG)
            plt.close(fig)

    for f in sorted(OUT.glob("TECH-*")):
        print(f"  {f.name}  ({f.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    render()
