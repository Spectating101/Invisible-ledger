"""Finishes the YZU-layout Word copy. Usage: python3 yzu_post.py in.docx out.docx [pages.json]
Tables: three rules, 9 pt, widths from content within the 15 cm text width, header repeated, rows kept whole. Captions: label bold. Figures: at most 15 cm wide.
Page numbers: the front matter (title page to the list of figures) is numbered i, ii, iii (the title page counted but not printed), the main text from Chapter 1
is numbered 1, 2, 3 (two sections). Contents, list of tables and list of figures are real Word fields (TOC), written with the page numbers found in a first
pass (pages.json), so they are right as delivered and refresh in Word with Ctrl+A, F9."""
import sys, os, re, json, copy, docx
from docx.shared import Pt, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
src, out = sys.argv[1], sys.argv[2]
PAGES = json.load(open(sys.argv[3])) if len(sys.argv) > 3 and os.path.exists(sys.argv[3]) else {}
d = docx.Document(src)
TW = 8505                                                           # 15 cm in twips
def rule(edge, sz):
    el = OxmlElement(f"w:{edge}"); el.set(qn("w:val"), "single"); el.set(qn("w:sz"), str(sz)); el.set(qn("w:space"), "0"); el.set(qn("w:color"), "000000"); return el
def run_fmt(p, size=None, bold=None):
    for r in p.runs:
        if size: r.font.size = Pt(size)
        if bold is not None: r.font.bold = bold
# equations: markers -> tabs
for p in d.paragraphs:
    if p.style.name.lower() == "equation":
        for r in p.runs:
            if "§T§" in r.text: r.text = r.text.replace("§T§", "\t")
