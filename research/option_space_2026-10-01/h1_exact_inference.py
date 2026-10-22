"""H1: exact inference and four robustness checks (22 Oct 2026, EXPLORATORY: designed after the registered and exploratory H1 results were known).

Reads only committed tables. Does not change any registered result; it asks whether the main H1 result (5 Indonesian and regional platforms against 27
foreign ones, median |yearly change in log take rate| per platform) survives inference that does not rest on large-sample approximations.

A. Exact permutation test. All C(32,5) = 201,376 ways to pick which 5 of the 32 platforms form the Indonesian and regional group are enumerated; the p-value
   is the share of splits whose difference in group medians is at least the observed one (no random draws). Also the exact Mann-Whitney p (exact null
   distribution of U, no normal approximation; the committed 0.0038 uses scipy's normal approximation because the groups are larger than 8).
B. Size of the difference: the Hodges-Lehmann shift (median of the 135 pairwise differences) with a 95% interval from inverting the exact two-sided
   Mann-Whitney test; and a firm-level bootstrap interval for the ratio of group medians (unstable with 5 platforms; reported as such).
C. Sea moved to the regional group (6 against 26): Sea's Indonesian business is Shopee, but its company-wide figures are regional.
D. Drop any two of the five Indonesian and regional platforms (10 cases): worst-case exact p.
E. Young platforms only: firm-years up to 5 years after listing, same metric, group medians per platform (platforms with at least 2 such pairs).
Run from this folder: python3 h1_exact_inference.py -> tables/h1_exact_inference.json"""
import itertools, json, math, re
import numpy as np, pandas as pd

# ---- the committed firm-level medians (output of h1_extended.py)
F = pd.read_csv("tables/h1_extended_firms.csv")
assert len(F) == 32 and (F.group == "Indonesia").sum() == 5
IDN = F[F.group == "Indonesia"]
x = IDN.median_abs.values; y = F[F.group != "Indonesia"].median_abs.values
names = F.firm.tolist(); vals = F.median_abs.values

def u_null_counts(n1, n2):
    """Exact null counts of the Mann-Whitney U statistic: coefficients of the Gaussian binomial [n1+n2 choose n1]_q."""
    c = [1]
    for i in range(1, n1 + 1):
        # multiply by (1 - q^(n2+i)), then divide by (1 - q^i)
        d = c + [0] * (n2 + i)
        for k in range(len(c)):
            d[k + n2 + i] -= c[k]
        e = d[:]
        for k in range(i, len(e)):
            e[k] += e[k - i]
        c = e
    L = n1 * n2 + 1
    return np.array(c[:L], dtype=object)

def exact_mw_p(a, b):
    """One-sided exact p that U >= observed, U = number of pairs with a_i > b_j (ties count one half)."""
    n1, n2 = len(a), len(b)
    u = sum((ai > bj) + 0.5 * (ai == bj) for ai in a for bj in b)
    cnt = u_null_counts(n1, n2); tot = sum(cnt)
    k = int(math.ceil(u))
    return float(sum(cnt[k:]) / tot), float(u)

def exact_perm_p(vals, k):
    """Exact p over all C(n,k) splits, statistic = median(group of k) - median(rest); group of k are the 'Indonesian' labels."""
    n = len(vals); obs_idx = None
    combos = np.array(list(itertools.combinations(range(n), k)), dtype=np.int16)
    mask = np.zeros((len(combos), n), dtype=bool)
    mask[np.arange(len(combos))[:, None], combos] = True
    V = np.broadcast_to(vals, mask.shape)
    in_ = np.sort(np.where(mask, V, np.inf), axis=1)[:, : k]
    out_ = np.sort(np.where(~mask, V, np.inf), axis=1)[:, : n - k]
    stat = np.median(in_, axis=1) - np.median(out_, axis=1)
    return stat, len(combos)

# ---------- A. exact tests
obs = float(np.median(x) - np.median(y))
stat, ncomb = exact_perm_p(vals, 5)
labels_obs = IDN.index.values
p_perm = float((stat >= obs - 1e-12).sum() / ncomb)
p_mw, U = exact_mw_p(x, y)
res = {"A_exact": {"firms_idn": 5, "firms_foreign": 27, "median_idn": float(np.median(x)), "median_foreign": float(np.median(y)),
                    "difference_in_medians": obs, "splits_enumerated": int(ncomb), "exact_permutation_p": p_perm,
                    "exact_mannwhitney_p": p_mw, "U": U, "committed_normal_approx_p": 0.0038}}

