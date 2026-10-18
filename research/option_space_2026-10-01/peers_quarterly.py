"""Quarterly transaction value (V) and revenue (R) for listed peers, from their own earnings releases (SEC EDGAR), 1 Oct 2026.

V = gross bookings / GOV / GBV / GMV / GMS (each firm's own label); R = revenue as reported. Values were extracted by an LLM worker
and VERIFIED here: each number must appear in a release filed 10-130 days after the quarter ends (its own release) AND, for quarters
more than a year old, again in a release filed 300+ days after that (the restated comparative). Failures are listed.
Scope notes: DoorDash GOV jumps in 2025Q4 (Deliveroo acquisition); Airbnb/Booking revenue is recognised at check-in while V is at booking,
so ratios are computed on trailing-four-quarter (TTM) sums. Etsy GMS is rounded to $0.1bn after 2021 (coarse).
Run: PYTHONPATH=... python3 peers_quarterly.py <corpus_peers_dir>
"""
import datetime as dt, pathlib, re, sys
import numpy as np, pandas as pd

RAW = {  # ticker: (V unit multiplier to $M, "Q|V|R" lines)
 "UBER": (1, "2019Q1|14649|3099 2019Q2|15756|3166 2019Q3|16465|3813 2019Q4|18131|4069 2020Q1|15776|3543 2020Q2|10224|2241 2020Q3|14745|3129 2020Q4|17152|3165 2021Q1|19536|2903 2021Q2|21900|3929 2021Q3|23113|4845 2021Q4|25866|5778 2022Q1|26449|6854 2022Q2|29078|8073 2022Q3|29119|8343 2022Q4|30749|8607 2023Q1|31408|8823 2023Q2|33601|9230 2023Q3|35281|9292 2023Q4|37575|9936 2024Q1|37651|10131 2024Q2|39952|10700 2024Q3|40973|11188 2024Q4|44197|11959 2025Q1|42818|11533 2025Q2|46756|12651 2025Q3|49740|13467 2025Q4|54140|14366 2026Q1|53720|13203 2026Q2|58022|14191"),
 "LYFT": (1, "2023Q3|3554|1158 2023Q4|3724|1225 2024Q1|3693|1277 2024Q2|4019|1436 2024Q3|4108|1523 2024Q4|4279|1550 2025Q1|4162|1450 2025Q2|4490|1588 2025Q3|4780|1685 2025Q4|5074|1593 2026Q1|4946|1651 2026Q2|5504|1844"),
 "DASH": (1, "2020Q4|8179|970 2021Q1|9913|1077 2021Q2|10500|1236 2021Q3|10400|1275 2021Q4|11159|1300 2022Q1|12353|1456 2022Q2|13081|1608 2022Q3|13534|1701 2022Q4|14446|1818 2023Q1|15913|2035 2023Q2|16468|2133 2023Q3|16751|2164 2023Q4|17639|2303 2024Q1|19239|2513 2024Q2|19711|2630 2024Q3|20002|2706 2024Q4|21279|2873 2025Q1|23076|3032 2025Q2|24244|3284 2025Q3|25015|3446 2025Q4|29683|3955 2026Q1|31604|4036 2026Q2|33078|4454"),
 "ABNB": (1, "2020Q4|5900|859 2021Q1|10300|887 2021Q2|13400|1335 2021Q3|11900|2237 2021Q4|11300|1532 2022Q1|17200|1509 2022Q2|17000|2104 2022Q3|15600|2884 2022Q4|13500|1902 2023Q1|20400|1818 2023Q2|19100|2484 2023Q3|18300|3397 2023Q4|15500|2218 2024Q1|22900|2142 2024Q2|21200|2748 2024Q3|20100|3732 2024Q4|17600|2480 2025Q1|24500|2272 2025Q2|23500|3096 2025Q3|22900|4095 2025Q4|20400|2778 2026Q1|29200|2678 2026Q2|27200|3608"),
 "BKNG": (1000, "2018Q4|19.6|3213 2019Q1|25.4|2837 2019Q2|25.0|3850 2019Q3|25.3|5040 2019Q4|20.7|3339 2020Q1|12.4|2288 2020Q2|2.3|630 2020Q3|13.4|2640 2020Q4|7.3|1238 2021Q1|11.9|1141 2021Q2|22.0|2160 2021Q3|23.7|4676 2021Q4|19.0|2981 2022Q1|27.3|2695 2022Q2|34.5|4294 2022Q3|32.1|6052 2022Q4|27.3|4049 2023Q1|39.4|3778 2023Q2|39.7|5462 2023Q3|39.8|7341 2023Q4|31.7|4784 2024Q1|43.5|4415 2024Q2|41.4|5859 2024Q3|43.4|7994 2024Q4|37.2|5471 2025Q1|46.7|4762 2025Q2|46.7|6798 2025Q3|49.7|9008 2025Q4|43.0|6349 2026Q1|53.8|5532 2026Q2|51.0|7352"),
 "EBAY": (1000, "2018Q4|24.6|2877 2019Q1|22.6|2643 2019Q2|22.6|2687 2019Q3|21.7|2649 2019Q4|23.3|2821 2020Q1|21.3|2374 2020Q2|27.1|2865 2020Q3|25.0|2606 2020Q4|26.6|2868 2021Q1|27.5|3023 2021Q2|22.1|2668 2021Q3|19.5|2501 2021Q4|20.7|2613 2022Q1|19.4|2483 2022Q2|18.5|2422 2022Q3|17.7|2380 2022Q4|18.2|2510 2023Q1|18.4|2510 2023Q2|18.2|2540 2023Q3|18.0|2500 2023Q4|18.6|2562 2024Q1|18.6|2556 2024Q2|18.4|2572 2024Q3|18.3|2576 2024Q4|19.3|2579 2025Q1|18.8|2585 2025Q2|19.5|2730 2025Q3|20.1|2820 2025Q4|21.2|2965 2026Q1|22.2|3089 2026Q2|22.4|3134"),
 "ETSY": (1, "2018Q4|1246.5|200.0 2019Q1|1024.0|169.3 2019Q2|1094.8|181.1 2019Q3|1200.4|197.9 2019Q4|1655.7|270.0 2020Q1|1353.3|228.1 2020Q2|2688.8|428.7 2020Q3|2633.9|451.5 2020Q4|3605.1|617.4 2021Q1|3100|550.6 2021Q2|3000|528.9 2021Q3|3100|532.4 2021Q4|4200|717.1 2022Q1|3300|579.3 2022Q2|3000|585.1 2022Q3|3000|594.5 2022Q4|4000|807.2 2023Q1|3100|640.9 2023Q2|3000|628.9 2023Q3|3000|636.3 2023Q4|4000|842.3 2024Q1|3000|646.0 2024Q2|2900|647.8 2024Q3|2900|662.4 2024Q4|3700|852.2 2025Q1|2800|651.2 2025Q2|2800|672.7 2025Q3|2724.7|678.0 2025Q4|3592.6|881.6"),
}
rows = []
for tk, (mult, s) in RAW.items():
    for item in s.split():
        q, v, r = item.split("|"); rows.append((tk, q, float(v) * mult, float(r)))
