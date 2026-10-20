"""Three rulers for the same economy, by quarter (3 Oct 2026, exploratory).

Ruler 1, official: household + NPISH final consumption, Indonesia (BPS national accounts via OECD QNA, not seasonally adjusted,
  rupiah, current and constant prices), saved in tables/src/oecd_qna_idn_2021_2026.csv (downloaded 3 Oct 2026 from sdmx.oecd.org).
Ruler 2, platform sales (V) and Ruler 3, platform revenue (R):
  GoTo on-demand (Indonesia-dominant): GTV and net revenue, IDR bn, recast basis, from goto_on_demand.py; 2026Q2 from the GoTo
  2Q26 release as quoted in PREREGISTRATION.md (Rp16.7tn GTV, Rp3.6tn net revenue; rounded to one decimal of a trillion).
  Grab On-Demand (Southeast Asia, USD m): GMV and Mobility+Deliveries revenue, from grab_quarterly.py; 2026Q2 grade B- (summary).
  Sea/Shopee (Asia + Brazil, USD m): GMV and marketplace revenue, from tables/shopee_quarterly_take_rate.csv.
Growth is year on year. Platform series are nominal; compare them with nominal official spending. Grab and Shopee are regional,
so they show the gap between rulers, not Indonesian spending. Nothing here says official GDP is wrong."""
import pathlib
import pandas as pd
here = pathlib.Path(__file__).parent

o = pd.read_csv(here / "tables/src/oecd_qna_idn_2021_2026.csv")
o = o[(o.SECTOR == "S1M") & (o.TRANSACTION == "P3") & (o.ADJUSTMENT == "N") & (o.UNIT_MEASURE == "XDC") & (o.TRANSFORMATION == "N")]
o = o.pivot_table(index="TIME_PERIOD", columns="PRICE_BASE", values="OBS_VALUE").rename(columns={"Q": "real", "V": "nominal"})
o.index = [i.replace("-", "") for i in o.index]

goto = pd.DataFrame({"V": [13414, 15052, 16348, 17058, 15710, 16371, 16743, 17710, 16344, 16700],
                     "R": [2255, 2634, 2901, 3090, 3007, 2987, 3205, 3397, 3360, 3600]},
                    index=["2024Q1", "2024Q2", "2024Q3", "2024Q4", "2025Q1", "2025Q2", "2025Q3", "2025Q4", "2026Q1", "2026Q2"])
g = {  # quarter: (mob_gmv, del_gmv, rev_mob, rev_del) from grab_quarterly.py; 2026Q2 from PREREGISTRATION.md baselines
 "2022Q1": (834, 2562, 112, 91), "2022Q2": (1035, 2476, 161, 134), "2022Q3": (1086, 2439, 176, 171), "2022Q4": (1149, 2350, 189, 268),
 "2023Q1": (1218, 2344, 194, 275), "2023Q2": (1320, 2573, 208, 292), "2023Q3": (1407, 2608, 231, 306), "2023Q4": (1474, 2648, 237, 321),
 "2024Q1": (1547, 2695, 247, 350), "2024Q2": (1584, 2850, 247, 356), "2024Q3": (1694, 2965, 271, 380), "2024Q4": (1815, 3213, 282, 407),
 "2025Q1": (1804, 3129, 282, 415), "2025Q2": (1883, 3471, 295, 439), "2025Q3": (2041, 3733, 317, 465), "2025Q4": (2174, 3904, 325, 481),
 "2026Q1": (2223, 3908, 337, 510), "2026Q2": (2214, 4249, 331, 531)}
grab = pd.DataFrame({q: {"V": a + b, "R": c + d} for q, (a, b, c, d) in g.items()}).T
s = pd.read_csv(here / "tables/shopee_quarterly_take_rate.csv", index_col="period")[["gmv", "marketplace_revenue"]].rename(columns={"gmv": "V", "marketplace_revenue": "R"})

def yoy(x):
    return (100 * (x / x.shift(4) - 1)).round(1)
out = pd.DataFrame(index=sorted(set(o.index) | set(goto.index) | set(grab.index) | set(s.index)))
out["official_real"] = yoy(o.real)
out["official_nominal"] = yoy(o.nominal)
for name, df in (("goto", goto), ("grab", grab), ("shopee", s)):
    out[f"{name}_sales"] = yoy(df.V.astype(float)).reindex(out.index)
    out[f"{name}_revenue"] = yoy(df.R.astype(float)).reindex(out.index)
    out[f"{name}_gap"] = (out[f"{name}_revenue"] - out[f"{name}_sales"]).round(1)
out = out.loc["2022Q1":].dropna(how="all")
out.index.name = "quarter"
out.to_csv(here / "tables/three_rulers_quarterly.csv")
pd.set_option("display.width", 200)
print(out.to_string())

r = out.loc["2023Q1":"2026Q2"]
print("\nQuarters where revenue growth exceeded sales growth by 10+ points:")
for n in ("goto", "grab", "shopee"):
    v = r[f"{n}_gap"].dropna()
    print(f"  {n}: {int((v >= 10).sum())} of {len(v)}; median gap {v.median():+.1f} pts")
v = r[["goto_sales", "official_nominal"]].dropna()
print(f"GoTo on-demand sales growth below official nominal spending growth in {int((v.goto_sales < v.official_nominal).sum())} of {len(v)} quarters")
