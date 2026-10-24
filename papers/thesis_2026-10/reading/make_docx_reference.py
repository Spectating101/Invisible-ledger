"""Writes docx_reference.docx, the style template of the condensed Word copy. It copies the compact PDF (style.css and style_compact.css): A4, margins
14 mm above and below and 15 mm at the sides, Source Serif 4 at 9.4 pt with exact 12.1 pt lines, justified text, 13.5 pt left-aligned chapter headings,
a 12 pt title with a rule, a centred 8 pt page number, and an Equation style with a centre and a right tab. Run: python3 make_docx_reference.py"""
import subprocess, docx
from docx.shared import Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
subprocess.run(["pandoc", "-o", "/tmp/ref_default.docx", "--print-default-data-file", "reference.docx"], check=True)
d = docx.Document("/tmp/ref_default.docx")
by = {s.name.lower(): s for s in d.styles}
sec = d.sections[0]
sec.page_height, sec.page_width = Mm(297), Mm(210)
sec.left_margin = sec.right_margin = Mm(15); sec.top_margin = sec.bottom_margin = Mm(14)
sec.footer_distance = Mm(6)
TEXT_W = 180.0
FONT = "Source Serif 4"; INK = RGBColor(0x11, 0x11, 0x11)
def setfont(st, size, bold=None, italic=None, color=INK):
    st.font.name = FONT
    rpr = st.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
    if rf is None: rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"): rf.set(qn(a), FONT)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
    st.font.size = Pt(size); st.font.color.rgb = color
    if bold is not None: st.font.bold = bold
    if italic is not None: st.font.italic = italic
def para(st, line=None, before=0, after=0, align=None, keep=None):
    pf = st.paragraph_format
    if line: pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(line)
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    if align is not None: pf.alignment = align
    if keep: pf.keep_with_next = True
J, L, C = WD_ALIGN_PARAGRAPH.JUSTIFY, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER
BODY = 9.4; LH = round(BODY * 1.285, 1)          # 12.1 pt, as the PDF's line-height 1.285
for n in ("normal", "body text", "first paragraph"):
    setfont(by[n], BODY); para(by[n], LH, 0, 3.9, J)
setfont(by["compact"], BODY); para(by["compact"], LH, 0, 1.0, L)
setfont(by["block text"], BODY); para(by["block text"], LH, 4.3, 5.7, L)
by["block text"].paragraph_format.left_indent = Mm(8); by["block text"].paragraph_format.right_indent = Mm(8)
setfont(by["title"], 12, True); para(by["title"], 15.6, 0, 2.8, L)
setfont(by["subtitle"], 9, False, True); para(by["subtitle"], 11.6, 0, 11, L)
pPr = by["subtitle"].element.get_or_add_pPr(); bdr = OxmlElement("w:pBdr"); b = OxmlElement("w:bottom")
for k, v in (("val", "single"), ("sz", "6"), ("space", "6"), ("color", "999999")): b.set(qn("w:" + k), v)
bdr.append(b); pPr.append(bdr)
for n in ("author", "date"): setfont(by[n], 9); para(by[n], 11.6, 0, 1, L)
setfont(by["heading 1"], 13.5, True, False); para(by["heading 1"], 17.6, 19.8, 8.5, L, True)
setfont(by["heading 2"], 10.6, True, False); para(by["heading 2"], 13.6, 11.3, 2.8, L, True)
setfont(by["heading 3"], 9.6, True, True); para(by["heading 3"], 12.3, 8.5, 2.8, L, True)
setfont(by["heading 4"], 9.4, True, False); para(by["heading 4"], LH, 6, 2, L, True)
for n in ("table caption", "image caption", "caption"):
    if n in by: setfont(by[n], 8.8, False, False); para(by[n], 12.3, 7, 2.8, L)
setfont(by["footnote text"], 8.4); para(by["footnote text"], 10.8, 0, 1, L)
if "equation" not in by:
    eq = d.styles.add_style("Equation", WD_STYLE_TYPE.PARAGRAPH); eq.base_style = by["normal"]
else: eq = by["equation"]
setfont(eq, 9.6); para(eq, 12.3, 4.3, 5.7, L); eq.paragraph_format.keep_together = True
eq.paragraph_format.tab_stops.add_tab_stop(Mm(TEXT_W / 2), WD_TAB_ALIGNMENT.CENTER); eq.paragraph_format.tab_stops.add_tab_stop(Mm(TEXT_W), WD_TAB_ALIGNMENT.RIGHT)
p = sec.footer.paragraphs[0] if sec.footer.paragraphs else sec.footer.add_paragraph(); p.alignment = C
r = p.add_run()
for t, txt in (("begin", None), ("instr", " PAGE "), ("separate", None), ("text", "1"), ("end", None)):
    if t == "instr": el = OxmlElement("w:instrText"); el.set(qn("xml:space"), "preserve"); el.text = txt
    elif t == "text": el = OxmlElement("w:t"); el.text = txt
    else: el = OxmlElement("w:fldChar"); el.set(qn("w:fldCharType"), t)
    r._r.append(el)
r.font.size = Pt(8); r.font.name = FONT
d.save("docx_reference.docx"); print("docx_reference.docx written")
