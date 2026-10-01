"""Option-space numbers for the Invisible Ledger thesis phase (1 Oct 2026).

Reads only committed repo CSVs; writes tables to ./tables/. Nothing here changes
research data. Exploratory: tests are descriptive, small-N, and cluster-aware where noted.

Run: PYTHONPATH=/home/phyrexian/.local/lib/python3.13/site-packages python3 build_numbers.py
"""
import itertools
import json
import pathlib

import numpy as np
import pandas as pd
from scipy import stats

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path(__file__).resolve().parent / "tables"
OUT.mkdir(exist_ok=True)
RNG = np.random.default_rng(20261001)

HT = ROOT / "outputs/hypothesis_tests_2026-09-10"
GE = ROOT / "data/global_ecommerce"

# ---------------------------------------------------------------- load
idn_t = pd.read_csv(HT / "indonesia_longitudinal_candidate_transitions.csv")
idn_l = pd.read_csv(HT / "indonesia_longitudinal_candidate_levels.csv")
ext_t = pd.read_csv(GE / "global_platform_growth_divergence.csv")
ext_l = pd.read_csv(GE / "global_platform_matched_annual.csv")

# ---------------------------------------------------------------- unified transitions
rows = []
for _, r in idn_t.iterrows():
    y0, y1 = (int(x) for x in r.transition.split("-"))
    constructed = r.series in ("Grab", "Shopee")
    rows.append(dict(
        set="IDN_constructed" if constructed else "IDN_main",
        firm=r.series, y0=y0, y1=y1,
        gV=r.transaction_growth_pct, gR=r.revenue_growth_pct,
        clean=True, tier=r.evidence_tier))
for _, r in ext_t.iterrows():
    rows.append(dict(
        set="EXT_clean" if r.clean_scope_transition == "yes" else "EXT_unclean",
        firm=r.issuer, y0=int(r.from_year), y1=int(r.to_year),
        gV=r.transaction_growth_pct, gR=r.revenue_growth_pct,
        clean=r.clean_scope_transition == "yes", tier="external"))
T = pd.DataFrame(rows)

# take rates from the level tables (percent of transaction value)
m_idn = {(r.series, int(r.year)): r.monetization_rate_pct for r in idn_l.itertuples()}
m_ext = {(r.issuer, int(r.year)): r.take_rate_pct for r in ext_l.itertuples()}
m_all = {**m_idn, **m_ext}
T["m0_pct"] = [m_all.get((f, y)) for f, y in zip(T.firm, T.y0)]
T["m1_pct"] = [m_all.get((f, y)) for f, y in zip(T.firm, T.y1)]
T["E0"] = 100 / T.m0_pct - 1
T["E1"] = 100 / T.m1_pct - 1

T["D_pp"] = T.gR - T.gV
T["lnV"] = np.log1p(T.gV / 100)
T["lnR"] = np.log1p(T.gR / 100)
T["dlnm"] = T.lnR - T.lnV                       # log change in take rate (exact identity)
T["abs_dlnm"] = T.dlnm.abs()
T["abs_D"] = T.D_pp.abs()
T["dlnm_from_levels"] = np.log(T.m1_pct / T.m0_pct)
T["identity_gap"] = (T.dlnm - T.dlnm_from_levels).abs()
T["opposite_sign"] = (T.gV * T.gR) < 0
T["story"] = np.select(
    [(T.gV < 0) & (T.gR > 0), (T.gV > 0) & (T.gR < 0),
     T.dlnm > 0.10, T.dlnm < -0.10],
    ["V down, R up", "V up, R down", "R outruns V", "R lags V"], "tracks (|dlnm|<=0.10)")
T["firm_first_year"] = T.groupby("firm").y0.transform("min")
T["age"] = T.y0 - T.firm_first_year
T.to_csv(OUT / "transitions_master.csv", index=False)

