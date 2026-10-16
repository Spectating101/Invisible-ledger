"""Turns the chapter Markdown into print-ready Markdown: equations as centred blocks with real subscripts, caption and note
paragraphs tagged for styling, figure alt text dropped so captions print once. Reads files named on the command line, writes stdout."""
import re, sys, html
def sub(expr):
    expr = html.escape(expr)
    return re.sub(r"_((?:i,t−1)|[A-Za-z0-9]+)", r"<sub>\1</sub>", expr)
def eq(m):
    body, no = m.group(1).rstrip(), m.group(2)
    return f'<div class="eq"><span class="eq-body">{sub(body)}</span><span class="eq-no">{no}</span></div>'
out = []
for f in sys.argv[1:]:
    t = open(f, encoding="utf-8").read()
    t = re.sub(r"```\n(.+?)\s+(\(\d+\))\s*\n```", eq, t)
    t = re.sub(r"^!\[[^]]*\]\(", "![](", t, flags=re.M)
    t = t.replace("β_V", "β<sub>V</sub>").replace("β_m", "β<sub>m</sub>")
    t = re.sub(r"(?<![A-Za-z0-9_/.`])([A-Za-z])_(it|t|i,t−1)(?![A-Za-z0-9_])", r"\1<sub>\2</sub>", t)
    t = re.sub(r"^\*\*(Table [0-9A-Z.]+\.)\s*(.*?)\*\*\s*$", r'<p class="tcap"><span class="lbl">\1</span> \2</p>', t, flags=re.M)
    t = re.sub(r"^\*\*(Figure [0-9.]+\.[^*]*)\*\*(.*)$", lambda m: f'<p class="fcap"><strong>{m.group(1)}</strong>{m.group(2)}</p>', t, flags=re.M)
    t = re.sub(r"^\*Note:\*(.*)$", lambda m: f'<p class="note"><em>Note:</em>{m.group(1)}</p>', t, flags=re.M)
    out.append(t.rstrip() + "\n\n")
sys.stdout.write("".join(out))
