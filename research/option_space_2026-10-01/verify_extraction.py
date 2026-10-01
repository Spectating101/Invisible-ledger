"""Verify an LLM-extracted quarterly table against its source text (1 Oct 2026).

Input: a JSONL file with keys quarter, field, value, unit, file, quote (one value per line).
A row is VERIFIED only if (1) the named file exists in the corpus folder, (2) the quote appears in that file after
whitespace normalisation, and (3) the number appears in the quote (any common formatting: 1,234 / 1.234 / $1.2 billion
= 1,200 million). Anything else is UNVERIFIED and must be checked by hand before it is used.

Usage: python3 verify_extraction.py <extraction.jsonl> <corpus_dir> <out_prefix>
Writes <out_prefix>_verified.csv (all rows with status) and <out_prefix>_wide.csv (verified values, quarter x field).
"""
import json
import pathlib
import re
import sys

import pandas as pd


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace(" ", " ").replace("|", " ")).strip().lower()


def numbers_in(text: str) -> set:
    out = set()
    for m in re.finditer(r"-?\d[\d,]*\.?\d*", text):
        raw = m.group(0).replace(",", "")
        try:
            out.add(round(float(raw), 4))
        except ValueError:
            pass
    return out


def number_matches(value, quote: str) -> bool:
    if value is None:
        return True
    try:
        v = float(value)
    except (TypeError, ValueError):
        return False
    nums = numbers_in(quote)
    cands = {round(v, 4), round(abs(v), 4)}
    if abs(v) >= 1:
        cands |= {round(v / 1000, 4), round(v * 1000, 4)}  # million vs billion / trillion phrasing
    return any(c in nums for c in cands)


def main(src, corpus, prefix):
    corpus = pathlib.Path(corpus)
    texts = {p.name: norm(p.read_text(errors="ignore")) for p in corpus.glob("*.txt")}
    rows = []
    for line in pathlib.Path(src).read_text().splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            continue
        f, q = r.get("file", ""), r.get("quote") or ""
        if r.get("value") is None and r.get("field") != "note":
            r["status"] = "NULL (not stated)"
        elif f not in texts:
            r["status"] = "UNVERIFIED: file not found"
        elif norm(q) not in texts[f]:
            r["status"] = "UNVERIFIED: quote not in file"
        elif r.get("field") != "note" and not number_matches(r.get("value"), q):
            r["status"] = "UNVERIFIED: number not in quote"
        else:
            r["status"] = "VERIFIED"
        rows.append(r)
    df = pd.DataFrame(rows)
    df.to_csv(f"{prefix}_verified.csv", index=False)
    print(df.status.value_counts().to_string())
    ok = df[(df.status == "VERIFIED") & (df.field != "note")]
    wide = ok.pivot_table(index="quarter", columns="field", values="value", aggfunc="first")
    wide.to_csv(f"{prefix}_wide.csv")
    print(f"\nverified cells: {wide.notna().sum().sum()} across {wide.shape[0]} quarters x {wide.shape[1]} fields")


if __name__ == "__main__":
    main(*sys.argv[1:4])
