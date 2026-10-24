"""First pass of the YZU build: finds the printed page number of every heading and caption in a converted PDF. Usage: python3 yzu_pages.py in.pdf out.json
Front matter ends on the page before Chapter 1; printed numbers are Arabic from Chapter 1 (page 1)."""
import json, re, subprocess, sys
pdf, out = sys.argv[1], sys.argv[2]
n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
pages = [subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", pdf, "-"], capture_output=True, text=True).stdout for i in range(1, n + 1)]
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("“", '"').replace("”", '"')).strip()
lines = [[norm(l) for l in p.splitlines() if l.strip()] for p in pages]
first = next(i for i, ls in enumerate(lines) if any(l == "Chapter 1 Introduction" for l in ls) and not any(re.search(r"\.{4,}", l) for l in ls))
json.dump({"front_pages": first, "total": n}, open(out + ".meta", "w"))
entries = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else None
result = {}
for e in json.load(open(out + ".want")):
    key = norm(e)[:42]
    for i in range(first, n):
        if any(l.startswith(key) for l in lines[i]): result[e] = i - first + 1; break
# front-matter entries: Roman numerals, counted from the title page (the cover is not numbered)
def roman(k):
    vals = [(10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]; r = ""
    for v, sym in vals:
        while k >= v: r += sym; k -= v
    return r
front = {"Title Page": 1}
for title, key in (("ABSTRACT", "Abstract"), ("Contents", "Table of Contents"), ("List of Tables", "List of Tables"), ("List of Figures", "List of Figures"), ("Symbols and Abbreviations", "Symbols and Abbreviations")):
    for i in range(0, first):
        if title in lines[i][:8] and (title == "ABSTRACT" or lines[i][0] == title): front[key] = i; break   # physical page i+1; the title page is physical page 2 = i
for key, k in front.items(): result["front:" + key] = roman(k) if key != "Title Page" else "i"
json.dump(result, open(out, "w"), indent=0, ensure_ascii=False)
print(f"front matter {first} pages; {len(result)} of {len(json.load(open(out + '.want')))} entries placed")
