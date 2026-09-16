#!/usr/bin/env python3
"""Whole-paper restructure of the proposal (16 September).

Rebuilds the abstract and every chapter from the approved DOCX (title page, styles, figure
paragraph, reference list) following the whole-paper read: the substitution is shown on page 2
with four records of 2023, the sample and scope are named in Chapter 1, the headline rests on the
issuer-reported main sample, constructed series are identified as group ratios, and the tax thread
is reduced to a rule built on one record.

Usage: restructure_proposal_2026-09-16.py APPROVED.docx OUT.docx FIGURE.png
Then run scripts/finalize_proposal_format.py OUT.docx
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

SRC, OUT = sys.argv[1], sys.argv[2]
doc = Document(SRC)
FONT = "Times New Roman"
J, L, C = WD_ALIGN_PARAGRAPH.JUSTIFY, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER


FOOTNOTES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:footnotes xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:footnote w:type="separator" w:id="-1"><w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr><w:r><w:separator/></w:r></w:p></w:footnote>
<w:footnote w:type="continuationSeparator" w:id="0"><w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr><w:r><w:continuationSeparator/></w:r></w:p></w:footnote>
%s</w:footnotes>"""

FOOTNOTE_BODY = """<w:footnote w:id="%d"><w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="both"/></w:pPr>
<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman"/><w:vertAlign w:val="superscript"/><w:sz w:val="20"/></w:rPr><w:footnoteRef/></w:r>
<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman"/><w:sz w:val="20"/></w:rPr><w:t xml:space="preserve"> %s</w:t></w:r></w:p></w:footnote>"""


def add_footnotes(document, texts):
    """Attach a real footnotes part; python-docx has no API for it."""
    from docx.opc.constants import CONTENT_TYPE as CT, RELATIONSHIP_TYPE as RT
    from docx.opc.packuri import PackURI
    from docx.opc.part import Part
    body = "\n".join(FOOTNOTE_BODY % (i + 2, t) for i, t in enumerate(texts))
    part = Part(PackURI("/word/footnotes.xml"), CT.WML_FOOTNOTES,
                (FOOTNOTES_XML % body).encode("utf-8"), document.part.package)
    document.part.relate_to(part, RT.FOOTNOTES)


def footnote_ref(paragraph, note_id):
    r = paragraph.add_run()
    font(r, 12)
    r._element.get_or_add_rPr().append(OxmlElement("w:vertAlign"))
    r._element.rPr.find(qn("w:vertAlign")).set(qn("w:val"), "superscript")
    ref = OxmlElement("w:footnoteReference")
    ref.set(qn("w:id"), str(note_id))
    r._element.append(ref)


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
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), FONT)
    run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic


def add_runs(p, text, size=12, bold=False, italic=False):
    for i, part in enumerate(re.split(r"_\{(\w+)\}", text)):   # "_{it}" marks a subscript
        if part:
            r = p.add_run(part)
            font(r, size, bold, italic)
            if i % 2:
                r.font.subscript = True


def replace_in(p, old, new):
    if old not in p.text:
        raise RuntimeError("text not found: " + old)
    for r in p.runs:
        if old in r.text:
            r.text = r.text.replace(old, new)
            return
    raise RuntimeError("text split across runs: " + old)


class Writer:
    after_table = False

    def __init__(self, anchor_el):
        self.anchor = anchor_el

    def _p(self):
        el = OxmlElement("w:p")
        self.anchor.addprevious(el)
        p = Paragraph(el, doc._body)
        if self.after_table:
            p.paragraph_format.space_before = Pt(6)
            self.after_table = False
        return p

    def h1(self, text):
        p = self._p(); p.style = "Heading 1"; p.alignment = L; add_runs(p, text, bold=True)

    def h2(self, text):
        p = self._p(); p.style = "Heading 2"; p.alignment = L; add_runs(p, text, bold=True)

    def para(self, text, align=J, bold=False, italic=False):
        p = self._p(); p.style = "Normal"; p.alignment = align
        add_runs(p, text, bold=bold, italic=italic)
        return p

    def hyp(self, text):
        p = self.para(text, L, bold=True)
        p.paragraph_format.keep_with_next = True

    def eq(self, text):
        p = self.para(text, C, italic=True)
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True

    def caption(self, text, center=False):
        p = self._p(); p.style = "Normal"; p.alignment = C if center else L
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
                add_runs(Paragraph(pel, None), text, size=9, bold=(ri == 0))
                tr.append(tc)
            tbl.append(tr)
        self.anchor.addprevious(tbl)
        self.after_table = True
        return Table(tbl, doc._body)



# ------------------------------------------------------------------ figure, anchors, clear body
FIG_PNG = sys.argv[3] if len(sys.argv) > 3 else "papers/current/figures/figure1_ecosystem_ratio_timeseries.png"
figure_el = copy.deepcopy(next(p._p for p in doc.paragraphs if p._p.xpath(".//w:drawing")))
rid = figure_el.xpath(".//a:blip/@r:embed")[0]
doc.part.related_parts[rid]._blob = open(FIG_PNG, "rb").read()   # regenerated Figure 1
abstract_h = find("Abstract")._p
refs_h = find("References")._p
clear_between(abstract_h, refs_h)
w = Writer(refs_h)

# ------------------------------------------------------------------ abstract
w.para(
    "Digital economy is measured through several records: the transaction value platforms process, the revenue "
    "they recognize, national e-commerce statistics and payment data. These records are often used "
    "interchangeably, yet each captures a different part of the same activity. This study asks how much economic "
    "activity remains invisible when digital platforms are measured through their reported revenue. I define the "
    "invisible wedge as the difference between transaction value and platform-recognized revenue and follow it "
    "across Indonesian platforms from 2020 to 2025. In 2023, Tokopedia, Shopee and Grab processed US$43.23 billion "
    "of transaction value against US$3.16 billion of recognized revenue. The relationship is not stable: among the "
    "platforms that report both figures themselves, revenue grew faster than transaction value in six of eight "
    "year-to-year comparisons and moved against it in two. National statistics and payment records disagree with "
    "the platform picture and with each other. BPS-Statistics Indonesia reports a marketplace channel smaller than "
    "two platforms' own transaction value and places 98.5 percent of 2023–2024 e-commerce growth outside it, while "
    "payment measures grew up to eleven times as fast. Eight platform businesses outside Indonesia show the same "
    "boundary with smaller year-to-year divergence. The proposal compares these records rather than treating any "
    "one of them as the measure of digital activity.")

# ------------------------------------------------------------------ Chapter 1
w.h1("1. Introduction")
w.para(
    "Southeast Asia's digital economy grew from approximately US$100 billion in 2020 to US$263 billion in 2024 "
    "(Google, Temasek and Bain 2020, 2024). That figure is one record of the activity: the gross value of the "
    "transactions involved. The platforms that carry those transactions report a different number, their own "
    "revenue; national statistical agencies report a third, the online sales of surveyed businesses; and payment "
    "systems report a fourth, the value of funds moved. Each is correct for what it measures. These measures are "
    "often used interchangeably even though they do not measure the same thing, and this paper argues that doing "
    "so produces systematically wrong conclusions about the scale and growth of platform economies.")
w.para(
    "Suppose a platform processes 100 units of transaction value but recognizes only 10 as revenue. The remaining "
    "90 are still recorded within the platform's system but do not constitute platform revenue; they represent "
    "merchant receipts, driver payouts, inventory costs, taxes, and other pass-through payments. An analyst using "
    "the platform's accounts sees 10, while one measuring the commerce it processes sees 100. I call the difference "
    "the invisible wedge. Neither number is wrong. Revenue records what the platform earned and transaction value "
    "records what it carried; questions about the size and growth of the digital economy concern what was carried, "
    "while the figure a listed platform must report in its financial statements is what it earned.")
w.para(
    "Indonesia, the largest digital market in Southeast Asia, shows how far apart these records are. The study "
    "covers the five Indonesian platforms that publish usable transaction and revenue figures: the marketplaces "
    "Tokopedia, Shopee, Blibli and Bukalapak, and Grab, whose Indonesian business is mainly delivery and other "
    "on-demand services. In 2023, Tokopedia, Shopee and Grab together processed US$43.23 billion of transaction "
    "value against US$3.16 billion of recognized revenue, a wedge of US$40.07 billion. BPS-Statistics Indonesia, the "
    "national statistical agency, placed the marketplace component of e-commerce at about US$13.2 billion and all "
    "e-commerce at US$72.3 billion. These figures cover different scopes and definitions, and that is the point: "
    "each answers a different question, and anyone quoting "
    "one of them as the size of the digital economy has chosen a record.")
w.para(
    "The records also disagree about growth. Between 2022 and 2023, Tokopedia's revenue rose 53.2 percent while the "
    "transaction value it processed fell 8.9 percent: read through its accounts the platform was expanding quickly, "
    "read through its transactions it was shrinking. The reversal is not isolated. Among the three platforms that "
    "report both figures themselves, revenue grew faster than transaction value in six of eight year-to-year "
    "comparisons between 2020 and 2025, and the two moved in opposite directions twice. Nationally, BPS reports "
    "e-commerce value up 17.1 percent between 2023 and 2024, with 98.5 percent of the increase outside the "
    "marketplace channel that platform accounts describe, while payment measures from Bank Indonesia, the central "
    "bank, grew between 1.8 and 11 times as fast.")
w.para(
    "A statement about how large Indonesia's digital economy is, or how fast it grew, is therefore a statement about "
    "a record. An investor reading platform revenue and an analyst sizing e-commerce from marketplace figures will "
    "reach different conclusions about the same years, and each will have read the record correctly.")
w.h2("1.1 Research question and objectives")
w.para("One question drives the proposal:")
w.para("How much economic activity remains invisible when digital platforms are measured through their reported "
       "revenue?", C, bold=True)