df = pd.DataFrame(rows, columns=["firm", "quarter", "V", "R"])

def qend(q): y, n = int(q[:4]), int(q[5]); return dt.date(y, 3 * n, [31, 30, 30, 31][n - 1])
def cands(x, mult):
    v = x / mult if mult != 1 and x >= 100 else x
    outs = {f"{x:,.0f}", f"{x:.1f}", f"{x/1000:.1f}", f"{x/1000:.2f}", f"{x:,.1f}", f"{v:.1f}"}
    return outs
def present(x, text, mult):
    for t in cands(x, mult):
        if re.search(r"(?<![\d.,])" + re.escape(t) + r"(?![\d])", text): return True
    ip = int(x)  # decimals (Lyft/Etsy): integer part followed by .d
    for k in {ip, ip + 1}:
        if re.search(r"(?<![\d.,])" + re.escape(f"{k:,}") + r"\.\d", text): return True
    return False

flags, status = [], []
if len(sys.argv) > 1:
    base = pathlib.Path(sys.argv[1]); docs = {}
    for tk in RAW:
        docs[tk] = [(dt.date.fromisoformat(p.name[:10]), p.read_text(errors="ignore")) for p in (base / tk).glob("*.txt")]
    for i, r in df.iterrows():
        e = qend(r.quarter); mult = RAW[r.firm][0]; own = comp = False
        for d, t in docs[r.firm]:
            gap = (d - e).days
            if 10 <= gap <= 130 and present(r.V, t, mult) and present(r.R, t, 1): own = True
            if 300 <= gap <= 520 and present(r.V, t, mult) and present(r.R, t, 1): comp = True
        old = (dt.date(2026, 9, 30) - e).days > 520
        st = "VERIFIED(own+comparative)" if own and comp else ("VERIFIED(own only; latest year)" if own and not old else ("OWN ONLY" if own else "FAIL"))
        status.append(st)
    df["status"] = status
    print(df.status.value_counts().to_string()); print("\nby firm:"); print(pd.crosstab(df.firm, df.status).to_string())
    print("\nFAIL/OWN-ONLY rows:\n", df[df.status.isin(["FAIL", "OWN ONLY"])][["firm", "quarter", "V", "R", "status"]].to_string())
df.to_csv(pathlib.Path(__file__).parent / "tables/peers_quarterly.csv", index=False)
