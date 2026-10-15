# Mock oral examination: "Invisible Ledger" (MSc Finance, Yuan Ze University)

Date of mock: 15 October 2026. Text examined: `papers/thesis_2026-10/reading/thesis_reading_copy_2026-10-15.md` (Chapters 1 to 7, Appendices A to D, references). The panel read only that file before writing Parts 1 and 2. `papers/thesis_2026-10/EDIT_HISTORY.md` Part A was read afterwards, for Part 3 only.

This is a simulation. The examiners' names are the real committee's, but the reports are written to anticipate their concerns. They are not their words. Every section number and figure quoted below comes from the reading copy.

---

## 1. Examiners' written reports

### 1.1 Prof. De-Rong Kong (advisor)

**Summary of the thesis.** The thesis asks how much commerce a platform's revenue leaves out, and when that choice changes the conclusion about growth. On the platform side it compares the size of yearly take-rate changes for five Indonesian and regional platform series with 27 listed platforms abroad. It rejects H1 and splits revenue moves into commerce, fees and incentives. On the national side it splits BPS's online sales growth into businesses and sales per business (H2 holds). It then runs a registered entry test on the BPS survey files, which fails: about half of the 2023 rise in the seller count is not first-time entry. Chapter 6 maps Indonesia's 2026 rules to the part of the figures each acts on.

**Strengths.**
1. The writing has improved greatly since the proposal. Sentences are short (my count: mean about 16 words, median 16). Each paragraph opens with its point, and the tone is no longer defensive. I could follow Chapters 1, 3 and 6 without rereading.
2. Terms are defined once, in Table 3.1, with plain meanings. The ecosystem ratio is stated twice to be the author's own measure (Sections 3.1, 3.2).
3. Every sample's scope is stated for the Indonesian series (Table 4.1), including the regional scope of Grab and the Vietnam part of GoTo.
4. Findings are given at economic scale: a wedge of about US$40 billion, a tax worth US$60 to 300 million a year, 306 to 458 thousand extra sellers.
5. Each result carries a label: registered, exploratory or descriptive. Failed predictions are reported in their own section (7.3). This is unusually honest for a master's thesis.

**Major concerns.**
1. **Not every term is defined at first use.** GoTo, Grab, Gojek and Sea are never introduced as companies: what they are, where they are listed, what they do. GoTo first appears as a citation in Chapter 1, Grab in Section 4.1, and Gojek only in Section 5.9. Momentum Works is used in Section 4.2 and explained only in Table 4.3. "Rank correlation" is defined in Section 5.7, one sentence after its first use. "One-sided" is never explained in plain words.
2. **One term for one thing.** Transaction value is defined well, but the text also calls it "the commerce a platform carries", "platform commerce", "buying through platforms" and "sales". Table 3.1 allows "seller", "business" and "online seller" as synonyms. A reader in a second language will wonder whether these are different objects. Pick one term per object and keep it.
3. **The appendices are not yet thesis text.** Appendix A.1 lists tickers (ACVA, ASAPQ, DIBS, HEPS...) and says "full company names are to be added". Appendix A.4 uses internal labels ("conditional country reconstruction", "direct issuer scope pending"). These do not match the labels of Table 4.1 ("Direct segment disclosure", "Direct company disclosure") or Section 4.10. Appendices B and D cite code files (`tables/...json`, `h1_extended.py`) and say "Details moved from Chapter 5" and "working draft, 13 Oct". Move file paths into one replication note, and use the same labels everywhere.
4. **The scope of the foreign and market-value samples is incomplete.** Which years do the 27 foreign platforms cover? Which countries are they listed in? Which years make up the 138 market-value platform-years? Which seven countries are in the World Bank comparison (only Malaysia and Thailand are named)?
5. **Finance literature is thin for an MSc Finance thesis.** Bowen et al., Davis, Trueman et al., Rajgopal et al., Givoly et al. and Berg et al. are all relevant, but most are from 2000 to 2003. Add recent work on how markets use non-financial performance measures (key performance indicators) and how platforms are valued. Also add work on platform pricing after funding tightened.

