"""EXPLORATORY check (15 Oct 2026): does the way foreign platforms book incentives paid to end users explain the H1 gap?

Designed AFTER the H1 result was known. Not a pre-registered test. Not evidence for or against H1 in the registered sense.

Classes come from reading each platform's revenue-recognition policy (see INCENTIVE_ACCOUNTING.md in this folder):
  DEDUCTS  end-user incentives reduce revenue
  EXPENSES end-user incentives are booked as sales and marketing (or cost of revenue), not against revenue
  MIXED    rule-based split (e.g. Sea: reduce revenue up to the revenue from that order, excess to marketing)
  NA       no material end-user incentives disclosed
Inputs (read only): ../tables/h1_extended_firms.csv (one median |dln take rate| per platform, built by h1_extended.py),
                    ../tables/spinoff_panel.csv (for the Yatra variant without its IFRS 15 break year).
Run from this folder: python3 incentive_accounting_check.py  -> prints JSON; writes nothing."""
import json, pathlib
import numpy as np, pandas as pd
from scipy import stats

HERE = pathlib.Path(__file__).parent
F = pd.read_csv(HERE.parent / "tables/h1_extended_firms.csv")
S = pd.read_csv(HERE.parent / "tables/spinoff_panel.csv")

CLASS = {
    # explicit EXPENSES statements in the filings
    "eBay": "EXPENSES", "DIBS": "EXPENSES", "PDD": "EXPENSES", "MOGU": "EXPENSES",
    # EXPENSES, weaker evidence (inferred, small, or late in the window)
    "BABA": "EXPENSES_WEAK", "Rakuten": "EXPENSES_WEAK", "Shopify": "EXPENSES_WEAK", "Etsy": "EXPENSES_WEAK",
    # rule-based split or partly unclear
    "Sea / Shopee": "MIXED", "Mercado Libre": "MIXED", "Ozon": "MIXED",
    # deduct from revenue
    "ACVA": "DEDUCTS", "ASAPQ": "DEDUCTS", "DESP": "DEDUCTS", "EXPE": "DEDUCTS", "GrubHub": "DEDUCTS",
    "HEPS": "DEDUCTS", "Jumia": "DEDUCTS", "KSPI": "DEDUCTS", "REAL": "DEDUCTS", "SEAT": "DEDUCTS",
    "Zalando": "DEDUCTS",
    "YTRA": "CHANGED",  # marketing expense until FY2018, reduction of revenue from FY2019 (IFRS 15, not restated)
    # no material end-user incentives
    "FVRR": "NA", "UPWK": "NA", "VCSA": "NA", "RBA": "NA",
}
rng = np.random.default_rng(20261015)
IDN = F[F.group == "Indonesia"].set_index("firm").median_abs
FOR = F[F.group != "Indonesia"].set_index("firm").median_abs
assert set(FOR.index) == set(CLASS), set(FOR.index) ^ set(CLASS)

# Yatra without the FY2018->FY2019 pair, the year its incentive accounting changed
y = S[(S.entity == "YTRA") & S.g_m.notna() & (S.flag_1p != "exclude")]
ytra_ex2019 = float(y[y.year != 2019].g_m.abs().median())


def test(foreign, label):
    xa, xb = IDN.values, foreign.values
    obs = np.median(xa) - np.median(xb); pool = np.concatenate([xa, xb]); k = len(xa); hits = 0
    for _ in range(9999):
        rng.shuffle(pool); hits += (np.median(pool[:k]) - np.median(pool[k:])) >= obs
    return {"label": label, "foreign_platforms": len(xb), "median_indonesia": round(float(np.median(xa)), 4),
            "median_foreign": round(float(np.median(xb)), 4),
            "mannwhitney_p": round(float(stats.mannwhitneyu(xa, xb, alternative="greater").pvalue), 4),
            "shuffle_p": round((hits + 1) / 10000, 4)}


cls = pd.Series(CLASS)
res = {"class_counts": cls.value_counts().to_dict(),
       "class_medians_of_platform_medians": {c: round(float(FOR[cls[cls == c].index].median()), 4) for c in cls.unique()},
       "ytra_median_all_pairs": round(float(FOR["YTRA"]), 4), "ytra_median_without_FY2019_pair": round(ytra_ex2019, 4)}
drop = lambda classes: FOR[~FOR.index.isin(cls[cls.isin(classes)].index)]
res["tests"] = [
    test(FOR, "all 27 (reproduces the main test)"),
    test(drop(["EXPENSES"]), "drop 4 with an explicit EXPENSES policy"),
    test(drop(["EXPENSES", "EXPENSES_WEAK"]), "drop all 8 EXPENSES (explicit and weaker)"),
    test(drop(["EXPENSES", "EXPENSES_WEAK", "CHANGED"]), "drop 8 EXPENSES and Yatra"),
    test(drop(["EXPENSES", "EXPENSES_WEAK", "MIXED", "CHANGED"]), "keep only DEDUCTS and NA"),
    test(FOR[cls[cls == "DEDUCTS"].index], "keep only DEDUCTS"),
    test(FOR.drop("YTRA").pipe(lambda s: pd.concat([s, pd.Series({"YTRA": ytra_ex2019})])), "all 27, Yatra without FY2019 pair"),
]
# within the foreign group: do EXPENSES platforms move less than DEDUCTS platforms? (two-sided)
e = FOR[cls[cls.isin(["EXPENSES", "EXPENSES_WEAK"])].index]; d = FOR[cls[cls == "DEDUCTS"].index]
res["foreign_EXPENSES_vs_DEDUCTS"] = {"n": [len(e), len(d)], "median_expenses": round(float(e.median()), 4),
                                      "median_deducts": round(float(d.median()), 4),
                                      "mannwhitney_p_two_sided": round(float(stats.mannwhitneyu(e, d).pvalue), 4)}
print(json.dumps(res, indent=1))
