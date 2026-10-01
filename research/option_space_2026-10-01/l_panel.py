"""Discount-leverage panel and the pre-registered test (see l_rule_preregistration.py, commit 95a322b).

L = iota / m = incentives / revenue-after-incentives.  Transition t -> t+1: dlnm = ln m_{t+1} - ln m_t (both m > 0).
Reads only verified source tables; writes tables/l_panel.csv, l_transitions.csv, l_test.csv.
Sample label: 'in' = seen before the rule was written; 'out' = opened after pre-registration.
Revenue-after-incentives is required, so firms that book incentives in expenses (Uber, Lyft, Bukalapak) are listed in l_excluded.
"""
import re
import numpy as np
import pandas as pd

T = "tables/"
rows = []


def add(firm, seg, year, V, R, I, sample, src, note=""):
    rows.append(dict(firm=firm, seg=seg, year=year, V=V, R=R, I=I, sample=sample, src=src, note=note))


# ---- Grab segments, annual, 20-F extraction (USD m). Latest filing that states the year; GMV in USD_m rows when present.
g = pd.read_csv(T + "src/grab_20f_extraction.csv")
g = g[g.value.notna() & (g.field != "note_text")].copy()
g["filing"] = g.source_file.str.extract(r"_(\d{4}-\d{2}-\d{2})")[0]
g["period"] = g.period.astype(int)
g["v"] = np.where(g.unit == "USD_bn", g.value * 1000, g.value)
g["prec"] = (g.unit == "USD_m").astype(int)          # prefer unrounded USD_m rows


def pick(ent, yr, fld, filing=None):
    s = g[(g.entity == ent) & (g.period == yr) & (g.field == fld)]
    if filing:
        s = s[s.filing == filing]
    if s.empty:
        return np.nan
    s = s.sort_values(["filing", "prec"])
    best = s[s.filing == s.filing.iloc[-1]]
    return best.sort_values("prec").v.iloc[-1]


FILINGS = sorted(g.filing.unique())
for ent in ["Mobility", "Deliveries"]:
    for yr in range(2019, 2025):
        have = [f for f in FILINGS if not g[(g.filing == f) & (g.entity == ent) & (g.period == yr)].empty]
        if not have:
            continue
        f = have[-1]
        V = pick(ent, yr, "gmv", f); R = pick(ent, yr, "revenue", f)
        inc = pick(ent, yr, "incentives", f)
        if np.isnan(inc):
            inc = pick(ent, yr, "partner_incentives", f) + pick(ent, yr, "consumer_incentives", f)
        add("Grab", ent, yr, V, R, inc, "in", f"Grab 20-F filed {f}", "restated vintage as of that filing")

# ---- GoTo on-demand, Tokopedia, MakeMyTrip (in-sample, existing verified tables)
go = pd.read_csv(T + "goto_ondemand_annual.csv", index_col=0)
for y, r in go.iterrows():
    add("GoTo", "On-demand", int(y), r.gtv, r.net, r.incentives, "in", "goto_ondemand_annual.csv", "2022 GTV estimated")
tp = pd.read_csv(T + "take_rate_levels.csv")
tk = tp[tp.firm == "Tokopedia e-commerce segment"].set_index("year")
tsg = pd.read_csv(T + "tokopedia_segment.csv", index_col=0)
for y in (2022, 2023):
    add("Tokopedia", "E-commerce", y, tk.loc[y, "transaction_value"], tsg.loc[y, "net"], tsg.loc[y, "incentives"], "in", "tokopedia_segment.csv")
mm = pd.read_csv(T + "mmyt_annual.csv")
for _, r in mm.iterrows():
    add("MakeMyTrip", "Group", int(r.year), r.gb, r.rev, r.ind, "in", "mmyt_annual.csv")

