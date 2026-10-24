"""Finishes the condensed Word copy: three-line tables (rule above and below the header and at the foot), 9.5 pt table text, headers repeated
across pages, rows kept whole, and every caption kept with its table or figure. Usage: python3 docx_post.py in.docx out.docx"""
import sys, docx
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
d = docx.Document(sys.argv[1])
def border(cell_or_tbl_pr, edge, sz):
    el = OxmlElement(f"w:{edge}"); el.set(qn("w:val"), "single"); el.set(qn("w:sz"), str(sz)); el.set(qn("w:space"), "0"); el.set(qn("w:color"), "000000")
    return el
for t in d.tables:
    tblPr = t._tbl.tblPr
    for old in tblPr.findall(qn("w:tblBorders")): tblPr.remove(old)
    b = OxmlElement("w:tblBorders")
    b.append(border(None, "top", 8)); b.append(border(None, "bottom", 8)); tblPr.append(b)
    for old in tblPr.findall(qn("w:tblW")): tblPr.remove(old)
    w = OxmlElement("w:tblW"); w.set(qn("w:w"), "5000"); w.set(qn("w:type"), "pct"); tblPr.append(w)
    for i, row in enumerate(t.rows):
        trPr = row._tr.get_or_add_trPr()
        cs = OxmlElement("w:cantSplit"); trPr.append(cs)
        if i == 0:
            h = OxmlElement("w:tblHeader"); trPr.append(h)
        for c in row.cells:
            tcPr = c._tc.get_or_add_tcPr()
            if i == 0:
                tb = OxmlElement("w:tcBorders"); tb.append(border(None, "bottom", 4)); tcPr.append(tb)
            for p in c.paragraphs:
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p.paragraph_format.space_after = Pt(1); p.paragraph_format.space_before = Pt(1); p.paragraph_format.line_spacing = 1.0
                for r in p.runs:
                    r.font.size = Pt(9)
                    if i == 0: r.font.bold = True
# equations: the markers become the tabs that centre the formula and set the number at the right margin
for p in d.paragraphs:
    if p.style.name.lower() == "equation":
        for r in p.runs:
            if "§T§" in r.text: r.text = r.text.replace("§T§", "\t")
# column widths follow the content (pandoc gives pipe tables equal columns when no line is long)
for t in d.tables:
    n = len(t.columns); lens = [8] * n
    for row in t.rows:
        for i, c in enumerate(row.cells):
            if i < n: lens[i] = max(lens[i], min(len(c.text), 70) + 6)
    tot = sum(lens)
    t.autofit = False
    grid = t._tbl.tblGrid
    for i, gc in enumerate(grid.findall(qn("w:gridCol"))):
        gc.set(qn("w:w"), str(int(9300 * lens[i] / tot)))
    for row in t.rows:
        for i, c in enumerate(row.cells):
            tcPr = c._tc.get_or_add_tcPr()
            for old in tcPr.findall(qn("w:tcW")): tcPr.remove(old)
            w = OxmlElement("w:tcW"); w.set(qn("w:w"), str(int(9300 * lens[i] / tot))); w.set(qn("w:type"), "dxa"); tcPr.insert(0, w)
# keep a caption with the table or figure that follows or precedes it
paras = d.paragraphs
for p in paras:
    txt = p.text.strip()
    if txt.startswith("Table ") and txt[6:7].isdigit() and len(txt) < 400:
        p.paragraph_format.keep_with_next = True; p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for r in p.runs: r.font.size = Pt(10)
    if txt.startswith("Figure ") and txt[7:8].isdigit():
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for r in p.runs: r.font.size = Pt(10)
    if txt.startswith("Note:"):
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for r in p.runs: r.font.size = Pt(9.5)
# figures: centred and kept with the caption below
for p in paras:
    if p._p.xpath(".//w:drawing"):
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.keep_with_next = True
d.save(sys.argv[2])
