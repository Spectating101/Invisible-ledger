# How the 27 foreign platforms book incentives paid to end users (15 Oct 2026)

Status: research note, not thesis text. Exploratory. The re-test below was designed after the H1 result was known. Nothing here changes Chapter 5.

Script: `incentive_accounting_check.py` (this folder). It reads `../tables/h1_extended_firms.csv` and `../tables/spinoff_panel.csv` and writes nothing.

## Why this check

The June 2026 FASB EITF issue summary (*Consideration Payable to a Customer*, 23 June 2026, https://storage.fasb.org/EITF-Issue%20Summary-Consideration%20Payable%20to%20a%20Customer-20260623.pdf) reports "significant diversity in practice." The question is whether a marketplace's incentives to end users (shoppers, riders, guests: its customer's customers) reduce revenue or are booked as sales and marketing. If many foreign platforms book them as marketing, their take rates would move less when incentives change. That would be an accounting reason for part of the H1 gap. GoTo, Grab and Tokopedia take incentives out of revenue.

## Summary

- **The 27 platforms do not book end-user incentives the same way.** Eight book them mainly as costs, not against revenue (4 with an explicit policy: eBay, 1stDibs, PDD, Mogu; 4 with weaker evidence: Alibaba, Rakuten, Shopify, Etsy). Eleven deduct them from revenue. Three use a rule or are partly unclear (Sea, Mercado Libre, Ozon). Four have no material end-user incentives (Fiverr, Upwork, Vacasa, RB Global). One changed policy inside the sample (Yatra).
- **Accounting does not explain the gap.** The eight that book incentives as costs do not have steadier take rates. Their median of platform medians is 0.060, against 0.075 for the eleven that deduct (two-sided Mann–Whitney p = 0.90). Dropping them leaves the foreign median at 0.062 and the Mann–Whitney p at 0.0035 (main test: 0.0038).
- **The most volatile foreign platforms are not the "expense" ones.** Sea (0.25), Alibaba (0.21), Mogu (0.21), Ozon (0.18) and Jumia (0.16) top the foreign list. Sea caps the deduction at the revenue from each order. Alibaba and Mogu book promotions as marketing. Jumia deducts. The class does not line up with volatility.
- **One policy change sits inside the sample.** Yatra moved customer inducement costs from marketing to a reduction of revenue on 1 April 2018 (IFRS 15, not restated). Its FY2018 to FY2019 take-rate change is −0.45 in log terms, a break caused by accounting. Its median barely moves (0.035 to 0.032) because it has 11 pairs. This is a direct example of how much the booking choice can move a take rate in one year.
- **The suggested Uber rule needs correcting.** In the 2025 10-K, Uber books targeted end-user discounts as sales and marketing. It books market-wide promotions as a reduction of revenue. When customer incentives exceed the revenue from a trip, Uber books the shortfall as a reduction of revenue. Sea is the platform that reduces revenue up to the order's revenue and sends the excess to marketing.
- **Uber, DoorDash, Lyft, Airbnb and Booking are not among the 27.** They appear only in the quarterly check (Appendix B: 3 against 8). They are classified below for that check, and the quarterly test was not re-run.

## Platforms and years in the H1 test

Years are the later year of each yearly pair used (from `tables/spinoff_panel.csv` and `tables/transitions_master.csv`). Fiscal years end in March for Alibaba, Mogu and Yatra.

| Platform | Revenue used in the panel | Pairs (later year) |
|---|---|---|
| ACV Auctions (ACVA) | total revenue | 2021–2025 |
| Waitr (ASAPQ) | revenue | 2017–2022 |
| Alibaba (BABA) | total revenue | FY2015–FY2021 |
| Despegar (DESP) | total revenue | 2016–2024 |
| 1stDibs (DIBS) | net revenue | 2020–2025 |
| Expedia (EXPE) | total revenue | 2015–2025 |
| Fiverr (FVRR) | total revenue | 2019–2025 |
| GrubHub | total revenues | 2015–2020 |
| Hepsiburada (HEPS) | revenues | 2020–2024 |
| Kaspi.kz (KSPI) | total revenue | 2022–2025 |
| Mogu (MOGU) | total revenues | FY2018–FY2026 |
| Ozon | total revenue | 2022 |
| PDD | total revenues | 2018–2021 |
| RB Global (RBA) | total revenue | 2015–2025 |
| The RealReal (REAL) | total revenue | 2018–2025 |
| Vivid Seats (SEAT) | revenue | 2020–2025 |
| Upwork (UPWK) | revenue | 2018–2025 |
| Vacasa (VCSA) | total revenue | 2020–2024 |
| Yatra (YTRA) | total revenue | FY2016–FY2026 |
| Etsy | total revenue | 2020, 2022, 2024 |
| Jumia | total revenue | 2022, 2023, 2025 |
| Mercado Libre | commerce revenue | 2022, 2023 |
| Rakuten | Domestic EC segment revenue | 2025 |
| Sea / Shopee | e-commerce segment revenue | 2018–2021, 2023–2025 |
| Shopify | total revenue | 2020–2022, 2024, 2025 |
| Zalando | group revenue | 2021–2024 |
| eBay | net revenue | 2022–2025 |

## Treatment by platform

Classes: **DEDUCTS** (end-user incentives reduce revenue), **EXPENSES** (booked as sales and marketing or cost of revenue), **MIXED** (rule-based split, or partly unclear), **NA** (no material end-user incentives disclosed), **CHANGED** (policy changed inside the sample). "Weak" means the policy is inferred, small, or applies only late in the window. All quotes are copied from the filing text. Section names are given because the converted text has no page numbers.

| Platform | Class | Principal or agent | Quote | Source (section) | Policy change in sample years |
|---|---|---|---|---|---|
| eBay | EXPENSES | Agent for marketplace fees | "Promotions and incentives to most buyers on our Marketplace platforms, to whom we have no performance obligation, are recognized as sales and marketing expense." | 10-K FY2025, Note 1, Revenue recognition: https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm ; same sentence in 10-K FY2021: https://www.sec.gov/Archives/edgar/data/1065088/000106508822000006/ebay-20211231.htm | None seen (FY2021 and FY2025 identical) |
| 1stDibs (DIBS) | EXPENSES | Agent (net) | "The Company records discounts provided to the end buyer, to whom the Company has no performance obligation, such as promotional discounts, in sales and marketing expense since the discounts are not related directly to the Company's revenue source but rather used as a marketing tool, and the seller is not made aware of the discounts provided to the end buyer." | 10-K FY2025, Note 2, Revenue recognition: https://www.sec.gov/Archives/edgar/data/1600641/000160064126000007/dibs-20251231.htm ; same in 10-K FY2021 | None seen |
| PDD | EXPENSES | Agent for marketplace services | "We recognize the amounts of coupons and credits as marketing expenses when future purchases are completed or when the credits are issued. Discounts unconditionally provided to the consumers are recognized as marketing expenses when the related transaction services revenues from merchants are recognized." | 20-F FY2021, Item 5 critical accounting policies, Revenue recognition: https://www.sec.gov/Archives/edgar/data/1737806/000110465922049283/pdd-20211231x20f.htm ; FY2018 20-F: "the Group recognizes the amounts of redeemed coupons as marketing expenses when future purchases are made" | None seen. Membership coupons are netted against membership revenue first (small) |
| Mogu (MOGU) | EXPENSES | Agent for marketplace; principal for small direct sales | "As the users are required to make future purchases of the merchants' merchandises to redeem the vouchers, the Group recognizes the amounts of redeemed vouchers as marketing expenses when future purchases are made." | 20-F FY2026 (Mar 2026), Note 2: https://www.sec.gov/Archives/edgar/data/1743971/000119312526315001/mogu-20260331.htm ; same in 20-F FY2019 | None seen |
| Alibaba (BABA) | EXPENSES (weak) | Mostly principal for marketing services to merchants; net for some commissions | "Sales and marketing expenses consist primarily of online and offline advertising expenses, promotion expenses, staff costs and share-based compensation expense, sales commissions and other related incidental expenses that are incurred directly to attract or retain consumers and merchants." No explicit rule on consumer incentives in the revenue note. | 20-F FY2021 (Mar 2021), Note 2(j): https://www.sec.gov/Archives/edgar/data/1577552/000110465921096092/baba-20210331x20f.htm | Not checked year by year |
| Rakuten (Domestic EC) | EXPENSES (weak) | Agent for Ichiba fees; principal for Rakuten 24 and Books | Points: "In anticipation of the future use of such points by members, the Group Companies recorded a provision for customer points at an estimated amount based on historical experiences etc." Parent-company income statement lists "Point expenses" of ¥159,065 million (2023) inside selling, general and administrative expenses. Rakuten Card points, by contrast, "are deducted from the interchange fees." | Annual Securities Report FY2023 (English), notes on provisions and revenue: https://links.sgx.com/1.0.0/corporate-announcements/IXQCWEONVGSEYPA3/808102_Annual%20Securities%20Report_FY2023.pdf | The test pair is 2024–2025. The FY2024 and FY2025 reports were not read |
| Shopify | EXPENSES (weak) | Mostly principal (gross); agent for shipping labels, apps, themes | "Rewards issued to buyers, to whom we have no performance obligation, are generally expensed as a cost of revenues, however depending on the program policy the rewards were earned under, they may be expensed as sales and marketing." | 10-K FY2025, Note 2, Rewards Program: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm ; same in 10-K FY2024 | Shop Cash is not mentioned in the FY2019 or FY2023 40-F cover documents. The financial-statement exhibits of those 40-Fs were not read. Buyer rewards look small and recent |
| Etsy | EXPENSES (weak) | Mostly gross for fees; net for shipping labels | "we held several site-wide promotional events in 2024 funded by a small allocation of Etsy's marketing dollars." No end-user incentive policy in the revenue note. | 10-K FY2024, Item 1, Promotional events: https://www.sec.gov/Archives/edgar/data/1370637/000137063725000017/etsy-20241231.htm | No such events in the FY2019 10-K. Incentives look small in every year |
| Sea / Shopee | MIXED | Agent for marketplace | "sales incentives given to end users as a result of a concurrent sale are recognized as reductions of the corresponding consideration that the Company expects to receive. In some instances, the Company may record losses from transactions when the sales incentives provided exceed the revenue earned from the customer on a transaction-by-transaction basis. Such losses are then reclassified and recorded in sales and marketing expenses." | 20-F FY2025, Note 2(s), Advertising expenditure (local copy `sources/core_public_documents/sea_fy2025_20f_yahoo_cdn.htm`); same in FY2023 20-F. FY2017 20-F: "To the extent that the sales incentives exceed commission received, the excess is recorded in sales and marketing expenses." https://www.sec.gov/Archives/edgar/data/1703399/000119312518113294/d414468d20f.htm | Same rule throughout. The basis moved from ASC 605-50 (FY2017) to ASC 606 |
| Mercado Libre | MIXED | Agent for marketplace and most shipping; principal for 1P and some shipping | Shipping: "When the Company acts as an agent, revenues derived from the shipping services are … presented net of the transportation costs charged by third-party carriers … As part of the Company's business strategy, shipping costs may be fully or partially subsidized at the Company's option." Loyalty: "Benefits granted to customers under the Company's loyalty program are accounted for as material rights and therefore the allocated amount of revenue is deferred". Coupons are listed under advertising: "use of targeted promotional discount coupons." | 10-K FY2023, Note 2, Revenue recognition, and Item 1 (Marketing): https://www.sec.gov/Archives/edgar/data/1099590/000109959024000008/meli-20231231.htm | Shipping subsidies reduce revenue when MELI is agent. Where coupons are booked is not stated |
| Ozon | MIXED (partly unclear) | Agent for marketplace (net); principal for direct sales | "Where the loyalty points give rise to a material right to the customer, a portion of the transaction price is allocated to the respective performance obligation … and recognized as deferred revenue". Sales and marketing includes "costs aimed at improving loyalty of customers." No rule for other buyer discounts. | 20-F FY2022, Note 2(d): https://www.sec.gov/Archives/edgar/data/1822829/000119312523115002/d445088d20f.htm | One pair only (2021–2022) |
| ACV Auctions | DEDUCTS | Agent (net) for auction fees | "Promotions and incentives, which are consideration payable to a customer, are recognized as a reduction of revenue when revenue is recognized." Buyers and sellers both pay fees, so both are customers. | 10-K FY2025, Note 2: https://www.sec.gov/Archives/edgar/data/1637873/000163787326000011/acva-20251231.htm ; same in 10-K FY2021 | None seen |
| Waitr (ASAPQ) | DEDUCTS | Agent (net) | "we recognize as revenue only our fees (which are assessed as a percentage of the total food sales … net of any diner promotions or refunds to diners) and diner fees." | 10-K FY2018, Item 7: https://www.sec.gov/Archives/edgar/data/1653247/000156459019007876/wtrh-10k_20181231.htm . The FY2022 10-K says the company "is an agent of the restaurant and the diner", so diners are customers: https://www.sec.gov/Archives/edgar/data/1653247/000165324723000038/wtrh-20221231.htm | No promotion wording in the FY2022 10-K. Not checked for FY2017 and FY2019–FY2021 |
| Despegar | DEDUCTS (inferred) | Agent (net) for most travel | "We consider both the traveler and the travel supplier as our customers." Loyalty: "The portion of each travel product sale attributable to loyalty points is initially deferred and then recognized in loyalty revenue when the points are redeemed." No explicit sentence on discount coupons. Bank fees for interest-free installments go to cost of revenue. | 20-F FY2024, Note 3, Revenue recognition: https://www.sec.gov/Archives/edgar/data/1703141/000162828025020808/desp-20241231.htm | Not checked year by year |
| Expedia | DEDUCTS | Agent for most merchant and agency hotel; travelers are customers | "Current Discount Offers. These promotions include dollar or percent off discounts to be applied against current purchases. We record the discounts as reduction in revenue at the date we record the corresponding revenue transaction." | 10-K FY2025, Note 2, Marketing Promotions: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm ; same in 10-K FY2017 | Loyalty moved from a cost recorded against revenue (FY2017) to deferral of revenue (ASC 606, 2018). Both reduce revenue |
| GrubHub | DEDUCTS | Agent for takeout; principal for delivery | "The Company periodically provides incentive offers to restaurants and diners to use our platform. These promotions are generally cash credits to be applied against purchases. These incentive offers are recorded as a reduction in revenues, generally on the date the corresponding order revenue is recognized." | 10-K FY2020, Note 2: https://www.sec.gov/Archives/edgar/data/1594109/000156459021009522/grub-10k_20201231.htm ; same in 10-K FY2016 | None seen |
| Hepsiburada | DEDUCTS | Agent for marketplace; principal for 1P | "The Group may, at times, provide discounts to the Marketplace customers. Any such discounts affect the amount of commission the Group will retain and are thus recognized as a reduction of revenue since they are a discount provided to a customer by the Group and therefore reduce the commission to be received." | 20-F FY2024, Note 2, Revenue: https://www.sec.gov/Archives/edgar/data/1850235/000110465925041729/heps-20241231x20f.htm ; same in 20-F FY2021 | None seen |
| Jumia | DEDUCTS | Agent for marketplace; principal for 1P | "Incentives to end consumers, which include discounts or vouchers, and marketplace subsidies to sellers are consideration payable to a customer and are recognized as a reduction of revenue." | 20-F FY2025, Item 5: https://www.sec.gov/Archives/edgar/data/1756708/000175670826000015/jmia-20251231.htm ; same in 20-F FY2021 | None seen |
| Kaspi.kz | DEDUCTS | Mixed (fees net; retail gross) | "Bonuses are accounted as variable consideration paid to customers … these bonuses are presented as a deduction from revenue. For segment reporting purposes we continue to account for rewards as selling and marketing expenses". | 20-F FY2023, Note 3: https://www.sec.gov/Archives/edgar/data/1985487/000095017024049512/kspi-20231231.htm ; same in 20-F FY2025 | The panel uses group revenue, which is net of rewards |
| The RealReal | DEDUCTS | Agent (net) for consignment; principal for direct | "Buyer incentives apply to specific buyers and consist of coupons or promotions that offer credits in connection with purchases on the Company's platform, and do not impact the commissions paid to consignors. These are treated as a reduction of consignment revenue and direct revenue." | 10-K FY2025, Note 2, Incentives: https://www.sec.gov/Archives/edgar/data/1573221/000157322126000010/real-20251231.htm ; FY2019: "Promotional incentives … offered to consignors and buyers. These are treated as a reduction of consignment and service revenue and direct revenue." | None seen |
| Vivid Seats | DEDUCTS | Agent (net) for marketplace | "Revenue primarily consists of service fees from ticketing operations and is reduced by incentives provided to ticket buyers." | 10-K FY2021, Note 2: https://www.sec.gov/Archives/edgar/data/1856031/000095017022003749/seat-20211231.htm ; same in 10-K FY2025 | None seen |
| Zalando | DEDUCTS | Principal for wholesale (most revenue); agent for Partner Program | "Revenue is recorded net of sales deductions, taxes and duties." Consumers are its direct customers, so a consumer discount is a price cut. | Annual Report 2022, Notes, Revenue recognition: https://corporate.zalando.com/public/media-download/Annual%20Report_Zalando%20SE_22_EN_230603_sc.pdf?VersionId=HV7ssiSfln45xsj90RjE7e1c5b94wXRi | Reports for 2020, 2021, 2023 and 2024 were not read |
| Yatra | CHANGED (EXPENSES to DEDUCTS) | Agent (net) for air; gross for some packages | FY2017: "the company also incurs customer inducement and acquisition costs … such as upfront cash incentives, which when incurred are recorded as marketing and sales promotion costs." FY2019: "pursuant to which upfront cash incentives, loyalty programs costs for customer inducement and acquisition costs … some of which, when incurred, were previously recorded as marketing and sales promotion costs, are now recorded as an offset of revenue … the comparative information has not been r[estated]". | 20-F FY2017: https://www.sec.gov/Archives/edgar/data/1516899/000114420417035210/v469854_20f.htm ; 20-F FY2019, Item 5: https://www.sec.gov/Archives/edgar/data/1516899/000104746919004463/a2239368z20-f.htm ; FY2026 still deducts | Yes. From 1 April 2018 (FY2019), not restated. Revenue fell 23.6% while gross bookings rose 20.1%. The panel's FY2019 pair (−0.45) is an accounting break |
| Fiverr | NA | Agent (net) | "Revenue is recognized on a net basis since the Company has concluded that it acts as an agent on its platform". "The Company's customers are the users on its platform." No end-user incentive policy is disclosed. | 20-F FY2025, Note 2: https://www.sec.gov/Archives/edgar/data/1762301/000117891326000858/zk2634486.htm | None seen |
| Upwork | NA | Agent (net) for talent fees | "the Company presents revenue from talent service fees on a net basis as an agent." No end-user incentive policy is disclosed. | 10-K FY2025, Note 2: https://www.sec.gov/Archives/edgar/data/1627475/000162747526000012/upwk-20251231.htm | None seen |
| Vacasa | NA | Agent for homeowners | Only cancellation refunds are discussed: "We account for these refunds as variable consideration, which results in a reduction to revenue." No promotional incentive policy. | 10-K FY2024, Item 7: https://www.sec.gov/Archives/edgar/data/1874944/000187494425000003/vcsa-20241231.htm | None seen |
| RB Global | NA | Net for commissions; gross for inventory sales | No end-user incentive policy found in the FY2021 or FY2025 10-K revenue notes. | https://www.sec.gov/Archives/edgar/data/1046102/000162828026011682/rba-20251231.htm | Not checked for FY2015–FY2020 |

### Platforms outside the 27 (quarterly check only; priority list from the coordinator)

| Platform | Class | Quote | Source (latest 10-K, Note 2 or revenue policy) |
|---|---|---|---|
| Uber | EXPENSES for targeted end-user promotions; market-wide promotions and shortfalls DEDUCT | "We record the cost of these discounts and promotions to end-users who are not our customers as sales and marketing expenses at the time they are redeemed by the end-user." Also: "End-user discounts and promotions are recorded to sales and marketing expenses with the exception of market-wide promotions which are recorded as a reduction of revenue." | 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm |
| Lyft | EXPENSES for riders; driver incentives DEDUCT | "Incentives provided to riders are generally recognized as sales and marketing expense with the exception of market-wide marketing promotions." | 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1759509/000162828026006960/lyft-20251231.htm |
| DoorDash | DEDUCTS (mostly) | "Promotions offered to consumers are primarily recorded as a reduction of revenue". Referral credits up to fair value go to sales and marketing. | 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1792789/000179278926000013/dash-20251231.htm |
| Airbnb | DEDUCTS (mostly) | "Revenue is net of incentives and refunds provided to customers." Referral coupons go to marketing up to fair value; once a customer redeems one, revenue is reduced. | 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm |
| Booking | DEDUCTS | "The estimated value of the incentives granted and the loyalty points expected to be redeemed is generally recognized as a reduction of revenue at the time they are granted." | 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm |

Only the latest 10-K was read for these five. Years before 2025 were not checked here; `tables/src/us_10k_NOTES.txt` has earlier notes on Uber, Lyft and DoorDash.

### Not checked, or checked only in part

- Rakuten FY2024 and FY2025 reports (the only pair in the test). The class rests on the FY2023 report.
- Zalando 2020, 2021, 2023 and 2024 annual reports. The class rests on the 2022 report.
- Shopify 40-F financial-statement exhibits for FY2019–FY2023. Only the cover documents and the FY2024 and FY2025 10-Ks were read.
- Alibaba: no explicit consumer-incentive sentence was found. The class is inferred from the sales and marketing policy.
- Despegar and Ozon: no explicit sentence on discount coupons.
- For most platforms only the first and last filings in the window were read. A change in between would be missed unless later notes mention it. Yatra's change was found this way.

## Exploratory re-test

Exploratory. It was designed after the H1 result was known. The unit is one median of |Δln take rate| per platform, as in `h1_extended.py`. The Indonesian and regional group (5 platforms, median 0.201) is unchanged. Tests are one-sided Mann–Whitney plus a label-shuffle test (9,999 shuffles, seed 20261015). The main test reproduces Mann–Whitney p = 0.0038. Its shuffle p is 0.019 here against 0.0221 in Appendix B because the seed differs.

| Foreign group | Platforms | Foreign median | Mann–Whitney p | Shuffle p |
|---|---|---|---|---|
| All 27 (main test) | 27 | 0.062 | 0.0038 | 0.019 |
| Drop 4 with an explicit EXPENSES policy | 23 | 0.062 | 0.0033 | 0.017 |
| Drop all 8 EXPENSES (explicit and weak) | 19 | 0.062 | 0.0035 | 0.007 |
| Drop 8 EXPENSES and Yatra | 18 | 0.066 | 0.0045 | 0.009 |
| Keep only DEDUCTS and NA | 15 | 0.062 | 0.0012 | 0.002 |
| Keep only DEDUCTS | 11 | 0.075 | 0.0043 | 0.005 |
| All 27, Yatra without its FY2019 break | 27 | 0.062 | 0.0038 | 0.023 |

Within the foreign group, the 8 EXPENSES platforms have a median of 0.060 and the 11 DEDUCTS platforms 0.075. The two-sided Mann–Whitney p is 0.90, so there is no sign that booking incentives as marketing steadies the take rate. The MIXED group has the highest median (0.177: Sea 0.25, Ozon 0.18, Mercado Libre 0.06). Sea's rule still deducts incentives up to the revenue from each order, so its revenue absorbs most incentive swings.

**Reading.** The accounting choice could in principle damp a platform's take-rate swings. In this sample it does not explain the gap. Every version keeps the Indonesian median at more than 2.5 times the foreign median, with Mann–Whitney p below 0.005. Yatra shows the size of the effect in a single year: one reclassification moved its log take rate by 0.45. The median per platform absorbs one such break when a platform has many pairs. A platform with one or two pairs would not absorb it.

**Two cautions.** The classes rest on policy text, not on amounts. Most filings do not report end-user incentives separately, so the share of incentives that sits outside revenue is unknown. The comparison also cannot fix the scope differences (segment against group revenue, first-party sales) already listed in Chapter 4.

## Draft sentences for Chapter 7.4 (limits)

Each sentence is 12 to 18 words. The numbers are from the table above.

> Foreign platforms do not all book shopper discounts the same way, as accounting rule makers noted in 2026. Eight of the 27 record these discounts mainly as marketing costs, not as lower revenue. Such platforms could show steadier take rates for an accounting reason alone. Their take rates were not steadier: median yearly change 0.06, against 0.07 for platforms that deduct. Without them, the foreign median stays at 0.06, and the test still gives p = 0.004. This check was designed after the result was known, so it is exploratory.

Shorter version (two sentences):

> Eight foreign platforms book shopper discounts as marketing costs, which could steady their take rates. Dropping them leaves the foreign median at 0.06 and the gap with Indonesia in place.

Word check: "Foreign platforms … in 2026" 18; "Eight of the 27 … lower revenue" 17; "Such platforms … alone" 12; "Their take rates … that deduct" 16; "Without them … p = 0.004" 18; "This check … exploratory" 14. Short version: 15 and 16. The 0.06 is the median of the 8 platforms that book discounts as costs (0.0596). The 0.07 is the median of the 11 that deduct them (0.0745). The p = 0.004 is the Mann–Whitney p without the eight (0.0035).

For Chapter 7.5 (next steps), if wanted: collect each foreign platform's yearly amount of end-user incentives where filings report it, and add it back to revenue before testing again.
