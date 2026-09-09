"""New procurement script. Preserves downloaded bytes; does not change original IL data."""
from pathlib import Path
import csv, hashlib, json, urllib.request
import subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
SOURCES = {
 'blibli_fy2022': 'https://about.blibli.com/en/media/press-release/pt-global-digital-niaga-tbk-2022-full-year-results-performance-2',
 'blibli_fy2023': 'https://about.blibli.com/id/media/press-release/pt-global-digital-niaga-tbk-2023-full-year-results-performance',
 'blibli_fy2024': 'https://about.blibli.com/en/media/press-release/pt-global-digital-niaga-tbk-2024-full-year-results-performance',
 'blibli_fy2025': 'https://about.blibli.com/en/media/press-release/pt-global-digital-niaga-tbk-2025-full-year-results-performance',
 'blibli_q12023': 'https://about.blibli.com/en/media/press-release/2023-first-quarter-results-performance-pt-global-digital-niaga-tbk',
 'blibli_q32023': 'https://about.blibli.com/en/media/press-release/2023-third-quarter-results-performance',
 'blibli_prospectus': 'https://about.blibli.com/investor-relations/prospectus/Final%20Prospectus%20IPO%20-%20PT%20Global%20Digital%20Niaga%20Tbk.pdf',
 'bukalapak_ir': 'https://about.bukalapak.com/id/investor-relations/',
 'bukalapak_ir_main': 'https://www.bukalapak.com/investor-relations',
 'bukalapak_fy2022_release': 'https://www.prnewswire.com/apac/news-releases/buka-finished-2022-with-positive-contribution-margin-301784373.html',
 'blibli_q22024': 'https://about.blibli.com/en/media/press-release/pt-global-digital-niaga-tbk-2024-second-quarter-results-performance',
 'blibli_q32024': 'https://about.blibli.com/en/media/press-release/pt-global-digital-niaga-tbk-2024-third-quarter-results-performance',
 'blibli_q12025': 'https://about.blibli.com/en/media/press-release/pt-global-digital-niaga-tbk-2025-first-quarter-results-performance-2',
 'blibli_q22025': 'https://about.blibli.com/en/media/press-release/pt-global-digital-niaga-tbk-2025-second-quarter-results-performance',
 'bukalapak_ar2021_mirror': 'https://companiesmarketcap.com/annual-reports/72327.ar.en.2021.pdf',
 'bukalapak_ar2022_mirror': 'https://companiesmarketcap.com/annual-reports/72327.ar.en.2022.pdf',
 'bukalapak_ar2023_mirror': 'https://companiesmarketcap.com/annual-reports/72327.ar.en.2023.pdf',
 'bukalapak_ar2024_mirror': 'https://companiesmarketcap.com/annual-reports/72327.ar.en.2024.pdf',
 'grab_fy2025_20f': 'https://d18rn0p25nwr6d.cloudfront.net/CIK-0001855612/4d2a05a2-f9ed-4b40-9803-129963531f02.pdf',
 'momentum_2020_indonesia': 'https://thelowdown.momentum.asia/indonesia-ecommerce-marketplace-gmv-reached-us40-billion-with-shopee-and-tokopedia-leading/',
 'momentum_2025_asean_release': 'https://thelowdown.momentum.asia/wp-content/uploads/2026/04/Embargoed-Press-release-Momentum-Works-Ecommerce-in-SEA-2026.pdf',
 'bukalapak_sr2024_mirror': 'https://companiesmarketcap.com/sustainability-reports/72327.sar.en.2024.pdf',
 'bukalapak_sr2021_mirror': 'https://companiesmarketcap.com/sustainability-reports/72327.sar.en.2021.pdf',
}

def fetch(item):
 name, url = item
 existing=ROOT/'procurement_log.json'
 if existing.exists():
  for old in json.loads(existing.read_text()):
   if old['source_id']==name and old['url']==url and old['status']=='downloaded' and (ROOT/old['file']).exists():return old
 row = dict(source_id=name,url=url,status='',file='',bytes=0,sha256='',error='')
 try:
  req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (academic source verification)'})
  with urllib.request.urlopen(req, timeout=45) as response:
   data = response.read(); row['resolved_url']=response.url
  ext = '.pdf' if data.startswith(b'%PDF') else '.html'
  path=ROOT/'raw_sources'/(name+ext); path.parent.mkdir(parents=True,exist_ok=True)
  if path.exists() and path.read_bytes()!=data:
   path=path.with_name(name+'_'+hashlib.sha256(data).hexdigest()[:10]+ext)
  path.write_bytes(data)
  row.update(status='downloaded',file=str(path.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  extracts=ROOT/'text_extracts'; extracts.mkdir(exist_ok=True)
  if ext=='.pdf':
   subprocess.run(['pdftotext','-layout',str(path),str(extracts/(name+'.txt'))],check=True)
  if ext=='.html':
   soup=BeautifulSoup(data,'html.parser')
   extracts=ROOT/'text_extracts'; extracts.mkdir(exist_ok=True)
   (extracts/(name+'.txt')).write_text(soup.get_text('\n',strip=True),encoding='utf-8')
   row['pdf_links']=[a.get('href') for a in soup.find_all('a',href=True) if '.pdf' in a['href'].lower()]
 except Exception as e: row.update(status='failed',error=str(e))
 return row

if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=5) as pool: rows=list(pool.map(fetch,SOURCES.items()))
 links=[(r['source_id']+'_linked_'+str(i),u) for r in rows for i,u in enumerate(r.get('pdf_links',[]))]
 with ThreadPoolExecutor(max_workers=5) as pool: rows.extend(pool.map(fetch,links))
 (ROOT/'procurement_log.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
 for row in rows: print(json.dumps(row))
