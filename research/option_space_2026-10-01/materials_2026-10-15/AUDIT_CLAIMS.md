# Audit of claims and research integrity (15 Oct 2026)

Scope: `papers/thesis_2026-10/ch1_introduction.md` to `ch5_results.md`, `drafts/ch6_draft_2026-10-14.md`, `drafts/ch7_draft_2026-10-14.md`, `appendix_notes.md`, checked against AGENTS.md (Research boundaries; Thesis story and writing standard), `papers/thesis_2026-10/README.md` (Claims), `PART7_ANSWER_AND_LIMITS.md`, `PREREGISTRATION.md` (all addenda, with commit times), `publishable_track/PREREGISTRATION.md`, the 27 Sep proposal text and the committed tables. No file other than this one was edited. Nothing was committed.

Paths below are short forms: `ch1` to `ch5` = `papers/thesis_2026-10/chN_*.md`; `ch6`, `ch7` = the 14 Oct drafts; `appC`, `appB` = `papers/thesis_2026-10/appendix_notes.md`; `PREREG` = `research/option_space_2026-10-01/PREREGISTRATION.md`.

Registration timeline used (from `git log --date=iso -- PREREG`): sections A to E 2 Oct 20:53 (ec6d1eb); E2b, E5, E6 2 Oct 23:31 (26ab2cf); R1 to R3 3 Oct 00:22; E2c, E7 3 Oct 01:59; RBI 3 Oct 18:56; E8 3 Oct 22:58; W1 to W3 3 Oct 23:05, results 23:11; F1 to F3 3 Oct 23:10, results 23:11; X2, X3 3 Oct 23:16:44, results 23:17:20; BPS results 7 Oct 19:46 (files bought October 2026); Q1 registration and result in one commit, 7 Oct 19:55 (f38f91d); M1, M2 8 Oct 17:42, results 8 Oct 17:49; tax-start withdrawal 15 Oct (07871b1). Discount-leverage rule registered 2 Oct 00:07 in `l_rule_preregistration.py` (95a322b).

---

## A. High severity (fix before the thesis goes to the committee)

### A1. X3 could not fail: its outcome followed from figures seen before registration
- **Where:** `ch5:188` ("the World Bank results were registered"), `ch5:210` (Indonesia "the highest share of seven countries"), `appC:161` (F3, X3 "Hold").
- **Problem:** the X addendum (PREREG line 82) lists as already seen the published share of firms filing tax electronically in each country (Malaysia 86.2, Thailand 83.4, Viet Nam 99.6, Philippines 63.3, Singapore 99.9). The share with *neither* a website *nor* e-filing cannot exceed the share without e-filing: at most 13.8, 16.6, 0.4, 36.7 and 0.1 percent. Indonesia's 39.9 percent was already known from F3, run five minutes earlier. So every comparison in X3 was settled before registration. This is the same defect as the withdrawn tax-start prediction (outcome public before registration). The registration and result commits are 36 seconds apart.
- **Fix:** dated addendum withdrawing X3 as a registered test ("outcome implied by published e-filing shares seen before registration"). In `appC:161` split F3 from X3 and mark X3 "Withdrawn: implied by published figures"; in `ch5:188` say the World Bank results for Indonesia were registered and the seven-country ranking is descriptive. Keep the 39.9 percent figure and the ranking as descriptive.

