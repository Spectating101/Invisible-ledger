# Chapter 4. Data and Methods

This chapter describes the data and the tests behind the results in Chapter 5. It starts with the platform data, which serve the measure of the wedge and the test of H1. It then shows how revenue movements are traced to fees and incentives. After that it turns to the national survey, the entry test and the further analyses. The last parts cover the comparison with national and payment figures, the market values, and the rules that keep every number traceable.

## 4.1 Platform data

A platform-year is one platform's revenue and transaction value in one year. Both come from the company's own reports. Revenue is the amount in its financial statements, and transaction value is the figure it discloses in annual reports and earnings releases. Companies define transaction value in different ways. Some include shipping charges, digital goods or travel. The thesis keeps each company's own definition and records it in a definition map. Each take rate is built within one company, so the company's own definition cancels out of its yearly changes unless the company changes it.

Two groups of platforms are compared. The Indonesian and regional group has five platforms, listed in Table 4.1. Two of them, Grab and GoTo, are ride-hailing and delivery businesses, which the thesis calls on-demand. The foreign group has 27 listed platforms. Eight form the first benchmark: Etsy, eBay, Jumia, Mercado Libre, Rakuten, Sea, Shopify and Zalando. The other 19 were added to make the comparison larger. They include online marketplaces, travel and ticketing sites, freelance and resale platforms, and food delivery. Ten more were examined and left out: six sell mostly their own goods, and four do not disclose transaction value. Sea sits in the group although Indonesia is one of its main markets. Chapter 5 reports the narrower test of section 4.2 with and without it. The appendix lists every platform and year.

**Table 4.1. The Indonesian and regional group of platforms**

| Platform series | What it covers | Years | Yearly pairs | How it is labelled |
|---|---|---|---|---|
| Tokopedia | The e-commerce segment of GoTo, an Indonesian marketplace | 2022–2023 | 1 | Direct segment disclosure |
| Blibli | Blibli's third-party retail segment, which includes online travel | 2021–2025 | 4 | Direct segment disclosure |
| Bukalapak | The whole Bukalapak group, mainly in Indonesia, including Mitra, its online-to-offline business | 2020–2023 | 3 | Direct company disclosure |
| Grab on-demand | Grab's rides and deliveries across Southeast Asia, not Indonesia alone | 2020–2024 | 4 | Direct segment disclosure |
| GoTo on-demand | GoTo's rides and deliveries segment, in Indonesia and Vietnam to 2024 | 2022–2025 | 3 | Direct segment disclosure; the 2022 transaction value is an estimate |

Table 4.1 states the scope of each series because the series differ. Only Tokopedia is an Indonesian segment alone. Grab covers the region, GoTo's on-demand segment included Vietnam until 2024, and Bukalapak covers a whole group. The thesis never adds the series together. Each platform enters the tests on its own.

Three rules govern the pairs. Two consecutive platform-years form a pair, and nothing else does. A missing year stays missing and is never filled in. Annual and quarterly pairs are never pooled. Each pair uses the company's own financial year. A take rate is a ratio of two amounts in one currency, so the tests need no exchange rate. Running text gives amounts in US dollars, converted at the World Bank's official average rate for the year.

Two extra rules apply to the foreign group. A company that sells goods itself reports the whole sale as revenue, and its take rate then says little about a platform. For the 19 added platforms, the thesis drops any year in which the company's own goods make up more than half of its revenue. A pair is kept when its second year passes this rule. Years in which own goods make up between a fifth and a half are kept and marked. For the eight first platforms, a pair counts only if the company reported both amounts on the same scope in both years. After these rules, the foreign group has 158 yearly pairs, and the Indonesian group has 15.

The first objective uses a different set of amounts. It sums the transaction value and revenue of three major platforms in Indonesia in 2023: Tokopedia, Shopee and Grab. It then computes the wedge and the ecosystem ratio from the sums. For each platform, it also computes them for every year available between 2020 and 2025, and the appendix gives the results. Tokopedia reports both amounts for its segment. Shopee's transaction value is an outside estimate by Momentum Works. Its revenue assumes a take rate of 10 percent, which the thesis varies from 9 to 11 percent. Grab reports its Indonesian revenue, and the thesis derives its Indonesian transaction value from Grab's company-wide ratio of the two amounts. The thesis also drops each platform in turn.

## 4.2 The test of H1

H1 says that revenue and transaction value grow in proportion. If they do, the take rate stays close to steady. The test measures how far each platform's take rate moves from one year to the next.

