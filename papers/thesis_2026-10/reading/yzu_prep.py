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
t = re.sub(r"^\*\*(Table \d+\.) (.*?)\*\*\s*$", r'::: {custom-style="Table Caption"}\n\1 \2\n:::', t, flags=re.M)
def fig(m):
    title = m.group(2).strip(); rest = m.group(3).strip()
    out = '::: {custom-style="Figure Caption"}\n' + m.group(1) + " " + title + "\n:::\n"
    if rest: out += '\n::: {custom-style="Table Note"}\n' + rest + "\n:::"
    return out
t = re.sub(r"^\*\*(Figure \d+\.) ([^*]*)\*\*(.*)$", fig, t, flags=re.M)
t = re.sub(r"^\*Note:\*(.*)$", lambda m: '::: {custom-style="Table Note"}\n*Note:*' + m.group(1) + "\n:::", t, flags=re.M)
sys.stdout.write(t)