w.para(
    "Indonesia provides the main empirical setting. Three objectives follow: first, to measure the invisible wedge "
    "across the platform histories available from 2020 to 2025; second, to explain large movements using disclosed "
    "changes in monetization, customer incentives, revenue recognition, and reporting scope; and third, to compare "
    "the platform evidence with national e-commerce and payment records, to determine whether they give the same "
    "account of economic scale and growth and what their disagreement implies for measures built on a single record.")
w.para(
    "A separate comparison of eight listed platform businesses outside Indonesia, including eBay, Etsy, Shopify and "
    "Mercado Libre, tests whether the same separation between transaction value and revenue appears under other "
    "business models.")
w.h2("1.2 Contributions")
w.para(
    "First, the study turns the invisible wedge from a one-year estimate into a measure followed over time, and "
    "shows that revenue is not a stable guide to the commerce behind it: among the issuer-reported platforms, "
    "revenue outgrew transaction value in six of eight comparisons and moved against it twice.")
w.para(
    "Second, I explain why the wedge moves using accounting components the platforms disclose. Of the increase in "
    "Tokopedia's net revenue between 2022 and 2023, 60.6 percent reconciles to lower customer incentives and 39.4 "
    "percent to higher gross revenue, in a year when its transaction value fell.")
w.para(
    "Third, I extend the comparison beyond company accounts and show that national statistics and payment records "
    "disagree with the platform picture, and with each other, about both the level and the growth of Indonesian "
    "digital commerce.")
w.para(
    "Fourth, the study separates the figures issuers report from those that must be constructed, and shows that the "
    "longitudinal result rests on the reported figures alone.")
w.h2("1.3 Positioning the contribution")
w.para(
    "The contribution is a finance measurement problem before it is a tax-policy one. Platform accounts make the "
    "intermediation boundary observable, but that boundary affects the conclusions investors, researchers, "
    "statistical agencies, and policymakers draw about scale, growth, and monetization. De Franco, Kothari and Verdi "
    "(2011) show why comparable accounting bases matter, while Berg et al. (2020) show that intermediary-held digital "
    "traces contain information conventional records can miss. This paper applies those ideas to platform economies "
    "and shows that the record chosen to describe digital activity changes the economic conclusion.")

# ------------------------------------------------------------------ Chapter 2
w.h1("2. Literature Review and Research Gap")
w.para(
    "Digital platforms sit between economic activity and the records used to measure it. They facilitate "
    "transactions between buyers and sellers, recognize only part of that activity as their own revenue, and "
    "generate records that can also appear in payment, statistical, and administrative systems. Existing research "
    "explains each part of this process from a different angle. Taken together, it provides the foundation for "
    "asking how much activity remains invisible when platforms are measured through reported revenue.")
w.h2("2.1 Platform Economics and Revenue Recognition")
w.para(
    "Platform economics explains why the value of commerce processed through a platform can be much larger than the "
    "revenue the platform records. Digital platforms often connect consumers with merchants or other service "
    "providers and earn commissions, fees, advertising, logistics, or other intermediation revenue rather than the "
    "full value of every transaction they facilitate (Rochet and Tirole 2003; Caillaud and Jullien 2003; Parker and "
    "Van Alstyne 2005; Armstrong 2006; Hagiu and Wright 2015; Evans and Schmalensee 2016).")
w.para(
    "Accounting can widen or narrow this difference. Under IFRS 15, whether a company acts as a principal or an agent "
    "affects whether it recognizes the full customer payment or only the amount it earns from arranging the "
    "transaction (International Accounting Standards Board 2014). Customer incentives, monetization, service mix, "
    "acquisitions, and changes in business scope can also move reported revenue without an equivalent change in "
    "transaction activity. De Franco, Kothari and Verdi (2011) show why comparable accounting bases matter when "
    "financial information is interpreted. The literature therefore explains why a transaction–revenue gap can exist "
    "and move over time, but not how economically large that gap becomes in practice.")
w.h2("2.2 Measuring the Digital Economy")
w.para(
    "Official measurement frameworks already distinguish between the commerce facilitated through a platform and "
    "the service provided by the platform itself. National-accounting guidance separates the buyer-seller "
    "transaction from the platform's intermediation service rather than treating the full transaction value as "
    "platform output (Ahmad and Schreyer 2016; International Monetary Fund 2018; OECD 2023; United Nations et al. "
    "2025).")
w.para(
    "In practice, the quantities are published by different producers. Industry reports size the regional digital "
    "economy by gross merchandise value (Google, Temasek and Bain 2024), national statistics measure the online sales "
    "of surveyed businesses (BPS-Statistics Indonesia 2025), and listed platforms report the revenue they recognize "
    "under IFRS 15 (International Accounting Standards Board 2014). A difference that is harmless when the measures "
    "move together becomes important when they do not, because the choice of measure can change conclusions about "
    "economic scale and growth. This thesis therefore compares the records rather than assuming that one can "
    "substitute for another.")
w.h2("2.3 Digital Records and Third-Party Information")
w.para(
    "Activity outside platform revenue is still recorded. Merchants and service providers can be small, "
    "self-employed, or weakly represented in conventional financial records while their transactions leave detailed "
    "records inside a digital platform. This differs from the usual shadow-economy problem, where part of the "
    "difficulty is that economic activity leaves few reliable formal records (La Porta and Shleifer 2014; Ulyssea "
    "2018; Medina and Schneider 2019). Digital records can contain useful economic information that conventional "
    "records miss (Berg et al. 2020), and platform-mediated activity can create additional financial and "
    "administrative traces (Barrios, Hochberg and Yi 2022; Denes, Lagaras and Tsoutsoura 2025).")
w.para(
    "These records also matter once they become available to government. Public-finance research shows that "
    "compliance and enforcement change when information about income or transactions is independently reported by "
    "third parties (Kleven et al. 2011; Pomeranz 2015; Naritomi 2019; Kleven, Kreiner and Saez 2016; Slemrod 2019). "
    "The OECD Model Rules (OECD 2020) and the European Union's DAC7 regime (European Union 2021) apply this principle "
    "to digital platforms, and Indonesia's Minister of Finance Regulation No. 37 of 2025 (PMK 37/2025) follows the "
    "same logic through seller identification, transaction-linked "
    "reporting, and marketplace withholding. The relevance here is informational: records outside platform revenue "
    "exist, and what they can show depends on which of them a measure or a rule draws on.")
w.h2("2.4 Research Gap")
w.para(
    "Existing research explains the pieces of the problem separately. Platform economics explains why transaction "
    "value can exceed revenue; accounting explains why the gap can move; official measurement frameworks explain why "
    "these quantities should not be treated as equivalent; and research on digital records explains why activity "
    "outside revenue is still observable.")
w.para(
    "What remains less clear is how large these differences become in practice, whether they persist over time, and "
    "whether choosing one record instead of another changes the economic conclusion. This thesis addresses that gap "
    "by measuring the invisible wedge over time, examining disclosed reasons for major movements, comparing platform "
    "accounts with national e-commerce and payment records, and using external platform evidence to test whether "
    "the same pattern appears beyond Indonesia.")

# ------------------------------------------------------------------ Chapter 3
w.h1("3. Theoretical Framework and Hypotheses")
w.para(
    "Digital platform activity can be observed through several records, but those records do not measure the same "
    "economic object. The framework begins with the difference between the value a platform processes and the "
    "revenue it recognizes, then asks whether that relationship remains stable over time and whether other records "
    "produce the same account of digital activity.")
w.para(
    "For the platform analysis, transaction value and revenue are paired only when they refer to the same period and "
    "business activity. Figures that issuers report and figures that must be constructed are kept apart, as are "
    "national statistics and payment records (Section 4).")
w.h2("3.1 Measurement Framework")
w.para("Let V_{it} denote transaction value processed by platform i in period t, and R_{it} the revenue recognized "
       "over the same matched period and business scope. The absolute invisible wedge is:")
w.eq("W_{it} = V_{it} − R_{it}")
w.para("W is transaction value outside the platform's recognized revenue, not an omission from its accounts: both "
       "inputs can appear in the same company report. It is not merchant profit, worker income, taxable income, unpaid "
       "tax, tax evasion, or value added. Because platforms differ in size, I also express the "
       "wedge relative to revenue. The Ecosystem Ratio is:")
w.eq("E_{it} = (V_{it} − R_{it}) / R_{it}")
w.para(
    "An E of 9 means that for every one unit of platform revenue, nine units of transaction value lie outside the "
    "revenue line. Seen from the other side, E is the platform's monetization rate, t = R/V, inverted: E = 1/t − 1, so "
    "a platform keeping 2.5 percent of transaction value has an E of 39. It is reported this way because the question "
    "concerns the commerce outside revenue rather than the share the platform captures.")
w.para(
    "The Ecosystem Ratio is constructed for this study as a descriptive transformation of the monetization rate, not "
    "a new underlying quantity or a measure adopted from prior work. Its basis is the "
    "platform-economics result that booked revenue need not track the transaction value a multisided platform "
    "coordinates (Rochet and Tirole 2003; Hagiu and Wright 2015; Evans and Schmalensee 2016), together with the "
    "accounting result that the share of transaction value entering revenue is itself a reporting choice "
    "(International Accounting Standards Board 2014; De Franco, Kothari and Verdi 2011).")
w.para("A single ratio does not show whether the relationship holds through time, so I define annual growth "
       "divergence as:")
w.eq("D_{it} = g(R_{it}) − g(V_{it})")
w.para(
    "A positive D means revenue grew faster than transaction value, so the platform captured a larger share and E "
    "fell; a negative D means the reverse. If revenue were a stable proxy for transaction value, D would stay close "
    "to zero. Together, W, E, and D describe the size of the wedge and how it changes over time.")
w.h2("3.2 Hypotheses")
w.para(
    "The four hypotheses test the research question one record at a time. H1 concerns transaction value and revenue "
    "within platforms, H2 and H3 the national e-commerce evidence, and H4 the comparison across records. None is "
    "interpreted as a causal claim. Table 1 pairs each hypothesis with the evidence that tests it.")
