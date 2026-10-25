"""Before-and-after preview of the thesis text (25 Oct 2026). Run from the repository root:
    python3 papers/thesis_2026-10/reading/build_preview.py [BASE_COMMIT]
Writes papers/thesis_2026-10/PREVIEW_BEFORE_AFTER.md. BEFORE is the text at BASE_COMMIT (default a1f1af2: the thesis as sent to Prof. Kong on 24 Oct,
with her Chapter 1 edits already ported); AFTER is the working tree. Every changed paragraph is shown with its old and new wording; inside the new
wording, ~~struck~~ words were deleted and **bold** words were added. New and removed paragraphs are labelled. Tables are abbreviated."""
import difflib, os, re, subprocess, sys

BASE = sys.argv[1] if len(sys.argv) > 1 else "a1f1af2"
T = "papers/thesis_2026-10/"
FILES = [("Abstract", "abstract.md"), ("Chapter 1. Introduction", "ch1_introduction.md"), ("Chapter 2. Literature review", "ch2_literature.md"),
         ("Chapter 3. Framework and hypotheses", "ch3_framework.md"), ("Chapter 4. Data and methods", "ch4_data_methods.md"),
         ("Chapter 5. Results", "ch5_results.md"), ("Chapter 6. Discussion and policy implications", "drafts/ch6_draft_2026-10-14.md"),
         ("Chapter 7. Conclusion", "drafts/ch7_draft_2026-10-14.md")]

