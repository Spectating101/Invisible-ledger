"""BPS vs platforms: what each yardstick says about Indonesian e-commerce (2023 anchor), in rupiah where possible.
Inputs (all quote-verified or from the repo's certified tables):
  BPS national levels (outputs/hypothesis_tests_2026-09-10/bps_national_levels.csv): total and EXCLUSIVE marketplace value.
  BPS multiple-response marketplace share (32.74%) is NOT additive and is never converted to money here.
  Tokopedia GTV 2022-23 (GoTo 4Q23 release, rupiah, no FX).  Shopee Indonesia = repo's conditional reconstruction (modelled, labelled).
  e-Conomy SEA Indonesia e-commerce GMV and Bank Indonesia e-commerce value: tables/src/bps_bridge_extraction.csv.
FX 15,236.88 IDR/USD is the 2023 rate already used in build_numbers.py. Nothing here sizes the scope items; it only bounds the gap.
Writes tables/bps_bridge.csv and tables/bps_bridge_scope_items.csv."""
import pathlib
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = pathlib.Path(__file__).resolve().parent / "tables"
FX = 15236.88
bl = pd.read_csv(ROOT / "outputs/hypothesis_tests_2026-09-10/bps_national_levels.csv").set_index("year")
ex = pd.read_csv(T / "src/bps_bridge_extraction.csv")
ex = ex[ex.value.notna()]
tl = pd.read_csv(T / "take_rate_levels.csv")


def one(entity, field, period, src):
    s = ex[(ex.entity == entity) & (ex.field == field) & (ex.period == period) & (ex.source_file == src)]
    assert len(s) >= 1, (entity, field, period, src)
    return float(s.value.iloc[0])


tokopedia23 = one("Tokopedia", "GTV", 2023, "goto_fy2023.txt") / 1000     # IDR tn
tokopedia22 = one("Tokopedia", "GTV", 2022, "goto_fy2023.txt") / 1000
shopee_id = tl[(tl.firm == "Shopee") & (tl.evidence_tier == "conditional_country_reconstruction")].set_index("year").transaction_value
econ23 = one("eConomy", "ecommerce_gmv", 2023, "economy_sea_2024_indonesia.txt")
econ24a = one("eConomy", "ecommerce_gmv", 2024, "economy_sea_2024_indonesia.txt")
econ24b = one("eConomy", "ecommerce_gmv", 2024, "economy_sea_2025_indonesia.txt")
bi24 = one("BI", "ecommerce_value", 2024, "bi_cerita_umkm.txt")

b23, b24 = bl.loc[2023], bl.loc[2024]
rows = [
    ("BPS total e-commerce sales 2023", b23.transaction_value_idr_trillion, "BPS survey of businesses, business online-sales revenue"),
    ("BPS marketplace (exclusive split) 2023", b23.marketplace_value_idr_trillion, "BPS; additive part of total"),
    ("Tokopedia GTV 2023", tokopedia23, "GoTo release; includes digital goods, cars, motorcycles"),
    ("Shopee Indonesia GMV 2023 (modelled)", shopee_id[2023] * FX / 1000, "repo conditional reconstruction; Sea GMV includes shipping and other charges"),
    ("Tokopedia + Shopee Indonesia 2023", tokopedia23 + shopee_id[2023] * FX / 1000, "sum of the two rows above"),
    ("e-Conomy SEA Indonesia e-commerce GMV 2023", econ23 * FX / 1000, "US$59bn (2024 edition) at 2023 FX; the 2023 edition printed 62"),
    ("BPS total 2024", b24.transaction_value_idr_trillion, "BPS"),
    ("BPS marketplace (exclusive) 2024", b24.marketplace_value_idr_trillion, "BPS"),
    ("Bank Indonesia e-commerce value 2024", bi24, "BI 'Cerita BI', payments-style series"),
]
B = pd.DataFrame(rows, columns=["measure", "idr_tn", "note"])
B["usd_bn_at_2023_fx"] = B.idr_tn * 1000 / FX
B.round(1).to_csv(T / "bps_bridge.csv", index=False)

mk23 = b23.marketplace_value_idr_trillion
plat = tokopedia23 + shopee_id[2023] * FX / 1000
ratios = {
    "Tokopedia alone / BPS marketplace (all marketplaces), 2023": tokopedia23 / mk23,
    "Tokopedia + Shopee Indonesia / BPS marketplace, 2023": plat / mk23,
    "BPS marketplace / (Tokopedia + Shopee Indonesia) = share of platform value BPS shows": mk23 / plat,
    "scope difference that would have to explain the gap (1 - above)": 1 - mk23 / plat,
    "BPS total / e-Conomy total, 2023": b23.transaction_value_idr_trillion / (econ23 * FX / 1000),
    "BPS total 2024 / Bank Indonesia 2024": b24.transaction_value_idr_trillion / bi24,
    "BPS total growth 2023-24 (%)": 100 * (b24.transaction_value_idr_trillion / b23.transaction_value_idr_trillion - 1),
    "e-Conomy total growth 2023-24, 2024 edition (%)": 100 * (econ24a / econ23 - 1),
    "e-Conomy total growth 2023-24, 2025 edition (%)": 100 * (econ24b / 59 - 1),
    "BPS marketplace growth 2023-24 (%)": 100 * (b24.marketplace_value_idr_trillion / mk23 - 1),
    "Shopee Indonesia growth 2023-24, modelled (%)": 100 * (shopee_id[2024] / shopee_id[2023] - 1),
}
for k, v in ratios.items():
    print(f"{k}: {v:.2f}")
pd.Series(ratios).round(3).to_csv(T / "bps_bridge_ratios.csv", header=["value"])

scope = [
    ("Shopee GMV includes shipping and other charges", "platform > BPS sales", "Sea 20-F 2024 definition sentence", "not sized in any filing"),
    ("Tokopedia GTV includes digital goods, cars and motorcycles; commission base excludes digital goods and some high-value items", "platform > BPS goods sales", "GoTo 4Q23 release; GoTo financial statements 2024 (Tokopedia agreement)", "not sized; only a growth contrast (core GTV -26% vs total -8% in 4Q23)"),
    ("BPS value is business online-sales revenue, collected from businesses (formal and informal) with an online order in the year", "BPS <= platform", "BPS provincial books (Sulut, Bali 2023)", "survey frame is businesses, not individual sellers or foreign sellers"),
    ("BPS marketplace share is 18.23% on the exclusive split and 32.74% on the multiple-response question", "do not mix", "BPS 2023/2024 publications as recorded in the repo", "only the exclusive split is additive"),
    ("BPS reference year: survey in year t+1 asks about activity in year t", "timing", "BPS Statistik E-Commerce 2022 vs 2023 books", "alignment checked for 2023 only"),
    ("Three national yardsticks for 2024: BPS Rp1,289tn, e-Conomy about US$62-65bn, Bank Indonesia Rp487tn", "ruler risk", "BPS; e-Conomy 2024 and 2025 editions; BI Cerita BI", "BPS/BI = 2.6x"),
]
pd.DataFrame(scope, columns=["item", "direction", "evidence", "sizing"]).to_csv(T / "bps_bridge_scope_items.csv", index=False)