### A2. The entry test (E5): information bearing on its outcome sat in a BPS publication the researcher held at registration (verify)
- **Where:** `ch1:35`, `ch3:154`, `ch4:93`, `ch5:21`, `ch5:140`, `ch7:31`, `appC:153`.
- **Problem:** `sources/core_public_documents/bps_ecommerce_statistics_2024.pdf` (committed 9 Sep 2026, 2dda91b) is the "local 2024 publication" that the 2 Oct E5 addendum cites. Its Appendix 12 gives the 2024 sellers by start year (before 2020: 33.66%; 2020-22: 37.55%; 2023 or later: 28.79%; `bps_cohort_2024_published.py`). Sellers who began before 2023 and still sold in 2024 were 0.7121 x 4,400,972 = 3.13 million. If the population was the same in 2023 and 2024 (which ch5:160 accepts), at least 3.13 million of the 3.82 million 2023 sellers began before 2023, so at most 17.9 percent began in 2023: below the 21.5 percent threshold. The published table therefore implied E5's failure under the thesis's own reading of 2024. In addition, the 2023 edition (Statistik E-Commerce 2023, published 30 Jan 2025, cited in `data/bps_official/bps_ecommerce_national_indicators_2020_2023.csv` since September) may print the same start-year table for 2023, which would be E5's exact outcome. The BPS page returned 403 to this audit, so this was not verified. The registration does not list either table as already seen. The thesis's statement is narrowly true ("before the survey files were opened"), but a reader takes it to mean the outcome was unknown.
- **Fix:** (1) Check the 2023 edition's appendices for a start-year table and record what was read before 2 Oct. (2) Add a dated addendum stating that the 2024 edition's start-year table, in the repository at registration, implied a share of at most 17.9 percent if the 2023-24 population was stable. If the 2023 edition printed the 2023 start-year shares, E5 must be withdrawn as a registered test, as the tax-start prediction was. (3) In the thesis, label E5 "registered before the files were opened; a published table already pointed to the outcome" (one sentence in 4.7 and a note in appC). The outcome itself stands and needs no hedging in the story; only the "registered" label changes. The same check should be run for E2, E2b and E2c: earlier BPS editions may print the 2020 and 2022 marketplace-use shares.

### A3. A registered test is missing from the thesis: the discount-leverage rule (L)
- **Where:** absent from `appC:146-168`, `ch5` 5.3, `ch6:41-43` and `ch7:29-39`.
- **Problem:** PREREG section B (2 Oct) commits that "L is reported as headroom with its failures", and `l_rule_preregistration.py` registered P1 to P3 before the out-of-sample data were opened. Results (PREREG line 104): P1 holds but rests on 2 cases; P3 fails at the headline threshold; the out-of-sample rank correlation is 0.20 (p = 0.43). PART7 lists it among "What failed (reported, not hidden)". The thesis reports none of it, while Chapter 6 discusses the same lever ("the lever that moved take rates most often", `ch6:41`). This is selective reporting of a registered failure.
- **Fix:** add a row to Appendix C ("Discount-leverage rule | larger take-rate moves when incentives are large relative to revenue | 2 Oct 2026 | Points the right way; too few out-of-sample cases; P3 fails at the headline threshold"). Add one sentence to 7.3 and one to 6.2 where incentives are discussed.

### A4. The coding fix that flipped F3 is not disclosed
- **Where:** `appC:160-161` (F1, F2 "Hold"; F3 "Hold"), `ch5:210`.
- **Problem:** PREREG line 81: under the coding stated at registration, F3 came out false (13.0 percent); the code for j36 was corrected after that run to "fully or partially", which reproduces the World Bank's published 37.5 percent, and F3 then holds. The correction is defensible, but a verdict that changed after a post-result recode is a textbook forking-path flag if it is not disclosed.
- **Fix:** in `appC` add "after one disclosed coding correction (j36: the registered coding did not match the questionnaire; under it F3 failed at 13.0 percent)". One clause in `ch4:111` or the note to 5.9.

### A5. Sampling noise is "ruled out" in the story, against the Claims rule
- **Where:** `ch5:164` ("Sampling noise does not explain the break."); also `ch5:22` lists it as a check.
- **Problem:** PART7 dated note of 10 Oct: sampling error is stated as "large in the scenarios checked", not ruled out. The calculation assumes one edition's error rates for both years and independent surveys; at twice the error the margin is 2.3 standard errors (`appB:140`), which the chapter does not give.
- **Fix:** "Sampling noise is unlikely to explain the extra count. It is about 4.6 times the usual noise in the change, and 2.3 times if the true noise were twice as large." Keep the assumptions in 7.4 (already at `ch7:53`).

