#!/usr/bin/env python3
"""Figure 1: Ecosystem Ratio by platform. Issuer-reported pairs solid, constructed series dashed.

Grab's and Shopee's Indonesian ratios equal group ratios by construction, so they are drawn
dashed and grey to keep them visually apart from the issuer-reported main sample."""
import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = sys.argv[1] if len(sys.argv) > 1 else "papers/current/figures/figure1_ecosystem_ratio_timeseries.png"
lv = pd.read_csv("outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_levels.csv")
lv["E"] = (lv.transaction_value - lv.revenue_value) / lv.revenue_value
series = [  # (data label, legend label, constructed?, marker)
    ("Tokopedia e-commerce segment", "Tokopedia", False, "^"),
    ("Blibli 3P Retail", "Blibli (third-party)", False, "D"),
    ("Bukalapak Group", "Bukalapak (Group)", False, "v"),
    ("Grab", "Grab (constructed)", True, "o"),
    ("Shopee", "Shopee (constructed)", True, "s"),
]
plt.rcParams.update({"font.family": "serif", "font.serif": ["Liberation Serif", "Times New Roman", "DejaVu Serif"],
                     "font.size": 11})
fig, ax = plt.subplots(figsize=(11.0, 4.006), dpi=225)
for key, label, constructed, marker in series:
    g = lv[lv.series == key].sort_values("year")
    ax.plot(g.year, g.E, marker=marker, markersize=6, linewidth=1.8 if not constructed else 1.4,
            linestyle="--" if constructed else "-", color="0.55" if constructed else "black",
            markerfacecolor="white" if constructed else "black", label=label)
ax.set_xticks(range(2020, 2026))
ax.set_xlim(2019.7, 2025.3)
ax.set_ylim(0, 200)
ax.set_xlabel("Fiscal year")
ax.set_ylabel("Ecosystem Ratio, E = (V − R) / R")
ax.grid(axis="y", color="0.88", linewidth=0.8)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.13), ncol=5, frameon=False, fontsize=10)
fig.tight_layout()
fig.savefig(out, dpi=225)
print("wrote", out)
