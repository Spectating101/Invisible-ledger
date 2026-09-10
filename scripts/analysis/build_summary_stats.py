#!/usr/bin/env python3
"""Table 1, matching the advisor-supplied sample draft (De-Rong Kong & Tse-Chun Lin's
CryptoPunks paper) structurally:
  Panel A: observation counts by year x category, with row/column totals
  Panel B: N, Mean, Median by category

Mapped onto this thesis: Panel A = firm-quarter counts by year and firm;
Panel B = N/Mean/Median of GMV, revenue, and the ecosystem ratio, by firm.
"""
from __future__ import annotations

import csv
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent

panel = list(csv.DictReader((HERE / "panel.csv").open()))
for r in panel:
    r["year"] = r["quarter"][:4]
    r["gmv"] = float(r["gmv"])
    r["revenue"] = float(r["revenue"])
    r["ecosystem_ratio"] = float(r["ecosystem_ratio"])

firms = ["GRAB", "GOTO", "SEA"]
years = sorted({r["year"] for r in panel})

lines = []
lines.append("Table 1. Summary statistics")
lines.append("")
lines.append(
    "This table reports summary statistics for the firm-quarter panel used in the "
    "empirical analysis. Figures are drawn from each platform's own quarterly earnings "
    "press releases and, for annual/semi-annual periods, SEC XBRL filings (Grab, Sea). "
    "The sample period is 2022Q1 through 2026Q1. Panel A reports the number of "
    "firm-quarter observations by year and by platform. Panel B reports GMV/GTV, "
    "revenue, and the ecosystem ratio (GMV divided by revenue) by platform. Currency "
    "and scale differ by platform -- see the Currency column in Panel B, read literally "
    "(GoTo's figures are in IDR TRILLIONS, Grab's and Sea's in USD millions) -- but the "
    "ecosystem ratio itself is unit-free and therefore comparable across platforms "
    "regardless of currency or scale."
)
lines.append("")
lines.append("Panel A. Number of firm-quarter observations by year and platform")
lines.append("")
header = f"{'Year':<8}" + "".join(f"{f:>8}" for f in firms) + f"{'Total':>8}"
lines.append(header)
totals = {f: 0 for f in firms}
for y in years:
    row = [y]
    yr_total = 0
    counts = {}
    for f in firms:
        n = sum(1 for r in panel if r["year"] == y and r["firm"] == f)
        counts[f] = n
        totals[f] += n
        yr_total += n
    line = f"{y:<8}" + "".join(f"{counts[f]:>8}" for f in firms) + f"{yr_total:>8}"
    lines.append(line)
grand_total = sum(totals.values())
lines.append(f"{'Total':<8}" + "".join(f"{totals[f]:>8}" for f in firms) + f"{grand_total:>8}")
lines.append("")
lines.append("Panel B. GMV/GTV, revenue, and ecosystem ratio by platform")
lines.append("")
lines.append(f"{'Platform':<10}{'N':>5}{'Currency':>18}{'GMV Mean':>14}{'GMV Median':>14}"
             f"{'Rev Mean':>12}{'Rev Median':>12}{'Ratio Mean':>12}{'Ratio Median':>14}")
for f in firms:
    rows = [r for r in panel if r["firm"] == f]
    if not rows:
        continue
    cur = rows[0]["currency"]
    gmv = [r["gmv"] for r in rows]
    rev = [r["revenue"] for r in rows]
    ratio = [r["ecosystem_ratio"] for r in rows]
    lines.append(
        f"{f:<10}{len(rows):>5}{cur:>18}{statistics.mean(gmv):>14,.1f}{statistics.median(gmv):>14,.1f}"
        f"{statistics.mean(rev):>12,.1f}{statistics.median(rev):>12,.1f}"
        f"{statistics.mean(ratio):>12.2f}{statistics.median(ratio):>14.2f}"
    )
lines.append("")
lines.append(
    "Note: GMV and revenue scale differs by platform -- read the Currency column "
    "literally, do not assume millions throughout (GoTo is trillions; Grab and Sea "
    "are millions). Grab's GMV figures use the 'On-Demand GMV' "
    "(mobility segment) definition in 2024Q1 onward and 'Total GMV' in 2022-2023; "
    "the two appear to be the same underlying scope under different labels, but this "
    "is inferred from one release's own wording, not independently confirmed across "
    "the full sample (see SOURCES.md). Sea's figures are Shopee-segment GMV against "
    "Sea's consolidated revenue (which also includes Garena and Monee), so Sea's "
    "ecosystem ratio is not on a like-for-like segment basis with Grab's or GoTo's, "
    "both of which pair segment/group GMV with the matching segment/group revenue."
)

text = "\n".join(lines)
(HERE / "table1_summary_statistics.txt").write_text(text)
print(text)
