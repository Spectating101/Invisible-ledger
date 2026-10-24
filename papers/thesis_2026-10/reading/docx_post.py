"""Finishes the condensed Word copy so that it looks like the compact PDF. Usage: python3 docx_post.py in.docx out.docx
Tables: three rules (1.2 px top and bottom, 0.6 px under the header), 8 pt text, column widths from the content, header repeated across pages, rows kept whole.
Captions: label in bold, 8.8 pt, kept with the table; figure captions 8.4 pt; notes 7.8 pt. Figures: 50 mm tall (84 mm for Figures 3.1 and 5.3). Equations: the markers
become the tabs that centre the formula and put the number at the right margin. Then Source Serif 4 is embedded (docx_fonts/, SIL Open Font License, unmodified)."""
import sys, os, re, uuid, zipfile, shutil, docx
from docx.shared import Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
src, out = sys.argv[1], sys.argv[2]
tmp = out + ".tmp.docx"
d = docx.Document(src)
HERE = os.path.dirname(os.path.abspath(__file__))
def rule(edge, sz):
    el = OxmlElement(f"w:{edge}"); el.set(qn("w:val"), "single"); el.set(qn("w:sz"), str(sz)); el.set(qn("w:space"), "0"); el.set(qn("w:color"), "111111"); return el
def fmt(p, size, before=0, after=0, line=None, color=None, align=WD_ALIGN_PARAGRAPH.LEFT):
    pf = p.paragraph_format; pf.alignment = align; pf.space_before = Pt(before); pf.space_after = Pt(after)
    if line: pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(line)
    for r in p.runs:
        r.font.size = Pt(size)
        if color: r.font.color.rgb = RGBColor.from_string(color)
TEXT_TW = 10200                                                   # 180 mm in twips
# tables
for t in d.tables:
    n = len(t.columns); lens = [8] * n
    for row in t.rows:
        for i, c in enumerate(row.cells):
            if i < n:
                words = c.text.split() or [""]
                lens[i] = max(lens[i], min(len(c.text), 70) + 6, int(max(len(w) for w in words) * 1.7) + 6)
    tot = sum(lens); wid = [int(TEXT_TW * x / tot) for x in lens]
    # no column narrower than its longest word at 8 pt bold (about 100 twips a character plus the cell margin); the widest column pays
    minw = []
    for i in range(n):
        longest = max((len(w) for row in t.rows for w in (row.cells[i].text.split() or [""])), default=4)
        minw.append(longest * 100 + 200)
    deficit = 0
    for i in range(n):
        if wid[i] < minw[i]: deficit += minw[i] - wid[i]; wid[i] = minw[i]
    if deficit:
        big = max(range(n), key=lambda i: wid[i]); wid[big] -= deficit
    tblPr = t._tbl.tblPr
    for tag in ("w:tblBorders", "w:tblW", "w:tblLayout", "w:tblCellMar"):
        for old in tblPr.findall(qn(tag)): tblPr.remove(old)
    b = OxmlElement("w:tblBorders"); b.append(rule("top", 7)); b.append(rule("bottom", 7)); tblPr.append(b)
    w = OxmlElement("w:tblW"); w.set(qn("w:w"), str(TEXT_TW)); w.set(qn("w:type"), "dxa"); tblPr.append(w)
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    mar = OxmlElement("w:tblCellMar")
    for edge, v in (("top", 24), ("left", 0), ("bottom", 24), ("right", 90)):
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
                tb = OxmlElement("w:tcBorders"); tb.append(rule("bottom", 4)); tcPr.append(tb)
            for p in c.paragraphs:
                fmt(p, 8, 0, 0, 10.0)
                if ri == 0:
                    for r in p.runs: r.font.bold = True
# a little space between a table and the paragraph that follows it (the PDF has a 5.7 pt margin there)
body = d.element.body
for tbl in body.findall(qn("w:tbl")):
    nxt = tbl.getnext()
    if nxt is not None and nxt.tag == qn("w:p"):
        pp = docx.text.paragraph.Paragraph(nxt, d)
        if not pp.text.strip().startswith(("Note:", "*Implied")): pp.paragraph_format.space_before = Pt(5.7)
