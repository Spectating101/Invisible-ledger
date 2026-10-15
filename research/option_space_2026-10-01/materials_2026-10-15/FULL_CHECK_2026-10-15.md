# Full check of the thesis, 15 October 2026

Four independent checks, each run by a reader who had not written the text:
- **Numbers:** `AUDIT_NUMBERS.md`, 920 numbers traced to their sources.
- **Consistency:** `AUDIT_CONSISTENCY.md`, cross-references, terms, labels and style.
- **Claims and registration:** `AUDIT_CLAIMS.md`, claim strength and registration integrity.
- **Mock examination:** `MOCK_EXAM.md`, three examiners, likely questions, verdicts.

Earlier inputs: `COLD_READ.md` and `FIX_LIST.md`. I verified the most serious findings myself; the items marked **(verified)** below were checked against the source or the text.

Nothing here has been applied yet. The order follows the researcher's priority: first what stops a reader from understanding the thesis easily, then errors, then integrity, then examiner content, then what is still missing.

---

## Verdict in one paragraph

The thesis is likely to pass, most likely with minor revisions. The mock panel gives about a 95 percent chance of passing: about 55 percent minor revisions and 35 percent major. The weak spot is the finance examiner. The evidence holds up: 893 of 920 numbers match their sources exactly, 9 more match within looser rounding, and every headline number is right. The sentences are easy to read, averaging 16 words, with none of the banned words. What still costs the reader is being told what the thesis is about before reading 26 pages, plus four dense stretches on the survey mechanics. Both are fixable in a day.

---

## A. Readability and ease of understanding (priority)

Ranked by how much each one slows a reader down.

1. **There is no one-page "what this is about".** The thesis has no abstract, so the reader starts Chapter 1 without the map. A plain abstract fixes this, and YZU requires one in English and in Chinese. It should give the question in one sentence, the two findings in two, and why it matters in one. This is the single biggest comfort gain.

2. **Names appear before they are introduced.** GoTo, Grab, Gojek, Sea, Momentum Works, e-Conomy, LSEG and the World Bank Enterprise Surveys each appear with no one-line introduction. Add one clause at first use, for example "GoTo, the Indonesian group that owns Gojek and, until 2024, Tokopedia".

3. **One thing goes by several names.** "Sales" is used for transaction value across Chapter 2. "Pricing" stands for a change in the take rate in 5.3 and 7.1. "Thin share" sits beside "thin take rate". BPS is defined four times. The vocabulary rules in the README already settle each of these; apply them.

4. **The survey mechanics are dense.** 4.7 and 4.8, then 5.7 to 5.9, are where every reader slowed down. The worst passages, in the mock examiner's ranking:
   - **5.7:** "Entrants account for 25 to 30 percent of that rise, and sellers not explained by entry for 15 to 17 percent… That leaves 53 to 59 percent of it with no source in the sellers' answers." It needs one sentence on how the shares were built, and plain nouns.
   - **4.8:** "…so both readings are computed and the one that passes is kept." Three conditions are packed into two sentences.
   - **5.9:** "at about twice BPS's total, while the monthly reading fails at about 23 times." The reader cannot tell that "twice" is the edge of the validation rule.
   - **5.8:** the section's key definition sits inside one relative clause. It needs two sentences and an example.
   - **6.5:** the P1 and P5 reading asks the reader to hold codes and ranges from the table. It needs plain words.

5. **The appendices read like working notes.** They contain tickers instead of names, script paths, internal labels and "working draft". A reader meets them last and judges the whole thesis by them. Rewrite them for a reader and keep the paths in a short note at the end.

6. **Thirteen sentences run over 30 words.** They are listed in `AUDIT_CONSISTENCY.md` Part 7, and most carry an equation or a list. Split the ones without an equation.

7. **Caveats repeat outside Chapter 7.** The rule is that caveats live in 7.4. A few repeat in 5.x and 6.x, and the audit lists them.

What already reads well, and should be kept as the model:
- Ch1's paragraph defining the wedge
- the trip example in 2.1
- the 21.5 percent arithmetic in 3.5
- the 2 percent platform example in 3.2
- "A cap on one fee does not fix the take rate" in 6.2
- the close of Chapter 7

---

## B. Errors to fix before anyone reads

