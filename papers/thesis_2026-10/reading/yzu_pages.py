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
json.dump(result, open(out, "w"), indent=0, ensure_ascii=False)
print(f"front matter {first} pages; {len(result)} of {len(json.load(open(out + '.want')))} entries placed")
