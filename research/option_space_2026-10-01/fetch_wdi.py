"""Fetch the public series used as controls and for exchange rates (25 Oct 2026): World Bank WDI and BIS central-bank policy rates.

Prof. Kong asked for home-market GDP growth, interest rates, inflation and household spending, and for the wedge in US dollars. This script
downloads exactly those series, once, and stores them in the repository so that nothing downstream needs the network:
  tables/src/wdi_extraction.csv          (country, indicator, year, value, fetched)
  tables/src/bis_policy_extraction.csv   (country, month, policy rate in percent, fetched; BIS WS_CBPOL, central bank policy rates, end of month)
The World Bank lending rate is missing for the US, Japan, India, Kazakhstan, Turkey and the euro area, so the interest rate used in the
regressions is the central-bank policy rate from the Bank for International Settlements (annual mean of the monthly values).
BIS has no series for Kazakhstan or Nigeria; the interest-rate column of the regressions therefore drops those two markets.
World Bank WDI is public (CC BY 4.0). It is NOT one of the licensed sources; the licensed World Bank files are the enterprise survey files.
Run from this folder: python3 fetch_wdi.py   (needs network; the regression scripts do not)."""
import csv, datetime, json, urllib.request

COUNTRIES = ["US", "ID", "CN", "JP", "DE", "KZ", "RU", "TR", "IN", "BR", "AR", "NG"]
INDICATORS = {
    "NY.GDP.MKTP.KD.ZG": "GDP growth (annual %)",
    "FP.CPI.TOTL.ZG": "Inflation, consumer prices (annual %)",
    "NE.CON.PRVT.KD.ZG": "Household final consumption expenditure, growth (annual %)",
    "FR.INR.LEND": "Lending interest rate (%)",
    "FR.INR.RINR": "Real interest rate (%)",
    "PA.NUS.FCRF": "Official exchange rate (LCU per US$, period average)",
}
rows = []
today = datetime.date.today().isoformat()
for ind, label in INDICATORS.items():
    url = f"https://api.worldbank.org/v2/country/{';'.join(COUNTRIES)}/indicator/{ind}?format=json&per_page=5000&date=2012:2025"
    with urllib.request.urlopen(url, timeout=60) as r:
        meta, data = json.load(r)
    for d in data:
        rows.append({"country": d["countryiso3code"][:3] and d["country"]["id"], "indicator": ind, "label": label, "year": int(d["date"]), "value": d["value"], "fetched": today})
rows.sort(key=lambda r: (r["indicator"], r["country"], r["year"]))
with open("tables/src/wdi_extraction.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["country", "indicator", "label", "year", "value", "fetched"]); w.writeheader(); w.writerows(rows)
have = {}
for r in rows:
    if r["value"] is not None: have.setdefault(r["indicator"], set()).add(r["country"])
print(len(rows), "rows")
for k, v in have.items(): print(k, len(v), "countries with data; missing:", sorted(set(COUNTRIES) - v))

# ---- BIS policy rates ----
areas = "US+CN+JP+XM+KZ+RU+TR+IN+BR+AR+NG+ID"
url = f"https://stats.bis.org/api/v2/data/dataflow/BIS/WS_CBPOL/1.0/M.{areas}?startPeriod=2012-01&format=csv"
import io
with urllib.request.urlopen(url, timeout=90) as r: txt = r.read().decode("utf8")
rd = csv.DictReader(io.StringIO(txt))
out = sorted(({"country": d["REF_AREA"], "month": d["TIME_PERIOD"], "policy_rate_pct": d["OBS_VALUE"], "fetched": today} for d in rd), key=lambda r: (r["country"], r["month"]))
with open("tables/src/bis_policy_extraction.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["country", "month", "policy_rate_pct", "fetched"]); w.writeheader(); w.writerows(out)
print("BIS", len(out), "rows; countries:", sorted({r["country"] for r in out}))
