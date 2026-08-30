#!/usr/bin/env python3
"""
Crta dijagram neuronske mreze u stilu ostalih metoda iz rada.

Boje, zaobljeni okviri, tamnoplavi naslov i sivi potpis uskladjeni su s
dijagramima Decision Tree, Random Forest i KNN.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parent.parent
IZLAZ = ROOT / "docs" / "dijagram_neuronska_mreza.png"

NASLOV = "#1B4F72"
NARANCA_F = "#FDEBD0"
NARANCA_B = "#D68910"
PLAVA_F = "#D6EAF8"
PLAVA_B = "#2E86C1"
ZELENA_F = "#D5F5E3"
ZELENA_B = "#1E8449"
SIVA = "#7F8C8D"
CRNA = "#1C2833"


def okvir(ax, x, y, w, h, fill, edge, lw=2.0):
    p = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.012,rounding_size=0.04",
        facecolor=fill, edgecolor=edge, linewidth=lw, zorder=2,
    )
    ax.add_patch(p)
    return p


def strelica(ax, x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="-|>", mutation_scale=14,
        color=CRNA, lw=1.4, zorder=1,
    ))


def neuroni(ax, cx, ys, r, fill, edge):
    for y in ys:
        ax.add_patch(Circle((cx, y), r, facecolor=fill, edgecolor=edge,
                            linewidth=1.4, zorder=3))


def main() -> None:
    # Jednak omjer osi da krugovi ostanu krugovi na sirokom platnu.
    fig, ax = plt.subplots(figsize=(12.6, 6.9), dpi=200)
    ax.set_xlim(0.00, 1.82)
    ax.set_ylim(0.00, 1.00)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    ax.text(0.91, 0.955, "Neuronska mreža imputacija",
            ha="center", va="center", fontsize=18, fontweight="bold",
            color=NASLOV, fontfamily="Calibri")

    # ---- okviri slojeva ----------------------------------------------------
    slojevi = [
        (0.06, 0.18, 0.36, 0.64, NARANCA_F, NARANCA_B),
        (0.52, 0.18, 0.36, 0.64, PLAVA_F, PLAVA_B),
        (0.98, 0.18, 0.36, 0.64, PLAVA_F, PLAVA_B),
        (1.44, 0.30, 0.32, 0.40, ZELENA_F, ZELENA_B),
    ]
    for x, y, w, h, f, e in slojevi:
        okvir(ax, x, y, w, h, f, e)

    strelica(ax, 0.42, 0.50, 0.515, 0.50)
    strelica(ax, 0.88, 0.50, 0.975, 0.50)
    strelica(ax, 1.34, 0.50, 1.435, 0.50)

    # ---- neuroni -----------------------------------------------------------
    r = 0.028
    ulaz_y = [0.70, 0.62, 0.50, 0.38, 0.30]
    h1_y = [0.72, 0.64, 0.56, 0.44, 0.36, 0.28]
    h2_y = [0.66, 0.56, 0.44, 0.34]
    neuroni(ax, 0.24, ulaz_y, r, "#FCF3CF", NARANCA_B)
    neuroni(ax, 0.70, h1_y, r, "#EBF5FB", PLAVA_B)
    neuroni(ax, 1.16, h2_y, r, "#EBF5FB", PLAVA_B)
    neuroni(ax, 1.60, [0.50], 0.036, "#EAFAF1", ZELENA_B)

    ax.text(0.24, 0.50, "···", ha="center", va="center", fontsize=13,
            color=NARANCA_B, fontfamily="Calibri", zorder=4)
    ax.text(0.70, 0.50, "···", ha="center", va="center", fontsize=13,
            color=PLAVA_B, fontfamily="Calibri", zorder=4)
    ax.text(1.16, 0.50, "···", ha="center", va="center", fontsize=13,
            color=PLAVA_B, fontfamily="Calibri", zorder=4)

    veze = [
        (0.268, ulaz_y[0], 0.672, h1_y[0]),
        (0.268, ulaz_y[0], 0.672, h1_y[2]),
        (0.268, ulaz_y[2], 0.672, h1_y[1]),
        (0.268, ulaz_y[2], 0.672, h1_y[4]),
        (0.268, ulaz_y[4], 0.672, h1_y[3]),
        (0.268, ulaz_y[4], 0.672, h1_y[5]),
        (0.728, h1_y[0], 1.132, h2_y[0]),
        (0.728, h1_y[2], 1.132, h2_y[1]),
        (0.728, h1_y[3], 1.132, h2_y[2]),
        (0.728, h1_y[5], 1.132, h2_y[3]),
        (1.188, h2_y[0], 1.564, 0.50),
        (1.188, h2_y[1], 1.564, 0.50),
        (1.188, h2_y[2], 1.564, 0.50),
        (1.188, h2_y[3], 1.564, 0.50),
    ]
    for x1, y1, x2, y2 in veze:
        ax.plot([x1, x2], [y1, y2], color="#5D6D7E", lw=0.7, zorder=1, alpha=0.7)

    ax.text(0.24, 0.775, "Ulaz", ha="center", va="center",
            fontsize=12, fontweight="bold", color=CRNA, fontfamily="Calibri")
    ax.text(0.24, 0.228, "11 značajki", ha="center", va="center",
            fontsize=10, color=CRNA, fontfamily="Calibri")

    ax.text(0.70, 0.775, "Skriveni sloj 1", ha="center", va="center",
            fontsize=12, fontweight="bold", color=CRNA, fontfamily="Calibri")
    ax.text(0.70, 0.228, "24 neurona, tanh", ha="center", va="center",
            fontsize=10, color=CRNA, fontfamily="Calibri")

    ax.text(1.16, 0.775, "Skriveni sloj 2", ha="center", va="center",
            fontsize=12, fontweight="bold", color=CRNA, fontfamily="Calibri")
    ax.text(1.16, 0.228, "12 neurona, tanh", ha="center", va="center",
            fontsize=10, color=CRNA, fontfamily="Calibri")

    ax.text(1.60, 0.655, "Izlaz", ha="center", va="center",
            fontsize=12, fontweight="bold", color=CRNA, fontfamily="Calibri")
    ax.text(1.60, 0.345, "rezidual", ha="center", va="center",
            fontsize=10, color=CRNA, fontfamily="Calibri")

    ax.text(0.91, 0.105,
            "Konačna procjena:  T = linearna baza + rezidual",
            ha="center", va="center", fontsize=11, fontstyle="italic",
            color=SIVA, fontfamily="Calibri")

    IZLAZ.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(IZLAZ, dpi=200, bbox_inches="tight", facecolor="white",
                pad_inches=0.12)
    plt.close(fig)
    print(f"spremljeno: {IZLAZ}")


if __name__ == "__main__":
    main()
