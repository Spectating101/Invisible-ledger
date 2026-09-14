import sys, re
sys.path.insert(0,'/tmp/build')
from surg_lib import *
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn

B='/home/phyrexian/Downloads/llm_automation/project_portfolio/Solarpunk-bitcoin/'
F=B+'Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx'
d=Document(F); body=d.element.body

def acc(ch):
    x=re.sub(r'<w:del [^>]*>.*?</w:del>','',ch.xml,flags=re.S)
    return ' '.join(re.sub(r'<[^>]+>','',x).split())
def style_of(p):
    ppr=p.find(qn('w:pPr'))
    if ppr is None: return ''
    s=ppr.find(qn('w:pStyle'))
    return s.get(qn('w:val')) if s is not None else ''

paras=[c for c in body.iterchildren() if c.tag.endswith('}p')]
refs=[p for p in paras if style_of(p)=='Reference']
bodytxt=' '.join(acc(p) for p in paras if style_of(p) not in ('Reference',))
bodytxt+=' '+' '.join(''.join(t.itertext()) for t in body.iterchildren() if t.tag.endswith('}tbl'))

def surname(r):
    m=re.match(r'\s*([A-Z][A-Za-zÀ-ÿ’\'-]+)', r)
    return m.group(1) if m else None

# institutional entries keep if their body keyword appears
INST={'OECD':'OECD','European':'DAC7','International Accounting':'IFRS','IASB':'IFRS',
      'Google':'Google','Momentum':'Momentum','International Labour':'International Labour'}
kept=struck=0
for p in refs:
    t=acc(p)
    if not t.strip(): continue
    sn=surname(t); hit=False
    for k,v in INST.items():
        if t.startswith(k): hit = v in bodytxt; break
    else:
        hit = bool(sn and re.search(r'\b'+re.escape(sn)+r'\b', bodytxt))
    if hit: kept+=1
    else:
        del_paragraph(p); struck+=1
print(f"references kept {kept}, struck as uncited {struck}")

# tighten body spacing a touch
for name,sa in (('Body',3),('BodyFirst',3),('Reference',2),('TableCaption',2),('TableNote',2)):
    try:
        pf=d.styles[name].paragraph_format
        pf.space_after=Pt(sa); pf.space_before=Pt(0)
    except KeyError: pass
for name,(sb,sa) in (('H1',(8,4)),('H2',(6,2))):
    try:
        pf=d.styles[name].paragraph_format
        pf.space_before=Pt(sb); pf.space_after=Pt(sa)
    except KeyError: pass
d.save(F); print("stage5 saved")