**Minor concerns.**
- There is no abstract in the reading copy. There is also no list of abbreviations (BPS, GTV, GMV, TPV, QRIS, LSEG, IFRS, DAC7).
- Section 1.1 opens with "This thesis sets out to change how the digital economy is measured" and "Decisions worth trillions of dollars rest on numbers...". This is a larger claim than the evidence supports, and it has no citation. Keep the ambition, but tie it to Indonesia and to what was measured.
- Chapter 1 gives only one view of Tokopedia: "about 60 percent of the extra revenue came from smaller discounts". Table 5.4 measures per unit of transaction value and finds that higher fees led (76 against 45). Section 5.3 explains the two views well, but the introduction should not favour one of them.
- The exemption is given as about US$34,000 (2022 rate, Sections 4.8 and 6.3) and as about US$32,000 (2024 rate, Table 6.1 note). One home figure is enough.
- Table 5.3 does not give units for "27.0" and "6.5" (they are percentage points of growth divergence).
- Table 4.3 and Table 6.1 are explained only by a lead-in sentence. Add one sentence on what the reader should take from each.
- Fourteen references are marked [UNVERIFIED]. One is the Momentum Works report, and half of the US$43 billion headline rests on it.

**Required revisions.** (1) Introduce each company at first use. (2) One term per object; trim the synonyms in Table 3.1. (3) Rewrite the appendices as thesis text: full names, consistent labels, no file paths in the body. (4) Give the scope (countries, years) of the foreign, market-value and World Bank samples. (5) Add an abstract and a list of abbreviations. (6) Add five to eight recent finance references, and engage with them in Sections 2.1 and 5.4. (7) Resolve the [UNVERIFIED] entries, starting with Momentum Works.

**Verdict: pass with minor revisions.**

---

### 1.2 Prof. Thomas (examiner, finance)

**Strengths.**
1. The question matters to finance. Investors are given revenue and GTV and must decide which growth is real. Equation (5) splits revenue growth into commerce and take rate using two public numbers. It is simple and portable, and it is useful to an analyst.
2. The answer to my proposal-stage question, "the wedge is just subtraction", is better now. Section 3.2 shows that the ecosystem ratio sets how far a one-point change in the take rate moves revenue growth. Section 5.2 then shows that the Indonesian and regional difference is mostly this thin-take-rate effect (about 1 point a year in both groups, p = 0.65). That is an honest and interesting result.
3. Chapter 6 now treats the commission cap concretely. The cap covers two-wheel rides only. That slice is about 7 percent of GoTo's group net revenue and about 2 percent of Grab's on-demand transaction value. GoTo cut incentives before the cap took effect, and its take rate rose from about 18 to about 22 percent.
4. Causal language is mostly controlled. The splits are "accounting, not causes" (Section 7.4). The market-value result is "an association" (Sections 4.5 and 7.4).

**Major concerns.**
1. **The finance contribution is the weakest part.** The only test that involves markets (Section 5.4) has 28 platforms, and just one is Indonesian (Bukalapak). Its central prediction, that markets value take-rate growth less, fails in the main sample (p = 0.20). It "holds" only in a run that the candidate herself sets aside. So the thesis tells an investor that revenue is a poor guide in Indonesia, but it has no market evidence from Indonesia. The candidate must explain why Grab, GoTo and Sea, all listed and all reporting GMV or GTV, are missing from the main market-value sample (Section 4.5 says only that it "lacks" Sea). If the answer is data, say so. If they can enter, they should.
2. **Inference on the market-value regression.** There are 28 clusters and 138 observations, with year effects, a one-sided test, and market value that includes share issuance. With so few clusters, conventional clustered standard errors are too small. Report a wild cluster bootstrap, or at least note the problem. Also consider log changes in enterprise value, or market value per share, to deal with share issuance (Section 7.4 notes the issue but does not fix it).
3. **Is this Indonesia, or life-cycle stage?** The Indonesian and regional platforms are young and mostly listed in 2021 and 2022. Their take rates moved as they changed from chasing growth to chasing profit. The foreign group is mostly mature. The most "Indonesian-like" foreign platform is Sea/Shopee, a Southeast Asian firm, with the largest median change abroad (0.25, Appendix A.1). Quarterly pairs after 2023 do not reject H1 (Section 5.2). This suggests a regional, period-specific repricing, not an Indonesian trait. The thesis half-says this (Section 7.3: "a period, 2021 to 2024"). Its framing in Chapter 1 ("In Indonesia, platform revenue also grew faster...") should match.
4. **The commission cap and the wedge: finish the arithmetic.** The thesis defines the wedge as what passes to "sellers, drivers and others" (Section 7.4). A cap from about 20 to 8 percent on a ride moves money from revenue into the wedge one for one, and raises the ecosystem ratio for that service. Say so in one paragraph. Give the size: a cap on a slice of 2 to 7 percent of the measure. The registered predictions (Section 6.5) are not yet scored. If the defence comes before mid-November, the chapter must say plainly what is pending.
5. **Political economy and the players.** The proposal question was about political involvement and who the players are. Chapter 6 maps each rule to the number it acts on, which is useful. But it does not describe the players' interests: drivers, platforms, ministries, the tax office, sellers. Nor does it say why each rule took the form it did. One example is that the government declined to cap marketplace fees but capped one ride fee. A short subsection on who gains and who loses from each rule, tied to equation (6), would answer this without causal claims.

