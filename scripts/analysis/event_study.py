#!/usr/bin/env python3
"""Event study: does the ecosystem ratio (GMV/Revenue) predict the market's
reaction to earnings announcements? Direct answer to the advisor's third comment --
"investigate whether investors benefit from a larger Invisible Ledger."

Method (market-adjusted model, the simplest defensible one for a 35-firm-
quarter sample -- not enough observations for a proper Fama-French factor
model):
  AR_t   = stock return_t - index return_t
  CAR    = sum(AR) over the event window [-1, +1] around announcement_date

Then: does CAR correlate with the ecosystem ratio level, or with its
quarter-over-quarter change (a "larger ledger" is arguably about growth in
the wedge, not its static level)?

Caveats stated in the output, not hidden in code comments only:
  - n=35 is small; per the advisor's first comment, this is a real but thin panel
  - GoTo's announcement dates are the earnings-call-transcript date in a few
    cases (round 2 notes some of these came from search snippets, not a
    press-release dateline directly) -- imprecision here biases toward
    finding nothing, not toward a false positive
  - Contaminated observations (concurrent_guidance == Y) are flagged and
    reported both included and excluded, reflecting the advisor's request to be able
    to drop them
"""
from __future__ import annotations

import csv
import statistics
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
DELIVER = HERE.parent

INDEX_FOR = {"GRAB": "NASDAQ", "GOTO": "JCI", "SEA": "SPX"}
TICKER_FOR = {"GRAB": "GRAB", "GOTO": "GOTO.JK", "SEA": "SE"}


def load_prices(path: Path, key_col: str) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for r in csv.DictReader(path.open()):
        k = r[key_col]
        out.setdefault(k, {})
        price = r.get("close_adj") or r.get("close")
        if price:
            out[k][r["date"]] = float(price)
    return out


def returns_around(prices: dict[str, float], center: str, window: int = 1) -> list[float]:
    """Daily returns for trading days in [-window, +window] around center."""
    dates = sorted(prices)
    if center not in dates:
        # snap to next available trading day (weekend/holiday announcement)
        later = [d for d in dates if d > center]
        if not later:
            return []
        center = later[0]
    idx = dates.index(center)
    lo, hi = max(0, idx - window), min(len(dates) - 1, idx + window)
    rets = []
    for i in range(max(1, lo), hi + 1):
        p0, p1 = prices[dates[i - 1]], prices[dates[i]]
        if p0:
            rets.append(p1 / p0 - 1)
    return rets


def main() -> int:
    stock_px = load_prices(DELIVER / "market_daily.csv", "ticker")
    idx_px = load_prices(DELIVER / "market_index_daily.csv", "index")

    panel = list(csv.DictReader((HERE / "panel.csv").open()))
    # sort per firm by quarter to compute QoQ change in ecosystem ratio
    panel.sort(key=lambda r: (r["firm"], r["quarter"]))
    by_firm: dict[str, list[dict]] = {}
    for r in panel:
        by_firm.setdefault(r["firm"], []).append(r)

    results = []
    for firm, rows in by_firm.items():
        ticker = TICKER_FOR[firm]
        index = INDEX_FOR[firm]
        for i, r in enumerate(rows):
            date = r["announcement_date"]
            if not date:
                continue
            stock_rets = returns_around(stock_px.get(ticker, {}), date)
            idx_rets = returns_around(idx_px.get(index, {}), date)
            n = min(len(stock_rets), len(idx_rets))
            if n == 0:
                continue
            car = sum(stock_rets[:n]) - sum(idx_rets[:n])
            ratio = float(r["ecosystem_ratio"])
            ratio_prev = float(rows[i - 1]["ecosystem_ratio"]) if i > 0 else None
            ratio_chg = (ratio / ratio_prev - 1) if ratio_prev else None
            results.append({
                "firm": firm, "quarter": r["quarter"], "date": date,
                "car_3day": round(car * 100, 3),
                "ecosystem_ratio": ratio, "ratio_qoq_chg_pct": round(ratio_chg * 100, 2) if ratio_chg is not None else None,
                "contaminated": r["concurrent_guidance"] == "Y",
            })

    out = HERE / "event_study_results.csv"
    cols = ["firm", "quarter", "date", "car_3day", "ecosystem_ratio", "ratio_qoq_chg_pct", "contaminated"]
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(results)

    print(f"event study: {len(results)} observations with a computable 3-day CAR\n")

    def corr(xs, ys):
        if len(xs) < 3:
            return None
        mx, my = statistics.mean(xs), statistics.mean(ys)
        num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        dx = sum((x - mx) ** 2 for x in xs) ** 0.5
        dy = sum((y - my) ** 2 for y in ys) ** 0.5
        return num / (dx * dy) if dx and dy else None

    for label, use_all in (("all observations", True), ("excluding contaminated (guidance changes)", False)):
        subset = results if use_all else [r for r in results if not r["contaminated"]]
        level = [(r["ecosystem_ratio"], r["car_3day"]) for r in subset]
        chg = [(r["ratio_qoq_chg_pct"], r["car_3day"]) for r in subset if r["ratio_qoq_chg_pct"] is not None]
        print(f"--- {label} (n={len(subset)}) ---")
        if level:
            c1 = corr([x for x, _ in level], [y for _, y in level])
            print(f"  corr(ecosystem ratio LEVEL, 3-day CAR) = {c1:.3f}" if c1 is not None else "  n too small")
        if chg:
            c2 = corr([x for x, _ in chg], [y for _, y in chg])
            print(f"  corr(ecosystem ratio QoQ CHANGE %, 3-day CAR) = {c2:.3f}, n={len(chg)}" if c2 is not None else "  n too small")
        print()

    print("mean 3-day CAR by firm:")
    for firm in by_firm:
        rs = [r["car_3day"] for r in results if r["firm"] == firm]
        if rs:
            print(f"  {firm}: mean={statistics.mean(rs):.3f}%  n={len(rs)}  sd={statistics.pstdev(rs):.3f}%" if len(rs) > 1 else f"  {firm}: {rs[0]:.3f}% n=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
