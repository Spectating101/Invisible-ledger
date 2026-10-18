# Committed 8 Oct 2026 from the extraction workspace (identical in all 25 job folders, md5 6688cf94a1b5e9aca1f796c547c90053).
# Used to accept every extraction in tables/src/ (see the *_NOTES.txt files for each run).
"""Acceptance check for an extraction job. Run in the repo root: python3 check_rows.py extraction.csv MIN_ROWS
Every non-null row needs: source_file present in this folder, quote found verbatim in that file (whitespace-insensitive, case-insensitive),
and the stated value appearing as a number inside the quote (allowing million/billion/thousand rescaling)."""
import csv, pathlib, re, sys
def norm(s): return re.sub(r"\s+", " ", s.replace(" ", " ").replace("|", " ")).strip().lower()
def nums(t):
    out = set()
    for m in re.finditer(r"\(?-?\d[\d,\.]*\d|\d", t):
        raw = m.group(0).strip("(").replace(",", "")
        try: out.add(round(float(raw), 4))
        except ValueError: pass
    return out
def val_ok(v, quote):
    v = float(v); n = nums(quote); c = {round(v, 4), round(abs(v), 4)}
    for k in (1e3, 1e6, 1e9):
        c |= {round(v / k, 4), round(abs(v) / k, 4), round(v * k, 4), round(abs(v) * k, 4)}
    return any(x in n for x in c)
src, min_rows = sys.argv[1], int(sys.argv[2])
rows = list(csv.DictReader(open(src)))
need = {"entity", "period", "field", "value", "unit", "source_file", "quote", "note"}
assert rows and need <= set(rows[0].keys()), f"need columns {need}"
texts, bad, ok, nulls = {}, 0, 0, 0
for r in rows:
    if r["value"].strip() == "":
        nulls += 1; continue
    f = r["source_file"]
    if f not in texts:
        p = pathlib.Path(f)
        texts[f] = norm(p.read_text(errors="ignore")) if p.exists() else None
    if texts[f] is None: bad += 1; print("NO FILE", r["entity"], r["period"], r["field"], f); continue
    if norm(r["quote"]) not in texts[f]: bad += 1; print("QUOTE NOT IN FILE", r["entity"], r["period"], r["field"]); continue
    if not val_ok(r["value"], r["quote"]): bad += 1; print("VALUE NOT IN QUOTE", r["entity"], r["period"], r["field"], r["value"]); continue
    ok += 1
print(f"rows {len(rows)}: verified {ok}, null {nulls}, failed {bad}")
assert bad == 0 and ok >= min_rows, f"need zero failures and >= {min_rows} verified rows"
