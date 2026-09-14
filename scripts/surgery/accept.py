import sys
from docx import Document
from docx.oxml.ns import qn
B='/home/phyrexian/Downloads/llm_automation/project_portfolio/Solarpunk-bitcoin/'
d=Document(B+'Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx'); body=d.element.body
for tr in list(body.findall('.//'+qn('w:tr'))):
    t=tr.find(qn('w:trPr'))
    if t is not None and t.find(qn('w:del')) is not None: tr.getparent().remove(tr)
for p in list(body.findall('.//'+qn('w:p'))):
    pp=p.find(qn('w:pPr'))
    if pp is not None:
        rp=pp.find(qn('w:rPr'))
        if rp is not None and rp.find(qn('w:del')) is not None: p.getparent().remove(p); continue
for e in list(body.findall('.//'+qn('w:del'))): e.getparent().remove(e)
for e in list(body.findall('.//'+qn('w:ins'))):
    par=e.getparent(); i=list(par).index(e)
    for ch in list(e): par.insert(i,ch); i+=1
    par.remove(e)
# drop table shells left empty once deleted rows are accepted
for tbl in list(body.findall('.//'+qn('w:tbl'))):
    if not tbl.findall(qn('w:tr')): tbl.getparent().remove(tbl)
d.save(B+'Invisible_Ledger_Proposal_Sept01_ACCEPTED_PREVIEW_2026-09-14.docx')
