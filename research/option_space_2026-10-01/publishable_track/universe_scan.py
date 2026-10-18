"""Scoping scan for the publishable track: which listed platforms report a transaction-value KPI (V) next to revenue (R)?
Source for SEC filers: EDGAR full-text search (10-K, 20-F, 40-F), 2 Oct 2026, saved in edgar_fts_by_company.json
('yrs' = fiscal years whose annual report MENTIONS the KPI term; a mention is not yet a verified numeric series).
Classification into groups is by hand. No KPI values or growth rates were looked at, so this scan does not touch any later test.
Non-SEC firms are listed from prior knowledge; their KPI years are unverified."""
import json, csv
fts = json.load(open("edgar_fts_by_company.json"))
VERIFIED = {"EBAY","MELI","SE","GRAB","JMIA","UBER","LYFT","DASH","CART","MMYT","DIDIY","DADA","FTCHQ","BABA","NBIS"}  # already have quote-verified rows in ../tables/src
CORE = {  # ticker: (group, KPI)
 "EBAY":("marketplace","GMV"),"MELI":("marketplace","GMV"),"ETSY":("marketplace","GMS"),"SE":("marketplace","GMV"),
 "BABA":("marketplace","GMV"),"JD":("marketplace","GMV"),"JMIA":("marketplace","GMV"),"VIPS":("marketplace","GMV"),
 "MOGU":("marketplace","GMV"),"FTCHQ":("marketplace","GMV"),"REAL":("marketplace","GMV"),"DIBS":("marketplace","GMV"),
 "NEGG":("marketplace","GMV"),"KSPI":("marketplace","GMV"),"DDL":("marketplace","GMV"),"HEPS":("marketplace","GMV"),
 "LQDT":("marketplace","GMV"),"RBA":("marketplace","GTV"),"ACVA":("marketplace","GMV"),"FVRR":("services marketplace","GMV"),
 "UPWK":("services marketplace","GSV"),"SEAT":("marketplace","GOV"),"UXIN":("marketplace","GMV"),
 "UBER":("mobility/delivery","Gross Bookings"),"LYFT":("mobility/delivery","Gross Bookings"),"DASH":("mobility/delivery","Marketplace GOV"),
 "CART":("mobility/delivery","GTV"),"GRAB":("mobility/delivery","GMV"),"DIDIY":("mobility/delivery","GTV"),
 "ASAPQ":("mobility/delivery","Gross Food Sales"),"DADA":("mobility/delivery","GMV"),"NBIS":("mobility/delivery","GMV/GBV (Yandex)"),
 "BKNG":("travel","Gross Bookings"),"EXPE":("travel","Gross Bookings"),"TCOM":("travel","GMV"),"MMYT":("travel","Gross Bookings"),
 "YTRA":("travel","Gross Bookings"),"DESP":("travel","Gross Bookings"),"TOUR":("travel","GMV"),"ABNB":("travel","GBV"),"VCSA":("travel","GBV"),
}
EXT = {"PYPL":"TPV","XYZ":"GPV","SHOP":"GMV","BIGC":"GMV","WIX":"GPV","SQSP":"GMV","TOST":"GPV","LSPD":"GPV","PAGS":"TPV","STNE":"TPV",
       "DLO":"TPV","FLYW":"TPV","AFRM":"GMV","GLBE":"GMV","VTEX":"GMV","OLO":"GMV","BZUN":"GMV"}
NAMEHINT = {"GrubHub":("mobility/delivery","Gross Food Sales"),"Orbitz":("travel","Gross Bookings"),"Ozon":("marketplace","GMV"),
            "Jumei":("marketplace","GMV"),"Liberty Expedia":None}
def ticker(n):
    if "(" not in n: return ""
    t = n.split("(")[1].split(")")[0].split(",")[0].strip()
    return t if "CIK" not in t else ""
rows = []
for cik, b in fts.items():
    t = ticker(b["name"]); grp = kpi = None; tier = ""
    if t in CORE: (grp, kpi), tier = CORE[t], "core"
    elif t in EXT: grp, kpi, tier = "payments/merchant software", EXT[t], "extension"
    else:
        for h, v in NAMEHINT.items():
            if h in b["name"] and v: (grp, kpi), tier = v, "core"
    if tier:
        ys = b["yrs"]
        rows.append(dict(firm=b["name"].split("(")[0].strip(), ticker=t, listing="SEC", tier=tier, group=grp, kpi=kpi,
                         first_year=ys[0], last_year=ys[-1], n_years_mentioned=len(ys), verified_rows_already=("yes" if t in VERIFIED else "no")))
NONSEC = [("Meituan","HKEX","mobility/delivery","GTV (food delivery)","yes"),("Delivery Hero","XETRA","mobility/delivery","GMV","yes"),
 ("Just Eat Takeaway.com","Euronext","mobility/delivery","GTV","yes"),("Deliveroo","LSE","mobility/delivery","GTV","yes"),
 ("Talabat","DFM","mobility/delivery","GMV","yes"),("Eternal (Zomato)","NSE","mobility/delivery","GOV","yes"),("Swiggy","NSE","mobility/delivery","GOV","yes"),
 ("GoTo","IDX","mobility/delivery","GTV","yes"),("Bukalapak","IDX","marketplace","TPV","yes"),("Blibli","IDX","marketplace","TPV","yes"),
 ("Zalando","XETRA","marketplace","GMV","no"),("Allegro","WSE","marketplace","GMV","no"),("Mercari","TSE","marketplace","GMV","no"),
 ("Rakuten","TSE","marketplace","Domestic EC GMS","no"),("Nykaa (FSN)","NSE","marketplace","GMV","no"),("Coupang","NYSE (no GMV KPI)","marketplace","none","no"),
 ("Pinduoduo/PDD","SEC (GMV dropped)","marketplace","GMV","no"),("Ozon (post-2022)","MOEX","marketplace","GMV","yes")]
for f, l, g, k, v in NONSEC:
    rows.append(dict(firm=f, ticker="", listing=l, tier="core", group=g, kpi=k, first_year="", last_year="", n_years_mentioned="", verified_rows_already=v))
rows.sort(key=lambda r: (r["tier"], r["group"], r["firm"]))
with open("universe_scan.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
core = [r for r in rows if r["tier"] == "core"]
sec3 = [r for r in core if r["listing"] == "SEC" and r["n_years_mentioned"] >= 3]
print(f"core firms: {len(core)} (SEC with >=3 mention-years: {len(sec3)}, non-SEC: {len(NONSEC)}); extension: {len(rows)-len(core)}")
from collections import Counter
print(Counter(r["group"] for r in core))
print("SEC core mention-years total:", sum(r["n_years_mentioned"] for r in sec3))
print("already verified:", sum(r["verified_rows_already"] == "yes" for r in core))
