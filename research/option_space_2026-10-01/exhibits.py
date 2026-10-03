"""Draft exhibits, one per story layer (4 Oct 2026). Built only from committed tables; PNGs in exhibits/.
Palette: reference categorical slots 1-2 (blue #2a78d6, orange #eb6834), validated (CVD dE 24.7, normal 33.6, contrast >= 3:1).
Text in neutral ink, never in series colour; every highlighted mark is also named in its label (identity is never colour alone).
Run: python3 exhibits.py"""
import json, pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = pathlib.Path(__file__).parent; OUT = HERE / "exhibits"; OUT.mkdir(exist_ok=True)
BLUE, ORANGE, INK, INK2, GRID, SURF = "#2a78d6", "#eb6834", "#0b0b0b", "#52514e", "#e4e3df", "#ffffff"
GREY = "#a3a29d"   # neutral reference, not a series colour
plt.rcParams.update({"font.size": 10, "axes.edgecolor": GRID, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False, "figure.facecolor": SURF,
                     "axes.facecolor": SURF, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True})


def finish(fig, ax, title, note, name):
    ax.grid(axis="y", visible=False)
    fig.text(0.01, 0.98, title, ha="left", va="top", fontsize=12, fontweight="bold", color=INK)
    fig.text(0.01, -0.03, note, ha="left", va="top", fontsize=8, color=INK2, wrap=True)
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight"); plt.close(fig)


# 1. Inside the app: Indonesia vs 27 foreign platforms (median yearly swing in the platform's cut)
f = pd.read_csv(HERE / "tables/h1_extended_firms.csv")
f["is_idn"] = f.group == "Indonesia"
f = f.sort_values("median_abs").reset_index(drop=True)
fig, ax = plt.subplots(figsize=(7, 8))
ax.barh(f.index, f.median_abs * 100, color=[ORANGE if i else BLUE for i in f.is_idn], height=0.6)
ax.set_yticks(f.index, [n.replace(" e-commerce segment", "").replace(" Retail", "") for n in f.firm], fontsize=7.5)
ax.set_xlabel("Typical yearly swing in the platform's cut (x100, firm median)")
ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=ORANGE), plt.Rectangle((0, 0), 1, 1, color=BLUE)],
          labels=["Indonesia and region (5 firms)", "Abroad (27 firms)"], frameon=False, loc="lower right")
finish(fig, ax, "Inside the app: the cut swings about 3x more in Indonesia",
       "Source: verified filings; h1_extended.py. Firm medians; Indonesia vs abroad p = 0.004 (firm level).", "1_inside_the_app.png")

# 2. Apps vs the nation: two camps of rulers, 2024 growth (official household spending shown as a neutral reference)
g = pd.read_csv(HERE / "tables/consistency_grid_growth.csv", index_col=0)["2024"].dropna()
app_only = {"Bank Indonesia e-commerce", "Momentum Works Indonesia GMV", "e-Conomy Indonesia e-commerce"}
ref = {"Official household spending (nominal)"}
g = g.drop(["GoTo on-demand revenue", "GoTo on-demand GTV", "QRIS payments"], errors="ignore").sort_values()
col = [BLUE if n in app_only else (GREY if n in ref else ORANGE) for n in g.index]
fig, ax = plt.subplots(figsize=(7, 3.8))
ax.barh(range(len(g)), g.values, color=col, height=0.6)
ax.set_yticks(range(len(g)), g.index)
for i, v in enumerate(g.values): ax.text(v + 0.6, i, f"{v:+.1f}%", va="center", fontsize=8.5, color=INK)
ax.set_xlabel("Growth in 2024, each ruler in its own unit")
ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=BLUE), plt.Rectangle((0, 0), 1, 1, color=ORANGE), plt.Rectangle((0, 0), 1, 1, color=GREY)],
          labels=["Sees mainly the apps", "Sees all sellers, parcels or tax receipts", "Reference: official household spending"],
          frameon=False, loc="lower right")
finish(fig, ax, "Apps vs the nation: rulers that see only the apps grow slowest",
       "Source: consistency_grid.py. Parcels are Southeast Asia-wide; digital-services VAT taxes foreign services; QR payments (+187%, mostly in-person) and GoTo (rides and food, not online selling) omitted.", "2_two_camps.png")

# 3. Outside the records: formal firms with neither a website nor online tax filing
c = pd.read_csv(HERE / "tables/wb_crosscountry.csv").sort_values("neither_share")
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.barh(c.country, c.neither_share, color=[ORANGE if x == "Indonesia" else BLUE for x in c.country], height=0.6)
for i, v in enumerate(c.neither_share): ax.text(v + 0.6, i, f"{v:.1f}%", va="center", fontsize=9, color=INK)
ax.set_xlabel("Share of formal firms (5+ employees) with no website and no online tax filing")
finish(fig, ax, "Outside the records: Indonesia leaves the most firms without a digital trail",
       "Source: World Bank Enterprise Surveys (Indonesia 2023 and latest per country); wb_crosscountry.py; weights wmedian.", "3_no_digital_trail.png")

# 4. The state: marketplace tax base under four rulers
t = pd.read_csv(HERE / "tables/tax_base_rulers.csv", index_col=0).sort_values("base_Rp_tn")
fig, ax = plt.subplots(figsize=(7, 3.2))
ax.barh(t.index, t.base_Rp_tn, color=BLUE, height=0.6)
for i, (b, tax) in enumerate(zip(t.base_Rp_tn, t["tax_at_0.5pct_Rp_tn"])):
    ax.text(b + 10, i, f"Rp{b:,.0f}tn  ->  tax at 0.5%: Rp{tax:.1f}tn", va="center", fontsize=8.5, color=INK)
ax.set_xlabel("Marketplace tax base, 2024 (Rp trillion)"); ax.set_xlim(0, t.base_Rp_tn.max() * 1.7)
finish(fig, ax, "The state: the same tax rests on a base that differs about 5x",
       "Source: tax_base_rulers.py. Upper bounds before the Rp500m exemption; the largest is about 0.2% of the 2026 tax target.", "4_tax_base.png")
print(sorted(p.name for p in OUT.glob("*.png")))
