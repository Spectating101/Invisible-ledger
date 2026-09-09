"""Extract the FY2025 20-F geographic revenue table; not a country GTV estimate."""
from pathlib import Path
import csv,re
ROOT=Path(__file__).resolve().parent
path=ROOT/'text_extracts/grab_fy2025_20f.txt'
text=path.read_text();start=text.index('ii)         Geographic information')
block=text[start:text.index('iii)',start)]
rows=[]
countries=['Indonesia','Malaysia','Philippines','Singapore','Thailand','Vietnam','Rest of Southeast Asia']
for line in block.splitlines():
 country=next((c for c in countries if line.strip().startswith(c)),None)
 if not country:continue
 vals=re.findall(r'\d[\d,]*',line.split(country,1)[1]);assert len(vals)==3,(line,vals)
 for year,value in zip([2025,2024,2023],vals):
  rows.append(dict(platform='Grab',country=country,year=year,revenue_usd_million=int(value.replace(',','')),status='direct_geographic_revenue_only',source_file='raw_sources/grab_fy2025_20f.pdf',pdf_page=text[:start].count('\f')+1,source_line=line.strip()))
assert len(rows)==21
for year,total in [(2025,3370),(2024,2797),(2023,2359)]:assert sum(r['revenue_usd_million'] for r in rows if r['year']==year)==total
with (ROOT/'source_extracts/grab_country_revenue_2023_2025.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('21 source country-year revenue rows; six named countries plus regional residual; no country GTV derived')
