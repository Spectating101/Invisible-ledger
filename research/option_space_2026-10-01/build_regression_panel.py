"""Build the platform-year panel for Prof. Kong's regressions (25 Oct 2026). EXPLORATORY: designed after the data were seen.

One row per platform-year with transaction value V and revenue R, in US dollars, for the same 32 platforms as the H1 sample
(5 Indonesian and regional, 27 abroad), under the same rules as the H1 test (h1_extended.py):
  - the same series: Blibli 3P retail, Bukalapak group, Tokopedia and the on-demand businesses of Grab and GoTo; the 8 foreign platforms chosen first
    (tables/take_rate_levels.csv) and the 19 added (tables/spinoff_panel.csv, firm-years with own goods over half of revenue excluded);
  - a year with no transaction value or no revenue is missing and never filled.
Amounts are in millions of each company's reporting currency in the source tables, and are converted to US dollars at the World Bank's
period-average official rate (tables/src/wdi_extraction.csv). Total assets come from SEC filings (tables/src/total_assets_extraction.csv)
and, for the five platforms that do not file with the SEC, from tables/src/total_assets_manual.csv (if present).
Controls by the platform's main market and year: GDP growth, consumer-price inflation, household-consumption growth (World Bank WDI) and the
central-bank policy rate (BIS, annual mean). The take rate and its components are NOT regressors (Prof. Kong's rule; E = 1/m - 1).
Outputs: tables/platform_attributes.csv, tables/regression_panel.csv.
Run from this folder: python3 build_regression_panel.py"""
import numpy as np, pandas as pd

T = pd.read_csv("tables/take_rate_levels.csv")
P = pd.read_csv("tables/l_panel.csv")
S = pd.read_csv("tables/spinoff_panel.csv")
W = pd.read_csv("tables/src/wdi_extraction.csv")
B = pd.read_csv("tables/src/bis_policy_extraction.csv")
A = pd.read_csv("tables/src/total_assets_extraction.csv")
try: M = pd.read_csv("tables/src/total_assets_manual.csv")
except FileNotFoundError: M = pd.DataFrame(columns=["entity", "year", "value_millions", "unit", "source"])

