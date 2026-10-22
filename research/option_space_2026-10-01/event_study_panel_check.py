"""Announcement-return regressions re-run on the COMMITTED derived panels (22 Oct 2026, exploratory). Prices and consensus estimates are licensed and not
in the repository, so the panels cannot be rebuilt here; this only re-estimates the regressions of event_study.py and event_study_surprise.py on them.
car ~ gV + dm + firm effects, and car ~ S + S x highdm + highdm + firm effects; errors clustered by calendar quarter of the announcement.
Run: python3 event_study_panel_check.py -> tables/event_study_panel_check.json"""
import json
import numpy as np, pandas as pd, statsmodels.formula.api as smf
T = "tables/"
E = pd.read_csv(T + "event_study_panel.csv"); S = pd.read_csv(T + "event_study_surprise_panel.csv")
def fit(form, d):
    r = smf.ols(form, d).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(d.cal_q)[0]})
    out = {k: {"coef": float(r.params[k]), "se": float(r.bse[k]), "p_two_sided": float(r.pvalues[k])} for k in r.params.index if not k.startswith(("C(", "Intercept"))}
    if "gV" in r.params and "dm" in r.params:
        t = r.t_test("gV - dm = 0"); out["gV_minus_dm"] = {"coef": float(np.squeeze(t.effect)), "p_two_sided": float(np.squeeze(t.pvalue))}
    out["n"] = int(r.nobs); return out
res = {"announcements": int(len(E)), "firms": int(E.firm.nunique()), "calendar_quarters": int(E.cal_q.nunique()),
       "A_volume_and_take_rate": fit("car ~ gV + dm + C(firm)", E),
       "surprise_announcements": int(len(S)), "surprise_firms": int(S.firm.nunique()),
       "B_surprise": fit("car ~ S + C(firm)", S),
       "C_surprise_x_high_take_rate_change": fit("car ~ S + Sx + highdm + C(firm)", S),
       "reading": "no coefficient is distinguishable from zero; the revenue surprise itself is not detected, so the sample cannot show whether its take-rate part is priced differently"}
s = json.dumps(res, indent=1); print(s); open(T + "event_study_panel_check.json", "w").write(s)