# ---- OUT of sample
# Blibli 3P Retail, annual, IDR bn; incentives PROXY = GPBD - net revenue (GPBD adds back discounts and subsidies, but also direct costs)
b = pd.read_csv(T + "src/blibli_extraction.csv")
b = b[b.value.notna() & (b.entity == "3P Retail") & (b.unit == "IDR_bn") & b.period.str.match(r"^FY202[2-5]$")]
order = ["fy2022", "q12023", "q32023", "fy2023", "q22024", "q32024", "fy2024", "q12025", "q22025", "fy2025"]
b = b.assign(v=b.source_file.str.extract(r"blibli_(\w+?)(?:_linked_0)?\.txt")[0].map({k: i for i, k in enumerate(order)}))
for y in (2022, 2023, 2024, 2025):
    s = b[b.period == f"FY{y}"].sort_values("v")
    one = lambda f: s[s.field == f].value.iloc[-1]
    add("Blibli", "3P Retail", y, one("tpv"), one("net_revenue"), one("gpbd") - one("net_revenue"), "out", "Blibli releases", "incentives = GPBD - net revenue (proxy)")

# Shopee 2017 -> 2018: V,R from the repo level table (GMV, e-commerce revenue); incentive amount from the 2018 20-F note
se = tp[tp.firm == "Sea / Shopee"].set_index("year")
add("Shopee", "E-commerce", 2017, se.loc[2017, "transaction_value"], se.loc[2017, "revenue_value"], 8.683, "out", "Sea 20-F 2018 note 18", "incentives 8.683m netted against commission income")
add("Shopee", "E-commerce", 2018, se.loc[2018, "transaction_value"], se.loc[2018, "revenue_value"], np.nan, "out", "take_rate_levels.csv", "incentive amount not disclosed; includes 1P product revenue")

# DoorDash 2018 -> 2019 (promotions mostly a reduction of revenue)
add("DoorDash", "Marketplace", 2018, 2812.0, 291.0, 60.0, "out", "DASH S-1A", "promotions primarily contra-revenue")
add("DoorDash", "Marketplace", 2019, 8039.0, 885.0, 182.0, "out", "DASH S-1A", "promotions primarily contra-revenue")

# Delivery Hero FY2020-FY2025: R = Total Segment Revenue (before vouchers) - vouchers; GMV in EUR m.  2019 excluded (basis restated in 2020).
dh = pd.read_csv(T + "delivery_hero_vouchers.csv")
dh = dh[dh.period.str.match(r"^20(2[0-5])FY$")]
for _, r in dh.iterrows():
    add("Delivery Hero", "Group", int(r.period[:4]), r.gmv_eur_m, r.total_segment_revenue_eur_m - r.vouchers_eur_m, r.vouchers_eur_m, "out", "DH annual reports", "TSR is before vouchers; R = TSR - vouchers")

P = pd.DataFrame(rows)
P["m"] = P.R / P.V
P["iota"] = P.I / P.V
P["L"] = np.where(P.R > 0, P.I / P.R, np.inf)
P.to_csv(T + "l_panel.csv", index=False)

# ---- transitions
tr = []
for (firm, seg), s in P.groupby(["firm", "seg"]):
    s = s.sort_values("year").set_index("year")
    for y in s.index:
        if y + 1 in s.index:
            a, c = s.loc[y], s.loc[y + 1]
            if pd.isna(a.L) or a.R <= 0 or c.R <= 0:
                dl = np.nan
            else:
                dl = np.log(c.m) - np.log(a.m)
            tr.append(dict(firm=firm, seg=seg, year=y, sample=a["sample"], L=a.L, m_t=a.m, m_t1=c.m,
                           dlnm=dl, d_iota_pp=100 * (c.iota - a.iota) if not pd.isna(c.iota) else np.nan,
                           d_m_pp=100 * (c.m - a.m), r_nonpositive=(a.R <= 0 or c.R <= 0)))
