"""Generira slike za docs/objasnjenje_neural_net.md"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parents[1] / "docs" / "slike"
OUT.mkdir(parents=True, exist_ok=True)

BLUE = "#0d47a1"
GREEN = "#2e7d32"
ORANGE = "#ef6c00"
RED = "#c62828"
GRAY = "#616161"
YELLOW = "#fff9c4"


def save(fig, name):
    path = OUT / name
    fig.savefig(path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved:", path.name)


def draw_box(ax, x, y, w, h, text, fc="#e3f2fd", ec=BLUE, fs=11):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor=fc, edgecolor=ec, linewidth=2,
    )
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs, fontweight="bold", color="#212121", wrap=True)


def arrow(ax, x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="-|>", mutation_scale=16, linewidth=2, color=GRAY,
    ))


def img_tok():
    fig, ax = plt.subplots(figsize=(14, 4))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 4)
    ax.axis("off")
    ax.set_title("Neural net — cijeli tok", fontsize=16, fontweight="bold", pad=12)

    boxes = [
        (0.3, 1.5, 2.0, 1.2, "Niz s\nrupama", "#fff3e0", ORANGE),
        (2.8, 1.5, 2.2, 1.2, "11 značajki\npo točki", "#e8f5e9", GREEN),
        (5.5, 2.2, 2.4, 1.0, "TRENING\n(poznate)", "#e3f2fd", BLUE),
        (5.5, 0.6, 2.4, 1.0, "PREDIKCIJA\n(rupe)", "#fce4ec", RED),
        (8.4, 1.5, 2.2, 1.2, "MLP\n11→24→12→1", "#f3e5f5", "#6a1b9a"),
        (11.1, 1.5, 2.4, 1.2, "lin_base +\nkorekcija", "#fffde7", "#f9a825"),
    ]
    for x, y, w, h, t, fc, ec in boxes:
        draw_box(ax, x, y, w, h, t, fc=fc, ec=ec, fs=10)

    arrow(ax, 2.3, 2.1, 2.8, 2.1)
    arrow(ax, 5.0, 2.1, 5.5, 2.7)
    arrow(ax, 5.0, 2.1, 5.5, 1.1)
    arrow(ax, 7.9, 2.7, 8.4, 2.1)
    arrow(ax, 7.9, 1.1, 8.4, 2.1)
    arrow(ax, 10.6, 2.1, 11.1, 2.1)

    ax.text(7.0, 0.1, "Koraci 3–4: jednom   |   Korak 5: za svaku rupu",
            ha="center", fontsize=10, color=GRAY, style="italic")
    save(fig, "nn_tok.png")


def img_arhitektura():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_title("Arhitektura mreže (MLP)", fontsize=16, fontweight="bold", pad=12)

    layers = [
        (1.0, "ULAZ\n11 značajki", 11, "#e3f2fd", BLUE),
        (4.0, "SKRIVENI 1\n24 neurona\ntanh", 24, "#e8f5e9", GREEN),
        (7.0, "SKRIVENI 2\n12 neurona\ntanh", 12, "#fff3e0", ORANGE),
        (10.0, "IZLAZ\n1 broj\n(korekcija)", 1, "#fce4ec", RED),
    ]
    for x, label, n, fc, ec in layers:
        draw_box(ax, x, 4.8, 2.0, 0.9, label, fc=fc, ec=ec, fs=10)
        ys = [1.0 + i * (3.5 / max(n - 1, 1)) for i in range(n)] if n > 1 else [2.75]
        if n > 8:
            ys = [1.0 + i * (3.5 / 7) for i in range(8)]
            ax.text(x + 1.0, 0.5, f"... ukupno {n}", ha="center", fontsize=9, color=GRAY)
        for y in ys:
            circle = plt.Circle((x + 1.0, y), 0.12, color=ec, alpha=0.85)
            ax.add_patch(circle)

    for x in [3.2, 6.2, 9.2]:
        arrow(ax, x, 2.75, x + 0.6, 2.75)

    ax.text(6, 0.2, "Svaki neuron: zbroj(ulaz × težina) + bias  →  tanh  →  dalje",
            ha="center", fontsize=11, color=GRAY)
    save(fig, "nn_arhitektura.png")


def img_11_znacajki():
    fig, ax = plt.subplots(figsize=(13, 5))
    x = [0, 1, 2, 3, 4, 5, 6]
    y = [10, None, None, None, 16, 17, 19]
    y_plot = [10, 11.5, 13, 14.5, 16, 17, 19]

    ax.plot(x, y_plot, "--", color=GRAY, linewidth=1.5, alpha=0.6, label="lin_base (crta)")
    ax.plot([0, 4, 5, 6], [10, 16, 17, 19], "o-", color=BLUE, linewidth=2.5,
            markersize=10, label="poznato")
    ax.axvspan(0.8, 4.2, alpha=0.25, color=YELLOW, label="rupa")

    for xi, yi in [(0, 10), (4, 16)]:
        ax.annotate(f"prev/next\n{yi}°C", (xi, yi), textcoords="offset points",
                     xytext=(0, 14), ha="center", fontsize=10, fontweight="bold", color=BLUE)

    ax.annotate("alpha ≈ 0.33\n(sredina rupe)", (2, 13), fontsize=10, ha="center",
                bbox=dict(boxstyle="round", facecolor="#fff9c4", edgecolor=ORANGE))
    ax.annotate("d_prev=2, d_next=2", (2, 11.2), fontsize=9, ha="center", color=GRAY)

    ax.set_xticks(x)
    ax.set_xticklabels(["i=0", "1\n?", "2\n?", "3\n?", "4", "5", "6"])
    ax.set_ylabel("Temperatura (°C)", fontsize=12)
    ax.set_title("6 gap značajki — što mreža vidi oko rupe", fontsize=14, fontweight="bold")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(8, 21)

    table = (
        "#0 prev_val  #1 next_val  #2 alpha  #3 d_prev  #4 d_next  #5 lin_base\n"
        "+ #6 position  #7-8 sat sin/cos  #9-10 dan sin/cos"
    )
    fig.text(0.5, 0.02, table, ha="center", fontsize=10, color=GRAY,
             bbox=dict(boxstyle="round", facecolor="#f5f5f5"))
    save(fig, "nn_11_znacajki.png")


def img_ucenje():
    fig, ax = plt.subplots(figsize=(12, 4.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4.5)
    ax.axis("off")
    ax.set_title("Jedan korak učenja (ponavlja se 200 epoha)", fontsize=15, fontweight="bold", pad=10)

    steps = [
        (0.4, 1.6, "1. FORWARD\n11 brojeva → mreža\n→ predikcija", "#e3f2fd", BLUE),
        (3.1, 1.6, "2. GREŠKA\npredikcija − cilj\n(koliko crta griješi)", "#fff3e0", ORANGE),
        (5.8, 1.6, "3. BACKPROP\nkako promijeniti\ntežine?", "#e8f5e9", GREEN),
        (8.5, 1.6, "4. ADAM\npametno ažuriraj\ntežine", "#fce4ec", RED),
    ]
    for x, y, t, fc, ec in steps:
        draw_box(ax, x, y, 2.3, 1.4, t, fc=fc, ec=ec, fs=10)
    for x in [2.7, 5.4, 8.1]:
        arrow(ax, x + 0.15, 2.3, x + 0.55, 2.3)

    ax.annotate("", xy=(0.4, 1.3), xytext=(10.5, 1.3),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.5,
                                connectionstyle="arc3,rad=-0.4"))
    ax.text(5.5, 0.5, "ponovi za sve poznate točke (batch od 32)", ha="center",
            fontsize=10, color=GRAY, style="italic")
    save(fig, "nn_ucenje.png")


def img_adam():
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    ax.set_title("Što radi Adam?", fontsize=15, fontweight="bold", pad=10)

    draw_box(ax, 0.5, 1.5, 3.5, 1.5,
             "Obični gradijent\nuvijek isti korak\n→ može preskočiti\nili biti prespor",
             fc="#ffebee", ec=RED, fs=10)
    draw_box(ax, 6.0, 1.5, 3.5, 1.5,
             "Adam\nprilagođava korak\npo svakoj težini\n→ stabilnije učenje",
             fc="#e8f5e9", ec=GREEN, fs=10)
    arrow(ax, 4.0, 2.25, 6.0, 2.25)
    ax.text(5.0, 0.6, "U kodu: nn_adam_step() nakon backprop", ha="center", fontsize=10, color=GRAY)
    save(fig, "nn_adam.png")


def img_vs_stablo():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Isti problem — drugi motor", fontsize=15, fontweight="bold", y=1.02)

    for ax, title, steps, color in [
        (axes[0], "Decision Tree", ["11 značajki", "pitanja DA/NE", "LIST: +1.2", "crta + list"], BLUE),
        (axes[1], "Neural Net", ["11 značajki", "težine × tanh", "izlaz: +1.1", "crta + izlaz"], "#6a1b9a"),
    ]:
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 5)
        ax.axis("off")
        ax.set_title(title, fontsize=13, fontweight="bold", color=color)
        for i, s in enumerate(steps):
            y = 3.8 - i * 1.0
            draw_box(ax, 0.5, y, 3.0, 0.75, s, fc="#f5f5f5", ec=color, fs=11)
            if i < len(steps) - 1:
                arrow(ax, 2.0, y, 2.0, y - 0.25)

    fig.text(0.5, 0.02,
             "Oba: treniraju samo na poznatim  |  predviđaju samo rupe  |  formula: lin_base + korekcija",
             ha="center", fontsize=10, color=GRAY)
    save(fig, "nn_vs_stablo.png")


def img_predikcija():
    fig, ax = plt.subplots(figsize=(11, 4))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 4)
    ax.axis("off")
    ax.set_title("Predikcija za jednu rupu", fontsize=15, fontweight="bold", pad=10)

    draw_box(ax, 0.3, 1.5, 2.2, 1.2, "11 značajki\nrupe", "#e8f5e9", GREEN, fs=10)
    draw_box(ax, 3.0, 1.5, 2.0, 1.2, "mreža\n(forward)", "#f3e5f5", "#6a1b9a", fs=10)
    draw_box(ax, 5.5, 1.5, 1.8, 1.2, "korekcija\n+1.1°C", "#fce4ec", RED, fs=10)
    draw_box(ax, 7.8, 1.5, 1.8, 1.2, "lin_base\n13°C", "#e3f2fd", BLUE, fs=10)
    draw_box(ax, 10.0, 1.5, 0.8, 1.2, "=", "#fff", "#fff", fs=14)
    draw_box(ax, 9.5, 0.2, 2.0, 0.9, "14.1°C", "#fffde7", "#f9a825", fs=12)

    for x in [2.5, 5.0, 7.3, 9.6]:
        arrow(ax, x, 2.1, x + 0.4, 2.1)
    ax.text(8.7, 2.1, "+", fontsize=16, ha="center", va="center", fontweight="bold")
    save(fig, "nn_predikcija.png")


def main():
    print("Generiram slike za neural net dokumentaciju...")
    img_tok()
    img_arhitektura()
    img_11_znacajki()
    img_ucenje()
    img_adam()
    img_vs_stablo()
    img_predikcija()
    print("Gotovo.")


if __name__ == "__main__":
    main()