### A6. Effects of the rules are claimed or implied
- **Where:** `ch6:45` ("How far the cap moves the companies' take rates is the subject of the predictions"), `ch6:95` ("If both hold, GoTo met the cap partly by spending more to grow. If P1 holds and P5 fails, GoTo let the lower commission show in its take rate"), `ch7:65` ("The outcomes will show how far the commission cap moved the companies' take rates").
- **Problem:** AGENTS and PART7 forbid any claim about a rule's effect; `ch6:95` (first sentence) and `ch7:59` say so too. A single before-after comparison, with no comparison group and rides pooled with deliveries, cannot show what the cap moved. The registered reading rules (PREREG line 23) are themselves causal, so the thesis must not adopt them as stated.
- **Fix:** `ch7:65`: "The outcomes will show how the companies' take rates moved in the first quarter under the cap; they cannot separate the cap from other changes." `ch6:45`: "How the take rates moved in the first quarter under the cap is the subject of Section 6.5." `ch6:95`: "If both hold, GoTo's take rate fell while its transaction value grew faster, which fits reinvestment. If P1 holds and P5 fails, the lower take rate came without faster growth." Add one line: the predictions are descriptive and are not a test of the cap's effect.

### A7. Existing sellers "added nothing" to the 2023 value rise
- **Where:** `ch5:166` ("Existing sellers reported a mean change of about −4 percent, so they added nothing to the rise").
- **Problem:** the −4.3 percent is a seller-weighted mean of a reported change. No revenue amounts exist for 2023, so it cannot be weighted by value. Sellers with 20 or more workers reported +1.4 percent (PREREG line 112), and they hold most of the value. PART7 grades the claim "Exploratory scenarios (brackets; no value weights)". The sentence states a value fact that the data cannot give.
- **Fix:** "Existing sellers reported a mean change of about −4 percent, counting each seller once. Their answers give no source for the rest of the rise, which is 53 to 59 percent of it." Label the paragraph exploratory.

### A8. The 2023 seller result is worded more strongly than the Claims rule allows
- **Where:** `ch5:3` ("About half of that rise did not come from sellers entering for the first time").
- **Problem:** README Claims rule: say "is not explained by first-time entry". "Did not come from" states as fact the very point that returners leave open. The rest of the thesis uses the agreed wording (`ch1:27`, `ch5:146`, `ch7:3`, `ch7:15`).
- **Fix:** "About half of that rise is not explained by sellers entering for the first time."

---

## B. Medium severity

### B1. H1: "the test planned in advance" and the forks in the main test
- **Where:** `ch5:13` (Table 5.1 label), `ch5:64-66`, `ch3:120`, `ch4:19`, `ch4:51`, `ch4:137`, `ch7:13`, `ch7:45`.
- **Problem:** (a) The "narrower test planned in advance" is the test in the 27 Sep proposal (proposal text, section 4.5). It was never registered, and the proposal already reported its results (pair-level p = 0.002; one median per platform p = 0.024). "Planned in advance" suggests that no results were known. (b) After that result, three things changed together: the measure (absolute D in points became absolute log change in the take rate), the treated group (3 marketplaces became 5 series, adding the region-wide Grab on-demand and GoTo on-demand), and the benchmark (8 platforms became 27). The 19 added platforms came from the spin-off extraction of 3 Oct (`publishable_track/PREREGISTRATION.md`), and the extended test was run at 19:41 that day (f4cba03), minutes after the spin-off results. The thesis discloses that the main test is exploratory (`ch4:137`, `ch5:64`, `ch7:45`), and Appendix B shows that each fork gives the same answer (p from 0.002 to 0.05 across the grid). That grid is the real defence, but the text does not name the three changes. (c) Table 3.2 and 4.3 call it the "main test" while 4.10 calls it exploratory. The verdict "H1 is rejected" is then stated firmly in `ch5:50` and `ch7:13`.
- **Fix:** in 4.3 add two sentences: "The proposal tested growth divergence for the three marketplaces against the eight platforms chosen first, and reported its result. The thesis then changed the measure, added the two on-demand series and widened the benchmark; Appendix B gives the result for each change." In `ch5:13` and `ch5:66` replace "planned in advance" with "set out in the proposal". The verdict sentence can stay firm, because the proposal's own test and every fork agree. That is an evidence claim, so say it once: "Every version of the test in Appendix B points the same way."

