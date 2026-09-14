import sys, re
sys.path.insert(0,'/tmp/build')
from surg_lib import *
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

B='/home/phyrexian/Downloads/llm_automation/project_portfolio/Solarpunk-bitcoin/'
F=B+'Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx'
d=Document(F); body=d.element.body

# 1) strip orphaned revision-note hyperlinks / bookmarks (they pointed at the deleted appendix)
killed=0
for h in list(body.findall('.//'+qn('w:hyperlink'))):
    anc=h.get(qn('w:anchor')) or ''
    if anc.startswith('RevNote') or anc.startswith('RevSrc'):
        h.getparent().remove(h); killed+=1
# leftover superscript digit runs immediately following removed links
for r in list(body.findall('.//'+qn('w:r'))):
    rpr=r.find(qn('w:rPr'))
    if rpr is None: continue
    va=rpr.find(qn('w:vertAlign'))
    if va is not None and va.get(qn('w:val'))=='superscript':
        txt=''.join(t.text or '' for t in r.iter(qn('w:t')))
        if r.find(qn('w:commentReference')) is not None: continue
        if txt.strip().isdigit():
            r.getparent().remove(r); killed+=1
print("revision-note artifacts removed:",killed)

# 2) fix run-split artifacts inside text I rebuilt
FIX=[("transaction value s and platform revenue s","transaction values and platform revenues"),
     ("record keeper s places","record keepers places"),
     ("deductible expenses ,","deductible expenses,"),
     ("  "," ")]
n=0
for t in body.iter(qn('w:t')):
    if not t.text: continue
    o=t.text
    for a,b in FIX: o=o.replace(a,b)
    o=re.sub(r'\s+\.','.',o); o=re.sub(r'\s+,',',',o)
    if o!=t.text: t.text=o; n+=1
for t in body.iter(qn('w:delText')):
    if t.text: t.text=re.sub(r'\s+\.','.',t.text)
print("text nodes repaired:",n)

# 3) add the missing 3.1 heading
def acc(ch):
    x=re.sub(r'<w:del [^>]*>.*?</w:del>','',ch.xml,flags=re.S)
    return ' '.join(re.sub(r'<[^>]+>','',x).split())
anchor=None
for ch in body.iterchildren():
    if ch.tag.endswith('}p') and acc(ch).startswith('3. Theoretical Framework'):
        anchor=ch; break
if anchor is not None:
    new_paragraph(body,'H2',[('ins','3.1 The measure')],anchor)
    print("3.1 heading inserted")

d.save(F); print("stage6 saved")
