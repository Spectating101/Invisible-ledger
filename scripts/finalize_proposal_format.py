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
        fmt.space_before = Pt(6 if text == "References" else 7)
        fmt.space_after = Pt(2.5)
        fmt.keep_with_next = True
        continue
    if paragraph.style.name == "Heading 2":
        for run in paragraph.runs:
            set_run_font(run, 12, True)
        fmt.space_before = Pt(4.5)
        fmt.space_after = Pt(1.5)
        fmt.keep_with_next = True
        continue
    if text.startswith("Table ") and ". " in text:
        for run in paragraph.runs:
            set_run_font(run, 9.5, True)
            run.italic = True
        fmt.space_before = Pt(3)
        fmt.space_after = Pt(1.5)
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
        fmt.space_after = Pt(2.5)
        fmt.line_spacing = 1.0291666667
    if text.startswith(post_table_starts):
        fmt.space_before = Pt(5)
        fmt.keep_together = True
    elif text.startswith("Figure 1 makes"):
        fmt.space_before = Pt(4.5)
        fmt.keep_together = True

# Widths mirror the polished proposal; Tables 1–2 also use explicit grids so
# the evidence labels and numeric columns remain readable on one line.
cell_widths = [
    [2835, 3402, 1655, 1655],
    [2721, 879, 879, 879, 935, 3254],
    [3816, 2865, 2865],
    [4773, 4773],
    [2232, 7315],
    [2160, 2160, 3096, 2131],
]
margin_lr = [35, 35, 55, 55, 55, 55]
margin_start = [38, 38, 38, 38, 30, 38]

for ti, table in enumerate(doc.tables):
    table.autofit = False
    widths = cell_widths[ti] if ti < len(cell_widths) else None
    if ti in (0, 1) and widths:
        for grid_col, width in zip(table._tbl.tblGrid.gridCol_lst, widths):
            grid_col.set(qn("w:w"), str(width))
    for row in table.rows:
        cant_split(row)
        for ci, cell in enumerate(row.cells):
            if widths and ci < len(widths):
                set_cell_width(cell, widths[ci])
            set_cell_margins(
                cell,
                45,
                margin_start[ti],
                45,
                margin_start[ti],
                margin_lr[ti],
                margin_lr[ti],
            )
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.space_before = Pt(0)
                paragraph.paragraph_format.space_after = Pt(0)
                paragraph.paragraph_format.line_spacing = 1.0
                for run in paragraph.runs:
                    set_run_font(run, 9)

if doc.inline_shapes:
    doc.inline_shapes[0].width = Cm(14.5288)
    doc.inline_shapes[0].height = Cm(7.42732)

doc.save(DOCX)
print(f"Formatted {DOCX}")