All are small. Each is checked against the source or the text.

| # | Where | Problem | Fix |
|---|---|---|---|
| B1 | 5.1, Table 5.2 note | The 9 and 11 percent results are swapped **(verified)** | "At 9 or 11 percent, the total wedge is US$40.3 or US$39.9 billion" |
| B2 | 6.2 and 5.10 | GoTo's second-quarter revenue growth is "21 percent"; the release says +20 | "about 20 percent" in both |
| B3 | 4.5, 5.4 | The second market-value run is described as "three segment series and three more whole companies" | It is five segment series and Mercado Libre (34 firms) |
| B4 | 6.3 | "17 to 24 percent"; the low end is 17.5 | "about 18 to 24 percent" |
| B5 | Appendix A.3 | Says the text gives 61/39 | The text gives 60/40; align |
| B6 | Appendix B | One row label says "Tokopedia's 2022–23 comparison" | It drops all three 2022–23 pairs; relabel |
| B7 | 5.4, Table 5.1, Appendix C | "Trimmed" | It was winsorised (extremes capped, none dropped) |
| B8 | 5.2, Ch7 | "2021 to 2024" | The sources say the large moves came in 2022–24; use "2022 to 2024" everywhere |
| B9 | 5.2 | The shuffle p = 0.06 is from a different Appendix B row than the test it is reported with | Report the matching shuffle p, or name the row |
| B10 | 5.7 | US$53 billion to US$72 billion reads as +36 percent, but the text says +41 | Say the growth is in rupiah, or give both years at one exchange rate |
| B11 | 4.6 | Promises the H2 split on both BPS counts | 2022–23 has only one count; fix the sentence |
| B12 | 7.4 | Says Shopee and Grab stay out of the tests | Appendix B has one check that includes them; say "out of the main tests" |
| B13 | 7.4 | "The files carry no area variables" | Chapter 5 runs a province analysis; say "no sampling-area or design variables" |
| B14 | 5.10 | "15 million Tokopedia merchants" has no extract or citation | Cite the source or drop the number |
| B15 | 6.2 | "Not yet in force by late August" is cited to an article from 8 July | Cite the August report (CH6_SOURCES 4c) |
| B16 | Ch6 | The August start and stop of the tax have no citation | Cite DJP (1 July) and the 5 August announcement |

---

## C. Integrity: registration and claim strength

These matter most at a defence. A skeptical examiner looks for them first.

1. **X3 could not fail, so it should be withdrawn as a registered test (verified).** X3 predicted that Indonesia's share of formal firms with neither a website nor online tax filing is the highest of seven countries. At registration, the published e-filing shares were already seen, and they cap every other country below Indonesia's 39.9 percent. This is the same problem as the tax-start prediction. Fix: a dated addendum withdrawing X3; the ranking becomes descriptive; Appendix C splits F3 from X3. The 39.9 percent figure stands.

2. **Disclose one fact about the entry test (E5) (checked).** BPS's 2024 publication, in the repository at registration, has a start-year table. It points to a share below 21.5 percent, but only if the seller population was stable between 2023 and 2024. It was first used on 8 October, after the test ran on 7 October, and nothing shows the 2023 shares were known in advance. E5 stands as registered. Add one honest note in Appendix C.

3. **A registered result is missing.** The discount-leverage rule (PREREGISTRATION section B) promised to report its failures. It partly failed: one prediction rests on two cases, one fails, and the out-of-sample rank correlation is 0.20. The thesis does not report it. Add one row to Appendix C and one sentence in 7.3.

4. **An F3 coding fix is not disclosed in the thesis.** A recode turned F3 from failing (13.0 percent) to holding. The registration addendum discloses the recode, but the thesis does not. Add it to the Appendix C note.

5. **Chapters 6 and 7 contradict themselves on the cap.** 6.2 and 7.5 say the predictions will show "how far the cap moved" take rates. 6.5 and 7.4 say they do not measure its effect. Fix 6.2 and 7.5 to say "what the companies' take rates did after the cap".

6. **Four sentences say more than the evidence:**
   - **5.7**, "Sampling noise does not explain the break" → "Sampling noise is very unlikely to explain the break" (the agreed 10 Oct wording).
   - **5.7**, "they added nothing to the rise" → "the typical existing seller reported no growth".
   - **Ch5 opening**, "did not come from sellers entering" → "is not explained by sellers entering".
   - **5.10**, "agree on growth where they cover the same sellers" → "agree that growth was small where they cover the same sellers". The two figures did not move identically.

