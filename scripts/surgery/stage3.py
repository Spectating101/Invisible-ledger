# -*- coding: utf-8 -*-
import sys, re, copy
sys.path.insert(0,'/tmp/build')
from surg_lib import *
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

B='/home/phyrexian/Downloads/llm_automation/project_portfolio/Solarpunk-bitcoin/'
F=B+'Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx'
d=Document(F); body=d.element.body

def acc(ch):
    x=re.sub(r'<w:del [^>]*>.*?</w:del>','',ch.xml,flags=re.S)
    return ' '.join(re.sub(r'<[^>]+>','',x).split())
def find(pred):
    for ch in body.iterchildren():
        if ch.tag.endswith('}p') and pred(acc(ch)): return ch
    return None
def ins_after(a, style, text): return new_paragraph(body, style, [('ins',text)], a)

def del_table(tbl):
    for tr in tbl.findall(qn('w:tr')):
        trPr=tr.find(qn('w:trPr'))
        if trPr is None: trPr=OxmlElement('w:trPr'); tr.insert(0,trPr)
        dl=OxmlElement('w:del'); dl.set(qn('w:id'),_id()); dl.set(qn('w:author'),AUTHOR); dl.set(qn('w:date'),DATE)
        trPr.append(dl)
        for p in tr.findall('.//'+qn('w:p')):
            rpr=first_rpr(p); txt=''.join(n.text or '' for n in p.iter(qn('w:t')))
            ppr=p.find(qn('w:pPr'))
            for ch in list(p):
                if ch is not ppr: p.remove(ch)
            if txt: p.append(_wrap('del',[_delrun(txt,rpr)]))

def ins_table(anchor, header, rows, size='19'):
    t=d.add_table(rows=1, cols=len(header))
    try: t.style='Table Grid'
    except Exception: pass
    t.alignment=WD_TABLE_ALIGNMENT.CENTER
    trPr=t.rows[0]._tr.get_or_add_trPr()
    th=OxmlElement('w:tblHeader'); th.set(qn('w:val'),'true'); trPr.append(th)
    def cellset(cell, txt, bold):
        cell.text=''
        p=cell.paragraphs[0]._p
        r=_run(txt); rpr=OxmlElement('w:rPr')
        rf=OxmlElement('w:rFonts')
        for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),'Times New Roman')
        rpr.append(rf)
        sz=OxmlElement('w:sz'); sz.set(qn('w:val'),size); rpr.append(sz)
        if bold: rpr.append(OxmlElement('w:b'))
        r.insert(0,rpr); p.append(_wrap('ins',[r]))
    for i,h in enumerate(header): cellset(t.rows[0].cells[i],h,True)
    for row in rows:
        tr=t.add_row(); trp=tr._tr.get_or_add_trPr()
        trp.append(OxmlElement('w:cantSplit'))
        ins=OxmlElement('w:ins'); ins.set(qn('w:id'),_id()); ins.set(qn('w:author'),AUTHOR); ins.set(qn('w:date'),DATE)
        trp.append(ins)
        for i,v in enumerate(row): cellset(tr.cells[i],v,False)
    body.remove(t._tbl); anchor.addnext(t._tbl)
    return t._tbl

def tbl_with(*needles):
    for c in body.iterchildren():
        if c.tag.endswith('}tbl'):
            txt=''.join(c.itertext())
            if all(n in txt for n in needles): return c
    return None

# ---- Table 1 (claims): strike rows tied to dropped material ----
t1=tbl_with('Established here')
assert t1 is not None, 'claims table not found'
for tr in t1.findall(qn('w:tr')):
    txt=' '.join(''.join(tr.itertext()).split())
    if re.search(r'ASEAN|Malaysia|GoTo|47-event|investor-response|LVG', txt, re.I):
        trPr=tr.find(qn('w:trPr'))
        if trPr is None: trPr=OxmlElement('w:trPr'); tr.insert(0,trPr)
        dl=OxmlElement('w:del'); dl.set(qn('w:id'),_id()); dl.set(qn('w:author'),AUTHOR); dl.set(qn('w:date'),DATE)
        trPr.append(dl)
        for p in tr.findall('.//'+qn('w:p')):
            rpr=first_rpr(p); tx=''.join(n.text or '' for n in p.iter(qn('w:t')))
            ppr=p.find(qn('w:pPr'))
            for ch in list(p):
                if ch is not ppr: p.remove(ch)
            if tx: p.append(_wrap('del',[_delrun(tx,rpr)]))

# ---- Table 2 -> evidence tiers ----
t2=tbl_with('Provenance','Metric')
assert t2 is not None, 'provenance table not found'
del_table(t2)
T2=ins_table(t2,
 ["Evidence tier","Series","Levels","Transitions"],
 [["Direct Indonesia-aligned segment","Tokopedia e-commerce","2","1"],
  ["Direct issuer, scope-pending","Blibli 3P Retail; Bukalapak Group","9","7"],
  ["Conditional country reconstruction","Grab Indonesia; Shopee Indonesia","6","4"],
  ["All tiers (inventory diagnostic)","5 series","17","12"]])

anch=find(lambda t:t.startswith('Two candidate observations are excluded under these rules'))

