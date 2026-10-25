# Appendices

These appendices hold the detail that the main text points to. Every number comes from a table in the project's repository, named in the notes in small type. Nothing here changes a result in Chapter 5.

## Appendix A. Definition of variables

### A.1 Variables

Every variable and symbol used in the empirical analyses is listed with its definition and data source. The subscripts i and t mark the platform and the year. Amounts in the text are in US dollars, at the World Bank's average rate for the year (World Bank 2026). Growth is the simple percentage change, g(X), defined in Panel A.

| Variable | Definition | Source |
|---|---|---|
| *Panel A: Platform measures* | | |
| V~it~ | Transaction value: everything bought through platform i in year t, in the company's own currency. Companies also call it gross merchandise value (GMV), gross transaction value (GTV) or total payment volume (TPV). | Company annual reports, annual filings (Form 20-F) and investor releases; Appendix B lists each series |
| R~it~ | Revenue: what the platform recognizes as its own income in its accounts, for the same business and period as V~it~. | Same as V~it~ |
| m~it~ | Take rate: R~it~ divided by V~it~, the share of each sale that the platform keeps. | Author's calculation |
| f~it~ | Fee rate: the platform's revenue before customer incentives, divided by V~it~. | Company reports; author's calculation |
| s~it~ | Incentive rate: customer incentives divided by V~it~. Customer incentives are the discounts, vouchers and other promotions that a platform pays for, which accounting rules normally deduct from revenue. | Company reports; author's calculation. Blibli's incentives are a proxy (Appendix B) |
| W~it~ | Invisible wedge: V~it~ minus R~it~, the part of transaction value that lies outside revenue, in currency. | Author's calculation |
| E~it~ | Ecosystem ratio: W~it~ divided by R~it~, equal to one divided by m~it~, minus one. The author's own measure. | Author's calculation |
| g(X~t~) | Growth of X from one year to the next as a share of the first year: (X~t~ − X~t−1~) divided by X~t−1~. A value of 0.09 means 9 percent. | Author's calculation |
| D~it~ | Growth divergence: g(R~it~) minus g(V~it~). A value of 0.62 means 62 percentage points. | Author's calculation |
| Δln X~t~ | Change in the natural logarithm of X from one year to the next. Used only where a registered test defined it so (equation (9)); everywhere else the change is g(X). | Author's calculation |
| *Panel B: National and survey measures* | | |
| N~t~ | Count of online sellers: BPS's estimate of the number of businesses selling online in year t. | BPS-Statistics Indonesia (2025a, 2025b); BPS e-commerce survey files for 2020, 2022 and 2023 (licensed) |
| Y~t~ | Total online sales value: BPS's published value of online sales in year t. | BPS-Statistics Indonesia (2025a, 2025b) |
| Y~t~ / N~t~ | Sales per business: Y~t~ divided by N~t~. | Author's calculation |
| First-time entry | A seller that reports beginning to sell online in the year being measured. The entry test uses the share of such sellers among the sellers of 2023. | BPS e-commerce survey file for 2023 (licensed) |
| *Panel C: Market variables* | | |
| MV~it~ | Market value: the year-end market value of listed platform i. | London Stock Exchange Group (LSEG) data (licensed) |
| β~V~, β~m~ | Coefficients in equation (8): how the change in market value moves with the change in transaction value and with the change in the take rate. | Author's estimate |
| *Panel D: Labels* | | |
| H1, H2 | The two hypotheses of Section 3.4. | Author's definition |
| *Panel E: Variables of the regressions (Chapter 5)* | | |
| Wedge in US dollars, and its natural logarithm | The invisible wedge W~it~ converted to US dollars at the period-average official exchange rate of the reporting currency, in US$ million. The regressions use its natural logarithm. | Company reports; World Bank (2026); author's calculation |
| Ecosystem ratio, capped | E~it~, set to its 5th percentile below that value and to its 95th percentile above that value, across all platform-years. | Author's calculation |
| g(R~it~), g(V~it~), capped | Growth of revenue and of transaction value as defined in Panel A, for consecutive years of one platform only, set to the 5th and 95th percentiles across all platforms. | Company reports; author's calculation |
| IndonesiaRegion | A dummy variable that equals one for Tokopedia, Blibli, Bukalapak and the on-demand businesses of Grab and GoTo, and zero for the 27 foreign platforms. | Author's classification (Appendix B) |
| ln(1+YearsListed) | Natural logarithm of one plus the number of years since the platform listed on a stock exchange; zero before listing. | Listing years from public record; author's calculation |
| ln(Assets) | Natural logarithm of the company's total assets in US dollars, converted at the period-average official exchange rate of the reporting currency. | SEC filings (U.S. Securities and Exchange Commission 2026) for 26 platforms; published financial statements for Tokopedia and GoTo, Blibli, Bukalapak, Rakuten and Zalando |
| OnDemand, Travel, Freelance, Resale | Dummy variables that equal one if the platform is of that type and zero otherwise. The base category is marketplace. | Author's classification (Appendix B) |
| EmergingMarket | A dummy variable that equals one if the platform's main market is Argentina, Brazil, China, India, Indonesia, Kazakhstan, Nigeria, Russia or Turkey, and zero otherwise. | Author's classification (Appendix B) |
| GDPGrowth | Growth of real gross domestic product of the platform's main market in year t, in percent. | World Bank (2026) |
| Inflation | Growth of consumer prices of the platform's main market in year t, in percent. | World Bank (2026) |
| HouseholdGrowth | Growth of real household final consumption expenditure of the platform's main market in year t, in percent. | World Bank (2026) |
| PolicyRate | The central bank's policy rate in the platform's main market, mean of the monthly values in year t, in percent. The euro-area rate is used for Germany. | Bank for International Settlements (2026) |

