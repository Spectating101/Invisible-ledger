"""Markdown for the YZU-layout Word copy: reads the concatenated chapter text on stdin, writes Markdown to stdout.
Changes made only in this build (the chapter files keep their chapter-based numbers): tables and figures are numbered 1, 2, 3 through the whole thesis
(YZU guideline III.2), in the order they appear, and every mention in the text follows; chapter titles read "Chapter 1 Introduction" (YZU's English template);
the abstract becomes an unnumbered front-matter pages; captions and notes get their own paragraph styles (a figure's title is the caption, its
description is the note below it)."""
import re, sys
t = sys.stdin.read()
tabs = re.findall(r"^\*\*Table (\d\.\d+)\.", t, flags=re.M); figs = re.findall(r"^\*\*Figure (\d\.\d+)\.", t, flags=re.M)
tmap = {k: str(i + 1) for i, k in enumerate(tabs)}; fmap = {k: str(i + 1) for i, k in enumerate(figs)}
def sub_refs(text):
    def one(kind, mp):
        def f(m):
            a = m.group(2); b = m.group(4)
            s = m.group(1) + mp.get(a, a)
            if b: s += m.group(3) + mp.get(b, b)
            return s
        return f
    text = re.sub(r"(Tables? )(\d\.\d+)(?!\d)( (?:and|to) )?(\d\.\d+)?(?!\d)" , lambda m: (m.group(1) + tmap.get(m.group(2), m.group(2)) + ((m.group(3) or "") + tmap.get(m.group(4), m.group(4)) if m.group(4) else (m.group(3) or ""))), text)
    text = re.sub(r"(Figures? )(\d\.\d+)(?!\d)( (?:and|to) )?(\d\.\d+)?(?!\d)", lambda m: (m.group(1) + fmap.get(m.group(2), m.group(2)) + ((m.group(3) or "") + fmap.get(m.group(4), m.group(4)) if m.group(4) else (m.group(3) or ""))), text)
    return text
t = sub_refs(t)
t = t.replace("](figures/", "](figures_yzu/")        # the six figures lettered in Times New Roman (see figures/make_figures.py, FIG_FONT)
t = re.sub(r"^# Chapter (\d)\. ", r"# Chapter \1 ", t, flags=re.M)
# the English abstract in YZU's layout (template A6): title, student and advisor, the submission block, then ABSTRACT
m = re.search(r"^# Abstract\s*\n(?:\s*\*\*(.*?)\*\*\s*\n)?", t, flags=re.M)
if m:
    hdr = ('::: {custom-style="Abstract Title"}\nThe Invisible Ledger: Quantifying the Invisible Wedge in Indonesia\u2019s Platform Economy\n:::\n\n'
           '::: {custom-style="Abstract Head"}\nStudent: Christopher Ongko  \u3000 Advisor: Dr. De-Rong Kong\n:::\n\n'
           '::: {custom-style="Abstract Head"}\nSubmitted to MS Program in Finance and Accounting\n:::\n\n'
           '::: {custom-style="Abstract Head"}\nCollege of Management, Yuan Ze University\n:::\n\n'
           '::: {custom-style="Abstract Label"}\nABSTRACT\n:::\n')
    t = t[:m.start()] + hdr + t[m.end():]
t = re.sub(r"^# (Abstract)\s*$", r'::: {custom-style="Front Heading"}\n\1\n:::', t, flags=re.M)
# figures, then tables, after the References, each on its own page, with "[Insert Table N about here]" after the paragraph of its chapter that first
# mentions it (Prof. Kong, 24 Oct; her sample draft). The Appendices follow them, as in her sample. A block is the title, the "This table" paragraph,
# panel labels, the table(s) and the note; a figure block is the image and its caption.
def mentions(p):
    s = set()
    for m in re.finditer(r"\b(Tables?|Figures?) (\d+(?:(?:, | and | to | & )\d+)*)", p):
        kind = "Table" if m.group(1).startswith("T") else "Figure"; nums = re.findall(r"\d+", m.group(2))
        if " to " in m.group(2) and len(nums) == 2: nums = [str(k) for k in range(int(nums[0]), int(nums[1]) + 1)]
        s |= {(kind, int(n)) for n in nums}
    return s
