"""Exhibits for the revised story (9 Oct 2026; order follows NARRATIVE_ARC.md). Built only from committed tables; PNGs in exhibits/v2/.
Same visual system as exhibits.py: reference categorical slots 1-2 (blue #2a78d6, orange #eb6834; validated CVD dE 24.7, normal 33.6, contrast >= 3:1)
plus a neutral grey for reference marks. Orange marks the Indonesian or newly surfaced quantity; blue the comparison. Text stays in neutral ink;
every coloured mark is also named in a label or legend. Static figures for the thesis and slides, so there is no hover layer.
Kept from exhibits.py without change: 5_bps_own_answers.png (entry vs already selling; sellers flat) and 6_verdict_2023.png (2023 hinge).
Superseded: exhibits.py figure 1 ("the cut swings about 3x more"), whose title reads as larger price changes; see h1_points_vs_log.py.
Run: python3 exhibits_v2.py"""
import json, pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = pathlib.Path(__file__).parent; OUT = HERE / "exhibits" / "v2"; OUT.mkdir(parents=True, exist_ok=True)
BLUE, ORANGE, INK, INK2, GRID, SURF, GREY = "#2a78d6", "#eb6834", "#0b0b0b", "#52514e", "#e4e3df", "#ffffff", "#a3a29d"
plt.rcParams.update({"font.size": 10, "axes.edgecolor": GRID, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False, "figure.facecolor": SURF,
                     "axes.facecolor": SURF, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True})


def pct(x):
    return f"{int(x + 0.5)}%"   # round half up, as in the text


def save(fig, title, note, name, top=0.88):
    fig.tight_layout(rect=(0, 0, 1, top))
    fig.text(0.01, 0.985, title, ha="left", va="top", fontsize=12, fontweight="bold", color=INK)
    fig.text(0.01, -0.01, note, ha="left", va="top", fontsize=8, color=INK2, wrap=True)
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight"); plt.close(fig)


# 1. The thin slice: same price changes as abroad (in rupiah per 100 sold), much bigger swing relative to what is kept
f = pd.read_csv(HERE / "tables/h1_points_vs_log_firms.csv"); j = json.load(open(HERE / "tables/h1_points_vs_log.json"))
fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6), gridspec_kw={"width_ratios": [1, 1, 1]})
rng = np.random.default_rng(1)
panels = [("share_kept_pct", "What the platform keeps\n(rupiah per 100 sold)", 1, "median_share_kept_pct"),
          ("change_points", "Yearly change in what it keeps\n(rupiah per 100 sold)", 1, "median_yearly_change_points"),
          ("change_log", "Yearly change relative to\nwhat it keeps (%)", 100, "median_yearly_change_log")]
for ax, (col, lab, k, key) in zip(axes, panels):
    for y, grp, c in [(1, "Indonesia", ORANGE), (0, "Foreign", BLUE)]:
        v = f[f.group == grp][col] * k
        ax.scatter(v, y + rng.uniform(-0.12, 0.12, len(v)), s=26, color=c, edgecolor=SURF, linewidth=0.8, zorder=3)
        m = j[key][grp] * k
        ax.plot([m, m], [y - 0.3, y + 0.3], color=INK, linewidth=2, zorder=4)
        ax.text(m, y + 0.36, f"median {m:.1f}", ha="center", va="bottom", fontsize=8.5, color=INK)
    ax.set_yticks([1, 0], ["Indonesia and\nregion (5)", "Abroad (26)"] if col == "share_kept_pct" else ["", ""])
    ax.set_ylim(-0.6, 1.75); ax.set_xlabel(lab); ax.grid(axis="y", visible=False)
axes[0].set_xscale("log"); axes[0].set_xticks([1, 3, 10, 30, 100], ["1", "3", "10", "30", "100"])
save(fig, "Same price changes, much thinner slice: why Indonesian platform revenue swings",
     "Source: issuer filings; h1_points_vs_log.py (exploratory). Each dot is one platform's median over its years. Indonesian marketplaces keep under 2 rupiah in 100; "
     "a typical platform abroad keeps about 17. Their yearly changes in rupiah are about the same (p = 0.65), so relative to the slice the Indonesian change is about three times "
     "as large (p = 0.003). Growth divergence equals the change in the share kept divided by the share kept.", "1_thin_slice.png", top=0.86)

