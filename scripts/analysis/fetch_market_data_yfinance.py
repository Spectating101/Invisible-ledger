"""Fetch raw daily market data for the Invisible Ledger event study.

This script is intentionally separate from the statistical script. It creates source CSVs
that Claude/reviewer can inspect before any CAR is accepted.

Requires: pip install yfinance pandas
Internet access required.
"""
from pathlib import Path
import yfinance as yf

OUT = Path(__file__).resolve().parents[1] / "market_data"
OUT.mkdir(exist_ok=True)
TICKERS = {
    "GRAB": "GRAB",
    "SE": "SE",
    "GOTO.JK": "GOTO.JK",
    "IXIC": "^IXIC",
    "GSPC": "^GSPC",
    "JKSE": "^JKSE",
}
START, END = "2022-01-01", "2026-06-02"
for name,ticker in TICKERS.items():
    df = yf.download(ticker, start=START, end=END, auto_adjust=False, progress=False)
    if df.empty:
        raise RuntimeError(f"No data returned for {ticker}")
    # Flatten columns in current yfinance versions.
    if getattr(df.columns, "nlevels", 1) > 1:
        df.columns = [c[0] for c in df.columns]
    df = df.reset_index()
    df.columns = [str(c).lower().replace(' ','_') for c in df.columns]
    df.to_csv(OUT / f"{name}.csv", index=False)
    print(name, len(df), df['date'].min(), df['date'].max())
