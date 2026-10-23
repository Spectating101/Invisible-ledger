# Thesis manuscript, October 2026 rewrite

The thesis written in full. Same title, research question, hypotheses and measures as the 27 Sep proposal (`papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf`); same chapters. One file per chapter while drafting; assembled into the YZU template at the end.

**Built from:** `research/option_space_2026-10-01/DRAFT_STORY_v1.md` (story and evidence map), `NARRATIVE_ARC.md` (order), `GOLDEN_PITCH.md` (voice), the groundwork Parts 1-7 with their dated notes, and `FINDINGS.md`. Every number comes from a script or ledger named there.

**How to continue this work (for any new session, local or cloud).**
1. Read `DECISIONS.md` in this folder first. It lists what the researcher has settled, what is open, how work has gone wrong before, and how to sync the branches. Then read Part D of `EDIT_HISTORY.md` for the chapter you will touch.
2. Sync before editing: `git fetch --all`, and take the branch with the newest thesis work (`DECISIONS.md` section 0). The current line is `claude/happy-pascal-uc2eya` and `claude/wizardly-cerf-2vgv2v`; `main` is behind until the October line is merged.
3. Show every change as before and after in chat, apply only what the researcher approves, then make one commit and add one row to `EDIT_HISTORY.md`.
4. The licensed data are not in the repository (`research/option_space_2026-10-01/LICENSED_DATA.md`). Writing does not need them; every number is in the committed tables, `FINDINGS.md` and the Part 1-7 files with their dated notes. Do not rerun the licensed scripts in a cloud session.
5. The researcher prefers explanations in chat, and asks for pushback when a request would weaken the thesis.

**Writing rules** (agreed with the researcher on 12 Oct 2026 after several rejected drafts; they override older style notes):
- **Spine.** Start each chapter from the proposal's and the oral deck's own paragraph order and handover lines (`papers/current/`); their flow worked. Lighten the sentences and insert the new findings where the line reaches them. Do not rebuild a chapter from the story drafts.
- **Write linearly.** Each paragraph answers what the previous one left open. Test for every paragraph: does it make the next one necessary, and does it add to the stakes? A paragraph that only states what exists is "almost duh" and must be rewritten or cut. Deliver whole chapters; do not spend a turn per paragraph.
- **Zoom in and out** to build stakes. Chapter 1 goes global first, then into Indonesia (the researcher's decision of 23 Oct, replacing the deck's scene-first order, which suits a speaker and not a reader): the size of online trade and who relies on the figures, why a stand-in can fail, Indonesia in 2023, the gap, then Indonesia as the case with its own amounts, ending on the chat and social selling events (Tanah Abang, TikTok Shop). The 12 to 13 Oct opening is kept in `alternatives/`.
- **Openers stand alone.** No paragraph or section opens on a word that leans on the previous one ("both", "these readers", "these figures", "described above", "for that"). Name the subject.
- **Register.** Statements of fact in a neutral academic tone; no rhetorical lines, no labelled beats, no section written as bullets in place of paragraphs (an early Chapter 2 or 1.2 draft was all bullets, which is why this rule exists, per the researcher, 13 Oct 2026). Prose carries the argument. A short numbered list is fine where items are parallel and later chapters refer back to them, such as the three research questions in 2.4 and at the start of Chapter 3. Rounded figures in the prose (41%, 5%, 53%, 9%); exact values in tables and notes. No regulation numbers or exact dates in the narrative. Sentences of about 15 to 18 words with connecting words; do not chop to 11 words.
- **Chapter 1.** No "main findings" section (it spoils the tension); a three-sentence declaration of the answer is enough. The first paragraph of 1.1 is the grand ambition, stated as boldly as the subject allows; the research question follows as the step needed to reach it. Contributions are tied to the three groups who rely on the figures.
- **Claims.** Each claim at its evidence strength. Never write that the extra 2023 sellers "were there all along" or "were only counted that year", that the gap is "too large to be chance", or that returning sellers are ruled out. Say "about half of the increase is not explained by first-time entry" and "the additional count was concentrated among older, long-established small businesses". The growth identity is D = (1 + gV)(m1 - m0)/m0. Do not mention "the proposal" in thesis prose.
- **Terms.** Define each once, in plain words (transaction value, revenue, take rate, invisible wedge, ecosystem ratio, growth divergence). Avoid "indicator", "Overall,", "therefore", "rather than". Do not use the sentence "of every 100 rupiah, about 7 appear as revenue".
- **Readability before safety** (12 Oct, evening). The test for a sentence is how easy it is to read, then whether it is right. A safer wording that makes a sentence heavier is rejected: that is what Prof. Kong and Prof. Thomas complained about. The ambition and the framing are bold by design and are not flagged for lacking proof. Back them with a source in a note or a later chapter when that is cheap, never by hedging the prose. Statements of what the data show keep their evidence strength (the Claims rule above). Flag a sentence only when it makes a different claim; say so once and offer the closest supportable version.
- **A movement gets its mechanism.** When a paragraph shows a movement (revenue up while sales fell), the paragraph that explains it says how it happened (the platform kept more of each sale; at Tokopedia, smaller discounts and incentives), not only that the measures differ.
- **One currency.** Running text uses US$, rounded, converted at the World Bank official rate for the year (`research/option_space_2026-10-01/tables/src/worldbank_fx_2022_2024.json`; 2024: Rp15,855 per US$). No bare rupiah in the narrative.
- **Show before you change.** Preview the change as before and after in chat; apply only what the researcher approves; then one commit, and a row in `EDIT_HISTORY.md`. When asked to assess a passage, print the full text first with numbered paragraphs, then say what each paragraph does and whether it hands over to the next, then list only reading problems (flow, openers, number density, currency), ranked.
- **Vocabulary** (settled in the 12 Oct seam pass; one word for one thing, in every chapter):
  - *transaction value* is the term for what is bought through a platform; "the commerce a platform carries" is its plain companion (tied once, in Table 3.1). "Sales" means a single sale, or BPS's national online sales, never a platform's transaction value.
  - *invisible wedge* or *the wedge* is transaction value minus revenue. Never "gap" for that quantity ("research gap" is a different thing).
  - *figure* is a published or reported number; *measure* is a yardstick, or one of the three the thesis builds (wedge, ecosystem ratio, growth divergence).
  - *count of online sellers*, then *the count*; *entry test*; *first-time entry*; *H1*, *H2*.
  - *chain* is used only in Chapter 3, for revenue, platform commerce and national commerce.
  - *report* for what an accounting statement shows; *records* for a platform's data on sales.
  - *take rate* for the share of each sale a platform keeps; *US$* for money in running text.