**Minor concerns.**
- Shopee Indonesia's revenue is set at an assumed 10 percent take rate, against Tokopedia's 2.5 percent. Why is Shopee's take rate four times Tokopedia's? Is it advertising, logistics, or a scope difference? Readers will ask.
- Blibli's 2022–23 revenue growth (+465 percent, from a 0.54 percent take rate) looks like a recognition or scope change. Appendix A.4 itself labels Blibli "scope pending". Say how much of the H1 result depends on Blibli. Appendix B shows that dropping it gives p = 0.014, so the answer is "not much". That belongs in Chapter 5.
- "Pricing, not more commerce, moved revenue" (Section 5.3) sounds causal. "Pricing accounts for most of the revenue move" is accurate.
- Section 3.4 describes the foreign group as platforms "where revenue and transaction value broadly move together". That assumes the result. Describe them by what they are.

**Required revisions.** (1) Explain the composition of the market-value sample, and add Grab, GoTo and Sea if the data exist. (2) Report small-cluster-robust inference for equation (8). (3) Add a paragraph or a check on the life-cycle and regional alternative (for example, Sea moved into the regional group, or years since listing). (4) Add the cap-to-wedge arithmetic in Section 6.2. (5) Add a short paragraph on the players' interests in Chapter 6. (6) Restate the finance contribution modestly in Sections 1.2 and 7.2: a portable split of revenue growth and a sensitivity result, plus one market association.

**Verdict: pass with major revisions** (borderline minor if items 1, 3 and 4 are fixed before the defence).

---

### 1.3 Third examiner (methods)

**Strengths.**
1. **The entry test is the best idea in the thesis.** It is simple and registered before the files were opened. The threshold is derived transparently (27.4 / 127.4 = 21.5 percent, Section 3.5). The bias argument (recall error pushes toward passing) is correct and makes the failure conservative. It is a reusable check for any survey that asks a start year.
2. Inference respects dependence. One median per platform avoids treating 15 pairs as independent (Section 4.3). Exact rank tests and shuffle tests are both reported, and Appendix B gives a full leave-one-out set.
3. The survey files are validated against published totals (within 1 percent) and against two published shares before any test (Section 4.6). This is good practice.
4. The cohort logic (a cohort can only shrink) is a clean identifying idea. The check against the 2024 published table, where the count "behaved normally again", is persuasive.
5. Registered, exploratory and descriptive results are kept apart throughout. The quarterly test (Q1) is honestly reclassified as a robustness check in Appendix C.