# ---- 4.3 candidate inventory ----
a=ins_after(anch,'H2','4.3 Candidate inventory across evidence modules')
a=ins_after(a,'BodyFirst','The study is not a single-fiscal-year design. Table 4 lists the seven retained modules. They are reported separately and never summed into one sample size, because their geographic, regulatory and business-model definitions differ.')
cap=ins_after(a,'TableCaption','Table 4. Retained evidence modules, coverage, and role. Each module has a distinct unit of observation; counts are not additive across rows.')
T3=ins_table(cap,["Module","Coverage","Retained scale","Role"],
 [["Direct Indonesian issuer candidates","FY2019–FY2025","13 period-matched platform/segment-years; 12 with positive revenue denominators","Candidate longitudinal core"],
  ["Conditional country reconstructions","FY2021–FY2024","6 Grab/Shopee platform-years","Sensitivity evidence only"],
  ["Indonesia marketplace structure","2022–2025","Platform-level market-share and structure evidence","Coverage, competition, structural breaks"],
  ["BPS official e-commerce evidence","2020–2024","National indicators; 39 provinces observed in 2023 and 2024","Activity, participation, channels, recordkeeping"],
  ["ASEAN corroboration","2019–2025","42 country-years from 450 source-vintage rows","Separate-country robustness"],
  ["Global issuer corroboration","Multi-year issuer histories","48 matched issuer-years, 8 businesses, 40 transitions","Business-model corroboration"],
  ["Historical quarterly accounting","2017–2022","47 company/segment-quarter observations","Historical disclosure evidence"]])

# ---- 4.4 Grab derivation (Kong requested) ----
a=new_paragraph(body,'H2',[('ins','4.4 Derivation of conditional country values')],T3)
a=ins_after(a,'BodyFirst','Grab discloses Indonesia revenue but not Indonesia transaction value, so its country transaction value must be derived; Table 5 sets out that derivation year by year. For each year the conditional construction applies Grab’s own Group monetization rate to its disclosed Indonesia revenue: Group monetization rate = Group revenue / Group GMV, and conditional Indonesia GMV = Indonesia revenue / Group monetization rate. The construction assumes that Grab’s Indonesian activity shares the Group revenue-to-GMV relationship: transparent and testable, but not a company disclosure and not independent evidence of an Indonesia-specific rate. Shopee’s Indonesian transaction value is an external market estimate and its revenue is derived from Sea’s disclosed monetization rate, so both Shopee inputs are conditional. The external estimate is taken from Momentum Works, whose annual Southeast Asian e-commerce report is the only recurring public source disaggregating regional marketplace gross merchandise value by country and platform. It is used because Sea Limited discloses no Indonesian figure, is labelled a third-party estimate wherever it enters a calculation, and is tested in the Section 5.1 sensitivity.')
cap=ins_after(a,'TableCaption','Table 5. Worked derivation of conditional Indonesia transaction value for Grab. Indonesia revenue is directly disclosed and Group revenue and Group GMV are source-reported; every Indonesia transaction value in the final column is derived by applying the Group monetization rate, not disclosed by the company.')
T4=ins_table(cap,["Year","Indonesia revenue","Group revenue","Group GMV","Conditional Indonesia GMV (derived)"],
 [["FY2021","US$79m","US$675m","US$16,061m","US$1,879.7m"],
  ["FY2022","US$275m","US$1,433m","US$19,937m","US$3,826.0m"],
  ["FY2023","US$605m","US$2,359m","US$20,983m","US$5,381.4m"]])

# ---- 4.5 key variables ----
a=new_paragraph(body,'H2',[('ins','4.5 Key variables')],T4)
a=ins_after(a,'BodyFirst','For each admissible platform-year the analysis records transaction value V, platform revenue R, the absolute wedge W = V − R, and the Ecosystem Ratio E = (V − R) / R. For each within-series annual transition it records transaction-value growth, revenue growth, and their difference D. Take rate is platform revenue divided by gross transaction value. Material divergences are reconciled against disclosed revenue components — customer incentives, gross and net revenue, monetization, and business scope — where the issuer reports them separately. That reconciliation is arithmetic against the issuer’s own categories; it is not a causal decomposition.')

# ---- 4.6 beyond platform accounts ----
a=ins_after(a,'H2','4.6 Evidence beyond platform accounts')
a=ins_after(a,'BodyFirst','BPS-Statistics Indonesia evidence, reported in Section 5.5, locates participant-facing digital commerce outside platform accounts. Bank Indonesia payment-system statistics provide supporting evidence on the infrastructure carrying that commerce; these series measure payment activity, not e-commerce sales. PMK 37/2025 provides for designated marketplaces to identify covered domestic sellers and to withhold and report Article 22 income tax at 0.5 percent of invoice gross turnover, using transaction-linked merchant turnover rather than marketplace corporate revenue. Blibli, Shopee Indonesia, Tokopedia, and Lazada were designated on 1 July 2026, with collection taking effect on 1 August 2026 after a month allowed for system adjustment. Application was subsequently postponed through 31 October 2026, amounts already withheld were ordered returned to sellers, and the mechanism is now scheduled to take effect on 1 November 2026. The Directorate General of Taxes describes the measure as a change in collection mechanism rather than a new tax, so it cannot be read as evidence that sellers previously underpaid. It establishes a legal reporting architecture; no completed post-implementation period yet exists from which to estimate a compliance effect.')

d.save(F); print("stage3 consolidated: §4.2-4.6 built")