For each pair of years, the thesis takes the change in the logarithm of the take rate. A log change treats a rise by some factor and a fall by the same factor as equal in size. It equals the log growth of revenue minus the log growth of transaction value. This makes it growth divergence measured in logs. Chapter 3 defines the same idea in points of growth, and the third check below uses that form. The log form does not depend on how fast transaction value grew. Tokopedia's log change in 2023 is 0.52, which means its take rate rose by a factor of 1.68, or 68 percent.

H1 is about proportion, so a rise and a fall both count against it. The test uses the size of each change and ignores its direction.

Each platform then gets one number: the median size of its yearly changes. The platform is the unit of the test, not the pair, because the pairs of one platform are not independent of one another. The test compares 5 numbers for the Indonesian and regional group with 27 for the foreign group.

Two tests compare the groups. The first is a one-sided Mann–Whitney test. It ranks all 32 platforms by their number and asks whether the Indonesian and regional platforms rank higher than chance would give. It is one-sided because H1 is rejected only if these platforms move more than the others, and not if they move less. The p-value is the chance of a ranking at least this lopsided if the groups did not differ. A small p-value counts against that. The second is a shuffle test. It assigns the group labels to the 32 platforms at random 9,999 times. It then counts how often the gap between the two group medians is at least as large as the real gap.

Four checks follow, and Chapter 5 reports each. The first drops each Indonesian platform in turn. The second treats Tokopedia and GoTo on-demand as one company, since GoTo owned both in 2022 and 2023. It combines their yearly changes in two ways: the median of all of them, and the average of the two platform medians. The third repeats the test with growth divergence in points, as defined in Chapter 3. The fourth is a narrower version that uses only the three Indonesian marketplaces and the eight platforms of the first foreign benchmark. It uses a different measure and a smaller benchmark, so it is not a stricter form of the main test. A description counts the pairs in which the take rate moved by 0.10 or less in log terms. An exploratory comparison, designed after the main result, sets two things side by side. One is the yearly change in the take rate, in percentage points. The other is the share of each sale that each platform keeps.

A quarterly version of the test is run where companies report quarterly pairs. It compares each quarter with the same quarter a year earlier, which removes seasonal swings. Its Indonesian and regional group is Grab on-demand, GoTo on-demand and Blibli. Its foreign group is eight listed platforms: Sea, Airbnb, Booking, DoorDash, eBay, Etsy, Lyft and Uber. It uses its own sample and is never mixed with the annual one.

## 4.3 Tracing revenue movements

The second objective asks where large movements in revenue came from. The thesis answers in two steps.

The first step divides each movement into volume and take rate. In log terms, revenue growth equals transaction value growth plus the change in the take rate. For each pair, the take-rate share is the size of the take-rate change divided by the sum of the sizes of both changes. The same split is made for the wedge, which equals transaction value minus revenue. The share is computed for the three Indonesian marketplaces (8 pairs) and the eight platforms of the first foreign benchmark (29 pairs). Chapter 5 compares their medians.

The second step finds the cause of a take-rate change. A platform's take rate equals the rate of its gross fees minus the rate of its incentives, each measured against transaction value. A rise comes from higher fees, from lower incentives, or from a change in the mix of businesses. The thesis also records where a company's accounting treatment or reporting scope matters, such as the deduction of incentives from revenue and the travel business inside Blibli's retail segment. The thesis splits the growth of revenue over a window into three parts. They are more commerce, a change in the fee rate and a change in the incentive rate.

It makes this split wherever a company discloses both its fees and its incentives. Tokopedia's audited segment note gives gross revenue, incentives and net revenue directly, and the thesis checks them against the audited consolidated statements. For Tokopedia it also reports the change line by line in rupiah, which is the usual way to read accounts. It says where the two views differ. For Grab it uses the annual filings, and for GoTo the audited statements. Blibli does not report incentives, so the thesis uses a proxy built from its releases, and the appendix shows how. Seven windows are traced in all, and the appendix lists them. Where a company does not separate the parts, the movement is left untraced, and the appendix table says so. The thesis reads company explanations as reports and does not test them.

## 4.4 The national survey and the entry test

The national data come from the survey of online sellers run by BPS, the national statistics office. BPS publishes the number of businesses selling online, their total online sales and the shares by channel (BPS 2025). The survey rounds are named for the survey year, but their questions refer to the year before. The thesis names a file by its round and a year by the year of activity. So the file for the 2024 round describes 2023.

H2 uses the published figures. National online sales value equals the number of businesses times the sales per business. In log terms, growth in value is growth in the number of businesses plus growth in sales per business.

```
share from more businesses = Δln(number of businesses) / Δln(value)
```

H2 holds on the published figures if this share is above one half. BPS prints two counts of businesses for 2023. The thesis computes the split with both and reports both. It never replaces one with the other.