### A.2 Sources compared in Objective 3

| Source | What it covers | How it counts |
|---|---|---|
| Platform reports | Everything bought through one platform | The platform's own records |
| BPS online-seller survey | Every business that sold online, including chat and social media | Listing in sampled areas, scaled up by survey weights |
| Bank Indonesia e-commerce statistics | Transactions of large e-commerce firms (Bank Indonesia 2025) | Data sent to the central bank; the method is not public |
| Industry estimates | Shopping marketplaces in Indonesia or Southeast Asia, from the research firm Momentum Works (2024), as quoted by Setyowati (2024), and the e-Conomy report (Google, Temasek and Bain 2024) | Outside estimates |
| Household spending | All household purchases | BPS national accounts |
| Payment figures | Payments made through systems such as QRIS, the national QR-code system | Payment records, in person and online |
| Adjacent figures | Parcels shipped in Southeast Asia, the value-added tax collected on foreign digital services (Directorate General of Taxes 2025), and the number of merchants a company reports | Used as context only, since none measures Indonesian e-commerce |

## Appendix B. Platforms, windows and the wedge by year

### B.1 The foreign group (27 platforms)

Pairs are consecutive years that pass the rules of Chapter 4, section 4.1: for the platforms added, the later year is not one in which own goods exceed half of revenue; for the eight chosen first, the reporting scope did not change. Ozon's one pair starts in a year that fails the own-goods rule (Appendix C). The median is the platform's median size of yearly change in log take rate. Source: `tables/spinoff_panel.csv`, `tables/transitions_master.csv`.

| Platform | Chosen first or added | Pairs | Median size of yearly change in log take rate |
|---|---|---|---|
| ACV Auctions | Added | 5 | 0.15 |
| Waitr | Added | 6 | 0.10 |
| Alibaba | Added | 7 | 0.21 |
| Despegar | Added | 9 | 0.07 |
| 1stDibs | Added | 6 | 0.03 |
| Expedia | Added | 11 | 0.03 |
| Fiverr | Added | 7 | 0.05 |
| Grubhub | Added | 6 | 0.09 |
| Hepsiburada | Added | 5 | 0.03 |
| Kaspi.kz | Added | 4 | 0.08 |
| Mogu | Added | 9 | 0.21 |
| Ozon | Added | 1 | 0.18 |
| PDD Holdings | Added | 4 | 0.13 |
| RB Global | Added | 11 | 0.06 |
| The RealReal | Added | 8 | 0.04 |
| Vivid Seats | Added | 6 | 0.07 |
| Upwork | Added | 8 | 0.04 |
| Vacasa | Added | 5 | 0.03 |
| Yatra | Added | 11 | 0.03 |
| Etsy | Chosen first | 3 | 0.07 |
| Jumia | Chosen first | 3 | 0.16 |
| Mercado Libre | Chosen first | 2 | 0.06 |
| Rakuten | Chosen first | 1 | 0.02 |
| Sea / Shopee | Chosen first | 7 | 0.25 |
| Shopify | Chosen first | 5 | 0.05 |
| Zalando | Chosen first | 4 | 0.02 |
| eBay | Chosen first | 4 | 0.03 |

Left out after examination: Dingdong, JD.com, Jumei, Liquidity Services, Newegg and Vipshop, because their own goods are most of revenue in every year; and four platforms that disclose no transaction value (Nebius Group, formerly Yandex; Trip.com; Tuniu; and Uxin).

### B.2 The Indonesian and regional group

