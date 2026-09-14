#!/usr/bin/env python3
"""Structural validation of OOXML .docx files.

Checks the class of problem that causes Word to report "unreadable content"
and silently repair a file -- distinct from rendering differences, which a
visual check catches. Run before sending any document.
"""
import sys, zipfile, re
from lxml import etree
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def validate(path):
    z=zipfile.ZipFile(path); names=set(z.namelist()); issues=[]
    for n in names:
        if n.endswith(('.xml','.rels')):
            try: etree.fromstring(z.read(n))
            except Exception as e: issues.append(f'malformed XML in {n}: {e}')
    ct=z.read('[Content_Types].xml').decode('utf8')
    for o in re.findall(r'PartName="/([^"]+)"',ct):
        if o not in names: issues.append(f'Content-Types override with no part: {o}')
    for n in [x for x in names if x.endswith('.rels')]:
        base=n.rsplit('_rels/',1)[0]
        for rel in etree.fromstring(z.read(n)):
            t=rel.get('Target')
            if rel.get('TargetMode','Internal')=='External' or not t or t.startswith('#'): continue
            p=(base+t).replace('/./','/')
            while '/../' in p: p=re.sub(r'[^/]+/\.\./','',p,count=1)
            if p.lstrip('/') not in names: issues.append(f'broken relationship {n} -> {t}')
    d=etree.fromstring(z.read('word/document.xml'))
    defined=set()
    if 'word/styles.xml' in names:
        defined={s.get(W+'styleId') for s in etree.fromstring(z.read('word/styles.xml')).iter(W+'style')}
    for e in list(d.iter(W+'pStyle'))+list(d.iter(W+'rStyle')):
        v=e.get(W+'val')
        if v and v not in defined: issues.append(f'undefined style reference: {v}')
    for ti,tbl in enumerate(d.iter(W+'tbl'),1):
        g=tbl.find(W+'tblGrid'); nc=len(g.findall(W+'gridCol')) if g is not None else 0
        for ri,tr in enumerate(tbl.findall(W+'tr'),1):
            sp=sum(int(tc.find(W+'tcPr').find(W+'gridSpan').get(W+'val'))
                   if (tc.find(W+'tcPr') is not None and tc.find(W+'tcPr').find(W+'gridSpan') is not None) else 1
                   for tc in tr.findall(W+'tc'))
            if nc and sp!=nc: issues.append(f'table {ti} row {ri}: {sp} cells vs {nc} grid columns')
    ids=[e.get(W+'id') for e in d.iter() if e.tag in (W+'ins',W+'del') and e.get(W+'id')]
    if len(ids)!=len(set(ids)):
        issues.append(f'{len(ids)-len(set(ids))} duplicate revision ids (Word may group unrelated changes on accept/reject)')
    cs={e.get(W+'id') for e in d.iter(W+'commentRangeStart')}
    ce={e.get(W+'id') for e in d.iter(W+'commentRangeEnd')}
    cd=set()
    if 'word/comments.xml' in names:
        cd={c.get(W+'id') for c in etree.fromstring(z.read('word/comments.xml')).iter(W+'comment')}
    if cs^ce: issues.append(f'unbalanced comment ranges: {sorted(cs^ce)}')
    if cd-cs: issues.append(f'orphaned comment definitions: {sorted(cd-cs)}')
    if cs-cd: issues.append(f'comment anchors with no definition: {sorted(cs-cd)}')
    fr={e.get(W+'id') for e in d.iter(W+'footnoteReference')}
    if fr and 'word/footnotes.xml' in names:
        fd={f.get(W+'id') for f in etree.fromstring(z.read('word/footnotes.xml')).iter(W+'footnote')}
        if fr-fd: issues.append(f'unresolved footnote references: {sorted(fr-fd)}')
    if d.find(W+'body/'+W+'sectPr') is None: issues.append('missing final sectPr')
    return issues

if __name__=='__main__':
    bad=0
    for p in sys.argv[1:]:
        iss=validate(p)
        print(f"{'CLEAN ' if not iss else 'ISSUES'}  {p.split('/')[-1]}")
        for i in iss: print(f"          - {i}")
        bad += bool(iss)
    sys.exit(1 if bad else 0)
