# -*- coding: utf-8 -*-
import sys, re
sys.path.insert(0,'/tmp/build')
from surg_lib import *
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

B='/home/phyrexian/Downloads/llm_automation/project_portfolio/Solarpunk-bitcoin/'
F=B+'Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx'
d=Document(F); body=d.element.body

def acc_text(ch):
    x=re.sub(r'<w:del [^>]*>.*?</w:del>','',ch.xml,flags=re.S)
    return ' '.join(re.sub(r'<[^>]+>','',x).split())

paras=[c for c in body.iterchildren() if c.tag.endswith('}p')]

# ---------- references: drop event-study-only, add finance ----------
DROP=re.compile(r'MacKinlay|Event studies in economics and finance|Brown and Warner|Fama')
refs=[p for p in paras if (p.find(qn('w:pPr')) is not None and
      (p.find(qn('w:pPr')).find(qn('w:pStyle')) is not None) and
      p.find(qn('w:pPr')).find(qn('w:pStyle')).get(qn('w:val'))=='Reference')]
print("reference paragraphs:",len(refs))
dropped=0
for p in refs:
    if DROP.search(acc_text(p)):
        del_paragraph(p); dropped+=1
print("event-study refs struck:",dropped)

have=' '.join(acc_text(p) for p in refs)
ADD=[
 "De Franco, G., Kothari, S. P., & Verdi, R. S. (2011). The benefits of financial statement comparability. Journal of Accounting Research, 49(4), 895–931.",
 "Berg, T., Burg, V., Gombović, A., & Puri, M. (2020). On the rise of FinTechs: Credit scoring using digital footprints. Review of Financial Studies, 33(7), 2845–2897.",
]
anchor=refs[-1] if refs else None
added=0
for r in ADD:
    key=r.split('(')[0].strip()
    if key.split(',')[0] in have: continue
    anchor=new_paragraph(body,'Reference',[('ins',r)],anchor); added+=1
print("finance refs inserted:",added)

# ---------- Flashpoint cover ----------
COVER=[("CoverBig","元智大學"),("CoverBig","YUAN ZE UNIVERSITY"),("Cover",""),
 ("Cover","管理學院財務金融暨會計碩士班"),("Cover","財務金融碩士學程"),("Cover",""),
 ("Cover","碩士論文計畫書"),("Cover","MASTER'S THESIS PROPOSAL"),("Cover",""),
 ("CoverBig","隱形帳簿：量化印尼平台經濟中的隱形楔子"),
 ("CoverBig","The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia's Platform Economy"),
 ("Cover",""),("Cover",""),
 ("Cover","研究生 / Student: 王新福 Christopher Ongko"),
 ("Cover","指導教授 / Advisor: 孔德蓉 De-Rong Kong"),("Cover",""),
 ("Cover","中華民國 115 年 9 月"),("Cover","September 2026")]
first=paras[0]
prev=None
for style,txt in COVER:
    p=OxmlElement('w:p')
    ppr=OxmlElement('w:pPr')
    st=OxmlElement('w:pStyle'); st.set(qn('w:val'),style); ppr.append(st)
    jc=OxmlElement('w:jc'); jc.set(qn('w:val'),'center'); ppr.append(jc)
    p.append(ppr)
    if txt: p.append(_run(txt))
    if prev is None: first.addprevious(p)
    else: prev.addnext(p)
    prev=p
# page break after cover
pb=OxmlElement('w:p'); r=OxmlElement('w:r')
br=OxmlElement('w:br'); br.set(qn('w:type'),'page'); r.append(br); pb.append(r)
prev.addnext(pb)

# ---------- Flashpoint page format ----------
for s in d.sections:
    s.page_width=Cm(21.0); s.page_height=Cm(29.7)
    s.top_margin=Cm(2.30); s.bottom_margin=Cm(2.00)
    s.left_margin=Cm(2.20); s.right_margin=Cm(2.20)
    s.header_distance=Cm(1.00); s.footer_distance=Cm(0.90)

# ---------- fonts: Times New Roman everywhere, black ----------
def force(styleobj, size=None, bold=None):
    f=styleobj.font
    f.name='Times New Roman'; f.color.rgb=RGBColor(0,0,0)
    if size: f.size=Pt(size)
    if bold is not None: f.bold=bold
    rpr=styleobj.element.get_or_add_rPr()
    rf=rpr.find(qn('w:rFonts'))
    if rf is None:
        rf=OxmlElement('w:rFonts'); rpr.insert(0,rf)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),'Times New Roman')

SPEC={'Normal':(12,None),'Body':(12,None),'BodyFirst':(12,None),'H1':(13,True),'H2':(12,True),
      'Equation':(12,None),'TableCaption':(10,None),'TableNote':(9.5,None),'Reference':(11,None),
      'Cover':(13,None),'CoverBig':(15,True)}
for name,(sz,bd) in SPEC.items():
    try: force(d.styles[name],sz,bd)
    except KeyError: pass
# strip any direct colour from runs
for p in body.iter(qn('w:r')):
    rpr=p.find(qn('w:rPr'))
    if rpr is not None:
        for c in rpr.findall(qn('w:color')): rpr.remove(c)

d.save(F); print("stage4 saved")
