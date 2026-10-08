# Part 2: the framework (version 2, 8 Oct 2026)

**Status: FROZEN 8 Oct 2026, version 4** (git tag `parts-1-7-v4-frozen-2026-10-08`). Version 3 corrected the size of the 2023 seller-count finding (about half the rise was sellers counted for the first time, 37-56%, not "mostly"; `bps_rise_accounting.py`, ledger v10), fixes stale lines and folds in the dated notes; version 2 is at tag `parts-1-4-v2-frozen-2026-10-08`. Version 4 (8 Oct, after the independent review in `../independent_review_2026-10-08/REVIEW.md`): stated as stand-in conditions; the 2023 seller gap stated as not explained by first-time entry, with returning sellers named; the market multiples treated as arithmetic; H1 test wording corrected; version 3 is at tag `parts-1-7-v3-frozen-2026-10-08`. Further changes only as dated notes at the end.
Follows from `PART1_PROBLEM_AND_STAKES.md`. Results and verdicts: `FINDINGS.md` and `PREREGISTRATION.md`. Every number here is recomputed by a claims ledger.
Part 2 is the proposal's framework (Figure 1, Section 3) with the same measures and the same two hypotheses. It adds one organising idea, tested at both levels the thesis studies. No measure or hypothesis changes.

## Terms (defined once, used throughout)

- **Transaction value**: the total value of everything bought through a platform in a period. Companies call it GMV, GTV or TPV; we treat these as one measure, and flag only a change of scope within one firm.
- **Revenue**: what the platform recognises as its own income, after customer incentives are deducted.
- **Take rate**: revenue divided by transaction value.
- **Invisible wedge**: transaction value minus revenue. Defined at platform level only; no national wedge is computed.
- **Ecosystem ratio**: invisible wedge divided by revenue (our own measure; used to describe size only).
- **Growth divergence**: revenue growth minus transaction value growth in the same year.
- **Customer incentives**: discounts, promotions and subsidies paid by the platform; deducted from revenue under IFRS 15 (consideration payable to a customer).
- **"Invisible"** keeps the proposal's meaning only: "The term refers to what a revenue-only measure excludes, not to unrecorded activity." Sellers outside platform and tax records are called that, or "unrecorded sellers", never "invisible".

## The organising idea

Every indicator of the online economy gets used as a stand-in for an activity, and it is a fair stand-in only while a condition holds. Platform revenue stands in for the commerce a platform carries while the take rate is steady; a higher take rate is a real change in the platform's income, but it makes revenue grow faster than the commerce. A survey's count of sellers stands in for entry while its coverage and sellers' participation are steady; wider coverage changes which activity enters the estimate. When the condition holds, the indicator follows the activity; when it breaks, the indicator moves for another reason.
The proposal already applied this at platform level: growth divergence tests whether revenue stays a fair guide to transaction value. Part 2 applies the same test at national level, and uses it to explain why indicators disagree and why the 2026 rules matter. In the writing, the idea is stated in plain words ("a fair stand-in while the condition holds"); no new label is introduced. The two mechanisms differ: pricing at platform level, coverage at national level.

## Level 1: inside a platform (H1 and Objective 2)

**Logic.** Revenue equals transaction value times the take rate, so revenue growth equals transaction value growth plus the change in the take rate. Growth divergence is the change in how revenue counts the activity. The take rate is the service fee rate minus the customer incentive rate; when incentives are large compared with what the platform keeps, cutting them moves the take rate a lot.

**Evidence.**
- The take rate changed about three times more in Indonesia than at 27 foreign platforms (one median per firm, one-sided Mann-Whitney p = 0.004; growth divergence measure p = 0.005; leave-one-out worst p = 0.016). `h1_extended.py`
- About two thirds of Indonesian revenue movement came from the take rate, against about a quarter abroad. `wedge_split.py`
- The take-rate rises came from incentive cuts and fee increases: incentive cuts were the larger part in 4 of 7 Indonesian windows, fee increases in 2 (Tokopedia 2022-23, Blibli 2022-25), and Grab on-demand 2021-24 split about equally. `growth_decomposition.py`
- Timing: the large changes came in 2022-24 (Grab and Blibli in 2022-23, GoTo in 2024, when its incentives fell from 11.3% to 5.0% of transaction value). Grab on-demand's take rate has been flat since early 2023 (13-14%); GoTo's and Blibli's kept rising in smaller steps. The quarterly test was falsified because it mostly covers the calmer period. `h1_quarterly.py`, `goto_on_demand.py`
- The 2022-24 swings are specific to the Indonesian and regional platforms (all 4 swung more than in other years), not seen in foreign platforms in lower-income markets (1 of 7) or high-income markets (5 of 14); all four listed in 2021-22 (exploratory, `timing_check.py`).
- Not a universal law: the spin-off tests across 29 firms (S1, S2) were falsified. Exploratory: young platforms in lower-income markets swing more, also without Indonesia.

