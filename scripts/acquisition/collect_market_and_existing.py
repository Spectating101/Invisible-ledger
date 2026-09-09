"""Additional public market series and byte-preserved existing IL evidence.
Market rows are supporting security-days, never country platform revenue observations.
"""
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import quote
import json,csv,hashlib,shutil,sys
import collect_broad_archive as archive
ROOT=archive.ROOT
OLD=Path('/home/phyrexian/Downloads/Invisible_Ledger_Empirical_Rebuild_2026-09-08')
copied=[]
for section in ['00_READ_FIRST','01_RAW_SOURCES','02_SOURCE_EXTRACTS','03_ANALYTIC_DATA','04_SCRIPTS','05_RESULTS','06_SUPPORTING_ASEAN','07_EVENT_AND_MARKET','08_LEGACY_NOT_ACTIVE','09_QUARTERLY_SOURCE_AUDIT','10_MEASUREMENT_RECONCILIATION']:
    for p in (OLD/section).rglob('*'):
        if not p.is_file() or p.suffix.lower() not in ['.csv','.xlsx','.pdf','.html','.htm','.json','.py','.md','.txt','.mjs']:continue
        relative=p.relative_to(OLD); dest=ROOT/'preserved_existing'/relative
        dest.parent.mkdir(parents=True,exist_ok=True)
        if not dest.exists():shutil.copy2(p,dest)
        before=hashlib.sha256(p.read_bytes()).hexdigest();after=hashlib.sha256(dest.read_bytes()).hexdigest()
        assert before==after
        copied.append(dict(original_path=str(p),preserved_file=str(dest.relative_to(ROOT)),bytes=p.stat().st_size,sha256=before,status='unchanged existing evidence; original limitations retained'))
with (ROOT/'preserved_existing_manifest.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(copied[0]));w.writeheader();w.writerows(copied)
if '--existing-only' in sys.argv:
    print(dict(preserved_files=len(copied)));sys.exit(0)
symbols=['GRAB','SE','GOTO.JK','BUKA.JK','BELI.JK','BABA','^IXIC','^GSPC','^JKSE']
start=int(datetime(2010,1,1,tzinfo=timezone.utc).timestamp())
end=int(datetime(2026,9,9,tzinfo=timezone.utc).timestamp())
items=[(f'https://query1.finance.yahoo.com/v8/finance/chart/{quote(s,safe="")}?period1={start}&period2={end}&interval=1d&events=div%2Csplits&includeAdjustedClose=true','market','','daily '+s) for s in symbols]
archive.collect(items);rows=[];events=[]
for symbol,(u,_,_,_) in zip(symbols,items):
    rec=archive.records[u]
    if rec['status']!='downloaded':continue
    try:
        result=json.loads(archive.read(rec))['chart']['result'][0]
        q=result['indicators']['quote'][0];adj=result['indicators'].get('adjclose',[{}])[0].get('adjclose',[])
        for i,t in enumerate(result.get('timestamp',[])):
            rows.append(dict(symbol=symbol,timestamp_utc=t,date_utc=datetime.fromtimestamp(t,timezone.utc).date().isoformat(),open=q.get('open',[])[i],high=q.get('high',[])[i],low=q.get('low',[])[i],close=q.get('close',[])[i],adjusted_close=adj[i] if i<len(adj) else None,volume=q.get('volume',[])[i],currency=result['meta'].get('currency',''),exchange_timezone=result['meta'].get('exchangeTimezoneName',''),source_file=rec['file'],source_url=u))
        for kind,values in result.get('events',{}).items():
            for event in values.values():events.append(dict(symbol=symbol,kind=kind,event_json=json.dumps(event),source_file=rec['file']))
    except Exception as e:print('parse failure',symbol,str(e))
for name,data in [('platform_market_daily_2010_2026.csv',rows),('platform_market_events.csv',events)]:
    if data:
        with (ROOT/name).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
print(dict(preserved_files=len(copied),market_rows=len(rows),price_nonmissing=sum(r['close'] is not None for r in rows),corporate_actions=len(events)))
