# Part 5: Objective 3, comparing the indicators (groundwork, 8 Oct 2026)

**Status: FROZEN 8 Oct 2026** (git tag `part-5-groundwork-frozen-2026-10-08`). Groundwork only: points for the writing stage. Further changes only as dated notes at the end.
Comes after H1 (Part 3) and H2 (Part 4) because it uses both. Builds on `PART2_FRAMEWORK.md` Level 3.
Numbers: `consistency_grid.py`, `yardsticks.py`, `three_rulers.py`, `bps_microdata_tests.py` (RBI), `gel_checks.py`, `part5_checks.py`, `tax_base_rulers.py`, `v_definition_map.py`; ledgers v3 to v8. Taiwan figures: `tables/src/taiwan_rulers.csv` (news-sourced, status per row).

## Punchline

- **The indicators disagree because each covers different sellers and counts them differently. Where they cover overlapping slices (marketplaces), they agree on slow growth. The disagreement sits outside the marketplaces, among chat-and-social sellers that only BPS reaches, and BPS's count of them jumped in 2023 with its coverage. Sizes cannot be reconciled.**
- Objective 3 of the proposal asked whether platform, national and payment indicators "give the same account of economic scale and growth". Answer: not of scale; of growth, only where they cover the same kind of seller.

## What each indicator covers and how it counts

| Indicator | Covers | Counts by | Note |
|---|---|---|---|
| Platform reports (GMV, GTV, TPV) | Everything bought through one platform | The platform's own records | Includes items a seller survey treats differently: Shopee shipping and other charges; Tokopedia digital goods (about 18-20% of GTV, mid-2022), cars and motorcycles; Blibli travel; Bukalapak virtual products; Grab offline-store sales and ads (`v_definition_map.csv`) |
| Bank Indonesia e-commerce | Transactions of large e-commerce firms | Data sent under confidentiality agreements; method not public | BI said in 2018 it reached about 60% of online transactions from a few large firms (news). 2023: value -4.7% while its count of transactions rose from 3.49bn to 3.71bn (news) |
| Momentum Works, e-Conomy | Shopping-marketplace GMV | Outside estimates | Third-party; definitions not fully public |
| BPS e-commerce survey | All sellers that sold online, including chat and social media | Listing in sampled areas, scaled up; the frame is updated each round | Its "marketplace" includes food and ride apps: of its marketplace sellers in 2023, 47% use a shopping marketplace and 43% only Gojek or Grab |
| Parcel counts (SEA market, J&T) | Physical shipments | Company counts | Southeast Asia-wide, not Indonesia |
| PMSE VAT | Foreign digital services (Netflix-type) | Tax receipts | Not online shops |
| QRIS payments | QR-code payments | Payment records | Mostly in-person payments; context only |
| Household spending | All household consumption | BPS national accounts | Reference |

## Growth: what agrees and what does not

- 2024: indicators covering mainly the platforms grew about 5-7% (Bank Indonesia +7.3%, Momentum Works +5.2%, e-Conomy +5.1%); BPS +17.1%. Adjacent indicators point the same way but measure other things (SEA parcels +25.2%, J&T +40.8%, PMSE VAT +24.9%, QRIS +187%). `consistency_grid.py`
- 2023: Bank Indonesia -4.7% while BPS +40.6%. `yardsticks.py`
- Overlapping slices agree: BPS's own marketplace slice grew 0.2% in 2022-23 in the mid scenario (0-13% across scenarios) and 1.45% in 2023-24 (published), in line with the platform indicators. `gel_checks.py`
- Reconciliation (RBI, pre-registered, holds): BPS's marketplace-to-consumer slice is 0.16-0.68x Bank Indonesia's 2022 figure, so BPS's larger total sits outside marketplaces.
- So the disagreement is located: it sits outside marketplaces, where BPS reaches chat-and-social sellers. Part 4 shows that in 2023 much of the count growth there came from BPS counting more existing sellers, and that most of BPS's 2023 value growth cannot be traced to what respondents reported.
- Platforms vs household spending, by quarter: GoTo's on-demand transaction value grew slower than nominal household spending in each of the last four quarters (2Q26: +2.0% vs +8.3%) while its revenue grew 20.5% (`three_rulers.py`). Grab and Sea grew faster, but their figures cover the region or Asia.

