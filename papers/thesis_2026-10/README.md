# Thesis manuscript, October 2026 rewrite

The thesis written in full. Same title, research question, hypotheses and measures as the 27 Sep proposal (`papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf`); same chapters. One file per chapter while drafting; assembled into the YZU template at the end.

**Built from:** `research/option_space_2026-10-01/DRAFT_STORY_v1.md` (story and evidence map), `NARRATIVE_ARC.md` (order), `GOLDEN_PITCH.md` (voice), the groundwork Parts 1-7 with their dated notes, and `FINDINGS.md`. Every number comes from a script or ledger named there.

**How to continue this work (for any new session, local or cloud).**
1. Work on branch `proposal/integrated-2026-09-16` (not `main`).
2. Read `EDIT_HISTORY.md` in this folder first: it lists every concern (committee, researcher, reviews), what was done, and what is still open.
3. Next steps, in order: recheck section 1.2 against the ambition paragraph in 1.1; write chapter 3 (terms, the formula, H1, H2, the entry test) and chapter 4 (data, tests); rewrite chapter 5 to ten question sections from `research/option_space_2026-10-01/DRAFT_STORY_v2.md` (the existing `ch5_results.md` is an older report-style draft); then chapters 2, 6, 7. Chapter 6 waits for the 27 Oct and mid-Nov results.
4. The licensed data are not in the repository (`research/option_space_2026-10-01/LICENSED_DATA.md`). Writing does not need them; every number is in the committed tables, `FINDINGS.md` and the Part 1-7 files with their dated notes. Do not rerun the licensed scripts in a cloud session.
5. The researcher prefers explanations in chat, and asks for pushback when a request would weaken the thesis.

**Writing rules** (agreed with the researcher on 12 Oct 2026 after several rejected drafts; they override older style notes):
- **Spine.** Start each chapter from the proposal's and the oral deck's own paragraph order and handover lines (`papers/current/`); their flow worked. Lighten the sentences and insert the new findings where the line reaches them. Do not rebuild a chapter from the story drafts.
- **Write linearly.** Each paragraph answers what the previous one left open. Test for every paragraph: does it make the next one necessary, and does it add to the stakes? A paragraph that only states what exists is "almost duh" and must be rewritten or cut. Deliver whole chapters; do not spend a turn per paragraph.
- **Zoom in and out** to build stakes: a concrete Indonesian scene, then the general point, then global stakes with amounts and the cost of being wrong, then Indonesia with its own amounts.
- **Openers stand alone.** No paragraph or section opens on a word that leans on the previous one ("both", "these readers", "these figures", "described above", "for that"). Name the subject.
- **Register.** Statements of fact in a neutral academic tone; no rhetorical lines, no labelled beats, no bullet lists in the running text of a section. Rounded figures in the prose (41%, 5%, 53%, 9%); exact values in tables and notes. No regulation numbers or exact dates in the narrative. Sentences of about 15 to 18 words with connecting words; do not chop to 11 words.
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

`EDIT_HISTORY.md` records each round of edits, the researcher's response and any open concern; read it before revising a chapter.

| File | Chapter | Status |
|---|---|---|
| `ch1_introduction.md` | 1 Introduction | drafted 12 Oct on the proposal's and deck's flow (opening, 1.1 question and objectives, 1.2 contributions, 1.3 structure); open concern on 1.1 in `EDIT_HISTORY.md` |
| `ch5_results.md` | 5 Results | early draft of 5.1-5.5 in the older report style; to be rewritten to the v3 structure (ten question sections, `research/option_space_2026-10-01/DRAFT_STORY_v2.md`) |
| `ch3_framework.md` | 3 Framework and Hypotheses | first full draft 12 Oct (evening), awaiting the researcher's reading: the chain of stand-ins, terms box (Table 3.1), the measures and the identity, H1, H2, the entry test, further analyses, tests table (Table 3.2); Figure 3.1 still to be drawn |
| `ch2_literature.md` | 2 Literature Review | first full draft 12 Oct (evening), awaiting the researcher's reading: on the proposal's four sections (2.1 pricing and revenue recognition, 2.2 measuring the online economy, 2.3 digital records and third-party information, 2.4 the gap), with the survey-count strand added (breaks, recall, exit, margins). Citations are author-year, every one traced to `REFERENCES_WORKING.md`; the bibliography itself is not yet built |
| `ch4_data_methods.md` | 4 Data and Methods | first full draft 12 Oct (night), awaiting the researcher's reading: platform data and the two groups (Table 4.1), the H1 test, tracing revenue movements, the BPS files and the entry test (Table 4.2), channels, records and reach, the comparison with national and payment figures (Table 4.3), market values, traceability. The appendix it points to (platform list, seven traced windows, registered tests) is not built |
| ch6, ch7 | | not started |
