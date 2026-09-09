#!/usr/bin/env python3
"""Recompute the event-study data from the preserved daily price files.

This is a replacement for the legacy script's missing ``market_data/*.csv``
dependency.  It reads the project-preserved combined stock and benchmark files,
uses the reviewed event-session ledger, and produces only unfiltered all-event
statistics while contamination classifications remain unresolved.  It does not
overwrite any legacy CAR file or manuscript output.

The event-study design is market-adjusted CAR[-1,+1]: stock return minus the
matched benchmark return for each session, summed over the three-session window.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "07_EVENT_AND_MARKET"
OUT = DATA / "recomputed_from_preserved_prices"

PANEL = DATA / "clean_event_panel_accounting.csv"
EVENTS = DATA / "event_session_ledger_REVIEWED.csv"
CONTAMINATION = DATA / "contamination_ledger_REVIEWED.csv"
STOCKS = DATA / "market_daily.csv"
INDICES = DATA / "market_index_daily.csv"

MARKETS = {
    "Grab": ("GRAB", "NASDAQ"),
    "Sea": ("SE", "SPX"),
    "GoTo": ("GOTO.JK", "JCI"),
}


def load_stock(ticker: str) -> pd.DataFrame:
    frame = pd.read_csv(STOCKS)
    frame = frame.loc[frame["ticker"].eq(ticker), ["date", "close_adj"]].copy()
    frame["date"] = pd.to_datetime(frame["date"]).dt.normalize()
    frame = frame.dropna().drop_duplicates("date").sort_values("date")
    frame["stock_return"] = frame["close_adj"].pct_change()
    return frame


def load_index(index: str) -> pd.DataFrame:
    frame = pd.read_csv(INDICES)
    frame = frame.loc[frame["index"].eq(index), ["date", "close"]].copy()
    frame["date"] = pd.to_datetime(frame["date"]).dt.normalize()
    frame = frame.dropna().drop_duplicates("date").sort_values("date")
    frame["benchmark_return"] = frame["close"].pct_change()
    return frame


def correlation_spec(frame: pd.DataFrame, variable: str, label: str) -> dict[str, float | int | str]:
    clean = frame[[variable, "car_m1_p1"]].dropna()
    if len(clean) < 3:
        return {"specification": label, "N": len(clean), "pearson_r": np.nan, "pearson_p": np.nan, "spearman_r": np.nan, "spearman_p": np.nan}
    pearson_r, pearson_p = pearsonr(clean[variable], clean["car_m1_p1"])
    spearman_r, spearman_p = spearmanr(clean[variable], clean["car_m1_p1"])
    return {"specification": label, "N": len(clean), "pearson_r": pearson_r, "pearson_p": pearson_p, "spearman_r": spearman_r, "spearman_p": spearman_p}


def main() -> None:
    panel = pd.read_csv(PANEL)
    events = pd.read_csv(EVENTS)
    contamination = pd.read_csv(CONTAMINATION)
    keys = ["platform", "fiscal_year", "quarter"]
    frame = panel.merge(events, on=keys, how="left", validate="one_to_one")
    frame = frame.merge(contamination, on=keys, how="left", validate="one_to_one")
    if frame["event_session_date"].isna().any():
        raise RuntimeError("Missing event-session dates in reviewed ledger")

    car_rows = []
    for platform, (ticker, benchmark) in MARKETS.items():
        stock = load_stock(ticker)
        index = load_index(benchmark)
        market = stock.merge(index, on="date", how="inner", validate="one_to_one").sort_values("date").reset_index(drop=True)
        market["abnormal_return"] = market["stock_return"] - market["benchmark_return"]
        for _, row in frame.loc[frame["platform"].eq(platform)].iterrows():
            event_date = pd.Timestamp(row["event_session_date"]).normalize()
            matches = market.index[market["date"].eq(event_date)].tolist()
            if len(matches) != 1:
                raise RuntimeError(f"{platform} {row['fiscal_year']}Q{row['quarter']}: event date {event_date.date()} absent or duplicated")
            position = matches[0]
            if position == 0 or position == len(market) - 1:
                raise RuntimeError(f"{platform} {row['fiscal_year']}Q{row['quarter']}: incomplete [-1,+1] window")
            window = market.loc[position - 1:position + 1]
            car_rows.append({
                "platform": platform,
                "fiscal_year": row["fiscal_year"],
                "quarter": row["quarter"],
                "event_session_date": event_date.date().isoformat(),
                "stock_ticker": ticker,
                "benchmark": benchmark,
                "ar_m1": window["abnormal_return"].iloc[0],
                "ar_0": window["abnormal_return"].iloc[1],
                "ar_p1": window["abnormal_return"].iloc[2],
                "car_m1_p1": window["abnormal_return"].sum(),
            })
    cars = pd.DataFrame(car_rows)
    results = frame.merge(cars, on=[*keys, "event_session_date"], how="left", validate="one_to_one")
    if results["car_m1_p1"].isna().any():
        raise RuntimeError("CAR computation did not cover every accounting-panel row")

    results["period_num"] = results["fiscal_year"] * 4 + results["quarter"]
    results["post_tokopedia_deconsolidation"] = results["period_num"] >= 2024 * 4 + 1
    flags = results["guidance_contaminated_working"].fillna("").str.lower().str.strip()
    unresolved = flags.isin(["unknown", "candidate", ""])
    specs = [
        correlation_spec(results, "ecosystem_ratio", "level — all events"),
        correlation_spec(results.loc[results["ratio_qoq"].notna()], "ratio_qoq", "qoq change — all events"),
        correlation_spec(results.loc[results["post_tokopedia_deconsolidation"]], "ecosystem_ratio", "level — post-2024Q1"),
        correlation_spec(results.loc[results["post_tokopedia_deconsolidation"] & results["ratio_qoq"].notna()], "ratio_qoq", "qoq change — post-2024Q1"),
    ]

    OUT.mkdir(parents=True, exist_ok=True)
    results.to_csv(OUT / "event_study_results_unfiltered_recomputed.csv", index=False)
    pd.DataFrame(specs).to_csv(OUT / "event_study_correlations_unfiltered_recomputed.csv", index=False)
    pd.DataFrame({
        "total_panel_rows": [len(results)],
        "rows_with_recomputed_car": [results["car_m1_p1"].notna().sum()],
        "unresolved_contamination_rows": [unresolved.sum()],
        "contamination_subset_status": ["BLOCKED until every event is classified yes/no" if unresolved.any() else "available"],
        "design": ["market-adjusted CAR[-1,+1]"],
    }).to_csv(OUT / "event_study_reproduction_status.csv", index=False)
    print(f"Recomputed unfiltered CARs for {len(results)} events from preserved price data.")
    print(f"Contamination-dependent specifications remain blocked for {unresolved.sum()} unresolved events.")


if __name__ == "__main__":
    main()
