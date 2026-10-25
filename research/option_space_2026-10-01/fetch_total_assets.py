"""Fetch annual total assets from SEC XBRL filings for the platforms that file with the SEC (25 Oct 2026).

Prof. Kong asked for firm size measured by total assets or users, not transaction value (transaction value is part of the wedge, so it would link
the regressor to the dependent variable mechanically). The repository held neither. For the platforms that file with the SEC (10-K, 20-F, 40-F),
this script downloads the 'Assets' fact from the SEC's public XBRL API and stores it, once, in
  tables/src/total_assets_extraction.csv   (entity, cik, period_end, year, value, unit, form, accession, filed, taxonomy, fetched)
Rules, the same as for revenue elsewhere in the thesis: only annual filings (10-K, 20-F, 40-F and their amendments); a year is the calendar year
of the fiscal period end; if a period end is reported in several filings, the LATEST filing is used (it carries any restatement).
Platforms that do not file with the SEC (Tokopedia/GoTo, Blibli, Bukalapak, Rakuten, Zalando) are not covered here; see total_assets_manual.csv.
Run from this folder: python3 fetch_total_assets.py   (needs network; the regression scripts do not)."""
import csv, datetime, json, time, urllib.request

UA = {"User-Agent": "Academic research christstrife@gmail.com"}
CIK = {"Grab on-demand": 1855612, "Etsy": 1370637, "eBay": 1065088, "Jumia": 1756708, "Mercado Libre": 1099590, "Sea / Shopee": 1703399, "Shopify": 1594805,
       "ACVA": 1637873, "ASAPQ": 1653247, "BABA": 1577552, "DESP": 1703141, "DIBS": 1600641, "EXPE": 1324424, "FVRR": 1762301, "GrubHub": 1594109,
       "HEPS": 1850235, "KSPI": 1985487, "MOGU": 1743971, "Ozon": 1822829, "PDD": 1737806, "RBA": 1046102, "REAL": 1573221, "SEAT": 1856031,
       "UPWK": 1627475, "VCSA": 1874944, "YTRA": 1516899}
FORMS = {"10-K", "10-K/A", "20-F", "20-F/A", "40-F", "40-F/A"}
today = datetime.date.today().isoformat()
out = []
for ent, cik in CIK.items():
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r: facts = json.load(r)["facts"]
    except Exception as e:
        print(ent, "ERROR", e); continue
    best = {}
    for tax in ("us-gaap", "ifrs-full"):
        node = facts.get(tax, {}).get("Assets")
        if not node: continue
        for unit, pts in node["units"].items():
            for p in pts:
                if p.get("form") not in FORMS: continue
                key = (p["end"], unit)
                if key not in best or p["filed"] > best[key]["filed"]:
                    best[key] = {**p, "taxonomy": tax, "unit": unit}
    for (end, unit), p in sorted(best.items()):
        out.append({"entity": ent, "cik": cik, "period_end": end, "year": int(end[:4]), "value": p["val"], "unit": unit, "form": p["form"],
                    "accession": p["accn"], "filed": p["filed"], "taxonomy": p["taxonomy"], "fetched": today})
    print(f"{ent:16s} {len([o for o in out if o['entity']==ent])} year-ends")
    time.sleep(0.2)
with open("tables/src/total_assets_extraction.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["entity", "cik", "period_end", "year", "value", "unit", "form", "accession", "filed", "taxonomy", "fetched"])
    w.writeheader(); w.writerows(out)
print(len(out), "rows written")
