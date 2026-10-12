# Handoff: The Invisible Ledger thesis (state on 12 October 2026)

For any agent or person taking over. Read this file, then the two files it points to in section 3, before changing anything.

## 0. Catch up fast

**Ten-minute path.** (1) This file, sections 0 to 4. (2) `papers/thesis_2026-10/README.md`, the "How to continue" and "Writing rules" parts. (3) `papers/thesis_2026-10/EDIT_HISTORY.md`, Part A (the committee) and Part D (what was tried on chapter 1). (4) `papers/thesis_2026-10/ch1_introduction.md`, to hear the agreed voice. Then start on section 6.

**One-paragraph state.** The proposal passed on 1 October. In the following eleven days the research was finished: the BPS survey files were bought and analysed, the comparison group of platforms abroad grew from 8 to 27 (set against 5 Indonesian and regional platforms), a market test was run, and the story was settled. Since 12 October the work is **writing the thesis**, by hand, in `papers/thesis_2026-10/`. Chapter 1 is drafted. No new analysis is planned; the only research items left are the registered predictions, which are scored on the dates in section 7 and feed chapter 6.

**Things in this repository that will mislead you.**

| Stale item | Why it misleads | Use instead |
|---|---|---|
| Branch `main` | Stops on 1 October; its routing documents are out of date | `proposal/integrated-2026-09-16` |
| September manuscripts (`papers/current/archive/manuscripts_2026-09/`) and `scripts/build_thesis_manuscript.py` | Four hypotheses, older numbers, generated text | `papers/thesis_2026-10/` |
| The 24 September proposal | Has H3 and H4 and a different abstract | The 27 September PDF (H1 and H2 only) |
| "6 of 8 comparisons", "8 platforms abroad", p = 0.002 | True for the proposal's main sample, but no longer the main H1 result | 5 Indonesian and regional platforms vs 27 abroad, p = 0.004 |
| Chart `exhibits/1_inside_the_app.png` ("the cut swings about 3x more") | Reads as larger price changes; that reading was corrected | `exhibits/v2/1_thin_slice.png` |
| `papers/thesis_2026-10/ch5_results.md` | An early draft in a report style the researcher rejected | Rewrite from `DRAFT_STORY_v2.md` under the writing rules |
| `DRAFT_STORY_v1.md`, `DRAFT_STORY_v2.md` | Story drafts; v2 has labelled steps and is scaffolding | Content source only, never pasted as thesis text |
| `research/option_space_2026-10-01/archive/` | The old options map | Parts 1-7 and `FINDINGS.md` |

## 1. What this project is

A master's thesis (MSc Finance, Yuan Ze University) by Christopher Ongko. Advisor: Prof. De-Rong Kong. Examiner: Prof. Thomas. Title: *The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia's Platform Economy*.

The proposal passed its oral on 1 October 2026. The thesis executes that proposal: **same title, research question, two hypotheses (H1, H2) and measures. Do not change them.** The approved proposal is `papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf`; the presented deck is `papers/current/IL_Proposal_Oral_Deck_v4.10_Christopher_Ongko.pptx`.

On 12 October the advisor wrote: focus on the issues she and Prof. Thomas raised; the topic should not change completely; most of all, improve the writing.

## 2. Where things stand

