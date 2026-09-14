# -*- coding: utf-8 -*-
import sys, re, copy
sys.path.insert(0,'/tmp/build')
from surg_lib import *
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

B='/home/phyrexian/Downloads/llm_automation/project_portfolio/Solarpunk-bitcoin/'
SRC=B+'Invisible_Ledger_Sept0126_Kong.docx'
OUT=B+'Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx'

d=Document(SRC); body=d.element.body
accept_existing(body)           # Kong's edits become the baseline
kids=list(body.iterchildren())

def P(i): return kids[i]

# ---------------- 1. structural removals (authorised wholesale) ----------------
# front matter 0-125 -> replaced by proposal cover ; 176-283 (S4.3-S11) ; 335-end (appendices, rev notes)
def purge(a,b):
    for e in kids[a:b+1]:
        if e.tag.endswith('}sectPr'): continue
        par=e.getparent()
        if par is not None: par.remove(e)

# verified body anchors from the paragraph map
i_refs, i_appA = 284, 335
print("anchors: refs", i_refs, "appA", i_appA,
      "| refs text:", ' '.join(''.join(kids[i_refs].itertext()).split())[:40],
      "| appA text:", ' '.join(''.join(kids[i_appA].itertext()).split())[:40])
assert 'References' in ''.join(kids[i_refs].itertext())
assert 'Appendix A' in ''.join(kids[i_appA].itertext())

purge(i_appA, len(kids)-1)      # appendices + revision notes
purge(176, i_refs-1)            # S4.3 .. S11
purge(0, 125)                   # front matter

# ---------------- 2. sentence-level surgery in S1-S4.2 ----------------
S = {}

S[127]=[('del','Southeast Asia\u2019s digital economy grew from $98 billion in 2020 to $263 billion in 2024 (Google, Temasek and Bain 2024).'),
 ('ins','Southeast Asia\u2019s digital economy grew from $100 billion in gross merchandise value in 2020 to $263 billion in 2024 (Google, Temasek and Bain 2020, 2024).'),
 ('keep',' Digital platform scale, however, is not the same as tax-administrative visibility. These platforms record transactions, determine participant payouts, and book their own revenue, while the gross receipts earned by merchants, drivers, and other participants may remain outside routine third-party income reporting. I call this administrative information gap the \u201cinvisible wedge.\u201d The empirical question is whether this digitally recorded but separately reported flow is large enough to matter for tax administration.')]

S[128]=[('del','th e invisible wedge using an Indonesia-focused sample of Grab, GoTo , and Shopee, and then applies the resulting retained - share estimates to calibrate four additional markets within the Association of Southeast Asian Nations (ASEAN) : Vietnam, the Philippines, Thailand, and Malaysia.'),
 ('ins','This paper evaluates the invisible wedge using an Indonesia-focused longitudinal sample of listed platform companies whose filings report both gross transaction value and platform revenue for the same period and the same business scope.')]

S[129]=[('del','Grab, GoTo , and Shopee provide'),('ins','Listed Indonesian platform companies provide'),
 ('keep',' useful empirical settings because they directly intermediate transactions between consumers and merchants or service providers and publish financial disclosures from which transaction value s and platform revenue s can be observed or transparently derived. Their dual role as transaction intermediaries and record keeper s places them at the center of the paper’s third-party-reporting framework.')]

