# -*- coding: utf-8 -*-
"""Plan LISTW LED - trasy tasm, dlugosci, zasilacze. Wymiary w cm."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.lines import Line2D

fig, ax = plt.subplots(figsize=(15, 12))
WALL="#2b2b2b"
COVE="#2ca02c"; BIAS="#ff7f0e"; SZAF="#7f7f7f"; BIUR="#9467bd"; COKOL="#1f77b4"

# kontur
ax.add_patch(Rectangle((0,0),493,456, fill=False, lw=4, ec=WALL))
ax.add_patch(Rectangle((0,0),62,264, fill=True, fc="#f4f1ea", ec=WALL, lw=2))
ax.plot([62,62],[10,254], color="#8a7f6a", lw=2.5, ls=(0,(6,4)))
ax.plot([0,62],[264,264], color=WALL, lw=2)
# meble
ax.add_patch(Rectangle((290,2),110,9, fc="#222", ec="#222"))
ax.text(345,24,"TV", ha="center", fontsize=12, fontweight="bold")
ax.add_patch(Rectangle((250,380),200,55, fc="#efeadf", ec="#cbbfa6", lw=1))
ax.text(350,408,"KANAPA", ha="center", va="center", fontsize=9, color="#9a8f78")
ax.add_patch(Rectangle((8,290),58,150, fc="#efeadf", ec="#bcae90", lw=1))
ax.text(150,360,"BIURO", ha="center", fontsize=11, fontweight="bold", color="#aaa")
ax.text(31,150,"SZAFA", ha="center", va="center", fontsize=8, rotation=90, color="#9a8f78")

def run(pts, color, lw=8):
    xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    ax.plot(xs,ys, color=color, lw=lw, solid_capstyle="round",
            solid_joinstyle="round", zorder=5, alpha=0.9)

def lbl(x,y,t,color):
    ax.text(x,y,t, ha="center", va="center", fontsize=9, color="white",
            fontweight="bold", zorder=7,
            bbox=dict(boxstyle="round,pad=0.25", fc=color, ec="none"))

# ---- L1 COVE sufitowy salon (C-ksztalt, ~10 m) ----
cove=[(80,55),(470,55),(470,430),(250,430)]
run(cove, COVE, 9)
lbl(275,42,"L1  COVE sufit  3.9 m", COVE)
lbl(486,240,"3.8 m", COVE)
lbl(360,444,"2.2 m", COVE)

# ---- L2 BIAS za TV (ramka wokol TV, ~3.5 m) ----
bias=[(285,30),(285,8),(405,8),(405,30)]
run(bias, BIAS, 7)
lbl(345,40,"L2  BIAS za TV  ~3.5 m", BIAS)

# ---- L3 SZAFA wewnatrz (~2.4 m) ----
run([(16,60),(16,240)], SZAF, 7)
lbl(40,150,"L3  szafa  2.4 m", SZAF)

# ---- L4 (opcja) listwa nad biurkiem / pod polka (~1.5 m) ----
run([(12,300),(12,420)], BIUR, 6)
lbl(70,455,"L4 (opcja) biurko 1.5 m", BIUR)

# ---- L5 (opcja) cokol zabudowy TV - efekt 'floating' (~3 m) ----
run([(285,372),(285,360),(405,360),(405,372)], COKOL, 6)
lbl(345,352,"L5 (opcja) cokol TV  ~3 m", COKOL)

# ---- ZASILACZE (PSU) ----
def psu(x,y,t):
    ax.add_patch(FancyBboxPatch((x,y),70,30, boxstyle="round,pad=2",
                 fc="#ffe9c7", ec="#e08a00", lw=2, zorder=8))
    ax.text(x+35,y+15,t, ha="center", va="center", fontsize=8,
            fontweight="bold", color="#a85b00", zorder=9)
psu(75,120,"ZASILACZ\nnad szafa")     # cove + szafa
ax.annotate("",xy=(120,130),xytext=(150,130),arrowprops=dict(arrowstyle="->",color="#e08a00"))
psu(410,90,"ZASILACZ\nza TV")          # bias + cokol
ax.text(350,150,"(zasilacze 24V w dostepnym miejscu\n- rewizja / nad szafa / w zabudowie TV)",
        ha="center", fontsize=8, color="#a85b00")

# ---------- TABELA DOBORU ----------
tab=(
"DOBOR TASM LED  (system 24V, profil ALU + dyfuzor)\n"
"--------------------------------------------------\n"
"L1 COVE sufit (ob.2)   ~10 m  | biala CCT/COB 10W/m\n"
"        -> 100W  ->  zasilacz 24V 150W\n\n"
"L2 BIAS za TV (ob.3)   ~3.5 m | RGBW 14W/m\n"
"        -> 50W   ->  zasilacz 24V 75W\n\n"
"L3 SZAFA (ob.7)        ~2.4 m | biala 10W/m + czujnik\n"
"        -> 24W   ->  zasilacz 24V 40W\n\n"
"L4 BIURKO (opcja)      ~1.5 m | biala CCT 10W/m\n"
"L5 COKOL TV (opcja)    ~3.0 m | biala/RGB 10W/m\n"
"        L4+L5 -> ~45W -> wspolny zasilacz 24V 75W\n\n"
"WSKAZOWKI:\n"
" - COB (bez kropek) do cove i miejsc widocznych\n"
" - profil ALU = chlodzenie + rowne swiatlo\n"
" - zasilanie z 2 stron tasmy >5 m (spadek napiecia)\n"
" - cove: 2700-3000K cieplo; biurko 4000K\n"
" - przekroj 2x1.5mm2 od zasilacza, blisko tasm\n"
" - zostaw rewizje do kazdego zasilacza!"
)
ax.text(560,40,tab, fontsize=9, va="top", ha="left", family="monospace",
        bbox=dict(boxstyle="round,pad=0.7", fc="#fff6e6", ec="#e08a00", lw=1.5))

# legenda
leg=[(COVE,"L1 Cove sufit"),(BIAS,"L2 Bias za TV"),(SZAF,"L3 Szafa"),
     (BIUR,"L4 Biurko (opcja)"),(COKOL,"L5 Cokol TV (opcja)")]
h=[Line2D([0],[0],color=c,lw=6,label=t) for c,t in leg]
ax.legend(handles=h, loc="lower left", bbox_to_anchor=(1.02,0.0),
          fontsize=9, frameon=True, title="LISTWY LED", title_fontsize=10)

ax.set_xlim(-40,920); ax.set_ylim(-30,490)
ax.invert_yaxis(); ax.set_aspect("equal"); ax.axis("off")
ax.set_title("LISTWY LED - trasy, dlugosci i zasilacze (24V, profil ALU)",
             fontsize=14, fontweight="bold", pad=12)
plt.tight_layout()
plt.savefig("/home/user/architekt-wnetrz/plan_listwy_led.png", dpi=135,
            bbox_inches="tight", facecolor="white")
print("saved")