### B2. Market-value test: the registration says some market values had been seen
- **Where:** `ch3:191` ("written down before the market values were collected"), `ch4:69`, `appC:164-165`, `ch7:21`.
- **Problem:** the M addendum (PREREG line 116) says year-end US-dollar market values for 19 platforms, 2019-2025, had been seen in the 2 Oct multiples check. `multiples_dispersion.py` used them for 7 US firms that are in the main sample (Uber, Lyft, DoorDash, Airbnb, Booking, Etsy, eBay). The registration and result commits are seven minutes apart (ab24063, b517f8e). The thesis drops the disclosure.
- **Fix:** `ch4:69`: "The test was written down before the market values for the test were pulled; year-end values for some of the same firms had been seen in an earlier descriptive check." Same clause in `appC:164`.

### B3. "National figures agree on growth where they cover the same sellers"
- **Where:** `ch5:25` (Table 5.1, labelled "Registered"), `ch5:216-218`, `ch7:17`.
- **Problem:** (a) The figures behind the claim do not support "agree": Bank Indonesia fell 4.7 percent while BPS's marketplace slice grew 0.2 to 13 percent across scenarios (2.8 percent in the high one) in 2022-23. (b) The two do not cover the same sellers: 43 percent of BPS's marketplace sellers use only Gojek or Grab (`ch5:194`), and Bank Indonesia covers large e-commerce firms. (c) The registered test (RBI) concerns level, not growth. PART7 line 35 ("Firm on growth (RBI pre-registered)") mislabels it, and Table 5.1 carries that over.
- **Fix:** "Where the national figures cover similar ground, the marketplaces, their growth is small: BPS's marketplace slice grew by 0.2 to 13 percent and Bank Indonesia's figure fell by 5 percent. Most of the disagreement sits outside the marketplaces." In Table 5.1 label the growth claim "Descriptive" and the level comparison "Registered, mixed". In `ch7:17` use "where they cover similar ground".

### B4. The wedge total "does not depend on the assumed rates"
- **Where:** `ch5:44`.
- **Problem:** the sensitivity varies only Shopee's take rate. Two thirds of the summed revenue (US$2.15bn of 3.16bn) is an assumption, and Shopee's transaction value is an outside estimate that is never varied. Grab's figure is derived from a company-wide ratio. Dropping Shopee halves the wedge. Table 5.2 labels each row correctly; the sentence overstates.
- **Fix:** "The total changes little with Shopee's assumed take rate. It rests mainly on Momentum Works' estimate of Shopee's transaction value, and dropping any one platform still leaves more than US$20 billion."

### B5. "Pricing, not more commerce, moved revenue"
- **Where:** `ch5:15` (Table 5.1), `ch5:82`, `ch1:27` ("mainly because platforms kept a larger share").
- **Problem:** the take-rate term of equation (5) includes changes in business mix and scope as well as fees and incentives. PART7 grades pricing as the cause as firm only for Grab and Tokopedia, "not separable for Blibli, Bukalapak, GoTo". GoTo's own 2Q26 explanation names product mix (`ch6:39`).
- **Fix:** "A larger take rate, not more commerce, moved revenue." Then: "At Tokopedia and Grab the reports tie the rise to fees and incentives; at Blibli, Bukalapak and GoTo, pricing cannot be separated from a change in mix."

### B6. Counting heterogeneous measures as votes: "five of six measures"
- **Where:** `ch5:122`, `ch7:15`, `appD:172`.
- **Problem:** the six are a segment disclosure (Tokopedia), a segment with an estimated base that also covers Vietnam (GoTo on-demand), a whole group that includes offline agents (Bukalapak), a segment that includes travel (Blibli), a central-bank figure with no public method, and an outside estimate (Momentum Works). Tokopedia's sales also sit inside the Momentum Works estimate and probably inside Bank Indonesia's, so they are not independent. A tally treats them as one sample of six.
- **Fix:** list the measures with their labels (Appendix D already has the values), and replace the tally with "None of the measures of buying through platforms, except Blibli's, grew as fast as household spending." Add "these measures overlap and are not independent" to the note of Figure 5.3.

