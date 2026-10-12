# Handoff: The Invisible Ledger thesis (state on 12 October 2026)

For any agent or person taking over. Read this file, then the two files it points to in section 3, before changing anything.

## 1. What this project is

A master's thesis (MSc Finance, Yuan Ze University) by Christopher Ongko. Advisor: Prof. De-Rong Kong. Examiner: Prof. Thomas. Title: *The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia's Platform Economy*.

The proposal passed its oral on 1 October 2026. The thesis executes that proposal: **same title, research question, two hypotheses (H1, H2) and measures. Do not change them.** The approved proposal is `papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf`; the presented deck is `papers/current/IL_Proposal_Oral_Deck_v4.10_Christopher_Ongko.pptx`.

On 12 October the advisor wrote: focus on the issues she and Prof. Thomas raised; the topic should not change completely; most of all, improve the writing.

## 2. Where things stand

| Area | State |
|---|---|
| Research and evidence | **Complete.** Every number is rebuilt by `research/option_space_2026-10-01/rebuild_all.sh` (272 ledger checks pass). No further analysis is planned. |
| Story | **Settled.** Golden pitch and five-part arc frozen (tags `golden-pitch-2026-10-08`, `narrative-arc-2026-10-09`). |
| Thesis text | **Started.** Chapter 1 drafted and revised over many rounds. Chapter 5 has an older draft to be rewritten. Chapters 2, 3, 4, 6, 7 not started. |
| Advisor | Progress deck and data package ready (`papers/IL_Advisor_Package_2026-10-12.zip`); the researcher uploads it. The advisor has **not yet seen** the change in what H2 means. |
| Branch | All work is on `proposal/integrated-2026-09-16`. **Not on `main`** (PR #9 is open). |

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
2. Write chapter 3 (terms in one box, the growth formula, H1, H2, the entry test) and chapter 4 (data and tests).
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
- **Do not push to `main`** or merge PR #9 without the researcher saying so.

## 9. How the researcher works

- Prefers explanations in chat; files only when asked or when they are the deliverable.
- Wants honest assessments and pushback when a request would weaken the thesis; does not want reassurance.
- Judges the writing by ear: expect to be corrected on flow and tone, and record each round in `EDIT_HISTORY.md`.
- Cheap checks on existing data are always worth running; new analysis is not wanted now.

## 10. Open items

- The advisor has not yet seen the H2 framing (progress deck, slide 14 asks her).
- Section 1.1 should be "brief, yet impactful" as standard prose; two attempts were rejected (`EDIT_HISTORY.md`, Part D).
- Citations are not yet in the chapter text.
- The YZU template is not yet in the repository.
- Root-level files not part of the thesis are untracked and should be left alone (`side-academic-papers-*.zip`, `ssrn-7514022.pdf`, `Attraction-json_2026-10-09.zip`, a Chinese-named PDF).
