import sys, re
sys.path.insert(0,'/tmp/build')
from surg_lib import *
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy
B='/home/phyrexian/Downloads/llm_automation/project_portfolio/Solarpunk-bitcoin/'
F=B+'Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx'
d=Document(F); body=d.element.body
t1=None
for t in d.tables:
    if 'Established here' in ''.join(t._tbl.itertext()):
        t1=t._tbl; break
assert t1 is not None, 'claims table not found'
live=[tr for tr in t1.findall(qn('w:tr'))
      if not (tr.find(qn('w:trPr')) is not None and tr.find(qn('w:trPr')).find(qn('w:del')) is not None)]
model=live[-1]
ROWS=[("A longitudinal Indonesian series of the transaction–revenue wedge across seventeen admitted platform-years, reported by evidence tier.",
       "A population estimate of Indonesia's platform economy, or a complete measure of activity outside platform accounts."),
      ("An arithmetic reconciliation of selected large divergences against disclosed revenue components.",
       "A causal decomposition of why monetization, incentives, or perimeter changed."),
      ("A legal route from marketplace-held seller and transaction records into third-party reporting and withholding.",
       "That compliance, collections, or enforcement outcomes have improved under PMK 37/2025.")]
anchor=live[-1]
for a,b in ROWS:
    tr=copy.deepcopy(model)
    trp=tr.find(qn('w:trPr'))
    if trp is None:
        trp=OxmlElement('w:trPr'); tr.insert(0,trp)
    for old in trp.findall(qn('w:ins')): trp.remove(old)
    ins=OxmlElement('w:ins'); ins.set(qn('w:id'),_id()); ins.set(qn('w:author'),AUTHOR); ins.set(qn('w:date'),DATE)
    trp.append(ins)
    for cell,txt in zip(tr.findall(qn('w:tc')), (a,b)):
        for p in cell.findall(qn('w:p')):
            rpr=first_rpr(p); ppr=p.find(qn('w:pPr'))
            for ch in list(p):
                if ch is not ppr: p.remove(ch)
        ps=cell.findall(qn('w:p'))
        for extra in ps[1:]: cell.remove(extra)
        p=ps[0]
        p.append(_wrap('ins',[_run(txt, first_rpr(model.findall(qn('w:tc'))[0].findall(qn('w:p'))[0]))]))
    anchor.addnext(tr); anchor=tr
d.save(F); print("Table 1 rows added:",len(ROWS))
