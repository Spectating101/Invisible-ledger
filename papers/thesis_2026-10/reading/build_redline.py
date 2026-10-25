"""Full redline of the whole thesis text (25 Oct 2026): the complete BEFORE text and the complete AFTER text in one stream.
Run from the repository root:
    python3 papers/thesis_2026-10/reading/build_redline.py [BASE_COMMIT_OR_TAG] [OUT_BASENAME]
BASE (default a1f1af2: the thesis as sent to Prof. Kong on 24 Oct, her Chapter 1 edits ported in) is compared with the working tree.
Unchanged text is printed as it is. A deleted word is struck through in red, an added word is underlined in blue. A whole paragraph, table, equation or
figure that exists on one side only sits in a red (deleted) or blue (added) box. Every changed block carries an ID, [C001], listed in a change index.
Writes papers/thesis_2026-10/<OUT>.md, papers/thesis_2026-10/<OUT>_INDEX.csv and (with the print step of the shell recipe) the PDF. Nothing in the
thesis files is changed."""
import csv, difflib, os, re, shutil, subprocess, sys

BASE = sys.argv[1] if len(sys.argv) > 1 else "a1f1af2"
OUT = sys.argv[2] if len(sys.argv) > 2 else "REDLINE_FULL"
T = "papers/thesis_2026-10/"
FILES = [("Abstract", "abstract.md"), ("Symbols and Abbreviations (page removed)", "symbols.md"), ("Chapter 1. Introduction", "ch1_introduction.md"),
         ("Chapter 2. Literature review", "ch2_literature.md"), ("Chapter 3. Framework and hypotheses", "ch3_framework.md"),
         ("Chapter 4. Data and methods", "ch4_data_methods.md"), ("Chapter 5. Results", "ch5_results.md"),
         ("Chapter 6. Discussion and policy implications", "drafts/ch6_draft_2026-10-14.md"), ("Chapter 7. Conclusion", "drafts/ch7_draft_2026-10-14.md"),
         ("Appendices", "appendix_notes.md"), ("References", "references.md")]
OLD_IMG = T + "redline_tmp/old/"

def git_show(path, binary=False):
    r = subprocess.run(["git", "show", f"{BASE}:{path}"], capture_output=True)
    return r.stdout if binary else (r.stdout.decode("utf8") if r.returncode == 0 else "")
def after(path): return open(T + path, encoding="utf8").read() if os.path.exists(T + path) else ""

def blocks(text):
    out, cur, in_code = [], [], False
    for line in text.split("\n"):
        if line.startswith("```"): in_code = not in_code
        if not in_code and not line.strip() and not line.startswith("```"):
            if cur: out.append("\n".join(cur)); cur = []
        else: cur.append(line)
    if cur: out.append("\n".join(cur))
    return [b for b in out if b.strip()]
def kind(b):
    if b.startswith("#"): return "heading"
    if b.startswith("```"): return "code"
    if b.lstrip().startswith("|"): return "table"
    if b.startswith("!["): return "image"
    return "para"
tokens = lambda s: re.findall(r"\S+", s)
def ratio(a, b): return difflib.SequenceMatcher(None, tokens(a), tokens(b), autojunk=False).ratio()

def wdiff(a, b):
    """word-level markup of b against a, keeping line breaks (list items): (markup, n_deleted, n_inserted)"""
    ta, tb = re.findall(r"\n|\S+", a), re.findall(r"\n|\S+", b); out = []; nd = ni = 0
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if op == "equal": out.append(" ".join(tb[j1:j2]))
        else:
            if i2 > i1: out.append("<del>" + " ".join(t for t in ta[i1:i2] if t != "\n") + "</del>" if any(t != "\n" for t in ta[i1:i2]) else ""); nd += sum(1 for t in ta[i1:i2] if t != "\n")
            if j2 > j1:
                seg = tb[j1:j2]
                if any(t != "\n" for t in seg): out.append("<ins>" + " ".join(t for t in seg if t != "\n") + "</ins>")
                if seg[-1] == "\n" or seg[0] == "\n": out.append("\n")
                ni += sum(1 for t in seg if t != "\n")
    return re.sub(r" ?\n ?", "\n", " ".join(o for o in out if o)), nd, ni

