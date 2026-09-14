# -*- coding: utf-8 -*-
import re,sys,difflib,unicodedata
sys.path.insert(0,'/tmp/build')

def norm(s):
    s=unicodedata.normalize('NFKD',s)
    s=s.replace('’',"'").replace('“','"').replace('”','"')
    s=s.replace('–','-').replace('—','-').replace('−','-')
    s=re.sub(r'HYPERLINK.*?"\d+"','',s)
    s=re.sub(r'[^a-z0-9 ]',' ',s.lower())
    return re.sub(r'\s+',' ',s).strip()

def sents(t):
    t=re.sub(r'\s+',' ',t)
    out=[]
    for s in re.split(r'(?<=[.;:])\s+(?=[A-Z(])',t):
        n=norm(s)
        if len(n.split())>=8: out.append((s.strip(),n))
    return out

def load(p):
    return open(p,encoding='utf8',errors='ignore').read()

def sect(txt,start,end):
    i=txt.rfind(start); j=txt.find(end,i+1) if end else len(txt)
    if j<0: j=len(txt)
    return txt[i:j] if i>=0 else ''

# ---------- ROOTSTOCK: Kong Sept01 accepted, sections 1-4 ----------
sep=load('/tmp/sep01_FINAL.txt')
root_txt=load('/tmp/root_s14.txt')
# strip table bodies (short lines) to keep prose
root=sents(root_txt)
print(f"ROOTSTOCK (Kong Sept-01 accepted, S1-S4): {len(root)} prose sentences\n")

CANDS=[
 ("Sep-12 Committee Rebuild",  '/tmp/c_rebuild.txt'),
 ("Sep-12 Committee Flow Rev", '/tmp/c_flow.txt'),
 ("Sep-13 Flashpoint Plain",   '/tmp/c_flash.txt'),
 ("Sep-14 Latest Best",        '/tmp/c_latest.txt'),
 ("Sep-14 Rootstock (new)",    '/tmp/c_new.txt'),
]

rows=[]
detail={}
for name,path in CANDS:
    cand=sents(load(path))
    cn=[n for _,n in cand]
    verb=near=echo=0; lost=[]
    for orig,n in root:
        best=0.0
        for c in cn:
            r=difflib.SequenceMatcher(None,n,c).ratio()
            if r>best: best=r
            if best>0.97: break
        if best>=0.95: verb+=1
        elif best>=0.75: near+=1
        elif best>=0.55: echo+=1
        else: lost.append((orig,best))
    tot=len(root)
    rows.append((name,verb,near,echo,len(lost),tot,len(cand)))
    detail[name]=lost

print(f"{'Version':<28}{'verbatim':>9}{'near':>7}{'echo':>7}{'gone':>7}{'carried%':>10}{'cand sents':>11}")
print("-"*79)
for name,v,nr,e,l,tot,cs in rows:
    carried=100*(v+nr)/tot
    print(f"{name:<28}{v:>9}{nr:>7}{e:>7}{l:>7}{carried:>9.0f}%{cs:>11}")
print()
for name,_ in CANDS:
    print(f"\n### Kong sentences with NO trace in {name} ({len(detail[name])}):")
    for orig,b in detail[name][:14]:
        print(f"   [{b:.2f}] {orig[:132]}")
