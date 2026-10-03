"""How big is the marketplace tax base? Depends on the ruler (3 Oct 2026, exploratory arithmetic, 2024 values).
PMK 37/2025: marketplaces withhold 0.5% of sellers' gross turnover; individuals up to Rp500m a year exempt (indo_policy_extraction.csv).
Rulers (Rp trillion, 2024): BPS marketplace channel 203.58 (BPS presentation 31 Mar 2025); BI e-commerce 487.01 (yardsticks.py);
Momentum Works Indonesia e-commerce GMV US$56.5bn and e-Conomy Indonesia e-commerce GMV US$62bn (indo_market_extraction.csv), converted at
the World Bank 2024 average rate Rp15,855.45 per US$. 2026 central-government tax target Rp2,357.7tn (RAPBN 2026, news).
Upper bounds: before the Rp500m exemption and before any non-compliance; the 2026 target is a different year, used only for scale."""
import json, pathlib
import pandas as pd
here = pathlib.Path(__file__).parent
fx = json.load(open(here / "tables/src/worldbank_fx_2022_2024.json"))["IDN"]["2024"]
base = pd.Series({"BPS marketplace channel": 203.58, "Bank Indonesia e-commerce": 487.01,
                  "Momentum Works marketplace GMV": 56.5 * fx / 1000, "e-Conomy e-commerce GMV": 62 * fx / 1000})
d = pd.DataFrame({"base_Rp_tn": base.round(1)})
d["tax_at_0.5pct_Rp_tn"] = (0.005 * base).round(2)
d["pct_of_2026_tax_target"] = (100 * 0.005 * base / 2357.7).round(3)
d["times_BPS_base"] = (base / base.iloc[0]).round(2)
d.to_csv(here / "tables/tax_base_rulers.csv")
print(d.to_string())
