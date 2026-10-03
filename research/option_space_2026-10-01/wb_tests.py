"""World Bank Enterprise Surveys, Indonesia 2023: registered tests W1-W3 (informal) and F1-F3 (formal), PREREGISTRATION.md addenda of 3 Oct 2026.
Data are licensed and never committed; pass the folder that holds the unzipped download.
Codes: 1 = yes, 2 = no, negative = missing. Weights: wmedian (informal and formal), wmedian_BR for the Version A e-payment question.
Run: python3 wb_tests.py <folder> -> tables/wb_tests_results.json"""
import json, pathlib, sys
import numpy as np, pandas as pd

root = pathlib.Path(sys.argv[1])
inf = pd.read_stata(root / "WBES-IS_Indonesia2023_Data/Indonesia-2023-ISES-full-data.dta", convert_categoricals=False)
fml = pd.read_stata(root / "WBES_Indonesia2023_Data/Indonesia-2023-full-data.dta", convert_categoricals=False)


def yes(s): return s.where(s.isin([1, 2])) == 1                  # NaN-aware: missing stays missing
def valid(s): return s.isin([1, 2])
def wmean(x, w):
    ok = x.notna() & w.notna()
    return float((x[ok] * w[ok]).sum() / w[ok].sum()) if ok.any() else float("nan")


out = {}
# ---- informal (unregistered businesses, six cities) ----
w = inf.wmedian
sm = inf.IDd3a
grp = {"social_media": sm == 1, "no_social_media": sm == 2}
out["n_informal"] = int(len(inf))
for k, g in grp.items():
    out[f"W1_records_{k}"] = 100 * wmean(yes(inf.ir4)[g & valid(inf.ir4)].astype(float), w[g & valid(inf.ir4)])
    # digital receipt among all firms in the group: k11e asked only of digital-money users, so non-users count as 'no'
    rec = np.where(inf.k11a == 2, 0.0, np.where(inf.k11e == 1, 1.0, np.where(inf.k11e == 2, 0.0, np.nan)))
    rec = pd.Series(rec, index=inf.index)
    out[f"W2_digital_receipt_{k}"] = 100 * wmean(rec[g], w[g])
    sales = inf.d6.where(inf.d6 >= 0) * 12
    out[f"W3_mean_annual_sales_Rp_{k}"] = wmean(sales[g], w[g])
    out[f"W3_median_annual_sales_Rp_{k}"] = float(sales[g].dropna().median()) if sales[g].notna().any() else float("nan")
out["share_social_media_weighted"] = 100 * wmean((sm == 1).astype(float)[valid(sm)], w[valid(sm)])

# ---- formal (5+ employees) ----
wf, wbr = fml.wmedian, fml.get("wmedian_BR")
site = fml.c22b
out["n_formal"] = int(len(fml))
for k, g in {"website": site == 1, "no_website": site == 2}.items():
    e = fml.k33_BR.where(fml.k33_BR >= 0)
    out[f"F1_epay_sales_share_{k}"] = wmean(e[g], wbr[g]) if wbr is not None else float("nan")
    # j36 is coded 1 = yes fully, 2 = yes partially, 3 = no (corrected after the first run; see addendum)
    jv = fml.j36.isin([1, 2, 3])
    out[f"F2_efile_any_{k}"] = 100 * wmean((fml.j36.isin([1, 2]))[g & jv].astype(float), wf[g & jv])
    out[f"F2_efile_fully_{k}"] = 100 * wmean((fml.j36 == 1)[g & jv].astype(float), wf[g & jv])
jv = fml.j36.isin([1, 2, 3])
out["check_efile_fully_all_firms"] = 100 * wmean((fml.j36 == 1)[jv].astype(float), wf[jv])
out["check_efile_any_all_firms"] = 100 * wmean((fml.j36.isin([1, 2]))[jv].astype(float), wf[jv])
both_no = (site == 2) & (fml.j36 == 3)
known = valid(site) & jv
out["F3_no_website_no_efile_share"] = 100 * wmean(both_no[known].astype(float), wf[known])

v = {"W1 (records higher with social media)": out["W1_records_social_media"] > out["W1_records_no_social_media"],
     "W2 (digital receipt higher with social media)": out["W2_digital_receipt_social_media"] > out["W2_digital_receipt_no_social_media"],
     "W3 (social-media sellers' mean annual sales < Rp100m)": out["W3_mean_annual_sales_Rp_social_media"] < 100e6,
     "F1 (e-pay share higher with website)": out["F1_epay_sales_share_website"] > out["F1_epay_sales_share_no_website"],
     "F2 (e-filing, fully or partially, higher with website)": out["F2_efile_any_website"] > out["F2_efile_any_no_website"],
     "F3 (no website and no e-filing > 1/3)": out["F3_no_website_no_efile_share"] > 100 / 3}
out["verdicts"] = {k: bool(x) for k, x in v.items()}
s = json.dumps(out, indent=1, default=float); print(s)
open(pathlib.Path(__file__).parent / "tables/wb_tests_results.json", "w").write(s)