# ---- platform attributes (author's classification; each choice is recorded with its reason) ----
# name used in the tables; group; type; main market (World Bank country code); reporting currency; listing year (as in h1_extended.py)
ATTR = [
 # key,                          label,               grp,   type,           mkt, cur,   listed, note
 ("Tokopedia e-commerce segment", "Tokopedia",         "IDN", "marketplace",  "ID", "IDR", 2022, "segment of GoTo, listed on the Indonesia Stock Exchange in 2022"),
 ("Blibli 3P Retail",            "Blibli",            "IDN", "marketplace",  "ID", "IDR", 2022, "third-party retail segment; includes online travel"),
 ("Bukalapak Group",             "Bukalapak",         "IDN", "marketplace",  "ID", "IDR", 2021, "whole group, mainly Indonesia"),
 ("Grab on-demand",              "Grab (on-demand)",  "IDN", "on-demand",    "ID", "USD", 2021, "Southeast Asia; Indonesia taken as the main market"),
 ("GoTo on-demand",              "GoTo (on-demand)",  "IDN", "on-demand",    "ID", "IDR", 2022, "Indonesia and Vietnam to 2024"),
 ("Etsy",                        "Etsy",              "FOR", "marketplace",  "US", "USD", 2015, ""),
 ("eBay",                        "eBay",              "FOR", "marketplace",  "US", "USD", 1998, ""),
 ("Jumia",                       "Jumia",             "FOR", "marketplace",  "NG", "USD", 2019, "pan-African; Nigeria taken as the main market"),
 ("Mercado Libre",               "Mercado Libre",     "FOR", "marketplace",  "BR", "USD", 2007, "Latin America; Brazil is the largest market"),
 ("Rakuten",                     "Rakuten",           "FOR", "marketplace",  "JP", "JPY", 2000, "domestic e-commerce segment"),
 ("Sea / Shopee",                "Sea (Shopee)",      "FOR", "marketplace",  "ID", "USD", 2017, "Shopee has Indonesia as a main market (Chapter 4)"),
 ("Shopify",                     "Shopify",           "FOR", "marketplace",  "US", "USD", 2015, "commerce platform; merchants mainly in the US"),
 ("Zalando",                     "Zalando",           "FOR", "marketplace",  "DE", "EUR", 2014, ""),
 ("ACVA",                        "ACV Auctions",      "FOR", "resale",       "US", "USD", 2021, "wholesale vehicle auctions"),
 ("ASAPQ",                       "Waitr",             "FOR", "on-demand",    "US", "USD", 2018, "food delivery"),
 ("BABA",                        "Alibaba",           "FOR", "marketplace",  "CN", "CNY", 2014, ""),
 ("DESP",                        "Despegar",          "FOR", "travel",       "AR", "USD", 2017, "Latin America; Argentina is the headquarters"),
 ("DIBS",                        "1stDibs",           "FOR", "resale",       "US", "USD", 2021, ""),
 ("EXPE",                        "Expedia",           "FOR", "travel",       "US", "USD", 2005, ""),
 ("FVRR",                        "Fiverr",            "FOR", "freelance",    "US", "USD", 2019, "Israeli company; customers mainly in the US"),
 ("GrubHub",                     "Grubhub",           "FOR", "on-demand",    "US", "USD", 2014, "food delivery"),
 ("HEPS",                        "Hepsiburada",       "FOR", "marketplace",  "TR", "TRY", 2021, ""),
 ("KSPI",                        "Kaspi.kz",          "FOR", "marketplace",  "KZ", "KZT", 2020, "payments, marketplace and fintech"),
 ("MOGU",                        "Mogu",              "FOR", "marketplace",  "CN", "CNY", 2018, ""),
 ("Ozon",                        "Ozon",              "FOR", "marketplace",  "RU", "RUB", 2020, ""),
 ("PDD",                         "Pinduoduo",         "FOR", "marketplace",  "CN", "CNY", 2018, ""),
 ("RBA",                         "RB Global",         "FOR", "resale",       "US", "USD", 1998, "industrial auctions"),
 ("REAL",                        "The RealReal",      "FOR", "resale",       "US", "USD", 2019, ""),
 ("SEAT",                        "Vivid Seats",       "FOR", "travel",       "US", "USD", 2021, "ticketing"),
 ("UPWK",                        "Upwork",            "FOR", "freelance",    "US", "USD", 2018, ""),
 ("VCSA",                        "Vacasa",            "FOR", "travel",       "US", "USD", 2021, "vacation rentals"),
 ("YTRA",                        "Yatra",             "FOR", "travel",       "IN", "INR", 2016, ""),
]
attr = pd.DataFrame(ATTR, columns=["key", "platform", "grp", "type", "market", "currency", "listed", "note"])
attr["indonesia_region"] = (attr.grp == "IDN").astype(int)
attr["emerging_market"] = attr.market.isin(["ID", "NG", "BR", "AR", "CN", "TR", "KZ", "RU", "IN"]).astype(int)
attr.to_csv("tables/platform_attributes.csv", index=False)

# ---- levels of V and R, millions of reporting currency ----
parts = []
tk = T[T.firm.isin(["Tokopedia e-commerce segment", "Blibli 3P Retail", "Bukalapak Group", "Etsy", "eBay", "Jumia", "Mercado Libre", "Rakuten", "Sea / Shopee", "Shopify", "Zalando"])]
parts.append(tk.rename(columns={"firm": "key", "transaction_value": "V", "revenue_value": "R"})[["key", "year", "V", "R"]])
grab = P[P.firm == "Grab"].groupby("year")[["V", "R"]].sum().reset_index().assign(key="Grab on-demand")
goto = P[(P.firm == "GoTo") & (P.seg == "On-demand")][["year", "V", "R"]].assign(key="GoTo on-demand")
parts.append(pd.concat([grab, goto])[lambda d: d.R > 0][["key", "year", "V", "R"]])
new = S[(S.flag_1p != "exclude") & S.entity.isin(attr.key)].rename(columns={"entity": "key", "revenue": "R"})[["key", "year", "V", "R"]]
parts.append(new)
L = pd.concat(parts, ignore_index=True).dropna(subset=["V", "R"])
# Blibli's series in take_rate_levels.csv is in IDR billion; every other series is in millions of its currency
for c in ("V", "R"): L.loc[L.key == "Blibli 3P Retail", c] *= 1000
L = L[(L.V > 0) & (L.R > 0)].drop_duplicates(["key", "year"]).sort_values(["key", "year"]).reset_index(drop=True)
L = L.merge(attr, on="key", how="inner")