w.hyp("H1. Within the same platform, transaction value and platform revenue do not grow in proportion.")
w.para("If they did, D would stay close to zero and E would be constant. The test is whether D departs from zero and "
       "changes sign.")
w.hyp("H2. National e-commerce growth comes mainly from more participating businesses rather than from higher "
      "sales per business.")
w.para("Growth driven by new sellers can take place in channels that platform accounts do not cover. The split is "
       "arithmetic and does not assign new businesses to particular channels.")
w.hyp("H3. Marketplace participation is associated with stronger financial recordkeeping.")
w.para("Recordkeeping determines whether activity outside platform accounts leaves a record that statistics can "
       "observe. The relationship is tested as an association.")
w.hyp("H4. The measured growth of Indonesian digital commerce depends on the record used, both within platforms "
      "and in national statistics.")
w.para("H4 is the central claim of the thesis. It fails if revenue grows in step with transaction value within "
       "platforms and the marketplace channel grows in step with all e-commerce. Level differences between platform "
       "and BPS figures, and payment growth, are reported as context because their definitions and coverage differ.")
w.caption("Table 1. Hypotheses and principal empirical tests.")
w.table([
    ["Hypothesis", "Principal empirical test"],
    ["H1 - Transaction-revenue divergence",
     "Growth divergence D and the Ecosystem Ratio for the platforms that report both figures"],
    ["H2 - Sources of e-commerce growth", "BPS national e-commerce value split into business count and sales per business"],
    ["H3 - Marketplace participation and recordkeeping", "BPS published comparison of marketplace and non-marketplace sellers"],
    ["H4 - Measurement choice", "Growth of revenue against transaction value within platforms, and of the marketplace "
     "channel against all e-commerce in BPS"],
])
w.para("The comparison of platform businesses outside Indonesia corroborates H1 rather than forming a fifth "
       "hypothesis.")

# ------------------------------------------------------------------ Chapter 4
w.h1("4. Data and Methodology")
w.para(
    "The study uses several records because no single one captures every part of digital platform activity. "
    "Platform reports provide transaction value and revenue; BPS-Statistics Indonesia provides national e-commerce "
    "and business evidence; Bank Indonesia provides payment statistics; and platform companies outside Indonesia "
    "provide a separate comparison. The records answer different questions and are not combined into one dataset.")
w.h2("4.1 Selecting the Platform Evidence")
w.para(
    "The basic observation is one platform in one year, with transaction value and revenue referring to the same "
    "period and, as closely as possible, the same business activity. An observation is retained only when its "
    "period, geographic and business coverage, units, definitions, and source can be identified; measures referring "
    "to different periods are excluded, and major changes in accounting definitions or business structure are "
    "recorded.")
w.para(
    "The sample consists of the Indonesian platforms that publish both transaction value and revenue. Lazada and "
    "TikTok Shop, both large in Indonesia, are outside it because no matched Indonesian revenue series has been "
    "located for either. The window runs from the first matched pair, Bukalapak in 2020, to the latest, Blibli in "
    "2025. It is a sample of disclosing cases rather than a representative sample of Indonesian platforms.")
w.caption("Table 2. Indonesian platform evidence.")
w.table([
    ["Type of evidence", "Platforms", "Annual observations", "Role"],
    ["Issuer-reported, Indonesia-aligned", "Tokopedia e-commerce", "2", "Main sample: cleanest scope, shortest window"],
    ["Issuer-reported, broader scope", "Blibli third-party business; Bukalapak Group", "9",
     "Main sample: most of the time series"],
    ["Requires construction", "Grab; Shopee Indonesia", "6", "Supporting: 2023 scale comparison"],
])
w.para(
    "Table 2 separates the pairs issuers report themselves from the country figures that must be constructed. The "
    "main sample is the first group: 11 platform-years yielding 8 year-to-year comparisons. Adding Grab and Shopee "
    "gives 17 platform-years and 12 comparisons. A 2020 Blibli pair from its prospectus is used only in a separate "
    "sensitivity.")
w.para(
    "Each series covers the years in which a matched pair exists. Tokopedia is an Indonesia-aligned segment rather "
    "than a literal country line and enters only for 2022 and 2023: the 2021 pair covers mismatched periods, and the "
    "Tokopedia and TikTok Shop businesses were combined under PT Tokopedia on 31 January 2024, after which the listed "
    "parent reports a contractual fee rather than platform revenue. Blibli's reported pairs run from 2021 to 2025, "
    "and its third-party segment includes online travel. Bukalapak reports at Group level, including some overseas "
    "activity, from 2020 to 2023; its 2024 pair is excluded because transaction value covers nine months and revenue "
    "twelve. Grab is observed from 2021 to 2023, after which it reports transaction value on a different basis, and "
    "Shopee from 2022 to 2024.")
w.h2("4.2 Comparing Platform Activity Through Time")
w.para(
    "Changes through time are examined mainly by comparing each platform with itself. This keeps the company, "
    "business activity, and reporting convention as similar as the disclosures allow. When transaction value and "
    "revenue move sharply apart, disclosed changes in monetization, customer incentives, revenue recognition, and "
    "business scope are used to reconcile the movement where the filings permit; these reconciliations are "
    "arithmetic rather than causal.")
gtv = w.para(
    "Companies use different names for transaction activity, including gross transaction value (GTV), gross "
    "merchandise value (GMV), and total payment volume (TPV). Transaction value, V, is the umbrella concept in this "
    "proposal and GTV is the label used for it, while each issuer's own label and definition are retained and "
    "checked rather than assumed to be identical.")
footnote_ref(gtv, 2)
w.para(
    "Growth rates are computed in each issuer's reporting currency, so exchange-rate movements do not enter D. US "
    "dollar values are used only for the 2023 cross-section, where rupiah figures are converted at the World Bank's "
    "2023 official exchange rate of 15,236.88 rupiah per dollar (World Bank n.d.).")
w.h2("4.3 Direct and Constructed Indonesia Measures")
w.para("Not every company reports the same Indonesia-specific information. Table 3 sets out, for each platform, what "
       "is disclosed directly, what has to be constructed, and the limitation that follows.")
w.caption("Table 3. Construction of the principal platform measures.")
w.table([
    ["Platform", "Directly available", "Constructed or external input", "Main limitation"],
    ["Tokopedia", "E-commerce transaction value and segment revenue", "None for matched pair",
     "Indonesia-aligned segment, not literal country line"],
    ["Grab", "Indonesia revenue; Group revenue and GTV", "Indonesia GTV derived from Group figures",
     "Indonesian ratio equals the Group ratio"],
    ["Shopee", "Group service monetization rate", "External Indonesia transaction estimate; Indonesia revenue derived",
     "Indonesian ratio set by the Group rate"],
    ["Blibli / Bukalapak", "Reported transaction and revenue pairs", "None for retained pairs",
     "Scope extends beyond Indonesian goods commerce"],
])
w.para("Grab reports Indonesian revenue directly but not Indonesian transaction value. Indonesian GTV is therefore "
       "estimated as:")
w.eq("Indonesia GTV = Indonesia revenue × Group GTV / Group revenue")
w.para("The Group monetization rate is platform revenue divided by gross transaction value.")
w.para(
    "Sea Limited does not report Shopee transaction value separately for Indonesia. Indonesian transaction value is "
    "taken from Momentum Works, a Singapore-based industry research firm whose annual Southeast Asian e-commerce "
    "report is widely cited for country-level platform transaction estimates. It is used because no issuer discloses "
    "Shopee's Indonesian transaction value, it is labeled as a third-party estimate wherever it appears, and "
    "Indonesian revenue is then estimated using Sea's Group service monetization rate:")
w.eq("Indonesia revenue = Indonesia transaction value × Group monetization rate")
w.para(
    "In both cases the Indonesian ratio is fixed by construction: Grab's Indonesian E equals its Group E, and "
    "Shopee's is the inverse of Sea's monetization rate less one. The two series therefore contribute Indonesian "
    "levels, through Grab's reported revenue and the external Shopee estimate, but no independent Indonesian "
    "evidence on the ratio or its movement, which is why they are outside the main sample.")
w.h2("4.4 Evidence Beyond Platform Accounts")
w.caption("Table 4. Records used and their role.")
w.table([
    ["Evidence source", "What is observed", "Role"],
    ["Indonesian platform histories", "Transaction value and revenue through time", "Measure the wedge and its movement"],
    ["BPS national e-commerce statistics", "Online sales of surveyed businesses, by channel, and the number of businesses",
     "Examine the level and sources of growth"],
    ["BPS marketplace study", "Business-level marketplace and recordkeeping evidence",
     "Examine the association with financial recordkeeping"],
    ["Bank Indonesia", "Economy-wide digital payment measures", "Context on payment growth"],
    ["Platform companies outside Indonesia", "Matched transaction and revenue measures",
     "Test whether the same boundary appears elsewhere"],
])
w.para("Table 4 gives each record a single role. The records answer different questions, so they are reported "
       "separately rather than pooled into one estimate.")
w.para("For H2, national e-commerce value S is written as:")
w.eq("S = N × A")
w.para(
    "where N is the estimated number of e-commerce businesses and A is implied nominal sales per business, and the "
    "change in S is divided arithmetically between the two. BPS publishes two counts of 2023 businesses; the count "
    "consistent with its stated growth figure is used, and the other is retained as a sensitivity check.")
w.para(
    "For H3, BPS's published business-level comparison of marketplace and non-marketplace sellers is used. For H4, "
    "BPS's split of e-commerce value by sales channel is set against the platform evidence. Bank Indonesia payment "
    "measures provide context only: they cover payments across the whole economy, and their growth also reflects the "
    "adoption of payment methods and substitution between them, so they are never added to platform or BPS values or "
    "read as estimates of e-commerce growth.")
