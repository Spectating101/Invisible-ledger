"""Markdown for the condensed Word copy: reads the raw chapter files named on the command line and writes one Markdown stream to stdout.
Equations become centred paragraphs (style Equation, number at the right margin; plain text with real subscripts, so they show in every Word), subscripts in running text become subscripts, figure alt text is dropped so each caption prints once.
The notes and placeholders are removed by condense.py and the key sentences are bolded by boldkey.py, as in the condensed PDF (see build_condensed_docx.sh)."""
import re, sys
def sub(e):
    e = e.replace("β_V", "β~V~").replace("β_m", "β~m~")
    e = re.sub(r"_(i,t−1|it|t)\b", lambda m: "~" + m.group(1) + "~", e)
    return re.sub(r"\s{2,}", " ", e.strip())
def eq(m):
    body = sub(m.group(1)).replace("year effect", "year effect")
    return '\n::: {custom-style="Equation"}\n§T§' + body + "§T§(" + m.group(2) + ")\n:::\n"
t = sys.stdin.read()
t = re.sub(r"```\n(.+?)\s+\((\d+)\)\s*\n```", eq, t)
t = re.sub(r"^!\[[^]]*\]\(", "![](", t, flags=re.M)
t = t.replace("β_V", "β~V~").replace("β_m", "β~m~")
t = re.sub(r"(?<![A-Za-z0-9_/.`])([A-Za-z])_(it|t|i,t−1)(?![A-Za-z0-9_])", r"\1~\2~", t)
sys.stdout.write(t)