| Platform series | What it covers | Years | Yearly pairs | How it is labelled |
|---|---|---|---|---|
| Tokopedia | The e-commerce segment of GoTo, an Indonesian marketplace | 2022–2023 | 1 | Direct segment disclosure |
| Blibli | Blibli's third-party retail segment, which includes online travel | 2021–2025 | 4 | Direct segment disclosure |
| Bukalapak | The whole Bukalapak group, mainly in Indonesia, including Mitra, its online-to-offline business | 2020–2023 | 3 | Direct company disclosure |
| Grab on-demand | Grab's rides and deliveries across Southeast Asia, not Indonesia alone | 2020–2024 | 4 | Direct segment disclosure |
| GoTo on-demand | GoTo's rides and deliveries segment, in Indonesia and Vietnam to 2024 | 2022–2025 | 3 | Direct segment disclosure; the 2022 transaction value is an estimate |

| Platform | Pairs | Median size of yearly change in log take rate | Share of pairs with a change of 0.10 or less |
|---|---|---|---|
| Blibli third-party retail | 4 | 0.25 | 0.00 |
| Bukalapak Group | 3 | 0.14 | 0.33 |
| GoTo on-demand | 3 | 0.09 | 0.67 |
| Grab on-demand | 4 | 0.20 | 0.50 |
| Tokopedia | 1 | 0.52 | 0.00 |

### B.3 The seven windows traced

Shares are of the log growth of revenue, because the split into more commerce, higher fees and lower incentives is exact only in logs. Source: `tables/growth_decomposition.csv`, built from `tables/l_panel.csv` by `growth_decomposition.py`. Tokopedia, GoTo: audited statements. Grab: annual filings, summed over mobility and deliveries. Blibli: incentives are a proxy (gross profit before discounts less net revenue) and stay out of the main sample. GoTo's 2022 transaction value is an estimate (2022 first and second quarters backed out of 2023 year-on-year comparisons).

| Platform and window | Growth of revenue (%) | Growth of transaction value (%) | Take rate, start (%) | Take rate, end (%) | More commerce | Higher fees | Lower incentives |
|---|---|---|---|---|---|---|---|
| Grab on-demand, 2021–24 | 320.5 | 62.3 | 5.34 | 13.83 | 33.7 | 33.8 | 32.5 |
| Grab on-demand, 2022–24 | 85.8 | 30.1 | 9.69 | 13.83 | 42.5 | 10.6 | 46.9 |
| GoTo on-demand, 2023–25 | 114.2 | 22.4 | 10.62 | 18.58 | 26.6 | 6.1 | 67.3 |
| GoTo on-demand, 2022–25 | 110.7 | 9.6 | 9.66 | 18.58 | 12.3 | 36.1 | 51.7 |
| Tokopedia, 2022–23 | 53.2 | -8.9 | 1.48 | 2.48 | -21.9 | 76.5 | 45.4 |
| Blibli third-party retail, 2022–25 | 679.4 | 43.6 | 0.54 | 2.92 | 17.6 | 62.6 | 19.8 |
| Blibli third-party retail, 2022–23 | 465.3 | 34.7 | 0.54 | 2.25 | 17.2 | 20.1 | 62.7 |

Tokopedia, 2022–23, line by line (Rp million, `tables/tokopedia_segment.csv`): gross revenue 8,143,239 to 8,988,909; incentives 4,112,320 to 2,813,719; net revenue 4,030,919 to 6,175,190. Net revenue rose by 2,144,271, of which lower incentives account for 60.6 percent and higher gross revenue for 39.4 percent (about 60 and 40 percent in the text).

### B.4 Wedge and ecosystem ratio by platform-year, Indonesian series

Original currency and units, as in the filings: Rp million for Tokopedia and Bukalapak, Rp billion for Blibli, and US$ billion for Grab and Shopee, whose Indonesian amounts are derived or estimated. Shopee's revenue assumes a take rate of 8.4 percent in 2022, 10 percent in 2023 and 10.8 percent in 2024. Table 5.2 converts Tokopedia's 2023 rupiah amounts to US dollars. Take rate and ecosystem ratio carry no currency. Each label names the source of the transaction value and of the revenue in that row. Source: `tables/take_rate_levels.csv`.