w.h2("4.5 External Evidence and Robustness")
w.para(
    "The external comparison contains 48 matched annual observations for eight listed platform businesses from 2017 "
    "to 2025: eBay, Etsy, Jumia, Mercado Libre, Rakuten, Sea, Shopify and Zalando. It tests whether the same "
    "separation between transaction value and revenue appears under other business models and is reported "
    "separately from the Indonesian evidence.")
w.para(
    "Robustness checks vary the admission rules, revenue definitions, publication versions, and the assumptions in "
    "the constructed country measures. The resulting ranges are reported as sensitivity ranges rather than "
    "statistical confidence intervals.")

# ------------------------------------------------------------------ Chapter 5
w.h1("5. Preliminary Evidence and Feasibility")
w.para(
    "The evidence assembled so far establishes that the proposed comparisons can be carried out and that the choice "
    "of record produces economically meaningful differences. The results first show the scale and movement of the "
    "wedge, then compare the platform picture with national and payment records.")
w.h2("5.1 Platform Scale and Movement")
w.para(
    "The 2023 comparison covers Shopee and Tokopedia, which together represented about 70 percent of estimated "
    "Indonesian marketplace transaction value, and Grab, a major delivery intermediary.")
w.caption("Table 5. Indonesia-focused 2023 platform comparison, US$ billions.")
w.table([
    ["Case", "Transaction value V", "Revenue R", "Wedge W", "Ecosystem Ratio E", "Evidence"],
    ["Grab Indonesia", "5.381", "0.605", "4.776", "7.895x", "Transaction value constructed"],
    ["Tokopedia", "16.331", "0.405", "15.926", "39.296x", "Issuer-reported pair"],
    ["Shopee Indonesia", "21.520", "2.152", "19.368", "9.000x", "Transaction value and revenue estimated"],
    ["Three platforms", "43.233", "3.162", "40.070", "12.671x", "Sum of three cases, not national total"],
])
w.para(
    "Table 5 reports that cross-section. Across the three platforms, US$43.23 billion of transaction value "
    "corresponds to US$3.16 billion of recognized revenue, a wedge of US$40.07 billion and a ratio of 13.7 to 1. The "
    "wedge is equivalent in magnitude to about 2.9 percent of Indonesia's 2023 nominal GDP of US$1.371 trillion "
    "(World Bank n.d.); the comparison is of magnitude only, since the wedge is transaction value rather than value "
    "added.")
w.para(
    "Two of the three ratios rest on construction. Shopee's 9.0 is the inverse of the assumed Group monetization rate "
    "less one, and Grab's 7.9 is its Group ratio. Varying Shopee's rate between 9 and 11 percent moves the combined "
    "wedge only between US$39.86 billion and US$40.29 billion, and excluding any one platform leaves at least "
    "US$20.70 billion.")
w.para(
    "Blibli's third-party business and Bukalapak Group, which report both figures themselves, carried wedges of "
    "US$3.20 billion and US$10.50 billion in 2023 at the same exchange rate. They are not added to the total because "
    "their measures include online travel and Group-level activity, but their ratios, 43.4 and 36.0, sit close to "
    "Tokopedia's 39.3: the three issuer-reported ratios lie between 36 and 43, while the two constructed ratios "
    "reflect Group monetization.")
w.para(
    "The relationship is not stable. Across the eight year-to-year comparisons in the main sample, revenue grew "
    "faster than transaction value in six, with a median absolute gap of 38.92 percentage points between the two "
    "growth rates, and the two moved in opposite directions twice. Without the largest comparison, revenue still "
    "grew faster in five of seven, with a median gap of 15.74 points, and excluding any single platform leaves "
    "revenue faster in most comparisons and at least one reversal. Including Grab and Shopee gives ten of twelve, but "
    "those four comparisons track Group monetization rather than Indonesian activity. Figure 1 shows the Ecosystem "
    "Ratio for each platform; every series ends lower than it began, though not by a steady decline.")
w.element(figure_el)
w.caption("Figure 1. Ecosystem Ratio by platform, 2020–2025. Solid lines are issuer-reported pairs; dashed lines are "
          "constructed Indonesian series whose ratios equal Group ratios by construction.", center=True)
w.para(
    "Tokopedia shows why the two measures separate. Between 2022 and 2023 its transaction value fell 8.9 percent "
    "while third-party net revenue rose 53.2 percent; 60.6 percent of the revenue increase reconciles to lower "
    "customer incentives and 39.4 percent to higher gross revenue. Read through its accounts the platform was "
    "growing quickly, read through its transactions it was shrinking. Blibli shows the same reversal in 2024–2025, "
    "when transaction value fell 1.89 percent and net revenue rose 12.07 percent, so the pattern is not confined to "
    "one platform or one year, although Blibli's revenue components have yet to be reconciled.")
w.h2("5.2 Evidence Beyond Platform Revenue")
w.para(
    "National statistics give a different account of the same commerce, beginning with its level. BPS measures the "
    "online sales reported by surveyed e-commerce businesses, whereas platform transaction value is the gross value "
    "of orders processed, and the external Shopee estimate explicitly includes cancelled and returned orders. For "
    "2023, BPS places the marketplace component at Rp200.68 trillion, about US$13.2 billion, in its exclusive split of "
    "transaction value by sales channel, while Tokopedia and Shopee alone reported US$37.9 billion. The figures are "
    "not yet like-for-like: channel attribution, reporting definitions and the populations covered all differ, and "
    "reconciling them is part of the thesis before any remainder is attributed to coverage.")
w.para("Growth can be compared more directly. Table 6 summarizes the evidence for H2–H4 and the payment context.")
w.caption("Table 6. Preliminary evidence beyond platform accounts.")
w.table([
    ["Question", "Preliminary evidence", "Interpretation"],
    ["Where does e-commerce growth come from?",
     "E-commerce value +17.08%; estimated business count +15.31%; sales per business +1.54%. The business count "
     "accounts for 90.29% of the increase (70.95% under BPS's other count)",
     "Growth comes mainly from more businesses selling online (H2)"],
    ["Where does that growth occur?",
     "Marketplace channel +1.45%; other channels +20.57%; 98.46% of the increase is outside the marketplace channel",
     "Marketplace records capture little of recent growth (H4)"],
    ["Are marketplace use and financial records related?",
     "Complete financial statements: 28.63% of marketplace users versus 12.25% of non-marketplace users",
     "Marketplace participation is associated with stronger recordkeeping (H3)"],
    ["Do payment records show the same growth?",
     "BPS e-commerce +17.08%; electronic-money shopping +30.47%; mobile-banking payments and purchases +82.84%; "
     "QRIS +186.98%",
     "Context only: payment measures grow 1.8 to 11 times as fast, and also reflect adoption and substitution"],
])
w.para(
    "The channels outside marketplaces are mainly social media and instant messaging: in 2023, 95.33 percent of "
    "e-commerce businesses sold through instant messaging, and BPS's multiple-response measure attributes 44.04 "
    "percent of transaction value to social media against 32.74 percent to marketplaces. These shares describe one "
    "year and do not allocate the 2023–2024 increase among channels. The business-count split is arithmetic and the "
    "recordkeeping result is an association.")
w.h2("5.3 Feasibility and Scope of the Preliminary Findings")
w.para(
    "The preliminary evidence supports each hypothesis and shows that the comparisons can be completed. It supports "
    "H1 through the six of eight comparisons in which revenue outgrew transaction value; H2 through the business-count "
    "share of growth; H3 through BPS's business-level comparison; and H4 through the different growth recorded within "
    "platforms and within the national channel split.")
w.para(
    "The external comparison corroborates the direction of H1 and qualifies its size. Transaction value exceeds "
    "revenue in all eight businesses, with monetization rates from about 2.4 percent at Shopify to about 25 percent "
    "at Mercado Libre among the marketplaces. Among the 29 comparisons free of acquisitions or perimeter changes, "
    "revenue grew faster than transaction value in 22 and the two moved in opposite directions in 4, but the median "
    "gap, 7.1 percentage points, is far smaller than in the Indonesian main sample.")
w.para(
    "PMK 37/2025 shows the same question arising in administration. Administered by the Directorate General of Taxes "
    "(DJP), it requires designated marketplace operators to report seller-linked transactions and withhold tax, with "
    "implementation from 1 November 2026. It draws on the records of designated operators, whose scope does not "
    "automatically match BPS's marketplace channel, so mapping one to the other is needed before any statement about "
    "its coverage; its compliance and revenue effects lie outside this study.")
w.para(
    "At this stage, the proposed measurement can be constructed, followed through time, reconciled to disclosed "
    "accounting changes, and compared with independent records of Indonesian digital commerce.")

# ------------------------------------------------------------------ Chapter 6
w.h1("6. Why the Problem Matters")
w.para(
    "These records are designed to measure different things, and the problem arises when one is used as a "
    "substitute for another. Platform revenue measures what the platform earns, transaction value the commerce it "
    "carries, national e-commerce statistics the online sales of businesses, and payment systems the movement of "
    "funds. Between 2022 and 2024 they disagreed about both the size and the growth of Indonesian digital commerce: "
    "Tokopedia's transactions shrank while its revenue grew, the marketplace channel was almost flat while national "
    "e-commerce rose 17 percent, and payment measures rose by as much as 187 percent. A reader who takes any one of "
    "them as the measure of the digital economy, whether to value a platform or to size the sector, inherits that "
    "record's view.")

# ------------------------------------------------------------------ Chapter 7
w.h1("7. Limitations and Robustness")
w.para(
    "The evidence is descriptive, and its limits are specific. The main sample is small: three issuer-reported "
    "platforms, 11 platform-years and 8 comparisons, which supports description rather than statistical inference. "
    "Its scope is uneven: Tokopedia is an Indonesia-aligned segment observed for two years, Blibli's segment includes "
    "online travel, and Bukalapak reports at Group level. Grab's and Shopee's Indonesian figures are constructed, so "
    "their ratios carry no independent Indonesian information, and Shopee's revenue rests on an assumed monetization "
    "rate. The records compared in Section 5.2 are defined differently, so their disagreement is measured at this "
    "stage rather than reconciled.")