**Major concerns.**
1. **H2 after the entry test.** The thesis reports that H2 holds (71 percent extensive margin). It then shows that 37 to 56 percent of the rise in the count is not entry. It never asks the obvious next question: does H2 still hold on the part of the count that is entry? Saying "the split is arithmetic" (Section 3.4) is true but does not answer it. Either recompute the split under the two exit scenarios, or explain why it cannot be done. If the reason is that the 2024 file has no revenue amounts (Section 7.4), say so where H2 is reported, and state what the result means for H2.
2. **The H1 benchmark defines the hypothesis.** H1 is stated in absolute terms ("grow in proportion"), but it is tested relative to a foreign group. The foreign group is heterogeneous: travel, freelance, resale, food delivery. Tokopedia contributes a single pair, yet its median counts the same as eBay's four pairs or Expedia's eleven. State the test as relative in the hypothesis or in Table 3.2. Report how the result depends on platforms with one or two pairs.
3. **The main H1 test is exploratory, and the registered one is weak.** With three platforms against eight, the registered test gives p = 0.024 by rank test, but its shuffle comes close without passing (p = 0.06). All tests are one-sided. The candidate handles this honestly (Section 7.4), but Chapter 1 and Section 7.1 state "H1 is rejected" without the qualifier. The verdict should carry "exploratory" wherever it is stated.
4. **The value side of the survey rests on fragile brackets.** The validation rule accepts a middle scenario between half and double BPS's total. The annual reading passes "at about twice BPS's total" (Section 5.9), which is at the edge of the rule. Value shares, the 1-in-5 marketplace share, and the tax reach of 17 to 24 percent of value all inherit this. Show the result if the rule were "within 50 percent".
5. **Section 5.7 on value is not traceable.** It says entrants account for 25 to 30 percent of the 2023 rise in value, and that 53 to 59 percent has no source. But Section 7.4 says the 2024 file (describing 2023) has no revenue amounts. How were entrants' values computed? This paragraph needs a method sentence in Section 4.7, or it should be cut.
6. **Why was BPS not asked?** A frame change is the leading explanation (Section 5.7). The thesis says it "did not contact BPS" (Section 7.4). A one-paragraph query to BPS about the 2024 round's sampling frame and listing could settle it. If the data-use agreement forbids contact, say so.

**Minor concerns.**
- Registration is in the author's own repository, dated by commits (Appendix C). Commit dates can be rewritten. A public timestamp, such as the Open Science Framework or a signed tag pushed to a public host, would strengthen the "registered" label. At least state that the repository history was not rewritten.
- The shuffle test's statistic is not named (difference in medians? rank sum?). This explains why the shuffle p (0.022) differs from the Mann–Whitney p (0.004).
- The sampling-noise check applies one year's error rates to both years and assumes independent samples (Section 5.7). Overlapping areas would make the error of the change smaller, so the 4.6 figure is probably conservative. Say which way the bias runs.
- The 5 percent exit rate comes from one cohort over one interval. Show sensitivity at 3 and 8 percent.
- Quarterly pairs compare each quarter with the same quarter a year earlier, and they overlap. They are strongly autocorrelated, so p = 0.19 has very little power. Say so.

**Required revisions.** (1) Report H2 after removing the extra sellers, or explain why that cannot be done. (2) State the H1 test as relative, and report the weight of single-pair platforms. (3) Carry the label "exploratory" into every statement of the H1 verdict. (4) Add the method behind the value figures in Section 5.7, or remove them. (5) Add the bracket and exit-rate sensitivities. (6) Name the shuffle statistic.

**Verdict: pass with minor revisions.**

---

## 2. The 15 most likely oral-defence questions (ranked by likelihood)

Strength scale: **strong** = the thesis gives a clear, defensible answer; **partial** = the material is there but must be assembled or conceded; **weak** = the thesis does not answer it.

**Q1 (Thomas). "Your wedge is 97 to 99 percent of transaction value. Is W just V by another name? What does it add?"**
Where: Sections 3.2, 5.1, 1.2. Strength: **partial**.
Model answer: "Yes, at a thin take rate the wedge is almost all of transaction value. It measures size, and on its own it is not the test. Its size next to revenue, the ecosystem ratio, is what matters for growth. Equation (4) shows that a 1-point rise in the take rate lifts revenue by about 50 percent when the platform keeps 2 percent, and by about 6 percent when it keeps 17 percent. Growth divergence (D) then carries the test of H1."