### B7. Counting overlapping windows and dependent predictions
- **Where:** `ch6:41` ("Lower incentives were the larger part ... in four of the seven windows"; "the lever that moved take rates most often"); `ch6:77` ("Nine predictions"); `ch6:85` (P5).
- **Problem:** (a) The seven windows include two each for Grab, GoTo and Blibli; `ch5:84` says they are not independent, but Chapter 6 repeats the count without that caveat. By platform the count is GoTo incentives, Grab mixed, Blibli mixed, Tokopedia fees. (b) R1 is derived from P1 and P3 (registered as "not independent evidence"), and P3 and P5 test the same quantity, so nine predictions concern five quantities. (c) P5 as registered leaves a gap: it "holds" at 5 percent or more and is "falsified" only below 2 percent, so a result of 2 to 5 percent has no verdict. Deciding that gap after 27 Oct would be a forking path.
- **Fix:** (a) `ch6:41`: "Lower incentives led at GoTo and in one window each at Grab and Blibli; higher fees led at Tokopedia." (b) `ch6:77`: "Nine predictions on five company figures and one national figure; R1 follows from P1 and P3, and P3 and P5 concern the same growth rate." (c) Before 27 Oct, add a dated PREREG addendum on how a P5 result between 2 and 5 percent will be scored (for example "neither confirmed nor falsified"), and print that rule in Table 6.2.

### B8. The coverage reading is stated as established in several sentences
- **Where:** `ch5:158` ("The cohort counts show the break directly"), `ch5:162` ("The break sat in chat and social selling"), `ch5:200` ("the chat-only sellers added to the count"), `ch6:73` (a new frame "can move the count", set beside the 2023 result).
- **Problem:** the cohort growth is equally consistent with returning sellers (`ch5:184`). These sentences assume the coverage reading; the section's own conclusion (`ch5:168`) is properly two-sided.
- **Fix:** `ch5:158`: "The cohort counts show where the extra count sits." `ch5:162`: "The extra count was concentrated in chat and social selling." `ch5:200`: "may partly reflect the extra chat-only sellers in the 2023 count." `ch6:73`: keep, but start the second sentence with "A frame change is one reading of the 2023 rise; ...".

### B9. The World Bank registered comparisons are reported selectively
- **Where:** `ch5:208` ("World Bank surveys of Indonesian firms show the same thin records").
- **Problem:** only the 70 percent without records among social-media users is given. The registered W1 and W2 results (social-media users keep written records and take digital payments *more* often than other unregistered firms, 29.9 against 12.3 percent) are left out, and the framing ("the same thin records") reads as if the registered evidence pointed only one way. F1, F2 and X2 are also absent from the chapter (they are in appC).
- **Fix:** add: "They still keep records more often than unregistered firms that do not use social media, 30 against 12 percent, as registered."

### B10. The prediction ranges were revised once before registration; the thesis does not say so
- **Where:** `ch6:83-85`, `appC:166`.
- **Problem:** P1 and P3 were first written on 1 Oct (f855136) and widened on 2 Oct after reading the earnings-call text (P1 from −1.5 to −0.3 became a fall of 0.3 to 2.5 points; P3 from 0-8 to 0-12 percent). The revision came before any 3Q26 number and is disclosed in PREREG, but widening a range makes it easier to hold.
- **Fix:** one clause in the note to Table 6.2: "P1 and P3 were widened once, on 2 October, after the earnings-call text was read and before any result existed (Appendix C)."

