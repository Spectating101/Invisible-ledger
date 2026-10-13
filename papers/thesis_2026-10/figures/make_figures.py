"""Figures for Chapter 5 of the thesis (13 Oct 2026). Built only from committed tables; no licensed data are read.
Palette: reference categorical slots 1 (blue #2a78d6) and 2 (orange #eb6834), validated on a white surface (CVD dE 24.7, normal 33.6, contrast >= 3:1),
plus neutral grey. Colour follows the entity in every figure: blue = what the Indonesian-side comparison group or fees stand for is NOT fixed by colour alone;
every mark is also named by a label or legend. Text is neutral ink. Run from the repository root: python3 papers/thesis_2026-10/figures/make_figures.py"""
import json, pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[3]
T = ROOT / "research/option_space_2026-10-01/tables"
OUT = pathlib.Path(__file__).resolve().parent
BLUE, ORANGE, GREY, INK, INK2, GRID = "#2a78d6", "#eb6834", "#a3a29d", "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({"font.size": 9, "font.family": "DejaVu Sans", "axes.edgecolor": GRID, "axes.labelcolor": INK2, "xtick.color": INK2,
                     "ytick.color": INK, "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
                     "figure.facecolor": "white", "axes.facecolor": "white", "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.axisbelow": True, "savefig.dpi": 300})

def save(fig, name):
    fig.savefig(OUT / name, bbox_inches="tight", facecolor="white"); plt.close(fig)

# ---- Figure 5.1: the thin slice -------------------------------------------------------------------------------------------------------
f = pd.read_csv(T / "h1_points_vs_log_firms.csv")
f["change_pct"] = 100 * f.change_log
rng = np.random.default_rng(7)
fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.7), sharey=True)
panels = [("share_kept_pct", "What the platform keeps\n(percent of each sale)", True), ("change_points", "Yearly change in what it keeps\n(percentage points)", False),
          ("change_pct", "Yearly change relative to\nwhat it keeps (percent)", False)]
rows = [("Indonesian and regional (5)", f[f.group == "Indonesia"], ORANGE, 1), ("Foreign (26)", f[f.group == "Foreign"], BLUE, 0)]
for ax, (col, lab, logx) in zip(axes, panels):
    for name, d, c, y in rows:
        jit = y + rng.uniform(-0.16, 0.16, len(d))
        ax.scatter(d[col], jit, s=22, color=c, edgecolor="white", linewidth=0.8, zorder=3)
        m = d[col].median()
        ax.plot([m, m], [y - 0.32, y + 0.32], color=INK, lw=2, zorder=4)
        ax.text(m, y + 0.38, f"median {m:.1f}", ha="center", va="bottom", fontsize=8, color=INK)
    if logx: ax.set_xscale("log"); ax.set_xticks([1, 3, 10, 30, 100]); ax.set_xticklabels(["1", "3", "10", "30", "100"])
    ax.set_xlabel(lab); ax.set_ylim(-0.6, 1.8); ax.set_yticks([0, 1]); ax.tick_params(axis="y", length=0); ax.grid(axis="y", visible=False)
axes[0].set_yticklabels(["Foreign (26)", "Indonesian and\nregional (5)"])
fig.tight_layout(); save(fig, "fig5_1_thin_slice.png")

