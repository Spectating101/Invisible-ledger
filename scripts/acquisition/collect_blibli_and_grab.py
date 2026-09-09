"""Public IR page embedded document lists; supplements existing saved Grab history."""
import re,json
import collect_broad_archive as a
pages=[(f'https://about.blibli.com/en/investor-relations/{slug}','blibli','','issuer document index') for slug in ['annual-reports','financial-information','sustainability-reports','prospectus']]
a.collect(pages)
items=[]
for url,module,_,_ in pages:
    r=a.records[url]
    if r['status']!='downloaded':continue
    text=a.read(r).replace('\\/','/')
    for link in set(re.findall(r'https[^\s"<>]+\.pdf',text,re.I)):
        items.append((link,module,url,'embedded issuer PDF link'))
grab=[
'https://s205.q4cdn.com/179588156/files/doc_financials/2026/q2/Grab-Reports-Record-Second-Quarter-2026-Results.pdf',
'https://s205.q4cdn.com/179588156/files/doc_financials/2026/q2/Grab-Q2-2026-Earnings-Presentation.pdf',
'https://s205.q4cdn.com/179588156/files/doc_financials/2026/q2/Grab-Q2-2026-Earnings-Remarks.pdf',
]
items.extend((u,'grab','https://investors.grab.com/financial-information/quarterly-results/default.aspx','Q2 2026 issuer disclosure') for u in grab)
a.collect(items)
print('discovered issuer PDF URLs',len(set(u for u,*_ in items)))