| Series | Year | Transaction value | Revenue | Wedge | Take rate (%) | Ecosystem ratio | Label |
|---|---|---|---|---|---|---|---|
| Grab | 2021 | 1.88 | 0.08 | 1.80 | 4.20 | 22.8 | Revenue: country disclosure; value: derived |
| Grab | 2022 | 3.83 | 0.28 | 3.55 | 7.19 | 12.9 | Revenue: country disclosure; value: derived |
| Grab | 2023 | 5.38 | 0.60 | 4.78 | 11.24 | 7.9 | Revenue: country disclosure; value: derived |
| Shopee | 2022 | 18.68 | 1.57 | 17.11 | 8.40 | 10.9 | Value: outside estimate; revenue: scenario |
| Shopee | 2023 | 21.52 | 2.15 | 19.37 | 10.00 | 9.0 | Value: outside estimate; revenue: scenario |
| Shopee | 2024 | 25.99 | 2.81 | 23.18 | 10.80 | 8.3 | Value: outside estimate; revenue: scenario |
| Tokopedia | 2022 | 273,146,166 | 4,030,919 | 269,115,247 | 1.48 | 66.8 | Direct segment disclosure |
| Tokopedia | 2023 | 248,836,156 | 6,175,190 | 242,660,966 | 2.48 | 39.3 | Direct segment disclosure |
| Blibli third-party retail | 2021 | 15,746 | 122 | 15,624 | 0.77 | 128.1 | Segment disclosure, includes travel |
| Blibli third-party retail | 2022 | 37,050 | 199 | 36,851 | 0.54 | 185.2 | Segment disclosure, includes travel |
| Blibli third-party retail | 2023 | 49,912 | 1,125 | 48,787 | 2.25 | 43.4 | Segment disclosure, includes travel |
| Blibli third-party retail | 2024 | 54,210 | 1,384 | 52,826 | 2.55 | 38.2 | Segment disclosure, includes travel |
| Blibli third-party retail | 2025 | 53,187 | 1,551 | 51,636 | 2.92 | 33.3 | Segment disclosure, includes travel |
| Bukalapak Group | 2020 | 85,081,843 | 1,351,664 | 83,730,179 | 1.59 | 61.9 | Company-wide disclosure |
| Bukalapak Group | 2021 | 122,618,794 | 1,869,122 | 120,749,672 | 1.52 | 64.6 | Company-wide disclosure |
| Bukalapak Group | 2022 | 153,738,958 | 3,618,366 | 150,120,592 | 2.35 | 41.5 | Company-wide disclosure |
| Bukalapak Group | 2023 | 164,380,065 | 4,438,269 | 159,941,796 | 2.70 | 36.0 | Company-wide disclosure |

### B.5 Classification of the platforms in the regressions

The type, the main market and the listing year are the author's classification from public record. The main market is the country whose macroeconomic conditions are attached to the platform: the United States for most US-listed platforms, Indonesia for Sea (Shopee), Nigeria for Jumia, Brazil for Mercado Libre and Argentina for Despegar. Source: `tables/platform_attributes.csv`.

| Platform | Group | Type | Main market | Reporting currency | Listed |
|---|---|---|---|---|---:|
| Tokopedia | Indonesian and regional | Marketplace | ID | IDR | 2022 |
| Blibli | Indonesian and regional | Marketplace | ID | IDR | 2022 |
| Bukalapak | Indonesian and regional | Marketplace | ID | IDR | 2021 |
| Grab (on-demand) | Indonesian and regional | On-demand | ID | USD | 2021 |
| GoTo (on-demand) | Indonesian and regional | On-demand | ID | IDR | 2022 |
| Etsy | Foreign | Marketplace | US | USD | 2015 |
| eBay | Foreign | Marketplace | US | USD | 1998 |
| Jumia | Foreign | Marketplace | NG | USD | 2019 |
| Mercado Libre | Foreign | Marketplace | BR | USD | 2007 |
| Rakuten | Foreign | Marketplace | JP | JPY | 2000 |
| Sea (Shopee) | Foreign | Marketplace | ID | USD | 2017 |
| Shopify | Foreign | Marketplace | US | USD | 2015 |
| Zalando | Foreign | Marketplace | DE | EUR | 2014 |
| ACV Auctions | Foreign | Resale and auctions | US | USD | 2021 |
| Waitr | Foreign | On-demand | US | USD | 2018 |
| Alibaba | Foreign | Marketplace | CN | CNY | 2014 |
| Despegar | Foreign | Travel and ticketing | AR | USD | 2017 |
| 1stDibs | Foreign | Resale and auctions | US | USD | 2021 |
| Expedia | Foreign | Travel and ticketing | US | USD | 2005 |
| Fiverr | Foreign | Freelance | US | USD | 2019 |
| Grubhub | Foreign | On-demand | US | USD | 2014 |
| Hepsiburada | Foreign | Marketplace | TR | TRY | 2021 |
| Kaspi.kz | Foreign | Marketplace | KZ | KZT | 2020 |
| Mogu | Foreign | Marketplace | CN | CNY | 2018 |
| Ozon | Foreign | Marketplace | RU | RUB | 2020 |
| Pinduoduo | Foreign | Marketplace | CN | CNY | 2018 |
| RB Global | Foreign | Resale and auctions | US | USD | 1998 |
| The RealReal | Foreign | Resale and auctions | US | USD | 2019 |
| Vivid Seats | Foreign | Travel and ticketing | US | USD | 2021 |
| Upwork | Foreign | Freelance | US | USD | 2018 |
| Vacasa | Foreign | Travel and ticketing | US | USD | 2021 |
| Yatra | Foreign | Travel and ticketing | IN | INR | 2016 |

