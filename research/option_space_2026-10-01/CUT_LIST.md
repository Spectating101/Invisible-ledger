# Cut list: what goes where in the thesis (8 Oct 2026)

Nothing is deleted. Every result, script, table and note stays in this folder and keeps being rebuilt by `rebuild_all.sh`. This list only decides where each piece appears in the thesis: in the **main text**, in an **appendix**, or held in **reserve** (kept for the defence, the later paper or a presentation, and pulled back in if a reader or examiner asks).
Order follows the proposal. Term rule: "invisible" means only what revenue or an indicator leaves out (Part 2, terms).

## The line the main text has to carry

How much does a platform-based measure leave out, and when does that change the conclusion about growth? Revenue is about 7% of what passes through the platforms, and platform channels are about 16-26% of online sales value. Each number is a fair stand-in only while a condition holds, and the conclusion flips when it breaks: in 2022-24 for platform revenue (the take rate moved), in 2023 for the official seller count (about half of the rise not explained by first-time entry). Everything in the main text serves that line; everything else supports it from the appendix or waits in reserve.

## Main text

| Chapter | Item | Source |
|---|---|---|
| 1 Introduction | Tokopedia hook (revenue up, transaction value down); the numbers disagree, including Bank Indonesia vs BPS in 2023; who uses them (investors, GDP, tax, the ride-hailing cap) in one paragraph; why now in one paragraph; what is not claimed in one sentence | Part 1 |
| 2 Literature | Platform pricing and revenue recognition (Rochet-Tirole, IFRS 15, Givoly et al.); measuring the digital economy (Ahmad-Schreyer, OECD 2023, UNCTAD); survey discontinuities (van den Brakel et al.); third-party information and tax (Kleven et al., Pomeranz) | Parts 1, 2 |
| 3 Framework | Terms, defined once; the idea (what an indicator covers vs how it counts); the separate jobs of the invisible wedge (size) and growth divergence (reliability); H1 and H2 unchanged | Part 2 |
| 4 Data and method | Issuer-reported platform pairs; the 27-platform foreign benchmark; BPS microdata (three rounds); pre-registration as the discipline; claims ledgers | Parts 2-4, `PREREGISTRATION.md` |
| 5.1 Objective 1 | Wedge size 2023 (US$40.07bn, ecosystem ratio 12.7) with its robustness; revenue about 7% of transaction value | Part 3 |
| 5.2 H1 | Rejected: 5 vs 27 platforms (p = 0.004), main sample alone stated (p = 0.06); two thirds of revenue movement from the take rate vs a quarter abroad; cause per platform (Grab pricing, Tokopedia 60.6% from lower incentives, GoTo 2024); the 2022-24 period; Exhibit 1 | Part 3 |
| 5.2b What markets did (added 8 Oct) | Market value moves with transaction value (M2, an association); take-rate growth has a smaller point estimate, not significant (M1 falsified, stated); market value is not stock return; the multiples comparison only as a denominator illustration | Part 3 dated note, `m1_market_value.py` |
| 5.3 The 2023 verdict | Headlines boomed while Indonesia-only buying measures stalled and sellers reported a worse year; Exhibit 6 | Part 3 |
| 5.4 H2 | Holds on the published split; E5 falsified, E6; about half of the 2023 rise not explained by first-time entry (37-56%), sampling noise an unlikely explanation on a later-wave sensitivity (4.6 SE using BPS's 2024 published RSEs), among chat-and-social-only sellers, pointing to wider coverage; returning sellers named as the open alternative; 2024 normal entry; Exhibit 5 | Part 4 |
| 5.5 Additional analyses | Channels: platform channels about 16-26% of online sales value, marketplace use falling, about 96% use chat or social; records: 28.6% vs 12.3%, book-keeping falling 2020-22; one sentence on formal firms (39.9%, highest of 7) | Part 4 |
| 5.6 Objective 3 | Overlapping slices agree on slow growth; the disagreement sits outside marketplaces; sizes cannot be reconciled (one paragraph); RBI; Exhibit 2 | Part 5 |
| 6 Why it matters | Short table of the rules and what each acts on; the marketplace tax's reach (at most about 5% of sellers, 17-24% of value, every marketplace seller identified); the cap scoped to two-wheel rides; the scheduled tests, with results added after 27 Oct and mid-Nov; Exhibit 4 | Part 6 |
| 7 Conclusion and limits | Answer to the research question at both levels; claim-strength table; what failed (one list); limits once | Part 7 |

## Appendix (in the thesis, out of the main text)

| Item | Source |
|---|---|
| H1 robustness: leave-one-out, ex-Sea benchmark, growth-divergence measure, tracking shares, Fisher test, the main-sample platform shuffle | `test_battery.csv`, `h1_extended.py`, Part 3 |
| H1 with quarterly pairs (falsified) | `h1_quarterly.py` |
| H1 with GoTo's two segments grouped as one issuer (independent review) | `../independent_review_2026-10-08/review_checks.py` |
| Returning-seller scenarios and the typical-seller vs total-sales example (independent review) | `../independent_review_2026-10-08/review_checks.py` |
| Market-value regression table (main, winsorised, with segments) and the multiples by firm (added 8 Oct) | `m1_market_value.py` |
| Wedge over time by platform (added 8 Oct; one line of it in 5.1) | `wedge_over_time.py` |
| Revenue decomposition by window; the wedge split table; Tokopedia's two views; Grab pricing vs mix; Blibli's travel mix; GoTo 2024 incentives | `growth_decomposition.py`, `wedge_split.py`, `h1_groundwork.py` |
| BPS data checks (weights, 28.63/12.25 reproduced); bracket scenarios; the full E1-E8 and RBI results | `bps_microdata_tests.py`, `PREREGISTRATION.md` |
| H2 evidence detail: cohort table; channel split; province check; sellers' reports 2022 vs 2023; question wording; the 2024 published cohorts; rise accounting with exit sensitivity; the province RSE table and noise check | `bps_cohort_check.py`, `bps_h2_cheap_checks.py`, `bps_frame_check.py`, `gel_checks.py`, `bps_rise_accounting.py`, `rq_closing_checks.py` |
| BPS value side (untraced share, scenarios) | `gel_checks.py`, Part 4 |
| Indicator table (what each covers and how it counts); the 11-indicator growth grid; the size-gap explanation (definitions, thin top, counts, composition, cross-border ruled out) | Part 5, `consistency_grid.py`, `part5_checks.py` |
| Definition map of transaction value by platform | `v_definition_map.py` |
| World Bank evidence: informal sellers (six cities) and the seven-country formal comparison; Exhibit 3 | `wb_tests.py`, `wb_crosscountry.py` |
| Tax base by indicator (about 5x; 0.04-0.21% of the 2026 target); the Grab ride share | `tax_base_rulers.py`, `part6_checks.py` |
| Policy timeline and primary legal texts | `tables/src/policy_timeline_web.csv`, `../../sources/policy_primary/MANIFEST.md` |
| Pre-registration record and the full failure list with coding fixes | `PREREGISTRATION.md`, Part 7 |
| Platforms vs household spending by quarter (basis of prediction R2) | `three_rulers.py` |

## Reserve (kept, not in the thesis unless asked)

| Item | Kept for | Source |
|---|---|---|
| Spin-off tests S1-S3 and the 29-firm panel | The later paper; one main-text clause "not a worldwide law" may cite it | `publishable_track/`, `spinoff_tests.py` |
| Market-income pattern (young platforms in lower-income markets swing more) | Defence Q&A on "why Indonesia" | `h1_extended.py` part B |
| Listing timing and the listing check | Defence Q&A on "why 2022-24"; descriptive, not a tested cause | `timing_check.py`, `listing_check.py` |
| Discount-leverage rule | Defence Q&A; points the right way, too thin to cite | `l_panel.py`, `l_rule_preregistration.py` |
| Event study and stock returns (exploratory, licensed prices) | The proposal's "later extension" | `event_study*.py` |
| Valuation practice detail (multiples, broker notes) | Defence Q&A on investors; the literature stays in chapter 2 | Part 1 |
| Competition (KPPU) and credit (MicroSave, Berg et al.) users | Presentation and discussion; one clause at most in chapter 1 | Part 1 |
| Taiwan comparison (registers vs area survey; tax ID rule; momo; foodpanda) | The Taiwanese audience and relatability; robustness of the framing | `tables/src/taiwan_rulers.csv`, Part 5 |
| GDP credibility debate (LPEM, CELIOS, Irwandi) | Context only, by the scope rule; at most one sentence | `tables/src/policy_timeline_web.csv` |
| Payment data detail (QRIS) | One clause in 5.6 as context | `consistency_grid.py` |
| Census and PP 20/2026 (influencers) detail | Discussion if asked; in the timeline | Part 6 |
| Publication assessment, case-series idea, public-version framing | After the defence | Part 1, memory notes |
| The old options map | History only | `archive/ATLAS.md` |

## Rules for the writing stage

- Each number has one home chapter; the abstract and the conclusion may repeat the headline.
- If an examiner or reader asks about a reserve item, pull it in from its source; nothing needs to be re-derived.
- Moving an item between tiers is a one-line change here; record it with a date.

## Dated notes

- **9 Oct 2026, items added since the cut list was written, and where they go.** Story order now follows `NARRATIVE_ARC.md` (two layers: the arc is the narrative, these chapters are the written form).
  - Main text, 5.4 H2: the entry test named as "the entry test of H2" (registered 2 Oct as E5), closing the proposal's own stated limit; the seller profile in one paragraph (`bps_newly_counted_profile.py`, exploratory); the part-year selling check as the main answer to returning sellers (`bps_returning_check.py`, exploratory).
  - Main text, 5.2 H1: the thin-slice reading, same price changes in points as abroad on a much thinner slice (`h1_points_vs_log.py`, exploratory), as the job of the wedge; it also answers the oral question on the wedge vs growth divergence (framework chapter states D = change in m / m).
  - Main text, chapter 1 and chapter 6: the four foreign platform rules (`tables/src/platform_seller_rules_intl.csv`); the Tanah Abang citations (`GOLDEN_PITCH.md` dated note).
  - Literature chapter: McKenzie and Paffhausen (2019) for small-firm exit; Neter and Waksberg (1964) for recall; van den Brakel, Smith and Compton (2008) and van den Brakel, Zhang and Tam (2020) for survey breaks; Trueman, Wong and Zhang (2000) and Rajgopal, Venkatachalam and Kotha (2003) for markets pricing activity measures; UNCTAD (2024) as the closest existing comparison (no novelty claim on comparing platform and national figures). Working list: `REFERENCES_WORKING.md`.
  - Appendix: full profile tables with the 2020-22 control; the month-of-selling table; the points-vs-logs firm table; the exact growth identities and the movement-share definition (independent review, `../independent_review_2026-10-08/RESULTS_INSERTS.md`).
  - Defence notes (reserve): the three prepared answers (returning sellers; was the ban wrong; is the thin-slice result obvious).

