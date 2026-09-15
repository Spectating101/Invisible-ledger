#!/usr/bin/env python3
"""Rebuild the proposal body on the 16 September freeze.

Keeps the title page, styles, Chapter 2 paragraphs, Figure 1 and the reference list of the FINAL
DOCX. Rewrites the abstract and Chapter 1 (research question kept verbatim) and Chapters 3-8 and
Appendix A following the frozen structure, with the claims stated plainly, the robustness numbers
restored and each interpretive boundary stated once (Section 7).

Usage: rebuild_proposal_2026-09-16.py [IN.docx] [OUT.docx]
Run scripts/finalize_proposal_format.py on OUT afterwards.
"""
import copy
import re
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt
from docx.table import Table
from docx.text.paragraph import Paragraph

SRC = sys.argv[1] if len(sys.argv) > 1 else "papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.docx"
OUT = sys.argv[2] if len(sys.argv) > 2 else SRC
doc = Document(SRC)
FONT = "Times New Roman"


def find(text):
    for p in doc.paragraphs:
        if p.text.strip() == text:
            return p
    raise RuntimeError("paragraph not found: " + text)


def clear_between(start_el, end_el):
    node = start_el.getnext()
    while node is not None and node is not end_el:
        nxt = node.getnext()
        node.getparent().remove(node)
        node = nxt


def font(run, size, bold=None, italic=None):
    run.font.name = FONT
    rpr = run._element.get_or_add_rPr()
    rpr.rFonts.set(qn("w:eastAsia"), FONT)
    run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic


def add_runs(p, text, size=12, bold=False, italic=False):
    # "_{it}" marks a subscript
    for i, part in enumerate(re.split(r"_\{(\w+)\}", text)):
        if not part:
            continue
        r = p.add_run(part)
        font(r, size, bold, italic)
        if i % 2:
            r.font.subscript = True


