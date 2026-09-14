import sys, re, zipfile, shutil, os
sys.path.insert(0,'/tmp/build')
from surg_lib import *
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

B='/home/phyrexian/Downloads/llm_automation/project_portfolio/Solarpunk-bitcoin/'
F=B+'Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx'
d=Document(F); body=d.element.body

# --- re-anchor comment 153 (GoTo/Indonesia scope) onto the new sample-table caption ---
def acc(ch):
    x=re.sub(r'<w:del [^>]*>.*?</w:del>','',ch.xml,flags=re.S)
    return ' '.join(re.sub(r'<[^>]+>','',x).split())
target=None
for ch in body.iterchildren():
    if ch.tag.endswith('}p') and acc(ch).startswith('Table 2. Evidence tiers'):
        target=ch; break
if target is not None:
    s=OxmlElement('w:commentRangeStart'); s.set(qn('w:id'),'153')
    e=OxmlElement('w:commentRangeEnd');   e.set(qn('w:id'),'153')
    r=OxmlElement('w:r'); rp=OxmlElement('w:rPr')
    va=OxmlElement('w:vertAlign'); va.set(qn('w:val'),'superscript'); rp.append(va)
    ref=OxmlElement('w:commentReference'); ref.set(qn('w:id'),'153')
    r.append(rp); r.append(ref)
    ppr=target.find(qn('w:pPr'))
    target.insert(1 if ppr is not None else 0, s)
    target.append(e); target.append(r)
    print("comment id153 re-anchored to the sample-table caption")
d.save(F)

# --- prune orphaned comment entries so Word does not flag the package ---
doc_xml=zipfile.ZipFile(F).read('word/document.xml').decode('utf8')
live=set(re.findall(r'<w:commentRangeStart w:id="(\d+)"',doc_xml))
tmp=F+'.tmp'
zin=zipfile.ZipFile(F); zout=zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED)
removed=[]
for item in zin.infolist():
    data=zin.read(item.filename)
    if item.filename in ('word/comments.xml','word/commentsExtended.xml',
                         'word/commentsIds.xml','word/commentsExtensible.xml'):
        x=data.decode('utf8')
        if item.filename=='word/comments.xml':
            def drop(m):
                cid=re.search(r'w:id="(\d+)"',m.group(0)).group(1)
                if cid in live: return m.group(0)
                removed.append(cid); return ''
            x=re.sub(r'<w:comment .*?</w:comment>',drop,x,flags=re.S)
        else:
            # strip paraId-keyed entries whose comment is gone: safest is to empty these parts
            x=re.sub(r'<w15:commentEx [^>]*/>','',x)
            x=re.sub(r'<w16cid:commentId [^>]*/>','',x)
            x=re.sub(r'<w16cex:commentExtensible [^>]*/>','',x)
        data=x.encode('utf8')
    zout.writestr(item, data)
zin.close(); zout.close(); shutil.move(tmp,F)
print(f"orphaned comment entries pruned: {len(removed)} -> ids {sorted(set(removed),key=int)}")
z=zipfile.ZipFile(F)
print("comments remaining:", len(re.findall(r'<w:comment ', z.read('word/comments.xml').decode('utf8'))))
print("anchors:", len(re.findall(r'<w:commentRangeStart', z.read('word/document.xml').decode('utf8'))))