w.para("Table 7 pairs each supported conclusion with what it does not establish.")
w.caption("Table 7. Main inference boundaries.")
w.table([
    ["Evidence supports", "Does not by itself establish"],
    ["W, E, and D describe the size and movement of the wedge.",
     "Participant profit, taxable income, unpaid tax, tax evasion, or missing GDP."],
    ["Issuer-reported pairs show revenue and transaction value moving apart within platforms.",
     "Independent Indonesian ratio evidence from the constructed Grab and Shopee series."],
    ["Disclosed revenue components reconcile selected movements in the wedge.",
     "A causal effect of incentives, monetization, or accounting choices."],
    ["BPS evidence describes the sources and channels of e-commerce growth and recordkeeping associations.",
     "Causal business entry, productivity effects, or marketplace-induced formalization."],
    ["Platform, BPS and payment records disagree in level and growth.",
     "That either record is wrong, or that payment values measure sales."],
    ["PMK 37/2025 draws on designated operators' transaction records.",
     "Its coverage of the digital economy, or a compliance or tax-revenue effect."],
])
w.para(
    "Robustness is reported as sensitivity ranges: Shopee's assumed rate is varied, each platform is excluded in "
    "turn, the largest comparison is dropped, and the longitudinal result is restricted to issuer-reported pairs.")

# ------------------------------------------------------------------ Chapter 8
w.h1("8. Next Steps")
w.para(
    "The data and empirical framework are assembled. The remaining work is to confirm with the committee the "
    "treatment of the broader-scope and constructed series, reconcile the definitions behind the BPS and platform "
    "levels, divide movements in the wedge into changes in transaction volume and in monetization, and complete the "
    "robustness checks. Table 8 sets out that schedule.")
w.caption("Table 8. Planned work toward the final thesis.")
w.table([
    ["Period", "Planned work"],
    ["Proposal stage", "Incorporate examination feedback; confirm the main sample and the treatment of broader-scope and "
                       "constructed series."],
    ["October–November 2026", "Reconcile BPS and platform definitions; divide wedge movements into volume and "
                              "monetization effects; complete robustness checks; finalize tables and figures."],
    ["Before the final defense", "Complete the full manuscript and the final citation and consistency review."],
])
w.para(
    "The proposed study begins from a simple distinction between the value a platform processes and the revenue it "
    "recognizes. The preliminary evidence shows that the records of Indonesia's digital commerce disagree about its "
    "size and its growth, and that the disagreement is large enough to change the conclusion a reader draws. The "
    "thesis measures that disagreement and identifies which conclusions depend on the record chosen.")

# ------------------------------------------------------------------ Appendix A
w.h1("Appendix A - Variables and Data Sources")
w.caption("Table A1. Variable definitions and sources.")
w.table([
    ["Variable", "Definition", "Source"],
    ["V", "Transaction value processed through the platform in the period", "Issuer disclosure, or construction (Table 3)"],
    ["R", "Revenue the platform recognizes for the same period and business scope",
     "Issuer disclosure, or construction (Table 3)"],
    ["t = R / V", "Monetization rate: the share of transaction value recognized as revenue", "Computed"],
    ["W = V − R", "Invisible wedge: transaction value outside recognized revenue", "Computed"],
    ["E = (V − R) / R = 1/t − 1", "Ecosystem Ratio: wedge per unit of revenue; constructed for this study", "Computed"],
    ["D = g(R) − g(V)", "Growth divergence: revenue growth minus transaction-value growth",
     "Computed from consecutive years"],
    ["S = N × A", "National e-commerce value: number of businesses times sales per business", "BPS-Statistics Indonesia"],
])
w.para("Table A1 defines each variable and says where it comes from. Table A2 traces each record to the filings and "
       "publications behind it.")
w.caption("Table A2. Source lineage by evidence type.")
w.table([
    ["Evidence type", "Platform / source", "Transaction-value source", "Revenue / comparison source"],
    ["Issuer-reported, Indonesia-aligned", "Tokopedia e-commerce", "GoTo annual report, e-commerce segment metrics",
     "GoTo annual report, segment note"],
    ["Issuer-reported, broader scope", "Blibli third-party business",
     "Global Digital Niaga prospectus and results releases", "Same issuer filings"],
    ["Issuer-reported, broader scope", "Bukalapak Group", "Bukalapak annual and sustainability reports",
     "Same issuer filings"],
    ["Requires construction", "Grab Indonesia", "Derived from Indonesia revenue and Group monetization rate",
     "Grab Form 20-F"],
    ["Requires construction", "Shopee Indonesia", "Momentum Works Southeast Asia e-commerce estimate",
     "Derived from Sea Limited Form 20-F"],
    ["National statistics", "BPS-Statistics Indonesia", "E-Commerce Statistics 2023 and 2024; marketplace study",
     "Business-count, channel and recordkeeping evidence"],
    ["Payment statistics", "Bank Indonesia", "Payment System Statistics and QRIS reports", "Growth-rate comparison only"],
    ["Exchange rate and GDP", "World Bank", "World Development Indicators, 2023",
     "Converts 2023 rupiah values; GDP scale comparison"],
    ["External corroboration", "eBay, Etsy, Jumia, Mercado Libre, Rakuten, Sea, Shopify, Zalando",
     "Issuer transaction measures", "Issuer revenue measures"],
    ["Regulatory", "PMK 37/2025; DJP", "Ministry of Finance / Directorate General of Taxes",
     "Institutional architecture only"],
])
w.para("Every figure used in this proposal traces to a named file and locator in the accompanying data package.")

# ------------------------------------------------------------------ previewed revisions 1-8 (17 September)
def _para_containing(text):
    hits = [p for p in doc.paragraphs if text in p.text]
    assert len(hits) == 1, (len(hits), text[:60])
    assert len(hits[0].runs) == 1, ("multi-run paragraph", text[:60])
    return hits[0]


def revise_sub(old, new):
    par = _para_containing(old)
    par.runs[0].text = par.runs[0].text.replace(old, new)


def revise_whole(start, new):
    par = _para_containing(start)
    par.runs[0].text = new


def delete_para(start):
    par = _para_containing(start)
    par._p.getparent().remove(par._p)


def insert_after(start, text):
    """Insert a same-style, single-run paragraph after the unique matching paragraph."""
    par = _para_containing(start)
    new_p = copy.deepcopy(par._p)
    par._p.addnext(new_p)
    new_par = Paragraph(new_p, par._parent)
    for run in new_par.runs[1:]:
        run._element.getparent().remove(run._element)
    if not new_par.runs:
        new_par.add_run()
    new_par.runs[0].text = text
    return new_par


def revise_cell(old, new):
    hits = []
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if cell.text.strip() == old:
                    hits.append(cell)
    assert len(hits) == 1, (len(hits), old)
    cell = hits[0]
    cell.paragraphs[0].runs[0].text = new


def revise_cell_in_row(row_key, old, new):
    hits = []
    for table in doc.tables:
        for row in table.rows:
            if any(row_key in cell.text for cell in row.cells):
                for cell in row.cells:
                    if cell.text.strip() == old:
                        hits.append(cell)
    assert len(hits) == 1, (len(hits), row_key, old)
    hits[0].paragraphs[0].runs[0].text = new


# 1. which platforms report what
revise_sub("The study covers the five Indonesian platforms that publish usable transaction and revenue figures: the "
           "marketplaces Tokopedia, Shopee, Blibli and Bukalapak, and Grab, whose Indonesian business is mainly "
           "delivery and other on-demand services.",
           "The study covers five platforms. Tokopedia, Blibli and Bukalapak report transaction value and revenue "
           "themselves; for the marketplace Shopee and for Grab, whose Indonesian business is mainly delivery and other "
           "on-demand services, the Indonesian figures are partly constructed.")
# 2. take-rate sentence
revise_sub("Seen from the other side, E is the platform's monetization rate, t = R/V, inverted: E = 1/t − 1, so a "
           "platform keeping 2.5 percent of transaction value has an E of 39.",
           "E carries the same information as the platform's monetization rate, t = R/V, since E = 1/t − 1: a platform "
           "that recognizes 2.5 percent of transaction value as revenue has an E of 39.")
# 3. accounting basis
revise_sub("the share of transaction value entering revenue is itself a reporting choice",
           "the share of transaction value entering revenue depends on how revenue is recognized, including whether "
           "the platform acts as principal or agent")
# 4. digital records opening
revise_sub("Activity outside platform revenue is still recorded. Merchants and service providers can be small, "
           "self-employed, or weakly represented in conventional financial records while their transactions leave "
           "detailed records inside a digital platform.",
           "Transactions outside a platform's revenue can still leave a detailed record. Merchants and service providers "
           "can be small, self-employed, or weakly represented in conventional financial records, yet the transactions "
           "they make on a platform are recorded by it.")
# 5. 100/10/90
revise_sub("they represent merchant receipts", "they include merchant receipts")
# 6. section 4.1 sample and windows
revise_whole("The sample consists of the Indonesian platforms that publish both transaction value and revenue.",
    "The main sample consists of the platforms that report transaction value and revenue themselves: Tokopedia, Blibli "
    "and Bukalapak. Grab and Shopee, whose Indonesian figures must be constructed, support the 2023 scale comparison. "
    "Lazada and TikTok Shop, both large in Indonesia, are outside the sample because no matched Indonesian revenue "
    "series has been located for either. The platforms are disclosing cases rather than a representative sample of "
    "Indonesian platforms.")