# ---- exchange rates (LCU per US$, period average) ----
CTRY = {"USD": "US", "IDR": "ID", "CNY": "CN", "JPY": "JP", "EUR": "DE", "KZT": "KZ", "RUB": "RU", "TRY": "TR", "INR": "IN"}
fx = W[W.indicator == "PA.NUS.FCRF"].pivot(index="year", columns="country", values="value")
L["fx"] = [1.0 if c == "USD" else fx.loc[y, CTRY[c]] if y in fx.index else np.nan for c, y in zip(L.currency, L.year)]
L = L[L.fx.notna()].copy()      # no World Bank rate yet for 2026: Mogu and Yatra FY2026 drop out
for c in ("V", "R"): L[c + "_usd"] = L[c] / L.fx
L["wedge_usd"] = L.V_usd - L.R_usd
L["ln_wedge_usd"] = np.log(L.wedge_usd)
L["ecosystem_ratio"] = L.wedge_usd / L.R_usd
L["ln_V_usd"] = np.log(L.V_usd)

# ---- growth, simple percentage change within the retained series (consecutive years only) ----
L = L.sort_values(["key", "year"])
for c in ("V", "R"):
    prev = L.groupby("key")[c].shift(); gap = L.groupby("key").year.diff()
    L["g_" + c] = np.where(gap == 1, L[c] / prev - 1, np.nan)

# ---- platform characteristics ----
L["years_listed"] = (L.year - L.listed).clip(lower=0)
L["ln1_years_listed"] = np.log1p(L.years_listed)
L["pre_listing"] = (L.year < L.listed).astype(int)

# ---- total assets, millions of reporting currency -> US dollars ----
a = A[A.entity.isin(attr.key)].copy()
a = a.merge(attr[["key", "currency"]], left_on="entity", right_on="key")
a = a[a.unit == a.currency].assign(value_millions=lambda d: d.value / 1e6)[["entity", "year", "value_millions"]].rename(columns={"entity": "key"})
m = M.rename(columns={"entity": "key"})[["key", "year", "value_millions"]] if len(M) else pd.DataFrame(columns=["key", "year", "value_millions"])
assets = pd.concat([a, m]).drop_duplicates(["key", "year"], keep="last")
L = L.merge(assets.rename(columns={"value_millions": "assets_lcu"}), on=["key", "year"], how="left")
L["assets_lcu"] = pd.to_numeric(L.assets_lcu, errors="coerce")
L["assets_usd"] = L.assets_lcu / L.fx
L["ln_assets_usd"] = np.log(L.assets_usd)

# ---- home-market macro controls ----
wide = W.pivot_table(index=["country", "year"], columns="indicator", values="value").reset_index()
wide = wide.rename(columns={"NY.GDP.MKTP.KD.ZG": "gdp_growth", "FP.CPI.TOTL.ZG": "inflation", "NE.CON.PRVT.KD.ZG": "household_growth"})
B["year"] = B.month.str[:4].astype(int); B["country"] = B.country.replace({"XM": "DE"})
pol = B.groupby(["country", "year"]).policy_rate_pct.mean().reset_index().rename(columns={"policy_rate_pct": "policy_rate"})
L = L.merge(wide[["country", "year", "gdp_growth", "inflation", "household_growth"]], left_on=["market", "year"], right_on=["country", "year"], how="left").drop(columns="country")
L = L.merge(pol, left_on=["market", "year"], right_on=["country", "year"], how="left").drop(columns="country")

cols = ["key", "platform", "grp", "indonesia_region", "type", "market", "emerging_market", "currency", "year", "V", "R", "fx", "V_usd", "R_usd", "wedge_usd",
        "ln_wedge_usd", "ecosystem_ratio", "ln_V_usd", "g_V", "g_R", "listed", "years_listed", "ln1_years_listed", "pre_listing", "assets_usd", "ln_assets_usd",
        "gdp_growth", "inflation", "household_growth", "policy_rate"]
L = L[cols].sort_values(["grp", "platform", "year"]).reset_index(drop=True)
L.to_csv("tables/regression_panel.csv", index=False)
print(L.shape, "platform-years;", L.key.nunique(), "platforms;", (L.grp == "IDN").sum(), "Indonesian and regional rows")
print("non-missing:", {c: int(L[c].notna().sum()) for c in ["ln_wedge_usd", "g_V", "g_R", "ln_assets_usd", "gdp_growth", "inflation", "household_growth", "policy_rate"]})
print("platforms with no assets:", sorted(set(L.platform) - set(L[L.assets_usd.notna()].platform)))