def before(path):
    r = subprocess.run(["git", "show", f"{BASE}:{T}{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""
def after(path): return open(T + path, encoding="utf8").read()

def sections(text):
    """[(key, heading, [blocks])]; key is the section number, or '0' for the text before the first ## heading."""
    parts = re.split(r"^(## .*)$", text, flags=re.M); out = [("0", parts[0].strip().split("\n")[0] if parts[0].strip().startswith("#") else "", parts[0])]
    for i in range(1, len(parts), 2):
        h = parts[i]; m = re.match(r"## (\d+\.\d+|Appendix [A-E])", h)
        out.append((m.group(1) if m else h, h[3:], parts[i + 1]))
    return [(k, h, [b.strip() for b in re.split(r"\n\s*\n", body) if b.strip()]) for k, h, body in out]

words = lambda s: re.findall(r"\S+", s)
def ratio(a, b): return difflib.SequenceMatcher(None, words(a), words(b), autojunk=False).ratio()
def tok(s): return re.findall(r"\n|\S+", s)
def marked(a, b):
    wa, wb = tok(a), tok(b); out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, wa, wb, autojunk=False).get_opcodes():
        if op == "equal": out.append(" ".join(wb[j1:j2]))
        else:
            if i2 > i1: out.append("~~" + " ".join(wa[i1:i2]).replace("~~", "") + "~~")
            if j2 > j1: out.append("**" + " ".join(wb[j1:j2]).replace("**", "") + "**")
    return re.sub(r" ?\n ?", "\n", " ".join(out))
def quote(b, kind=None):
    lines = b.split("\n")
    if b.lstrip().startswith("|") and len(lines) > 4: lines = lines[:3] + [f"… (table of {len(lines) - 2} rows)"]
    return "\n".join("> " + l for l in lines)

def diff_blocks(a, b):
    out = []; sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal": continue
        A, B = a[i1:i2], b[j1:j2]; used = set(); pairs = {}
        for j, nb in enumerate(B):
            best, bi = 0.0, None
            for i, na in enumerate(A):
                if i in used or na.lstrip().startswith("|") != nb.lstrip().startswith("|"): continue
                r = ratio(na, nb)
                if r > best: best, bi = r, i
            if bi is not None and best >= 0.45: pairs[j] = bi; used.add(bi)
        placed_removed = set()
        for j, nb in enumerate(B):
            if j in pairs:
                i = pairs[j]
                for ri in range(len(A)):                      # removed paragraphs that sat before this one
                    if ri < i and ri not in used and ri not in placed_removed: out.append(("REMOVED", A[ri], None)); placed_removed.add(ri)
                out.append(("CHANGED", A[i], nb))
            else: out.append(("NEW", None, nb))
        for ri in range(len(A)):
            if ri not in used and ri not in placed_removed: out.append(("REMOVED", A[ri], None))
    return out

md = []
stats = {"CHANGED": 0, "NEW": 0, "REMOVED": 0}
for title, path in FILES:
    sb, sa = {k: (h, bl) for k, h, bl in sections(before(path))}, {k: (h, bl) for k, h, bl in sections(after(path))}
    keys = [k for k in list(sa) + [k for k in sb if k not in sa]]
    body = []
    for k in keys:
        hb, bb = sb.get(k, ("", [])); ha, ba = sa.get(k, ("", []))
        ch = diff_blocks(bb, ba)
        if not ch and hb == ha: continue
        label = re.sub(r"^# ", "", ha or hb) + " (opening)" if k == "0" else (ha or hb)
        sec = [f"### {label}" + (f"   *(was: {hb})*" if hb and ha and hb != ha else "") + ("   *(section removed)*" if k not in sa else "") + ("   *(new section)*" if k not in sb else ""), ""]
        for kind, x, y in ch:
            stats[kind] += 1
            if kind == "CHANGED":
                sec += ["**BEFORE**", "", quote(x), "", "**AFTER** (~~deleted~~, **added**)", "", quote(marked(x, y)) if not y.lstrip().startswith("|") else quote(y), ""]
            elif kind == "NEW": sec += ["**NEW**", "", quote(y), ""]
            else: sec += ["**REMOVED**", "", quote(x), ""]
        body += sec
    if body: md += [f"## {title}", ""] + body
body_md = "\n".join(md)

# ---------------------------------------------------------------- sizes and counts for the summary pages
def nwords(txt): return len(re.findall(r"\S+", re.sub(r"```.*?```", "", txt, flags=re.S)))
main_files = [f for _, f in FILES[1:]]
w_before = sum(nwords(before(f)) for f in main_files); w_after = sum(nwords(after(f)) for f in main_files)
def pages(path):
    r = subprocess.run(["pdfinfo", path], capture_output=True, text=True); m = re.search(r"Pages:\s+(\d+)", r.stdout); return m.group(1) if m else "?"
R = T + "reading/"
def para_words(path, prefixes):
    txt = after(path); tot = 0
    for b in re.split(r"\n\s*\n", txt):
        if any(b.startswith(p) for p in prefixes): tot += len(b.split())
    return tot
cut5 = para_words("ch5_results.md", ["The test of the size of moves was set up", "Both tests of the size of moves", "Quarterly pairs do not reject", "Age does not explain"])
cut4 = para_words("ch4_data_methods.md", ["The second objective, to reconcile", "The sources differ by company"])
sec = lambda path, num: sum(len(b.split()) for k, h, bl in sections(after(path)) if k == num for b in bl)
front = f"""# Thesis changes since the 24 October version: before and after, for your review

Prepared 25 October 2026. **BEFORE** is the text you sent Prof. Kong on 24 October, with her Chapter 1 edits already ported in (commit `{BASE}`). **AFTER** is the text now (the 25 October YZU file and the other copies are built from it). Every change below is already applied and committed, so each one can be reverted, but none has been shown to you before; this document is that preview. Nothing here has been sent to her.

## A. Her comments, and what became of each

| Her item | What was done | Where to look | Your call |
|---|---|---|---|
| Overall: the empirical design does not test the hypotheses well enough | Direct tests added: revenue growth on transaction value growth for H1; OLS of the wedge and the ecosystem ratio on platform and home-market features | 3.3, 5.2, 5.3; Tables 5.3 and 5.4 | Read 5.2 and 5.3. All of it is exploratory |
| Overall: tighten, get to the point | **Not done.** The main text grew from {w_before:,} to {w_after:,} words | see the notes in section D | Choose the cuts |
| Overall: strengthen the economic implications | Investors, sellers and drivers, and policy, each in a paragraph in 5.3; investors in 7.2 | 5.3, 7.2 | Check the wording on market power |
| 1. Drop the Symbols page; spell out abbreviations | Done. Symbols are in Appendix A; BPS, UNCTAD, OECD, LSEG, QRIS spelled out at first use | Appendix A; 1.1, 1.2, 4.5, 5.10 | none |
| 2. Table 1 (literature gaps) | Dropped; the gaps are in the list in 2.4 | 2.4 | none |
| 2. Tables 2 and 7 to Appendix A | Done (terms in 3.1 became prose; sources are Appendix A.2) | 3.1, Appendix A | none |
| 2. Tables 3 and 4 | Dropped (for the defence slides) | 3.4, 3.6 | none |
| 2. Table 5 to the appendix | Done (Appendix B.2) | Appendix B.2 | none |
| 2. Table 6 as a footnote | Done: the first footnote in the thesis | 4.6 | none |
| 2. Table 8 | Dropped; each section states its label | 5 (opening) | none |
| 2. Table 9 kept and cited in 3.2 | Done | 3.2, 5.1 | none |
| 2. Table 10 (test of H1) replaced by the correlation matrix | Done. The group test of take-rate moves is now text and Appendix C | 5.2, Table 5.2 | none |
| 2. Tables 11 and 12 replaced by summary statistics and OLS | Table 11 replaced (the seven windows moved to Appendix B.3). **Table 12 (the 2023 rise in the count) is still in the text, in 5.7** | 5.3, 5.7 | Needs her answer |
| 2. Figure 2 as Panels A, B and C | Done. The right panel is now a simple percentage change | Figure 5.1 | Check the figure |
| 2. Section 3.3 | Replaced by direct tests | 3.3 | none |
| 3. Appendix A, definition of variables | Done, in her three-column form, with the regression variables in Panel E | Appendix A | none |
| 4. Summary statistics and correlations in one table | Done. Panel B has nine variables; inflation and household spending were left out for width (they correlate 0.80 with the policy rate and 0.92 with GDP growth) | Table 5.2 | Say if she wants all eleven |
| 4. Correlation of revenue growth and transaction value growth for H1 | Done: 0.90 abroad, 0.31 in Indonesia and the region | 5.2 | none |
| 4. OLS of ln(wedge) or the ecosystem ratio | Done with her controls; wedge in US dollars; size by total assets; take rate not a regressor; errors clustered by platform. Competitive entry and regulatory events are replaced by year dummies | Table 5.4 | Needs her answer on events |
| 4. Simple percentage change instead of log change | Done, except the registered market-value test (kept in logs as registered) and Appendix B.3 and Figure 5.2 (an exact split needs logs) | 3.2, 3.3, 5.2, 5.6, 5.7 | Needs her answer |
| 5. Economic implications in results and conclusion | Done | 5.3, 7.2 | see above |
| 6. Figures and tables after the References; "[Insert Table N about here]" | Done in the YZU Word file: six figures, then seven tables, each on its own page after the References, with 13 markers placed after the paragraph that first mentions each in its chapter; the Appendices follow, as in her sample. The reading, compact, condensed and editing copies keep them inline | YZU file, after the References | Say if she also wants the markers in the reading copy |
| 6. Captions that explain how to read each table | Done for all seven tables (a "This table…" paragraph under each title) | 5.1 to 5.5, 6.1, 6.2 | none |
| 23. Abbreviations spelled out at first use | Also fixed on 25 Oct: OLS expanded at first use (3.3); "SEC filings" now read "filings with the US Securities and Exchange Commission" | 3.3, 4.4, 5.3 | none |
| In her file: comments 23 (abbreviations), 26 (coverage) | Done | 1.1 | none |
| In her file: comment 46 (wedge against transaction value) | Done: it is 0.9994 in levels by construction, so the test is in growth rates | 5.2 | none |
| In her file: comment 47 (regression for H2), comments 48 and 49 (entry test inside the further analyses) | **Not done.** No unit for the H2 regression; the entry test is still its own section | 3.5, 5.6 | Needs her answer |

## B. Size and numbers

| | Before (24 Oct) | After (25 Oct) |
|---|---|---|
| YZU Word file, pages | 84 | {pages(R + "thesis_YZU_layout_2026-10-25.pdf")} |
| Reading copy, pages | 60 | {pages(R + "thesis_reading_copy_2026-10-25.pdf")} |
| Compact copy, pages | 27 | {pages(R + "thesis_compact_2026-10-25.pdf")} |
| Condensed Word file, pages | 26 | {pages(R + "yzu_tmp/chk/thesis_condensed_2026-10-25.pdf")} |
| Tables in the YZU file | 14 | 7 |
| Figures | 6 | 6 |
| Main text, words (Chapters 1 to 7) | {w_before:,} | {w_after:,} |
| Equations | 8 | 9 |
| Appendices | A to D | A to E (A is the variable definitions) |
| Automatic checks that pass | 314 | 398 |
| H1: size of take-rate moves, Indonesia against abroad | "about three times" (0.20 against 0.06 in logs) | 3.6 times (22 against 6 percent a year, simple change); the log version still gives 0.20 against 0.06 |
| H1 in growth rates | not reported | slope 0.99 abroad, 0.40 in Indonesia and the region (p = 0.02 against 1) |
| H2 | "more businesses account for 71 percent of the growth" | the number of businesses grew 27 percent and sales per business 10 percent |
| H2 read as wider coverage | "42 to 54 percent" | count +12 to 17 percent against sales per business +14 to 17 percent |

## C. How to read the changes

Each block below is one paragraph of the text. **BEFORE** is the old wording. **AFTER** is the new wording, with ~~deleted words struck through~~ and **added words in bold**. **NEW** and **REMOVED** are paragraphs that exist on one side only. Tables are abbreviated to their first rows. Appendices are not compared line by line: Appendix A (variables), B.5 (classification of the platforms) and C.3 (checks on the new tests) are new; the old Appendices A to D are now B to E.

"""
notes = f"""

## D. My review notes

**Things I would not claim more strongly than the text does**

1. The Indonesia and region result rests on five platforms. The wild bootstrap allows for the small number of clusters, but it does not create information. In the growth test the Indonesian and regional group has 15 pairs, and the slope's p-value (0.02) uses a t distribution with four degrees of freedom. I removed a claim that the two correlations differ at p < 0.001 for the same reason.
2. Total assets are for the whole company. Tokopedia and GoTo (on-demand) carry the same figure, the GoTo group's. Rakuten's includes its bank.
3. I assigned each platform's main market and type. Six assignments are ambiguous; the result is unchanged without them (Appendix C.3).
4. The size and macro controls explain the wedge, not the difference between the groups: the wedge is almost all transaction value, so the wedge regression mostly shows that big platforms carry a lot. The ecosystem ratio is where the groups differ. Prof. Kong may ask why the wedge regression is there; the honest answer is that she asked for it, and that its result is itself informative.
5. "Market power" in the sellers and drivers paragraph is stated as an open question, because the thesis has no seller-side data.

**Where the text got longer, against her request to tighten.** The new tests add about {w_after - w_before:,} words net. Candidates to cut or move to Appendix C, with the current word counts: the paragraphs on the narrower first test, the direction of moves, the quarterly pairs and age in 5.2 ({cut5} words); the account of the seven windows and the company sources in 4.4 ({cut4} words); 7.4 on the limits ({sec("drafts/ch7_draft_2026-10-14.md", "7.4")} words) overlaps with the new limits paragraph. Section 5.2 is now {sec("ch5_results.md", "5.2")} words and 5.3 is {sec("ch5_results.md", "5.3")}.

**Inconsistencies I know about.** Figure 5.2, the Tokopedia split and Appendix B.3 are in logs because the split of revenue growth into commerce, fees and incentives is exact only in logs; Appendix C.1 keeps the first version of the H1 test in logs. The market-value regression keeps its registered log definition. A simple-change version needs the licensed market values and a local run, which I have not written.

**Decisions I need from you**

1. Send Prof. Kong the nine questions in `KONG_COMMENTS_TRACE.md`, section 6, or only the ones still open: the unit of the H2 regression, whether Tables 13 and 14 (now 6.1 and 6.2) and the older figures stay, what counts as competitive entry or a regulatory event for the foreign platforms, and whether the entry test belongs inside the further analyses.
2. What to cut for length. The layout step is done, so cuts no longer move it, but each cut changes the page numbers in the YZU file (rebuilt in one command).
3. Whether the abstract (195 words) stays as it is; the new second paragraph adds four words.
"""
open(T + "PREVIEW_BEFORE_AFTER.md", "w", encoding="utf8").write(front + body_md + notes)
print(stats, "main text words", w_before, w_after)