The entry test needs the survey files themselves. BPS sold them under a data-use agreement, and Table 4.2 lists them. Each row is one business that sold online in the activity year, and each business has a survey weight. The weight shows how many businesses in the country the row represents, so the weights add up to the national count. The files carry no business identifier across rounds. They carry no area variable below the province. The rounds compare groups of sellers, not the same sellers over time.

**Table 4.2. The three BPS survey files**

| Survey round | Activity year | Rows | Weighted total | BPS count |
|---|---|---|---|---|
| E-Commerce 2021 | 2020 | 11,848 | 2,361,423 | 2,361,423 |
| E-Commerce 2023 | 2022 | 31,724 | 2,995,986 | 2,995,879* |
| E-Commerce 2024 | 2023 | 39,736 | 3,814,799 | 3,816,750 |

*Implied by the published count for 2023 and its published growth of 27.4 percent.

Two checks come before any test. The weighted total of each file must fall within 1 percent of the BPS count, and Table 4.2 shows that all three do. The 2024 file must also reproduce two published shares: 28.63 percent of marketplace sellers and 12.25 percent of other sellers keep complete financial statements. It does so to two decimals. The check confirms that the thesis reads the files as BPS does.

The entry test follows the rule written in Chapter 3. In the 2024 file, the weighted share of businesses that began selling online in 2023 must be at least 21.5 percent. The threshold comes from the published rise of 27.4 percent: 27.4 divided by 127.4 is 21.5 percent. If the weights had matched BPS's other count for 2023, the threshold would have been 23.9 percent. They did not, so 21.5 percent stands. The test was written down and dated in the project's code archive, called the repository, before the files were opened.

If the test fails, a second question follows: how large is the part of the rise that first-time entry does not explain? The thesis answers with a cohort check. A cohort is the group of sellers that began selling online by a given year. If two surveys count the same population, a cohort can only shrink between them, because sellers stop and no new seller can join it. A cohort that grows means the later survey counted sellers the earlier one missed, or that sellers returned after a pause.

The thesis compares the 2023 survey's count of sellers who began before 2023 with the whole 2022 count. It makes the comparison twice. The first assumes that no seller stopped. The second assumes that sellers stopped at about 5 percent a year, the rate at which one cohort shrank between the 2020 and 2022 surveys. The gap is then stated as a share of the published rise. Chapter 5 reports both.

The rest of the national analysis adds a value side, a profile of the extra sellers, a check on part-year selling and a returners scenario. The value side asks how much of the rise in BPS's online sales value the newly counted sellers and the entrants could account for. It values each group at the 2022 average value per seller. For sellers who use only chat or social media, the value is scaled down. It repeats this under each of the three bracket scenarios of section 4.5. What is left over would have to come from sellers who were already counted. The profile takes each group's count in the 2023 survey above what the group's yearly change between the 2020 and 2022 surveys would give. It reports each group's share of that excess. The part-year check uses the months in which each seller sold. It asks whether sellers who returned after a pause could explain the excess. The scenario asks how many returners would remove the unexplained part.

The cohort check and four further checks were designed after the entry test failed, so Chapter 5 labels them exploratory. The first compares count growth with sample size and with the share of new sellers across the 34 provinces. The second splits the extra sellers by the channels they use. The third uses what sellers report about their own sales; its median result was registered, and the rest is exploratory. The fourth asks whether sampling error could explain the gap, using the relative standard errors that BPS publishes. A seller who stopped and returned keeps an old start year, so the files cannot rule out returners. Chapter 5 weighs that reading against the others.

## 4.5 Channels, records and reach

Two further analyses use the same files, and a third builds on them. The first asks which channels sellers use and how sales divide between them. The questions list websites, e-mail, chat, social media and marketplaces, and they ask what share of sales is offline, on marketplaces or elsewhere online. The published tables also split the 2023 to 2024 rise in value between marketplaces and other channels. BPS counts food and ride apps in its marketplace category, so the thesis reports the shares as BPS defines them.

Value by channel needs more care. The 2021 and 2023 files give each business's revenue in four brackets, and the 2024 file gives none. The thesis assigns each bracket a low, a middle and a high amount, and it reports all three scenarios. The scenario amounts were fixed before the file was opened. The 2023 questionnaire asks for monthly revenue, but the bracket limits are annual size classes. The thesis computes both readings and keeps the one that passes a validation rule. The middle scenario's total for 2022, from the 2023 file, must lie between half and double BPS's published total of about US$53 billion. A second rule applies if the lower brackets alone already exceed that total: the thesis then reports value shares as ranges only. If validation fails, it reports only the range between the low and the high scenario.