# tables
for t in d.tables:
    n = len(t.columns); lens = [6] * n
    for row in t.rows:
        for i, c in enumerate(row.cells):
            if i < n:
                words = c.text.split() or [""]
                lens[i] = max(lens[i], min(len(c.text), 70) + 4, int(max(len(w) for w in words) * 1.5) + 4)
    tot = sum(lens); wid = [int(TW * x / tot) for x in lens]
    minw = [max((len(w) for row in t.rows for w in (row.cells[i].text.split() or [""])), default=4) * 95 + 180 for i in range(n)]
    deficit = 0
    for i in range(n):
        if wid[i] < minw[i]: deficit += minw[i] - wid[i]; wid[i] = minw[i]
    if deficit: big = max(range(n), key=lambda i: wid[i]); wid[big] -= deficit
    FS = 9
    if n >= 10: wid = [1500] + [(TW - 1500) // (n - 1)] * (n - 1); FS = 8      # a wide matrix (Prof. Kong's correlation table): 8 pt, fixed first column
    tblPr = t._tbl.tblPr
    for tag in ("w:tblBorders", "w:tblW", "w:tblLayout", "w:tblCellMar"):
        for old in tblPr.findall(qn(tag)): tblPr.remove(old)
    b = OxmlElement("w:tblBorders"); b.append(rule("top", 8)); b.append(rule("bottom", 8)); tblPr.append(b)
    w = OxmlElement("w:tblW"); w.set(qn("w:w"), str(TW)); w.set(qn("w:type"), "dxa"); tblPr.append(w)
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    mar = OxmlElement("w:tblCellMar")
    for edge, v in (("top", 30), ("left", 0), ("bottom", 30), ("right", 100)):
        e = OxmlElement(f"w:{edge}"); e.set(qn("w:w"), str(v)); e.set(qn("w:type"), "dxa"); mar.append(e)
    tblPr.append(mar)
    for i, gc in enumerate(t._tbl.tblGrid.findall(qn("w:gridCol"))): gc.set(qn("w:w"), str(wid[i]))
    for ri, row in enumerate(t.rows):
        trPr = row._tr.get_or_add_trPr(); trPr.append(OxmlElement("w:cantSplit"))
        if ri == 0: trPr.append(OxmlElement("w:tblHeader"))
        for ci, c in enumerate(row.cells):
            tcPr = c._tc.get_or_add_tcPr()
            for old in tcPr.findall(qn("w:tcW")): tcPr.remove(old)
            tw = OxmlElement("w:tcW"); tw.set(qn("w:w"), str(wid[ci])); tw.set(qn("w:type"), "dxa"); tcPr.insert(0, tw)
            if ri == 0:
                tb = OxmlElement("w:tcBorders"); tb.append(rule("bottom", 5)); tcPr.append(tb)
            for p in c.paragraphs:
                pf = p.paragraph_format; pf.alignment = WD_ALIGN_PARAGRAPH.LEFT; pf.space_before = Pt(0); pf.space_after = Pt(0)
                pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(11)
                run_fmt(p, FS, True if ri == 0 else None)
# panel labels (rows whose other cells are empty) span the whole table, as in a journal's variable table
for t in d.tables:
    for row in t.rows:
        cs = row.cells
        if len(cs) > 1 and cs[0].text.strip().startswith("Panel") and all(not c.text.strip() for c in cs[1:]):
            cs[0].merge(cs[-1])
            for pp_ in row.cells[0].paragraphs: pp_.paragraph_format.keep_with_next = True      # a panel label stays with its first row
# group headers over several columns (a header row such as "Variable | Group A | | | | Group B | | | |") span their columns, centred
for t in d.tables:
    r0 = t.rows[0].cells
    if len(r0) > 4 and r0[0].text.strip() == "Variable" and r0[1].text.strip() and not r0[2].text.strip():
        i = 1
        while i < len(r0):
            j = i + 1
            while j < len(r0) and not r0[j].text.strip(): j += 1
            if r0[i].text.strip() and j - i > 1:
                mc = r0[i].merge(r0[j - 1])
                for pp_ in mc.paragraphs: pp_.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            i = j
# keep tables from splitting badly: a table of up to 12 rows stays whole; a longer one keeps its first three rows and its last two together
for t in d.tables:
    rows = t.rows; nr = len(rows)
    keep = set(range(nr - 1)) if nr <= 12 else set([0, 1, 2, nr - 2])
    for ri in keep:
        for c in rows[ri].cells:
            for p in c.paragraphs: p.paragraph_format.keep_with_next = True
# "[Insert Table N about here]": centred, on its own line
for p in d.paragraphs:
    if p.style.name == "Insert Marker":
        pf = p.paragraph_format; pf.alignment = WD_ALIGN_PARAGRAPH.CENTER; pf.first_line_indent = Mm(0); pf.space_before = Pt(6); pf.space_after = Pt(6)
        pf.line_spacing_rule = WD_LINE_SPACING.SINGLE; pf.keep_together = True
# figures and tables after the References: each block starts on a new page (yzu_prep.py puts a "§PB§" paragraph before the block)
first_float = None
for p in list(d.paragraphs):
    if p.text.strip() == "§PB§":
        nxt = p._p.getnext()
        if nxt is not None and nxt.tag == qn("w:p"):
            docx.text.paragraph.Paragraph(nxt, d).paragraph_format.page_break_before = True
        if first_float is None: first_float = nxt
        p._p.getparent().remove(p._p)
# references: left-aligned with a hanging indent (justified text spreads the long web addresses into wide gaps)
in_refs = False
for p in d.paragraphs:
    if p._p is first_float: in_refs = False
    if p.style.name == "Heading 1": in_refs = (p.text.strip() == "References")
    elif in_refs and p.text.strip():
        pf = p.paragraph_format
        pf.alignment = WD_ALIGN_PARAGRAPH.LEFT; pf.left_indent = Mm(12.5); pf.first_line_indent = Mm(-12.5); pf.space_after = Pt(6)
# space after a table
for tbl in d.element.body.findall(qn("w:tbl")):
    nxt = tbl.getnext()
    if nxt is not None and nxt.tag == qn("w:p"):
        pp = docx.text.paragraph.Paragraph(nxt, d)
        if pp.style.name != "Table Note": pp.paragraph_format.space_before = Pt(8)
# captions: label bold
paras = d.paragraphs
for p in paras:
    sty = p.style.name
    if sty in ("Table Caption", "Figure Caption"):
        m = re.match(r"((?:Table|Figure) \d+\.)(.*)", p.text, flags=re.S)
        if m:
            for r in list(p.runs): r._r.getparent().remove(r._r)
            r1 = p.add_run(m.group(1)); r1.font.bold = True
            r2 = p.add_run(m.group(2)); r2.font.bold = False
            if sty == "Figure Caption": p.paragraph_format.keep_with_next = True      # the description below stays with its figure
# a table's title, its caption paragraph and its panel labels stay with the table they describe
for p in paras:
    if p.style.name == "Table Caption" or (p.style.name == "Table Note" and (p.text.startswith("This table") or p.text.startswith("Panel "))):
        p.paragraph_format.keep_with_next = True
# figures: at most 15 cm wide and 10 cm tall, centred, kept with the caption
for idx, p in enumerate(paras):
    if p._p.xpath(".//w:drawing"):
        for shp in p._p.xpath(".//wp:inline"):
            ext = shp.find(qn("wp:extent")); cx, cy = int(ext.get("cx")), int(ext.get("cy"))
            scale = min(Mm(150) / cx, Mm(100) / cy); cx, cy = int(cx * scale), int(cy * scale)
            ext.set("cx", str(cx)); ext.set("cy", str(cy))
            for e in shp.xpath(".//a:ext"): e.set("cx", str(cx)); e.set("cy", str(cy))
        pf = p.paragraph_format; pf.alignment = WD_ALIGN_PARAGRAPH.CENTER; pf.keep_with_next = True; pf.space_before = Pt(10); pf.space_after = Pt(0)
        pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
# paragraphs that name files are left-aligned (justified, the long file names stretch the word spacing); file names in Courier New
for st in d.styles:
    if st.name == "Verbatim Char":
        st.font.name = "Courier New"; st.font.size = Pt(10)
        rpr = st.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
        if rf is None: rf = OxmlElement("w:rFonts"); rpr.append(rf)
        for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"): rf.set(qn(a), "Courier New")
for p in d.paragraphs:
    if any(r.style is not None and r.style.name == "Verbatim Char" for r in p.runs):
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
# ---- fields: contents, list of tables, list of figures
body = d.element.body
def text_of(p): return "".join(t.text or "" for t in p.iter(qn("w:t")))
def mkrun(text=None, tab=False, fld=None, instr=None):
    r = OxmlElement("w:r")
    if fld: f = OxmlElement("w:fldChar"); f.set(qn("w:fldCharType"), fld); r.append(f)
    if instr:
        i = OxmlElement("w:instrText"); i.set(qn("xml:space"), "preserve"); i.text = instr; r.append(i)
    if tab: r.append(OxmlElement("w:tab"))
    if text is not None:
        t = OxmlElement("w:t"); t.set(qn("xml:space"), "preserve"); t.text = text; r.append(t)
    return r
def mkpara(style, text, page, first_instr=None, last=False):
    p = OxmlElement("w:p"); pPr = OxmlElement("w:pPr"); st = OxmlElement("w:pStyle"); st.set(qn("w:val"), style); pPr.append(st); p.append(pPr)
    if first_instr:
        p.append(mkrun(fld="begin")); p.append(mkrun(instr=first_instr)); p.append(mkrun(fld="separate"))
    p.append(mkrun(text)); p.append(mkrun(tab=True)); p.append(mkrun(str(page)))
    if last: p.append(mkrun(fld="end"))
    return p
def styleid(name):
    for s in d.styles:
        if s.name.lower() == name.lower(): return s.style_id
    raise KeyError(name)
def fill(slot_text, entries, instr, style_for):
    slot = next(p for p in body.iter(qn("w:p")) if text_of(p).strip() == slot_text)
    prev = slot
    for k, (lvl, text) in enumerate(entries):
        np_ = mkpara(styleid(style_for(lvl)), text, PAGES.get(text, "0"), instr if k == 0 else None, k == len(entries) - 1)
        prev.addnext(np_); prev = np_
    body.remove(slot)
heads, tcaps, fcaps = [], [], []
seen_main = False
for p in paras:
    sty = p.style.name
    if text_of(p._p).strip() == "§SECT§": seen_main = True
    if sty in ("Heading 1", "Heading 2") and seen_main: heads.append((1 if sty == "Heading 1" else 2, p.text.strip()))
    if sty == "Table Caption": tcaps.append((1, p.text.strip()))
    if sty == "Figure Caption": fcaps.append((1, p.text.strip()))
slot_toc = next(p for p in body.iter(qn("w:p")) if text_of(p).strip() == "§TOC§")
for title, key in ([("Title Page", "Title Page"), ("Abstract", "Abstract"), ("Table of Contents", "Table of Contents"), ("List of Tables", "List of Tables"), ("List of Figures", "List of Figures")]):
    pp = OxmlElement("w:p"); pPr = OxmlElement("w:pPr"); st = OxmlElement("w:pStyle"); st.set(qn("w:val"), styleid("toc 1")); pPr.append(st)
    rp = OxmlElement("w:rPr"); b = OxmlElement("w:b"); b.set(qn("w:val"), "0"); rp.append(b); pPr.append(rp); pp.append(pPr)
    pp.append(mkrun(title)); pp.append(mkrun(tab=True)); pp.append(mkrun(PAGES.get("front:" + key, "i")))
    for r_ in pp.findall(qn("w:r")):
        rp_ = OxmlElement("w:rPr"); b_ = OxmlElement("w:b"); b_.set(qn("w:val"), "0"); rp_.append(b_); r_.insert(0, rp_)
    slot_toc.addprevious(pp)
fill("§TOC§", heads, r'TOC \o "1-2" \u', lambda l: "toc 1" if l == 1 else "toc 2")
fill("§LOT§", tcaps, r'TOC \t "Table Caption,1"', lambda l: "table of figures")
fill("§LOF§", fcaps, r'TOC \t "Figure Caption,1"', lambda l: "table of figures")
# ---- two page-number sections: front matter in lower-case Roman numerals (title page not printed), main text in Arabic from 1
final = body.find(qn("w:sectPr"))
# the cover and the title page are sections of their own: no footer, and the margins of YZU's templates (3.17 cm at the sides, 2.54 cm above and below); the binding margin applies from the abstract on
def plain_section(sp):
    for ref in sp.findall(qn("w:footerReference")): sp.remove(ref)
    pm = sp.find(qn("w:pgMar"))
    for k, v in (("top", 1440), ("bottom", 1440), ("left", 1797), ("right", 1797), ("footer", 0)): pm.set(qn("w:" + k), str(v))
    return sp
for slot_text in ("§COVER§", "§TITLE§"):
    sl = next(p for p in body.iter(qn("w:p")) if text_of(p).strip() == slot_text)
    for ch in list(sl): sl.remove(ch)
    pp_ = OxmlElement("w:pPr"); pp_.append(plain_section(copy.deepcopy(final))); sl.insert(0, pp_)
def pgnum(sp, fmt, start=None):
    for old in sp.findall(qn("w:pgNumType")): sp.remove(old)
    e = OxmlElement("w:pgNumType"); e.set(qn("w:fmt"), fmt)
    if start is not None: e.set(qn("w:start"), str(start))
    # pgNumType goes after pgMar in the schema order
    pm = sp.find(qn("w:pgMar")); pm.addnext(e)
front = copy.deepcopy(final)
pgnum(front, "lowerRoman", 2)
pgnum(final, "decimal", 1)
slot = next(p for p in body.iter(qn("w:p")) if text_of(p).strip() == "§SECT§")
for ch in list(slot): slot.remove(ch)
pPr = OxmlElement("w:pPr"); pPr.append(front); slot.insert(0, pPr)
d.save(out + ".tmp")
d2 = docx.Document(out + ".tmp")
d2.save(out); os.remove(out + ".tmp")
print("wrote", out)