- **The committee's points** and where each is answered: see Part A of `EDIT_HISTORY.md`.

`DECISIONS.md` is the one-page record of what is settled and what is open. `EDIT_HISTORY.md` is the append-only log of each round of edits and the researcher's response; read Part D of it before revising a chapter.

| File | Chapter | State (23 Oct 2026) |
|---|---|---|
| `ch1_introduction.md` | 1 Introduction | Order approved 12 to 13 Oct and restored 23 Oct; open: 1.1 brevity, the 1.2 and 1.3 wording (`DECISIONS.md`) |
| `ch2_literature.md` | 2 Literature Review | Three-part form confirmed 13 Oct |
| `ch3_framework.md` | 3 Framework and Hypotheses | Accepted for now 13 Oct; a cold read is still due |
| `ch4_data_methods.md` | 4 Data and Methods | Follows Chapter 5's order and points to Chapter 3; exact-inference checks added 22 Oct |
| `ch5_results.md` | 5 Results | Ten sections on Figure 3.1's two links; 5.2 stands; readability pass 1 applied 23 Oct; a linear pass of Chapters 5 and 6 awaits approval |
| `drafts/ch6_draft_2026-10-14.md`, `drafts/ch7_draft_2026-10-14.md` | 6 The Rules and How Far They Reach; 7 Conclusion | The live chapter files, despite the folder name; 6.5 waits for the scoring dates (27 Oct, early Nov, mid Nov) |
| `appendix_notes.md` | Appendices | Platform lists, windows, every check on the H1 test, registered tests with outcomes |
| `references.md` | References | Checked 16 Oct; two entries rest on a named secondary source; APA until the YZU style is settled |
| `symbols.md`, `abstract.md` | Symbols and Abbreviations; Abstract | English only; the Chinese abstract, keywords and title page are the researcher's |
| `reading/` | Reading copies | `build_reading.sh` (full copy and editing DOCX) and `build_compact.sh` (Chapters 1 to 7, short and dense; the 59 key sentences listed in `reading/keypoints.txt` are bold, so the bold alone summarises the thesis: `boldkey.py`; the full copy and the thesis text carry no bold); judge layout by the full copy |
| `alternatives/` | Tried, not adopted | Not read by any build |
