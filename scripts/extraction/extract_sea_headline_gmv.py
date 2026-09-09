"""Explicit numeric GMV disclosures, retaining rounded units and quote context.
No inferred missing values, revenue pairs, or country allocation. Release period is
not necessarily the observation period: Q4 releases also contain full-year values.
"""
from pathlib import Path
import json,re,csv
ROOT=Path(__file__).resolve().parent/'broad_archive'
data=json.loads((ROOT/'manifest.json').read_text()); rows=[]
pat=re.compile(r'(?:Gross merchandise value\s*\([“\"]GMV[”\"]\)|GMV)\s+was\s+US\$([\d,.]+)\s+(billion|million)([^.]*\.)',re.I)
for r in data:
    if r.get('module')!='sea' or not r.get('label','').endswith('press_release') or not r.get('text_file'):continue
    for page,body in enumerate((ROOT/r['text_file']).read_text().split('\f'),1):
        text=re.sub(r'\s+',' ',body)
        for m in pat.finditer(text):
            rows.append(dict(issuer='Sea/Shopee',release_period=r['label'].replace(' press_release',''),metric='GMV',value=m.group(1).replace(',',''),currency='USD',scale=m.group(2),pdf_page=page,quote=text[max(0,m.start()-60):min(len(text),m.end()+120)],source_file=r['file'],source_url=r['url'],status='rounded issuer disclosure; observation period and reporting vintage require review; not Indonesia-only'))
with (ROOT/'sea_gmv_disclosure_candidates.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('GMV source disclosures',len(rows),'release periods',len(set(r['release_period'] for r in rows)))