# ---- Figure 5.2: Tokopedia, two ways to split the rise ---------------------------------------------------------------------------------
s = pd.read_csv(T / "tokopedia_segment.csv", index_col=0)
dg = s.loc[2023] - s.loc[2022]
inc_share, gross_share = -dg.incentives / dg.net * 100, dg.gross / dg.net * 100
g = pd.read_csv(T / "growth_decomposition.csv"); g = g[(g.firm == "Tokopedia")].iloc[0]
vol, fee, dis = 100 * g.share_from_volume, 100 * g.share_from_fee, 100 * g.share_from_discount_cut
fig, (a, b) = plt.subplots(1, 2, figsize=(7.2, 2.5), gridspec_kw={"width_ratios": [1, 1.25]})
a.barh([1, 0], [inc_share, gross_share], color=[ORANGE, BLUE], height=0.5, zorder=3)
for y, v in zip([1, 0], [inc_share, gross_share]): a.text(v + 1.5, y, f"{v:.1f}", va="center", color=INK)
a.set_yticks([1, 0]); a.set_yticklabels(["Lower incentives", "Higher gross fees"]); a.set_xlim(0, 80); a.set_xlabel("Share of the extra net revenue (percent)")
a.set_title("By lines of the accounts", fontsize=9, color=INK, loc="left", fontweight="bold")
cols = [GREY, BLUE, ORANGE]; vals = [vol, fee, dis]; labs = ["More commerce", "Higher fees", "Lower incentives"]
b.barh([2, 1, 0], vals, color=cols, height=0.5, zorder=3)
for y, v in zip([2, 1, 0], vals): b.text(v + (2 if v > 0 else -2), y, f"{v:.0f}".replace("-", "−"), va="center", ha="left" if v > 0 else "right", color=INK)
b.axvline(0, color=INK2, lw=0.8, zorder=4); b.set_yticks([2, 1, 0]); b.set_yticklabels(labs); b.set_xlim(-40, 95)
b.set_xlabel("Share of the growth of revenue (percent)"); b.set_title("Per unit of transaction value", fontsize=9, color=INK, loc="left", fontweight="bold")
for ax in (a, b): ax.grid(axis="y", visible=False); ax.tick_params(axis="y", length=0)
fig.tight_layout(); save(fig, "fig5_2_tokopedia_two_views.png")

# ---- Figure 5.3: 2023 growth, each measure in its own unit ----------------------------------------------------------------------------
items = [("Household spending", 9.4, GREY, "Reference"), ("Tokopedia transaction value", -8.9, BLUE, "Buying through platforms"),
         ("GoTo on-demand transaction value", -10.5, BLUE, "Buying through platforms"), ("Bank Indonesia e-commerce", -4.7, BLUE, "Buying through platforms"),
         ("Momentum Works marketplace estimate", 3.5, BLUE, "Buying through platforms"), ("Bukalapak transaction value", 6.9, BLUE, "Buying through platforms"),
         ("Blibli third-party retail transaction value", 34.7, BLUE, "Buying through platforms"), ("Tokopedia revenue", 53.2, ORANGE, "Figures that described a boom"),
         ("BPS e-commerce value", 40.6, ORANGE, "Figures that described a boom"), ("BPS online sellers (count)", 27.4, ORANGE, "Figures that described a boom")]
order = [i for i in items if i[3] == "Figures that described a boom"] + [items[0]] + sorted([i for i in items if i[3] == "Buying through platforms"], key=lambda t: -t[1])
order = sorted(order[:3], key=lambda t: -t[1]) + order[3:]
fig, ax = plt.subplots(figsize=(7.2, 3.9))
ys = np.arange(len(order))[::-1]
ax.barh(ys, [o[1] for o in order], color=[o[2] for o in order], height=0.62, zorder=3)
for y, o in zip(ys, order): ax.text(o[1] + (1.0 if o[1] >= 0 else -1.0), y, f"{o[1]:+.1f}".replace("-", "−"), va="center", ha="left" if o[1] >= 0 else "right", color=INK, fontsize=8.5)
ax.axvline(0, color=INK2, lw=0.9, zorder=4); ax.set_yticks(ys); ax.set_yticklabels([o[0] for o in order]); ax.tick_params(axis="y", length=0)
ax.set_xlim(-24, 62); ax.set_xlabel("Growth in 2023 (percent); each measure in its own unit"); ax.grid(axis="y", visible=False)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=ORANGE, label="Figures that described a boom"), Patch(color=GREY, label="Reference"), Patch(color=BLUE, label="Buying through platforms")],
          loc="lower right", frameon=False, fontsize=8.5)
fig.tight_layout(); save(fig, "fig5_3_growth_2023.png")

