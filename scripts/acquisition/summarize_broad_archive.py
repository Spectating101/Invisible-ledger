"""Count distinct layers honestly and validate saved files, without adding them into N."""
from pathlib import Path
from collections import Counter
import csv,json,hashlib
ROOT=Path(__file__).resolve().parent
B=ROOT/'broad_archive'
manifest=json.loads((B/'manifest.json').read_text())
good=[r for r in manifest if r['status']=='downloaded']
for r in good:assert hashlib.sha256((B/r['file']).read_bytes()).hexdigest()==r['sha256'],r['file']
catalog=[]
for base in [ROOT/'source_extracts',B]:
    for p in base.rglob('*.csv'):
        with p.open(newline='',encoding='utf-8-sig',errors='replace') as f:
            reader=csv.reader(f); header=next(reader,[]); n=sum(1 for _ in reader)
        role='existing material: retain original scope/status' if 'preserved_existing' in str(p) else 'new extract or inventory: see file-specific status'
        catalog.append(dict(file=str(p.relative_to(ROOT)),rows=n,columns=len(header),bytes=p.stat().st_size,role=role))
with (ROOT/'CSV_FILE_INDEX.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(catalog[0]));w.writeheader();w.writerows(catalog)
def read(name):
    p=B/name
    return list(csv.DictReader(p.open())) if p.exists() else []
market=read('platform_market_daily_2010_2026.csv');wb=read('asean_worldbank_context_2000_2025.csv');articles=read('momentum_publisher_articles.csv')
assert len({(r['symbol'],r['timestamp_utc']) for r in market})==len(market),'duplicate market keys'
assert len({(r['iso3'],r['year'],r['indicator']) for r in wb})==len(wb),'duplicate WB keys'
summary=dict(downloaded_files=len(good),unique_download_hashes=len({r['sha256'] for r in good}),downloaded_bytes=sum(r['bytes'] for r in good),modules=dict(Counter(r['module'] for r in good)),failed_urls=[dict(url=r['url'],error=r.get('error','')) for r in manifest if r['status']!='downloaded'],preserved_existing_files=len(read('preserved_existing_manifest.csv')),market_security_days=len(market),market_nonmissing_close=sum(r['close']!='' for r in market),market_by_symbol=dict(Counter(r['symbol'] for r in market)),worldbank_country_year_indicator_slots=len(wb),worldbank_nonmissing=sum(r['value']!='' for r in wb),publisher_articles=len(articles),publisher_market_report_candidates=sum(r['market_report_candidate']=='True' for r in articles),search_excerpts=len(read('searchable_source_excerpts.csv')),csv_files=len(catalog),main_sample_N='not finalized; none of these layer totals is the Indonesia sample N',checks=['downloaded byte hashes passed','security-timestamp uniqueness passed','country-year-indicator uniqueness passed'])
(ROOT/'BROAD_COLLECTION_COUNTS.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