**Q2 (Thomas). "The ride-hailing commission was capped from about 20 to 8 percent. How does that bear on the wedge and on your results?"**
Where: Sections 6.1, 6.2, 6.5. Strength: **partial** (the slice is sized; the direct wedge effect is not stated; the outcomes are unscored).
Model answer: "The cap acts on the fee rate in equation (6). It moves money from revenue into the part that passes to drivers, so for that service the wedge and the ecosystem ratio rise. But it covers only two-wheel rides: about 7 percent of GoTo's group net revenue and about 2 percent of Grab's on-demand transaction value. Before the cap, GoTo cut incentives and its take rate rose from about 18 to 22 percent. My registered predictions P1 to P5 will show from late October how far the cap moved the reported take rates."

**Q3 (Methods / Thomas). "Five platforms against 27, one-sided tests, and Tokopedia has one pair. How can you reject H1?"**
Where: Sections 4.3, 5.2, 7.4; Appendix B. Strength: **strong** on robustness, **partial** on framing.
Model answer: "Each platform gives one median, so pairs are not counted as independent. The rank test gives p = 0.004 and the shuffle p = 0.022. Dropping any one platform, Ozon, Zalando, or the eight foreign platforms that book discounts as marketing costs keeps p at or below 0.016. A two-sided test would roughly double p and stay below 1 percent. I label the main test exploratory because it was set up after the narrower registered test. That test points the same way (p = 0.024), though its shuffle gives only p = 0.06."

**Q4 (Methods / Thomas). "In percentage points the groups do not differ (p = 0.65). Isn't the H1 rejection just a small denominator?"**
Where: Sections 3.2, 5.2, 7.1. Strength: **strong** (the thesis makes this its own finding).
Model answer: "Yes. That is the finding, not a flaw. Both groups move their take rates by about 1 point a year, but Indonesian and regional platforms start from about 1.6 percent against about 17 percent. For revenue as a guide to commerce, the relative change is what matters, because revenue growth equals the relative change in the take rate plus volume growth. So the same pricing behaviour makes revenue a much worse guide where the take rate is thin."

**Q5 (Thomas). "What is the finance contribution? Your market-value prediction failed."**
Where: Sections 1.2, 5.4, 7.2, 7.3. Strength: **partial**.
Model answer: "There are three parts. First, a split of revenue growth into commerce and take rate that any investor can compute from two public numbers. In Indonesia the take rate accounts for about two thirds of a revenue move, against about a quarter abroad. Second, a sensitivity result: the thinner the take rate, the more ordinary fee or incentive changes move revenue growth. Third, a registered market test. Market value moves with transaction value (0.6, p = 0.002), but I find no evidence that markets discount take-rate growth (p = 0.20). I report that failure, and the event-study extension is listed as a next step."

**Q6 (Methods). "Your entry test failed. Does H2 still hold once the extra sellers are removed?"**
Where: Sections 3.4, 3.5, 5.6, 7.4. Strength: **weak**.
Model answer: "H2 holds on BPS's published figures, at 71 percent from 2022 to 2023 and again in 2023 to 2024. The entry test shows that part of the published rise in the count is not first-time entry, so it qualifies what 'more businesses' means. I could not clean the value side the same way, because the 2024 file has no revenue amounts. My conclusion is therefore that H2 holds as published, and that its extensive margin for 2023 is overstated by the coverage break." (The candidate should prepare a back-of-envelope version with 306 and 458 thousand removed.)

**Q7 (Thomas). "Is this an Indonesian trait or a stage in a young platform's life? Sea has the largest moves abroad."**
Where: Sections 3.4, 5.2, 7.3; Appendix A.1. Strength: **partial**.
Model answer: "The quarterly test does not reject H1 (p = 0.19), so the rejection describes 2021 to 2024, not a lasting trait. Platform theory predicts that platforms hold down one side's price to attract it, then raise it once both sides have joined, and that fits this period. Sea, the regional platform in the foreign group, has the largest median move abroad (0.25), which supports a regional repricing period. I describe the result as a period of repricing in the region, not a fixed property of Indonesia."

