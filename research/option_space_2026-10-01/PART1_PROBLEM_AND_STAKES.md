# Part 1: the problem and why it matters (consolidated 7 Oct 2026)

Part 1 of the thesis has two jobs: state the problem, and show why it matters. Part 1 is the approved proposal's problem, unchanged in scope, with stronger backing. Every claim below names what backs it. Claims we cannot back were removed, not propped up.
Companion files: `FINDINGS.md` (all results), `PREREGISTRATION.md` (tests and verdicts), `../../sources/policy_primary/MANIFEST.md` (legal texts).

## A. The problem

**Claim.** Indonesia's online economy is reported through several numbers that measure different things. They give different sizes and growth rates, sometimes opposite directions. So the conclusion about size and growth depends on which number you pick.

| Piece | What backs it | Where |
|---|---|---|
| Several numbers, different definitions | Each source's own definition: platform sales (GMV, GTV, TPV), platform revenue, BPS survey, Bank Indonesia figure, payment data | `tables/v_definition_map.csv`; BPS and BI method notes |
| Different sizes and growth | 11 counters compared: those seeing mainly the apps grow slowly, those seeing all sellers, parcels or tax grow fast | `consistency_grid.py` |
| Opposite directions between state offices | Bank Indonesia's figure fell while BPS's rose sharply in the same year (2023) | `yardsticks.py` |
| Opposite directions inside one firm | Tokopedia 2022-23: revenue up, sales down, both from its own reports | proposal Table 5; filings |
| A known measurement problem | E-commerce figures clash because definitions differ (UNCTAD); GDP counts a platform's fee, not the sales it carries (Ahmad and Schreyer 2016; OECD 2023) | references below |

Removed as unproven: "people treat the numbers as the same"; "investors, statisticians and the government each draw the wrong conclusion".

## B. Why it matters: who uses these numbers

| User | How they use the number | Backing | What our evidence adds |
|---|---|---|---|
| Investors | Forecast revenue as sales times the platform's cut; value firms with revenue or sales multiples; price activity numbers | Trueman, Wong and Zhang 2000, 2001; Rajgopal, Venkatachalam and Kotha 2003; Givoly et al. 2019; Liu, Nissim and Thomas 2002; Damodaran; SEC Release 33-10751 (2020); broker notes (practitioner illustration only) | Tokopedia: a revenue multiple and a sales multiple point in opposite directions; the cut swings about 3x more in Indonesia than abroad; about two thirds of revenue change came from the cut (`h1_extended.py`, `wedge_split.py`) |
| Statistics office (GDP) | BPS's e-commerce survey supports GDP compilation; platforms must send data to BPS | SILASTIK survey description; Peraturan BPS 4/2023 (primary text); OECD Digital Supply and Use Tables handbook (2023) | Part of BPS's 2023 count growth follows its survey design, not entry (E5; exploratory `bps_frame_check.py`); BI and BPS disagree |
| Tax office | 0.5% of sellers' marketplace sales, individuals up to Rp500m exempt; collection starts 1 Nov 2026 | PMK 37/2025, PENG-46/PJ.09/2026, PP 20/2026 (primary texts); OECD Model Rules (2020) and EU DAC7; Kleven et al. 2011; Pomeranz 2015; Brockmeyer and Hernandez; Naritomi 2019 | Tax base differs about 5x by source (`tax_base_rulers.py`); larger sellers hold most marketplace value but most sellers are exempt (E8) |
| Drivers (fee cap, ride-hailing only) | Commission taken from ride-hailing drivers capped at 8% from 1 Jul 2026. Applies to Gojek and Grab rides only, not to marketplaces (Tokopedia, Shopee, Blibli, Bukalapak); the government declined to cap marketplace seller fees (May 2026) | Perpres 27/2026 (announced 1 May 2026; text not published on JDIH Setneg as of 7 Oct 2026); KP 667/2022 and KP 1001/2022 (via news); Hall, Horton and Knoepfle; WageIndicator | Relevant only to our on-demand tier (Grab and GoTo on-demand), whose cut moved a lot when discounts ended. Our on-demand cut mixes rides and food delivery and is net of promos, so it is not the same number as the capped ride commission; the main marketplace sample is untouched by the cap |
| Trade rules (discounts) | Repeated unreasonable subsidies and below-cost discounts defined as price manipulation | Permendag 19/2026 Art. 18(2) and Permendag 31/2023 (primary texts) | Ending discounts was the main driver of the revenue jumps (`growth_decomposition.py`) |
| Competition authority | Judged TikTok-Tokopedia on market shares; conditional approval | KPPU decision (news only so far); Filistrucchi et al. 2014 | Shares differ by sales or by revenue because cuts differ several-fold across platforms (`take_rate_levels.csv`) |
| Small sellers (credit) | Need records to borrow | MicroSave 2025; Berg et al. 2020 | Book-keeping falling (23% to 15%, 2020-2023); Indonesia has the most formal firms without a digital trail of 7 countries (`bps_descriptives.py`, `wb_crosscountry.py`) |

## C. Why now

All in 2025-26, each acting on a number we measure: ride-hailing commission cap announced May, in force July 2026 (Gojek and Grab rides only); discount rule June 2026 (Permendag 19/2026); economic census 15 Jun to 31 Aug 2026; marketplace tax collection from 1 Nov 2026; platform data duty to BPS (since 2024). Pre-registered predictions are scored on Q3 2026 results (GoTo 27 Oct; BPS GDP early Nov; Grab and Sea mid-Nov).

