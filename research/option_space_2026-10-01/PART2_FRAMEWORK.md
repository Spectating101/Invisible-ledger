# Part 2: the framework (consolidated 7 Oct 2026)

**Status: FROZEN 7 Oct 2026** (git tag `parts-1-2-frozen-2026-10-07`). Changes only as dated notes at the end of this file.
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

## The organising idea

Every indicator of the online economy reflects two things: **what it covers** (the activity) and **how it counts** that activity. Its growth comes from either one. When how it counts stays the same, the indicator is a fair guide to the activity. When how it counts changes, the indicator moves even if the activity did not.
The proposal already applied this at platform level: growth divergence tests whether revenue stays a fair guide to transaction value. Part 2 applies the same test at national level, and uses it to explain why indicators disagree and why the 2026 rules matter. In the writing, the idea is stated in plain words ("what it covers" and "how it counts"); no new label is introduced.

## Level 1: inside a platform (H1 and Objective 2)

**Logic.** Revenue equals transaction value times the take rate, so revenue growth equals transaction value growth plus the change in the take rate. Growth divergence is the change in how revenue counts the activity. The take rate is the service fee rate minus the customer incentive rate; when incentives are large compared with what the platform keeps, cutting them moves the take rate a lot.

**Evidence.**
- The take rate changed about three times more in Indonesia than at 27 foreign platforms (one median per firm, one-sided Mann-Whitney p = 0.004; growth divergence measure p = 0.005; leave-one-out worst p = 0.016). `h1_extended.py`
- About two thirds of Indonesian revenue movement came from the take rate, against about a quarter abroad. `wedge_split.py`
- The take-rate rises came from incentive cuts and fee increases: incentive cuts were the larger part in 4 of 7 Indonesian windows, fee increases in 2 (Tokopedia 2022-23, Blibli 2022-25), and Grab on-demand 2021-24 split about equally. `growth_decomposition.py`
- Timing: the large changes came in 2021-23. Grab on-demand's take rate has been flat since early 2023 (13-14%); GoTo on-demand's and Blibli's kept rising in smaller steps. The quarterly test was falsified because it mostly covers this calmer period. `h1_quarterly.py`
- Not a universal law: the spin-off tests across 29 firms (S1, S2) were falsified. Exploratory: young platforms in lower-income markets swing more, also without Indonesia.