**Q8 (Thomas). "Who are the players, and what about political involvement?"**
Where: Sections 6.1 to 6.4. Strength: **partial**.
Model answer: "Chapter 6 maps each rule to the part of the figures it acts on. The ride-fee cap followed driver protests and acts on the fee rate. The discount rule acts on the incentive rate. The marketplace tax is collected by four marketplaces. The data rule and the census act on BPS's coverage. The government declined to cap marketplace fees even as Shopee and TikTok Shop raised them. I measure what each rule can reach and make no claim about its effects."

**Q9 (Kong). "Platforms define GTV differently. How can you compare them?"**
Where: Section 3.1 (rule 2), Sections 4.1, 4.3. Strength: **strong**.
Model answer: "I never compare the level of one platform's transaction value with another's in the tests. Each platform is compared only with itself from one year to the next, so its own definition cancels out of the yearly change in the take rate, as long as the definition and business mix stay the same. Pairs where the reporting scope changed are dropped."

**Q10 (Methods). "Your 'registered' tests sit in your own repository. Why should we trust the dates?"**
Where: Section 4.10; Appendix C. Strength: **partial**.
Model answer: "Each prediction was committed with a date before the data were opened. Appendix C lists the dates, and the repository records file checksums. I report every outcome, including six failures, and I relabel the quarterly test as a robustness check because the annual result was already known. A public timestamp would be stronger, and I can add one for the remaining predictions."

**Q11 (Methods). "If a frame change is the likely cause, why not ask BPS?"**
Where: Sections 5.7, 7.4, 6.4. Strength: **weak**.
Model answer: "The files carry no area or design variables, so I could not test the frame directly, and I did not contact BPS. The 2024 published table behaves normally again, which points to a one-year break. The entry test can be repeated on the first survey that uses the 2026 census frame. Contacting BPS is a reasonable next step."

**Q12 (Kong / Thomas). "The US$40 billion headline rests on a Momentum Works estimate and an assumed Shopee take rate. How reliable is it?"**
Where: Sections 4.2, 5.1 (Table 5.2 note). Strength: **partial** (the sensitivity is strong, but the source has not been seen).
Model answer: "The wedge depends little on the take rate. At 9, 11 or 11.5 percent for Shopee it stays between US$39.8 and 40.3 billion, and dropping any one platform still leaves more than US$20 billion. Each amount carries its label: Tokopedia is direct, Shopee's transaction value is an outside estimate, and Grab's is derived. The figure is a sum of three platforms, not a national total, and it is not used in the hypothesis tests."

**Q13 (Thomas). "Is your decomposition causal? Did pricing cause revenue to rise?"**
Where: Sections 3.3, 5.3, 7.4. Strength: **strong**.
Model answer: "No. Equations (5) and (6) are identities. They show how revenue moved (more commerce, higher fees, lower incentives), not why the company chose it. Company explanations are reported as statements and not tested, and Section 7.4 says the splits are accounting, not causes."

**Q14 (Thomas / Methods). "The market-value sample has 28 clusters, includes share issuance, and leaves out Grab, GoTo and Sea. What can it show?"**
Where: Sections 4.5, 5.4, 7.4, 7.5. Strength: **partial**.
Model answer: "It shows an association across listed platforms with whole-company figures: market value moves with transaction value. Because issuance changes market value, I do not call it a return, and I make no causal claim. The second run, with segment series, finds the predicted gap, but it mixes segment figures with whole-company values, so I do not rely on it. A returns test around announcements is the stated next step." (The candidate must also prepare a one-line reason why Grab, GoTo and Sea are missing.)

**Q15 (Kong). "How did you get 'at most 1 in 20 sellers' for the marketplace tax?"**
Where: Sections 4.8, 6.3. Strength: **strong**.
Model answer: "In 2022, marketplace sellers above BPS's bracket line of about US$20,000 a year were about 5 percent of all online sellers. The tax exempts individuals up to about US$34,000, so the true share is smaller. BPS's marketplace category also includes food and ride apps, which do not collect the tax. So 1 in 20 is an upper limit for two reasons, and on value the limit is 17 to 24 percent."

---

## 3. Were the 1 October committee concerns answered? (EDIT_HISTORY Part A)

