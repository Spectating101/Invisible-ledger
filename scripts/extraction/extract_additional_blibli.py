"""New reported-cell candidates from three additional text-readable issuer tables."""
from pathlib import Path
import json,csv,re
ROOT=Path(__file__).resolve().parent;B=ROOT/'broad_archive'
config={'Earnings-Release-1H23': [('2023Q2',0),('2022Q2',1),('2023H1',3),('2022H1',4)],'Earnings-Release-1Q26':[('2026Q1',0),('2025Q1',1),('2025FY',3)],'Earnings-Release-1H26':[('2026Q2',0),('2025Q2',1),('2026H1',3),('2025H1',4)]}
segments=['1P Retail','3P Retail','Institutions','Physical Stores','Group'];rows=[]
for r in json.loads((B/'manifest.json').read_text()):
    key=next((k for k in config if k in r['url']),None)
    if not key or not r.get('text_file'):continue
    text=(B/r['text_file']).read_text();start=text.index('Selected Segmental Metrics');block=text[start:];block=block[:block.index('Take Rate')]
    metric=None;values={};lines={}
    for line in block.splitlines():
        if re.match(r'\s*Total Processing Value',line):metric='tpv';continue
        if re.match(r'\s*Net Revenues\s*$',line):metric='revenue';continue
        if re.match(r'\s*Gross Profit Before Discount',line):metric='gpbd';continue
        if metric is None:continue
        scope=next((s for s in segments[:-1] if s in line),None)
        total=re.match(r'\s*(Total (?:TPV|Net Revenues?|GPBD))',line)
        if total:scope='Group'
        if not scope:continue
        label=total.group(1) if total else scope
        nums=re.findall(r'\(?-?\d[\d,]*(?:\.\d+)?\)?',line.split(label,1)[1])
        for period,col in config[key]:
            token=nums[col];values[(period,scope,metric)]=float(token.replace(',','').replace('(','-').replace(')',''));lines[(period,scope,metric)]=line.strip()
    for period,_ in config[key]:
        for scope in segments:
            row=dict(platform='Blibli/GDN',period=period,scope=scope,unit='IDR billion',source_file='broad_archive/'+r['file'],source_url=r['url'],pdf_page=text[:start].count('\f')+1,status='reported table extraction; geographic eligibility and visual cell review pending')
            for m in ['tpv','revenue','gpbd']:
                row[m]=values[(period,scope,m)];row[m+'_source_line']=lines[(period,scope,m)]
            rows.append(row)
        for m in ['tpv','revenue','gpbd']:
            delta=values[(period,'Group',m)]-sum(values[(period,s,m)] for s in segments[:-1])
            assert abs(delta)<=2,(period,m,delta)
with (ROOT/'source_extracts/blibli_additional_reported_pairs.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('new table rows',len(rows),'quarter keys',sorted({r['period'] for r in rows if 'Q' in r['period']}))
