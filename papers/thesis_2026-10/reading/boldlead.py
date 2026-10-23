"""Bolds the first sentence of each prose paragraph, for the compact reading copy only. Reads Markdown on stdin, writes it to stdout.
Skips tables, headings, figures, captions, notes, block quotes, numbered lists, one-sentence paragraphs and paragraphs that start in lower case (the "where…" lines under an equation). A first sentence over 45 words
(citations not counted) is left plain, because a long bold sentence stops guiding the eye. The thesis text itself is never changed."""
import re, sys
SKIP = ("|", "#", "!", "<", "```", "**", "*Note", ">")
ABBR = ("al", "e.g", "i.e", "vs", "etc", "approx")
def first_sentence_end(p):
    depth = 0
    for i, c in enumerate(p):
        if c == "(":
            depth += 1
        elif c == ")":
            depth = max(0, depth - 1)
        elif c == "." and depth == 0 and i + 2 < len(p) and p[i + 1] == " " and p[i + 2].isupper():
            w = re.findall(r"[A-Za-z.]+$", p[:i])
            if w and w[-1].lower().rstrip(".") in ABBR:
                continue
            if i < 25:
                continue
            return i + 1
    return None
out = []
for ln in sys.stdin.read().split("\n"):
    if ln.strip() and not ln.startswith(SKIP) and not re.match(r"\s*\d+\.\s", ln) and not ln.startswith("  ") and not ln[0].islower():
        e = first_sentence_end(ln)
        if e and len(re.sub(r"\([^()]*\d{4}[^()]*\)", "", ln[:e]).split()) <= 45:
            ln = "**" + ln[:e] + "**" + ln[e:]
    out.append(ln)
sys.stdout.write("\n".join(out))