| Concern (who) | Now answered? |
|---|---|
| Definitions and terms confusing (Thomas) | **Answered.** Table 3.1 defines each term once in plain words. Remaining gaps: company names at first use, and inconsistent appendix labels. |
| The wedge is "just subtraction"; why D and not W (Thomas) | **Mostly answered.** Sections 3.2 and 5.2 make the thin-take-rate argument. But Section 5.1 (W is 97 to 99 percent of V) partly supports his point, so concede that W measures size and D carries the test. |
| Commission cap 20% to 8% and the wedge (Thomas) | **Partly.** Section 6.2 sizes the slice and documents the incentive cut before the cap. The direct effect (fee moves from R into W) is not stated, and P1 to P5 are unscored. |
| Political involvement and economic players (Thomas) | **Partly.** The rules are mapped to the measures (Table 6.1). Players' interests and the reasons for each rule's form are not discussed. |
| Talk limited to 10 minutes (Thomas) | **Not a thesis issue.** A short final-defence deck is still needed. |
| How transaction value compares across platforms (Kong) | **Answered in method** (rule 2, within-platform changes). The promised definition map is not in the appendices, and A.1 lacks company names. |
| Proposal very hard to read; too cautious (Kong) | **Largely answered** (see Part 5). The remaining weak spots are the survey-method passages and the appendices. |
| Keep to the issues she and Thomas raised (Kong, 12 Oct) | **Answered** for Thomas's four points, with the gaps noted above. |
| Topic should not change completely (Kong, 12 Oct) | **Answered.** Title, research question, H1, H2 and measures are kept, and the entry test is presented as a check on H2. Whether she accepts that the centre has shifted toward the 2023 seller count is her call. |
| Improve the writing; read it through (Kong, 12 Oct) | **Answered for Chapters 1 to 7.** The appendices still read like working notes. |

---

## 4. Overall verdict

**Probability of passing: about 95 percent.** A Taiwanese MSc Finance committee rarely fails a thesis with this much original data, registered tests and an engaged advisor.

**Most likely outcome: pass with minor revisions** (about 55 percent). Next is pass with major revisions (about 35 percent), driven by Thomas's concerns about the finance contribution and the market-value sample. Pass without revision is about 5 percent, and fail about 5 percent, mainly if the defence comes before Chapter 6.5 can be filled and the committee treats the thesis as unfinished.

**The five changes that would most raise the outcome, ranked by payoff for effort:**

1. **Clean the appendices and front matter (low effort, high payoff).** Use full company names, one set of labels matching Table 4.1 and Section 4.10, and no file paths or draft notes in the body. Add an abstract and a list of abbreviations. Introduce GoTo, Grab, Sea, Gojek and Momentum Works at first use. Tone down the first paragraph of Section 1.1. This answers most of Kong's report in a day.
2. **Answer H2 after the entry test (low to medium effort, high payoff).** Add one paragraph to Section 5.6 or 5.7. Recompute the extensive-margin share with the 306 and 458 thousand extra sellers removed from the count. Alternatively, state why the value side cannot be cleaned and what the result means for H2. This is the sharpest question the panel can ask, and the thesis currently has no answer.
3. **Add the cap-to-wedge arithmetic and the players paragraph to Chapter 6 (low effort, high payoff with Thomas).** Two paragraphs. First, the cap moves the fee from revenue into the drivers' share (the wedge) on a slice of about 2 to 7 percent of the measure. Second, who gains and who loses from each rule in Table 6.1. Also add a dated line on which Section 6.5 outcomes will exist at the defence.
4. **Strengthen the market-value test (medium effort, high payoff for a finance degree).** Explain why Grab, GoTo and Sea are absent, and add them if possible. Report wild-cluster-bootstrap p-values. Show one version net of share issuance. Restate the finance contribution modestly in Sections 1.2 and 7.2.
5. **Test the life-cycle and regional alternative for H1 (medium effort, medium-high payoff).** Rerun the test with Sea moved to the regional group, or with a control for years since listing. Say in Chapter 1 that the rejection describes 2021 to 2024. Also carry "exploratory" into every statement of the H1 verdict, and state in Table 3.2 that the test is relative.

