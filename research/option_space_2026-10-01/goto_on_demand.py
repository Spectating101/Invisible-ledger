"""GoTo on-demand (Gojek) segment: gross revenue, incentives, net revenue, take rates (1 Oct 2026, exploratory).

ANNUAL (IDR million) comes from GoTo's audited consolidated financial statements, segment note ('Segment revenues, gross / less
Incentives to customers / Segment revenues, net', On-demand services, third parties): FY2022 from the FY2023 statements' comparative
column, FY2023, FY2024, FY2025 from their own statements. Identity checked exactly: gross - incentives = net.
QUARTERLY GTV and gross revenue come from GoTo's quarterly releases/presentations (as originally reported); net revenue from
2024 comparatives shown in the 2025-26 presentations (recast basis). FY2022 GTV is an ESTIMATE (Q1/Q2 backed out of 2023 YoY comparisons).
Run: python3 goto_on_demand.py <path to broad_archive/text/goto>
"""
import pathlib, re, sys
import pandas as pd

ann = pd.DataFrame({
    "gross":      [11_492_527, 11_915_076, 14_035_179, 15_030_994],
    "incentives": [5_624_803, 6_145_077, 3_173_938, 2_669_735],
    "net":        [5_867_724, 5_769_999, 10_861_241, 12_361_259],
    "gtv":        [60_730_000, 54_336_000, 63_057_000, 66_534_000],   # 2022 estimated; others = sum of four reported quarters
    "gtv_basis":  ["ESTIMATE (2022Q1/Q2 backed out of 2023 YoY; Q3,Q4 as reported)", "sum of reported quarters", "sum of reported quarters (as reported, before 2025 recast)", "sum of reported quarters (2025 basis)"],
}, index=[2022, 2023, 2024, 2025])
assert ((ann.gross - ann.incentives - ann.net).abs() <= 1).all(), "gross - incentives != net"
for c in ("gross", "incentives", "net"):
    ann[c + "_pct_of_gtv"] = (100 * ann[c] / ann.gtv).round(1)
ann["incent_share_of_gross_pct"] = (100 * ann.incentives / ann.gross).round(1)
if len(sys.argv) > 1:   # verify numbers appear in the audited statements
    d = pathlib.Path(sys.argv[1])
    txt = {y: "".join(p.read_text(errors="ignore") for p in d.glob(pat)) for y, pat in {2023: "*LK_20GOTO_31_20Des_202023*.txt", 2024: "*LK_20GOTO_31_20Des_202024*.txt", 2025: "*LK_20GOTO_2031_20Dec_202025*.txt"}.items()}
    chk = {2022: (2023, "11,492,527 5,624,803 5,867,724"), 2023: (2023, "11,915,076 6,145,077 5,769,999"), 2024: (2024, "14,035,179 3,173,938 10,861,241"), 2025: (2025, "15,030,994 2,669,735 12,361,259")}
    for y, (src, nums) in chk.items():
        ok = all(re.search(re.escape(n), txt[src]) for n in nums.split())
        print(f"FY{y}: numbers found in audited statements: {ok}")
ann.to_csv(pathlib.Path(__file__).parent / "tables/goto_ondemand_annual.csv")
print(ann.drop(columns="gtv_basis").to_string())

# quarterly net take rate (net revenue / GTV), recast basis, IDR billion
q = pd.DataFrame({"gtv": [13414, 15052, 16348, 17058, 15710, 16371, 16743, 17710, 16344],
                  "net": [2255, 2634, 2901, 3090, 3007, 2987, 3205, 3397, 3360]},
                 index=["2024Q1", "2024Q2", "2024Q3", "2024Q4", "2025Q1", "2025Q2", "2025Q3", "2025Q4", "2026Q1"])
q["net_take_pct"] = (100 * q.net / q.gtv).round(1)
q.to_csv(pathlib.Path(__file__).parent / "tables/goto_ondemand_quarterly_net.csv")
print("\n", q.to_string())
a, b = ann.loc[2023], ann.loc[2024]
dm = b.net_pct_of_gtv - a.net_pct_of_gtv; dt = b.gross_pct_of_gtv - a.gross_pct_of_gtv; di = b.incentives_pct_of_gtv - a.incentives_pct_of_gtv
print(f"\n2023->2024: net take {a.net_pct_of_gtv}% -> {b.net_pct_of_gtv}% ({dm:+.1f}pt) = gross fee {dt:+.1f}pt minus incentives {di:+.1f}pt -> {100 * (-di) / dm:.0f}% of the rise is incentive cuts")
