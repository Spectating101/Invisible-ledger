# Decisions and current state: read this first

Updated 23 Oct 2026. This is the one page any session (Claude, ChatGPT or other) reads before touching the thesis. It states what the researcher has already decided, what is still open, and how work goes wrong. The reasons and every round are in `EDIT_HISTORY.md`, which is an append-only log. The writing rules are in `README.md`. **The researcher's instruction in the current conversation beats this page and the log.** If it contradicts a settled item below, do what was asked, mention the conflict once, and update this page. Do not revert it, do not argue from the log, and do not make the researcher repeat it.

## 0. Before you change anything

1. **Sync first.** Run `git fetch --all`, then `git log --all -1 --format='%h %D %ad' -- papers/thesis_2026-10`, and merge or fast-forward the branch with the newest thesis work before you edit. Several sessions work on this thesis on different branches. If the branches have diverged, tell the researcher; do not pick one silently.
2. **Read this page, then Part D of `EDIT_HISTORY.md` for the chapter you will touch.** Part D records what was approved and what was rejected. The approvals are early in the log, not at the end, so reading only the end of the log misses them.
3. **Check the settled list below.** If your idea touches a settled item, say so and ask. Do not present it as a fresh option.
4. **Show before and after in chat. Apply only what the researcher approves.** One commit per round and one row in the log.
5. **Judge feel and layout by the full reading copy, not the compact one.** The compact copy is 9.4 pt with about 110 characters a line, built to be short.

## 1. Settled: the researcher decided; do not reopen unless they ask

