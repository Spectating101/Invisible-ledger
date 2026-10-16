"""Figure 3.1 of the thesis (draft, 15 Oct 2026): the three nested quantities and the two links tested by H1 and H2.
Illustrative only, not to scale. Same palette and ink as make_figures.py. Run from the repository root:
python3 papers/thesis_2026-10/figures/make_fig3_1.py"""
import pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

OUT = pathlib.Path(__file__).resolve().parent
BLUE, ORANGE, INK, INK2 = "#2a78d6", "#eb6834", "#0b0b0b", "#52514e"
plt.rcParams.update({"font.size": 9, "font.family": "DejaVu Sans", "savefig.dpi": 300})

fig, ax = plt.subplots(figsize=(7.2, 3.9))
ax.set_xlim(0, 13.2); ax.set_ylim(0, 7); ax.set_aspect("equal"); ax.axis("off")
# circles share a bottom point so each sits inside the next
base = 0.4
for r, face, edge, lw in [(3.2, "#eef4fc", BLUE, 1.6), (2.0, "#dbe8fa", BLUE, 1.6), (0.9, "#fbe3d9", ORANGE, 1.8)]:
    ax.add_patch(Circle((3.6, base + r), r, facecolor=face, edgecolor=edge, linewidth=lw))
ax.text(3.6, base + 2 * 3.2 - 0.45, "All online commerce", ha="center", va="top", fontsize=10, fontweight="bold", color=INK)
ax.text(3.6, base + 2 * 3.2 - 0.85, "every channel, including chat\nand social media", ha="center", va="top", fontsize=8, color=INK2)
ax.text(3.6, base + 2 * 2.0 - 0.35, "Platform commerce", ha="center", va="top", fontsize=10, fontweight="bold", color=INK)
ax.text(3.6, base + 2 * 2.0 - 0.72, "transaction value, V", ha="center", va="top", fontsize=8, color=INK2)
ax.text(3.6, base + 0.9 + 0.12, "Revenue", ha="center", va="center", fontsize=9.5, fontweight="bold", color=INK)
ax.text(3.6, base + 0.9 - 0.3, "R", ha="center", va="center", fontsize=8, color=INK2)
ax.text(3.6, base + 2.45, "invisible wedge W = V − R", ha="center", va="center", fontsize=8, color=INK2, style="italic")

def link(y_from, y_to, label, sub, y_text):
    ax.add_patch(FancyArrowPatch((7.3, y_from), (7.3, y_to), arrowstyle="<->", mutation_scale=12, color=INK, lw=1.2))
    ax.plot([3.8, 7.3], [y_from, y_from], color=INK2, lw=0.6, ls=":")
    ax.plot([3.8, 7.3], [y_to, y_to], color=INK2, lw=0.6, ls=":")
    ax.text(7.55, y_text + 0.2, label, ha="left", va="center", fontsize=10, fontweight="bold", color=INK)
    ax.text(7.55, y_text - 0.3, sub, ha="left", va="center", fontsize=8, color=INK2)

link(base + 1.8, base + 4.0, "H1, the inner link", "Does revenue grow in proportion\nto transaction value?", base + 2.75)
link(base + 4.0, base + 6.4, "H2, the outer link", "Does national online growth come\nmainly from more businesses?", base + 5.2)
fig.savefig(OUT / "fig3_1_two_links.png", bbox_inches="tight", facecolor="white"); plt.close(fig)
