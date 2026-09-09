#!/usr/bin/env python3
"""Fold round-4 (Grab gap-fill) rows into the existing CSVs, same schema."""
from __future__ import annotations

import csv
from pathlib import Path

from verified_round4_grab import ROWS

HERE = Path(__file__).resolve().parent
DELIVER = HERE.parent
A_PATH = DELIVER / "platform_fundamentals_quarterly.csv"
C_PATH = DELIVER / "announcement_dates.csv"


def gmv_note(r: dict) -> str:
    parts = ["Shopee GMV (e-commerce segment, not Sea's consolidated total revenue)."]
    if r.get("note"):
        parts.append(r["note"])
    parts.append(f"Source: {r['url']}, accessed 2026-08-06.")
    return " ".join(parts)


def rev_note(r: dict) -> str:
    parts = []
    if r.get("note") and "revenue" in r["note"].lower():
        parts.append(r["note"])
    parts.append(f"Sea consolidated GAAP revenue. Source: {r['url']}, accessed 2026-08-06.")
    return " ".join(parts)


def main() -> int:
    a_rows = list(csv.DictReader(A_PATH.open(encoding="utf-8")))
    a_cols = list(a_rows[0].keys())
    keys = {(r["firm"], r["fiscal_quarter"]): r for r in a_rows}

    added = updated = 0
    for r in ROWS:
        key = (r["firm"], r["fq"])
        row = keys.get(key)
        if row is None:
            row = {c: "" for c in a_cols}
            row["firm"], row["fiscal_quarter"] = r["firm"], r["fq"]
            row["reporting_currency"] = "USD"
            a_rows.append(row)
            keys[key] = row
            added += 1
        else:
            updated += 1
        if r.get("gmv_usd_m") is not None:
            row["gmv_usd_m"] = r["gmv_usd_m"]
            row["gmv_usd_m_source"] = gmv_note(r)
        if r.get("rev_usd_m") is not None:
            row["revenue_usd_m"] = r["rev_usd_m"]
            row["revenue_usd_m_source"] = rev_note(r)

    a_rows.sort(key=lambda r: (r["firm"], r["fiscal_quarter"]))
    with A_PATH.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=a_cols)
        w.writeheader()
        w.writerows(a_rows)

    c_rows = list(csv.DictReader(C_PATH.open(encoding="utf-8")))
    c_cols = list(c_rows[0].keys())
    c_keys = {(r["firm"], r["fiscal_quarter"]) for r in c_rows}
    added_c = 0
    for r in ROWS:
        key = (r["firm"], r["fq"])
        if key in c_keys:
            continue
        c_rows.append({
            "firm": r["firm"], "fiscal_quarter": r["fq"],
            "announcement_date": r["date"], "announcement_time": "", "timezone": "",
            "source_url": r["url"],
            "concurrent_guidance": "Y" if str(r.get("guidance", "")).strip().startswith(("Y", "mentioned")) else "N",
            "concurrent_other": r.get("other", ""),
        })
        c_keys.add(key)
        added_c += 1

    c_rows.sort(key=lambda r: (r["firm"], r["fiscal_quarter"]))
    with C_PATH.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=c_cols)
        w.writeheader()
        w.writerows(c_rows)

    print(f"Dataset A: {added} new, {updated} updated -> {len(a_rows)} total")
    print(f"Dataset C: {added_c} new -> {len(c_rows)} total")

    by_firm = {}
    for r in a_rows:
        by_firm.setdefault(r["firm"], [0, 0])
        by_firm[r["firm"]][0] += 1
        if r["gmv_usd_m"]:
            by_firm[r["firm"]][1] += 1
    print("\nGMV/GTV fill by firm (GoTo counted separately -- IDR only, see SOURCES.md):")
    for firm, (total, filled) in sorted(by_firm.items()):
        print(f"  {firm}: {filled}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