## Size: why the levels cannot be reconciled

- BPS's marketplace slice (about Rp204tn, 2024) is about 4.4 times smaller than Momentum Works' marketplace GMV (about Rp896tn) (`tax_base_rulers.py`).
- Partly definitions: platform GMV includes shipping, digital goods, travel, vehicles and offline sales that a survey of sellers' marketplace receipts does not count the same way.
- Very likely partly coverage at the top: sellers with Rp50bn+ a year are 0.5% of BPS's marketplace sellers but 18-39% of the slice's value (scenarios), resting on 19 sample rows; an area survey is thinnest where platform GMV is concentrated.
- Counts are not comparable: Tokopedia alone reported about 15 million merchants (2022, company statement); BPS counts about 0.6 million marketplace sellers. Platform counts include inactive and occasional accounts.
- Composition widens the gap: BPS's slice includes food and ride merchants that shopping-marketplace GMV excludes.
- Ruled out: foreign (cross-border) sellers, under 1% of Shopee transactions and stopped in October 2023 (company statement).
- Conclusion: growth comparisons across overlapping slices are usable; level comparisons between BPS and platform GMV are not (as the proposal said, "not yet like-for-like"), and we can now say why.

## Contrast: Taiwan (relatability, not evidence)

- Taiwan measures online selling mainly through registered businesses (the Ministry of Economic Affairs retail survey, the census of industry and services, tax returns). Retail online sales grew 2.6%, 2.7% and 2.8% in 2023-25, about 13-14% of retail.
- Indonesia's BPS surveys sampled areas and reaches unregistered chat-and-social sellers: broader, but its count moves with coverage.
- Taiwan brings social and messaging sellers in through tax registration (business name and tax ID shown since 2023); Indonesia taxes through marketplaces.
- Descriptive contrast from published figures; no test, no claim about Taiwan's numbers.

## Objections and answers

- Different units: only growth rates are compared across indicators, each in its own unit; levels only where definitions were reconciled.
- Bank Indonesia's method is not public: stated; BI is described from its own statements (news) as covering large platforms.
- Momentum Works and e-Conomy are estimates: stated; they are used for direction, not levels.
- Parcels, PMSE VAT and QRIS are not Indonesian online selling: shown as adjacent indicators, not evidence.
- BPS's marketplace slice includes food and ride merchants: stated; the agreement is between overlapping slices, not the same slice.
- Growth of the marketplace slice in 2022-23 depends on bracket scenarios: the range is reported (0-13%).

## What Objective 3 does and does not conclude

- Does: the indicators do not give the same account of scale; they give the same account of growth only where they cover overlapping kinds of sellers; the disagreement sits outside marketplaces, among sellers only BPS reaches, and in 2023 it was enlarged by BPS's coverage change.
- Does not: which indicator is the true economy; anything about Bank Indonesia's internal method; anything about Taiwan's numbers; anything about GDP.

## Compared with the proposal

- Same: the roles of the indicators (proposal Table 4), payment data as context only, the observation that BPS and platform levels are "not yet like-for-like" (BPS marketplace about US$13.2bn vs Tokopedia plus the Shopee estimate US$37.9bn in 2023).
- Added: what each indicator covers and how it counts; the disagreement located outside marketplaces; overlapping slices agreeing on growth; the size gap partly explained (definitions, coverage at the top, counts, composition) and one explanation ruled out; Bank Indonesia's coverage as stated by BI; the Taiwan contrast.

## Open items

- Bank Indonesia's method and coverage for 2023-24 (only 2017-18 statements found).
- Momentum Works' and e-Conomy's definitions in detail.

## Dated notes

(none)