## Appendix C. The checks on the tests of H1 and on the regressions

### C.1 The checks

The main test is described in Section 5.2. This appendix keeps its first measure, the absolute change in the log take rate, and lists each check with both p-values where both exist. Sources: `h1_extended.py` (`tables/h1_extended_results.json`), `tables/test_battery.csv`, `tables/h1_quarterly_results.json`, `tables/h1_points_vs_log.json`, `tables/h1_thesis_drops.json`. The two rows on how platforms book shopper discounts come from `research/option_space_2026-10-01/materials_2026-10-15/incentive_accounting_check.py` (classification and filing quotes in `INCENTIVE_ACCOUNTING.md`); their shuffle uses a different seed.

| Check | Indonesian and regional (median) | Foreign (median) | Mann–Whitney p | Shuffle p |
|---|---|---|---|---|
| Main test, 5 against 27 | 0.201 | 0.062 | 0.0038 | 0.0221 |
| 5 against the 8 chosen first | 0.201 | 0.055 | 0.0225 | 0.0497 |
| 5 against the 19 added | 0.201 | 0.070 | 0.0046 | 0.0175 |
| Without the 8 foreign platforms that book shopper discounts as marketing costs (exploratory, 15 Oct 2026) | 0.201 | 0.062 | 0.0035 | 0.0066 |
| Only the 11 foreign platforms that deduct shopper discounts from revenue (exploratory, 15 Oct 2026) | 0.201 | 0.075 | 0.0043 | 0.0052 |
| Growth divergence in points, 5 against 26 | 27.0 | 6.5 | 0.0055 | |
| Without Ozon, 26 foreign platforms | 0.201 | 0.060 | 0.0030 | 0.0215 |
| Without Zalando, 26 foreign platforms | 0.201 | 0.064 | 0.0045 | 0.0238 |
| Without Ozon and Zalando, 25 foreign platforms | 0.201 | 0.062 | 0.0036 | 0.0230 |
| Without Blibli third-party retail | 0.169 | | 0.0137 | 0.0364 |
| Without Bukalapak Group | 0.225 | | 0.0049 | 0.0070 |
| Without GoTo on-demand | 0.225 | | 0.0030 | 0.0071 |
| Without Grab on-demand | 0.194 | | 0.0094 | 0.0166 |
| Without Tokopedia | 0.169 | | 0.0164 | 0.0409 |
| Three marketplaces against the 8 chosen first, comparing pairs of years, absolute growth divergence in points | 38.917 | 7.105 | 0.0022 | 0.0606 |
| Three marketplaces against the 8 chosen first, one median per platform, absolute growth divergence in points (claims ledger C47, `build_numbers.py`) | | | 0.0242 | |
| Three marketplaces against the 8 chosen first, comparing pairs of years, absolute growth divergence in points (without Sea) | 38.917 | 4.192 | <0.0001 | 0.0083 |
| Three marketplaces against the 8 chosen first, comparing pairs of years, absolute change in log take rate | 0.252 | 0.055 | 0.0037 | 0.0303 |
| Three marketplaces against the 8 chosen first, comparing pairs of years, absolute change in log take rate (without Sea) | 0.252 | 0.033 | 0.0001 | 0.0167 |
| Three marketplaces, dropping all three 2022–23 comparisons (5 pairs), absolute growth divergence in points | 14.411 | 7.105 | 0.0248 | 0.2222 |
| Three marketplaces, dropping the largest comparison (7 pairs), absolute growth divergence in points | 15.738 | 7.105 | 0.0061 | 0.0606 |
| Three marketplaces against all 40 foreign pairs, absolute growth divergence in points | 38.917 | 7.373 | 0.0014 | 0.0121 |
| Five Indonesian and regional series including constructed Grab and Shopee (12 pairs) against the 8 chosen first, absolute growth divergence in points | 42.017 | 7.105 | 0.0006 | 0.0225 |
| Tokopedia and GoTo on-demand as one company, 4 against 27 | | | 0.003 | 0.007 |
| Exact tests over all 201,376 ways to pick the five platforms, main test (exploratory, 22 Oct 2026) | 0.201 | 0.062 | 0.0038 | 0.0214 |
| Sea moved to the regional group, 6 against 26 (exploratory, 22 Oct 2026; exact tests) | 0.225 | 0.060 | 0.0004 | 0.0006 |
| Dropping any two of the five platforms, 10 cases (exploratory, 22 Oct 2026; exact test) | 0.137 to 0.250 | 0.062 | 0.003 to 0.058 | |
| Only years up to 5 after listing, 4 against 18 platforms (exploratory, 22 Oct 2026; exact test) | 0.169 | 0.069 | 0.059 | |
| Quarterly pairs, 3 against 8 (same quarter a year earlier) | 0.071 | 0.049 | 0.19 | 0.33 |