## D. What Part 1 does not claim

That anyone made a bad decision; any effect of the policies (no causal claims); that the economy is bigger than measured.

## E. Gaps

| Gap | Status |
|---|---|
| Perpres 27/2026 text | Not on the official database; cite as announced |
| Transport ministry decree applying the cap | jdih.dephub.go.id unreachable from this network; number not reported |
| KPPU decision document | News only |
| Original broker reports | News summaries only; illustration, or obtain originals |
| Sensus Ekonomi 2026 page; Nota Keuangan RAPBN 2026 | Not retrieved |

## How Part 1 sits in the thesis

- Introduction, problem paragraph: Tokopedia hook (as in the proposal); several numbers with different definitions; they disagree, including the two state offices; the choice changes the conclusion.
- Introduction stakes paragraph and Section 6 ("Why the problem matters"): the users table in short form; the 2026 timing; one sentence on what is not claimed.

## Is this worth doing? (assessment, 7 Oct 2026)

**Master's thesis: clearly yes.** A real question with stakes, original microdata, pre-registered tests with failures reported, and a clear answer. The risk is the writing, not the problem: the committee's main complaint was readability.

**Publication: yes, as a measurement paper in a field or regional journal, not a top general journal.**
- Strengths: new evidence on why e-commerce numbers clash, with microdata, for a large emerging economy; the BPS finding (official seller growth the respondents' own answers cannot reproduce); a policy hook that is spreading internationally (commission caps, platform tax reporting); pre-registration and out-of-sample scoring.
- Weaknesses a referee would raise: three main Indonesian platforms; constructed Grab and Shopee figures; descriptive, not causal; the survey-design finding is exploratory at province level (no regency or design variables in the files; BPS sampling details would be needed); the spin-off tests showed it is not a worldwide law.
- Realistic homes (judgement, not a promise): Bulletin of Indonesian Economic Studies (closest fit); Review of Income and Wealth or the IARIW conference (measurement); an accounting outlet for a separate revenue-vs-GMV piece once the sample is larger; conferences first (NTA for the tax and records angle).

**Timing.** It helps: the rules are landing now and the predictions are scored in real time. It does not carry a paper: review takes one to two years, and the policy ground keeps moving (unpublished Perpres, a possible further tax delay, the GoTo-Grab merger). A paper must rest on the lasting measurement lesson: revenue tracks pricing, official counts move with survey design, sellers stay unrecorded.

**Practical.** Any use of the BPS microdata beyond the thesis needs a new abstraksi to BPS first (SPPD 19/LADU/0000/10/2026, clause 2d). Finish the thesis plainly first; it is the first draft of the paper.

## References used in Part 1 (verified online 7 Oct 2026)

- Ahmad, N. and P. Schreyer (2016). Measuring GDP in a Digitalised Economy. OECD Statistics Working Papers.
- Berg, T., V. Burg, A. Gombovic and M. Puri (2020). On the rise of FinTechs: Credit scoring using digital footprints. Review of Financial Studies 33(7).
- Brockmeyer, A. and M. Hernandez. Taxation, information, and withholding: Evidence from Costa Rica. World Bank Policy Research Working Paper 7600 (2016); CEPR DP17716 (2022).
- Damodaran, A. The Dark Side of Valuation: Valuing young, distressed and complex businesses (NYU Stern papers).
- Filistrucchi, L., D. Geradin, E. van Damme and P. Affeldt (2014). Market definition in two-sided markets: Theory and practice. Journal of Competition Law and Economics 10(2), 293-339.
- Givoly, D., Y. Li, B. Lourie and A. Nekrasov (2019). Key performance indicators as supplements to earnings. Review of Accounting Studies 24(4), 1147-1183.
- Hall, J., J. Horton and D. Knoepfle. Pricing in designed markets: The case of ride-sharing (NBER w30883).
- Kleven, H. J., M. B. Knudsen, C. T. Kreiner, S. Pedersen and E. Saez (2011). Unwilling or unable to cheat? Econometrica 79(3), 651-692.
- Liu, J., D. Nissim and J. Thomas (2002). Equity valuation using multiples. Journal of Accounting Research 40(1), 135-172.
- MicroSave Consulting (2025). The landscape and financial access of social commerce sellers in Indonesia.
- Naritomi, J. (2019). Consumers as tax auditors. American Economic Review 109(9), 3031-3072.
- OECD (2020). Model Rules for Reporting by Platform Operators with respect to Sellers in the Sharing and Gig Economy; EU Council Directive 2021/514 (DAC7).
- OECD (2023). Handbook on Compiling Digital Supply and Use Tables.
- Pomeranz, D. (2015). No taxation without information. American Economic Review 105(8), 2539-2569.
- Rajgopal, S., M. Venkatachalam and S. Kotha (2003). The value relevance of network advantages: The case of e-commerce firms. Journal of Accounting Research 41(1), 135-162.
- Trueman, B., M. H. F. Wong and X.-J. Zhang (2000). The eyeballs have it: Searching for the value in Internet stocks. Journal of Accounting Research 38 (Supplement), 137-162.
- Trueman, B., M. H. F. Wong and X.-J. Zhang (2001). Back to basics: Forecasting the revenues of Internet firms. Review of Accounting Studies 6(2-3), 305-329.
- U.S. SEC (2020). Commission Guidance on Management's Discussion and Analysis (Release 33-10751).
- Primary legal texts and official documents: see `../../sources/policy_primary/MANIFEST.md`; BPS Statistik E-Commerce publications; SILASTIK survey pages.
