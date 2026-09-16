import re
from docx import Document
from docx.shared import Pt, Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import sys

DOCX = sys.argv[1] if len(sys.argv) > 1 else "papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.docx"


def set_run_font(run, size=None, bold=None):
    run.font.name = "Times New Roman"
    run._element.rPr.rFonts.set(qn("w:ascii"), "Times New Roman")
    run._element.rPr.rFonts.set(qn("w:hAnsi"), "Times New Roman")
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    if size is not None:
        run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold


def set_cell_margins(cell, top=45, start=38, bottom=45, end=38, left=None, right=None):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = tcPr.find(qn("w:tcMar"))
    if tcMar is None:
        tcMar = OxmlElement("w:tcMar")
        tcPr.append(tcMar)
    values = {"top": top, "start": start, "bottom": bottom, "end": end}
    if left is not None:
        values["left"] = left
    if right is not None:
        values["right"] = right
    for side, value in values.items():
        el = tcMar.find(qn("w:" + side))
        if el is None:
            el = OxmlElement("w:" + side)
            tcMar.append(el)
        el.set(qn("w:w"), str(value))
        el.set(qn("w:type"), "dxa")


def set_cell_width(cell, twips):
    tcPr = cell._tc.get_or_add_tcPr()
    tcW = tcPr.find(qn("w:tcW"))
    if tcW is None:
        tcW = OxmlElement("w:tcW")
        tcPr.append(tcW)
    tcW.set(qn("w:w"), str(twips))
    tcW.set(qn("w:type"), "dxa")


def cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    if trPr.find(qn("w:cantSplit")) is None:
        trPr.append(OxmlElement("w:cantSplit"))


doc = Document(DOCX)
sec = doc.sections[0]
sec.page_width = Cm(21.0)
sec.page_height = Cm(29.7)
sec.top_margin = Cm(1.98085)
sec.bottom_margin = Cm(1.82915)
sec.left_margin = Cm(2.08315)
sec.right_margin = Cm(2.08315)

for name, size, bold, before, after in [
    ("Normal", 12, None, 0, 2.5),
    ("Heading 1", 12, True, 7, 2.5),
    ("Heading 2", 12, True, 4.5, 1.5),
]:
    style = doc.styles[name]
    style.font.name = "Times New Roman"
    style._element.rPr.rFonts.set(qn("w:ascii"), "Times New Roman")
    style._element.rPr.rFonts.set(qn("w:hAnsi"), "Times New Roman")
    style._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    style.paragraph_format.space_before = Pt(before)
    style.paragraph_format.space_after = Pt(after)

doc.styles["Normal"].paragraph_format.line_spacing = 1.0291666667

# Keep Table 1 labels aligned with Appendix A and current main.
replacements = {
    "Direct Indonesia-aligned segment": "Direct Indonesia-aligned",
    "Direct issuer, scope-pending": "Direct, scope-pending",
    "Conditional country reconstruction": "Conditional reconstruction",
}
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            value = cell.text.strip()
            if value in replacements:
                cell.text = replacements[value]

ref_idx = next(i for i, p in enumerate(doc.paragraphs) if p.text.strip() == "References")
post_table_starts = (
    "Table 1 shows",
    "Table 2 reports",
    "Table 3 compares",
    "Table 4 summarizes",
    "Every figure used",
)

for i, paragraph in enumerate(doc.paragraphs):
    text = paragraph.text.strip()
    fmt = paragraph.paragraph_format
    if not text:
        continue
    if i > ref_idx:
        for run in paragraph.runs:
            set_run_font(run, 10.5)
        fmt.space_before = Pt(0)
        fmt.space_after = Pt(0.6)
        fmt.line_spacing = 1.0
        fmt.left_indent = Cm(0.381)
        fmt.first_line_indent = Cm(-0.381)
        continue
    if paragraph.style.name == "Heading 1":
        for run in paragraph.runs:
            set_run_font(run, 12, True)
        fmt.space_before = Pt(8 if text == "References" else 10)
        fmt.space_after = Pt(5.0)
        fmt.keep_with_next = True
        continue
    if paragraph.style.name == "Heading 2":
        for run in paragraph.runs:
            set_run_font(run, 12, True)
        fmt.space_before = Pt(7)
        fmt.space_after = Pt(3)
        fmt.keep_with_next = True
        continue
    if re.match(r"^Table [0-9A]+\.", text):   # a caption, not prose that merely opens with a table reference
        for run in paragraph.runs:
            set_run_font(run, 9.5, True)
            run.italic = True
        fmt.space_before = Pt(4)
        fmt.space_after = Pt(2.5)
        fmt.line_spacing = 1.0
        fmt.keep_with_next = True
        continue
    if text.startswith("Figure 1."):
        for run in paragraph.runs:
            set_run_font(run, 9.5, True)
            run.italic = True
        fmt.space_before = Pt(2)
        fmt.space_after = Pt(1.5)
        fmt.line_spacing = 1.0
        fmt.keep_with_next = True
        continue
    for run in paragraph.runs:
        set_run_font(run, 12)
    if i >= 14:
        fmt.space_after = Pt(4.0)
        fmt.line_spacing = 1.0291666667
    if re.match(r"^Table \d+ (shows|reports|compares|summarizes|sets)\b", text) or text.startswith("Every figure used"):
        fmt.space_before = Pt(5)
        fmt.keep_together = True
    elif text.startswith(("Figure 1 makes", "Figure 1 shows")):
        fmt.space_before = Pt(4.5)
        fmt.keep_together = True