def cells(line): return [c.strip() for c in line.strip().strip("|").split("|")]
def is_sep(line): return bool(re.fullmatch(r"\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?", line.strip()))
def row(cs): return "| " + " | ".join(cs) + " |"
def table_diff(a, b):
    """row-level, then cell-level, markup of table b against table a: (markdown, n_deleted, n_inserted)"""
    la, lb = a.split("\n"), b.split("\n"); out = []; nd = ni = 0
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, la, lb, autojunk=False).get_opcodes():
        if op == "equal": out += lb[j1:j2]; continue
        A, B = la[i1:i2], lb[j1:j2]; used = set(); k = 0
        for jb, rb in enumerate(B):
            if is_sep(rb): out.append(rb); continue
            best, bi = 0.0, None
            for ia, ra in enumerate(A):
                if ia in used or is_sep(ra) or len(cells(ra)) != len(cells(rb)): continue
                r = ratio(ra, rb)
                if r > best: best, bi = r, ia
            if bi is not None and best >= 0.4:
                used.add(bi); ca, cb = cells(A[bi]), cells(rb); mc = []
                for x, y in zip(ca, cb):
                    m, d, n = wdiff(x, y) if (x or y) else ("", 0, 0); mc.append(m); nd += d; ni += n
                out.append(row(mc))
            else:
                cb = cells(rb); out.append(row([f"<ins>{c}</ins>" if c else "" for c in cb])); ni += sum(len(tokens(c)) for c in cb)
        for ia, ra in enumerate(A):
            if ia not in used and not is_sep(ra):
                ca = cells(ra); out.append(row([f"<del>{c}</del>" if c else "" for c in ca])); nd += sum(len(tokens(c)) for c in ca)
    return "\n".join(out), nd, ni

def align(a, b):
    """[('eq', x), ('chg', x, y), ('del', x), ('ins', y)] in document order"""
    res = []; sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal": res += [("eq", x) for x in b[j1:j2]]; continue
        A, B = a[i1:i2], b[j1:j2]; used = set(); emitted = set(); pairs = {}
        for jb, y in enumerate(B):
            best, bi = 0.0, None
            for ia, x in enumerate(A):
                if ia in used or kind(x) != kind(y): continue
                r = ratio(x, y) if kind(y) != "image" else (1.0 if x == y else 0.0)
                if r > best: best, bi = r, ia
            if bi is not None and best >= 0.45: pairs[jb] = bi; used.add(bi)
        for jb, y in enumerate(B):
            if jb in pairs:
                ia = pairs[jb]
                for r_ in range(len(A)):
                    if r_ < ia and r_ not in used and r_ not in emitted: res.append(("del", A[r_])); emitted.add(r_)
                res.append(("chg", A[ia], y))
            else: res.append(("ins", y))
        for r_ in range(len(A)):
            if r_ not in used and r_ not in emitted: res.append(("del", A[r_]))
    return res

REASONS = {  # (file, section) -> why it changed; "*" is the file default. This mapping is mine, not hers.
 ("abstract.md", "*"): "H1 result restated (growth test, 3.6 times)",
 ("symbols.md", "*"): "Symbols page dropped (her item 1); symbols now in Appendix A",
 ("ch1_introduction.md", "*"): "Abbreviations at first use (item 1, comment 23); comment 26; H1 result restated",
 ("ch2_literature.md", "*"): "Table 1 dropped; gaps stated in the list (item 2)",
 ("ch3_framework.md", "3.1"): "Table 2 (terms) became prose; symbols to Appendix A (items 1, 2)",
 ("ch3_framework.md", "3.2"): "Take-rate identity moved here; Table 9 cited as the example (item 2)",
 ("ch3_framework.md", "3.3"): "Section 3.3 replaced by the direct tests (items 2 and 4)",
 ("ch3_framework.md", "3.4"): "Hypotheses table dropped; H1 tests restated; H2 in simple growth (items 2 and 4)",
 ("ch3_framework.md", "3.6"): "Further-analyses table dropped; market-value test keeps its registered logs; equations renumbered",
 ("ch3_framework.md", "*"): "Chapter 3 restructure (items 2 and 4)",
 ("ch4_data_methods.md", "4.1"): "Table 4.1 moved to Appendix B (item 2)",
 ("ch4_data_methods.md", "4.3"): "H1 tests: growth regression added; simple percentage change (item 4)",
 ("ch4_data_methods.md", "4.4"): "New: data and variables of the regressions (item 4)",
 ("ch4_data_methods.md", "4.5"): "LSEG spelled out; equation renumbered",
 ("ch4_data_methods.md", "4.6"): "Table 4.2 became a footnote (item 2); equation renumbered",
 ("ch4_data_methods.md", "4.9"): "Table 4.3 moved to Appendix A (item 2)",
 ("ch4_data_methods.md", "4.10"): "Public inputs added",
 ("ch4_data_methods.md", "*"): "Chapter 4 changes",
 ("ch5_results.md", "0"): "Table 5.1 dropped (item 2); wedge table renumbered",
 ("ch5_results.md", "5.1"): "Wedge table renumbered; table caption",
 ("ch5_results.md", "5.2"): "Summary statistics, correlations and the H1 growth test (item 4); Figure panels (item 2)",
 ("ch5_results.md", "5.3"): "OLS of the wedge and the ecosystem ratio; economic implications (items 4 and 5)",
 ("ch5_results.md", "5.4"): "Equation renumbered",
 ("ch5_results.md", "5.6"): "H2 restated in simple percentage change (item 4)",
 ("ch5_results.md", "5.7"): "H2 coverage readings restated in simple percentage change (item 4)",
 ("ch5_results.md", "5.10"): "QRIS spelled out (item 1)",
 ("ch5_results.md", "*"): "Chapter 5 changes",
 ("drafts/ch6_draft_2026-10-14.md", "*"): "Equation renumbered; table reference; national identity number",
 ("drafts/ch7_draft_2026-10-14.md", "7.1"): "Answer restated with the new tests",
 ("drafts/ch7_draft_2026-10-14.md", "7.2"): "Investor implications restated (item 5)",
 ("drafts/ch7_draft_2026-10-14.md", "7.4"): "Limits of the new tests added",
 ("drafts/ch7_draft_2026-10-14.md", "*"): "Conclusion restated",
 ("appendix_notes.md", "*"): "New Appendix A (variables), relettering A to B, B.5, C.3 (items 1, 3)",
 ("references.md", "*"): "Sources added or generalised",
}
def snip(b):
    kd = kind(b)
    if kd == "table": return "[table] " + " / ".join(cells(b.split("\n")[0]))[:70]
    if kd == "code": return "[equation] " + b.split("\n")[1].strip()[:60] if "\n" in b else "[equation]"
    if kd == "image": return "[figure] " + (img_path(b) or "")
    return " ".join(tokens(b))[:90]