# ---- Figure 5.4: who the extra sellers were ------------------------------------------------------------------------------------------
p = json.load(open(T / "bps_newly_counted_profile.json"))["profile"]
sec = p["sector"]
groups = [("Business opened before 2010", p["business opened"]["before 2010"]["share_of_2022_count_pct"], p["business opened"]["before 2010"]["share_of_beyond_normal_pct"]),
          ("Owner aged 50 or over", p["owner age"]["50 and over"]["share_of_2022_count_pct"], p["owner age"]["50 and over"]["share_of_beyond_normal_pct"]),
          ("Outside Java", p["island"]["outside Java"]["share_of_2022_count_pct"], p["island"]["outside Java"]["share_of_beyond_normal_pct"]),
          ("Food and lodging, or making goods", sec["food and lodging"]["share_of_2022_count_pct"] + sec["making goods"]["share_of_2022_count_pct"],
           sec["food and lodging"]["share_of_beyond_normal_pct"] + sec["making goods"]["share_of_beyond_normal_pct"])]
fig, ax = plt.subplots(figsize=(7.2, 2.9)); y0 = np.arange(len(groups))[::-1]; h = 0.34
ax.barh(y0 + h / 2, [g_[2] for g_ in groups], height=h, color=ORANGE, zorder=3, label="Share of the extra sellers counted in 2023")
ax.barh(y0 - h / 2, [g_[1] for g_ in groups], height=h, color=BLUE, zorder=3, label="Share of all sellers in the 2022 count")
for y, g_ in zip(y0, groups):
    ax.text(g_[2] + 1, y + h / 2, f"{g_[2]:.1f}", va="center", color=INK, fontsize=8.5); ax.text(g_[1] + 1, y - h / 2, f"{g_[1]:.1f}", va="center", color=INK, fontsize=8.5)
ax.set_yticks(y0); ax.set_yticklabels([g_[0] for g_ in groups]); ax.tick_params(axis="y", length=0); ax.grid(axis="y", visible=False)
ax.set_xlim(0, 70); ax.set_xlabel("Percent of each group of sellers"); ax.legend(loc="lower left", bbox_to_anchor=(-0.02, 1.0), ncol=1, frameon=False, fontsize=8.5)
fig.tight_layout(); save(fig, "fig5_4_extra_sellers.png")

# ---- Figure 5.5: marketplace use and financial statements --------------------------------------------------------------------------------
d = json.load(open(T / "bps_descriptives.json"))
yrs_m = [2020, 2022, 2023, 2024]; mk = [d["marketplace_share"]["2020"], d["marketplace_share"]["2022"], d["marketplace_share"]["2023"], d["marketplace_share"]["2024_published"]]
yrs_b = [2020, 2022, 2023]; bk = [d["books_share"]["2020"], d["books_share"]["2022"], d["books_share"]["2023"]]
fig, ax = plt.subplots(figsize=(6.2, 2.9))
ax.plot(yrs_m, mk, color=BLUE, lw=2, marker="o", ms=7, mec="white", mew=1.5, zorder=3, label="Sellers who use a marketplace")
ax.plot(yrs_b, bk, color=ORANGE, lw=2, marker="o", ms=7, mec="white", mew=1.5, zorder=3, label="Sellers who keep complete financial statements")
for x, v in zip(yrs_m, mk):
    up = x == 2023
    ax.text(x, v + (0.8 if up else -0.8), f"{v:.1f}", ha="center", va="bottom" if up else "top", color=INK, fontsize=8.5)
for x, v in zip(yrs_b, bk):
    down = x == 2023
    ax.text(x, v + (-0.8 if down else 0.8), f"{v:.1f}", ha="center", va="top" if down else "bottom", color=INK, fontsize=8.5)
ax.set_xticks(yrs_m); ax.set_ylim(10, 28); ax.set_ylabel("Percent of online sellers"); ax.legend(loc="upper right", frameon=False, fontsize=8.5)
ax.grid(axis="x", visible=False)
fig.tight_layout(); save(fig, "fig5_5_marketplace_and_records.png")
print("ok")
