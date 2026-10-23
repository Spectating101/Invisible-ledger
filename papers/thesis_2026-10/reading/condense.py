"""Makes the compact reading copy read as a condensed thesis: removes what only the author needs while the work is unfinished. Reads Markdown
on stdin, writes it to stdout. Removes (1) the "Results slot" note and the closing line of 6.5, (2) the Outcome column of Table 6.2, which is
empty until the 2026 results arrive, (3) the author's note and the repeated title in the abstract. The chapter files are not changed."""
import re, sys
out, in_t62 = [], False
for ln in sys.stdin.read().split("\n"):
    if ln.startswith("> **[Results slot]**"):
        continue
    if ln.strip() == "The outcomes will be reported whatever their direction, as the other registered tests are.":
        continue
    if ln.startswith("*[Chinese abstract"):
        continue
    if ln.startswith("**The Invisible Ledger: Quantifying the Invisible Wedge"):
        continue
    if ln.startswith("| Prediction |") and ln.rstrip().endswith("| Outcome |"):
        in_t62 = True
    if in_t62 and ln.startswith("|"):
        cells = ln.strip().strip("|").split("|")[:-1]
        ln = "|" + "|".join(cells) + "|"
    elif in_t62:
        in_t62 = False
    out.append(ln)
sys.stdout.write(re.sub(r"\n{3,}", "\n\n", "\n".join(out)))