### B11. Stale project files still list the withdrawn tax-start prediction
- **Where (thesis files are consistent:** `ch6:17`, `ch6:49`, `ch6:93`, `ch7:39`, `appC:167`**):** `PART7_ANSWER_AND_LIMITS.md:71`, `FINDINGS.md:113`, `HANDOFF.md:93`, `materials_2026-10-15/SCORING_PREP.md:18`; `PART6_WHY_IT_MATTERS_GROUNDWORK.md:39` (superseded by its own dated note at line 74).
- **Problem:** a session that scores on 1 Nov from HANDOFF or SCORING_PREP would score a withdrawn prediction.
- **Fix:** add a dated note to each (frozen files only by dated note) pointing to the 15 Oct addendum. Remove the 1 Nov row from HANDOFF's dated table and the scoring block from SCORING_PREP.

### B12. The contents of an unpublished regulation are stated as fact
- **Where:** `ch6:15` (presidential regulation "released 8 October 2026; neither text public"), `ch6:35` ("The presidential regulation released in October 2026 asks another ministry to set delivery fees").
- **Problem:** PREREG section A withdrew the name "Perpres 27/2026" until a primary text is found, and 4.8 promises a status label for each rule. "Released" and "not public" contradict each other, and its contents come from secondary sources.
- **Fix:** in Table 6.1 mark the status "Reported in the news; text not read"; in `ch6:35` write "According to news reports, a presidential regulation of October 2026 asks ...".

---

## C. Low severity