7. **"Planned in advance" reads as a fourth evidence label.** The narrower H1 test was planned before the wider one, but the proposal had already reported its result. Call it "the narrower test, set before the wider one" and keep the labels to three: registered, exploratory, descriptive.

8. **Votes from overlapping evidence.** "Five of six measures" and "four of seven windows" count overlapping evidence; the windows overlap and two measures share a company. Each already has a note, so make sure the note sits next to the count.

9. **P5 has a gap between 2 and 5 percent** (neither holds nor fails). It is registered that way, so leave it and report it as registered. Table 6.2 now says so.

Clean, so nothing to do:
- The wedge is never called GDP, income or tax.
- The ecosystem ratio is always the author's own measure.
- No business-level licensed data appear.
- The withdrawn tax-start prediction is handled consistently in the thesis files.
- No pointers are broken, numbering is in order, and there are no banned words and no bare rupiah in prose.

---

## D. What the examiners will press (content, not wording)

From `MOCK_EXAM.md`, with the three verdicts:
- **Prof. Kong:** minor revisions.
- **Prof. Thomas:** major revisions, or minor if fixed before the defence.
- **Methods examiner:** minor revisions.

Worth doing, ranked by payoff for effort:
1. **Prof. Thomas: the cap and the wedge.** Add one paragraph of arithmetic to 6.2: what a cut from 20 to 8 percent on rides that are about 6 percent of Grab's mobility transaction value does to the on-demand take rate and the wedge. Also add one short paragraph on who gains and loses (drivers, platforms, the state). This answers both of his oral questions directly.
2. **The methods examiner: does H2 still hold once the extra sellers are taken out?** One recalculation from published figures and Table 5.5: with the 306 to 458 thousand removed from the 2023 count, compute the share of growth from more businesses. This turns the entry test into a direct answer to H2.
3. **Prof. Thomas: the finance contribution.** Adopt the drafted finance paragraph for 1.2 and 7.2 (`FINANCE_FRAMING.md`). In 4.5, say why Grab, GoTo and Sea are not in the market-value sample, or add them if their data allow.
4. **Is H1 about Indonesia, or about young platforms in a repricing period?** The thesis already has the timing check: foreign platforms did not swing more within three years of listing. Move it from the groundwork into 5.2 as one sentence with Appendix B.
5. **Prof. Kong:** add a list of abbreviations, and say the scope (country and business) of the foreign and market-value samples in one line each.

Answered already, from the 1 October defence:
- definitions and readability
- the purpose of the wedge
- the commission cap (partly; see item 1)
- political involvement (partly; see item 1)

Still missing from 1 October: a map of how each platform defines transaction value. A short appendix table would close it.

---

## E. Still to produce

- English abstract, Chinese abstract, Chinese title and keywords (YZU requires all of them).
- Acknowledgements and a list of abbreviations and symbols.
- Section 6.5 results: GoTo on 27 Oct, BPS early November, Grab and Sea mid-November.
- Reference list: 14 details still marked [UNVERIFIED], mostly web addresses and dates; Momentum Works is the most important.
- YZU assembly: number tables and figures straight through, plus the front-matter order, margins and spacing (`YZU_FORMAT.md`).
- Confirm with the program office: English language and citation style.

---

## How it passes

As it stands, the thesis passes. The likeliest outcome is minor revisions. The risk of major revisions comes almost entirely from Prof. Thomas's finance questions and from any integrity point an examiner finds before you disclose it.

Three steps would move it firmly to minor or clean:
1. Disclose and fix the integrity items (C1 to C6) yourself. They are small, and an examiner who finds them first will read everything else less charitably.
2. Write the abstract and make the readability pass in section A. This was the committee's main complaint, and it is now within reach.
3. Add the cap arithmetic and the H2-after-entry answer (D1 and D2). Each is a paragraph, and each answers a question already asked.

Reading time is about two hours for the compact copy. Chapters 3 to 5 carry most of the content, and the dense stretches (4.7–4.8, 5.7–5.9) are where a reader will need to slow down.