IDN = T[T.set == "IDN_main"]
IDNALL = T[T.set.isin(["IDN_main", "IDN_constructed"])]
EXT = T[T.set == "EXT_clean"]
EXTX = EXT[EXT.firm != "Sea / Shopee"]
EXTALL = T[T.set.str.startswith("EXT")]


def mw(a, b, col):
    return stats.mannwhitneyu(a[col], b[col], alternative="greater").pvalue


def firm_med(df, col):
    return df.groupby("firm")[col].median()


def perm_firm(idn_df, ext_df, col, reps=None):
    """Exact firm-level label permutation: how often do 3 randomly chosen firms look this extreme?"""
    fm = pd.concat([firm_med(idn_df, col), firm_med(ext_df, col)])
    k = idn_df.firm.nunique()
    obs = firm_med(idn_df, col).mean()
    vals = fm.values
    combos = list(itertools.combinations(range(len(vals)), k))
    dist = np.array([vals[list(c)].mean() for c in combos])
    return (dist >= obs - 1e-12).mean(), len(combos)


def cluster_boot(a, b, col, reps=5000):
    fa, fb = a.firm.unique(), b.firm.unique()
    diffs = []
    for _ in range(reps):
        sa = RNG.choice(fa, len(fa)); sb = RNG.choice(fb, len(fb))
        xa = np.concatenate([a.loc[a.firm == f, col].values for f in sa])
        xb = np.concatenate([b.loc[b.firm == f, col].values for f in sb])
        diffs.append(np.median(xa) - np.median(xb))
    d = np.array(diffs)
    return np.percentile(d, [2.5, 97.5])


# ---------------------------------------------------------------- test battery
bat = []
for metric in ("abs_D", "abs_dlnm"):
    for label, a, b in [
        ("IDN_main(8) vs EXT_clean(29)", IDN, EXT),
        ("IDN_main(8) vs EXT_clean ex-Sea(22)", IDN, EXTX),
        ("IDN_main(8) vs EXT_all(40)", IDN, EXTALL),
        ("IDN_main drop 2022-23 (5) vs EXT_clean", IDN[IDN.y0 != 2022], EXT),
        ("IDN_main drop largest (7) vs EXT_clean", IDN.drop(IDN[metric].idxmax()), EXT),
        ("IDN incl constructed (12) vs EXT_clean", IDNALL, EXT),
        ("Sea/Shopee(7) vs EXT_clean ex-Sea(22)", EXT[EXT.firm == "Sea / Shopee"], EXTX),
    ]:
        p_obs = mw(a, b, metric)
        p_firm, ncomb = (perm_firm(a, b, metric) if a.firm.nunique() >= 2 and b.firm.nunique() >= 2
                         else (np.nan, 0))
        lo, hi = cluster_boot(a, b, metric, 2000) if a.firm.nunique() >= 2 else (np.nan, np.nan)
        bat.append(dict(metric=metric, comparison=label,
                        n_a=len(a), firms_a=a.firm.nunique(), n_b=len(b), firms_b=b.firm.nunique(),
                        median_a=a[metric].median(), median_b=b[metric].median(),
                        mw_p_obs_level=p_obs, firm_perm_p=p_firm, firm_perm_combos=ncomb,
                        cluster_boot_95_diff_median=f"[{lo:.3f}, {hi:.3f}]"))
pd.DataFrame(bat).to_csv(OUT / "test_battery.csv", index=False)