revise_whole("Table 2 separates the pairs issuers report themselves",
    "Table 2 gives the main sample 11 platform-years and 8 year-to-year comparisons; adding Grab and Shopee gives 17 and "
    "12. Each series covers only the years in which a matched pair exists. Tokopedia, an Indonesia-aligned segment rather "
    "than a literal country line, appears for 2022 and 2023: its 2021 pair covers mismatched periods, and after the "
    "Tokopedia and TikTok Shop businesses were combined under PT Tokopedia on 31 January 2024, the listed parent reports "
    "a contractual fee rather than platform revenue. Blibli runs from 2021 to 2025, with a 2020 prospectus pair used "
    "only as a sensitivity, and its third-party segment includes online travel. Bukalapak runs from 2020 to 2023 at Group "
    "level, including some overseas activity; its 2024 pair is excluded because it covers nine months of transactions "
    "against twelve of revenue. Grab runs from 2021 to 2023, after which its transaction measure changes basis, and "
    "Shopee from 2022 to 2024.")
delete_para("Each series covers the years in which a matched pair exists. Tokopedia is an Indonesia-aligned segment")
# 7. section 5.3
revise_whole("The preliminary evidence supports each hypothesis and shows that the comparisons can be completed.",
    "The preliminary evidence supports each hypothesis: H1 through the six of eight comparisons in which revenue outgrew "
    "transaction value, H2 through the business-count share of growth, H3 through BPS's business-level comparison, and "
    "H4 through the different growth recorded within platforms and within the national channel split.")
revise_whole("The external comparison corroborates the direction of H1 and qualifies its size.",
    "Outside Indonesia, transaction value exceeds revenue in all eight businesses, with monetization rates from about 2.4 "
    "percent at Shopify to about 25 percent at Mercado Libre among the marketplaces. In the 29 comparisons free of "
    "acquisitions or perimeter changes, revenue grew faster than transaction value in 22 and the two moved in opposite "
    "directions in 4. The median gap of 7.1 percentage points is far smaller than in Indonesia, so the external evidence "
    "confirms the direction of H1 while qualifying its size.")
revise_whole("PMK 37/2025 shows the same question arising in administration.",
    "PMK 37/2025, administered by the Directorate General of Taxes (DJP), raises the same question in administration: "
    "from 1 November 2026 it requires designated marketplace operators to report seller-linked transactions and withhold "
    "tax. Its designated operators do not automatically correspond to BPS's marketplace channel, so its coverage cannot "
    "yet be measured, and its compliance and revenue effects lie outside this study.")
delete_para("At this stage, the proposed measurement can be constructed")
# 8. chapter 6
revise_whole("These records are designed to measure different things",
    "These records measure different things, and the problem arises when one stands in for another. Between 2022 and "
    "2024 they disagreed about both the size and the growth of Indonesian digital commerce: Tokopedia's transactions "
    "shrank while its revenue grew, the marketplace channel was almost flat while national e-commerce rose 17 percent, "
    "and payment measures rose by as much as 187 percent. A reader who takes any one of them as the measure of the "
    "digital economy, whether to value a platform or to size the sector, inherits that record's view.")

# ------------------------------------------------------------------ iterative polish, loop 1: narrative spine
revise_sub("revenue grew faster than transaction value in six of eight year-to-year comparisons and moved against it "
           "in two.",
           "revenue grew faster than transaction value in six of eight year-to-year comparisons and moved in the "
           "opposite direction in two.")
revise_sub("Eight platform businesses outside Indonesia show the same boundary with smaller year-to-year divergence.",
           "Eight platform businesses outside Indonesia show the same transaction-revenue distinction with smaller "
           "year-to-year divergence.")
revise_sub("BPS-Statistics Indonesia reports a marketplace channel smaller than two platforms' own transaction value",
           "BPS-Statistics Indonesia, using its own definitions, reports a 2023 marketplace figure below the "
           "transaction value of Tokopedia and Shopee alone")

revise_whole("Southeast Asia's digital economy grew from approximately US$100 billion",
    "Southeast Asia's digital economy grew from approximately US$100 billion in 2020 to US$263 billion in 2024 "
    "(Google, Temasek and Bain 2020, 2024). That figure is one record of the activity: the gross value of the "
    "transactions involved. The platforms that carry those transactions report a different number, their own revenue; "
    "national statistical agencies report a third, the online sales of surveyed businesses; and payment systems report "
    "a fourth, the value of funds moved. Each is correct for what it measures. These measures are often used "
    "interchangeably even though they do not measure the same thing. Substituting one for another changes the measured "
    "scale, growth and even the direction of digital activity.")

revise_whole("Suppose a platform processes 100 units of transaction value",
    "Suppose a platform processes 100 units of transaction value but recognizes only 10 as revenue, meaning that only "
    "10 counts as the platform's own revenue in its accounts. Depending on the business model, the remaining 90 can "
    "include merchant receipts, driver payouts, inventory costs, taxes and other pass-through payments. An analyst using "
    "the platform's accounts sees 10, while one measuring the commerce it processes sees 100. I call the difference the "
    "invisible wedge. Neither number is wrong: revenue records what the platform earned, while transaction value records "
    "what it carried. The arithmetic is familiar; the measurement problem is that the relationship does not remain "
    "fixed.")

revise_whole("Indonesia, the largest digital market in Southeast Asia, shows how far apart these records are.",
    "Indonesia, the largest digital market in Southeast Asia, shows how far apart these records are. The study covers "
    "four marketplaces-Tokopedia, Blibli, Bukalapak and Shopee-plus Grab, whose Indonesian business is mainly delivery "
    "and other on-demand services. Tokopedia, Blibli and Bukalapak report both measures themselves. Grab's transaction "
    "value uses Indonesian revenue and its company-wide ratio; Shopee combines Momentum Works' Indonesian estimate with "
    "Sea's company-wide monetization rate. In 2023, "
    "Tokopedia, Shopee and Grab together processed US$43.23 billion of transaction value against US$3.16 billion of "
    "recognized revenue, a wedge of US$40.07 billion. BPS-Statistics Indonesia, the national statistical agency, placed "
    "the marketplace component of e-commerce at about US$13.2 billion and all e-commerce at US$72.3 billion. These "
    "records are not yet directly comparable because their definitions and scopes differ. Each answers a different "
    "question; quoting one as the size of the digital economy means choosing a particular record.")

revise_sub("while payment measures from Bank Indonesia, the central bank, grew between 1.8 and 11 times as fast.",
           "while economy-wide payment measures from Bank Indonesia, the central bank, grew between 1.8 and 11 times "
           "as fast.")
revise_sub("with 98.5 percent of the increase outside the marketplace channel that platform accounts describe,",
           "with 98.5 percent of the increase outside BPS's marketplace category,")
revise_whole("A statement about how large Indonesia's digital economy is",
    "A statement about how large Indonesia's digital economy is, or how fast it grew, is therefore a statement about a "
    "record. An investor reading platform revenue and an analyst sizing e-commerce from marketplace figures can reach "
    "different conclusions about the same years. Neither record is internally wrong; the error lies in treating either "
    "one as the measure of the digital economy.")

revise_whole("Indonesia provides the main empirical setting. Three objectives follow:",
    "Indonesia provides the main empirical setting. Three objectives follow. First, I measure the invisible wedge across "
    "the platform histories available from 2020 to 2025. Second, I reconcile selected large movements with disclosed "
    "changes in monetization, customer incentives, revenue recognition and reporting scope. Third, I compare the platform "
    "evidence with national e-commerce and payment records to determine whether they give the same account of economic "
    "scale and growth.")
revise_whole("Second, I explain why the wedge moves using accounting components",
    "Second, I reconcile a major movement in the wedge using accounting components the platform discloses. Of the "
    "increase in Tokopedia's net revenue between 2022 and 2023, 60.6 percent reconciles to lower customer incentives and "
    "39.4 percent to higher gross revenue, in a year when its transaction value fell.")
revise_whole("The contribution is a finance measurement problem before it is a tax-policy one.",
    "The contribution is a finance measurement problem. Platform reports reveal both the commerce a platform carries "
    "and the revenue it recognizes, allowing the consequences of substituting one measure for the other to be observed "
    "directly. De Franco, Kothari and Verdi (2011) show why comparable accounting bases matter, while Berg et al. (2020) "
    "show that intermediary-held digital traces contain information conventional records can miss. This paper applies "
    "those ideas to platform economies and shows that the record chosen to describe digital activity changes the "
    "economic conclusion.")

# ------------------------------------------------------------------ iterative polish, loop 2: literature and framework
revise_sub("four marketplaces-Tokopedia, Blibli, Bukalapak and Shopee-plus Grab",
           "four marketplaces—Tokopedia, Blibli, Bukalapak and Shopee—plus Grab")
revise_sub("and moved against it twice.", "and moved in the opposite direction twice.")
revise_sub("places 98.5 percent of 2023–2024 e-commerce growth outside it",
           "places 98.5 percent of 2023–2024 e-commerce growth outside its marketplace category")

revise_sub("Accounting can widen or narrow this difference. Under IFRS 15,",
           "Revenue-recognition rules affect how much of this difference appears in the accounts. Under International "
           "Financial Reporting Standard 15 (IFRS 15),")
revise_whole("Transactions outside a platform's revenue can still leave a detailed record.",
    "Transactions that do not enter a platform's revenue can still leave detailed records within the platform's system. "
    "Merchants and service providers can be small, self-employed, or weakly represented in conventional financial "
    "records, yet the transactions they make on a platform are recorded by it. This differs from shadow-economy settings, "
    "where reliable formal records may be sparse (La Porta and Shleifer 2014; Ulyssea 2018; Medina and Schneider 2019). "
    "Platform-mediated activity can also create traces outside conventional records (Berg et al. 2020; Barrios, Hochberg "
    "and Yi 2022; Denes, Lagaras and Tsoutsoura 2025).")