The four rows marked 22 Oct 2026 were added after all other results were known, so they are exploratory. They use exact tests, which list every possible split of the 32 platforms, and they agree with the approximations in Section 5.2. The typical gap between an Indonesian or regional platform and a foreign one is 0.117 in the size of the yearly change in log take rate. That is the median of all 135 pairwise differences, with an exact 95 percent interval of 0.039 to 0.223. The ratio of the group medians is 3.3, and a bootstrap interval of 1.4 to 8.5 shows how loosely five platforms fix its size. Moving Sea to the regional group makes the gap clearer. Dropping two platforms can weaken it. The one case above 0.05 drops Blibli and Tokopedia, the two largest movers, and leaves p = 0.058. Keeping only the years up to five after listing leaves the same direction, but p = 0.059 (`tables/h1_exact_inference.json`, from `h1_exact_inference.py`).

Growth in revenue and growth in transaction value had a correlation of 0.10 in the Indonesian main sample and 0.98 in the foreign sample excluding Sea (`tables/claims_ledger.csv`, C48 and C49).

The quarterly sample is Grab on-demand, GoTo on-demand and Blibli against Sea, Airbnb, Booking, DoorDash, eBay, Etsy, Lyft and Uber. Airbnb and Booking use trailing four-quarter sums because they book revenue at check-in. DoorDash pairs ending in 2025Q4 or later are dropped because of an acquisition.

In the pairs of the Indonesian and regional group, the take rate stayed within about 10 percent (0.10 in log terms) in one third of pairs, against 67 to 69 percent in the foreign groups. The version of the test with growth divergence in points has 26 foreign platforms because Ozon has no pair in which both years pass the own-goods rule. The main test keeps Ozon's pair, whose later year passes, and the first rows above show that dropping it, or Zalando, leaves the result in place.

The comparison in points of the take rate (exploratory, `h1_points_vs_log.py`): median yearly change 1.01 points in the Indonesian and regional group and 0.98 points in the foreign group (26 platforms), Mann–Whitney p = 0.65; median share kept 1.59 percent against 16.93 percent.


### C.2 Where the 2023 break sits (exploratory)

At the top of the size distribution, sellers with revenue above Rp50 billion a year (about US$3.4 million at the 2022 rate) were 0.5 percent of BPS's marketplace sellers in 2022 and held between 18 and 39 percent of the marketplace slice's value, resting on 19 sample rows (`tables/part5_checks.json`).

Across the 34 provinces, count growth had a rank correlation of 0.10 (p = 0.59) with the share of new sellers and 0.35 (p = 0.04) with growth in sample size. In 23 provinces count growth exceeded what entry can explain, and these provinces carry 98.5 percent of the increase. The standard error of the national count implied by BPS's published relative standard errors is about 1.4 percent. The 306 thousand newly counted sellers are about 4.6 times the standard error of the change, and 2.3 times if the true error were twice as large (`tables/bps_frame_check.json`, `tables/rq_closing_checks.json`).

### C.3 Checks on the growth test and on the regressions (exploratory, 25 Oct 2026)

The first table repeats the test of the size of take-rate moves with other measures of the yearly change. The second gives the correlation of revenue growth and transaction value growth with and without capping the growth rates, and the rank correlation. The third lists the checks on the coefficient on IndonesiaRegion in Table 5.4. Sources: `h1_simple_change.py` (`tables/h1_simple_change.json`), `kong_regressions.py` (`tables/kong_results.json`), `build_regression_panel.py` (`tables/regression_panel.csv`).

| Measure of the yearly change in the take rate | Indonesian and regional (median) | Foreign (median) | Ratio | Mann–Whitney p |
|---|---|---|---|---|
| Absolute change in the logarithm (the first version) | 0.201 | 0.062 | 3.3 | 0.0038 |
| Absolute simple percentage change (Section 5.2) | 0.224 | 0.062 | 3.6 | 0.0031 |
| Absolute change over the mean of the two take rates | 0.199 | 0.062 | 3.2 | 0.0038 |