| Area | State |
|---|---|
| Research and evidence | **Complete.** Every number is rebuilt by `research/option_space_2026-10-01/rebuild_all.sh` (272 ledger checks pass). No further analysis is planned. |
| Story | **Settled.** Golden pitch and five-part arc frozen (tags `golden-pitch-2026-10-08`, `narrative-arc-2026-10-09`). |
| Thesis text | **Started.** Chapter 1 drafted and revised over many rounds (introduction and 1.1 reviewed; 1.2 and 1.3 next). Chapters 2 and 3 have first full drafts (12 Oct, evening), awaiting the researcher's reading; a seam pass then aligned Chapters 1 to 3 with each other (vocabulary, the H2 and entry-test spine, order, numbers; see `EDIT_HISTORY.md`, last section). Chapter 5 has an older draft to be rewritten. Chapters 4, 6, 7 not started. |
| Advisor | Progress deck and data package ready (`papers/IL_Advisor_Package_2026-10-12.zip`); the researcher uploads it. The advisor has **not yet seen** the change in what H2 means. |
| Branch | All work is on `proposal/integrated-2026-09-16`, about 140 commits ahead of `main`. **`main` is stale** (it stops on 1 Oct, when PR #9 merged). |

## 3. Read these first

1. `papers/thesis_2026-10/README.md`: how to continue, and the writing rules agreed with the researcher.
2. `papers/thesis_2026-10/EDIT_HISTORY.md`: every concern raised by the committee, the researcher and the independent reviews, what was done, and what is still open.

## 4. What the thesis says (do not drift from this)

- Platform revenue shows a small part of the commerce platforms carry (the invisible wedge), and platforms carry about a fifth of Indonesia's online sales.
- **H1 is rejected:** revenue did not grow in proportion to transaction value. Indonesian platforms changed what they keep by about as much as platforms abroad, but they keep a much smaller share of each sale, so the same change moved their revenue about three times as much. Much of the change was fewer discounts.
- In 2023, the headline figures described a boom; buying through platforms mostly did not grow, and sellers reported a hard year.
- **H2 holds on BPS's published numbers,** but about half of the 2023 increase in online sellers is **not explained by first-time entry** (a test written down before the survey files were opened). The additional count was concentrated among older, long-established small businesses selling through messaging and social media. Sellers returning after a break is the open alternative; it is checked, not ruled out.
- Indonesia's new rules reach only what their figures cover: the marketplace tax can collect from about one online seller in twenty.

Frozen wording of the pitch: `research/option_space_2026-10-01/GOLDEN_PITCH.md` (read its dated notes; one sentence was repaired on 10 Oct).

## 5. Map of the repository

| What | Where |
|---|---|
| Thesis chapters in progress | `papers/thesis_2026-10/` |
| Approved proposal and oral deck | `papers/current/` |
| Advisor package (deck, charts, data workbook) | `papers/advisor_package_2026-10/`, zipped at `papers/IL_Advisor_Package_2026-10-12.zip` |
| All evidence, scripts, tables, charts | `research/option_space_2026-10-01/` |
| Every number in one place | `research/option_space_2026-10-01/FINDINGS.md` |
| Groundwork per chapter, with dated corrections | `PART1_…` to `PART7_…` in that folder (frozen; changes only as dated notes) |
| Story drafts (v1 prose, v2 labelled steps: scaffolding, not print text) | `DRAFT_STORY_v1.md`, `DRAFT_STORY_v2.md` in that folder |
| Order of the story | `NARRATIVE_ARC.md` in that folder |
| Tests registered before the data | `PREREGISTRATION.md` in that folder |
| What goes in main text, appendix, reserve | `CUT_LIST.md` in that folder |
| References with what each supports | `REFERENCES_WORKING.md` in that folder |
| Charts (print and slide versions) | `exhibits/`, `exhibits/v2/`, `exhibits/deck/`; built by `exhibits.py`, `exhibits_v2.py` |
| Progress deck and its build script | `research/option_space_2026-10-01/deck/` |
| Independent reviews (Codex, ChatGPT) | `research/independent_review_2026-10-08/`, `research/independent_review_2026-10-09/` |
| Licensed data: what is off the repository and why | `research/option_space_2026-10-01/LICENSED_DATA.md` |
| Which file is canonical | `CANONICAL_ARTIFACTS.md`, `AGENTS.md` |

## 6. Next steps, in order

1. Recheck section 1.2 (contributions) of chapter 1 against the ambition paragraph in 1.1.
2. Chapters 2 and 3 have first drafts (`ch2_literature.md`, `ch3_framework.md`) and Chapters 1 to 3 have had a seam pass; revise from the researcher's reading, then write chapter 4. **Chapter 4 owes the reader**: both groups for the H1 test (Indonesian platforms and the foreign benchmark); the entry-test rule; the data behind each test; how revenue movements are traced to fees and discounts (Objective 2); how the platform evidence is compared with national and payment figures (Objective 3).
3. Rewrite chapter 5 as ten sections, each answering one question, using `DRAFT_STORY_v2.md` for content and the writing rules for form.
4. Write chapters 2, 6 and 7. Chapter 6 waits for the scheduled results below.
5. Insert citations; format to the YZU template (the researcher obtains it).

## 7. Dates outside our control

| Date | Event | What to do |
|---|---|---|
| 27 Oct 2026 | GoTo 3Q26 results | Score the registered predictions (`score_q3_2026.py`, `PREREGISTRATION.md`) |
| 1 Nov 2026 | Marketplace tax due to start (registered expectation: it slips) | Record what happened |
| Early Nov 2026 | BPS 3Q26 GDP | Score prediction R2 |
| Mid Nov 2026 | Grab and Sea 3Q26 results | Score the remaining predictions |
| About December 2026 | Thesis defence | — |

## 8. Rules that must not be broken

- **Licensed data.** BPS survey microdata, LSEG market values and World Bank survey files are never committed, uploaded or shared. Only national totals and test results are. The raw files exist only on the researcher's machine; a cloud session cannot rerun the scripts that need them and should not try.
- **No contact with BPS** by email or otherwise (the researcher's decision).
- **Credentials and payments** are handled by the researcher, never in chat.
- **No new hypothesis, no new concept.** Improvements go through what the proposal promised. The entry test is presented as closing a limit the proposal itself named.
- **No overclaiming.** Unsupported lines are dropped, not propped up. The claim wording to avoid is listed in the thesis README.
- **Frozen files** (`PART1`-`PART7`, `GOLDEN_PITCH.md`, `NARRATIVE_ARC.md`) change only through dated notes at the end.
- **Do not push to `main`** or merge the working branch into it without the researcher saying so. PRs #6, #7 and #8 are old drafts; leave them.

## 9. How the researcher works

- Prefers explanations in chat; files only when asked or when they are the deliverable.
- Wants honest assessments and pushback when a request would weaken the thesis; does not want reassurance.
- Judges the writing by ear: expect to be corrected on flow and tone, and record each round in `EDIT_HISTORY.md`.
- Cheap checks on existing data are always worth running; new analysis is not wanted now.
- **Readability comes before safety.** On 12 Oct (evening) the researcher said he does not want flags on the ambition paragraph ("technically no evidence, it is an educated guess, I am not going for safer options"), and that a safer claim that makes a sentence convoluted is the very thing Prof. Kong and Prof. Thomas complained about. So: the ambition and framing stay bold and are not flagged; support goes in notes or later chapters, never into hedged prose; flag a sentence only when it makes a different claim, once. This sits beside section 8: statements of what the data show keep their evidence strength; the framing is bold by design.
- **He reviews before and after.** Show the change as before and after in chat, apply only what he approves, commit once per round, log it in `EDIT_HISTORY.md`. To assess a passage: print the full text with numbered paragraphs, say what each paragraph does and whether it hands over to the next, then list only reading problems, ranked.
- **Vocabulary is fixed** (thesis README, Vocabulary rule): wedge, not gap; transaction value, with "the commerce a platform carries" as its plain companion; figure for a published number, measure for a yardstick; count of online sellers; entry test. New chapters use these words; run a sweep for the old ones before sending a chapter.
- **Style settled in this round** (full list in the thesis README, Writing rules): paragraph openers name their subject; a movement gets its mechanism in the paragraph that explains it; one currency (US$, rounded, World Bank rate for the year); no bare rupiah in the narrative.

## 10. Open items

- The advisor has not yet seen the H2 framing (progress deck, slide 14 asks her).
- Section 1.1 should be "brief, yet impactful" as standard prose; two attempts were rejected (`EDIT_HISTORY.md`, Part D).
- Citations are not yet in the chapter text.
- The YZU template is not yet in the repository.
- Chapter 1: the introduction and 1.1 were reviewed and revised on 12 Oct (evening); 1.2 and 1.3 were then rebuilt in the seam pass and have not yet been read by the researcher. Section 1.1 is 28 words longer than before (+7 percent) against the open wish for it to be brief; cut candidates are in `EDIT_HISTORY.md`.
- Chapter 3 now gives each link of the chain its own condition (inner: take rate steady; outer: national growth comes from sellers the platforms record; the count: survey keeps reaching the same sellers). The advisor has not yet seen how H2 is framed, so confirm this wording with the researcher before it goes to her.
- Root-level files not part of the thesis are untracked and should be left alone (`side-academic-papers-*.zip`, `ssrn-7514022.pdf`, `Attraction-json_2026-10-09.zip`, a Chinese-named PDF).

## 11. Notes for a cloud or fresh session (added 12 Oct after a cloud session's first read)

- **Fetch the full history first.** A shallow clone of `main` shows only 14 Sep to 1 Oct and leads to a wrong picture (old manuscripts, H1-H4, "6 of 8", the 24 Sep proposal). The live work is on `origin/proposal/integrated-2026-09-16`.
- **Base your work on `origin/proposal/integrated-2026-09-16`.** If the session was assigned a branch cut from `main` (for example `claude/...`), move it to the tip of the integrated branch before the first commit, and open any pull request **against the integrated branch, not `main`**.
- **Numbers.** Take them only from `research/option_space_2026-10-01/FINDINGS.md`, the Part 1-7 files with their dated notes, and section 4 above. H1 now rests on 5 Indonesian and regional platforms against 27 abroad (p = 0.004); the proposal's 8-platform comparison is the earlier version. Anything from the 24 Sep proposal, the September manuscripts or `main`'s routing documents is out of date.
- **Two notes exist only on `main`:** `docs/MEASUREMENT_PROXY_FRAMEWORK_2026-09-23.md` and `docs/PAPER_COMPARISON_BASELINE_2026-09-23.md`. Both predate the 27 Sep proposal: the first is the "adequate proxy" framing of the 24 Sep lineage (superseded by the stand-in conditions in Part 2), the second ranks the researcher's wider set of papers. Neither is needed for the thesis; leave them on `main`.
- **Do not run or trust the old generators** (`scripts/build_thesis_manuscript.py`, proposal surgery scripts). The thesis is written by hand in `papers/thesis_2026-10/`.
- **Working with two sessions.** A cloud session works on its own branch (`claude/happy-pascal-uc2eya` this time), kept at the tip of the integrated branch. It sends changes back by pull request into the integrated branch when the researcher asks, never into `main`. Only one session edits the thesis files at a time; fetch before editing.
- **First task:** section 6, step 1 (recheck section 1.2 of chapter 1), then chapters 3 and 4. Log each round of the researcher's feedback in `papers/thesis_2026-10/EDIT_HISTORY.md`.

## 12. Timeline

Entries before October come from the repository history and file metadata, as reconstructed by a cloud session on 12 October.

| When | What happened |
|---|---|
| Dec 2025 to Jan 2026 | Origin of the idea; an early paper with large wedge and GDP claims, later withdrawn. An abstract was accepted at the National Tax Association conference (not attended) |
| Aug to early Sep 2026 | Prof. Kong marked up two drafts (about 20 comments each); on 8 Sep the scope was reset to Indonesia |
| 9 to 17 Sep | Evidence backend and results ledger built; proposal rebuilt several times |
| 21 to 24 Sep | The 24 September proposal (with H3 and H4), later superseded |
| 27 Sep | **The active proposal** (H1 and H2 only) |
| 1 Oct | Proposal oral passed. Prof. Thomas and Prof. Kong raised the points in `EDIT_HISTORY.md` Part A. PR #9 merged into `main` |
| 1 to 4 Oct | Quarterly data, tests registered before the data, World Bank tests, the 27-platform comparison |
| 2 Oct | The BPS tests (including the entry test) registered, before the files were opened |
| 6 to 7 Oct | BPS survey files bought and analysed; results committed on 7 Oct |
| 8 Oct | Groundwork Parts 1-7 frozen at version 4; first independent review adopted; market test; golden pitch frozen |
| 9 Oct | Narrative arc frozen; seller profile; returning-seller check; thin-slice check; progress deck built |
| 10 Oct | Claim repairs after the second independent review |
| 12 Oct | Prof. Kong's message; thesis rewrite started; chapter 1 went through about 14 rounds; this handoff written |

## 13. Numbers at a glance

Exact values for tables and notes; the running text uses rounded figures. Source for all: `FINDINGS.md` and the Part files, unless a script is named.

| Topic | Numbers |
|---|---|
| Invisible wedge, 2023, three platforms | Transaction value US$43.23bn, revenue US$3.16bn, wedge US$40.07bn, ecosystem ratio 12.7; revenue about 7% of transaction value |
| Platforms' share of online sales (BPS survey) | 16-26% |
| H1 | 5 vs 27 platforms; yearly change in the take rate 0.20 vs 0.06 (log points), p = 0.004; leave-one-out worst p = 0.016; growth divergence 27.0 vs 6.5 points, p = 0.005; main sample alone p = 0.06 (a different test); quarterly version fails, p = 0.19 |
| Thin slice (exploratory) | Take rate 1.6% vs 16.9% (medians); yearly change about 1.0 point in both (p = 0.65); D = (1 + gV)(m1 - m0)/m0 |
| What moved revenue | Take rate was 66.5% of the movement in Indonesia vs 26.7% abroad (share of absolute log components) |
| Tokopedia 2022-23 | Transaction value -8.9%, revenue +53.2%; lower incentives explain 60.6% of the rise |
| Market test | 28 firms, 138 firm-years; b = 0.60, p = 0.002 for transaction value; second prediction not supported (b = 0.33, p = 0.20) |
| 2023 headline figures | BPS online sales +40.6%, online sellers +27.4% (about 819,000); Bank Indonesia -4.7%; household spending +9.4%; 5 of 6 measures of buying through platforms below household spending |
| Sellers' answers, 2023 | 24% up, 44% same, 32% down; "lack of demand" 41% (35% in 2022) |
| Entry test (registered) | Needed 21.5% starting in 2023; observed 13.45%; 513,000 first-time sellers; 37-56% of the rise not first-time entry; 4.6 standard errors in a sampling-error check (2.3 at twice the error) |
| Who the extra sellers were (exploratory) | Opened before 2010: 41% vs 18%; owner 50+: 41% vs 29%; outside Java: 36% vs 24%; food or making goods: 53% vs 39% |
| Returning-seller check (exploratory) | Part-year selling among sellers who started by 2021: 472,000 to 318,000 |
| Tax reach | About 5% of online sellers taxable (upper bound), holding 17-24% of online sales; marketplace sellers 17.8% of sellers; 13.5% of the rest want to join a marketplace |
| Size of the market, 2024 | BPS Rp1,289tn; Bank Indonesia Rp487tn; tax at 0.5% on Rp204tn to Rp983tn gives Rp1.0-4.9tn |
| Global | Business e-commerce sales almost US$27 trillion in 2022, 43 economies (UNCTAD 2024) |

## 14. Codes and names you will meet

| Code or name | Meaning |
|---|---|
| V, R, m, W, E, D | Transaction value; revenue; take rate (R/V); invisible wedge (V - R); ecosystem ratio (W/R); growth divergence (growth of R minus growth of V) |
| E1 to E8 | Tests on the BPS survey files, registered 2 Oct. **E5 is the entry test**; E6 concerns sellers already in business |
| M1, M2 | The market-value tests (M2 held, M1 did not) |
| Q1 | H1 with quarterly data (did not hold) |
| W1-W3, F1-F3 | World Bank survey tests (informal and formal firms) |
| S1-S3 | Spin-off tests across other countries (S1 and S2 did not hold: the pattern is not universal) |
| P1-P5, R1-R3 | Predictions for the third-quarter 2026 results, scored on the dates in section 7 |
| "Version 4" | The current state of the frozen groundwork Parts 1-7 (tag `parts-1-7-v4-frozen-2026-10-08`), plus dated notes |
| BPS; BI | Indonesia's statistics office; Bank Indonesia (the central bank) |
| SILASTIK; SPPD | BPS's data service; the signed data-use statement for the survey files |
| PMK 37/2025; Permendag 31/2023; Permendag 19/2026; Perpres 27/2026 | The marketplace tax; the 2023 ban on transactions in social media apps; the 2026 trade rule limiting discounts; the ride-hailing commission cap (text not published, cited as announced) |

## 15. What Prof. Kong asks for, from her markups

Define every term at first use; use one term and one currency throughout; explain every table in the text; state each sample's scope; say plainly which measures are the author's own (the ecosystem ratio is); and above all make it easier to read. These matter most in chapters 3 and 4.

