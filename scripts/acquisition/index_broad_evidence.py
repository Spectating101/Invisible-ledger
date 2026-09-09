"""New search aid for saved evidence. Excerpts are not independent observations."""
from pathlib import Path
import csv,json,re,hashlib,collections
ROOT=Path(__file__).resolve().parent/'broad_archive'
records=json.loads((ROOT/'manifest.json').read_text())
rows=[]; documents=[]
pattern=re.compile(r'\b(GMV|GTV|TPV|Indonesia|Malaysia|Vietnam|Thailand|Philippines|Singapore|monetization|incentives|principal|agent|e-commerce|marketplace)\b',re.I)
for r in records:
    if r['status']!='downloaded':continue
    p=ROOT/r['file']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],p
    documents.append(dict(module=r['module'],label=r.get('label',''),file=r['file'],bytes=r['bytes'],sha256=r['sha256'],url=r['url'],parent=r.get('parent',''),retrieved_utc=r.get('retrieved_utc',''),text_file=r.get('text_file','')))
    if not r.get('text_file'):continue
    for page,body in enumerate((ROOT/r['text_file']).read_text(errors='replace').split('\f'),1):
        lines=body.splitlines()
        for i,line in enumerate(lines):
            terms=pattern.findall(line)
            if not terms:continue
            rows.append(dict(module=r['module'],source_file=r['file'],pdf_page=page,line_on_page=i+1,matched_terms=';'.join(sorted(set(terms))),excerpt=' '.join(x.strip() for x in lines[max(0,i-1):i+3]),source_url=r['url'],status='search excerpt; not validated numeric observation'))
for name,data in [('document_manifest.csv',documents),('searchable_source_excerpts.csv',rows)]:
    if data:
        with (ROOT/name).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
print(json.dumps(dict(documents=len(documents),unique_bytes=len(set(r['sha256'] for r in documents)),source_excerpts=len(rows),modules=dict(collections.Counter(r['module'] for r in documents))),indent=2))