| Sample | Correlation, capped | Correlation, not capped | Rank correlation | Pairs |
|---|---|---|---|---|
| Foreign | 0.90 | 0.54 | 0.89 | 166 |
| Indonesian and regional | 0.31 | 0.18 | 0.64 | 15 |
| All platforms | 0.84 | 0.53 | 0.87 | 181 |

| Check | Dependent variable | IndonesiaRegion | p | Wild-bootstrap p | Observations |
|---|---|---:|---:|---:|---:|
| Table 5.4, column (3) | ln(Wedge) | 0.080 | 0.841 | 0.866 | 178 |
| Table 5.4, column (6) | Ecosystem ratio | 17.092 | <0.001 | 0.005 | 178 |
| Without Blibli | ln(Wedge); Ecosystem ratio | 0.267; 15.330 | | | |
| Without Bukalapak | ln(Wedge); Ecosystem ratio | -0.256; 16.072 | | | |
| Without GoTo (on-demand) | ln(Wedge); Ecosystem ratio | 0.148; 18.344 | | | |
| Without Grab (on-demand) | ln(Wedge); Ecosystem ratio | 0.023; 17.803 | | | |
| Without Tokopedia | ln(Wedge); Ecosystem ratio | 0.104; 16.620 | | | |
| Without year dummies | ln(Wedge) | -0.302 | 0.395 |  |  |
| Without year dummies | Ecosystem ratio | 12.939 | <0.001 |  |  |
| Without total assets | ln(Wedge) | 1.197 | 0.246 |  | 187 |
| Without total assets | Ecosystem ratio | 17.027 | <0.001 |  | 187 |
| Without years before listing | ln(Wedge) | -0.113 | 0.711 |  | 165 |
| Without years before listing | Ecosystem ratio | 16.244 | <0.001 |  | 165 |
| Without Alibaba, Pinduoduo, Rakuten and Shopify | ln(Wedge) | 0.383 | 0.394 |  |  |
| Without Alibaba, Pinduoduo, Rakuten and Shopify | Ecosystem ratio | 20.954 | <0.001 |  |  |
| With a dummy for emerging home markets | ln(Wedge) | 0.065 | 0.869 | 0.886 |  |
| With a dummy for emerging home markets | Ecosystem ratio | 16.888 | <0.001 | 0.027 |  |
| Without the six platforms with an ambiguous main market (Sea, Jumia, Mercado Libre, Despegar, Shopify, Fiverr) | ln(Wedge) | 0.145 | 0.743 | 0.801 | 144 |
| Without the six platforms with an ambiguous main market (Sea, Jumia, Mercado Libre, Despegar, Shopify, Fiverr) | Ecosystem ratio | 16.974 | <0.001 | 0.024 | 144 |
| Natural logarithm of the ecosystem ratio | ln(Ecosystem ratio) | 1.677 | <0.001 | 0.006 |  |
| Ecosystem ratio not capped | Ecosystem ratio | 28.550 | 0.008 |  |  |

## Appendix D. Registered tests and their outcomes

A registered test was written down, dated and stored in the repository before the data it concerns were opened. The dates are those of the commits in `research/option_space_2026-10-01/PREREGISTRATION.md`. Exact wording and thresholds are in that file.

