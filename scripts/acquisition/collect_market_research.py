"""Original market research publisher articles, not numerical platform observations.
Uses the publisher's public WordPress API; preserves original JSON and article links.
Figures are collected only for directly relevant market-report titles.
"""
import csv,json,re
from urllib.parse import quote,urljoin
from bs4 import BeautifulSoup
import collect_broad_archive as a
posts={}
for query in ['ecommerce','food delivery']:
    for page in range(1,21):
        u=f'https://thelowdown.momentum.asia/wp-json/wp/v2/posts?search={quote(query)}&per_page=100&page={page}&before=2026-09-09T23:59:59'
        a.collect([(u,'momentum','','public publisher article search')])
        r=a.records[u]
        if r['status']!='downloaded':break
        data=json.loads(a.read(r))
        if not isinstance(data,list):break
        for p in data:posts[p['id']]=(p,r['file'])
        if len(data)<100:break
rows=[];figures=[]
for p,source in posts.values():
    title=BeautifulSoup(p['title']['rendered'],'html.parser').get_text(' ',strip=True)
    soup=BeautifulSoup(p['content']['rendered'],'html.parser')
    text=soup.get_text(' ',strip=True)
    relevant=bool(re.search(r'GMV|market share|new report|ecommerce in southeast|e-commerce in southeast|food delivery.*(20\d\d|report)|indonesia.*(market|ecommerce)',title,re.I))
    rows.append(dict(post_id=p['id'],published=p['date'],title=title,url=p['link'],source_json=source,market_report_candidate=relevant,article_text=text,status='publisher narrative; not numeric dataset'))
    if relevant:
        for image in soup.select('img[src]'):
            u=urljoin(p['link'],image['src'])
            if 'momentum.asia' in u:figures.append((u,'momentum_figures',p['link'],title))
        for link in soup.select('a[href]'):
            u=urljoin(p['link'],link['href'])
            if '.pdf' in u.lower() and 'momentum.asia' in u:figures.append((u,'momentum_reports',p['link'],title))
with (a.ROOT/'momentum_publisher_articles.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
a.collect(figures)
print(dict(publisher_articles=len(rows),market_report_candidates=sum(r['market_report_candidate'] for r in rows),figure_and_report_urls=len(set(x[0] for x in figures))))