def lead(tag, mk):
    return f"{tag}\n\n{mk}" if re.match(r"(<[a-z]+>)?(\d+\.|[-*]) ", mk) else f"{tag} {mk}"
def reason(f, sec): return REASONS.get((f, sec)) or REASONS.get((f, "*"), "")

# images: keep the old version of any figure that changed
os.makedirs(OLD_IMG + "figures", exist_ok=True)
def img_path(b): m = re.match(r"!\[[^\]]*\]\(([^)]+)\)", b); return m.group(1) if m else None
def image_changed(b):
    p = img_path(b)
    if not p: return False
    new = open(T + p, "rb").read() if os.path.exists(T + p) else b""
    old = git_show(T + p, binary=True)
    if old and new and old != new:
        d = OLD_IMG + p; os.makedirs(os.path.dirname(d), exist_ok=True); open(d, "wb").write(old); return True
    return False
def old_image_block(b): return b.replace("](" + img_path(b) + ")", "](redline_tmp/old/" + img_path(b) + ")")

def code_diff(a, b):
    la, lb = a.split("\n"), b.split("\n"); out = []; nd = ni = 0
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, la, lb, autojunk=False).get_opcodes():
        if op == "equal": out += [f"  {x}" for x in lb[j1:j2]]
        else:
            out += [f"- {x}" for x in la[i1:i2]]; nd += i2 - i1; out += [f"+ {x}" for x in lb[j1:j2]]; ni += j2 - j1
    return "<pre class=\"cdiff\">" + "\n".join(x.replace("&", "&amp;").replace("<", "&lt;") for x in out) + "</pre>", nd, ni

