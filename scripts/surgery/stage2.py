# -*- coding: utf-8 -*-
import sys, copy, re
sys.path.insert(0,'/tmp/build')
from surg_lib import *
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

B='/home/phyrexian/Downloads/llm_automation/project_portfolio/Solarpunk-bitcoin/'
F=B+'Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx'
d=Document(F); body=d.element.body

def find(pred):
    for ch in body.iterchildren():
        if ch.tag.endswith('}p'):
            x=re.sub(r'<w:del [^>]*>.*?</w:del>','',ch.xml,flags=re.S)
            t=' '.join(re.sub(r'<[^>]+>','',x).split())
            if pred(t): return ch
    return None

def ins_after(anchor, style, text):
    return new_paragraph(body, style, [('ins',text)], anchor)

# ---------- 1.1 heading + research question ----------
a=find(lambda t:t.strip()=='1. Introduction')
ins_after(a,'H2','1.1 Research Background and Motivation')

a=find(lambda t:t.startswith('The paper measures gross participant-facing transaction value'))
a=ins_after(a,'Body','The thesis therefore asks how large the invisible wedge is in Indonesia’s platform economy, how it changes through time, what mechanisms explain those changes, and how much of the participant-facing activity already recorded by platforms enters routine third-party reporting and tax administration.')

# ---------- 2.2 accounting ----------
a=find(lambda t:t.startswith('The economics of multisided platforms begins'))
a=ins_after(a,'H2','2.2 Revenue recognition and the accounting boundary')
ins_after(a,'BodyFirst','Accounting rules and business-model design determine how transaction value becomes platform revenue. Under IFRS 15, principal–agent treatment affects whether revenue is presented gross or net. Customer incentives, advertising and service income, acquisitions, and changes in reporting perimeter can move recognized revenue without an equivalent change in facilitated commerce. Comparability matters because users of financial statements must understand how similar economic events map into reported numbers; De Franco, Kothari, and Verdi (2011) show that comparability is associated with a stronger analyst information environment. These mechanisms determine how the invisible wedge appears in corporate accounts and how it changes through time.')

# ---------- 2.6 research gap ----------
a=find(lambda t:t.startswith('Corporate digital-tax reforms'))
a=ins_after(a,'Body','Indonesia’s PMK 37/2025 applies the same logic through seller identification, transaction-linked reporting, and marketplace withholding.')
a=ins_after(a,'H2','2.6 Research gap')
ins_after(a,'BodyFirst','Taken together, these literatures explain why transaction value can exceed platform revenue, why accounting presentation can move the two apart, why participant reporting remains incomplete, and why third-party information matters for tax administration. What remains less developed is a longitudinal, source-auditable account for a single market that measures the invisible wedge, explains why it changes, and connects the digitally recorded participant-facing flow to the reporting mechanisms through which a tax authority can observe it. This thesis addresses that gap for Indonesia.')

# ---------- 3.2 movement ----------
a=find(lambda t:t.startswith('This distinction is essential.'))
a=ins_after(a,'H2','3.2 Movement over time')
a=ins_after(a,'BodyFirst','The ecosystem ratio measures scale at a point in time. Because the transaction–revenue relationship also changes, the analysis defines a growth-divergence measure.')
a=ins_after(a,'Equation','Growth divergence = transaction-value growth − platform-revenue growth    (2)')
ins_after(a,'Body','A value of zero indicates that transaction value and revenue move together and the wedge is stable in relative terms. A positive value indicates transaction value growing faster than revenue, widening the wedge; a negative value indicates the reverse. Opposite signs identify periods in which transaction activity and platform revenue move in different directions, which are the cases where a monetization or reporting mechanism is most likely to be doing the work. Material movements are then reconciled against disclosed revenue components: monetization, customer incentives, gross-versus-net revenue recognition, and changes in business scope.')

# ---------- 4.1 new platform-selection paragraph ----------
a=find(lambda t:'Public listing makes these platforms unusually observable' in t)
ins_after(a,'Body','Grab does not disclose gross transaction value by country; its transaction measures are reported by business line, so an Indonesian figure must be derived from a company-wide take rate. Sea Limited discloses revenue for Southeast Asia as a single region with no Indonesia breakout, so Shopee\u2019s Indonesian transaction value must be drawn from an external market-research source. GoTo reports both inputs directly, but only at Group level, which includes operations outside Indonesia. No listed platform therefore publishes a strictly country-labelled matched pair for Indonesia. Three Indonesian issuers come closest and carry the longitudinal evidence: PT Global Digital Niaga Tbk (Blibli), PT Bukalapak.com Tbk, and Tokopedia, reported as an e-commerce segment within PT GoTo Gojek Tokopedia Tbk. Each reports transaction value and revenue for the same period from a single issuer disclosure, but their perimeters differ: Tokopedia\u2019s e-commerce segment is Indonesia-aligned, Blibli\u2019s 3P Retail segment also contains travel, and Bukalapak\u2019s Group figures include overseas operations. Section 4.2 therefore admits every observation under an explicit evidence tier rather than treating any of them as an Indonesia-only measurement.')


# ---- Abstract (advisor comment 2: 100-150 words) ----
a=find(lambda t:t.strip()=='1. Introduction')
h=new_paragraph(body,'H1',[('ins','Abstract')],a)
h.addnext(a)  # keep Introduction after the abstract block
ap=new_paragraph(body,'BodyFirst',[('ins',"This study measures the gap between the transaction value digital platforms process in Indonesia and the revenue those platforms recognize for themselves. I call that gap the invisible wedge and measure it with an Ecosystem Ratio, defined as unbooked gross transaction value divided by booked platform revenue. Because no Indonesian platform discloses a strictly country-labelled matched pair, every observation is admitted under a named evidence tier and tiers are never pooled. Seventeen platform-year levels across five issuer series spanning FY2019 to FY2025 show that the wedge moves, and disclosed revenue components explain the largest movements. Evidence from forty-eight matched issuer-years outside Indonesia indicates that the wedge is a general property of platform intermediation whose magnitude depends on business model. Official statistics and Indonesia's marketplace withholding rules then locate the activity and the records beyond platform accounts.")],h)

d.save(F); print("stage2a saved; paragraphs now:", len([1 for c in body.iterchildren() if c.tag.endswith('}p')]))
