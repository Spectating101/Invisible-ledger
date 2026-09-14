# FIX 5: real footnote for the GTV/GMV terminology (advisor comment 130)
import sys, re, zipfile, shutil
sys.path.insert(0,'/tmp/build')
from surg_lib import *
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
B='/home/phyrexian/Downloads/llm_automation/project_portfolio/Solarpunk-bitcoin/'
F=B+'Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx'
d=Document(F); body=d.element.body
part=d.part
fpart=None
for rel in part.rels.values():
    if 'footnotes' in rel.reltype: fpart=rel.target_part
if fpart is None:
    print('no footnotes part'); sys.exit()
froot=fpart._element if hasattr(fpart,'_element') else None
from lxml import etree
froot=etree.fromstring(fpart.blob)
ids=[int(f.get(qn('w:id'))) for f in froot.findall(qn('w:footnote'))]
new_id=max(ids)+1
TXT=("Gross transaction value (GTV) and gross merchandise value (GMV) denote the same quantity; issuers label it "
     "differently. Grab and Sea report GMV, while GoTo, Blibli and Bukalapak report GTV or transaction processing value. "
     "This proposal uses GTV throughout and preserves each issuer's own label only when quoting a disclosed figure.")
fn=OxmlElement('w:footnote'); fn.set(qn('w:id'),str(new_id))
p=OxmlElement('w:p')
ppr=OxmlElement('w:pPr'); st=OxmlElement('w:pStyle'); st.set(qn('w:val'),'FootnoteText'); ppr.append(st); p.append(ppr)
r0=OxmlElement('w:r'); rpr0=OxmlElement('w:rPr'); sr=OxmlElement('w:rStyle'); sr.set(qn('w:val'),'FootnoteReference'); rpr0.append(sr); r0.append(rpr0)
r0.append(OxmlElement('w:footnoteRef')); p.append(r0)
r1=OxmlElement('w:r'); t1=OxmlElement('w:t'); t1.set(qn('xml:space'),'preserve'); t1.text=' '+TXT; r1.append(t1); p.append(r1)
fn.append(p); froot.append(fn)
fpart._blob = etree.tostring(froot, xml_declaration=True, encoding='UTF-8', standalone=True)

# anchor the footnote after the GTV/GMV definition sentence
def acc(ch):
    x=re.sub(r'<w:del [^>]*>.*?</w:del>','',ch.xml,flags=re.S)
    return ' '.join(re.sub(r'<[^>]+>','',x).split())
target=None
for ch in body.iterchildren():
    if ch.tag.endswith('}p') and 'regardless of who ultimately receives the proceeds' in acc(ch):
        target=ch; break
if target is None: print('anchor paragraph not found'); sys.exit()
ref=OxmlElement('w:r')
rpr=OxmlElement('w:rPr'); rs=OxmlElement('w:rStyle'); rs.set(qn('w:val'),'FootnoteReference'); rpr.append(rs); ref.append(rpr)
fr=OxmlElement('w:footnoteReference'); fr.set(qn('w:id'),str(new_id)); ref.append(fr)
ins=OxmlElement('w:ins'); ins.set(qn('w:id'),_id()); ins.set(qn('w:author'),AUTHOR); ins.set(qn('w:date'),DATE); ins.append(ref)
target.append(ins)
d.save(F)
# rewrite footnotes.xml into the saved package
tmp=F+'.tmp'
zin=zipfile.ZipFile(F); zout=zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED)
for it in zin.infolist():
    data=zin.read(it.filename)
    if it.filename=='word/footnotes.xml': data=fpart._blob
    zout.writestr(it,data)
zin.close(); zout.close(); shutil.move(tmp,F)
print(f'FIX5 footnote id={new_id} added and anchored')