(Next in line: resolve the 14 [UNVERIFIED] references, starting with Momentum Works, and add the bracket and exit-rate sensitivities.)

---

## 5. Readability verdict

**Verdict: yes, it is now easy to read for a non-native English reader, in Chapters 1, 2, 3, 6 and 7 and most of Chapter 5.** By my count of the main text (excluding tables, headings and equations), sentences average 16.3 words, with a median of 16. About 8 percent run over 25 words, and most of those carry an equation. None of the banned words appear ("indicator", "Overall,", "therefore", "rather than", "However", "Moreover"). Paragraphs lead with their point, and examples carry the ideas (the 100-for-a-trip example, the 2-percent platform). The difficulty that remains is in the content, not the sentence length. It sits in the survey-method passages (Sections 4.7, 4.8, 5.7 to 5.9), which pack several conditional ideas into short sentences, and in the appendices, which read like working notes. Kong would likely say "much easier to read". She would mark the appendices and the bracket and cohort passages.

### Five passages that read best

1. Chapter 1: "The two are different amounts. A platform keeps only part of each sale, as commissions and fees. The rest is the seller's receipts, the driver's fare or another amount that passes through. This thesis calls the difference the invisible wedge. The term means what a revenue-only measure leaves out. It does not mean activity that goes unrecorded."
2. Section 2.1: "If a rider pays 100 for a trip and the driver keeps 80, such a company records 20. Discounts and vouchers that it pays for are normally deducted from its revenue."
3. Section 3.5: "The 21.5 percent threshold comes from arithmetic. The published count of online sellers rose by 27.4 percent in 2023. Suppose every extra seller was new and no seller stopped. Then for every 100 sellers a year earlier there were 127.4, and 27.4 of those were new."
4. Section 3.2: "A platform that keeps 2 percent of each sale has an ecosystem ratio of 49. If its transaction value is flat, a rise in its take rate to 3 percent raises its revenue by 50 percent. A platform that keeps 17 percent has an ecosystem ratio near 5, and a rise to 18 percent raises its revenue by about 6 percent."
5. Section 6.2: "A cap on one fee does not fix the take rate, because the platform still sets its incentives." (The Chapter 7 close is a close second: "Revenue is what a platform keeps. ... A reader who checks which condition holds can use any of them.")

### Five passages that still read worst

1. Section 5.7: "Entrants account for 25 to 30 percent of that rise, and sellers not explained by entry for 15 to 17 percent. Existing sellers reported a mean change of about −4 percent, so they added nothing to the rise. That leaves 53 to 59 percent of it with no source in the sellers' answers." *Why:* "sellers not explained by entry" is a stacked noun phrase, "no source in the sellers' answers" is abstract, and the method behind the numbers is not given.
2. Section 4.8: "The 2023 questionnaire asks for monthly revenue but the bracket limits are annual size classes, so both readings are computed and the one that passes is kept. If the lower brackets alone already exceed the total, value shares are reported as ranges." *Why:* three conditions in two sentences, and "the one that passes" points back to a rule the reader must hold in mind.
3. Section 5.9: "The annual reading of the brackets passes the validation rule, at about twice BPS's total, while the monthly reading fails at about 23 times. The lower brackets alone exceed BPS's total, so the shares are ranges." *Why:* "at about twice" and "at about 23 times" have no stated object. A reader cannot tell that "twice" is the edge of the rule.
4. Section 5.8: "Each group's extra count is its 2023 count above what its own yearly change from 2020 to 2022 would give (Section 4.7)." *Why:* the key definition of the section is folded into one relative clause. It needs two sentences and an example.
5. Section 6.5: "P1 and P5 are read together. If both hold, GoTo met the cap partly by spending more to grow. If P1 holds and P5 fails, GoTo let the lower commission show in its take rate without spending more to grow." Also Table 6.2, P4: "Grab's change in the rides take rate, less its change in the deliveries take rate, is at most +0.3 points." *Why:* the reader must hold two prediction codes and their ranges from the table to follow the logic. (Close behind: Section 4.1, "One added pair, Ozon from 2021 to 2022, ends in a kept year but starts in a dropped one.")