# direction / sign tests
sg = []
for label, df in [("IDN_main", IDN), ("IDN_constructed", T[T.set == "IDN_constructed"]),
                  ("EXT_clean", EXT), ("EXT_clean ex-Sea", EXTX), ("EXT_all", EXTALL)]:
    pos = int((df.dlnm > 0).sum()); n = len(df)
    sg.append(dict(set=label, n=n, revenue_faster=pos,
                   binom_two_sided_p=stats.binomtest(pos, n, 0.5).pvalue,
                   opposite_sign=int(df.opposite_sign.sum()),
                   median_signed_D=df.D_pp.median(), median_abs_D=df.abs_D.median(),
                   median_signed_dlnm=df.dlnm.median(), median_abs_dlnm=df.abs_dlnm.median(),
                   share_tracking_le_0p05=(df.abs_dlnm <= 0.05).mean(),
                   share_tracking_le_0p10=(df.abs_dlnm <= 0.10).mean(),
                   share_tracking_le_0p20=(df.abs_dlnm <= 0.20).mean()))
pd.DataFrame(sg).to_csv(OUT / "direction_and_tracking.csv", index=False)
fx = stats.fisher_exact([[int(IDN.opposite_sign.sum()), len(IDN) - int(IDN.opposite_sign.sum())],
                         [int(EXT.opposite_sign.sum()), len(EXT) - int(EXT.opposite_sign.sum())]])
tr = stats.fisher_exact([[int((IDN.abs_dlnm <= 0.10).sum()), int((IDN.abs_dlnm > 0.10).sum())],
                         [int((EXT.abs_dlnm <= 0.10).sum()), int((EXT.abs_dlnm > 0.10).sum())]])
pd.DataFrame([dict(test="reversals IDN_main vs EXT_clean (Fisher exact, two-sided)", p=fx.pvalue),
              dict(test="tracking within +-0.10 log pts IDN_main vs EXT_clean (Fisher exact)", p=tr.pvalue)]) \
    .to_csv(OUT / "fisher_tests.csv", index=False)

# ---------------------------------------------------------------- decomposition by story
T.groupby(["set", "story"]).size().unstack(fill_value=0).to_csv(OUT / "story_counts_by_set.csv")
T[["set", "firm", "y0", "y1", "gV", "gR", "D_pp", "dlnm", "m0_pct", "m1_pct", "story"]] \
    .sort_values(["set", "firm", "y0"]).round(3).to_csv(OUT / "transition_stories.csv", index=False)

# ---------------------------------------------------------------- year effects
yr = T[T.set.isin(["IDN_main", "EXT_clean"])].groupby(["set", "y0"]).agg(
    n=("dlnm", "size"), med_dlnm=("dlnm", "median"),
    share_pos=("dlnm", lambda s: (s > 0).mean())).round(3)
yr.to_csv(OUT / "year_effects.csv")

# ---------------------------------------------------------------- life cycle (age) analysis
lc = T[T.set.isin(["IDN_main", "EXT_clean"])].copy()
lc["firm_id"] = lc.firm
multi = lc.groupby("firm").filter(lambda d: len(d) >= 3)


def fe_slope(df, ycol="abs_dlnm"):
    y = df[ycol] - df.groupby("firm")[ycol].transform("mean")
    x = df.age - df.groupby("firm").age.transform("mean")
    return (x * y).sum() / (x * x).sum()


obs = fe_slope(multi)
perms = []
for _ in range(5000):
    sh = multi.copy()
    sh["age"] = sh.groupby("firm").age.transform(lambda s: RNG.permutation(s.values))
    perms.append(fe_slope(sh))
