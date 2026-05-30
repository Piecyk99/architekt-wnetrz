# -*- coding: utf-8 -*-
"""Rzut z naniesionym oswietleniem i podzialem na obwody/wlaczniki."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.lines import Line2D

fig, ax = plt.subplots(figsize=(13, 12))

# --- kolory obwodow ---
C1 = "#1f77b4"  # Salon glowne
C2 = "#2ca02c"  # Cove tasma sufitowa
C3 = "#ff7f0e"  # Bias za TV
C4 = "#d62728"  # Akcenty sciany TV
C5 = "#9467bd"  # Biuro
C6 = "#17becf"  # Przejscie / komunikacja
C7 = "#7f7f7f"  # Szafa (auto)

WALL = "#2b2b2b"

# ---------- SCIANY / KONTUR ----------
# pokoj glowny
ax.add_patch(Rectangle((0, 0), 493, 456, fill=False, lw=4, ec=WALL))
# szafa przesuwna (gornie-lewo) 62 x 264
ax.add_patch(Rectangle((0, 0), 62, 264, fill=True, fc="#f0ece4", ec=WALL, lw=2))
# linia drzwi przesuwnych szafy (prawa krawedz)
ax.plot([62, 62], [10, 254], color="#8a7f6a", lw=3, ls=(0, (6, 4)))
# linia oddzielajaca biuro od salonu (dolna krawedz szafy w lewo)
ax.plot([0, 62], [264, 264], color=WALL, lw=2)

# ---------- MEBLE (orientacja) ----------
# TV na gornej scianie (centralnie, przy wejsciu)
ax.add_patch(Rectangle((290, 2), 110, 9, fc="#222", ec="#222"))
ax.text(345, 26, "TV", ha="center", va="center", fontsize=15, fontweight="bold")
# Kanapa na dole, twarz do TV
ax.add_patch(Rectangle((250, 380), 200, 55, fc="#e8e2d6", ec="#9a8f78", lw=1.5))
ax.text(350, 408, "KANAPA", ha="center", va="center", fontsize=11, color="#6b6253")
# Biurko przy lewej scianie (biuro)
ax.add_patch(Rectangle((8, 300), 58, 120, fc="#e8e2d6", ec="#9a8f78", lw=1.5))
ax.text(120, 360, "BIURO", ha="center", va="center", fontsize=13,
        fontweight="bold", color="#555")
ax.text(31, 130, "SZAFA\nPRZESUWNA\n(gospodarcze)", ha="center", va="center",
        fontsize=8.5, rotation=90, color="#6b6253")
ax.text(360, 200, "SALON", ha="center", va="center", fontsize=15,
        fontweight="bold", color="#bbb", zorder=0)

# ---------- WYMIARY ----------
def dim(x, y, t):
    ax.text(x, y, t, ha="center", va="center", fontsize=9, color="#444",
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))
dim(31, -16, "62")
dim(-22, 132, "264")
dim(-22, 360, "192")
dim(250, 470, "493")
dim(512, 228, "456")

# ============ OPRAWY / OBWODY ============
def spots(xs, ys, color, label, s=420):
    first = True
    for x in xs:
        for y in ys:
            ax.scatter(x, y, s=s, marker="o", facecolors="white",
                       edgecolors=color, linewidths=2.6, zorder=5)
            ax.scatter(x, y, s=s*0.18, marker="o", color=color, zorder=6)

# Obwod 1 - salon glowne (siatka oczek nad strefa wypoczynku)
for x in [215, 330, 445]:
    for y in [150, 300]:
        ax.scatter(x, y, s=430, facecolors="white", edgecolors=C1, lw=2.8, zorder=5)
        ax.scatter(x, y, s=70, color=C1, zorder=6)

# Obwod 4 - akcenty sciany TV (kierunkowe)
for x in [300, 345, 390]:
    ax.scatter(x, 60, s=430, facecolors="white", edgecolors=C4, lw=2.8, zorder=5)
    ax.scatter(x, 60, s=70, color=C4, marker=">", zorder=6)

# Obwod 3 - bias / tasma za TV
ax.plot([293, 397], [14, 14], color=C3, lw=7, solid_capstyle="round", zorder=4)

# Obwod 2 - cove tasma sufitowa (obwod salonu, kreskowana)
ax.add_patch(Rectangle((150, 70), 320, 360, fill=False, ec=C2, lw=3,
                       ls=(0, (8, 5)), zorder=3))

# Obwod 5 - biuro (oczka nad biurkiem)
for x in [37, 120]:
    ax.scatter(x, 340, s=430, facecolors="white", edgecolors=C5, lw=2.8, zorder=5)
    ax.scatter(x, 340, s=70, color=C5, zorder=6)
ax.scatter(37, 410, s=430, facecolors="white", edgecolors=C5, lw=2.8, zorder=5)
ax.scatter(37, 410, s=70, color=C5, zorder=6)

# Obwod 6 - przejscie / komunikacja
for x in [120, 200]:
    ax.scatter(x, 215, s=430, facecolors="white", edgecolors=C6, lw=2.8, zorder=5)
    ax.scatter(x, 215, s=70, color=C6, zorder=6)

# Obwod 7 - szafa (auto): oczka + tasma w srodku
for y in [80, 195]:
    ax.scatter(31, y, s=360, facecolors="white", edgecolors=C7, lw=2.6, zorder=5)
    ax.scatter(31, y, s=55, color=C7, zorder=6)
ax.plot([14, 14], [60, 230], color=C7, lw=5, solid_capstyle="round", zorder=4)

# ---------- PANELE WLACZNIKOW ----------
def panel(x, y, txt, anchor="left"):
    ax.add_patch(FancyBboxPatch((x, y), 70, 34, boxstyle="round,pad=2",
                 fc="#fff7d6", ec="#caa800", lw=2, zorder=8))
    ax.text(x+35, y+17, txt, ha="center", va="center", fontsize=9,
            fontweight="bold", color="#7a5c00", zorder=9)
# panel glowny przy wejsciu (srodek sciany TV)
panel(415, 20, "WP\npanel\nglowny")
ax.annotate("", xy=(430, 6), xytext=(450, 22),
            arrowprops=dict(arrowstyle="->", color="#caa800", lw=2))
ax.text(455, 4, "WEJSCIE", fontsize=9, fontweight="bold", color="#caa800")
# panel przy biurku
panel(90, 300, "WB\npanel\nbiurko")

# ---------- LEGENDA ----------
leg = [
    (C1, "Obwod 1  -  SALON glowne (6 oczek, sciemnialne)"),
    (C2, "Obwod 2  -  COVE / tasma sufitowa (sciemn., CCT)"),
    (C3, "Obwod 3  -  BIAS - tasma za TV"),
    (C4, "Obwod 4  -  AKCENTY sciany TV (3 kierunkowe)"),
    (C5, "Obwod 5  -  BIURO zadaniowe (3 oczka, CCT)"),
    (C6, "Obwod 6  -  PRZEJSCIE / komunikacja (2 oczka)"),
    (C7, "Obwod 7  -  SZAFA - auto (czujnik otwarcia)"),
]
handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor="white",
                  markeredgecolor=c, markeredgewidth=2.6, markersize=13, label=t)
           for c, t in leg]
ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(1.02, 1.0),
          fontsize=10, frameon=True, title="PODZIAL NA OBWODY",
          title_fontsize=11, borderpad=1, labelspacing=1.1)

# panel opis
ax.text(605, 150,
        "PANEL WP (wejscie):\n"
        "  - scena PRACA\n"
        "  - scena FILM\n"
        "  - scena RELAKS\n"
        "  - WYJSCIE (all off)\n\n"
        "PANEL WB (biurko):\n"
        "  - PRACA / STOP\n"
        "  - sciemnianie biura\n\n"
        "+ aplikacja / glos",
        fontsize=9.5, va="top", ha="left",
        bbox=dict(boxstyle="round,pad=0.6", fc="#fff7d6", ec="#caa800"))

ax.set_xlim(-60, 760)
ax.set_ylim(0, 500)
ax.invert_yaxis()
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("PLAN OSWIETLENIA - open space (biuro + salon/TV) + szafa przesuwna",
             fontsize=14, fontweight="bold", pad=14)

plt.tight_layout()
plt.savefig("/home/user/architekt-wnetrz/plan_oswietlenia.png", dpi=130,
            bbox_inches="tight", facecolor="white")
print("saved")