# ---------- B. size of the difference
d = np.sort(np.array([xi - yj for xi in x for yj in y]))
N = len(d); cnt = u_null_counts(5, 27); tot = sum(cnt); cum = np.cumsum([int(v) for v in cnt]) / int(tot)
c_lo = int(np.max(np.where(cum <= 0.025)[0]))      # largest c with P(U <= c) <= 0.025
lo, hi = float(d[c_lo]), float(d[N - c_lo - 1])    # d is 0-indexed: d_(c_lo+1) .. d_(N-c_lo)
hl = float(np.median(d))
rng = np.random.default_rng(20261022)
rat = []
for _ in range(20000):
    a = rng.choice(x, 5, replace=True); b = rng.choice(y, 27, replace=True); rat.append(np.median(a) / np.median(b))
res["B_size"] = {"hodges_lehmann_shift": hl, "ci95_low": lo, "ci95_high": hi,
                 "interval_method": "inversion of the exact two-sided Mann-Whitney test at 5%, coverage at least 95%",
                 "ratio_of_medians": float(np.median(x) / np.median(y)),
                 "ratio_bootstrap_ci95": [float(np.percentile(rat, 2.5)), float(np.percentile(rat, 97.5))],
                 "ratio_bootstrap_note": "firms resampled within group, 20,000 draws; unstable with 5 platforms"}

# ---------- C. Sea moved to the regional group
sea = F.index[F.firm == "Sea / Shopee"][0]
x2 = np.append(x, vals[sea]); y2 = np.delete(vals, np.append(IDN.index.values, sea))
mask_idx = np.append(IDN.index.values, sea)
stat6, n6 = exact_perm_p(vals, 6)
obs6 = float(np.median(x2) - np.median(y2))
p6, U6 = exact_mw_p(x2, y2)
res["C_sea_regional"] = {"firms_idn": 6, "firms_foreign": 26, "median_idn": float(np.median(x2)), "median_foreign": float(np.median(y2)),
                         "exact_permutation_p": float((stat6 >= obs6 - 1e-12).sum() / n6), "exact_mannwhitney_p": p6}

# ---------- D. drop any two of the five
rows = []
for pair in itertools.combinations(range(5), 2):
    keep = [i for i in range(5) if i not in pair]; xa = x[keep]
    p, _ = exact_mw_p(xa, y)
    rows.append({"dropped": [IDN.firm.iloc[i] for i in pair], "median_idn": float(np.median(xa)), "exact_mannwhitney_p": p})
res["D_drop_two"] = {"cases": rows, "worst_p": max(r["exact_mannwhitney_p"] for r in rows), "best_p": min(r["exact_mannwhitney_p"] for r in rows)}

# ---------- E. young platforms only (<= 5 years since listing), rebuilt exactly as h1_extended.py builds its yearly changes
src = open("h1_extended.py").read()
cut = src.index('allt["stage"]'); cut = src.index("\n", cut)
ns = {}
exec(compile(src[:cut], "h1_extended_head", "exec"), ns)
allt = ns["allt"]
y5 = allt[(allt.years_listed >= 0) & (allt.years_listed <= 5)]
per = y5.groupby(["firm", "group"]).agg(med=("abs", "median"), n=("abs", "size")).reset_index()
per = per[per.n >= 2]
gi = per[per.group == "Indonesia"].med.values; gf = per[per.group != "Indonesia"].med.values
pe, Ue = exact_mw_p(gi, gf)
res["E_young_only"] = {"rule": "firm-years up to 5 years after listing (listing years as in h1_extended.py); platforms with at least 2 such pairs",
                       "firms_idn": int(len(gi)), "firms_foreign": int(len(gf)), "median_idn": float(np.median(gi)), "median_foreign": float(np.median(gf)),
                       "exact_mannwhitney_p": pe}
s = json.dumps(res, indent=1); print(s); open("tables/h1_exact_inference.json", "w").write(s)
