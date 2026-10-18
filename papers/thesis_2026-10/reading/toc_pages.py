"""Second pass of the reading-copy build: finds the page of each heading in a first-pass PDF and writes the page numbers,
with dotted leaders, into the contents list of the HTML. Usage: python3 toc_pages.py first_pass.pdf reading.tmp.html"""
import html, re, subprocess, sys
pdf, page_html = sys.argv[1], sys.argv[2]
n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
pages = [subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), pdf, "-"], capture_output=True, text=True).stdout for i in range(1, n + 1)]
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'")).strip()
lines = [[norm(l) for l in p.splitlines() if l.strip()] for p in pages]
h = open(page_html, encoding="utf-8").read()
# contents pages: early pages listing at least four numbered sections
toc_end = max(i for i in range(min(6, n)) if sum(bool(re.match(r"^\d\.\d+ ", l)) for l in lines[i]) >= 4) + 1
def page_of(title):
    key = norm(html.unescape(re.sub(r"<[^>]+>", "", title)))[:40]
    for i in range(toc_end, n):
        if any(l.startswith(key) for l in lines[i]):
            return i + 1
    return None
missing = []
def fill(m):
    title = m.group(2)
    pg = page_of(title)
    if pg is None:
        missing.append(title); pg = ""
    return f'{m.group(1)}<span class="t">{title}</span><span class="lead"></span><span class="pg">{pg}</span></a>'
nav = re.search(r'<nav id="TOC".*?</nav>', h, flags=re.S).group(0)
new_nav = re.sub(r'(<a href="#[^"]*"[^>]*>)(.*?)</a>', fill, nav, flags=re.S)
open(page_html, "w", encoding="utf-8").write(h.replace(nav, new_nav))
if missing:
    print("no page found for:", missing)