# 2. Tokopedia 2022 -> 2023: net revenue up while transaction value fell (Rp trillion, GoTo 2023 annual report, Note 29)
net22, inc, gross, net23 = 4.030919, 1.298601, 0.845670, 6.175190
fig, ax = plt.subplots(figsize=(6.8, 3.6))
steps = [("2022 net\nrevenue", 0, net22, BLUE), ("Fewer\ndiscounts", net22, inc, ORANGE),
         ("Higher\ngross revenue", net22 + inc, gross, GREY), ("2023 net\nrevenue", 0, net23, BLUE)]
for i, (lab, base, h, c) in enumerate(steps):
    ax.bar(i, h, bottom=base, color=c, width=0.55)
    ax.text(i, base + h + 0.1, f"{h:.2f}" if i in (0, 3) else f"+{h:.2f} ({100 * h / (net23 - net22):.1f}%)", ha="center", fontsize=9, color=INK)
ax.set_xticks(range(4), [s[0] for s in steps]); ax.set_ylim(0, 7.2); ax.set_ylabel("Rp trillion"); ax.grid(axis="x", visible=False)
save(fig, "Tokopedia 2023: revenue up 53% while buying on it fell 9%",
     "Source: GoTo 2023 annual report (operating metrics; Note 29, third-party e-commerce segment, 2022 restated). Net revenue = gross revenue minus customer incentives; "
     "incentives fell from Rp4.11tn to Rp2.81tn. Shares of the net revenue increase at full precision (independent review, measurement_checks.py). "
     "Transaction value fell 8.9%.", "2_tokopedia_2023.png")

# 3. Who the extra sellers are: share among sellers beyond the normal year-to-year change vs share of the 2022 count
p = json.load(open(HERE / "tables/bps_newly_counted_profile.json"))["profile"]
pick = [("Business opened before 2010", ["business opened"], ["before 2010"]),
        ("Started selling online 6+ years\nafter opening", ["years between opening and selling online"], ["6 or more"]),
        ("Owner aged 50 or over", ["owner age"], ["50 and over"]),
        ("Outside Java", ["island"], ["outside Java"]),
        ("Food and drink, or making goods", ["sector"], ["food and lodging", "making goods"]),
        ("Owner schooled to high school\nor less", ["owner education (2023 survey codes inferred)"], ["high school or less"])]
rows = [(lab, sum(p[g[0]][k]["share_of_beyond_normal_pct"] for k in ks), sum(p[g[0]][k]["share_of_2022_count_pct"] for k in ks)) for lab, g, ks in pick]
fig, ax = plt.subplots(figsize=(7.4, 4.2))
y = np.arange(len(rows))[::-1]
ax.barh(y + 0.18, [r[1] for r in rows], height=0.34, color=ORANGE, label="Extra sellers counted in 2023")
ax.barh(y - 0.18, [r[2] for r in rows], height=0.34, color=BLUE, label="All sellers in the 2022 count")
for yy, r in zip(y, rows):
    ax.text(r[1] + 1, yy + 0.18, pct(r[1]), va="center", fontsize=8.5, color=INK)
    ax.text(r[2] + 1, yy - 0.18, pct(r[2]), va="center", fontsize=8.5, color=INK)
ax.set_yticks(y, [r[0] for r in rows]); ax.set_xlim(0, 100); ax.set_xlabel("Share of each group (%)"); ax.grid(axis="y", visible=False)
ax.legend(frameon=False, loc="upper right", fontsize=8.5)
save(fig, "Who the extra 2023 sellers were: long-running small businesses, not start-ups",
     "Source: BPS e-commerce survey microdata (2021, 2023 and 2024 files), weighted; bps_newly_counted_profile.py (exploratory). Extra sellers: pre-2023 sellers in the 2023 survey "
     "beyond each group's normal yearly change (taken from the 2020-22 surveys), about 450 thousand. The surveys do not follow individual businesses. "
     "Education codes for the 2024 file are inferred. Almost all of the extra count sells only through chat and social media.", "3_who_they_are.png")

