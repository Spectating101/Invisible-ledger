"""Extract reported table cells, retaining reporting vintages and overlapping periods.
These are candidate issuer/segment observations, NOT an approved Indonesia sample.
"""
from pathlib import Path
import csv, re, json
from collections import defaultdict
ROOT=Path(__file__).resolve().parent
CONFIG={
 'blibli_fy2022_linked_0': [('2022Q4',0),('2021Q4',1),('2022FY',3),('2021FY',4)],
 'blibli_fy2024_linked_0': [('2024Q4',0),('2023Q4',1),('2024FY',3),('2023FY',4)],
 'blibli_fy2025_linked_0': [('2025Q4',0),('2024Q4',1),('2025FY',3),('2024FY',4)],
 'blibli_q12023_linked_0': [('2023Q1',0),('2022Q1',1)],
 'blibli_q32023_linked_0': [('2023Q3',0),('2022Q3',1),('2023M9',3),('2022M9',4)],
}
SEGMENTS=['1P Retail','3P Retail','Institutions','Physical Stores','Group']
logs={r['source_id']:r for r in json.loads((ROOT/'procurement_log.json').read_text())}
rows=[]
for source,periods in CONFIG.items():
 text=(ROOT/'text_extracts'/(source+'.txt')).read_text()
 # Begin at the operational table, not prose mentioning the metric.
 start=text.index('Selected Segmental Metrics')
 block=text[start:]; block=block[:block.index('Take Rate')]
 metric=None; values={}; locators={}
 for line in block.splitlines():
  if re.match(r'\s*Total Processing Value',line): metric='tpv';continue
  if re.match(r'\s*Net Revenues\s*$',line): metric='revenue';continue
  if re.match(r'\s*Gross Profit Before Discount',line): metric='gpbd';continue
  if metric is None: continue
  segment=next((s for s in SEGMENTS[:-1] if s in line),None)
  if re.match(r'\s*Total (TPV|Net Revenue|GPBD)',line):segment='Group'
  if segment is None:continue
  label=segment if segment!='Group' else re.search(r'Total (?:TPV|Net Revenues?|GPBD)',line).group()
  tail=line.split(label,1)[1]
  nums=re.findall(r'\(?-?\d[\d,]*(?:\.\d+)?\)?',tail)
  for period,col in periods:
   assert col<len(nums),(source,line,nums)
   token=nums[col]; value=float(token.replace(',','').replace('(','-').replace(')',''))
   values[(period,segment,metric)]=value
   locators[(period,segment,metric)]=line.strip()
 for period,_ in periods:
  for segment in SEGMENTS:
   row=dict(platform='Blibli/GDN',period=period,frequency='annual' if period.endswith('FY') else ('cumulative_9m' if period.endswith('M9') else 'quarter'),scope=segment,unit='IDR billion',source_id=source,source_url=logs[source]['url'],source_file=logs[source]['file'],source_page=text[:start].count('\f')+1,status='reported_cells_extracted; geography_and_scope_review_pending',indonesia_country_pair_confirmed='no')
   for metric in ['tpv','revenue','gpbd']:
    key=(period,segment,metric);assert key in values,key
    row[metric]=values[key];row[metric+'_source_line']=locators[key]
   rows.append(row)
out=ROOT/'source_extracts';out.mkdir(exist_ok=True)
def save(name,items):
 with (out/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(items[0]));w.writeheader();w.writerows(items)
save('blibli_reported_pairs_all_vintages.csv',rows)
groups=defaultdict(list)
for r in rows:groups[(r['period'],r['scope'])].append(r)
conflicts=[]
for key,rr in groups.items():
 if len({(r['tpv'],r['revenue'],r['gpbd']) for r in rr})>1:
  for r in rr:conflicts.append({k:r[k] for k in ['period','scope','tpv','revenue','gpbd','source_id']})
if conflicts:save('blibli_reporting_vintage_conflicts.csv',conflicts)
annual=[r for r in rows if r['frequency']=='annual' and r['scope']=='Group']
save('blibli_annual_group_candidates_all_vintages.csv',annual)
summary={'source_version_pair_rows':len(rows),'distinct_period_scope_keys':len(groups),'distinct_group_annual_years':len({r['period'] for r in annual}),'distinct_segment_annual_keys':len({(r['period'],r['scope']) for r in rows if r['frequency']=='annual' and r['scope']!='Group'}),'distinct_group_quarters':len({r['period'] for r in rows if r['frequency']=='quarter' and r['scope']=='Group'}),'conflict_keys':len({(r['period'],r['scope']) for r in conflicts}),'new_confirmed_country_sample_rows':0}
(ROOT/'extraction_counts.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
