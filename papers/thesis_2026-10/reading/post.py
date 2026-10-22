"""Post-processes the pandoc HTML before printing: keeps each figure on one page with its caption and note,
and keeps short tables (10 body rows or fewer, under about 1,500 characters) from splitting across pages. Also left-aligns paragraphs that quote file names (justified text spaces them unevenly). Edits the file in place."""
import re, sys
p = sys.argv[1]
h = open(p, encoding="utf-8").read()
h = re.sub(r'(<p><img [^>]*/></p>\s*<p class="fcap">.*?</p>(\s*<p class="note">.*?</p>)?)',
           r'<div class="figblock">\1</div>', h, flags=re.S)
def keep(m):
    t = m.group(0)
    return t.replace("<table", '<table class="keep"', 1) if t.count("<tr") <= 11 and len(re.sub(r"<[^>]+>", "", t)) < 1500 else t
h = re.sub(r"<table.*?</table>", keep, h, flags=re.S)
h = re.sub(r"<p>((?:(?!</p>).)*?<code>(?:(?!</p>).)*?)</p>", r'<p class="left">\1</p>', h, flags=re.S)
open(p, "w", encoding="utf-8").write(h)
