# Part 6: why it matters, the 2026 rules (groundwork, 8 Oct 2026)

**Status: FROZEN 8 Oct 2026** (git tag `part-6-groundwork-frozen-2026-10-08`). Groundwork only: points for the writing stage. Further changes only as dated notes at the end.
Proposal section 6 ("Why the problem matters"). Uses Parts 3-5. Term rule (Part 2, terms): "invisible" means only what revenue or an indicator leaves out; sellers who sell only through chat, social media or their own sites are called "sellers off the platforms".
Numbers: `part6_checks.py` (ledger v9), `tax_base_rulers.py`, `gel_checks.py`, `bps_microdata_tests.py` (E2, E8), `bps_descriptives.py`, `grab_quarterly.py`. Legal texts: `../../sources/policy_primary/` (MANIFEST.md). Timeline: `tables/src/policy_timeline_web.csv` (status per row). Predictions: `PREREGISTRATION.md` sections A and C and the 3 Oct addendum.

## Punchline

- **Indonesia's 2025-26 rules each act on a part of the indicators this thesis measures: the platforms' take rate (the ride-hailing commission cap, the discount rule), sellers' sales inside marketplaces (the marketplace tax) and BPS's coverage (the platform-data rule, the 2026 economic census). Each reaches only its own slice. The marketplace tax, the one aimed at online sellers, can collect from at most about 1 in 20 online sellers and about a fifth of online sales value, though it identifies every marketplace seller.**
- No causal claim about any rule. The point is what each rule can reach, measured with the thesis's data, and which of our predictions test it on scheduled dates.

## The rules and what each acts on

| Rule | Status of the text | Covers | Acts on (thesis measure) | What our evidence says about that measure |
|---|---|---|---|---|
| Ride-hailing commission cap, 8% (Perpres 27/2026; transport ministry decree, named by GoTo as No. 532/2026) | Perpres announced 1 May 2026, not published on JDIH Setneg as of 7 Oct 2026; cap in force from 1 Jul 2026 (minister, GoTo call) | Commission on two-wheel ride-hailing trips (Gojek, Grab) | One component of the on-demand take rate | Rides are about 36% of Grab's on-demand GMV (group-wide, last 4 quarters; take rate on rides about 15%, deliveries about 13%), and two-wheel trips are under 6% of Grab's rides business (pre-registration notes). At GoTo the cap covers GoRide only; on-demand also includes food. Our on-demand take rate is net of incentives on both sides, so it need not fall one-for-one with the capped commission. Marketplaces (Tokopedia, Shopee, Blibli, Bukalapak) are not covered |
| Discount rule (Permendag 19/2026, Art. 18) | Primary text read | Marketplaces and online trade | Customer incentives, the main lever behind the take-rate jumps | Incentive cuts were the larger part of the take-rate rise in 4 of 7 Indonesian windows (Part 3). By 2024 much of that lever had already been pulled (GoTo on-demand incentives 11.3% to 5.0% of transaction value). Not pre-registered as a test: its effect cannot be separated from fee changes |
| Marketplace tax (PMK 37/2025; DJP PENG-46/PJ.09/2026) | Primary texts read (PENG-46 via DDTC mirror) | Domestic sellers on designated marketplaces; 0.5% of gross turnover; individuals up to Rp500m exempt; collection from 1 Nov 2026 | Sellers' transaction value inside marketplaces | See "How far the marketplace tax reaches" below |
| Small-business final tax (PP 20/2026) | Primary text read (signed 22 Apr 2026) | 0.5% final tax up to Rp4.8bn turnover; content creators (influencer, selebgram, blogger) excluded | Sellers outside marketplaces, partly | Context only: the BPS files cannot identify influencers |
| Platform data to BPS (Peraturan BPS 4/2023) | Primary text read | E-commerce operators must send BPS revenue, transactions, numbers of sellers and buyers, with sanctions | BPS's own coverage | In 2024Q4 only 61 operators had sent data (news). BPS's 2024 e-commerce publication describes its figures as survey-based and does not mention the platform data (our OCR of the publication). The official figure still rests on the area survey whose seller count moved with coverage in 2023 (Part 4) |
| Economic census 2026 (Sensus Ekonomi) | News (door to door, 15 Jun to 31 Aug 2026; counts online sellers, affiliates and influencers) | All businesses | BPS's sampling frame | BPS's e-commerce survey frame comes from the 2016 economic census (BPS presentation, read in full). Implication, not a prediction: when a 2026-based frame is adopted, e-commerce counts across that point need the same care as 2023 |
| Social-commerce payment ban (Permendag 31/2023) and TikTok-Tokopedia (KPPU conditional approval, 17 Jun 2025) | Permendag text read; KPPU decision news only | Payment features of social-media platforms; one merger | Channel structure | Context only. About 96% of sellers still sold through chat or social media in 2023 (Part 4) |