**Why the thesis needs both the invisible wedge and growth divergence** (the examiner's question). The invisible wedge equals transaction value times one minus the take rate. With a take rate of a few percent, one minus the take rate stays near one, so a pricing change barely moves the wedge but moves revenue a lot. The invisible wedge therefore measures size (it follows the activity; this part is arithmetic), and growth divergence measures whether revenue remains a reliable guide (the empirical finding is that Indonesian revenue moved mainly with the take rate). The ecosystem ratio swings with small take-rate changes when the take rate is small, so it describes size only.

**Comparing platforms** (the advisor's question). Take-rate levels are not comparable across business models; the test compares each platform with itself over time.

## Level 2: the nation (H2 and the additional analyses)

**Logic.** BPS does not count every online business. It selects regencies and census blocks, lists the businesses there, scales up, and updates its list of areas each round (BPS method notes). The H2 split (more businesses versus more sales per business) assumes that this coverage stayed the same. The microdata allows the same kind of test as growth divergence: did the business count grow with the activity (new sellers) or with how BPS counts?

**Evidence.**
- Entrants (E5, pre-registered, falsified): 13% of 2023 sellers began selling online in 2023. Even with no exits, entry explains at most a 15.5% rise in the business count; BPS published 27.4%. In growth terms, **at least 40% of the published rise is not explained by entry**. This is a lower bound: exits, and the tendency of respondents to date events as more recent than they were, would both make it larger.
- Incumbents (E6, pre-registered): sellers already online before 2023 reported a median change of zero in online revenue (24% up, 44% unchanged, 32% down).
- Provinces (exploratory): growth in the business count followed growth in the survey's sample size, not the share of entrants. `bps_frame_check.py`
- Why H2 still holds on paper: when the survey finds more existing sellers, their sales come with them, so the business count and e-commerce value rise together and the split reports "more businesses".
- The parallel with Level 1: about two thirds of platform revenue movement, and at least 40% of the 2023 rise in the official business count, came from how the indicator counts rather than from the activity.

**Who is outside every administrative indicator** (where "invisible" applies most directly; the proposal's additional analyses).
- Most online sellers sell through chat and social media (about 96% in 2023); marketplace use fell from 21.6% of sellers (2020) to 17.2% (2024, published). BPS's "marketplace" category is mostly food and ride merchants (Gojek 45%, Shopee 42%, Grab 42%, Tokopedia 13% of its marketplace sellers).
- The share of sellers keeping financial statements fell from 23.5% (2020) to 15.2% (2023); sellers without statements hold 30-40% of 2022 online value (range consistent with BPS's own total).
- Unregistered firms (World Bank, six cities): 27% sell through social media; their median sales are Rp60 million a year; 70% keep no written records. Formal firms: 39.9% in Indonesia have neither a website nor online tax filing, the highest of seven Southeast Asian countries.
- These sellers are outside platform records and outside tax records; only BPS's survey reaches them, and it reaches them through the sampling described above.

## Level 3: between indicators (Objective 3)

**Logic.** Each indicator covers different activity and counts it differently: Bank Indonesia uses figures reported by platforms (method not public); Momentum Works and e-Conomy are outside estimates; BPS surveys all sellers; parcel counts cover all of Southeast Asia; PMSE VAT taxes foreign digital services. Indicators therefore disagree because of coverage and because their ways of counting change at different times.

**Evidence.**
- In 2024, indicators covering mainly the platforms grew about 5-7%; BPS, the only Indonesia-wide count of all online sellers, grew 17.1%. Adjacent indicators point the same way but are not Indonesian e-commerce (parcels are Southeast Asia-wide; PMSE VAT covers foreign services). `consistency_grid.py`
- In 2023, Bank Indonesia's figure fell (-4.7%) while BPS's rose (+40.6%), in the same period in which platforms changed their take rates and BPS's coverage changed (Level 2). `yardsticks.py`
- Inside the BPS microdata, marketplace sales to final consumers are 0.16-0.68 times Bank Indonesia's 2022 figure, so BPS's larger total sits outside marketplaces (RBI, pre-registered).
- Limit: only platform reports and the BPS microdata let us separate coverage from counting; for Bank Indonesia and the outside estimates we cannot.

## Level 4: the rules (proposal Section 6)

Each 2026 rule acts on a part of how activity is counted or captured. No effect of any rule is claimed.
- The 8% commission cap (Perpres 27/2026, announced; text not published) covers the commission taken from drivers on Gojek and Grab rides only. Our on-demand take rate also includes food delivery, rider-side fees and incentives, so the two need not move together. Marketplaces are not covered.
- The discount rule (Permendag 19/2026, Article 18) covers below-cost and repeated unreasonable incentives on marketplaces: the incentive part of the take rate.
- The marketplace tax (PMK 37/2025; collection from 1 Nov 2026 under PENG-46/PJ.09/2026) is based on sellers' transaction value inside platforms: it sees activity only through platform records, so sellers outside platforms are outside its base. Larger sellers hold most marketplace value but most sellers are exempt (E8).
- The platform data rule (Peraturan BPS 4/2023) and the 2026 economic census change how BPS counts, which matters for comparing BPS figures across years.

## Boundaries

- The framework separates the activity from how it is counted only where both are visible (platform reports; BPS microdata). It does not say which indicator is the "true" economy.
- The national result is a lower bound for one transition (2022-23); sampling error cannot be separated from a coverage change because the files carry no area or design variables.
- The causes of the decisions (why platforms cut incentives in 2022; why BPS widened coverage) are supported by reports, not tested.
- No causal claim about any policy. The invisible wedge is not lost income, unpaid tax or missing GDP.

## How the files line up (one structure)

Thesis chapters follow the proposal's order; the organising idea is the reading applied in each chapter.

| Proposal order (chapters) | Part 2 level | README story layer |
|---|---|---|
| H1 and Objective 2 | Level 1, inside a platform | Inside the app |
| Objective 3 | Level 3, between indicators | Apps vs the nation |
| H2 and additional analyses | Level 2, the nation, and who is outside every indicator | Outside the apps |
| Section 6, why it matters | Level 4, the rules | The state |

**The thesis in one sentence.** Indicators of Indonesia's online economy move with both what they cover and how they count it; in 2021-23, much of the movement in platform revenue and in the official count of online sellers came from how they count, not from the activity.

## Compared with the proposal

- Same: the three rings; transaction value, revenue, take rate, invisible wedge, ecosystem ratio, growth divergence; H1 and H2; the role of each indicator.
- Clarified: one transaction value measure; take-rate levels are not compared across business models.
- Added (all backed): why the take rate moved (incentive cuts and fee increases, deducted under IFRS 15); separate jobs for the invisible wedge (size) and growth divergence (reliability); the time pattern (large changes 2021-23, smaller since); the business count treated as an estimate whose coverage can change, tested with the microdata; the records and channel evidence placed as the part outside every administrative indicator; the rules described as acting on how activity is counted.

## Open items (dated or outside our control)

Third-quarter 2026 scoring: GoTo 27 Oct (P1-P5, R1, R2); marketplace tax start 1 Nov; BPS GDP early Nov (R2); Grab and Sea mid-Nov (P4, R3); next BPS release (marketplace share prediction). Optional upgrades: BPS sampling design details (would make the province check firm evidence); Perpres 27/2026 and the transport ministry decree texts if published.

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
