# -*- coding: utf-8 -*-
"""ZBIORCZY plan oswietlenia: oczka + listwy LED razem. Wymiary w cm."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.lines import Line2D

fig, ax = plt.subplots(figsize=(16, 12))
WALL="#2b2b2b"
# oczka
C1="#1f77b4"; C4="#d62728"; C5="#9467bd"; C6="#17becf"; C7o="#7f7f7f"
# listwy
COVE="#2ca02c"; BIAS="#ff7f0e"; SZAF="#7f7f7f"; BIUR="#9467bd"; COKOL="#1f77b4"

# ---------- kontur ----------
ax.add_patch(Rectangle((0,0),493,456, fill=False, lw=4, ec=WALL))
ax.add_patch(Rectangle((0,0),62,264, fill=True, fc="#f4f1ea", ec=WALL, lw=2))
ax.plot([62,62],[10,254], color="#8a7f6a", lw=2.5, ls=(0,(6,4)))
ax.plot([0,62],[264,264], color=WALL, lw=2)
# meble
ax.add_patch(Rectangle((290,2),110,9, fc="#222", ec="#222"))
ax.text(345,26,"TV", ha="center", fontsize=12, fontweight="bold")
ax.add_patch(Rectangle((250,380),200,55, fc="#efeadf", ec="#cbbfa6", lw=1))
ax.text(350,408,"KANAPA", ha="center", va="center", fontsize=9, color="#9a8f78")
ax.add_patch(Rectangle((8,290),58,150, fc="#efeadf", ec="#bcae90", lw=1))
ax.text(150,360,"BIURO", ha="center", fontsize=11, fontweight="bold", color="#bbb")
ax.text(31,150,"SZAFA", ha="center", va="center", fontsize=8, rotation=90, color="#9a8f78")
ax.text(360,210,"SALON", ha="center", fontsize=14, fontweight="bold", color="#ddd", zorder=0)

# ============ LISTWY LED (rysowane pod oczkami) ============
def run(pts,color,lw=8):
    ax.plot([p[0] for p in pts],[p[1] for p in pts], color=color, lw=lw,
            solid_capstyle="round", solid_joinstyle="round", zorder=4, alpha=0.9)
def tag(x,y,t,color,fs=8):
    ax.text(x,y,t, ha="center", va="center", fontsize=fs, color="white",
            fontweight="bold", zorder=7,
            bbox=dict(boxstyle="round,pad=0.22", fc=color, ec="none"))

run([(80,55),(470,55),(470,430),(250,430)], COVE, 9)        # L1 cove
tag(160,55,"L1 COVE ~10 m", COVE)
run([(285,30),(285,8),(405,8),(405,30)], BIAS, 7)            # L2 bias
tag(345,42,"L2 BIAS 3.5 m", BIAS)
run([(16,60),(16,240)], SZAF, 7)                             # L3 szafa
tag(40,250,"L3 2.4 m", SZAF)
run([(12,300),(12,420)], BIUR, 6)                            # L4 biurko
tag(58,455,"L4 biurko 1.5 m", BIUR)
run([(285,372),(285,360),(405,360),(405,372)], COKOL, 6)     # L5 cokol TV
tag(345,352,"L5 cokol TV 3 m", COKOL)

# ============ OCZKA ============
def oczko(x,y,c,s=320,marker="o"):
    ax.scatter(x,y,s=s, facecolors="white", edgecolors=c, lw=2.6, zorder=6)
    ax.scatter(x,y,s=s*0.16, color=c, marker=marker, zorder=7)

SALON_X=[200,320,440]; SALON_Y=[140,290]
for x in SALON_X:
    for y in SALON_Y: oczko(x,y,C1)
for x in [285,345,405]: oczko(x,60,C4,270,">")     # akcenty TV
for y in [300,360,420]: oczko(40,y,C5,270)         # biuro
for x,y in [(120,210),(215,210)]: oczko(x,y,C6,270)# przejscie
for x,y in [(31,80),(31,200)]: oczko(x,y,C7o,250)  # szafa oczka

# ====== OTWOR (przejscie do kuchni) - centralnie OBOK TV + PANELE ======
# otwarte przejscie w GORNEJ scianie, tuz obok TV (z lewej) - ciag komunikacyjny
ax.plot([185,278],[0,0], color="white", lw=8, zorder=3)          # "wyciety" otwor
ax.plot([185,185],[-8,8], color=WALL, lw=3, zorder=3)            # osciezia
ax.plot([278,278],[-8,8], color=WALL, lw=3, zorder=3)
ax.annotate("", xy=(231,50), xytext=(231,-16),
            arrowprops=dict(arrowstyle="->", color="#caa800", lw=2.4), zorder=9)
ax.text(231,-40,"OTWOR  ->  KUCHNIA / KORYTARZ\n(obok TV; dalej drzwi wejsc. do domu)",
        ha="center", va="center", fontsize=8.5, fontweight="bold", color="#caa800")

def panel(x,y,t):
    ax.add_patch(FancyBboxPatch((x,y),66,30, boxstyle="round,pad=2",
                 fc="#fff7d6", ec="#caa800", lw=2, zorder=8))
    ax.text(x+33,y+15,t, ha="center", va="center", fontsize=8.5,
            fontweight="bold", color="#7a5c00", zorder=9)
panel(185,82,"WP wejscie")      # panel glowny przy otworze (obok TV)
panel(95,300,"WB biurko")       # panel dodatkowy przy biurku

# ============ LEGENDA ============
ocz=[(C1,"Oczka SALON (ob.1) - 6 szt"),
     (C4,"Oczka akcent TV (ob.4) - 3 szt"),
     (C5,"Oczka BIURO (ob.5) - 3 szt"),
     (C6,"Oczka PRZEJSCIE (ob.6) - 2 szt"),
     (C7o,"Oczka SZAFA (ob.7) - 2 szt")]
h1=[Line2D([0],[0],marker="o",color="w",markerfacecolor="white",
    markeredgecolor=c,markeredgewidth=2.4,markersize=11,label=t) for c,t in ocz]
lst=[(COVE,"L1 Cove sufit (ob.2) ~10 m"),
     (BIAS,"L2 Bias za TV (ob.3) 3.5 m"),
     (SZAF,"L3 Tasma szafa (ob.7) 2.4 m"),
     (BIUR,"L4 Tasma biurko (opcja) 1.5 m"),
     (COKOL,"L5 Cokol TV (opcja) 3 m")]
h2=[Line2D([0],[0],color=c,lw=6,label=t) for c,t in lst]
leg1=ax.legend(handles=h1, loc="upper left", bbox_to_anchor=(1.02,1.0),
          fontsize=9.5, frameon=True, title="OCZKA (oprawy punktowe)",
          title_fontsize=10.5, labelspacing=0.9)
ax.add_artist(leg1)
ax.legend(handles=h2, loc="upper left", bbox_to_anchor=(1.02,0.55),
          fontsize=9.5, frameon=True, title="LISTWY LED (tasmy 24V)",
          title_fontsize=10.5, labelspacing=0.9)

ax.text(560,150,
 "RAZEM: 16 oczek + 5 odcinkow tasm LED\n"
 "7 obwodow / sceny: Praca | Film | Relaks | Wyjscie\n"
 "Panele: WP (wejscie) + WB (biurko) + apka/glos\n"
 "Szafa: auto - czujnik otwarcia drzwi",
 fontsize=9, va="top",
 bbox=dict(boxstyle="round,pad=0.6", fc="#f3f7ff", ec="#3a6ea5"))

ax.set_xlim(-40,940); ax.set_ylim(-62,490)
ax.invert_yaxis(); ax.set_aspect("equal"); ax.axis("off")
ax.set_title("ZBIORCZY PLAN OSWIETLENIA - oczka + listwy LED",
             fontsize=15, fontweight="bold", pad=12)
plt.tight_layout()
plt.savefig("/home/user/architekt-wnetrz/plan_zbiorczy.png", dpi=135,
            bbox_inches="tight", facecolor="white")
print("saved")