| # | Where | Problem | Fix |
|---|---|---|---|
| C1 | `ch1:9` | Gives only the line-by-line view (60 percent from incentives); per unit of transaction value, higher fees led (`ch5:102`, Table 5.4: 76 vs 45). The opening picks the view that fits the story. | "In Tokopedia's accounts, smaller discounts and incentives gave about 60 percent of the extra revenue, and higher fees the rest." Leave the per-unit view to 5.3, as now. |
| C2 | `ch5:70`, `ch7:3`, `ch7:13`, `ch7:33` | The repricing period is given as "2021 to 2024"; PREREG (8 Oct) and PART7 say 2022-24, and grade the timing exploratory. | Choose one period and say why (Grab's largest move was 2021-22); use it everywhere. |
| C3 | `ch5:16`, `ch5:114`, `appC:164` | "Trimmed" for a run that was winsorised at 5/95 (registered wording). | "with extreme values capped". |
| C4 | `ch5:118` | "Market value follows the commerce" reads as direction; the result is an association (`ch7:57`). | "Market value moves with the commerce a platform carries." |
| C5 | `ch4:86-89` (Table 4.2) | The 2022 BPS count is given as 2,995,879, "implied"; BPS published 2,995,986 (Statistik E-Commerce 2023, executive summary; `data/bps_official/bps_ecommerce_national_indicators_2020_2023.csv`), which equals the weighted total exactly. | Use the published count, cite it, and drop the asterisk note. |
| C6 | `ch5:44` | "For platforms that report both amounts, the wedge was 97 to 99 percent": true only for the three marketplaces; Grab and GoTo on-demand also report both, at 81 to 90 percent. | "For the three marketplaces, ...". |
| C7 | `ch5:208` | "27 percent of unregistered firms use social media" is an unweighted count from the metadata (1,425 of 5,329); the other figures are weighted. | Use the weighted share, or say "of the firms surveyed". |
| C8 | `ch6:49`; `ch6:39`, `ch5:230` | "It had begun once in August 2026" rests on news not read in full (`CH6_SOURCES.md:120`). GoTo's 2Q26 revenue growth is 21 percent in the text and "+20%" in PREREG and management's statement. | Cite the August start or write "was halted in August"; check 20 against 21 in the source. |
| C9 | `ch5:162` vs `appB:140` | Underclaim: the link to sample growth (0.35) is called "only a weak link" in Chapter 5 but has p = 0.04 in Appendix B and supports the coverage reading. | "a modest link, at 0.35, which counts (p = 0.04)". |
| C10 | `ch5:142`, `ch3:162` | Considers only recall errors that date a start too late. Errors in the other direction, or sellers giving the start year of the business and not of online selling, would push the share down. | "The usual direction of recall error favours passing" and one clause naming the other possibility. |
| C11 | `ch6:51-59`, `ch7:25` | Survey-derived figures (5 percent, 17 to 24 percent, 8 percent, 13 percent) carry no BPS source line; the data-use statement requires BPS to be cited as the source. `ch7:49` and `appB:138` report a value share that rests on 19 sample rows. | Add "Source: BPS survey files; author's calculations" to each. Check whether BPS's terms set a minimum cell size for published figures. |
| C12 | `appA:9-41` | The 19 added benchmark platforms come from the separately registered spin-off extraction, whose registered tests S1 and S2 failed (PART7 lists them among reported failures). The thesis never says where the 19 came from. | One sentence in A.1: "The 19 added platforms were collected for a separate study registered on 3 October 2026; its own tests are reported there." |
| C13 | `appC:163-165`; X, W and F commits | Commit order is the only evidence of order: Q1 was registered and run in one commit; X results 36 seconds after its registration; M results 7 minutes after. | Keep download timestamps and checksums for the licensed files next to the commit times (the records in `LICENSED_DATA.md`) and cite them in the appC introduction. |
| C14 | `appC:157` vs PREREG line 99 | RBI is "Holds" in the registry and "mixed" in the thesis (the thesis is the more cautious reading). | A dated PREREG note saying the high scenario fails and the thesis reports the result as mixed. |

---

## D. Checked and found consistent

- **The wedge is never called missing GDP, undeclared income, unpaid tax or evasion:** `ch1:7`, `ch3:60`, `ch7:43`. "Evasion" appears only in the literature review about Denmark (`ch2:29`).
- **The ecosystem ratio is called the author's own measure:** `ch3:38`, `ch3:68`, `ch7:27`. It is never attributed to earlier literature.
- **Market value is not called a stock return:** `ch4:69`, `ch7:57`. The stock-return work is left to further research (`ch7:71`).
- **2023 sellers.** "There all along", "only counted that year" and "too large to be chance" do not appear. Returning sellers are not ruled out (`ch5:23`, `ch5:184`, `ch7:49`, `ch7:53`), and "older, long-running" is used as the README asks (`ch5:172`, `ch7:15`). The exceptions are A5, A8 and B8.
- **Tax-start withdrawal:** the thesis files treat it the same way throughout (`ch6:17`, `ch6:49`, `ch6:93`, `ch7:39`, `appC:167`). Only the project files in B11 are stale.
- **Registered failures are reported:** E5, E7, W3, Q1 and M1 appear in `ch5`, `ch7` 7.3 and `appC`, with their thresholds as registered. The exceptions are the L rule (A3) and the X3 and F3 problems (A1, A4).
- **Wording and thresholds match PREREG:** E1 to E8, RBI, W, F, X2, Q1, M1, M2, P1 to P5, R1 to R3 and the marketplace share in `appC` and Table 6.2 all match. The 15.79 percent and the P and R ranges are exact.
- **Exploratory labels:** the cohort accounting, province checks, profile, part-year check, thin-take-rate comparison, incentive-booking check and main H1 test are labelled exploratory (`ch4:101`, `ch4:137`, Table 5.1, `appB`, `ch7:45`, `ch7:53`).
- **Samples:** Indonesia, regional, segment and group scopes are labelled in Tables 4.1 and 5.2 and in `appA:4`. Annual and quarterly pairs are never pooled (`ch4:33`; Q1 is separate). Constructed Grab and Shopee figures stay out of the H1 test (`ch7:47`). The 2023 wedge sum is labelled "not a national total". The exceptions are B4 and B6.
- **Licensed data:** no business-level record is quoted. Only weighted national totals, shares and test statistics appear. BPS is named as the source in `ch4:139` and in the figure and table notes of Chapter 5 (C11 lists the gaps).

## E. Suggested order of work
1. A2 check (the 2023 BPS edition) and A1, then dated PREREG addenda for X3, E5 (whichever way the check falls), the P5 scoring gap (B7c, before 27 Oct) and the RBI verdict (C14).
2. Text fixes A3 to A8. Each is one or two sentences.
3. B1 to B12, then C.