md, index = [], []
n = 0
def newid(): global n; n += 1; return f"C{n:03d}"
for title, f in FILES:
    A, B = blocks(git_show(T + f)), blocks(after(f))
    if not A and not B: continue
    md += [f"\n<div class=\"filehead\">{title}</div>\n"]
    sec = "0"; heading = title
    for item in align(A, B):
        k = item[0]; cur = item[2] if k == "chg" else item[1]
        if kind(cur) == "heading":
            m = re.match(r"##? (\d+\.\d+|Appendix [A-E])", cur)
            if cur.startswith("## "): sec = m.group(1) if m else cur[3:]; heading = cur.lstrip("# ")
        if k == "eq" and kind(cur) == "image" and image_changed(cur):
            cid = newid(); tag = f'<span class="cid">{cid}</span>'
            md += [f'::: {{.del}}\n{tag} figure before\n\n{old_image_block(cur)}\n:::', "", f'::: {{.ins}}\n{tag} figure after\n\n{cur}\n:::', ""]
            index.append((cid, "changed", reason(f, sec), title, heading, 1, 1, "[figure] " + (img_path(cur) or ""))); continue
        if k == "eq": md += [cur, ""]; continue
        cid = newid(); tag = f'<span class="cid">{cid}</span>'; nd = ni = 0
        if k == "chg":
            x, y = item[1], item[2]; kd = kind(y)
            if kd == "table": mk, nd, ni = table_diff(x, y); md += [f"{tag} *table changed*", "", mk, ""]
            elif kd == "code": mk, nd, ni = code_diff(x, y); md += [f"{tag} *equation changed*", "", mk, ""]
            elif kd == "image":
                if image_changed(y):
                    md += [f'::: {{.del}}\n{tag} figure before\n\n{old_image_block(x)}\n:::', "", f'::: {{.ins}}\n{tag} figure after\n\n{y}\n:::', ""]; nd = ni = 1
                else: md += [y, ""]; cid = None; n -= 1
            elif kd == "heading":
                hs = re.match(r"(#+ )(.*)", y); ha = re.match(r"(#+ )(.*)", x)
                mk, nd, ni = wdiff(ha.group(2), hs.group(2)); md += [f"{hs.group(1)}{mk} {tag}", ""]
            else:
                mk, nd, ni = wdiff(x, y); md += [lead(tag, mk), ""]
            if cid: index.append((cid, "changed", reason(f, sec), title, heading, nd, ni, snip(y)))
        elif k == "del":
            x = item[1]; nd = len(tokens(x)); xx = old_image_block(x) if kind(x) == "image" and img_path(x) and not os.path.exists(T + img_path(x)) else x
            md += [f'::: {{.del}}\n{lead(tag, xx)}\n:::' if kind(x) in ("para", "heading") else f'::: {{.del}}\n{tag} *removed*\n\n{xx}\n:::', ""]
            index.append((cid, "removed", reason(f, sec), title, heading, nd, 0, snip(x)))
        else:
            y = item[1]; ni = len(tokens(y))
            md += [f'::: {{.ins}}\n{lead(tag, y)}\n:::' if kind(y) in ("para", "heading") else f'::: {{.ins}}\n{tag} *added*\n\n{y}\n:::', ""]
            index.append((cid, "added", reason(f, sec), title, heading, 0, ni, snip(y)))

# ---- index ----
cnt = {k: sum(1 for r in index if r[1] == k) for k in ("changed", "added", "removed")}
wd = sum(r[5] for r in index); wi = sum(r[6] for r in index)
by = {}
for r in index: by.setdefault(r[3], [0, 0, 0, 0]); by[r[3]][{"changed": 0, "added": 1, "removed": 2}[r[1]]] += 1; by[r[3]][3] += r[5] + r[6]
head = [f"# Full redline: the thesis as sent on 24 October against the thesis now", "",
        f"Prepared 25 October 2026. **BEFORE** = commit `{BASE}` (the text sent to Prof. Kong, her Chapter 1 edits ported in). **AFTER** = the current text. This file contains **both complete texts in one stream**: unchanged text is printed as it is, ~~deleted~~ words are <del>struck through in red</del>, <ins>added words are underlined in blue</ins>, and whole paragraphs, tables, equations or figures that exist on one side only sit in a red (removed) or blue (added) box. Each changed block has an ID such as <span class=\"cid\">C012</span>; the index below lists them all, with my reading of why each changed (my mapping to her comment items, not hers). Nothing here has been sent to her.", "",
        f"**Totals.** {cnt['changed']} changed blocks, {cnt['added']} added, {cnt['removed']} removed; about {wd:,} words deleted and {wi:,} added inside or between them.", "",
        "| Part | Changed | Added | Removed | Words touched |", "|---|---:|---:|---:|---:|"]
head += [f"| {k} | {v[0]} | {v[1]} | {v[2]} | {v[3]:,} |" for k, v in by.items()]
head += ["", "## Change index", "", "| ID | Type | Part | Section | Why (my mapping) | Starts with |", "|---|---|---|---|---|---|"]
esc = lambda s: s.replace("|", "\\|")
head += [f"| {r[0]} | {r[1]} | {esc(r[3])} | {esc(r[4])[:50]} | {esc(r[2])} | {esc(r[7])} |" for r in index]
head += ["", '<div class="pagebreak"></div>', ""]
open(T + OUT + ".md", "w", encoding="utf8").write("\n".join(head + md))
with open(T + OUT + "_INDEX.csv", "w", newline="", encoding="utf8") as fh:
    w = csv.writer(fh); w.writerow(["id", "type", "why_my_mapping", "part", "section", "words_deleted", "words_added", "starts_with"])
    for r in index: w.writerow([r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]])
print(cnt, "words deleted", wd, "added", wi)