revise_whole("These records also matter once they become available to government.",
    "Third-party information changes compliance and enforcement (Kleven et al. 2011; Pomeranz 2015; Naritomi 2019; "
    "Kleven, Kreiner and Saez 2016; Slemrod 2019). The OECD Model Rules (OECD 2020) and the European Union's DAC7 regime "
    "(European Union 2021) apply this principle to platforms, as does Indonesia's Minister of Finance Regulation No. 37 "
    "of 2025 through seller identification, transaction-linked reporting and marketplace withholding (Ministry of Finance "
    "of the Republic of Indonesia 2025). The relevance here is informational: what a measure or rule can show depends on "
    "the records it uses.")
revise_sub("research on digital records explains why activity outside revenue is still observable.",
           "research on digital records explains why some platform-mediated activity outside revenue can remain "
           "observable in platform records.")

revise_whole("W is transaction value outside the platform's recognized revenue, not an omission from its accounts:",
    "W is transaction value outside the platform's recognized revenue, not an omission from its accounts: both inputs "
    "can appear in the same company report. It is a transaction-value measure rather than an income or value-added "
    "measure; Section 7 states the corresponding inference boundaries. Because platforms differ in size, I also express "
    "the wedge relative to revenue. The Ecosystem Ratio is:")
revise_whole("An E of 9 means that for every one unit of platform revenue",
    "An E of 9 means that nine units of transaction value lie outside the revenue line for every unit recognized as "
    "platform revenue. E contains the same information as the platform's monetization rate, t = R/V, because E = 1/t − "
    "1. The residual form matches the research question, which concerns commerce outside recognized revenue.")
revise_whole("The Ecosystem Ratio is constructed for this study as a descriptive transformation",
    "The Ecosystem Ratio is a descriptive transformation constructed for this study, not a new underlying economic "
    "quantity or a measure adopted from prior work. Its interpretation rests on the platform-economics result that booked "
    "revenue need not track the transaction value a multisided platform coordinates (Rochet and Tirole 2003; Hagiu and "
    "Wright 2015; Evans and Schmalensee 2016), together with the accounting result that the share entering revenue "
    "depends on how revenue is recognized, including whether the platform acts as principal or agent (International "
    "Accounting Standards Board 2014; De Franco, Kothari and Verdi 2011).")
revise_sub("A single ratio does not show whether the relationship holds through time, so I define annual growth "
           "divergence as:",
           "A single ratio does not show whether the relationship holds through time, so I define annual growth "
           "divergence, where g(X) is the percentage growth of X from one year to the next, as:")
revise_whole("A positive D means revenue grew faster than transaction value",
    "A positive D means revenue grew faster than transaction value, so the platform recognized a larger share of "
    "transaction value as revenue and E fell; a negative D means the reverse. If revenue were a stable proxy for "
    "transaction value, D would remain close to zero. W gives the wedge in currency units, E expresses it relative to "
    "revenue, and D carries the central test: whether the relationship between revenue and transaction value remains "
    "stable through time.")
revise_whole("If they did, D would stay close to zero and E would be constant.",
    "If they did, D would remain close to zero and E would be constant. The test is whether D remains close to zero; "
    "changes in its sign identify especially strong reversals but are not required for H1.")
revise_whole("Recordkeeping determines whether activity outside platform accounts leaves a record",
    "Financial statements are one conventional record a business keeps of its own activity. H3 tests whether the "
    "prevalence of that record differs between marketplace and non-marketplace sellers; it does not treat the association "
    "as causal.")
revise_whole("H4. The measured growth of Indonesian digital commerce depends on the record used, both within platforms",
    "H4. Conclusions about the growth of Indonesian digital commerce change with the record used to measure it.")

# ------------------------------------------------------------------ iterative polish, loop 3: data and results
revise_cell("Annual observations", "Years and observations")
revise_cell_in_row("Tokopedia e-commerce", "2", "2022–2023 (2)")
revise_cell_in_row("Blibli third-party business", "9", "Blibli 2021–2025; Bukalapak 2020–2023 (9)")
revise_cell_in_row("Grab; Shopee Indonesia", "6", "Grab 2021–2023; Shopee 2022–2024 (6)")
revise_whole("Table 2 gives the main sample 11 platform-years",
    "Table 2 gives the main sample 11 platform-years and 8 year-to-year comparisons; adding Grab and Shopee gives 17 "
    "and 12. Each series covers only years for which a matched pair exists. Tokopedia's 2021 pair covers mismatched "
    "periods, and after its combination with TikTok Shop under PT Tokopedia on 31 January 2024, the listed parent reports "
    "a contractual fee rather than platform revenue. Blibli's third-party segment includes online travel; its 2020 "
    "prospectus pair is used only as a sensitivity. Bukalapak reports at Group level, including some overseas activity; "
    "its 2024 pair is excluded because it covers nine months of transactions against twelve of revenue. Grab's "
    "transaction measure changes basis after 2023.")

revise_whole("For H3, BPS's published business-level comparison",
    "For H3, BPS's published business-level comparison of marketplace and non-marketplace sellers is used. For H4, "
    "BPS's split of e-commerce value by sales channel is set against the platform evidence. Bank Indonesia's "
    "economy-wide payment measures provide an independent view of digitalization. Because they cover more than "
    "e-commerce and also reflect adoption and substitution between payment methods, they are compared by growth rate "
    "and are not treated as sales estimates.")

revise_whole("Two of the three ratios rest on construction.",
    "Two ratios rest on construction. Shopee's 9.0 follows from an assumed company-wide monetization rate of 10 percent; "
    "Grab's 7.9 is its company-wide ratio. Neither provides independent Indonesian ratio evidence. Varying Shopee's rate "
    "from 9 to 11 percent puts the combined wedge between US$39.86 billion and US$40.29 billion; excluding any platform "
    "leaves at least US$20.70 billion.")
revise_whole("Blibli's third-party business and Bukalapak Group, which report both figures themselves",
    "Blibli and Bukalapak report 2023 wedges of US$3.20 billion and US$10.50 billion but are excluded from the total "
    "because their measures include online travel and Group-level activity. Their ratios, 43.4 and 36.0, sit close to "
    "Tokopedia's 39.3; the constructed ratios instead reflect company-wide monetization.")
revise_whole("The relationship is not stable. Across the eight year-to-year comparisons",
    "The relationship is not stable. Revenue grew faster in six of eight main-sample comparisons; the median absolute "
    "gap is 38.92 percentage points, with two reversals. Tokopedia's 53.2 percent revenue growth against an 8.9 percent "
    "transaction-value decline gives a 62.1-point divergence. Dropping the largest comparison leaves five of seven and a "
    "15.74-point median; every leave-one-out sample retains a majority and a reversal. Adding Grab and Shopee gives ten "
    "of twelve, but those four comparisons track company-wide monetization. Figure 1 shows E for each platform; every "
    "series ends lower than it began, though not steadily.")
revise_sub("Read through its accounts the platform was growing quickly, read through its transactions it was shrinking.",
           "Its accounts alone suggest rapid growth; its transactions show contraction.")

revise_whole("National statistics give a different account of the same commerce, beginning with its level.",
    "National statistics give a different account of the same commerce, beginning with its level. BPS measures the "
    "online sales reported by surveyed e-commerce businesses, whereas platform transaction value is the gross value of "
    "orders processed, and the external Shopee estimate explicitly includes cancelled and returned orders. For 2023, "
    "BPS places the marketplace component at Rp200.68 trillion, about US$13.2 billion, in its exclusive channel split, "
    "where marketplaces account for 18.2 percent of transaction value. Tokopedia and Shopee alone reported US$37.9 "
    "billion. Channel attribution and reporting definitions differ, so the records are not yet like-for-like; the thesis "
    "will reconcile those definitions before attributing any remainder to coverage.")
revise_cell("Marketplace records capture little of recent growth (H4)",
            "Most measured growth occurs outside BPS's marketplace category (H4)")
revise_cell("BPS e-commerce +17.08%; electronic-money shopping +30.47%; mobile-banking payments and purchases +82.84%; "
            "QRIS +186.98%",
            "BPS e-commerce +17.08%; electronic-money shopping +30.47%; mobile-banking payments and purchases +82.84%; "
            "Quick Response Code Indonesian Standard (QRIS) +186.98%")
revise_whole("The channels outside marketplaces are mainly social media and instant messaging:",
    "BPS separately reports extensive use of non-marketplace channels. In 2023, 95.33 percent of e-commerce businesses "
    "used instant messaging. Its multiple-response measure, in which a business can report several channels, attributed "
    "44.04 percent of transaction value to social media and 32.74 percent to marketplaces; it is therefore not the same "
    "split as the exclusive 18.2 percent measure above. These figures describe the channel structure in 2023 and do not "
    "allocate the 2023–2024 increase among those channels. The business-count split is arithmetic and the recordkeeping "
    "result is an association.")

revise_whole("Outside Indonesia, transaction value exceeds revenue in all eight businesses",
    "Outside Indonesia, transaction value exceeds revenue in all eight businesses. Among the marketplaces, monetization "
    "rates range from about 2.4 percent at Shopify to about 25 percent at Mercado Libre. In the 29 comparisons not affected "
    "by acquisitions or changes in reporting scope, revenue grew faster than transaction value in 22 and the measures "
    "moved in opposite directions in 4. The external evidence therefore shows the same transaction-revenue separation, "
    "but a smaller typical divergence: the median gap is 7.1 percentage points, compared with 38.92 points in the "
    "Indonesian main sample.")
revise_whole("PMK 37/2025, administered by the Directorate General of Taxes (DJP), raises the same question",
    "PMK 37/2025 provides an administrative example. From 1 November 2026, the Directorate General of Taxes (DJP) "
    "requires designated marketplace operators to report seller-linked transactions and withhold tax. Those operators "
    "cannot yet be mapped directly to BPS's marketplace category; compliance and revenue effects remain outside this "
    "study.")