| Test | What it predicted | Registered | Outcome |
|---|---|---|---|
| E1 | Sellers without financial statements hold a smaller share of online value than of the count | 2 Oct 2026 | Holds, as a range (25.7 to 40.4 percent of value against 79.3 percent of the count) |
| E2 | The marketplace share of online value in 2022 is above the published 2023 figure | 2 Oct 2026 | Holds, as a range (22.6 to 25.6 percent) |
| E2b, E2c | Marketplace use did not rise between 2020 and 2024 | 2 Oct and 3 Oct 2026 | Hold (21.6, 19.8, 17.8 and 17.2 percent) |
| E3 | Shopee reaches at least as many sellers as Tokopedia | 2 Oct 2026 | Holds (7.5 against 2.2 percent of all sellers) |
| E4 | Entrants use chat or social media at least as often as earlier sellers | 2 Oct 2026 | Holds, with no power (nearly everyone uses them) |
| E5 | At least 21.5 percent of 2023 sellers began in 2023 (the entry test) | 2 Oct 2026 | Falsified (13.45 percent). Disclosure: BPS's 2024 publication, held at registration, has a table of 2024 sellers by start year; if the seller population were stable from 2023 to 2024, it would cap the 2023 share near 18 percent. The table was first used on 8 Oct, after the test ran on 7 Oct |
| E6 | The median change in sales of sellers already online is at most 10.36 percent | 2 Oct 2026 | Holds (median 0 percent) |
| E7 | The share of value held by sellers without statements fell by at most 5 points from 2020 to 2022 | 3 Oct 2026 | Falsified, narrowly (5.8 points; 3.3 on the second version) |
| E8 | Sellers with revenue of Rp300 million a year or more hold over half of marketplace value | 3 Oct 2026 | Holds (92.2 percent, middle scenario, an upper bound) |
| RBI | The marketplace part sold to final consumers is below Bank Indonesia's 2022 figure | 3 Oct 2026 | Holds in the low (0.16) and middle (0.68) scenarios; fails in the high one (1.62) |
| W1, W2 | Unregistered firms using social media keep written records and take digital payments more often | 3 Oct 2026 | Hold (29.9 against 12.3 percent; 11.5 against 2.7 percent) |
| W3 | Their mean annual sales are below Rp100 million (about US$6,600) | 3 Oct 2026 | Falsified (mean Rp111 million; median Rp60 million) |
| F1, F2 | Formal firms with a website take more e-payments and file taxes online more often | 3 Oct 2026 | Hold |
| F3 | More than one third of formal firms have neither a website nor online tax filing | 3 Oct 2026 | Holds (39.9 percent), after a disclosed coding fix: the first run read "yes, partially" as no for online filing and gave 13.0 percent; the questionnaire counts it as yes |
| X3 | Indonesia's share of firms with neither is the highest of the countries compared | 3 Oct 2026 | Withdrawn as a test (addendum of 16 Oct 2026): published e-filing shares seen at registration already capped every other country below Indonesia. Reported as descriptive (Malaysia 9.1, Thailand 8.7) |
| X2 | Firms with a website file taxes online more often, in at least 3 of 4 countries | 3 Oct 2026 | Holds in 4 of 4 |
| Q1 | The test of H1 with quarterly pairs rejects H1 | 7 Oct 2026, before it was run, but after the quarterly series had been built and the annual result was known, so it is a robustness check | Falsified (p = 0.19) |
| M1 | Markets value growth from more transactions more than growth from a higher take rate | 8 Oct 2026, before the market values were pulled | Falsified in the main sample (p = 0.20) and with extreme values capped (p = 0.16); holds in the second run of 34 platforms (p = 0.004), which mixes segment figures with whole-company values |
| M2 | Market value moves with transaction value | 8 Oct 2026 | Holds (p = 0.002) |
| L (P1 to P3) | Large take-rate moves driven by discounts occur only where incentives are at least as large as revenue (L of 1 or more) | 2 Oct 2026 | Thin support out of sample: P1 holds on 2 of 2 cases; P3 fails at the main threshold (median move 0.117 against 0.10); rank correlation 0.20 (p = 0.43) |
| P1 to P5, R1 to R3 | Predictions on the third-quarter 2026 results of GoTo, Grab and Sea | 2 and 3 Oct 2026 | Not yet scored; first results are due on 27 Oct 2026 |
| Marketplace tax start | The tax start slips again | 2 Oct 2026 | Withdrawn: collection began on 1 Oct 2026, before the prediction was registered (addendum of 15 Oct 2026) |
| BPS marketplace share | The next published marketplace share is at most 15.79 percent | 2 Oct 2026 | Not yet scored |

## Appendix E. The values behind Figures 5.3 to 5.5

**Growth in 2023, percent (Figure 5.3).** Household spending +9.4; Tokopedia transaction value −8.9; GoTo on-demand transaction value −10.5 (rests on an estimated 2022 value); Bank Indonesia e-commerce −4.7; Momentum Works marketplace estimate +3.5 (calculated from its published levels; its 2024 release states 3.7); Bukalapak transaction value +6.9; Blibli third-party retail transaction value +34.7; Tokopedia revenue +53.2; BPS e-commerce value +40.6; BPS online sellers +27.4. Sources: `tables/consistency_grid_growth.csv`, `tables/yardsticks_bi_bps.csv`, `tables/wedge_over_time.csv`, `tables/h1_groundwork.json`, company filings.

**Who the extra sellers were, percent (Figure 5.4).** Share of the 2022 count and share of the extra count: business opened before 2010, 18.3 and 40.5; owner aged 50 or over, 28.9 and 41.2; outside Java, 23.6 and 36.3; food and lodging or making goods, 38.5 and 53.0. Source: `tables/bps_newly_counted_profile.json`.

**Marketplace use and financial statements, percent of sellers (Figure 5.5).** Marketplace use: 21.6 (2020), 19.8 (2022), 17.8 (2023), 17.2 (2024, published). Complete financial statements: 23.5 (2020), 20.7 (2022), 15.2 (2023). Source: `tables/bps_descriptives.json`.

The figures are drawn from the tables named above (`papers/thesis_2026-10/figures/make_figures.py`). In each figure, a legend or label names every colour.