## How far the marketplace tax reaches

- Collects from: at most about **5.4% of online sellers** (marketplace sellers with Rp300m+ a year; 2023 file) and about **17-24% of online sales value** (2022, bracket scenarios: marketplace share of online value 23-26% times the share held by Rp300m+ sellers 77-94%). Both are upper bounds: the exemption is Rp500m, and BPS's brackets split at Rp300m.
- Identifies: every domestic seller on a designated marketplace, exempt or not, must give the marketplace a tax number or NIK and an address before being paid (PMK 37 Art. 6); exempt sellers also file a statement. Marketplace sellers are about **18% of online sellers** (17.8% in 2023; 17.2% in 2024, published).
- Does not touch: sellers off marketplaces, about four in five online sellers. Only **13.5%** of them want to join a marketplace.
- Raises: on a base that differs about 5x by indicator (Rp204tn to Rp983tn, 2024), 0.5% is Rp1.0-4.9tn before the exemption, 0.04-0.21% of the 2026 tax target.
- So in one line: **the tax collects from few sellers and little money, but it creates a record of every marketplace seller; it leaves the other four in five sellers where they were.**

## Scheduled tests (pre-registered, not yet scored)

| Date | Test | Rule it bears on |
|---|---|---|
| 27 Oct 2026 (GoTo 3Q26) | P1, P3, P5, R1: GoTo on-demand net take falls 0.3-2.5 points vs 2Q26; GTV growth 0-12% (and at least 5% under the reinvestment reading); revenue-minus-GTV gap -0.5 to +12.5 points | Commission cap |
| Early Nov 2026 (BPS 3Q26 GDP) | R2: GoTo on-demand sales growth below nominal household spending growth | Context for the cap and the "buying stalled" reading |
| Mid Nov 2026 (Grab, Sea 3Q26) | P2, P4: Grab on-demand take within -0.6 to +0.4 points; Mobility minus Deliveries change at or below +0.3 (stated power limit). R3: Shopee revenue growth minus GMV growth at least +10 points | Commission cap; seller fee increases |
| 1 Nov 2026 | Registered expectation: the marketplace tax start slips again | Marketplace tax |
| Next BPS release | BPS marketplace share of e-commerce value at or below 15.79% | Who the marketplace-based rules can reach |

## Objections and answers

- "You claim the rules work or fail": no. Reach is measured; effects are not. The only effect-related checks are the pre-registered company-number predictions above.
- "The Perpres text is not public": stated. The cap's terms come from the government announcement, the minister and GoTo's call.
- "Rp300m is not Rp500m": the reach figures are upper bounds and are labelled so.
- "The tax still adds records": agreed and stated; that is the identification line above, limited to marketplace sellers.
- "Grab figures are group-wide": stated; they show the cap touches a small slice of the measure, not Indonesia-only magnitudes.
- "The census will fix BPS's coverage": possibly; that is why comparisons across the new frame need care. Not claimed either way.

## What Part 6 concludes and does not conclude

- Concludes: each rule acts on one part of what the thesis measures and reaches only that part; the seller-facing tax reaches a small minority of online sellers and about a fifth of online value at most, while identifying the marketplace minority; the official figure the state would use to size this is the survey whose 2023 count moved with coverage.
- Does not conclude: any effect on prices, drivers' pay, tax revenue or seller behaviour; that any rule is good or bad; anything about Taiwan's or other countries' rules beyond design contrast.

## Compared with the proposal

| | Proposal (27 Sep, section 6) | Part 6 now |
|---|---|---|
| Content | One paragraph: indicators disagree; investors, statistics agencies and tax authorities can reach opposite conclusions; PMK 37/2025 as an example | A map of seven rules to the measures they act on, from primary texts where published |
| Tax | "Designated operators cannot yet be mapped to BPS's marketplace category; compliance and revenue effects outside this study" | Reach measured: about 5% of sellers and 17-24% of value at most; every marketplace seller identified; base differs about 5x |
| Cap | Asked about at the oral; not in the text | Scoped to two-wheel rides; its slice of the on-demand measure shown; predictions scored from 27 Oct |
| Effects | Outside the study | Still outside the study |

## Status of open items

- Perpres 27/2026 and the transport ministry decree texts: not obtainable from this network; cite as announced.
- KPPU decision document: news only.
- Nota Keuangan RAPBN 2026: content via news; the document loads by script.
- Scoring: on the dates above.

## Dated notes

(none)
