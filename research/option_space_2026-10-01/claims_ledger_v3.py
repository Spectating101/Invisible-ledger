"""Claims ledger v3 (3 Oct 2026): numbers stated in chat since ledger v2, recomputed from committed tables.
Covers the three rulers, the BI vs BPS yardsticks and the marketplace tax base. Status PASS when within tolerance, CHECK otherwise.
Run from this folder: python3 claims_ledger_v3.py -> tables/claims_ledger_v3.csv"""
import pandas as pd
T = "tables/"
r = pd.read_csv(T + "three_rulers_quarterly.csv", index_col="quarter")
y = pd.read_csv(T + "yardsticks_bi_bps.csv", index_col=0)
t = pd.read_csv(T + "tax_base_rulers.csv", index_col=0)
last4 = r.loc["2025Q3":"2026Q2"]
claims = [
 ("R01", "GoTo on-demand 2Q26: revenue growth (%)", 20.5, r.loc["2026Q2", "goto_revenue"], 0.1),
 ("R02", "GoTo on-demand 2Q26: sales growth (%)", 2.0, r.loc["2026Q2", "goto_sales"], 0.1),
 ("R03", "GoTo on-demand 2Q26: gap revenue minus sales (pts)", 18.5, r.loc["2026Q2", "goto_gap"], 0.1),
 ("R04", "Official household spending 2Q26, real growth (%)", 5.1, r.loc["2026Q2", "official_real"], 0.1),
 ("R05", "Official household spending 2Q26, nominal growth (%)", 8.3, r.loc["2026Q2", "official_nominal"], 0.1),
 ("R06", "GoTo sales growth below official nominal spending, 2025Q3-2026Q2 (quarters of 4)", 4, int((last4.goto_sales < last4.official_nominal).sum()), 0),
 ("R07", "Grab on-demand 2023Q1 revenue growth (%)", 131.0, r.loc["2023Q1", "grab_revenue"], 0.5),
 ("R08", "Grab on-demand 2023Q1 sales growth (%)", 4.9, r.loc["2023Q1", "grab_sales"], 0.1),
 ("R09", "Shopee 2022Q4 GMV growth (%)", -1.1, r.loc["2022Q4", "shopee_sales"], 0.1),
 ("R10", "Shopee 2022Q4 marketplace revenue growth (%)", 38.5, r.loc["2022Q4", "shopee_revenue"], 0.1),
 ("Y01", "BI e-commerce 2023 growth (%)", -4.7, y.loc[2023, "BI_growth_pct"], 0.05),
 ("Y02", "BPS e-commerce 2023 growth (%)", 40.6, y.loc[2023, "BPS_growth_pct"], 0.05),
 ("Y03", "BPS / BI 2022", 1.64, y.loc[2022, "BPS_div_BI"], 0.01),
 ("Y04", "BPS / BI 2023", 2.43, y.loc[2023, "BPS_div_BI"], 0.01),
 ("Y05", "BPS / BI 2024", 2.65, y.loc[2024, "BPS_div_BI"], 0.01),
 ("Y06", "BPS marketplace slice / BI, 2024", 0.42, y.loc[2024, "BPS_marketplace_div_BI"], 0.01),
 ("Y07", "BI e-commerce 2024 growth (%)", 7.3, y.loc[2024, "BI_growth_pct"], 0.05),
 ("T01", "Marketplace tax base: largest ruler / BPS marketplace", 4.83, t["times_BPS_base"].max(), 0.01),
 ("T02", "Tax at 0.5% on BPS marketplace base (Rp tn)", 1.02, t.loc["BPS marketplace channel", "tax_at_0.5pct_Rp_tn"], 0.01),
 ("T03", "Tax at 0.5% on largest base, % of 2026 tax target", 0.21, t["pct_of_2026_tax_target"].max(), 0.005),
]
rows = [dict(id=c, claim=s, stated=st, recomputed=round(float(g), 6), status="PASS" if abs(float(g) - st) <= tol else "CHECK") for c, s, st, g, tol in claims]
L = pd.DataFrame(rows); L.to_csv(T + "claims_ledger_v3.csv", index=False)
print(L.to_string(index=False)); print(L.status.value_counts().to_dict())