# captions, notes, figures
paras = d.paragraphs
for idx, p in enumerate(paras):
    txt = p.text.strip()
    if re.match(r"Table \d\.\d+\.", txt) and len(txt) < 400:                   # label bold, title plain
        label = re.match(r"(Table \d\.\d+\.)", txt).group(1); rest = txt[len(label):]
        for r in list(p.runs): r._r.getparent().remove(r._r)
        r1 = p.add_run(label); r1.font.bold = True
        r2 = p.add_run(rest); r2.font.bold = False
        fmt(p, 8.8, 7, 2.8, 12.3); p.paragraph_format.keep_with_next = True
    elif re.match(r"Figure \d\.\d+\.", txt):
        fmt(p, 8.4, 2.8, 8.5, 11.8)
    elif txt.startswith("Note:") or txt.startswith("*Implied"):
        fmt(p, 7.8, 2.8, 8.5, 10.9, "333333")
    if p._p.xpath(".//w:drawing"):
        nxt = paras[idx + 1].text.strip() if idx + 1 < len(paras) else ""
        big = nxt.startswith("Figure 3.1.") or nxt.startswith("Figure 5.3.")
        hmax = Mm(84 if big else 50)
        for shp in p._p.xpath(".//wp:inline"):
            ext = shp.find(qn("wp:extent")); cx, cy = int(ext.get("cx")), int(ext.get("cy"))
            scale = min(hmax / cy, Mm(180) / cx); cx, cy = int(cx * scale), int(cy * scale)
            ext.set("cx", str(cx)); ext.set("cy", str(cy))
            for e in shp.xpath(".//a:ext"): e.set("cx", str(cx)); e.set("cy", str(cy))
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(5.7); p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
# Greek letters are not in the embedded Latin files; give them a serif font of their own so they do not fall back to a sans face
import copy
GREEK = re.compile("([\u0370-\u03ff]+)")
def split_greek(par):
    for r in list(par.runs):
        t = r.text
        if not GREEK.search(t): continue
        parts = [x for x in GREEK.split(t) if x]
        anchor = r._r
        for k, part in enumerate(parts):
            new = copy.deepcopy(r._r)
            for tx in new.findall(qn("w:t")): new.remove(tx)
            tt = OxmlElement("w:t"); tt.text = part; tt.set(qn("xml:space"), "preserve"); new.append(tt)
            if GREEK.fullmatch(part):
                rPr = new.get_or_add_rPr(); rf = rPr.find(qn("w:rFonts"))
                if rf is None: rf = OxmlElement("w:rFonts"); rPr.insert(0, rf)
                for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"): rf.set(qn(a), "Cambria")
            anchor.addnext(new); anchor = new
        r._r.getparent().remove(r._r)
for par in d.paragraphs: split_greek(par)
for t in d.tables:
    for row in t.rows:
        for c in row.cells:
            for par in c.paragraphs: split_greek(par)
# equations: markers -> tabs (after the Greek split, so a tab never travels inside a split run)
for p in d.paragraphs:
    if p.style.name.lower() == "equation":
        for r in p.runs:
            if "§T§" in r.text: r.text = r.text.replace("§T§", "\t")
d.save(tmp)
# embed Source Serif 4 (obfuscated TrueType parts, as Word stores embedded fonts)
STY = [("Regular", "embedRegular"), ("Bold", "embedBold"), ("Italic", "embedItalic"), ("BoldItalic", "embedBoldItalic")]
def obfuscate(data, guid):
    key = bytes.fromhex(guid.strip("{}").replace("-", ""))[::-1]
    b = bytearray(data)
    for i in range(32): b[i] ^= key[i % 16]
    return bytes(b)
zin = zipfile.ZipFile(tmp); zout = zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED)
guids = {k: "{" + str(uuid.uuid4()).upper() + "}" for k, _ in STY}
for item in zin.infolist():
    data = zin.read(item.filename)
    if item.filename == "[Content_Types].xml":
        data = data.decode().replace("<Default Extension=\"png\"", "<Default Extension=\"odttf\" ContentType=\"application/vnd.openxmlformats-officedocument.obfuscatedFont\"/><Default Extension=\"png\"", 1).encode()
    elif item.filename == "word/settings.xml":
        data = re.sub(r"(<w:settings[^>]*>)", r"\1<w:embedTrueTypeFonts/><w:saveSubsetFonts/>", data.decode(), count=1).encode()
    elif item.filename == "word/fontTable.xml":
        s = data.decode()
        emb = "".join(f'<w:{tag} r:id="rIdF{i+1}" w:fontKey="{guids[k]}"/>' for i, (k, tag) in enumerate(STY))
        font = ('<w:font w:name="Source Serif 4"><w:altName w:val="Cambria"/><w:charset w:val="00"/><w:family w:val="roman"/><w:pitch w:val="variable"/>' + emb + '</w:font>')
        s = re.sub(r"(<w:fonts[^>]*>)", lambda m: m.group(1) + font, s, count=1)
        data = s.encode()
    zout.writestr(item, data)
rels = "".join(f'<Relationship Id="rIdF{i+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/font" Target="fonts/font{i+1}.odttf"/>' for i in range(4))
zout.writestr("word/_rels/fontTable.xml.rels", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' + rels + "</Relationships>")
for i, (k, _) in enumerate(STY):
    zout.writestr(f"word/fonts/font{i+1}.odttf", obfuscate(open(os.path.join(HERE, "docx_fonts", f"SourceSerif4-{k}.ttf"), "rb").read(), guids[k]))
zout.close(); zin.close(); os.remove(tmp)
print("wrote", out)
