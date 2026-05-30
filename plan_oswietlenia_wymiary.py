# -*- coding: utf-8 -*-
"""Plan oswietlenia - WERSJA WYMIAROWA do trasowania na suficie.
Wszystkie wymiary w cm, mierzone do OSI oczka.
Uklad wsp.: poczatek = lewy gorny rog pokoju, X w prawo, Y w dol."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(15, 12))

C1="#1f77b4"; C3="#ff7f0e"; C4="#d62728"; C5="#9467bd"; C6="#17becf"; C7="#7f7f7f"
WALL="#2b2b2b"; DIM="#c0392b"

# ---------- KONTUR / SCIANY ----------
ax.add_patch(Rectangle((0,0),493,456, fill=False, lw=4, ec=WALL))
ax.add_patch(Rectangle((0,0),62,264, fill=True, fc="#f4f1ea", ec=WALL, lw=2))
ax.plot([62,62],[10,254], color="#8a7f6a", lw=2.5, ls=(0,(6,4)))
ax.plot([0,62],[264,264], color=WALL, lw=2)

# meble (tlo)
ax.add_patch(Rectangle((290,2),110,9, fc="#222", ec="#222"))
ax.text(345,24,"TV", ha="center", fontsize=13, fontweight="bold")
ax.add_patch(Rectangle((250,380),200,55, fc="#efeadf", ec="#cbbf a6".replace(" ",""), lw=1))
ax.text(350,408,"KANAPA", ha="center", va="center", fontsize=10, color="#9a8f78")
ax.add_patch(Rectangle((8,290),58,150, fc="#efeadf", ec="#bcae90", lw=1))
ax.text(150,360,"BIURO", ha="center", fontsize=12, fontweight="bold", color="#999")
ax.text(31,150,"SZAFA", ha="center", va="center", fontsize=8, rotation=90, color="#9a8f78")

# ============ OPRAWY ============
SALON_X=[200,320,440]; SALON_Y=[140,290]
AKC_X=[285,345,405];   AKC_Y=60
BIURO_X=40;            BIURO_Y=[300,360,420]
PRZ=[(120,210),(215,210)]
SZAFA=[(31,80),(31,200)]

def oczko(x,y,c,s=300):
    ax.scatter(x,y,s=s, facecolors="white", edgecolors=c, lw=2.6, zorder=6)
    ax.scatter(x,y,s=s*0.16, color=c, zorder=7)

for x in SALON_X:
    for y in SALON_Y: oczko(x,y,C1)
for x in AKC_X: oczko(x,AKC_Y,C4,260)
for y in BIURO_Y: oczko(BIURO_X,y,C5,260)
for x,y in PRZ: oczko(x,y,C6,260)
for x,y in SZAFA: oczko(x,y,C7,240)
ax.plot([293,397],[14,14], color=C3, lw=6, solid_capstyle="round", zorder=4)  # bias
ax.plot([14,14],[60,230], color=C7, lw=4, solid_capstyle="round", zorder=4)   # tasma szafa

# ============ WYMIARY ============
def hdim(x1,x2,y,label,off=0):
    ax.annotate("", xy=(x1,y), xytext=(x2,y),
        arrowprops=dict(arrowstyle="<->", color=DIM, lw=1.4))
    ax.text((x1+x2)/2, y-7+off, label, ha="center", va="bottom",
            fontsize=9.5, color=DIM, fontweight="bold")
def vdim(y1,y2,x,label):
    ax.annotate("", xy=(x,y1), xytext=(x,y2),
        arrowprops=dict(arrowstyle="<->", color=DIM, lw=1.4))
    ax.text(x-6,(y1+y2)/2, label, ha="right", va="center",
            fontsize=9.5, color=DIM, fontweight="bold", rotation=90)
def ext(x1,y1,x2,y2):
    ax.plot([x1,x2],[y1,y2], color=DIM, lw=0.7, ls=(0,(3,3)), zorder=2)

# --- GORNY lancuch: kolumny salonu (X) ---
yt=-55
for x in [0]+SALON_X+[493]: ext(x,0,x,yt+4)
hdim(0,200,yt,"200"); hdim(200,320,yt,"120"); hdim(320,440,yt,"120"); hdim(440,493,yt,"53")
ax.text(246,yt-30,"<-- od LEWEJ sciany do osi oczek (salon) -->",
        ha="center", fontsize=9, color=DIM)

# --- LEWY lancuch: rzedy salonu (Y) ---
xl=-60
for y in [0]+SALON_Y+[456]: ext(0,y,xl+5,y)
vdim(0,140,xl,"140"); vdim(140,290,xl,"150"); vdim(290,456,xl,"166")
ax.text(xl-34,228,"od GORNEJ sciany (TV)", rotation=90, ha="center",
        va="center", fontsize=9, color=DIM)

# --- akcenty TV: odleglosc od sciany + rozstaw ---
ext(285,60,285,0); ext(405,60,405,0)
vdim(0,60,255,"60")
hdim(285,345,95,"60",off=14); hdim(345,405,95,"60",off=14)
ax.text(345,118,"akcenty TV (od sciany TV)", ha="center", fontsize=8, color=DIM)

# --- biuro: od lewej sciany + rozstaw ---
ext(40,300,0,300)
hdim(0,40,300,"40")
vdim(300,360,78,"60"); vdim(360,420,78,"60")
ax.text(96,360,"biuro", rotation=90, ha="center", va="center", fontsize=8, color=DIM)

# --- przejscie ---
ext(120,210,0,210)
hdim(0,120,210,"120"); hdim(120,215,232,"95",off=14)
vdim(0,210,470,"210")
ax.text(478,105,"przejscie\nod TV", fontsize=7.5, color=DIM, va="center")

# --- szafa: os + rozstaw ---
ext(31,80,62,80)
hdim(0,31,80,"31",off=-2)
vdim(0,80,82,"80"); vdim(80,200,82,"120")

# ============ TABELA TRASOWANIA ============
tab = (
"TRASOWANIE OCZEK  (wymiary w cm, do OSI)\n"
"----------------------------------------\n"
"SALON  (ob.1, 6 szt):\n"
"   X od lewej sc.:  200 | 320 | 440\n"
"   Y od gornej (TV): 140 | 290\n"
"   rozstaw: 120 (X) x 150 (Y)\n\n"
"AKCENTY TV (ob.4, 3 szt):\n"
"   60 od sciany TV;  X: 285|345|405 (co 60)\n\n"
"BIAS (ob.3): tasma za TV, ~12 od sc. gornej\n\n"
"BIURO (ob.5, 3 szt):\n"
"   40 od lewej sciany\n"
"   Y: 300 | 360 | 420 (co 60)\n\n"
"PRZEJSCIE (ob.6, 2 szt):\n"
"   Y=210 od TV;  X: 120 i 215\n\n"
"SZAFA (ob.7, 2 szt):\n"
"   w osi 31 od sc.;  Y: 80 i 200\n"
"   + tasma LED wzdluz szafy\n\n"
"ZASADA: oczka min. 30-40 cm od sciany;\n"
"rozstaw ~ 1.0-1.5 x wys. pomieszczenia."
)
ax.text(560, 70, tab, fontsize=9.2, va="top", ha="left", family="monospace",
        bbox=dict(boxstyle="round,pad=0.7", fc="#fbf7e9", ec="#caa800", lw=1.5))

# legenda kolorow (kompakt)
from matplotlib.lines import Line2D
leg=[(C1,"Salon (ob.1)"),(C4,"Akcenty TV (ob.4)"),(C3,"Bias (ob.3)"),
     (C5,"Biuro (ob.5)"),(C6,"Przejscie (ob.6)"),(C7,"Szafa (ob.7)")]
h=[Line2D([0],[0],marker="o",color="w",markerfacecolor="white",
   markeredgecolor=c,markeredgewidth=2.4,markersize=11,label=t) for c,t in leg]
ax.legend(handles=h, loc="lower left", bbox_to_anchor=(1.02,0.0),
          fontsize=9, frameon=True, title="OBWODY", title_fontsize=10)

ax.set_xlim(-110,900)
ax.set_ylim(-100,480)
ax.invert_yaxis()
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("PLAN OSWIETLENIA - WYMIARY DO TRASOWANIA (cm, do osi oczka)",
             fontsize=14, fontweight="bold", pad=12)
plt.tight_layout()
plt.savefig("/home/user/architekt-wnetrz/plan_oswietlenia_wymiary.png",
            dpi=135, bbox_inches="tight", facecolor="white")
print("saved")