S[131]=[('ins','I measure the wedge with '),
 ('keep','an ecosystem ratio defined as the gross transaction value (GTV) not recognized as platform revenue divided by the revenue that the platform does recognize'),
 ('keep','. '),
 ('del','The baseline estimate is constructed based on the disclosures in fiscal-year of 2023 disclosures. Inputs for Grab and Shopee are either Indonesia-specific or transparently derived for Indonesia . By contrast, GoTo reports the required inputs directly only at the Group level, which includes operations outside Indonesia. Consequently, the estimated wedge of US$66.8 billion should be interpreted as an Indonesia-focused baseline estimate. The corresponding figures for Vietnam, the Philippines, Thailand, and Malaysia are scenario- based calibrations derived from this benchmark rather than independently measured estimates.'),
 ('ins','Because the relationship between transaction value and revenue also changes, each year-to-year transition is measured as the difference between transaction-value growth and revenue growth, and material divergences are reconciled against disclosed revenue components. For FY2023, the three leading Indonesian platform cases place transaction value not booked as platform revenue at approximately US$40.07 billion, equivalent to roughly 2.9 percent of Indonesia’s nominal gross domestic product in that year. That figure is a sum of three documented cases under mixed evidence classes rather than an Indonesia-wide total, and the longitudinal evidence then asks whether the gap is widening, narrowing, or reversing.')]

S[136]=[('del','This study makes four contributions. First, it constructs a 2023 Indonesia-focused platform estimate and uses the combined 5.88% take rate only as a transparent calibration for four additional ASEAN markets. Derived and Group-level inputs are explicitly identified by provenance.'),
 ('ins','This study makes four contributions. First, it measures the invisible wedge in Indonesia on a longitudinal basis. Earlier evidence for this market rests on a single fiscal year; the core sample assembled here observes transaction value and platform revenue for the same period and business scope across seventeen admitted platform-years spanning FY2019–FY2025, which makes it possible to report not only the scale of the wedge but its direction of travel.')]

S[140]=[('del','Table 1 states the '),('ins','Table 2 states the '),('del','paper'),('ins','proposal'),
 ('keep','’s inferential boundaries before the estimates are presented. '),
 ('del','Appendix A records the revision and provenance trail separately so that the main text can focus on the final design and results.')]

S[156]=[('del','To capture the invisible wedge in Indonesia, I propose and construct a proxy ….'),
 ('ins','To capture the invisible wedge in Indonesia, I propose and construct a proxy called the Ecosystem Ratio. The measure is my own construction for this paper rather than one adopted from a prior study. It rests on Sections 2.1 and 2.2: booked revenue need not track coordinated transaction value, and the share entering revenue is itself a reporting choice.')]

S[160]=[('keep','The ecosystem ratio describes the scale of participant-facing transaction value relative to the platform’s auditable revenue base. A higher ratio indicates a larger unbooked transaction flow relative to the platform’s own revenue'),
 ('ins',', and therefore a wider administrative information gap'),
 ('keep','; it does not by itself imply greater participant profit, taxable income, value-added, non-compliance, or tax due.')]

S[164]=[('del','I focus on Grab, GoTo , and Shopee (operated by Sea Limited) because they are large ASEAN-origin consumer platforms that directly intermediate transactions and provide public financial disclosures sufficient to observe or transparently derive transaction value and platform revenue.'),
 ('ins','Platform selection follows from what can actually be measured. The Ecosystem Ratio requires both sides of the transaction–revenue boundary for the same period and the same business scope.'),
 ('keep',' Public listing makes these platforms unusually observable relative to private competitors, which is essential for the company-level measurement used here.')]

S[168]=[('keep','Scope note. These platforms do not provide interchangeable measurements of one common business model. '),('del','Grab and GoTo are centered on on-demand services, while Shopee is centered on e-commerce'),('ins','Grab is centered on on-demand services, while Shopee, Tokopedia, Blibli, and Bukalapak are centered on e-commerce'),('keep','; their geographic coverage and revenue-recognition conventions also differ. '),
 ('del','For that reason, the 2023 base is described as Indonesia-focused, cross-platform ratio levels are interpreted cautiously, and the four non-Indonesian country figures are treated as calibrations rather than direct measurements.'),
 ('ins','For that reason cross-platform ratio levels are interpreted cautiously, and the supporting FY2023 cross-section is reported separately from the core longitudinal sample rather than pooled with it.')]

