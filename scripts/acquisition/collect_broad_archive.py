"""New IL source acquisition. Public issuer archives and ASEAN context, not a main sample.
Preserves downloaded bytes, timestamps and discovery parents. No inferred country data.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlparse
from datetime import datetime, timezone
import requests, hashlib, json, csv, re, subprocess
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parent/'broad_archive'
ROOT.mkdir(exist_ok=True)
LOG=ROOT/'manifest.json'
old=json.loads(LOG.read_text()) if LOG.exists() else []
cache={r['url']:r for r in old if r.get('status')=='downloaded'}
records={r['url']:r for r in old}

def get(url, module, parent='', label=''):
    url=url.strip()
    if url in cache and (ROOT/cache[url]['file']).exists(): return cache[url]
    row=dict(url=url,module=module,parent=parent,label=label,retrieved_utc=datetime.now(timezone.utc).isoformat())
    try:
        r=requests.get(url,timeout=50,headers={'User-Agent':'Mozilla/5.0 (research source archive)'})
        r.raise_for_status(); b=r.content
        ct=r.headers.get('Content-Type','')
        ext='.pdf' if b.startswith(b'%PDF') else '.json' if 'json' in ct else '.png' if 'image/png' in ct else '.jpg' if 'image/jpeg' in ct else '.webp' if 'image/webp' in ct else '.html'
        name=re.sub(r'[^a-zA-Z0-9_.-]+','_',urlparse(url).path.split('/')[-1])[:95] or 'index'
        p=ROOT/'raw'/module/(hashlib.sha256(url.encode()).hexdigest()[:12]+'_'+name+ext)
        p.parent.mkdir(parents=True,exist_ok=True)
        if p.exists() and p.read_bytes()!=b:p=p.with_name(p.stem+'_'+hashlib.sha256(b).hexdigest()[:10]+ext)
        p.write_bytes(b)
        row.update(status='downloaded',file=str(p.relative_to(ROOT)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),resolved_url=r.url,content_type=r.headers.get('Content-Type',''))
        if ext=='.pdf':
            t=ROOT/'text'/module/(p.stem+'.txt');t.parent.mkdir(parents=True,exist_ok=True)
            proc=subprocess.run(['pdftotext','-layout',str(p),str(t)],capture_output=True,timeout=90)
            row['text_file']=str(t.relative_to(ROOT)) if t.exists() else ''
            row['text_extraction_ok']=proc.returncode==0
    except Exception as e:row.update(status='failed',error=str(e))
    return row

def save():LOG.write_text(json.dumps(list(records.values()),indent=2))
def collect(items):
    unique={u:(u,m,p,l) for u,m,p,l in items if u.startswith('http')}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for f in as_completed([pool.submit(get,*args) for args in unique.values()]):
            r=f.result();records[r['url']]=r;save()
    print('archive',len(records),'downloaded',sum(r['status']=='downloaded' for r in records.values()),flush=True)

def read(row):return (ROOT/row['file']).read_text(errors='replace')

def main():
    # API route discovered in Sea's public quarterly-results JavaScript.
    sea='https://www.sea.com/api/financial/resource'
    collect([(sea,'sea','','official quarterly resource API')])
    items=[]; index=[]
    if records[sea]['status']=='downloaded':
        for year in json.loads(read(records[sea])):
            for period in year['data']:
                for field in ['press_release','presentation','infographic','transcript','full_year_report']:
                    u=period.get(field,'').strip()
                    if u:
                        label=f"{year['year']} {period.get('quarter','')} {field}"
                        index.append(dict(issuer='Sea',year=year['year'],period=period.get('quarter',''),kind=field,url=u))
                        items.append((u,'sea',sea,label))
    # Each GoTo query is a publicly exposed year/quarter selector, not a guessed file.
    pages=[(f'https://www.gotocompany.com/investor-relations/en/quarterly-results?year={y}&item=Q{q}','goto','','quarter selector') for y in range(2021,2027) for q in range(1,5) if y<2026 or q<=2]
    collect(pages)
    for u,m,_,_ in pages:
        row=records[u]
        if row['status']!='downloaded':continue
        soup=BeautifulSoup(read(row),'html.parser')
        for a in soup.select('a[href]'):
            target=urljoin(u,a['href']).strip()
            if '.pdf' in target.lower():
                items.append((target,m,u,a.get_text(' ',strip=True)))
                index.append(dict(issuer='GoTo',year='',period='',kind=a.get_text(' ',strip=True),url=target))
    extras=[
      'https://asset-about.blibli.com/2025/10/Earnings-Release-9M25-PT-Global-Digital-Niaga-Tbk.pdf',
      'https://s4.bukalapak.com/content/documents/websites/7/109699/AR_PT_BUKALAPAK_COM_Tbk_2025.pdf',
    ]
    items.extend((u,'other_issuers','','additional issuer source') for u in extras)
    collect(items)
    with (ROOT/'issuer_document_index.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['issuer','year','period','kind','url']);w.writeheader();w.writerows(index)
    # Context/FX: country-year-indicator observations, never platform observations.
    countries='IDN;MYS;VNM;THA;PHL;SGP;BRN;KHM;LAO;MMR;TLS'
    indicators=['NY.GDP.MKTP.CD','NY.GDP.MKTP.KD.ZG','PA.NUS.FCRF','SP.POP.TOTL','IT.NET.USER.ZS','IT.NET.BBND.P2','IT.CEL.SETS.P2','NE.CON.PRVT.CD','NV.SRV.TOTL.ZS','GC.TAX.TOTL.GD.ZS']
    urls=[(f'https://api.worldbank.org/v2/country/{countries}/indicator/{i}?format=json&date=2000:2025&per_page=20000','worldbank','','country-year context; not platform N') for i in indicators]
    collect(urls); obs=[]
    for u,_,_,_ in urls:
        r=records[u]
        if r['status']!='downloaded':continue
        try:
            data=json.loads(read(r))
            if len(data)!=2 or not isinstance(data[1],list):continue
            for x in data[1]:
                obs.append(dict(country=x['country']['value'],iso3=x['countryiso3code'],year=x['date'],indicator=x['indicator']['id'],indicator_name=x['indicator']['value'],value=x['value'],unit=x['unit'],source_url=u,source_file=r['file']))
        except Exception as e:print('WB parse',u,str(e),flush=True)
    if obs:
        with (ROOT/'asean_worldbank_context_2000_2025.csv').open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(obs[0]));w.writeheader();w.writerows(obs)
    summary=dict(downloaded_files=sum(r['status']=='downloaded' for r in records.values()),failed_urls=sum(r['status']=='failed' for r in records.values()),issuer_link_records=len(index),context_rows_including_missing=len(obs),context_nonmissing=sum(x['value'] is not None for x in obs),new_validated_platform_observations='not counted: source acquisition and context only')
    (ROOT/'counts.json').write_text(json.dumps(summary,indent=2));print(summary,flush=True)
if __name__=='__main__':main()