| Area | Decision | Settled | Recorded |
|---|---|---|---|
| Concept | Title, research question, H1, H2 and the measures are those of the 27 Sep proposal (passed 1 Oct). No H3 or H4. | 1 Oct | AGENTS.md; Part A |
| Spine | The proposal's and the deck's paragraph order is the spine of each chapter. Lighten the sentences and insert new findings where the line reaches them. Do not rebuild a chapter on a new frame. | 12–13 Oct | README; Part D, Ch1 round 1 and "rebuilt on the proposal's spine" |
| Chapter 1 opening | Global first, then into Indonesia (the researcher's decision, 23 Oct): the size of online trade and who relies on the figures; why a stand-in can fail; Indonesia in 2023 (Tokopedia, BPS and the central bank); the gap; Indonesia as the case, ending on the Tanah Abang and TikTok Shop events. This replaces the 12–13 Oct scene-first order, which is kept in `alternatives/`. It follows the 8–9 Oct wish to frame Indonesia as an example of a bigger problem. | 23 Oct | Part B (8–9 Oct); log 23 Oct |
| Section 1.1 | The first paragraph is the grand ambition, bold by design, with no claim flags. The question follows as the step toward it. The question and hypotheses paragraphs stay as they are; the objectives keep the proposal's formal wording, which Chapters 4.4 and 4.9 echo. | 12 Oct; 23 Oct | Part B; Part D Ch1 rounds 10 to 19; log 23 Oct |
| Section 1.2 | The investor paragraph drops the abstract sentence on market value per dollar of revenue and per dollar of commerce; the closing paragraph ends after "…the rules that act on both". The 1.1 ambition paragraph was checked again and kept as it is (the researcher, 23 Oct). | 23 Oct | Log 23 Oct, "Chapter 1.2 and the opener" |
| Abbreviations | Not spelled out in the running text at first use. Prof. Kong asked for it twice (comments 107, 161, 163), but the researcher judged the parentheses clutter and decided on 23 Oct not to add them; `symbols.md` is the list. The abstract uses plain words instead ("the national statistics office's survey"). Do not propose adding expansions again. | 23 Oct | Log 23 Oct, "Kong's comments re-read" |
| No findings section | Chapter 1 has a short declaration of the answer ("In brief"), not a findings section. | 12 Oct | Part D, Ch1 round 5 |
| Linear writing | Each paragraph answers what the last left open. Openers name their subject ("both", "these", "this", "the same" never open a paragraph). A chapter stands on its own without restating. | 12–13 Oct | README; "Independence read correctly" |
| Readability before safety | A sentence is judged for ease first, then for being right. No hedging prose to protect claims. Statements of what the data show keep their evidence strength. | 12 Oct | README; Part B |
| Standing wording | "About half of the rise is not explained by first-time entry." Never "there all along", "too large to be chance", or returning sellers "ruled out". The wedge is what a revenue-only measure leaves out, never missing GDP, hidden income or unpaid tax. | 8–16 Oct | README Claims; Part C |
| Labels | Every Chapter 5 result is registered, exploratory or descriptive. The 5-against-27 H1 test is exploratory; the registered test is the narrower 3-against-8. | 13–16 Oct | Table 5.1; Part C |
| Chapter 2 | Three-part sections (the situation, what the research explains, where it stops). The gap is built from the stopping points; three questions as a short numbered list. | 13 Oct | Part D, "Chapter 2 applied in the three-part form" |
| Chapter 3 | Opens on the logic, then Figure 3.1, then Table 3.1 (terms defined once), equations (1) to (8). Accepted for now; a cold read is still due. | 13 Oct | Part D, "Chapter 3 rebuilt as the bridge" |
| Chapter 4 | Opens with a short, neutral statement of the data conditions (no apology). Follows Chapter 5's order and points to Chapter 3 instead of repeating it. | 13 Oct | Part D, "Chapter 4 restructured" |
| Chapter 5 | Answer-first sections on Figure 3.1's two links; Table 5.1 lists the results; rounded numbers in prose, exact values in tables; check detail in Appendices B and C. The order and wording of 5.2 stand (a linear reorder was tried and not adopted); no lead-ins that comment on the text. | 14 Oct; 23 Oct | Part D, "Chapters 1 to 5 aligned"; log 23 Oct |
| Chapter 6 | Inner link to outer; the tax is 6.3; 6.5 has a results slot. The tax-start prediction is withdrawn (its outcome was public before registration). | 14–15 Oct | Part D; `PREREGISTRATION.md` addendum |
| Chapter 7 | 7.3 matches Appendix C; 7.4 carries the whole list of limits, so the main chapters need not. | 14–15 Oct | Part D |
| Words and money | One word per concept (README Vocabulary). US$ in running text at the World Bank rate. | 12 Oct | README |
| Data | BPS and LSEG files are never shared or committed, only aggregates. No contact with BPS by email. Licensed scripts are not rerun in cloud sessions. | standing | Part B; `LICENSED_DATA.md` |

## 2. Open

**Needs the researcher's decision**
1. Section 1.1 should be "brief yet impactful". Two attempts failed (a shorter section; bullet lists). Untried: tighter sentences inside the same paragraphs.
2. The US$60 million to US$300 million tax range was cut from the Chapter 1 opening on 23 Oct (it stays in 6.3). Restore it if wanted.
3. Whether to restore the original wording of the lead-ins that readability pass 1 added (for example "One check goes the other way" in 5.2).
4. The GDP-scale sentence (2.92 percent, ledger C39).
5. The 13 proposal references the thesis dropped (`REFERENCE_VERIFY_16OCT.md`); the citation style (APA until the YZU template decides).
6. Prof. Kong had not yet seen the H2 framing (Part A, last confirmed 12 Oct).

**Work not yet done**
- A paragraph-by-paragraph linear pass of Chapters 5 and 6 (needs the researcher's before-and-after approval), the transaction-value definition map, and a "who gains and loses" note for each rule in Chapter 6.
- Section 6.5 scoring: GoTo 27 Oct; BPS early Nov; Grab and Sea mid Nov (`SCORING_PREP.md`).
- The Chinese abstract, keywords, title page and YZU assembly (the researcher's).
- The M1 upgrade run needs the researcher's LSEG machine.

## 3. How this has gone wrong before

1. **Caveats creep back into Chapters 5 to 7.** Each audit or upgrade pass adds checks and p-values to the main text. On 13 Oct and again on 23 Oct, the researcher found these chapters had become audit-log reporting. Put detail in Appendices B and C and in 7.4. The main text gets the result and at most one clause of caveat.
2. **Reordering or rebuilding away from the proposal's and deck's spine breaks the flow.** Seen in Chapter 1 round 1, in three rebuilds of Chapters 2 and 3 on 13 Oct, and in the Chapter 1 global-first reorder on 23 Oct.
3. **Line fixes judged by counts, not by reading.** Judge a change by reading it in context. No plainer-for-its-own-sake rewording; keep the sentence that is clearer.
4. **Reading the compact copy as a verdict on the layout or the text's weight.**
5. **Starting from stale routing.** Older files named the September branch as the working branch and listed chapters as unwritten. Corrected 23 Oct; if you meet such a statement, this page wins.
6. **Reading only the end of the log.** The approvals are in Part D.
7. **Putting the record above the researcher.** On 23 Oct a global-first Chapter 1 opening was asked for twice, then reversed because the log said scene-first had been approved on 12 Oct. The log is history; the researcher's current word is the instruction. Apply it and update the record.

## 4. Where things are (23 Oct 2026)

- **Branches.** The current line is `claude/happy-pascal-uc2eya` and `claude/wizardly-cerf-2vgv2v`, identical when this page was written. `main` is behind until the October line is merged by pull request. When it is merged, `main` is the single line.
- **Chapters.** Chapters 1 to 5, `abstract.md`, `symbols.md`, `references.md` and `appendix_notes.md` are in `papers/thesis_2026-10/`. Chapters 6 and 7 are the live files `drafts/ch6_draft_2026-10-14.md` and `drafts/ch7_draft_2026-10-14.md`.
- **Reading copies.** `reading/`: `thesis_reading_copy_<date>.pdf` (judge layout by this; it carries no notes to the reader either, via `condense.py`), `thesis_condensed_<date>.docx` (the condensed thesis as a Word file, 26 pages, same text, bold sentences and look as the compact PDF, Source Serif 4 embedded; `build_condensed_docx.sh`), `thesis_compact_<date>.pdf` (the condensed thesis: abstract and Chapters 1 to 7, short and dense, with no notes to the reader; `reading/condense.py` drops the empty Outcome column of Table 6.2, the results slot in 6.5 and the abstract's note to the author; 59 key sentences are bold so that the bold alone summarises the thesis, the researcher's choice of 23 Oct; the list is `reading/keypoints.txt`, and the build stops if an edit removes one of them; a format of the compact copy only), `thesis_editing_copy_<date>.docx`. Rebuild them with `build_reading.sh` and `build_compact.sh` after any text change.
- **Alternatives.** `alternatives/` holds earlier versions that were replaced (now the 12–13 Oct scene-first Chapter 1 opening). No build reads it.
- **Checks.** `research/option_space_2026-10-01/rebuild_all.sh` (314 automatic checks); audits in `materials_2026-10-15/`.
- **Researcher only.** The Chinese abstract, the YZU template and the final assembly.