S[170]=[('keep','Platform revenue and transaction value are taken from primary company disclosures'),
 ('del',': Grab and Sea Limited Form 20-F filings and investor releases, and GoTo annual and quarterly reports. Momentum Works (2024) is used only where an Indonesia-specific market-share input is not separately disclosed. The core cross-platform sample is fiscal year 2023, and Table 2 identifies whether each input is directly reported, derived for Indonesia, or reported only at GoTo Group level.'),
 ('ins','. A platform-year enters the core sample only when both measures cover the same period; the geographic and business scope can be identified; units, currency, and definitions are known; derived inputs can be traced to source disclosures; and material structural breaks are flagged rather than treated as ordinary year-to-year change. Annual totals, quarterly figures, and repeated publication vintages of the same period are not counted as independent observations. All monetary values are reported in U.S. dollars, converted from Indonesian rupiah at period-average official rates, with the native-currency figure retained in the source file.')]

S[171]=[('keep','Take rate is defined as platform revenue divided by gross transaction value (GTV).'),('ins',' Table 3 sets out the three tiers, the series admitted to each, and the number of levels and within-series transitions each contributes.'),
 ('del',' The base estimate’s blended take rate is the same ratio computed across all three platform rows combined—total platform revenue divided by total GTV, 5.88%—and is used only for the four-country scenario calibration in Section 7. Because the GoTo row is Group-level, I refer to this as the Indonesia-focused blended take rate rather than a perfectly country-isolated Indonesia parameter.')]

S[173]=[('del','Table 2. Source, derivation, and geographic scope of each 2023 Indonesia-focused platform input'),
 ('ins','Table 3. Evidence tiers for Indonesian platform observations. No strictly country-labelled matched pair exists, so each observation is admitted under one tier and reported under that label; tiers are never pooled into a single monetary total. Tokopedia is a business segment rather than an explicit country line; Blibli 3P Retail also contains tiket.com travel and Bukalapak reports at Group level with overseas operations; Grab and Shopee each require one side to be derived from a Group monetization rate or an external market estimate.')]

S[175]=[('del','Only GoTo supplies both inputs independently, but its reported figures are Group-level. Grab and Shopee ratios inherit the take-rate assumptions used to derive one or both Indonesia-specific components.'),
 ('ins','Two candidate observations are excluded under these rules. Tokopedia FY2021 is excluded because its transaction and revenue measures cover different periods, and Bukalapak FY2024 is excluded because transaction value covers nine months while revenue covers twelve. Tokopedia’s e-commerce operations were deconsolidated following the TikTok Shop transaction in 2024, which is recorded as a structural break rather than as a change in the wedge.')]

S[141]=[('del','Table 1. Claims supported—and not supported—by the paper’s evidence'),
 ('ins','Table 2. Claims supported and not supported by the evidence assembled for this proposal.')]

for i,segs in S.items(): rebuild(P(i), segs)

# whole-paragraph tracked deletions
for i in (137,138,165,166,167,172):
    del_paragraph(P(i))

# heading renumbering (tracked)
H={126:('1. Introduction','1. Introduction'),
   135:('1.1 Contributions','1.2 Contributions'),
   139:('1.2 What this paper does and does not claim','1.3 What this proposal does and does not claim'),
   143:('2. Literature review and theoretical framework','2. Literature Review and Research Gap'),
   155:('3. Theoretical framework: the ecosystem ratio','3. Theoretical Framework: the Ecosystem Ratio'),
   162:('4. Data, methodology, and provenance','4. Data and Methodology'),
   163:('4.1 Institutional background: Grab, GoTo , and Shopee','4.1 Empirical setting and platform selection'),
   169:('4.2 Sample construction','4.2 Admission rules and evidence tiers'),
   146:('2.2 Informality, platform work, and measurement','2.3 Informality, platform work, and measurement'),
   149:('2.3 Third-party reporting as tax capacity','2.4 Third-party reporting as tax capacity'),
   153:('2.4 Digital taxation and platform-reporting rules','2.5 Digital taxation and platform-reporting rules'),
  }
for i,(old,new) in H.items():
    if old==new: continue
    rebuild(P(i),[('del',old),('ins',new)])

d.save(OUT); print("stage1 saved", OUT)