p_lc = (np.array(perms) <= obs).mean()
per_firm = []
for f, d in multi.groupby("firm"):
    rho = stats.spearmanr(d.age, d.abs_dlnm)
    per_firm.append(dict(firm=f, n=len(d), spearman_age_vs_abs_dlnm=rho.statistic, p=rho.pvalue,
                         first_half_median=d.sort_values("age").abs_dlnm.iloc[: len(d) // 2].median(),
                         last_half_median=d.sort_values("age").abs_dlnm.iloc[-(len(d) // 2):].median()))
pd.DataFrame(per_firm).round(3).to_csv(OUT / "lifecycle_per_firm.csv", index=False)
pd.DataFrame([dict(fe_slope_abs_dlnm_per_year=obs, perm_p_one_sided_negative=p_lc,
                   firms=multi.firm.nunique(), n=len(multi))]).to_csv(OUT / "lifecycle_fe_regression.csv", index=False)

# ---------------------------------------------------------------- level leverage (E vs instability), firm level
lev = []
for label, df in [("EXT_clean", EXT), ("IDN_main+EXT_clean", pd.concat([IDN, EXT]))]:
    f = df.groupby("firm").agg(E0=("E0", "median"), abs_dlnm=("abs_dlnm", "median"), n=("abs_dlnm", "size"))
    r = stats.spearmanr(f.E0, f.abs_dlnm)
    r2 = stats.spearmanr(df.E0, df.abs_dlnm)
    lev.append(dict(sample=label, firm_level_rho=r.statistic, firm_level_p=r.pvalue, firms=len(f),
                    pooled_rows_rho=r2.statistic, pooled_rows_p=r2.pvalue, rows=len(df)))
pd.DataFrame(lev).round(4).to_csv(OUT / "leverage_test.csv", index=False)

# take rate levels by firm-year (all admitted layers) for atlas
lv = pd.concat([
    idn_l[["series", "year", "transaction_value", "revenue_value", "monetization_rate_pct", "evidence_tier"]]
    .rename(columns={"series": "firm"}),
    ext_l[["issuer", "year", "transaction_value", "revenue_value", "take_rate_pct"]]
    .rename(columns={"issuer": "firm", "take_rate_pct": "monetization_rate_pct"}).assign(evidence_tier="external")])
lv["E"] = 100 / lv.monetization_rate_pct - 1
lv.round(4).to_csv(OUT / "take_rate_levels.csv", index=False)

# ---------------------------------------------------------------- BPS recompute
bl = pd.read_csv(HT / "bps_national_levels.csv").set_index("year")
bps = {}
for a, b in ((2022, 2023), (2023, 2024), (2022, 2024)):
    S0, S1 = bl.loc[a, "transaction_value_idr_trillion"], bl.loc[b, "transaction_value_idr_trillion"]
    N0, N1 = bl.loc[a, "estimated_ecommerce_businesses"], bl.loc[b, "estimated_ecommerce_businesses"]
    bps[f"{a}-{b}"] = dict(
        S_growth=100 * (S1 / S0 - 1), N_growth=100 * (N1 / N0 - 1), A_growth=100 * ((S1 / N1) / (S0 / N0) - 1),
        count_share_log=100 * np.log(N1 / N0) / np.log(S1 / S0),
        count_share_sym=100 * (N1 - N0) * ((S0 / N0 + S1 / N1) / 2) / (S1 - S0))
m23, m24 = bl.loc[2023], bl.loc[2024]
bps["marketplace"] = dict(
    mkt_growth=100 * (m24.marketplace_value_idr_trillion / m23.marketplace_value_idr_trillion - 1),
    nonmkt_growth=100 * (m24.nonmarketplace_value_idr_trillion / m23.nonmarketplace_value_idr_trillion - 1),
    mkt_share_2023=100 * m23.marketplace_value_idr_trillion / m23.transaction_value_idr_trillion,
    mkt_share_2024=100 * m24.marketplace_value_idr_trillion / m24.transaction_value_idr_trillion,
    nonmkt_share_of_increase=100 * (m24.nonmarketplace_value_idr_trillion - m23.nonmarketplace_value_idr_trillion)
    / (m24.transaction_value_idr_trillion - m23.transaction_value_idr_trillion),
    mkt_usd_bn_2023=m23.marketplace_value_idr_trillion * 1000 / 15236.88,
    total_usd_bn_2023=m23.transaction_value_idr_trillion * 1000 / 15236.88)
# alternative 2023 count (3,934,981) sensitivity for 2023->2024
alt = 100 * (4400972 - 3934981) * ((1100.87 / 3934981 + 1288.93 / 4400972) / 2) / (1288.93 - 1100.87)
bps["alt_count_2023_2024_share"] = dict(count_share_log=alt)
json.dump(bps, open(OUT / "bps_recompute.json", "w"), indent=2, default=float)

# ---------------------------------------------------------------- FY2023 cross-section recompute
fy = pd.read_csv(ROOT / "data/indonesia_fy2023/fy2023_indonesia_main_rebuilt.csv")
V, R = fy.transaction_value_usd_b.sum(), fy.platform_revenue_usd_b.sum()
gdp = pd.read_csv(ROOT / "data/asean_context/asean_worldbank_context_2000_2025.csv")
gdp23 = gdp[(gdp.country == "Indonesia") & (gdp.year == 2023) & (gdp.indicator == "NY.GDP.MKTP.CD")].value.iloc[0] / 1e9
fy23 = dict(V=V, R=R, W=V - R, ratio_V_over_R=V / R, E=(V - R) / R, GDP_usd_bn=gdp23, W_over_GDP_pct=100 * (V - R) / gdp23)

# ---------------------------------------------------------------- claims ledger
tok = pd.read_csv(ROOT / "data/measurement/results/tokopedia_fy2022_2023_revenue_incentive_reconciliation.csv").iloc[0]
tk = IDN[IDN.firm.str.startswith("Tokopedia")].iloc[0]
pay = pd.read_csv(ROOT / "outputs/payment_ledger_2026-09-11/bps_payment_growth_comparison_2023_2024.csv")
glob = pd.read_csv(GE / "global_platform_summary.csv").set_index("metric").value
sumtab = pd.read_csv(HT / "indonesia_longitudinal_transition_summary.csv").set_index("evidence_tier")
bl_E = lv[(lv.firm == "Blibli 3P Retail") & (lv.year == 2023)].E.iloc[0]
bk_E = lv[(lv.firm == "Bukalapak Group") & (lv.year == 2023)].E.iloc[0]
Eend = {}
for f in ("Tokopedia e-commerce segment", "Blibli 3P Retail", "Bukalapak Group"):
    d = lv[lv.firm == f].sort_values("year")
    Eend[f] = (d.E.iloc[0], d.E.iloc[-1])
drop = IDN.drop(IDN.abs_D.idxmax())
claims = [
    # (id, where, statement, stated, recomputed, tol)
    ("C01", "proposal/deck", "Main sample median |D| (pp)", 38.92, IDN.abs_D.median(), 0.01),
    ("C02", "proposal/deck", "Main sample transitions", 8, len(IDN), 0),
    ("C03", "proposal/deck", "Revenue grew faster in (of 8)", 6, int((IDN.D_pp > 0).sum()), 0),
    ("C04", "proposal/deck", "Opposite-direction transitions (main)", 2, int(IDN.opposite_sign.sum()), 0),
    ("C05", "proposal", "Median signed D, main (pp) [handoff: 15.07]", 15.07, IDN.D_pp.median(), 0.01),
    ("C06", "proposal", "Drop largest: transitions", 7, len(drop), 0),
    ("C07", "proposal", "Drop largest: revenue faster in", 5, int((drop.D_pp > 0).sum()), 0),
    ("C08", "proposal", "Drop largest: median |D| (pp)", 15.74, drop.abs_D.median(), 0.01),
    ("C09", "proposal", "All five platforms: transitions", 12, len(IDNALL), 0),
    ("C10", "proposal", "All five: revenue faster in", 10, int((IDNALL.D_pp > 0).sum()), 0),
    ("C11", "proposal", "All five: median |D| (pp)", 42.02, IDNALL.abs_D.median(), 0.01),
    ("C12", "proposal", "Tokopedia V growth 2022-23 (%)", -8.9, tk.gV, 0.05),
    ("C13", "proposal", "Tokopedia net revenue growth 2022-23 (%)", 53.2, tk.gR, 0.05),
    ("C14", "proposal", "Tokopedia D (pp)", 62.1, tk.D_pp, 0.05),
    ("C15", "proposal", "Tokopedia: incentive share of net revenue change (%)", 60.6, 100 * tok.incentive_reduction_share_of_net_change, 0.05),
    ("C16", "proposal", "Tokopedia: gross revenue share (%)", 39.4, 100 * tok.gross_revenue_share_of_net_change, 0.05),
    ("C17", "proposal", "External: matched observations", 48, int(glob["matched_issuer_years"]), 0),
    ("C18", "proposal", "External: clean transitions", 29, int(glob["clean_scope_transitions"]), 0),
    ("C19", "proposal", "External: revenue faster in (of 29)", 22, int((EXT.D_pp > 0).sum()), 0),
    ("C20", "proposal", "External: opposite direction (clean)", 4, int(glob["opposite_direction_transitions_clean"]), 0),
    ("C21", "proposal", "External median |D| (pp)", 7.1, EXT.abs_D.median(), 0.05),
    ("C22", "proposal", "BPS total growth 2023-24 (%)", 17.08, bps["2023-2024"]["S_growth"], 0.01),
    ("C23", "proposal", "BPS marketplace growth (%)", 1.45, bps["marketplace"]["mkt_growth"], 0.01),
    ("C24", "proposal", "BPS non-marketplace growth (%)", 20.57, bps["marketplace"]["nonmkt_growth"], 0.01),
    ("C25", "proposal", "Share of increase outside marketplace (%)", 98.46, bps["marketplace"]["nonmkt_share_of_increase"], 0.01),
    ("C26", "proposal", "BPS businesses growth 2023-24 (%)", 15.31, bps["2023-2024"]["N_growth"], 0.01),
    ("C27", "proposal", "BPS sales per business growth (%)", 1.54, bps["2023-2024"]["A_growth"], 0.01),
    ("C28", "proposal", "Count share of increase 2023-24 (%)", 90.29, bps["2023-2024"]["count_share_sym"], 0.01),
    ("C29", "proposal", "Count share, alt 2023 count (%)", 70.95, alt, 0.01),
    ("C30", "deck", "Count share 2022-23 (%)", 71, bps["2022-2023"]["count_share_sym"], 0.5),
    ("C31", "deck", "BPS 2022-23 total growth (%)", 40.60, bps["2022-2023"]["S_growth"], 0.01),
    ("C32", "proposal", "BPS marketplace share 2023 (%)", 18.2, bps["marketplace"]["mkt_share_2023"], 0.05),
    ("C33", "deck", "BPS marketplace USD bn 2023", 13.2, bps["marketplace"]["mkt_usd_bn_2023"], 0.05),
    ("C34", "proposal", "FY2023 total V (US$ bn)", 43.23, fy23["V"], 0.005),
    ("C35", "proposal", "FY2023 total R (US$ bn)", 3.16, fy23["R"], 0.005),
    ("C36", "proposal", "FY2023 wedge (US$ bn)", 40.07, fy23["W"], 0.005),
    ("C37", "proposal", "FY2023 V/R", 13.7, fy23["ratio_V_over_R"], 0.05),
    ("C38", "proposal", "FY2023 E", 12.7, fy23["E"], 0.05),
    ("C39", "handoff", "Wedge as % of Indonesia 2023 GDP", 2.92, fy23["W_over_GDP_pct"], 0.01),
    ("C40", "proposal", "Blibli 2023 E", 43.4, bl_E, 0.05),
    ("C41", "proposal", "Bukalapak 2023 E", 36.0, bk_E, 0.05),
    ("C42", "proposal", "Tokopedia E 2023", 39.3, lv[(lv.firm.str.startswith('Tokopedia')) & (lv.year == 2023)].E.iloc[0], 0.05),
    ("C43", "proposal", "Every issuer-reported E ends below its start (count of 3)", 3,
     sum(1 for a, b in Eend.values() if b < a), 0),
    ("C44", "deck", "Mann-Whitney one-sided p, |D|, main vs external clean", 0.002,
     mw(IDN, EXT, "abs_D"), 0.0005),
    ("C45", "deck", "MW p drop largest", 0.006, mw(drop, EXT, "abs_D"), 0.0005),
    ("C46", "deck", "MW p excluding Sea (<0.001)", 0.001, mw(IDN, EXTX, "abs_D"), "lt"),
    ("C47", "deck", "MW p one median per firm (3 vs 8)", 0.024,
     stats.mannwhitneyu(firm_med(IDN, "abs_D"), firm_med(EXT, "abs_D"), alternative="greater").pvalue, 0.0005),
    ("C48", "deck", "Growth correlation, Indonesia main", 0.10, stats.pearsonr(IDN.gV, IDN.gR)[0], 0.005),
    ("C49", "deck", "Growth correlation, external excl. Sea", 0.98, stats.pearsonr(EXTX.gV, EXTX.gR)[0], 0.005),
]
for lab, metric in (("e-money shopping", 30.47), ("mobile banking", 82.84), ("QRIS", 186.98)):
    best = pay.iloc[(pay.growth_2023_2024_percent - metric).abs().argsort()[:1]].iloc[0]
    claims.append((f"C{50 + len([c for c in claims if c[0] >= 'C50'])}", "proposal",
                   f"Payments growth {lab} (%) matched row: {best.metric}", metric, best.growth_2023_2024_percent, 0.01))
    claims.append((f"C{50 + len([c for c in claims if c[0] >= 'C50'])}", "proposal",
                   f"{lab} multiple of BPS growth", round(metric / 17.08, 2), best.growth_2023_2024_percent / bps["2023-2024"]["S_growth"], 0.01))

led = []
for cid, where, st, stated, got, tol in claims:
    if tol == "lt":
        ok = got < stated
    else:
        ok = abs(got - stated) <= tol
    led.append(dict(id=cid, where=where, claim=st, stated=stated, recomputed=round(float(got), 6),
                    status="PASS" if ok else "CHECK"))
pd.DataFrame(led).to_csv(OUT / "claims_ledger.csv", index=False)
json.dump(fy23, open(OUT / "fy2023_recompute.json", "w"), indent=2, default=float)

print("identity max gap (dlnm vs ln m1/m0):", T.identity_gap.max())
print(pd.DataFrame(led).status.value_counts().to_dict())
print(pd.DataFrame(led)[lambda d: d.status != "PASS"].to_string())


# ================================================================ EXTENSIONS (1 Oct 2026 option-space)
# 1. Visibility ladder, Indonesia 2023 (US$ bn and % of GDP). Levels are NOT like-for-like; shown side by side only.
FX = 15236.88
bps23 = bl.loc[2023]
ladder = pd.DataFrame([
    ("GDP (World Bank)", gdp23, "official"),
    ("BPS national e-commerce value", bps23.transaction_value_idr_trillion * 1000 / FX, "survey of e-commerce businesses"),
    ("  of which BPS marketplace category", bps23.marketplace_value_idr_trillion * 1000 / FX, "survey, sales-media split"),
    ("  of which outside marketplace category", bps23.nonmarketplace_value_idr_trillion * 1000 / FX, "survey, sales-media split"),
    ("Three-platform transaction value (Grab constructed, Tokopedia, Shopee estimate)", fy23["V"], "mixed: reported/constructed/estimated"),
    ("Three-platform recognized revenue", fy23["R"], "mixed"),
    ("Three-platform wedge V-R", fy23["W"], "arithmetic"),
], columns=["layer", "usd_bn", "basis"])
ladder["pct_of_gdp"] = 100 * ladder.usd_bn / gdp23
ladder.round(3).to_csv(OUT / "visibility_ladder_2023.csv", index=False)

# 2. Value-added scenarios: what is the MOST that could be 'hidden GDP' if the wedge were all informal sales?
#    V is gross sales, not value added; value added = margin * V. Margins are SCENARIOS, not estimates.
sc = []
for label, base in (("platform wedge (US$40.07bn)", fy23["W"]),
                    ("BPS e-commerce total (US$72.25bn)", bps23.transaction_value_idr_trillion * 1000 / FX),
                    ("BPS outside-marketplace (US$59.1bn)", bps23.nonmarketplace_value_idr_trillion * 1000 / FX)):
    for margin in (0.05, 0.10, 0.20, 0.30):
        sc.append(dict(base=label, assumed_value_added_share=margin, value_added_usd_bn=base * margin,
                       pct_of_gdp=100 * base * margin / gdp23))
pd.DataFrame(sc).round(3).to_csv(OUT / "hidden_value_added_scenarios.csv", index=False)

# 3. Cross-platform take-rate table (levels, medians by firm, with issuer definitions)
dm = pd.read_csv(GE / "global_platform_definition_map.csv")
xp = lv.groupby("firm").agg(years=("year", "size"), first=("year", "min"), last=("year", "max"),
                           m_first=("monetization_rate_pct", "first"), m_last=("monetization_rate_pct", "last"),
                           m_median=("monetization_rate_pct", "median"), E_median=("E", "median")).round(3)
xp.to_csv(OUT / "cross_platform_take_rates.csv")
dm[["issuer", "segment", "transaction_metric", "revenue_metric", "transaction_definition", "revenue_definition", "currency"]] \
    .to_csv(OUT / "cross_platform_definitions.csv", index=False)

# 4. Incentive leverage: R = G - I, so dR/R = (G/R) dG/G - (I/R) dI/I.
#    Tokopedia (GoTo annual report levels as quoted in repo deck files; changes verified against measurement CSV).
G22, G23, I22, I23 = 8.14, 8.99, 4.11, 2.81     # IDR trillion
R22, R23 = G22 - I22, G23 - I23
tok_lev = dict(gross22=G22, gross23=G23, incent22=I22, incent23=I23, net22=R22, net23=R23,
               incentive_share_of_gross_22=I22 / G22, incentive_share_of_gross_23=I23 / G23,
               leverage_G_over_R_22=G22 / R22, leverage_G_over_R_23=G23 / R23,
               net_growth_pct=100 * (R23 / R22 - 1), gross_growth_pct=100 * (G23 / G22 - 1),
               incentive_change_pct=100 * (I23 / I22 - 1))
# Grab Q2 2026 (SEC 6-K via summary; verify against raw filing before use)
gr = dict(mobility_gmv=2214, mobility_rev=331, deliveries_gmv=4249, deliveries_rev=531, group_rev=997,
          incentives_total=706, incentives_pct_ondemand_gmv=10.9)
gr["mobility_take_pct"] = 100 * gr["mobility_rev"] / gr["mobility_gmv"]
gr["deliveries_take_pct"] = 100 * gr["deliveries_rev"] / gr["deliveries_gmv"]
od_gmv = gr["mobility_gmv"] + gr["deliveries_gmv"]; od_rev = gr["mobility_rev"] + gr["deliveries_rev"]
gr["ondemand_take_pct"] = 100 * od_rev / od_gmv
gr["gross_take_before_incentives_pct"] = gr["ondemand_take_pct"] + gr["incentives_pct_ondemand_gmv"]
gr["incentive_share_of_gross_take"] = gr["incentives_pct_ondemand_gmv"] / gr["gross_take_before_incentives_pct"]
json.dump(dict(tokopedia=tok_lev, grab_q2_2026_unverified=gr), open(OUT / "incentive_leverage.json", "w"), indent=2, default=float)
print("ladder/scenarios/xplatform/incentive tables written")