# 4. Not sellers back from a break: the rise is in sellers who sold online every month
r = json.load(open(HERE / "tables/bps_returning_check.json")); k = [x for x in r if x != "change_k"]
fig, ax = plt.subplots(figsize=(6.6, 3.2))
cats = ["Sold online every month", "Sold online part of the year"]
v0 = [r[k[0]]["all_12_months_k"], r[k[0]]["part_year_k"]]; v1 = [r[k[1]]["all_12_months_k"], r[k[1]]["part_year_k"]]
yy = np.array([1, 0])
ax.barh(yy + 0.18, [v / 1e3 for v in v1], height=0.34, color=ORANGE, label="2023 survey")
ax.barh(yy - 0.18, [v / 1e3 for v in v0], height=0.34, color=BLUE, label="2022 survey")
for y_, a, b in zip(yy, v1, v0):
    ax.text(a / 1e3 + 0.04, y_ + 0.18, f"{a / 1e3:.2f}m", va="center", fontsize=8.5, color=INK)
    ax.text(b / 1e3 + 0.04, y_ - 0.18, f"{b / 1e3:.2f}m", va="center", fontsize=8.5, color=INK)
ax.set_yticks(yy, cats); ax.set_xlim(0, 3.4); ax.set_xlabel("Sellers who started before the survey year (million)"); ax.grid(axis="y", visible=False)
ax.legend(frameon=False, loc="lower right", fontsize=8.5)
save(fig, "The rise is in sellers who sold online all year, not sellers coming back from a break",
     "Source: BPS e-commerce survey microdata, weighted; bps_returning_check.py (exploratory). A seller back from a break in 2022 would usually sell for only part of 2023. "
     "The month question changed format between the two files (a list of months vs twelve yes/no answers).", "4_full_year_sellers.png")

# 5. Who the marketplace tax reaches (share of online sellers, 2023)
t = json.load(open(HERE / "tables/part6_checks.json"))
pay = t["tax_seller_reach_pct"]; mk = t["marketplace_sellers_share_pct"]["2023"]; rec = mk - pay; out = 100 - mk
fig, ax = plt.subplots(figsize=(8.4, 1.9))
left = 0
for w, c in [(pay, ORANGE), (rec, "#f4b394"), (out, GREY)]:
    ax.barh(0, w, left=left, color=c, height=0.5, edgecolor=SURF, linewidth=2); left += w
ax.text(0, 0.33, f"Can be taxed: {pay:.0f}% of online sellers", ha="left", va="bottom", fontsize=9, color=INK)
ax.text(pay, -0.33, f"On record, not taxed: {rec:.0f}%", ha="left", va="top", fontsize=9, color=INK)
ax.text(mk + out / 2, 0, f"Outside the marketplaces: {out:.0f}%", ha="center", va="center", fontsize=9, color=INK)
ax.set_xlim(0, 100); ax.set_ylim(-0.75, 0.75); ax.axis("off")
save(fig, "The marketplace tax can collect from about 1 online seller in 20",
     f"Source: BPS e-commerce survey microdata and publications; PMK 37/2025; part6_checks.py. Can be taxed: marketplace sellers with Rp300m+ a year (upper bound; the exemption is Rp500m). "
     f"On record: every marketplace seller gives a tax number or NIK (Art. 6). Marketplace sellers were {mk:.1f}% of online sellers in 2023 (17.2% in 2024). "
     f"The taxable sellers hold about 17-24% of online sales value (2022). Only {t['off_marketplace_wanting_to_join_pct']:.1f}% of sellers outside the marketplaces want to join one.",
     "5_tax_reach.png", top=0.8)
print(sorted(x.name for x in OUT.glob("*.png")))
