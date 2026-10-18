"""Claims ledger v2 (2 Oct 2026): every number stated in the research summaries since the 1 Oct ledger, recomputed from committed tables.
'stated' = the value written in chat or memory; 'recomputed' = read from tables/*.csv.  Status PASS when within tolerance, CHECK otherwise (CHECK is a finding, not an error).
Licensed-data results (LSEG consensus, market caps) are listed in `not_reproducible` because their inputs are not committed.
Run from this folder: python3 claims_ledger_v2.py   -> tables/claims_ledger_v2.csv"""
import pandas as pd, numpy as np
T = "tables/"
gd = pd.read_csv(T + "growth_decomposition.csv").set_index(["firm", "window"])
lt = pd.read_csv(T + "l_test.csv"); rk = pd.read_csv(T + "l_rank_test.csv").set_index("sample")
tr = pd.read_csv(T + "l_transitions.csv"); bm = pd.read_csv(T + "l_big_moves.csv")
h1 = pd.read_csv(T + "h1_regional_tier.csv"); rat = pd.read_csv(T + "bps_bridge_ratios.csv", index_col=0)["value"]
ar = pd.read_csv(T + "asean_ruler_table.csv"); bl = pd.read_csv(T + "blibli_3p_quarterly.csv", index_col=0); sq = pd.read_csv(T + "shopee_quarterly_take_rate.csv", index_col=0)
sh = pd.read_csv(T + "h1_tolerance_shares.csv").set_index("set")
def g(f, w, c): return float(gd.loc[(f, w), c])
def arow(c, y, s): return float(ar[(ar.country == c) & (ar.year == y) & (ar.series.str.contains(s, regex=False))].ratio_to_econ.iloc[0])
# Malaysia census split, recomputed from the verified census figures (DOSM): 47,556 / RM398.2bn (2015) -> 78,236 / RM1,126.9bn (2022)
n15, n22, v15, v22 = 47556, 78236, 398.2, 1126.9
my_cnt = np.log(n22 / n15) / np.log(v22 / v15)
pmse = [731.4e-3, 3.90, 5.51, 6.76, 8.44]  # Rp tn, DJP: 2020 Rp731,4 miliar ... 2024 Rp8,44 triliun
grab_bq = pd.read_csv(T + "grab_quarterly_verified.csv", index_col=0)
l22 = tr[(tr.firm == "Grab") & (tr.seg == "Deliveries") & (tr.year == 2019)]
gx = pd.read_csv(T + "src/grab_20f_extraction.csv"); gx = gx[(gx.entity == "Grab Group") & (gx.period == 2019) & (gx.field == "revenue")]
big_disc = bm[bm.kind == "discount-driven"]
claims = [
 ("N01", "Decomposition: GoTo on-demand 2022-25, share of revenue growth from volume", 0.12, g("GoTo", "2022-2025", "share_from_volume"), 0.01),
 ("N02", "GoTo 2022-25, share from discount pull-back", 0.52, g("GoTo", "2022-2025", "share_from_discount_cut"), 0.01),
 ("N03", "Grab on-demand 2022-24, share from volume", 0.42, g("Grab", "2022-2024", "share_from_volume") if ("Grab", "2022-2024") in gd.index else gd.loc[("Grab", "2022-2024")].share_from_volume.iloc[0], 0.01),
 ("N04", "Grab 2022-24, share from discount pull-back", 0.47, float(gd.loc[("Grab", "2022-2024")].share_from_discount_cut.iloc[0]) if isinstance(gd.loc[("Grab", "2022-2024")], pd.DataFrame) else g("Grab", "2022-2024", "share_from_discount_cut"), 0.01),
 ("N05", "Delivery Hero 2020-25, share from volume", 0.80, g("Delivery Hero", "2020-2025", "share_from_volume"), 0.01),
 ("N06", "DoorDash 2018-19, share from volume", 0.94, g("DoorDash", "2018-2019", "share_from_volume"), 0.01),
 ("N07", "L test: transitions in the panel", 37, len(tr[tr.dlnm.notna()]), 0),
 ("N08", "Out-of-sample rank correlation of L with |dlnm|", 0.195, rk.loc["out-of-sample", "spearman"], 0.005),
 ("N09", "Out-of-sample transitions / firms", 18, rk.loc["out-of-sample", "n"], 0),
 ("N10", "In-sample rank correlation", 0.709, rk.loc["in-sample", "spearman"], 0.005),
 ("N11", "Discount-driven moves above 0.20 (count)", 5, len(big_disc), 0),
 ("N12", "...all with L >= 1.07 (minimum L among them)", 1.07, big_disc.L.min(), 0.01),
 ("N13", "Share of transitions with L<1 exceeding 0.20 (3 of 29)", 3, int(((tr.L < 1) & (tr.dlnm.abs() > 0.20)).sum()), 0),
 ("N14", "Grab 2019 reported revenue (US$ m)", -845, float(gx.value.iloc[0]), 0),
 ("N15", "Blibli 3P net take 4Q22 (%)", 0.32, bl.loc["2022Q4", "m_pct"], 0.01),
 ("N16", "Blibli 3P net take 1Q23 (%)", 2.07, bl.loc["2023Q1", "m_pct"], 0.01),
 ("N17", "Blibli: share of 4Q22-1Q23 rise from lower discounts and costs (proxy)", 0.81, (( bl.loc["2023Q1", "m_pct"] - bl.loc["2022Q4", "m_pct"]) - (bl.loc["2023Q1", "gpbd_take_pct"] - bl.loc["2022Q4", "gpbd_take_pct"])) / (bl.loc["2023Q1", "m_pct"] - bl.loc["2022Q4", "m_pct"]), 0.01),
 ("N18", "Shopee marketplace take rate 4Q18 (%)", 2.4, sq.loc["2018Q4", "mkt_take_pct"], 0.1),
 ("N19", "Shopee marketplace take rate 2Q26 (%)", 12.8, sq.loc["2026Q2", "mkt_take_pct"], 0.1),
 ("N20", "BPS bridge: Tokopedia + Shopee Indonesia / BPS marketplace, 2023", 2.87, rat["Tokopedia + Shopee Indonesia / BPS marketplace, 2023"], 0.01),
 ("N21", "BPS bridge: Tokopedia alone / BPS marketplace, 2023", 1.24, rat["Tokopedia alone / BPS marketplace (all marketplaces), 2023"], 0.01),
 ("N22", "BPS 2024 / Bank Indonesia 2024", 2.65, rat["BPS total 2024 / Bank Indonesia 2024"], 0.01),
 ("N23", "ASEAN ruler: Malaysia 2023 DOSM B2C / e-Conomy", 5.7, arow("Malaysia", 2023, "B2C"), 0.05),
 ("N24", "ASEAN ruler: Thailand 2023 ETDA B2C / e-Conomy", 3.8, arow("Thailand", 2023, "B2C"), 0.05),
 ("N25", "ASEAN ruler: Vietnam 2023 IDEA B2C / e-Conomy", 1.1, arow("Vietnam", 2023, "IDEA"), 0.05),
 ("N26", "ASEAN ruler: Indonesia 2023 BPS / e-Conomy", 1.22, arow("Indonesia", 2023, "BPS total (all"), 0.01),
 ("N27", "Malaysia 2015-22: share of growth from more establishments", 0.48, my_cnt, 0.01),
 ("N28", "PMSE VAT collected 2020-24 (Rp tn, sum of yearly DJP figures)", 25.35, sum(pmse), 0.02),
 ("N29", "H1 firm-level p, IDN_main + regional (5 firms) vs foreign clean (abs_dlnm)", 0.020, float(h1[(h1.metric == "abs_dlnm") & h1.test_set.str.startswith("IDN_main + REGIONAL") & (h1.benchmark == "EXT_clean (8 firms)")].firm_perm_p.iloc[0]), 0.001),
 ("N30", "H1 firm-level p, same, ex-Sea", 0.0038, float(h1[(h1.metric == "abs_dlnm") & h1.test_set.str.startswith("IDN_main + REGIONAL") & (h1.benchmark == "EXT_clean ex-Sea (7 firms)")].firm_perm_p.iloc[0]), 0.0005),
 ("N31", "Share of Indonesian main transitions within +-0.10", 0.125, sh.loc["IDN_main", "share_within_0.1"], 0.001),
 ("N32", "Share of foreign clean transitions within +-0.10", 0.69, sh.loc["EXT_clean", "share_within_0.1"], 0.005),
]
rows = []
for cid, st, stated, got, tol in claims:
    rows.append(dict(id=cid, claim=st, stated=stated, recomputed=round(float(got), 6), status="PASS" if abs(float(got) - stated) <= tol else "CHECK"))
L = pd.DataFrame(rows); L.to_csv(T + "claims_ledger_v2.csv", index=False)
print(L.status.value_counts().to_dict())
print(L[L.status == "CHECK"].to_string())
not_repro = ["analyst extrapolation (analyst_extrapolation.py): needs licensed LSEG consensus", "market value scaling (multiples_dispersion.py): needs licensed LSEG market caps",
             "timing_table.py Nasdaq drawdown column: needs licensed LSEG index prices", "v_definition_map.py: quotes read from scratch copies of filings (paths inside)"]
open(T + "claims_ledger_v2_NOT_REPRODUCIBLE_FROM_REPO.txt", "w").write("\n".join(not_repro) + "\n")
