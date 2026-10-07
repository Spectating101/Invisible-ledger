"""Claims ledger v7 (8 Oct 2026): cheap exploratory checks (timing of take-rate swings; BPS start-year cohorts; GoTo's 2024 incentive cut).
bps_cohort_check.py uses licensed microdata (not rebuilt); its national totals are committed in tables/bps_cohort_check.json.
Run from this folder: python3 claims_ledger_v7.py -> tables/claims_ledger_v7.csv"""
import json
import pandas as pd
T = "tables/"
t = json.load(open(T + "timing_check.json")); c = json.load(open(T + "bps_cohort_check.json")); c24 = json.load(open(T + "bps_cohort_2024_published.json")); h2 = json.load(open(T + "bps_h2_cheap_checks.json")); g = pd.read_csv(T + "goto_ondemand_annual.csv", index_col=0)
w = t["2022-24"]
claims = [
 ("T01", "2022-24 window: Indonesia and region, firms swinging more than in other years (of 4)", 4, w["Indonesia and region"]["firms_larger_in_window"], 0),
 ("T02", "2022-24 window: Indonesia and region median swing", 0.32, w["Indonesia and region"]["median_in_window"], 0.005),
 ("T03", "2022-24 window: Indonesia and region median swing, other years", 0.06, w["Indonesia and region"]["median_other_years"], 0.005),
 ("T04", "2022-24 window: foreign lower-income firms swinging more (of 7)", 1, w["Foreign, lower-income markets"]["firms_larger_in_window"], 0),
 ("T05", "2022-23 window: foreign lower-income firms swinging more (of 7)", 2, t["2022-23"]["Foreign, lower-income markets"]["firms_larger_in_window"], 0),
 ("T06", "2022-23 window: foreign high-income Wilcoxon p", 0.62, t["2022-23"]["Foreign, high-income markets"]["wilcoxon_one_sided_p"], 0.005),
 ("C01", "Sellers started online by 2021: 2022 survey (thousands)", 2559, c["started_by"]["2021"]["2022"], 1),
 ("C02", "Sellers started online by 2021: 2023 survey (thousands)", 2689, c["started_by"]["2021"]["2023"], 1),
 ("C03", "Sellers started by 2020: change 2020 to 2022 survey (%)", -9.9, c["started_by"]["2020"]["change_2020_to_2022_pct"], 0.1),
 ("C04", "Sellers started by 2020: change 2022 to 2023 survey (%)", 6.0, c["started_by"]["2020"]["change_2022_to_2023_pct"], 0.1),
 ("C05", "Pre-2023 sellers counted in 2023 beyond the 2022 count (thousands)", 306, c["rise_2022_to_2023"]["pre_2023_sellers_more_than_counted_before_k"], 1),
 ("C06", "Share of the 2023 rise from pre-2023 sellers not counted before (%)", 37.3, c["rise_2022_to_2023"]["share_of_rise_from_pre_2023_sellers_pct"], 0.1),
 ("C07", "Started selling online in 2022: 2022 survey (thousands)", 437, c["cohort_counts_thousands"]["2022"]["2022"], 1),
 ("C08", "Started selling online in 2022: 2023 survey (thousands)", 612, c["cohort_counts_thousands"]["2022"]["2023"], 1),
 ("C09", "2023->2024: sellers started before 2020, change (published 2024 vs 2023 survey, %)", -10.2, c24["change_before_2020_pct"], 0.05),
 ("C10", "2023->2024: sellers started 2020-22, change (%)", 0.1, c24["change_2020_2022_pct"], 0.05),
 ("C11", "2024: minimum new sellers (thousands)", 754, c24["min_entrants_2024_k"], 1),
 ("C12", "2023->2024: published rise in sellers (thousands)", 584, c24["published_rise_2023_2024_k"], 1),
 ("C13", "Sellers started by 2022, marketplace users: change 2022->2023 survey (%)", 0.3, h2["cohort_started_by_2022_by_channel_k"]["marketplace users"]["change_pct"], 0.05),
 ("C14", "Sellers started by 2022, chat or social only: change 2022->2023 survey (%)", 13.0, h2["cohort_started_by_2022_by_channel_k"]["chat or social only"]["change_pct"], 0.05),
 ("C15", "Financial statements, sellers started before 2020, 2022 survey (%)", 23.4, h2["financial_statements_by_cohort_pct"]["2022 survey, started before 2020"], 0.05),
 ("C16", "Financial statements, sellers started before 2020, 2023 survey (%)", 16.8, h2["financial_statements_by_cohort_pct"]["2023 survey, started before 2020"], 0.05),
 ("C17", "Revenue under Rp300m: sellers started 2022 (%)", 86.5, h2["revenue_bracket_by_cohort_2022_pct"]["started 2022"]["<300m"], 0.05),
 ("C18", "Revenue under Rp300m: sellers started before 2020 (%)", 80.7, h2["revenue_bracket_by_cohort_2022_pct"]["started before 2020"]["<300m"], 0.05),
 ("O01", "GoTo on-demand incentives as % of GTV, 2023", 11.3, g.loc[2023, "incentives_pct_of_gtv"], 0.05),
 ("O02", "GoTo on-demand incentives as % of GTV, 2024", 5.0, g.loc[2024, "incentives_pct_of_gtv"], 0.05),
]
L = pd.DataFrame([dict(id=i, claim=x, stated=s, recomputed=round(float(v), 6), status="PASS" if abs(float(v) - s) <= tol else "CHECK") for i, x, s, v, tol in claims])
L.to_csv(T + "claims_ledger_v7.csv", index=False); print(L.to_string(index=False)); print(L.status.value_counts().to_dict())
