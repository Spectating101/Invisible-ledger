#!/usr/bin/env python3
"""Fold round-2 verified quarters into the existing four CSVs, in place --
same schema, no parallel files, per the handoff's format rule 1."""
from __future__ import annotations

import csv
from pathlib import Path

from verified_round2 import ROWS

HERE = Path(__file__).resolve().parent
DELIVER = HERE.parent
A_PATH = DELIVER / "platform_fundamentals_quarterly.csv"
C_PATH = DELIVER / "announcement_dates.csv"


def gtv_note(r: dict) -> str:
    parts = []
    if r["firm"] == "GOTO":
        parts.append(f"Total Group GTV, Rp{r['gtv_idr_t']}T (no in-release USD unless noted).")
    elif r["firm"] == "GRAB":
        parts.append("On-Demand GMV (mobility segment only, not total Group GTV).")
    elif r["firm"] == "SEA":
        parts.append("Shopee GMV (e-commerce segment, not Sea's consolidated total revenue).")
    if r.get("note"):
        parts.append(r["note"])
    parts.append(f"Source: {r['url']}, accessed 2026-08-06.")
    return " ".join(parts)


def revenue_note(r: dict) -> str:
    parts = []
    if r["firm"] == "GOTO":
        bits = []
        if r.get("rev_gross_idr_t") is not None:
            bits.append(f"gross Rp{r['rev_gross_idr_t']}T")
        if r.get("rev_net_idr_t") is not None:
            bits.append(f"net Rp{r['rev_net_idr_t']}T")
        if r.get("rev_net_usd_m") is not None:
            bits.append(f"net ${r['rev_net_usd_m']}M as stated in release")
        parts.append("; ".join(bits) if bits else "not disclosed in this release")
    if r.get("note"):
        parts.append(r["note"])
    parts.append(f"Source: {r['url']}, accessed 2026-08-06.")
    return " ".join(parts)


def main() -> int:
    a_rows = list(csv.DictReader(A_PATH.open(encoding="utf-8")))
    a_cols = list(a_rows[0].keys())
    existing_keys = {(r["firm"], r["fiscal_quarter"]) for r in a_rows}

    added_a = updated_a = 0
    for r in ROWS:
        key = (r["firm"], r["fq"])
        row = None
        for existing in a_rows:
            if (existing["firm"], existing["fiscal_quarter"]) == key:
                row = existing
                updated_a += 1
                break
        if row is None:
            row = {c: "" for c in a_cols}
            row["firm"] = r["firm"]
            row["fiscal_quarter"] = r["fq"]
            row["reporting_currency"] = "IDR" if r["firm"] == "GOTO" else "USD"
            a_rows.append(row)
            existing_keys.add(key)
            added_a += 1

        # GMV / GTV
        if r["firm"] == "GOTO":
            row["gmv_usd_m"] = ""  # no honest USD conversion available for most quarters
        elif r.get("gmv_usd_m") is not None:
            row["gmv_usd_m"] = r["gmv_usd_m"]
        row["gmv_usd_m_source"] = gtv_note(r)

        # Revenue
        if r["firm"] == "GOTO":
            row["revenue_usd_m"] = r.get("rev_net_usd_m") or ""
        elif r.get("rev_usd_m") is not None:
            row["revenue_usd_m"] = r["rev_usd_m"]
        row["revenue_usd_m_source"] = revenue_note(r)

    a_rows.sort(key=lambda r: (r["firm"], r["fiscal_quarter"]))
    with A_PATH.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=a_cols)
        w.writeheader()
        w.writerows(a_rows)

    # Dataset C
    c_rows = list(csv.DictReader(C_PATH.open(encoding="utf-8")))
    c_cols = list(c_rows[0].keys()) if c_rows else [
        "firm", "fiscal_quarter", "announcement_date", "announcement_time",
        "timezone", "source_url", "concurrent_guidance", "concurrent_other",
    ]
    c_existing = {(r["firm"], r["fiscal_quarter"]) for r in c_rows}
    added_c = 0
    for r in ROWS:
        key = (r["firm"], r["fq"])
        if key in c_existing:
            continue
        c_rows.append({
            "firm": r["firm"],
            "fiscal_quarter": r["fq"],
            "announcement_date": r["date"],
            "announcement_time": "",
            "timezone": "",
            "source_url": r["url"],
            "concurrent_guidance": "Y" if str(r.get("guidance", "")).strip().startswith(("Y", "mentioned")) else "N",
            "concurrent_other": r.get("other", ""),
        })
        c_existing.add(key)
        added_c += 1

    c_rows.sort(key=lambda r: (r["firm"], r["fiscal_quarter"]))
    with C_PATH.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=c_cols)
        w.writeheader()
        w.writerows(c_rows)

    print(f"Dataset A: {added_a} new rows, {updated_a} existing rows updated -> {len(a_rows)} total")
    print(f"Dataset C: {added_c} new rows -> {len(c_rows)} total")

    by_firm_a = {}
    for r in a_rows:
        by_firm_a.setdefault(r["firm"], [0, 0])
        by_firm_a[r["firm"]][0] += 1
        if r["gmv_usd_m"]:
            by_firm_a[r["firm"]][1] += 1
    print("\nGMV fill rate by firm:")
    for firm, (total, filled) in sorted(by_firm_a.items()):
        print(f"  {firm}: {filled}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