def floats_to_end(t):
    paras = t.split("\n\n")
    ref = next((i for i, p in enumerate(paras) if p.startswith("# References")), None)
    if ref is None: return t
    keep, blocks, order, i = [], {}, [], 0
    while i < ref:
        p = paras[i]; mt = re.match(r"^\*\*Table (\d+)\.", p); mf = re.match(r"^!\[[^\]]*\]\(figures", p)
        if mt:
            blk, j = [p], i + 1
            while j < ref:
                q = paras[j]
                if q.startswith("This table ") or re.match(r"^\*Panel [A-Z]\. ", q) or q.startswith("|"): blk.append(q); j += 1
                elif q.startswith("*Note:*"): blk.append(q); j += 1; break
                else: break
            key = ("Table", int(mt.group(1)))
        elif mf and i + 1 < ref and re.match(r"^\*\*Figure (\d+)\.", paras[i + 1]):
            blk, j = [p, paras[i + 1]], i + 2; key = ("Figure", int(re.match(r"^\*\*Figure (\d+)\.", paras[i + 1]).group(1)))
        else:
            keep.append(p); i += 1; continue
        blocks[key] = blk; order.append((key, len(keep))); i = j
    marks = {}
    for key, pos in order:
        lo = max([k for k in range(min(pos, len(keep))) if keep[k].startswith("# Chapter")] or [0])
        hi = next((k for k in range(lo + 1, len(keep)) if keep[k].startswith("# ")), len(keep))
        at = next((k for k in range(lo, hi) if not keep[k].startswith(("#", "|", ":::")) and key in mentions(keep[k])), pos - 1)
        marks.setdefault(at, []).append('::: {custom-style="Insert Marker"}\n[Insert %s %d about here]\n:::' % key)
    body = []
    for k, p in enumerate(keep):
        body.append(p); body += marks.get(k, [])
    pb = '::: {custom-style="Page Start"}\n§PB§\n:::'
    floats = [x for kind in ("Figure", "Table") for key in sorted(k for k in blocks if k[0] == kind) for x in [pb] + blocks[key]]
    app = next((i for i in range(ref, len(paras)) if paras[i].startswith("# Appendices")), len(paras))
    return "\n\n".join(body + paras[ref:app] + floats + paras[app:])
t = floats_to_end(t)
t = re.sub(r"^\*\*(Table \d+\.) (.*?)\*\*\s*$", r'::: {custom-style="Table Caption"}\n\1 \2\n:::', t, flags=re.M)
# the caption of a table explains how to read it (Prof. Kong, 24 Oct): a paragraph that starts "This table" sits under the title, above the table; panel labels likewise
t = re.sub(r"^(This table [^\n]+)$", r'::: {custom-style="Table Note"}\n\1\n:::', t, flags=re.M)
t = re.sub(r"^\*(Panel [A-Z]\. [^*\n]+)\*\s*$", r'::: {custom-style="Table Note"}\n*\1*\n:::', t, flags=re.M)
def fig(m):
    title = m.group(2).strip(); rest = m.group(3).strip()
    out = '::: {custom-style="Figure Caption"}\n' + m.group(1) + " " + title + "\n:::\n"
    if rest: out += '\n::: {custom-style="Table Note"}\n' + rest + "\n:::"
    return out
t = re.sub(r"^\*\*(Figure \d+\.) ([^*]*)\*\*(.*)$", fig, t, flags=re.M)
t = re.sub(r"^\*Note:\*(.*)$", lambda m: '::: {custom-style="Table Note"}\n*Note:*' + m.group(1) + "\n:::", t, flags=re.M)
sys.stdout.write(t)