class Writer:
    def __init__(self, anchor_el):
        self.anchor = anchor_el

    after_table = False

    def _p(self):
        el = OxmlElement("w:p")
        self.anchor.addprevious(el)
        p = Paragraph(el, doc._body)
        if self.after_table:   # breathing room between a table and the prose below it
            p.paragraph_format.space_before = Pt(6)
            self.after_table = False
        return p

    def h1(self, text):
        p = self._p(); p.style = "Heading 1"; p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        add_runs(p, text, bold=True)

    def h2(self, text):
        p = self._p(); p.style = "Heading 2"; p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        add_runs(p, text, bold=True)

    def para(self, text, align=WD_ALIGN_PARAGRAPH.JUSTIFY, bold=False, italic=False):
        p = self._p(); p.style = "Normal"; p.alignment = align
        add_runs(p, text, bold=bold, italic=italic)
        return p

    def eq(self, text):
        p = self.para(text, WD_ALIGN_PARAGRAPH.CENTER, italic=True)
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True

    def caption(self, text, center=False):
        p = self._p(); p.style = "Normal"
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.LEFT
        add_runs(p, text, size=9.5, bold=True, italic=True)
        p.paragraph_format.keep_with_next = True

    def element(self, el):
        self.anchor.addprevious(el)

    def table(self, rows):
        ncols = len(rows[0])
        tbl = OxmlElement("w:tbl")
        tblPr = OxmlElement("w:tblPr")
        for tag, attrs in [("w:tblStyle", {"w:val": "TableGrid"}), ("w:tblW", {"w:type": "auto", "w:w": "0"}),
                           ("w:jc", {"w:val": "center"}), ("w:tblLayout", {"w:type": "fixed"})]:
            e = OxmlElement(tag)
            for k, v in attrs.items():
                e.set(qn(k), v)
            tblPr.append(e)
        tbl.append(tblPr)
        grid = OxmlElement("w:tblGrid")
        for _ in range(ncols):
            g = OxmlElement("w:gridCol"); g.set(qn("w:w"), str(9547 // ncols)); grid.append(g)
        tbl.append(grid)
        for ri, row in enumerate(rows):
            tr = OxmlElement("w:tr")
            trPr = OxmlElement("w:trPr")
            if ri == 0:
                h = OxmlElement("w:tblHeader"); h.set(qn("w:val"), "true"); trPr.append(h)
            trPr.append(OxmlElement("w:cantSplit"))
            tr.append(trPr)
            for text in row:
                tc = OxmlElement("w:tc")
                tcPr = OxmlElement("w:tcPr")
                va = OxmlElement("w:vAlign"); va.set(qn("w:val"), "center"); tcPr.append(va)
                tc.append(tcPr)
                pel = OxmlElement("w:p"); tc.append(pel)
                p = Paragraph(pel, None)
                add_runs(p, text, size=9, bold=(ri == 0))
                tr.append(tc)
            tbl.append(tr)
        self.anchor.addprevious(tbl)
        self.after_table = True
        return Table(tbl, doc._body)


# ---------------------------------------------------------------- figure and anchors
figure_el = copy.deepcopy(next(p._p for p in doc.paragraphs if p._p.xpath(".//w:drawing")))
abstract_h = find("Abstract")._p
ch2_h = find("2. Literature Review and Research Gap")._p
ch3_h = next(p._p for p in doc.paragraphs if p.text.strip().startswith("3. Theoretical Framework"))
refs_h = find("References")._p

# ---------------------------------------------------------------- abstract and Chapter 1
clear_between(abstract_h, ch2_h)
w = Writer(ch2_h)
w.para(
    "Digital economy is measured through records that do not describe the same thing. Platform revenue, "
    "e-commerce statistics and payment data are used as interchangeable measures of digital activity, yet each "
    "captures a different side of the boundary between the value a platform processes and the revenue it "
    "recognizes. I define the difference between transaction value and platform-recognized revenue as the "
    "invisible wedge and show that substituting one record for another misstates both the size of the digital "
    "economy and where it is growing. Indonesia, the largest digital market in Southeast Asia, is the empirical "
    "setting. In 2023, Tokopedia, Shopee and Grab processed US$43.23 billion of transaction value against "
    "US$3.16 billion of recognized revenue, a ratio of 13.7 to 1 and a wedge of US$40.07 billion that stays "
    "above US$20 billion when any one platform is excluded. Between 2020 and 2025, revenue grew faster than "
    "transaction value in ten of twelve year-to-year comparisons, so platform revenue understates the level of "
    "platform commerce and overstates its growth. National statistics place 98.5 percent of Indonesia's "
    "2023-2024 e-commerce growth outside the marketplace channel, and digital payment value grew up to eleven "
    "times as fast as e-commerce value. Evidence from eight platform businesses outside Indonesia shows the same "
    "boundary under other business models.")
w.h1("1. Introduction")
w.para(
    "Southeast Asia's digital economy grew from approximately US$100 billion in 2020 to US$263 billion in 2024 "
    "(Google, Temasek and Bain 2020, 2024). Digital platform scale, however, is not the same thing as platform "
    "revenue. Platforms record transactions, determine participant payouts, and book their own revenue, while "
    "national statistics and payment systems record other parts of the same economic activity. These measures "
    "are used interchangeably even though they do not measure the same thing. This paper argues that doing so "
    "produces systematically wrong conclusions about the scale and growth of platform economies.")
w.para(
    "Suppose a platform processes 100 units of transaction value but recognizes only 10 as revenue. The "
    "remaining 90 are still recorded within the platform's system but do not constitute platform revenue; they "
    "are merchant receipts, driver payouts, inventory costs, taxes, and other pass-through payments. An analyst "
    "using the platform's accounts sees 10, while one measuring the commerce it processes sees 100. I call the "
    "difference the invisible wedge.")
w.para(
    "Indonesia is the empirical setting. It is the largest digital market in Southeast Asia, and several records "
    "of the same activity can be compared there. Platform companies disclose transaction and revenue "
    "information; BPS-Statistics Indonesia, the national statistical agency, reports e-commerce activity; and "
    "Bank Indonesia, the country's central bank, reports digital payments. In 2023, the platform comparison "
    "covers Shopee and Tokopedia, which together represented about 70 percent of estimated Indonesian "
    "marketplace transaction value, together with Grab, a major intermediary in delivery and other digital "
    "services. The three platforms processed US$43.23 billion of transaction value against US$3.16 billion of "
    "recognized revenue, leaving a US$40.07 billion invisible wedge that stays above US$20 billion when any one "
    "of them is removed.")
w.para(
    "The difference also changes over time. Across twelve year-to-year comparisons between 2020 and 2025, "
    "revenue grew faster than transaction value in ten, and the median absolute gap between the two growth rates "
    "was 42 percentage points; in some years the two measures moved in opposite directions. Platform revenue "
    "therefore understates the level of platform-mediated commerce and, in most observed years, overstates its "
    "growth.")
w.para(
    "The same problem appears beyond company accounts. BPS reports that national e-commerce value grew 17.1 "
    "percent between 2023 and 2024, but about 98.5 percent of that increase occurred outside the marketplace "
    "component, and digital payment value reported by Bank Indonesia grew up to eleven times as fast as "
    "e-commerce value. Indonesia's Minister of Finance Regulation No. 37 of 2025, which introduces seller "
    "reporting and withholding through designated marketplaces, provides a further test of how platform-held "
    "transaction records enter administrative reporting.")
w.h2("1.1 Research question and objectives")
w.para("One question drives the proposal:")
w.para("How much economic activity remains invisible when digital platforms are measured through their reported "
       "revenue?", WD_ALIGN_PARAGRAPH.CENTER, bold=True)
w.para(
    "Indonesia provides the main empirical setting. Three objectives follow: first, to measure the invisible "
    "wedge across available platform histories from 2020 to 2025; second, to explain large movements using "
    "disclosed changes in monetization, customer incentives, revenue recognition, and reporting scope; and "
    "third, to compare the platform evidence with national e-commerce and payment records to determine whether "
    "they produce the same account of economic scale and growth.")
w.para(
    "A separate comparison of eight platform businesses outside Indonesia tests whether the same "
    "transaction-revenue separation appears under other business models.")
w.h2("1.2 Contributions")
w.para(
    "First, the study develops the invisible wedge from a one-year estimate into a measure that can be followed "
    "over time. From 2020 to 2025, revenue grows faster than transaction value in ten of twelve annual "
    "comparisons, showing that platform revenue is not a stable measure of either the level or the growth of "
    "platform-mediated commerce.")
w.para(
    "Second, I explain why the wedge moves using accounting components disclosed by the platforms themselves. "
    "Between 2022 and 2023, Tokopedia's transaction value fell 8.9 percent while net revenue from its "
    "third-party marketplace rose 53.2 percent. Lower customer incentives account for 60.6 percent of that "
    "increase in net revenue and higher gross revenue for the remainder.")
w.para(
    "Third, I extend the comparison beyond company accounts. National e-commerce statistics show that almost all "
    "of Indonesia's 2023-2024 growth occurred outside the marketplace component, while digital payment value "
    "grew up to eleven times as fast as e-commerce value. The records therefore produce different conclusions "
    "about the scale, growth, and location of digital activity.")
w.h2("1.3 Positioning the contribution")
w.para(
    "The contribution is a finance measurement problem before it is a tax-policy one. Platform accounts make the "
    "intermediation boundary observable, but that boundary affects the conclusions investors, researchers, "
    "statistical agencies, and policymakers draw about scale, growth, and monetization. De Franco, Kothari and "
    "Verdi (2011) show why comparable accounting bases matter, while Berg et al. (2020) show that "
    "intermediary-held digital traces contain information conventional records can miss. This paper applies "
    "those ideas to platform economies and shows that the measure chosen to describe digital activity changes "
    "the economic conclusion.")

# ---------------------------------------------------------------- Chapter 2 in-place edits
for p in doc.paragraphs:
    for old, new in [
        ("The OECD Model Rules and the European Union's DAC7 regime apply",
         "The OECD Model Rules (OECD 2020) and the European Union's DAC7 regime (European Union 2021) apply"),
        ("may still exist and become usable elsewhere.", "still exist and can become usable elsewhere."),
    ]:
        if old in p.text:
            for r in p.runs:
                if old in r.text:
                    r.text = r.text.replace(old, new)
                    break
            else:
                raise RuntimeError("run-split text in Chapter 2: " + old)

# Chapter 2 body paragraphs justified like the rest of the body
node = ch2_h.getnext()
while node is not None and node is not ch3_h:
    if node.tag == qn("w:p"):
        par = Paragraph(node, doc._body)
        if par.style.name == "Normal" and par.text.strip():
            par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    node = node.getnext()

# ---------------------------------------------------------------- Chapters 3-8 and Appendix A
start = ch3_h.getprevious()
clear_between(start, refs_h)
w = Writer(refs_h)
w.h1("3. Theoretical Framework and Hypotheses")
w.para(
    "Digital platform activity can be observed through several records, but those records do not measure the "
    "same economic object. The framework begins with the difference between the value a platform processes and "
    "the revenue it recognizes, then asks whether that relationship remains stable over time and whether other "
    "records produce the same account of digital activity.")
w.para(
    "For the platform analysis, transaction value and revenue are paired only when they refer to the same period "
    "and business activity. Broader-scope, reconstructed, national-statistical, and payment evidence is kept in "
    "separate analytical roles rather than combined into one sample.")
w.h2("3.1 Measurement Framework")
w.para(
    "Let V_{it} denote transaction value processed by platform i in year t, and R_{it} the revenue it "
    "recognizes over the same period and business scope. The absolute invisible wedge is:")
w.eq("W_{it} = V_{it} − R_{it}")
w.para(
    "W measures transaction value outside the platform's recognized revenue. It does not by itself imply "
    "participant profit, taxable income, value added, non-compliance, or tax due. Because platforms differ in "
    "size, I also express the wedge relative to revenue through the Ecosystem Ratio, which is constructed for "
    "this study:")
w.eq("E_{it} = (V_{it} − R_{it}) / R_{it}")
w.para(
    "An E of 9 means that for every one unit of platform revenue, nine additional units of transaction value lie "
    "outside the revenue line. A single ratio does not show whether transaction value and revenue move together "
    "through time, so I define annual growth divergence as:")
w.eq("D_{it} = g(V_{it}) − g(R_{it})")
w.para(
    "A positive D means transaction value grew faster than revenue; a negative D means revenue grew faster. "
    "Together, W, E, and D measure the size of the transaction-revenue boundary and how that boundary changes "
    "over time.")
w.h2("3.2 Hypotheses")
w.para(
    "The four hypotheses examine different layers of the same measurement problem. H1 tests the "
    "transaction-revenue boundary within platforms. H2 and H3 examine where activity and records outside "
    "platform revenue appear in national e-commerce evidence. H4 is the central claim of the thesis, and H1 to "
    "H3 establish the mechanisms behind it.")
w.para("H1. Platform revenue is not a stable proxy for the transaction value a platform processes.", WD_ALIGN_PARAGRAPH.LEFT, bold=True)
w.para(
    "If it were, transaction value and revenue would move proportionally within the same platform over time.")
w.para("H2. Aggregate e-commerce growth is driven mainly by growth in the number of participating businesses "
       "rather than by higher transaction value per business.", WD_ALIGN_PARAGRAPH.LEFT, bold=True)
w.para("This separates wider business participation from changes in the average value observed per business.")
w.para("H3. Marketplace participation is associated with stronger financial recordkeeping.", WD_ALIGN_PARAGRAPH.LEFT, bold=True)
w.para("This asks whether marketplace-mediated activity leaves a different recordkeeping pattern from other "
       "e-commerce activity.")
w.para("H4. Platform revenue, national e-commerce statistics and payment records are not interchangeable: "
       "substituting one for another changes the measured scale and growth of digital economic activity.",
       WD_ALIGN_PARAGRAPH.LEFT, bold=True)
w.para("This asks whether the records produce the same economic account when they observe different parts of "
       "digital activity.")
w.caption("Table 1. Hypotheses and principal empirical tests.")
w.table([
    ["Hypothesis", "Principal empirical test"],
    ["H1 - Transaction-revenue divergence",
     "Platform transaction value and revenue through time, the Ecosystem Ratio, and annual growth divergence"],
    ["H2 - Sources of e-commerce growth", "BPS national e-commerce value and business-count decomposition"],
    ["H3 - Marketplace participation and recordkeeping",
     "BPS published marketplace and financial-recordkeeping evidence"],
    ["H4 - Measurement choice", "Comparison of platform, national e-commerce, and payment records"],
])
w.para(
    "The comparison of platform businesses outside Indonesia is used as corroboration rather than as a fifth "
    "hypothesis. Indonesia's marketplace reporting regime is examined as an institutional application in "
    "Section 5.3.")

w.h1("4. Data and Methodology")
w.para(
    "The study uses several sources because no single record captures every part of digital platform activity. "
    "Platform reports provide transaction value and revenue; BPS-Statistics Indonesia provides national "
    "e-commerce and business evidence; Bank Indonesia provides payment statistics; and platform companies "
    "outside Indonesia provide a separate comparison. These sources answer different questions and are not "
    "combined into one dataset.")
w.h2("4.1 Selecting the Platform Evidence")
w.para(
    "The basic observation is one platform in one year, with transaction value and revenue referring to the same "
    "period and, as closely as possible, the same business activity. An observation is retained only when its "
    "period, geographic and business coverage, units, definitions, and source can be identified. Measures "
    "referring to different periods are excluded, while major changes in accounting definitions or business "
    "structure are recorded.")
w.caption("Table 2. Indonesian platform evidence.")
w.table([
    ["Type of evidence", "Platforms", "Annual observations", "Role"],
    ["Direct Indonesia-aligned data", "Tokopedia e-commerce", "2", "Main direct anchor"],
    ["Company-reported data with broader scope", "Blibli third-party business; Bukalapak Group", "9",
     "Evidence through time with stated scope limits"],
    ["Indonesia estimates requiring construction", "Grab; Shopee Indonesia", "6", "Supporting country evidence"],
])
w.para(
    "An annual observation is one matched transaction-and-revenue pair for one platform in one year. The 17 "
    "retained observations produce 12 year-to-year comparisons because the same platforms are not available in "
    "every year. Tokopedia is closely aligned with Indonesia but is not a literal country line. Blibli includes "
    "online travel, Bukalapak includes some overseas activity, and Grab and Shopee require additional "
    "construction. Tokopedia 2021 and Bukalapak 2024 are excluded because their transaction and revenue figures "
    "cover different periods.")
w.h2("4.2 Comparing Platform Activity Through Time")
w.para(
    "Changes through time are examined mainly by comparing each platform with itself. This keeps the company, "
    "business activity, and reporting convention as similar as the disclosures allow. When transaction value "
    "and revenue move sharply apart, disclosed changes in monetization, customer incentives, revenue "
    "recognition, and business scope are used to reconcile the movement where the filings permit.")
w.para(
    "Companies also use different names for transaction activity, including gross transaction value (GTV), "
    "gross merchandise value (GMV), and total payment volume (TPV). The original definitions are retained rather "
    "than assumed to be identical.")
w.para(
    "The cross-platform comparison uses the 2023 fiscal year, the last year in which the three principal "
    "platforms can be compared on the same basis. It measures the scale of the transaction-revenue difference "
    "for those platforms, and market-share estimates describe their coverage of marketplace transaction value.")
w.h2("4.3 Direct and Constructed Indonesia Measures")
w.para("Not every company reports the same Indonesia-specific information.")
w.caption("Table 3. Construction of the principal platform measures.")
w.table([
    ["Platform", "Directly available", "Constructed or external input", "Main limitation"],
    ["Tokopedia", "E-commerce transaction value and segment revenue", "None for matched pair",
     "Indonesia-aligned segment, not literal country line"],
    ["Grab", "Indonesia revenue; Group revenue and GTV", "Indonesia GTV derived from Group figures",
     "Assumes Group revenue-to-GTV relationship applies to Indonesia"],
    ["Shopee", "Group service monetization rate",
     "External Indonesia transaction estimate; Indonesia revenue derived", "Country measures are not independent disclosures"],
    ["Blibli / Bukalapak", "Reported transaction and revenue pairs", "None for retained pairs",
     "Scope extends beyond Indonesia alone"],
])
w.para("Grab reports Indonesian revenue directly but not Indonesian transaction value. Indonesian GTV is therefore "
       "estimated as:")
w.eq("Indonesia GTV = Indonesia revenue × Group GTV / Group revenue")
w.para(
    "Sea Limited does not report Shopee transaction value separately for Indonesia. Indonesian transaction value "
    "is taken from Momentum Works, and Indonesian revenue is estimated using Sea's Group service monetization "
    "rate:")
w.eq("Indonesia revenue = Indonesia transaction value × Group monetization rate")
w.para("Both constructions are labeled wherever they are used, and Section 5.1 reports how far the results move "
       "under alternative values of their inputs.")
w.h2("4.4 Evidence Beyond Platform Accounts")
w.caption("Table 4. Evidence modules and their role.")
w.table([
    ["Evidence source", "What is observed", "Role"],
    ["Indonesian platform histories", "Transaction value and revenue through time", "Measure the wedge and its movement"],
    ["BPS national e-commerce statistics", "National transaction value and estimated number of businesses",
     "Examine sources of aggregate growth"],
    ["BPS marketplace study", "Business-level marketplace and recordkeeping evidence",
     "Examine the association with financial recordkeeping"],
    ["Bank Indonesia", "Digital-payment measures", "Compare payment growth with e-commerce growth"],
    ["Platform companies outside Indonesia", "Matched transaction and revenue measures",
     "Test whether the same boundary appears elsewhere"],
])
w.para("For H2, national e-commerce value is expressed as:")
w.eq("V = N × A")
w.para(
    "where N is the estimated number of e-commerce businesses and A is implied nominal transaction value per "
    "business. Changes in total value are divided arithmetically between the business-count and "
    "value-per-business components. A conflicting published 2023 business count is retained as a sensitivity "
    "check.")
w.para(
    "For H3, BPS's published business-level evidence is used to examine the association between marketplace "
    "participation and financial recordkeeping, with province-level correlations as supporting diagnostics. For "
    "H4, Bank Indonesia payment measures are compared with e-commerce growth but are not added to platform or "
    "BPS transaction values.")
w.h2("4.5 External Evidence and Robustness")
w.para(
    "The external comparison contains 48 matched annual transaction-and-revenue observations from eight platform "
    "businesses covering 2017-2025. It tests whether the same transaction-revenue boundary appears under other "
    "business models and is kept separate from the Indonesian sample.")
w.para(
    "The robustness checks remove one platform at a time, vary every constructed input, replace ordinary growth "
    "rates with log changes, drop the most extreme year-to-year comparison, and restrict the evidence to pairs "
    "the companies report directly. Section 5 reports the resulting ranges.")

w.h1("5. Preliminary Evidence and Feasibility")
w.para(
    "The evidence assembled so far establishes that the proposed comparisons can be carried out and that the "
    "choice of record produces economically large differences. The preliminary results first show the scale and "
    "movement of the transaction-revenue boundary, then examine whether the wider Indonesian evidence tells the "
    "same story.")
w.h2("5.1 Platform Scale and Movement")
w.para("The 2023 fiscal year provides a common comparison across Grab, Tokopedia, and Shopee.")
w.caption("Table 5. Indonesia-focused 2023 platform comparison, US$ billions.")
w.table([
    ["Case", "Transaction value V", "Revenue R", "Wedge W", "Ecosystem Ratio E", "Evidence"],
    ["Grab Indonesia", "5.381", "0.605", "4.776", "7.895x", "Transaction value reconstructed"],
    ["Tokopedia", "16.331", "0.405", "15.926", "39.296x", "Direct matched pair"],
    ["Shopee Indonesia", "21.520", "2.152", "19.368", "9.000x", "Transaction value and revenue estimated"],
    ["Three platforms", "43.233", "3.162", "40.070", "12.671x", "Sum of three cases"],
])
w.para(
    "Across the three platforms, US$43.23 billion of transaction value corresponds to US$3.16 billion of "
    "recognized revenue, leaving a US$40.07 billion wedge; transaction value is 13.7 times recognized revenue. "
    "Tokopedia contributes 39.7 percent of the wedge, Shopee 48.3 percent and Grab 11.9 percent. Shopee's ratio "
    "of exactly 9.000 follows from applying Sea's Group monetization rate of 10.0 percent, so its revenue is an "
    "assumption. Varying that rate between 9 and 11 percent moves the combined wedge only between US$39.86 "
    "billion and US$40.29 billion, because Shopee's revenue is small relative to its transaction value. "
    "Excluding any one platform leaves a wedge between US$20.70 billion and US$35.29 billion, varying every "
    "constructed input one at a time keeps it between US$37.65 billion and US$42.49 billion, and Tokopedia "
    "alone, which requires no construction, carries a wedge of US$15.93 billion.")
w.para(
    "The relationship between the two measures is not stable. Across twelve year-to-year comparisons, revenue "
    "grows faster than transaction value in ten, and the median absolute gap between the two growth rates is "
    "42.02 percentage points. Restricting the evidence to pairs reported directly by Tokopedia, Blibli and "
    "Bukalapak gives nine comparisons, in which revenue grows faster in six and the median absolute gap is 42.94 "
    "points. On that restricted evidence the gap is 36.64 points in log changes and 29.34 points after removing "
    "the single largest comparison, stays between 29.34 and 52.52 points when any one comparison is left out, "
    "and every version that excludes one platform keeps at least one year in which the two measures move in "
    "opposite directions.")
w.para(
    "Tokopedia shows why the two measures separate. Between 2022 and 2023, its transaction value fell 8.9 percent "
    "while net revenue from its third-party marketplace rose 53.2 percent. Lower customer incentives account for "
    "60.6 percent of that increase and higher gross revenue for the remaining 39.4 percent, so the platform's "
    "revenue improved while the commerce it carried contracted.")
w.element(figure_el)
w.caption("Figure 1. Ecosystem Ratio through time for each platform, 2020-2025. Each line follows one platform's "
          "matched transaction value and revenue.", center=True)
w.h2("5.2 Evidence Beyond Platform Revenue")
w.para("National e-commerce and business evidence provides a different view of the same digital economy. Table 6 "
       "summarizes the preliminary evidence corresponding to H2-H4.")
w.caption("Table 6. Preliminary evidence beyond platform accounts.")
w.table([
    ["Question", "Preliminary evidence", "Interpretation"],
    ["Where does e-commerce growth come from?",
     "E-commerce value +17.08%; estimated business count +15.31%; implied nominal value per business +1.54%. "
     "The business count accounts for 90.29% of the increase (70.95% under the conflicting count)",
     "Growth comes mainly from more participating businesses (H2)"],
    ["Where does that growth occur?",
     "98.46% of the nominal increase occurs outside the marketplace component; marketplace share falls from "
     "18.2% to 15.8%",
     "Marketplace-based measurement misses almost all recent growth"],
    ["Are marketplace use and financial records related?",
     "Complete financial statements: 28.63% of marketplace users versus 12.25% of non-marketplace users",
     "Marketplace participation is associated with stronger financial recordkeeping (H3)"],
    ["Do other digital records show the same growth?",
     "BPS e-commerce +17.08%; electronic-money shopping +30.47%; mobile-banking payments and purchases +82.84%; "
     "QRIS +186.98%",
     "Payment measures grow 1.8 to 11 times as fast as e-commerce value (H4)"],
])
w.para(
    "The records do not agree. Between 2023 and 2024, marketplace value grew 1.45 percent, national e-commerce "
    "value grew 17.08 percent and payment measures grew between 30 and 187 percent, so the same year reads as "
    "stagnation or as rapid expansion depending on which record is used.")
w.h2("5.3 Feasibility and Institutional Application")
w.para(
    "The preliminary evidence is sufficient to motivate the full analysis. H1 is supported by the movement "
    "between transaction value and revenue within platforms, H2 and H3 by national and business-level BPS "
    "evidence, and H4 by the contrast between platform, e-commerce, and payment records.")
w.para(
    "Outside Indonesia, 48 matched company-years for eight platform businesses, including eBay, Etsy, Shopify, "
    "Mercado Libre and Sea, show the same boundary under other business models, with take rates among the "
    "marketplace businesses ranging from about 3 percent at Shopify to about 25 percent at Mercado Libre. Eleven "
    "of 40 year-to-year comparisons fail a clean-scope test because of acquisitions or perimeter changes, so the "
    "comparability problem the Indonesian design manages is a general feature of platform disclosure.")
w.para(
    "PMK 37/2025 applies the same distinction in policy. It requires designated marketplace operators to identify "
    "sellers, report transaction-linked turnover and withhold tax, with implementation scheduled for 1 November "
    "2026 after a postponement. Its reach is set by the channel it targets: the marketplace component carried "
    "15.8 percent of 2024 e-commerce value and 1.5 percent of 2023-2024 growth.")
w.para(
    "At this stage, the proposed measure can be constructed, followed through time, reconciled to disclosed "
    "accounting changes, and compared with independent records of Indonesian digital activity.")

w.h1("6. Why the Problem Matters")
w.para(
    "These records are designed to measure different things, and the error arises when one is used in place of "
    "another. Platform revenue measures what the platform recognizes as its own income, transaction value "
    "measures the commerce it processes, national e-commerce statistics describe the wider market, and payment "
    "systems record the movement of funds. An investor valuing platforms on revenue growth, a statistical agency "
    "sizing e-commerce from marketplace data and a policymaker reading payment growth as commerce growth are "
    "each working from a record that departs sharply from the activity they intend to measure, and each in a "
    "different direction.")
w.para(
    "Administrative use follows the same logic. Platform-held transaction records contain seller and transaction "
    "information that never appears in corporate revenue, and they become useful to government only when "
    "identity, reporting, transmission, and matching are in place. Indonesia's new reporting regime is built "
    "around the marketplace channel, so it inherits the coverage of that channel.")

w.h1("7. Limitations and Robustness")
w.caption("Table 7. Claims, evidence and robustness tests.")
w.table([
    ["Claim", "Evidence and robustness test"],
    ["Platform revenue understates platform commerce by more than an order of magnitude.",
     "2023 transaction value is 13.7 times revenue (wedge US$40.07bn). Holds across Shopee monetization of 9-11% "
     "(US$39.86-40.29bn), with any one platform excluded (at least US$20.70bn), under one-at-a-time input "
     "variation (US$37.65-42.49bn), and on Tokopedia alone (US$15.93bn)."],
    ["Platform revenue growth misstates commerce growth.",
     "Revenue outgrows transaction value in 10 of 12 year-to-year comparisons; median absolute gap 42.02 pp. "
     "Holds on directly reported pairs only (6 of 9; 42.94 pp), in log changes (36.64), without the largest "
     "comparison (29.34 pp), and with any one platform excluded."],
    ["Marketplace statistics miss where e-commerce grows.",
     "98.46% of 2023-2024 growth in e-commerce value falls outside the marketplace component. Holds on both the "
     "published amount and the rounded-share reconstruction (98.49%)."],
    ["Payment data overstate commerce growth.",
     "Electronic-money, mobile-banking and QRIS payment value grew 1.8 to 11 times as fast as e-commerce value, "
     "2023-2024."],
])
w.para(
    "The evidence is descriptive and the sample is small. The business-count decomposition is arithmetic, the "
    "recordkeeping result is an association, the Tokopedia reconciliation is an accounting identity rather than "
    "a causal estimate, and the ranges above are sensitivity ranges rather than statistical confidence "
    "intervals. Payment values are compared with e-commerce growth but are not treated as estimates of sales, "
    "and the compliance and revenue effects of PMK 37/2025 can be observed only after implementation.")
w.para(
    "Two sample decisions are put to the committee: whether Blibli and Bukalapak, whose reported figures extend "
    "beyond Indonesian goods marketplaces, enter the main longitudinal sample, and whether Grab and Shopee remain "
    "supporting evidence. The central results hold under either choice, because the growth result holds on "
    "directly reported pairs and the level result holds on Tokopedia alone.")

w.h1("8. Next Steps")
w.para(
    "The main data and empirical framework are already assembled. The remaining work is to settle the sample "
    "decisions, complete the robustness checks, verify source consistency, and develop the preliminary results "
    "into the full thesis analysis.")
w.caption("Table 8. Planned work toward the final thesis.")
w.table([
    ["Period", "Planned work"],
    ["Proposal stage", "Incorporate feedback from the proposal examination and finalize the empirical specification."],
    ["October-November 2026", "Complete remaining source checks and robustness analysis; finalize the main tables and figures."],
    ["Before the final defense", "Complete the full manuscript, integrate supporting evidence where it strengthens the "
     "argument, and conduct the final citation and consistency review."],
])
w.para(
    "The proposed study begins from a simple distinction between the value a platform processes and the revenue "
    "it recognizes. The preliminary evidence shows that this boundary is economically large, changes through "
    "time, and gives a different account of Indonesia's digital economy from national statistics and payment "
    "records. The final thesis measures how far those accounts diverge and which conclusions change when one "
    "record is used in place of another.")

w.h1("Appendix A - Data Sources by Evidence Type")
w.caption("Table A1. Source lineage by evidence type.")
w.table([
    ["Evidence type", "Platform or source", "Transaction-value source", "Revenue or comparison source"],
    ["Direct Indonesia-aligned", "Tokopedia e-commerce", "GoTo annual report, e-commerce segment metrics",
     "GoTo annual report, segment note"],
    ["Company-reported, broader scope", "Blibli third-party business",
     "Global Digital Niaga prospectus and results releases", "Same issuer filings"],
    ["Company-reported, broader scope", "Bukalapak Group", "Bukalapak annual and sustainability reports",
     "Same issuer filings"],
    ["Indonesia reconstruction", "Grab Indonesia", "Derived from Indonesia revenue and Group monetization rate",
     "Grab Form 20-F"],
    ["Indonesia reconstruction", "Shopee Indonesia", "Momentum Works Southeast Asia e-commerce estimate",
     "Derived from Sea Limited Form 20-F"],
    ["National statistics", "BPS-Statistics Indonesia", "E-Commerce Statistics 2023 and 2024; marketplace study",
     "Business-count and recordkeeping evidence"],
    ["Payment statistics", "Bank Indonesia", "Payment System Statistics and QRIS reports", "Growth-rate comparison only"],
    ["External corroboration", "Eight platform businesses", "Issuer transaction measures", "Issuer revenue measures"],
    ["Regulatory", "PMK 37/2025; DJP", "Ministry of Finance / Directorate General of Taxes",
     "Institutional architecture only"],
])
w.para("Every figure used in this proposal traces to a named file and locator in the accompanying data package.")

doc.save(OUT)
print("wrote", OUT)
