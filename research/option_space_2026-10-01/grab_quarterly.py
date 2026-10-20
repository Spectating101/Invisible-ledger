"""Grab quarterly On-Demand series (2022Q1-2026Q1): GMV, revenue, incentives. 1 Oct 2026, exploratory.

Values were extracted from Grab's own quarterly results releases (SEC exhibits) by an LLM worker and then VERIFIED here:
(1) each number must appear as a token in that quarter's own source text, (2) published identities must hold
(On-Demand GMV = Mobility + Deliveries; total incentives = partner + consumer), (3) the next year's comparative column must
match where the same number is shown again. Anything failing is flagged. USD millions, as originally reported in each quarter.

Run: PYTHONPATH=/home/phyrexian/.local/lib/python3.13/site-packages python3 grab_quarterly.py <corpus_grab_dir>
"""
import pathlib, re, sys
import numpy as np, pandas as pd

# quarter: (mob_gmv, del_gmv, od_gmv_reported, rev_total, rev_mob, rev_del, partner_inc, consumer_inc, total_inc_reported, od_inc_pct, adj_ebitda)
N = None
D = {
 "2022Q1": (834, 2562, N, 228, 112, 91, 216, 344, N, N, -287), "2022Q2": (1035, 2476, N, 321, 161, 134, 212, 311, N, N, -233),
 "2022Q3": (1086, 2439, N, 382, 176, 171, 199, 277, N, N, -161), "2022Q4": (1149, 2350, N, 502, 189, 268, 174, 238, N, N, -111),
 "2023Q1": (1218, 2344, N, 525, 194, 275, 169, 222, N, N, -66), "2023Q2": (1320, 2573, N, 567, 208, 292, 175, 245, N, N, -20),
 "2023Q3": (1407, 2608, 4015, 615, 231, 306, 165, 216, N, N, 29), "2023Q4": (1474, 2648, 4122, 653, 237, 321, 172, 225, N, N, 35),
 "2024Q1": (1547, 2695, 4242, 653, 247, 350, 177, 239, 416, 9.7, 62), "2024Q2": (1584, 2850, 4434, 664, 247, 356, 186, 266, 452, 10.1, 64),
 "2024Q3": (1694, 2965, 4659, 716, 271, 380, 187, 275, 462, 9.8, 90), "2024Q4": (1815, 3213, 5028, 764, 282, 407, 204, 308, 512, 10.1, 97),
 "2025Q1": (1804, 3129, 4932, 773, 282, 415, 215, 286, 501, 10.1, 106), "2025Q2": (1883, 3471, 5354, 819, 295, 439, 239, 307, 547, 10.1, 109),
 "2025Q3": (2041, 3733, 5774, 873, 317, 465, 263, 322, 585, 10.1, 136), "2025Q4": (2174, 3904, 6077, 906, 325, 481, 285, 353, 638, 10.4, 148),
 "2026Q1": (2223, 3908, 6131, 955, 337, 510, 305, 345, 650, 10.5, 154),
}
COLS = ["mob_gmv", "del_gmv", "od_gmv_reported", "rev_total", "rev_mob", "rev_del", "partner_inc", "consumer_inc", "total_inc_reported", "od_inc_pct_reported", "adj_ebitda"]
df = pd.DataFrame(D, index=COLS).T.astype(float)

# ---- verification 1: number token appears in that quarter's own source text
corpus = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
flags = []
if corpus:
    txt = {q: " ".join(p.read_text(errors="ignore") for p in corpus.glob(f"{q}__*.txt")) for q in df.index}
    for q, row in df.iterrows():
        for c in COLS:
            v = row[c]
            if np.isnan(v) or c == "adj_ebitda" and False:
                continue
            tok = [f"{abs(v):,.0f}", f"{abs(v):.0f}", f"{abs(v):.1f}", f"{abs(v) / 1000:.1f}", f"{abs(v) / 1000:.2f}"]
            if not any(re.search(r"(?<![\d.,])" + re.escape(t) + r"(?![\d])", txt[q]) for t in tok):
                flags.append((q, c, v, "number not found in that quarter's text"))
# ---- verification 2: published identities
df["od_gmv"] = df.mob_gmv + df.del_gmv
for q, r in df.iterrows():
    if not np.isnan(r.od_gmv_reported) and abs(r.od_gmv - r.od_gmv_reported) > 1.5:
        flags.append((q, "od_gmv", r.od_gmv_reported, f"mobility+deliveries = {r.od_gmv:.0f}"))
    if not np.isnan(r.total_inc_reported) and abs(r.partner_inc + r.consumer_inc - r.total_inc_reported) > 1.5:
        flags.append((q, "total_inc", r.total_inc_reported, f"partner+consumer = {r.partner_inc + r.consumer_inc:.0f}"))
# ---- verification 3: comparative columns (same number shown again a year later) -- partner/consumer incentive prior-year values
cmp = {"2024Q1": (169, 222), "2024Q2": (175, 245), "2024Q3": (165, 216), "2024Q4": (172, 225), "2025Q1": (177, 239), "2025Q2": (187, 266), "2025Q3": (187, 275), "2025Q4": (204, 308), "2026Q1": (215, 286)}
for q, (pp, cc) in cmp.items():
    y, n = int(q[:4]) - 1, q[4:]
    prev = f"{y}{n}"
    if abs(df.loc[prev, "partner_inc"] - pp) > 1.5 or abs(df.loc[prev, "consumer_inc"] - cc) > 1.5:
        flags.append((prev, "incentives vs comparative", f"{df.loc[prev, 'partner_inc']:.0f}/{df.loc[prev, 'consumer_inc']:.0f}", f"{q} release shows prior-year {pp}/{cc}"))

# ---- derived quantities (labelled DERIVED)
df["od_rev"] = df.rev_mob + df.rev_del
df["incentives"] = df.partner_inc + df.consumer_inc
df["m_pct"] = 100 * df.od_rev / df.od_gmv                      # net take rate on On-Demand GMV
df["iota_pct"] = 100 * df.incentives / df.od_gmv               # incentives as % of On-Demand GMV
df["tau_pct"] = df.m_pct + df.iota_pct                         # gross take before incentives
df["incent_share_of_gross_pct"] = 100 * df.iota_pct / df.tau_pct
df.round(2).to_csv(pathlib.Path(__file__).parent / "tables/grab_quarterly_verified.csv")
print(f"verification flags: {len(flags)}")
for f in flags: print("  FLAG", f)
cols = ["od_gmv", "od_rev", "incentives", "m_pct", "iota_pct", "tau_pct", "incent_share_of_gross_pct"]
print(df[cols].round(1).to_string())