# Tables are identified by header text, not position, so inserting or removing a table cannot
# shift widths onto the wrong one. Every table spans the 9547-dxa text width.
WIDTHS = {
    "Hypothesis":       [3300, 6247],
    "Type of evidence": [2700, 3100, 1300, 2447],
    "Platform":         [1500, 2700, 2800, 2547],
    "Evidence source":  [2600, 3600, 3347],
    "Case":             [2000, 1250, 1050, 1050, 1250, 2947],
    "Question":         [2050, 4450, 3047],
    "Claim":            [3100, 6447],
    "Evidence supports": [4500, 5047],
    "Period":           [2232, 7315],
    "Evidence type":    [2000, 2100, 2900, 2547],
}
MARGIN_LR = {"Case": 35, "Type of evidence": 35}

for table in doc.tables:
    table.autofit = False
    key = table.rows[0].cells[0].text.strip()
    widths = WIDTHS.get(key)
    if not widths or len(widths) != len(table.columns):
        widths = None
    else:
        for grid_col, width in zip(table._tbl.tblGrid.gridCol_lst, widths):
            grid_col.set(qn("w:w"), str(width))
    lr = MARGIN_LR.get(key, 55)
    last = len(table.rows) - 1
    for ri, row in enumerate(table.rows):
        cant_split(row)
        for ci, cell in enumerate(row.cells):
            if widths:
                set_cell_width(cell, widths[ci])
            set_cell_margins(cell, 45, 38, 45, 38, lr, lr)
            for paragraph in cell.paragraphs:
                pf = paragraph.paragraph_format
                pf.space_before = Pt(0)
                pf.space_after = Pt(0)
                pf.line_spacing = 1.0
                pf.keep_with_next = ri < last   # keeps each table whole, together with its caption
                for run in paragraph.runs:
                    set_run_font(run, 9)

# A heading keeps only the first line of what follows it, which strands headings such as "1.1" at
# the foot of a page. Keep the whole first block with its heading, and pull a short lead-in
# ("One question drives the proposal:") along with whatever it introduces.
blocks = list(doc.paragraphs)
for i, paragraph in enumerate(blocks[:-1]):
    if not paragraph.style.name.startswith("Heading"):
        continue
    nxt = blocks[i + 1]
    if not nxt.text.strip():
        continue
    nxt.paragraph_format.keep_together = True          # do not split that paragraph across pages
    if len(nxt.text.split()) <= 20:                     # a lead-in line, not a real paragraph
        nxt.paragraph_format.keep_with_next = True
        if i + 2 < len(blocks) and blocks[i + 2].text.strip():
            blocks[i + 2].paragraph_format.keep_together = True

# Table cells: align contents to the top so short cells do not float against tall neighbours.
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            tcPr = cell._tc.get_or_add_tcPr()
            vAlign = tcPr.find(qn("w:vAlign"))
            if vAlign is None:
                vAlign = OxmlElement("w:vAlign")
                tcPr.append(vAlign)
            vAlign.set(qn("w:val"), "top")

# Figure: fix the width, derive the height from the image's own pixel dimensions so the chart
# can never be stretched. A fixed width/height pair distorted it by about 40 percent before.
if doc.inline_shapes:
    shape = doc.inline_shapes[0]
    blip = shape._inline.graphic.graphicData.pic.blipFill.blip
    image = doc.part.related_parts[blip.embed].image
    shape.width = Cm(16.83)
    shape.height = int(shape.width * image.px_height / image.px_width)

doc.save(DOCX)
print(f"Formatted {DOCX}")
