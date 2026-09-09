#!/usr/bin/env python3
"""Build the actual analysis panel: firm-quarter GMV/GTV, revenue, ecosystem
ratio (GMV/Revenue -- unit-free, so GoTo's IDR figures are usable directly,
no FX conversion needed), and the announcement date for each quarter that has
one. This is the direct input to the event study below.

Self-contained: reads only from files shipped in this same folder/zip
(platform_fundamentals_quarterly.csv, announcement_dates.csv,
goto_idr_figures.csv). Does not import the round-2/3/4 dev scripts used to
originally source the data -- those were scratch files, not part of the
delivered package, and an earlier version of this script importing them
broke on a from-zip run (ModuleNotFoundError), caught in audit.
"""
from __future__ import annotations

import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
DELIVER = HERE.parent


def main() -> int:
    # Start from the CSV (has GRAB/SEA in USD already)
    a = list(csv.DictReader((DELIVER / "platform_fundamentals_quarterly.csv").open()))
    c = {(r["firm"], r["fiscal_quarter"]): r for r in csv.DictReader((DELIVER / "announcement_dates.csv").open())}

    panel = {}
    for r in a:
        key = (r["firm"], r["fiscal_quarter"])
        if r["gmv_usd_m"] and r["revenue_usd_m"]:
            panel[key] = {
                "firm": r["firm"], "quarter": r["fiscal_quarter"],
                "gmv": float(r["gmv_usd_m"]), "revenue": float(r["revenue_usd_m"]),
                "currency": "USD (millions)",
            }

    # GoTo: IDR figures, in TRILLIONS as GoTo itself reports them -- not
    # millions. An earlier version of the summary-stats table mislabeled
    # this as "millions" while the values were trillions throughout; fixed
    # here by carrying the unit explicitly rather than assuming it downstream.
    for r in csv.DictReader((HERE / "goto_idr_figures.csv").open()):
        key = ("GOTO", r["quarter"])
        panel[key] = {
            "firm": "GOTO", "quarter": r["quarter"],
            "gmv": float(r["gtv_idr_trillion"]), "revenue": float(r["net_revenue_idr_trillion"]),
            "currency": "IDR (trillions)",
        }

    rows = []
    for key, p in sorted(panel.items()):
        ann = c.get(key)
        p["ecosystem_ratio"] = round(p["gmv"] / p["revenue"], 3)
        p["announcement_date"] = ann["announcement_date"] if ann else ""
        p["concurrent_guidance"] = ann["concurrent_guidance"] if ann else ""
        rows.append(p)

    cols = ["firm", "quarter", "gmv", "revenue", "currency", "ecosystem_ratio",
            "announcement_date", "concurrent_guidance"]
    out = HERE / "panel.csv"
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    with_date = [r for r in rows if r["announcement_date"]]
    print(f"panel: {len(rows)} firm-quarters with GMV+revenue")
    print(f"  of which {len(with_date)} also have an announcement date (usable for event study)")
    for f in ("GRAB", "SEA", "GOTO"):
        n = sum(1 for r in with_date if r["firm"] == f)
        print(f"    {f}: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