# ------------------------------------------------------------------ iterative polish, loop 4: synthesis, limits and conclusion
revise_whole("BPS separately reports extensive use of non-marketplace channels.",
    "BPS also reports widespread use of non-marketplace channels. In 2023, 95.33 percent of e-commerce businesses used "
    "instant messaging. In its multiple-response measure, where a business can report several channels, social media "
    "accounted for 44.04 percent of transaction value and marketplaces for 32.74 percent; that measure is not comparable "
    "with the exclusive 18.2 percent split above. These figures describe the 2023 channel structure rather than the "
    "allocation of 2023–2024 growth. The business-count split is arithmetic and the recordkeeping result is an "
    "association.")
revise_whole("Outside Indonesia, transaction value exceeds revenue in all eight businesses.",
    "Outside Indonesia, transaction value exceeds revenue in all eight businesses. In the 29 comparisons not affected "
    "by acquisitions or changes in reporting scope, revenue grew faster than transaction value in 22 and the measures "
    "moved in opposite directions in 4. The median gap is 7.1 percentage points, compared with 38.92 points in the "
    "Indonesian main sample. Among the marketplaces, monetization rates range from about 2.4 percent at Shopify to about "
    "25 percent at Mercado Libre.")

revise_whole("These records measure different things, and the problem arises when one stands in for another.",
    "Indonesia's digital economy is observed through platform accounts, transaction measures, national statistics and "
    "payment records, which disagree about scale and growth. Revenue alone can reverse the apparent direction of platform "
    "activity, while a marketplace measure can show a different trend from all e-commerce. The contribution is to "
    "identify which conclusions depend on the record selected and why no fixed conversion from platform revenue can "
    "recover the commerce underneath it, rather than to claim a single missing total.")

revise_whole("The evidence is descriptive, and its limits are specific.",
    "The evidence is descriptive. The main sample has three platforms, 11 platform-years and 8 comparisons, supporting "
    "description rather than statistical inference. Scope differs: Tokopedia is observed for two years, Blibli includes "
    "online travel, and Bukalapak reports at Group level. Grab and Shopee are constructed, their ratios contain no "
    "independent Indonesian information, and Shopee's revenue uses an assumed monetization rate. Section 5.2 also compares "
    "differently defined records whose disagreement is measured but not yet reconciled.")
revise_cell("That either record is wrong, or that payment values measure sales.",
            "Which record, if any, contains measurement error, or that payment values measure sales.")

revise_whole("The data and empirical framework are assembled.",
    "The data and empirical framework are assembled. The remaining work will reconcile the definitions behind the BPS "
    "and platform levels, divide movements in the wedge into transaction-volume and monetization effects, test alternative "
    "admission rules, and complete the robustness checks. Table 8 sets out that schedule.")
revise_cell("Incorporate examination feedback; confirm the main sample and the treatment of broader-scope and constructed series.",
            "Incorporate examination feedback; finalize the treatment of broader-scope and constructed series.")
revise_whole("The proposed study begins from a simple distinction",
    "Indonesia's digital economy is observed through several records that measure different objects. The preliminary "
    "evidence shows that those records disagree about its size, growth and, in some cases, direction. This thesis measures "
    "that disagreement, tests whether the relationship between revenue and transaction value remains stable, and "
    "identifies which conclusions depend on the record chosen.")
revise_sub("Appendix A - Variables and Data Sources", "Appendix A. Variables and Data Sources")

# ------------------------------------------------------------------ iterative polish, loop 7: page-break cleanup
revise_whole("Sea Limited does not report Shopee transaction value separately for Indonesia.",
    "Sea Limited does not report Shopee transaction value separately for Indonesia. Momentum Works supplies the "
    "Indonesian estimate; its annual Southeast Asian e-commerce report is widely cited for country-level platform "
    "estimates and is used because no issuer discloses the figure. The value is labelled as a third-party estimate "
    "wherever it appears, and Indonesian revenue is estimated using Sea's Group service monetization rate:")
revise_whole("In both cases the Indonesian ratio is fixed by construction:",
    "Construction fixes both Indonesian ratios to company-wide relationships: Grab's E equals its Group E, while "
    "Shopee's is the inverse of Sea's monetization rate less one. The series contribute Indonesian levels but no "
    "independent evidence on the ratio or its movement, so they remain outside the main sample.")
revise_whole("Tokopedia shows why the two measures separate.",
    "Tokopedia illustrates the separation. In 2022–2023, transaction value fell 8.9 percent while third-party net "
    "revenue rose 53.2 percent; 60.6 percent of the revenue increase reconciles to lower customer incentives and 39.4 "
    "percent to higher gross revenue. Its accounts show growth while its transactions show contraction. Blibli similarly "
    "reversed in 2024–2025: transaction value fell 1.89 percent and net revenue rose 12.07 percent. Its revenue components "
    "remain unreconciled.")
_para_containing("Indonesia's digital economy is observed through several records that measure different objects.").paragraph_format.keep_together = True

# ------------------------------------------------------------------ iterative polish, loop 11: final precision and abstract tightening
revise_whole("Digital economy is measured through several records:",
    "Digital economy is measured through several records: the transaction value platforms process, the revenue they "
    "recognize, national e-commerce statistics and payment data. These records capture parts of the same activity. This "
    "study defines the invisible wedge as transaction value minus platform-recognized revenue and follows it across "
    "Indonesian platforms from 2020 to 2025. In 2023, Tokopedia, Shopee and Grab processed US$43.23 billion against "
    "US$3.16 billion of recognized revenue. The relationship was unstable: among platforms reporting both figures, "
    "revenue grew faster in six of eight year-to-year comparisons and moved in the opposite direction in two. "
    "BPS-Statistics Indonesia reports a 2023 marketplace figure below Tokopedia and Shopee's transaction value alone "
    "and places 98.5 percent of 2023–2024 e-commerce growth outside its marketplace category. Payment measures grew up "
    "to eleven times as fast. Eight platforms outside Indonesia show the transaction-revenue distinction with smaller "
    "divergence. Thus, conclusions about scale and growth depend on the record used.")

revise_sub("Each is correct for what it measures. These measures are often used interchangeably even though they do not "
           "measure the same thing.",
           "These records are designed to measure different things, yet they are often used interchangeably.")

revise_whole("Suppose a platform processes 100 units of transaction value",
    "Suppose a platform processes 100 units of transaction value but recognizes only 10 as its own revenue: the "
    "commissions and fees it earns for arranging the transactions. Depending on the business model, the remaining 90 "
    "can include merchant receipts, driver payouts, inventory costs, taxes and other pass-through payments. An analyst "
    "using the platform's accounts sees 10, while one measuring the commerce it processes sees 100. I call the "
    "difference the invisible wedge. Neither number is wrong: revenue records what the platform earned, while "
    "transaction value records what it carried. The arithmetic is familiar; the measurement problem is that the "
    "relationship does not remain fixed.")

revise_whole("A statement about how large Indonesia's digital economy is",
    "A statement about how large Indonesia's digital economy is, or how fast it grew, is therefore a statement about a "
    "record. An investor using platform revenue and an analyst using marketplace figures reach different conclusions "
    "about the same years because the records measure different objects. The error lies in treating either one as the "
    "measure of the digital economy.")

revise_sub("Indonesia's Minister of Finance Regulation No. 37 of 2025 through",
           "Indonesia's Minister of Finance Regulation No. 37 of 2025 (PMK 37/2025) through")

revise_whole("Blibli and Bukalapak report 2023 wedges of",
    "At the 2023 exchange rate, Blibli's and Bukalapak's reported transaction and revenue figures yield wedges of "
    "US$3.20 billion and US$10.50 billion. They are excluded from the total because their measures include online travel "
    "and Group-level activity. Their ratios, 43.4 and 36.0, sit close to Tokopedia's 39.3; the constructed ratios instead "
    "reflect company-wide monetization.")

revise_whole("National statistics give a different account of the same commerce, beginning with its level.",
    "National statistics give a different account of the same commerce, beginning with its level. BPS measures online "
    "sales reported by surveyed e-commerce businesses; Tokopedia reports GTV, while the external Shopee figure is a GMV "
    "estimate. For 2023, BPS places the marketplace component at Rp200.68 trillion, about US$13.2 billion, in its "
    "exclusive channel split, where marketplaces account for 18.2 percent of transaction value. Tokopedia's reported "
    "GTV and the external Shopee estimate total US$37.9 billion. Because channel attribution and reporting definitions "
    "differ, the records are not yet like-for-like. The thesis will reconcile those definitions before attributing any "
    "part of the difference to coverage.")

revise_sub("The value is labelled as a third-party estimate", "The value is labeled as a third-party estimate")

revise_whole("Indonesia's digital economy is observed through platform accounts, transaction measures, national",
    "Indonesia's digital economy is observed through platform accounts, transaction measures, national statistics and "
    "payment records, which disagree about scale and growth. Revenue alone can reverse the apparent direction of platform "
    "activity, while a marketplace measure can show a different trend from all e-commerce. The contribution is to "
    "identify which conclusions depend on the record selected and why no fixed conversion from platform revenue can "
    "recover the commerce underneath it.")

# ------------------------------------------------------------------ references: add World Bank, then footnote
last_ref = [p for p in doc.paragraphs if p.style.name == "Reference" and p.text.strip()][-1]
new_ref = copy.deepcopy(last_ref._p)
last_ref._p.addnext(new_ref)
rp = Paragraph(new_ref, doc._body)
for r in rp.runs[1:]:
    r._element.getparent().remove(r._element)
rp.runs[0].text = ("World Bank. (n.d.). World Development Indicators: GDP (current US$) and official exchange rate "
                   "(LCU per US$, period average), Indonesia. Washington, DC: World Bank.")

add_footnotes(doc, ["Issuer labels differ. GoTo reports GTV and Sea Limited reports GMV for Shopee; for these the label "
                    "differs but the measure is the same. Blibli and Bukalapak report TPV for the segments used here, "
                    "and Grab reports GMV for deliveries and mobility and TPV for financial services. Where a source "
                    "reports TPV the measure rests on a different basis, so it is retained under its own label rather "
                    "than relabeled as GTV."])
doc.save(OUT)
print("wrote", OUT)
