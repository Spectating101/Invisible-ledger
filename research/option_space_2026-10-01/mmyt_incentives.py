"""MakeMyTrip: gross bookings, revenue and customer inducement costs, 2018Q4-2026Q2 (calendar quarters), 1 Oct 2026, exploratory.
Source: MakeMyTrip 6-K earnings releases (SEC). Under IFRS these customer inducement costs are recorded as a REDUCTION OF REVENUE (MMYT's own wording),
so gross take = (revenue + inducement) / gross bookings and net take = revenue / gross bookings, as for Grab and GoTo.
Verification: each of gross bookings, revenue, inducement must appear (any usual formatting, incl. thousands) in a release filed 10-130 days after the quarter ends.
Run: PYTHONPATH=... python3 mmyt_incentives.py <corpus_peers_dir>
"""
import datetime as dt, pathlib, re, sys
import numpy as np, pandas as pd
S = """2018Q4|1413.5|124.8|96.3 2019Q1|1372.8|120.2|81.4 2019Q2|1693.6|141.7|105.3 2019Q3|1492.9|118.0|92.7 2019Q4|1700.5|146.9|105.0 2020Q1|1206.7|104.9|58.2 2020Q2|64.5|6.4|0.7 2020Q3|213.0|21.1|2.7 2020Q4|598.8|56.8|14.8 2021Q1|759.2|79.2|24.7 2021Q2|286.7|32.8|7.5 2021Q3|734.1|67.5|27.7 2021Q4|1155.7|115.0|42.4 2022Q1|1012.3|88.6|33.7 2022Q2|1612.5|142.7|56.8 2022Q3|1541.7|131.2|57.8 2022Q4|1738.2|170.5|60.7 2023Q1|1673.9|148.5|60.4 2023Q2|1987.5|196.7|61.2 2023Q3|1839.7|168.7|60.3 2023Q4|2088.3|214.2|66.0 2024Q1|2039.0|202.9|62.5 2024Q2|2380.4|254.5|74.2 2024Q3|2257.2|211.0|69.0 2024Q4|2612.4|267.4|80.5 2025Q1|2553.1|245.5|77.8 2025Q2|2608.5|268.8|89.1 2025Q3|2447.3|229.3|89.1 2025Q4|2784.5|295.7|103.2 2026Q1|2550.5|250.1|91.2 2026Q2|2854.7|285.6|106.8"""
df = pd.DataFrame([x.split("|") for x in S.split()], columns=["quarter", "gb", "rev", "ind"]); df[["gb", "rev", "ind"]] = df[["gb", "rev", "ind"]].astype(float)
def qend(q): y, n = int(q[:4]), int(q[5]); return dt.date(y, 3 * n, [31, 30, 30, 31][n - 1])
def present(x, t):
    forms = {f"{x:,.1f}", f"{x:.1f}", f"{round(x*1000):,}", f"{x:,.0f}"}
    if any(re.search(r"(?<![\d.,])" + re.escape(f) + r"(?![\d])", t) for f in forms): return True
    ip = f"{int(x):,}"; return bool(re.search(r"(?<![\d.,])" + re.escape(ip) + r"[.,]\d", t))
if len(sys.argv) > 1:
    docs = [(dt.date.fromisoformat(p.name[:10]), p.read_text(errors="ignore")) for p in (pathlib.Path(sys.argv[1]) / "MMYT").glob("*.txt")]
    ok = []
    for _, r in df.iterrows():
        e = qend(r.quarter); ok.append(any(10 <= (d - e).days <= 130 and present(r.gb, t) and present(r.rev, t) and present(r.ind, t) for d, t in docs))
    df["verified"] = ok; print(f"rows verified in own release: {sum(ok)} of {len(df)}"); print(df[~df.verified].to_string())
df["year"] = df.quarter.str[:4].astype(int)
a = df.groupby("year").agg(n=("quarter", "size"), gb=("gb", "sum"), rev=("rev", "sum"), ind=("ind", "sum")); a = a[a.n == 4]
a["net_take_pct"] = 100 * a.rev / a.gb; a["incent_pct"] = 100 * a.ind / a.gb; a["gross_take_pct"] = a.net_take_pct + a.incent_pct
a.round(2).to_csv(pathlib.Path(__file__).parent / "tables/mmyt_annual.csv"); print(a[["gb", "rev", "ind", "net_take_pct", "incent_pct", "gross_take_pct"]].round(1).to_string())
for y0, y1 in ((2019, 2023), (2019, 2025), (2023, 2025)):
    x, y = a.loc[y0], a.loc[y1]; dm = y.net_take_pct - x.net_take_pct; di = y.incent_pct - x.incent_pct; dt_ = y.gross_take_pct - x.gross_take_pct
    print(f"{y0}->{y1}: net take {x.net_take_pct:.1f}->{y.net_take_pct:.1f} ({dm:+.1f}pt) = gross {dt_:+.1f}pt - incentives {di:+.1f}pt")