The second asks whether a seller keeps complete financial statements. This bears on what platform records can add, because a seller with no statements leaves fewer formal records. The thesis reports the share of sellers with statements in each round. It reports the share of online value held by sellers without statements for 2020 and 2022, the two rounds with revenue brackets.

The third, developed in Chapter 6, counts how many sellers a rule based on platform records can reach. It counts marketplace sellers whose revenue is above a bracket line and expresses the count as a share of all online sellers. At the 2022 rate, BPS's brackets divide at about US$20,000 a year, and the marketplace tax exempts individual sellers up to about US$34,000. So the count above BPS's line is an upper limit on the sellers the tax can reach.

World Bank Enterprise Surveys add a check on records. They cover unregistered firms in six Indonesian cities in 2023, and formal firms with five or more employees in seven countries. The appendix describes them.

## 4.6 Comparing platform evidence with national and payment figures

The third objective compares the platform evidence with national and payment figures. Table 4.3 lists the sources and what each one counts. The sources differ in what they cover, so the comparison follows three rules.

**Table 4.3. Sources compared in Objective 3**

| Source | What it covers | How it counts |
|---|---|---|
| Platform reports | Everything bought through one platform | The platform's own records |
| BPS online-seller survey | Every business that sold online, including chat and social media | Listing in sampled areas, scaled up by survey weights |
| Bank Indonesia e-commerce statistics | Transactions of large e-commerce firms (Bank Indonesia 2025) | Data sent to the central bank; the method is not public |
| Industry estimates | Shopping marketplaces in Indonesia or Southeast Asia, from the research firm Momentum Works (2024) and the e-Conomy report (Google, Temasek and Bain 2024) | Outside estimates |
| Household spending | All household purchases | BPS national accounts |
| Payment figures | Payments made through systems such as QRIS, the national QR-code system | Payment records, in person and online |

First, the thesis compares growth rates across sources and keeps each source in its own unit. Second, it compares levels only after reconciling the definitions, using the definition map from section 4.1. Third, it compares sources most closely where their coverage overlaps. The 2023 file lets the thesis separate the part of BPS's marketplace sales that went to final consumers. It compares that part with Bank Indonesia's figure for the same year, in a test written down before the file was opened. The thesis also sets quarterly platform growth beside quarterly household spending growth. It treats payment figures as context. They show how people pay, and not what they buy online.

## 4.7 Market values

The last analysis asks whether markets value a platform's growth in transaction value differently from growth in its take rate. The data are year-end market values from the financial data service LSEG, under the university licence. The main sample has 28 listed platforms and 138 platform-years: Bukalapak and 27 platforms abroad. It overlaps with the groups in section 4.1 but is not the same, and it uses whole-company figures only. A regression relates the yearly change in log market value to the changes in log transaction value and log take rate. It gives one coefficient for each, adds a fixed effect for each year and clusters standard errors by company. Market values are taken at calendar year-end and matched to each company's financial year. Each prediction names a direction, so both tests are one-sided.

Two cautions come with the design. The result is an association. Market value also changes when a company issues shares, so the thesis does not call it a stock return. A second run adds the segment series of Blibli, GoTo and Grab and the whole-company figures of Mercado Libre, Sea and Rakuten. Segment figures do not match a whole company's market value, so that run is a robustness check and not the main test. The test was written down before the market values were pulled.

## 4.8 Keeping every number traceable

Every number in the thesis follows one path: source document, extract, analytic row, result. Each extract keeps the company's currency and units. Each value carries a label: direct company disclosure, direct segment disclosure, external estimate, derived value, conversion or scenario. The thesis never mixes the labels in one sample. It reports a restatement or a conflict between two reports and never overwrites one with the other. A single script rebuilds every table that depends only on committed files, apart from a few built once from local documents, which the script lists. In addition, 272 automatic checks confirm that each recorded result still matches its table.

The thesis also separates tests by when they were written. A registered test was written down, dated and stored in the repository before the data were opened. This applies, among others, to the entry test, the scenario rules for value, the comparison with Bank Indonesia and the market-value test. An exploratory test was designed after some results were seen. Chapter 5 marks each result as registered or exploratory, and the appendix lists the registered tests with their dates.

Three sources are licensed and are not in the repository: the BPS survey files, the LSEG market values and the World Bank survey files. The repository records the size and checksum of each file, so anyone who obtains the same files can check them. It holds the code that reads them and the national totals that the code produces, and no business-level record. BPS is cited as the source of every survey figure, in line with the data-use agreement. Chapter 7 states what these data cannot show.