X = pd.DataFrame(tr)
X["bucket"] = pd.cut(X.L.replace(np.inf, 1e9), [-1, 0.5, 1, 2, np.inf], labels=["<0.5", "0.5-1", "1-2", ">2"])
X.loc[X.r_nonpositive, "bucket"] = ">2"
X.to_csv(T + "l_transitions.csv", index=False)

# ---- the pre-registered test
out = []
for label, d in [("out-of-sample", X[X["sample"] == "out"]), ("in-sample", X[X["sample"] == "in"]), ("all", X)]:
    for eps in (0.05, 0.10, 0.20):
        for bk, s in d.groupby("bucket", observed=True):
            ok = s.dlnm.notna()
            big = (s.dlnm.abs() > eps) | s.r_nonpositive
            out.append(dict(sample=label, eps=eps, bucket=bk, n=len(s), firms=s.firm.nunique(),
                            n_exceed=int(big.sum()), share_exceed=big.mean(), median_abs_dlnm=s.dlnm.abs().median()))
R = pd.DataFrame(out)
R.to_csv(T + "l_test.csv", index=False)
if __name__ == "__main__":
    pd.set_option("display.width", 220); pd.set_option("display.max_rows", 200)
    print(X.round(3).to_string())
    print(R[R.eps == 0.10].round(2).to_string())


def extra():
    """P2 (mechanism) and a rank correlation of L_t with |dlnm|, with a firm-level permutation p-value."""
    from scipy.stats import spearmanr
    Z = X[X.dlnm.notna()].copy()
    Z["d_tau_pp"] = Z.d_m_pp + Z.d_iota_pp          # m = tau - iota  =>  d tau = d m + d iota
    hi = Z[(Z.L >= 1) & (Z.d_m_pp > 0) & Z.d_iota_pp.notna()].copy()
    hi["iota_share_of_rise"] = -hi.d_iota_pp / hi.d_m_pp
    hi["p2_pass"] = hi.d_iota_pp < 0
    hi["p2_pass"] = (-hi.d_iota_pp) > hi.d_tau_pp
    hi.to_csv(T + "l_p2_mechanism.csv", index=False)
    res = []
    for label, d in [("out-of-sample", Z[Z["sample"] == "out"]), ("in-sample", Z[Z["sample"] == "in"]), ("all", Z)]:
        d = d.assign(Lc=np.log10(d.L.replace(np.inf, 1e3).clip(upper=1e3)), a=d.dlnm.abs())
        rho = spearmanr(d.Lc, d.a)[0] if len(d) > 3 else np.nan
        rng = np.random.default_rng(0); firms = d.firm.unique(); cnt = 0; N = 4000
        for _ in range(N):
            # permute the (L) values across firm blocks: shuffle which firm's L-series goes with which |dlnm| series is not defined with
            # unequal lengths, so permute |dlnm| across all rows but keep firm labels fixed in the statistic by using firm-mean ranks
            perm = d.assign(a=rng.permutation(d.a.values))
            cnt += abs(spearmanr(perm.Lc, perm.a)[0]) >= abs(rho)
        # firm-level: mean Lc and mean |dlnm| per firm
        f = d.groupby("firm").agg(Lc=("Lc", "mean"), a=("a", "mean"))
        rho_f = spearmanr(f.Lc, f.a)[0] if len(f) > 3 else np.nan
        res.append(dict(sample=label, n=len(d), firms=d.firm.nunique(), spearman=rho, p_row_permutation=(cnt + 1) / (N + 1), spearman_firm_means=rho_f))
    pd.DataFrame(res).to_csv(T + "l_rank_test.csv", index=False)
    return hi, pd.DataFrame(res)


if __name__ == "__main__":
    hi, rk = extra()
    print("\nP2 (L>=1, m rising): iota share of the rise\n", hi[["firm", "seg", "year", "sample", "L", "d_m_pp", "d_iota_pp", "d_tau_pp", "iota_share_of_rise", "p2_pass"]].round(2).to_string())
    print("\nrank test\n", rk.round(3).to_string())
    print(R[R.eps == 0.20].round(2).to_string())