**Why the thesis needs both the invisible wedge and growth divergence** (the examiner's question). The invisible wedge equals transaction value times one minus the take rate. With a take rate of a few percent, one minus the take rate stays near one, so a pricing change barely moves the wedge but moves revenue a lot. The invisible wedge therefore measures size (it follows the activity; this part is arithmetic), and growth divergence measures whether revenue remains a reliable guide (the empirical finding is that Indonesian revenue moved mainly with the take rate). The ecosystem ratio swings with small take-rate changes when the take rate is small, so it describes size only.

**Comparing platforms** (the advisor's question). Take-rate levels are not comparable across business models; the test compares each platform with itself over time.

## Level 2: the nation (H2 and the additional analyses)

**Logic.** BPS does not count every online business. It selects regencies and census blocks, lists the businesses there, scales up, and updates its list of areas each round (BPS method notes). The H2 split (more businesses versus more sales per business) assumes that this coverage stayed the same. The microdata allows the same kind of test as growth divergence: did the business count grow with the activity (new sellers) or with how BPS counts?

**Evidence.**
- Entrants (E5, pre-registered, falsified): 13% of 2023 sellers began selling online in 2023, below the 21.5% that the published +27.4% requires even if no seller stopped. Respondents tend to date events as more recent than they were, which would overstate entrants, so the shortfall is conservative.
- Incumbents (E6, pre-registered): sellers already online before 2023 reported a median change of zero in online revenue (24% up, 44% unchanged, 32% down).
- Cohorts (exploratory): sellers who started selling online in a given past year can only become fewer. They shrank between the 2020 and 2022 surveys (started by 2020: -9.9%), grew between the 2022 and 2023 surveys (+6.0%), and shrank again from 2023 to 2024 (published 2024 table: started before 2020, -10.2%). Direct accounting of the 819 thousand rise: 513 thousand sellers started in 2023, and the 2023 survey counts 306 thousand more pre-2023 sellers than the whole 2022 count (37% of the rise, net of exits; about 56% if sellers stopped at the 2020-22 rate of about 5% a year). **So about half of the 2023 rise is not explained by first-time entry. The channel and province patterns point to wider survey coverage of chat-and-social sellers; sellers returning after a pause would also appear here and cannot be separated (returners equal to 10-15% of the 2022 count would remove the gap; independent review).** `bps_rise_accounting.py`. 2023 is a break year; 2024 behaves normally (at least 754 thousand new sellers against a rise of 584 thousand). `bps_cohort_check.py`, `bps_cohort_2024_published.py`
- Channel (exploratory): the extra pre-2023 sellers were all off-marketplace (sellers using only chat or social media +13%; marketplace users +0.3%). `bps_h2_cheap_checks.py`
- Provinces (exploratory): growth in the business count followed growth in the survey's sample size, not the share of entrants. `bps_frame_check.py`
- Value side (exploratory scenarios): of BPS's published 2022-23 value increase (Rp318tn), sellers not explained by entry account for about 15-17% and entrants for 25-30%; the remaining 53-59% is not traceable to existing sellers' own answers (mean reported change -4.3%; net up in 2022, net down in 2023). About half of the count jump is not first-time entry; most of the value jump cannot be traced to respondents' answers, which describe the typical seller rather than total sales. `gel_checks.py`
- Why H2 still holds on paper: when the survey finds more existing sellers, their sales come with them, so the business count and e-commerce value rise together and the split reports "more businesses".
- The parallel with Level 1: about two thirds of platform revenue movement came from the take rate rather than transaction value; about half (37-56%) of the 2023 rise in the official business count came from something other than first-time entry.

**Who is outside every administrative indicator** (sellers outside platform and tax records; the proposal's additional analyses).
- Most online sellers sell through chat and social media (about 96% in 2023); marketplace use fell from 21.6% of sellers (2020) to 17.2% (2024, published). BPS's "marketplace" category is about half food and ride merchants (43% of its marketplace sellers use only Gojek or Grab; 47% use a shopping marketplace; by app: Gojek 45%, Shopee 42%, Grab 42%, Tokopedia 13%).
- The share of sellers keeping financial statements fell from 23.5% (2020) to 20.7% (2022) under stable survey coverage, and to 15.2% (2023), a step that partly reflects the chat-only sellers added to the count (same pre-2020 cohort: 23.4% to 16.8% between surveys). Sellers without statements hold 30-40% of 2022 online value (range consistent with BPS's own total).
- Only 13.5% of off-marketplace sellers want to join a marketplace; at most about 5% of all online sellers are on marketplaces with annual revenue of Rp300m or more. `gel_checks.py`
- Unregistered firms (World Bank, six cities): 27% sell through social media; their median sales are Rp60 million a year; 70% keep no written records. Formal firms: 39.9% in Indonesia have neither a website nor online tax filing, the highest of seven Southeast Asian countries.
- These sellers are outside platform records and outside tax records; only BPS's survey reaches them, and in 2023 it reached many more of them.

## Level 3: between indicators (Objective 3)

**Logic.** Each indicator covers different activity and counts it differently: Bank Indonesia uses figures reported by platforms (method not public); Momentum Works and e-Conomy are outside estimates; BPS surveys all sellers; parcel counts cover all of Southeast Asia; PMSE VAT taxes foreign digital services. Indicators therefore disagree because of coverage and because their ways of counting change at different times.

**Evidence.**
- In 2024, indicators covering mainly the platforms grew about 5-7%; BPS, the only Indonesia-wide count of all online sellers, grew 17.1%. Adjacent indicators point the same way but are not Indonesian e-commerce (parcels are Southeast Asia-wide; PMSE VAT covers foreign services). `consistency_grid.py`
- In 2023, Bank Indonesia's figure fell (-4.7%) while BPS's rose (+40.6%), in the same period in which platforms changed their take rates and BPS's coverage changed (Level 2). `yardsticks.py`
- Where the indicators measure overlapping slices (BPS's marketplace slice is 47% shopping-marketplace sellers and 43% only Gojek or Grab merchants), they agree on slow growth: BPS's own marketplace slice grew about 0-13% in 2022-23 (0.2% in the mid scenario) and 1.45% in 2023-24, in line with Bank Indonesia, Momentum Works and e-Conomy. The disagreement sits outside marketplaces. `gel_checks.py`
- Inside the BPS microdata, marketplace sales to final consumers are 0.16-0.68 times Bank Indonesia's 2022 figure, so BPS's larger total sits outside marketplaces (RBI, pre-registered).
- Limit: only platform reports and the BPS microdata let us separate coverage from counting; for Bank Indonesia and the outside estimates we cannot.

## Level 4: the rules (proposal Section 6)

Each 2026 rule acts on a part of how activity is counted or captured. No effect of any rule is claimed.
- The 8% commission cap (Perpres 27/2026, announced; text not published) covers the commission taken from drivers on Gojek and Grab rides only. Our on-demand take rate also includes food delivery, rider-side fees and incentives, so the two need not move together. Marketplaces are not covered.
- The discount rule (Permendag 19/2026, Article 18) covers below-cost and repeated unreasonable incentives on marketplaces: the incentive part of the take rate.
- The marketplace tax (PMK 37/2025; collection from 1 Nov 2026 under PENG-46/PJ.09/2026) is based on sellers' transaction value inside platforms: it sees activity only through platform records, so sellers outside platforms are outside its base. Larger sellers hold most marketplace value but most sellers are exempt (E8); at most about 5% of all online sellers are marketplace sellers with Rp300m+ a year.
- The platform data rule (Peraturan BPS 4/2023) and the 2026 economic census change how BPS counts, which matters for comparing BPS figures across years.

## Boundaries

- The framework separates the activity from how it is counted only where both are visible (platform reports; BPS microdata). It does not say which indicator is the "true" economy.
- The national results are exploratory beyond E5 and E6; sampling noise is very unlikely to explain the 2023 surplus (about 4.6 standard errors on BPS's published RSEs; 2.3 at twice the RSE), but a frame change cannot be separated from other coverage changes because the files carry no area or design variables (BPS is not being contacted) [updated 8 Oct, see dated note]. The value side of 2023 is only partly traceable.
- The causes of the decisions (why platforms cut incentives in 2022; why BPS widened coverage) are supported by reports, not tested.
- No causal claim about any policy. The invisible wedge is not lost income, unpaid tax or missing GDP.

## How the files line up (one structure)

Thesis chapters follow the proposal's structure (H1, H2, then the comparison of indicators and why it matters); the organising idea is the reading applied in each chapter.

| Chapter (in the thesis) | Part 2 level | Groundwork file |
|---|---|---|
| Objective 1, H1 and Objective 2 | Level 1, inside a platform | `PART3_H1_GROUNDWORK.md` |
| H2 and the additional analyses | Level 2, the nation, and who is outside every indicator | `PART4_H2_GROUNDWORK.md` |
| Objective 3 (uses H1 and H2) | Level 3, between indicators | `PART5_OBJ3_GROUNDWORK.md` |
| Section 6, why it matters | Level 4, the rules | `PART6_WHY_IT_MATTERS_GROUNDWORK.md` |
| Conclusion: answer to the research question, what failed, limits | All levels | `PART7_ANSWER_AND_LIMITS.md` |

H2 comes before Objective 3 because Objective 3's explanation uses the H2 result; H1 and H2 are the proposal's two links (Figure 1).

**The thesis in one sentence.** Each indicator of Indonesia's online economy is a fair guide to another only while a condition holds: revenue tracks transaction value while the take rate is steady, and a survey's seller count tracks entry while its coverage and sellers' participation are steady. In 2022-24 the platforms' take rates moved, so revenue grew far faster than the commerce it carried; in 2023 about half of the rise in BPS's count of online sellers (37-56%) is not explained by first-time entry, which points to wider survey coverage of chat-and-social sellers.

## Compared with the proposal

- Same: the three rings; transaction value, revenue, take rate, invisible wedge, ecosystem ratio, growth divergence; H1 and H2; the role of each indicator.
- Clarified: one transaction value measure; take-rate levels are not compared across business models.
- Added (all backed): why the take rate moved (incentive cuts and fee increases, deducted under IFRS 15); separate jobs for the invisible wedge (size) and growth divergence (reliability); the time pattern (large changes 2022-24, specific to Indonesian and regional platforms, smaller since); the business count treated as an estimate whose coverage can change, tested with the microdata from several angles (2023 a break year, 2024 normal); the records and channel evidence placed as the part outside every administrative indicator; the rules described as acting on how activity is counted.

## Open items (dated or outside our control)

Third-quarter 2026 scoring: GoTo 27 Oct (P1-P5, R1, R2); marketplace tax start 1 Nov; BPS GDP early Nov (R2); Grab and Sea mid-Nov (P4, R3); next BPS release (marketplace share prediction). Not pursued: BPS sampling design details (the researcher decided not to contact BPS); the 2025 survey microdata (not released). Perpres 27/2026 and the transport ministry decree texts if published.

## References used in Part 2 (verified online 7 Oct 2026 unless marked)

- BPS-Statistics Indonesia. Statistik E-Commerce (2023, 2024 editions), technical notes on sampling and listing; SILASTIK survey descriptions (aim: updating the sampling frame; supporting GDP compilation).
- International Accounting Standards Board (2014). IFRS 15 Revenue from Contracts with Customers (consideration payable to a customer); KPMG (2023), revenue accounting for consideration payable to a customer.
- Momentum Works (2023). Our thoughts on GoTo's 2022 Q4 and FY results (incentive and marketing spend cut 34% year on year in Q4 2022).
- Neter, J. and J. Waksberg (1965). Response errors in collection of expenditures data by household interviews: An experimental study. U.S. Census Bureau technical paper (forward telescoping).
- van den Brakel, J., X. Zhang and S.-M. Tam (2020). Measuring discontinuities in time series obtained with repeated sample surveys. International Statistical Review 88(1), 155-175.
- UNCTAD. Work on measuring e-commerce and the digital economy (discrepancies from differing definitions).
- Rochet, J.-C. and J. Tirole (2003). Platform competition in two-sided markets. Journal of the European Economic Association 1(4), 990-1029.
- Givoly, D., Y. Li, B. Lourie and A. Nekrasov (2019). Key performance indicators as supplements to earnings. Review of Accounting Studies 24(4), 1147-1183.
- Ahmad, N. and P. Schreyer (2016). Measuring GDP in a Digitalised Economy. OECD Statistics Working Papers.
- MicroSave Consulting (2025). The landscape and financial access of social commerce sellers in Indonesia.
- World Bank Enterprise Surveys: Indonesia 2023 (formal), Indonesia Informal Sector Enterprise Survey 2023; latest formal surveys for Malaysia, Thailand, Viet Nam, Philippines, Cambodia, Singapore.
- From the proposal's reference list (to be re-checked in the reference review): Hagiu and Wright (2015); Evans and Schmalensee (2016); Hummels and Klenow (2005).
- Primary legal texts: `../../sources/policy_primary/MANIFEST.md`.

## Dated notes

- **8 Oct 2026, after version 3 (`rq_closing_checks.py`, ledger v11).** Sampling noise is very unlikely to explain the 2023 surplus: BPS's published RSEs (2024 edition, by province) imply a national RSE of about 1.4%, so the 306 thousand surplus is about 4.6 standard errors of the change (2.3 at twice the RSE). A frame change still cannot be separated from other coverage changes (no area or design variables; BPS not contacted). Also: the research question's "how much" is answered at two levels (Part 7): inside the platforms revenue is about 7% of transaction value; across the online economy, BPS's marketplace channel (shopping marketplaces plus food and ride apps) carries about 16-26% of online sales value (2022 microdata 22.6-25.6%; 18.2% in 2023 and 15.8% in 2024, published), so platform-based measures leave out about three quarters of online sales value in BPS's own survey.
