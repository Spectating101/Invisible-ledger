"""Cross-country World Bank check (X2, X3; PREREGISTRATION.md addendum of 3 Oct 2026, late night).
Latest formal Enterprise Survey per country; j36 coding read from each file's value labels; weight wmedian. Licensed data, never committed.
Run: python3 wb_crosscountry.py <folder with Indonesia 2023 file> <folder with the other country files> -> tables/wb_crosscountry.csv"""
import json, pathlib, sys
import pandas as pd

ido, xc = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
FILES = {"Indonesia": ido / "WBES_Indonesia2023_Data/Indonesia-2023-full-data.dta", "Malaysia": xc / "Malaysia-2024-full-data.dta",
         "Viet Nam": xc / "Viet-Nam-2023-full-data.dta", "Thailand": xc / "Thailand-2025-full-data.dta",
         "Philippines": xc / "Philippines-2023-full-data.dta", "Cambodia": xc / "Cambodia-2023-full-data.dta", "Singapore": xc / "Singapore-2023-full-data.dta"}
PUBLISHED_EFILE = {"Indonesia": 37.5, "Malaysia": 86.2, "Thailand": 83.4, "Viet Nam": 99.6, "Philippines": 63.3, "Cambodia": 56.6, "Singapore": 99.9}


rows = []
for c, f in FILES.items():
    with pd.io.stata.StataReader(f) as r:
        d = r.read(convert_categoricals=False); vl = r.value_labels(); lbl = dict(zip(d.columns, r._lbllist))
    labs = {int(k): v.lower() for k, v in vl.get(lbl.get("j36", ""), {}).items()}
    yes_codes = [k for k, v in labs.items() if v.startswith("yes")]
    no_codes = [k for k, v in labs.items() if v.startswith("no")]
    jv = d.j36.isin(yes_codes + no_codes); w = d.wmedian
    efile = float(100 * w[jv & d.j36.isin(yes_codes)].sum() / w[jv].sum())
    site_ok = d.c22b.isin([1, 2])
    def efile_in(g):
        m = jv & g
        return float(100 * w[m & d.j36.isin(yes_codes)].sum() / w[m].sum()) if m.any() else float("nan")
    known = site_ok & jv
    neither = float(100 * w[known & (d.c22b == 2) & d.j36.isin(no_codes)].sum() / w[known].sum())
    rows.append({"country": c, "firms": len(d), "j36_labels": labs, "efile_share": round(efile, 1), "published_efile": PUBLISHED_EFILE[c],
                 "data_check_pass": abs(efile - PUBLISHED_EFILE[c]) <= 1, "efile_with_website": round(efile_in(d.c22b == 1), 1),
                 "efile_without_website": round(efile_in(d.c22b == 2), 1), "neither_share": round(neither, 1)})
t = pd.DataFrame(rows)
t.drop(columns=["j36_labels"]).to_csv(pathlib.Path(__file__).parent / "tables/wb_crosscountry.csv", index=False)
print(t.drop(columns=["j36_labels"]).to_string(index=False)); print(t[["country", "j36_labels"]].to_string(index=False))
use = t[t.data_check_pass].set_index("country")
x2 = [c for c in ("Malaysia", "Thailand", "Philippines", "Cambodia") if c in use.index]
x2_hits = [c for c in x2 if use.loc[c, "efile_with_website"] > use.loc[c, "efile_without_website"]]
ido_n = t.set_index("country").loc["Indonesia", "neither_share"]
x3 = [c for c in ("Malaysia", "Thailand", "Viet Nam", "Singapore", "Philippines") if c in use.index]
x3_viol = [c for c in x3 if use.loc[c, "neither_share"] > ido_n]
print(json.dumps({"X2_holds_in": x2_hits, "X2_counted": x2, "X2_verdict": len(x2_hits) >= 3,
                  "X3_higher_than_Indonesia": x3_viol, "X3_counted": x3, "X3_verdict": len(x3_viol) == 0}, indent=1))
