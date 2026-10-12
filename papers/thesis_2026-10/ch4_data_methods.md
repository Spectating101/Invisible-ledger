# Chapter 4. Data and Methods

Indonesia lets this thesis look at the same online economy from two sides. Platforms report what passes through them and what they keep. BPS, the national statistics office, asks the sellers themselves. This chapter describes the evidence on each side and the tests that use it. It starts with the platforms, where H1 is tested and revenue movements are traced. It then turns to the survey, where H2 and the entry test are examined. It ends with the comparisons and market values that bring the two sides together.

## 4.1 Choosing the platforms

The basic observation is one platform in one year, which this thesis calls a platform-year. Revenue and transaction value come from the company's own reports, and they refer to the same year and, as closely as the filings allow, the same business. Revenue is the amount in the financial statements. Transaction value is the figure the company discloses in its annual report or earnings release. Companies define it in different ways, and some include shipping charges, digital goods or travel. The thesis keeps each company's own definition and records it. A take rate is built inside one company, so the definition cancels out of its yearly changes unless the company changes it.

Two groups of platforms are compared. The Indonesian and regional group has five platforms, listed in Table 4.1. Three are Indonesian marketplaces, and two are the on-demand businesses of Grab and GoTo, which cover rides and deliveries. The foreign group has 27 listed platforms in marketplaces, travel and ticketing, freelance work, resale and food delivery. Eight were chosen first, and 19 were added to widen the comparison. Ten more were examined and left out, six because they sell mostly their own goods and four because they do not disclose transaction value.

**Table 4.1. The Indonesian and regional group of platforms**

| Platform series | What it covers | Years | Yearly pairs | How it is labelled |
|---|---|---|---|---|
| Tokopedia | The e-commerce segment of GoTo, an Indonesian marketplace | 2022–2023 | 1 | Direct segment disclosure |
| Blibli | Blibli's third-party retail segment, which includes online travel | 2021–2025 | 4 | Direct segment disclosure |
| Bukalapak | The whole Bukalapak group, mainly in Indonesia, including Mitra, its online-to-offline business | 2020–2023 | 3 | Direct company disclosure |
| Grab on-demand | Grab's rides and deliveries across Southeast Asia, not Indonesia alone | 2020–2024 | 4 | Direct segment disclosure |
| GoTo on-demand | GoTo's rides and deliveries segment, in Indonesia and Vietnam to 2024 | 2022–2025 | 3 | Direct segment disclosure; the 2022 transaction value is an estimate |

Table 4.1 states the scope of each series because the series differ. Only Tokopedia is an Indonesian segment alone. Grab covers Southeast Asia, GoTo's on-demand segment included Vietnam until 2024, and Bukalapak covers a whole group. The thesis never adds the series together, and each platform enters the tests on its own. Sea, whose Shopee business has Indonesia as a main market, sits in the foreign group.

Three rules keep the pairs comparable. Two consecutive platform-years form a pair, and nothing else does. A missing year stays missing and is never filled in. Annual and quarterly pairs are never pooled. A take rate is a ratio of two amounts in one currency, so the tests need no exchange rate. Amounts in running text are in US dollars at the World Bank's average rate for the year. In the foreign group, a company that sells goods itself reports the whole sale as revenue, so its take rate says little about a platform. The thesis drops years in which own goods exceed half of revenue and marks years between a fifth and a half. The result is 15 pairs for the Indonesian and regional group and 158 for the foreign group.

## 4.2 Testing H1 and tracing the moves

H1 says that revenue and transaction value grow in proportion, which means that the take rate stays close to steady. The test asks how far each platform's take rate moves from one year to the next. For each pair of years it takes the change in the logarithm of the take rate. A log change treats a rise by some factor and a fall by the same factor as equal in size. It equals the log growth of revenue minus the log growth of transaction value. This is growth divergence measured in logs, and it does not depend on how fast transaction value grew. Tokopedia's log change in 2023 is 0.52, which is a rise by a factor of 1.68, or 68 percent.

A rise and a fall both count against H1, so the test uses the size of each change. Each platform gets one number, the median size of its yearly changes, because the pairs of one platform are not independent of one another. The test compares five numbers for the Indonesian and regional group with 27 for the foreign group. It asks whether the first group ranks higher than chance would give, using a one-sided Mann–Whitney test. It repeats the question by shuffling the group labels 9,999 times. The p-value is the chance of a result at least this lopsided if the groups did not differ. Appendix B lists the checks that follow. They drop each platform in turn, treat Tokopedia and GoTo as one company, use growth divergence in points as Chapter 3 defines it, narrow the test to the three marketplaces, and repeat it with quarterly pairs.

The second objective asks where large movements in revenue came from, and the thesis answers in two steps. The first divides each movement into volume and take rate. In log terms, revenue growth equals transaction value growth plus the change in the take rate. The take-rate share is the size of the take-rate change divided by the sum of the sizes of both changes. The same split is made for the wedge, which equals transaction value minus revenue. The second step finds the cause of a take-rate change. A platform's take rate equals the rate of its gross fees minus the rate of its incentives, each measured against transaction value. So a rise comes from higher fees, lower incentives or a change in the mix of businesses. Wherever a company discloses both, the thesis splits the growth of revenue over a window into three parts. They are more commerce, a change in the fee rate and a change in the incentive rate.

The sources differ by company. Tokopedia's audited segment note gives gross revenue, incentives and net revenue, and the thesis checks them against the audited consolidated statements. For Tokopedia it also reports the change line by line in rupiah, which is the usual way to read accounts, and it says where the two views differ. Grab is read from its annual filings and GoTo from its audited statements. Blibli does not report incentives, so its split rests on a proxy built from its releases. Seven windows are traced, and Appendix A lists them. The thesis also records where accounting treatment or reporting scope matters, such as the deduction of incentives from revenue and the travel business inside Blibli's retail segment. Company explanations are read as reports and are not tested.

## 4.3 Measuring the wedge in Indonesia

The first objective needs a different set of amounts. It sums the transaction value and revenue of three major platforms in Indonesia in 2023: Tokopedia, Shopee and Grab. Not every company reports Indonesia on its own. Tokopedia reports both amounts for its segment. Shopee's transaction value is an outside estimate by Momentum Works. Its revenue assumes a take rate of 10 percent, which the thesis varies from 9 to 11 percent. Grab reports its Indonesian revenue, and the thesis derives its Indonesian transaction value from Grab's company-wide ratio of the two amounts. The wedge and the ecosystem ratio are then computed from the sums. The thesis drops each platform in turn, and it repeats the exercise for every platform-year between 2020 and 2025 that the filings allow.

## 4.4 Evidence from the sellers

The national evidence comes from the survey of online sellers that BPS runs. BPS publishes the number of businesses selling online, their total online sales and the shares by channel (BPS 2025). The survey rounds are named for the survey year, but their questions refer to the year before. The thesis names a file by its round and a year by the year of activity, so the file for the 2024 round describes 2023.

H2 uses the published figures. National online sales value equals the number of businesses times the sales per business. In log terms, growth in value is growth in the number of businesses plus growth in sales per business. H2 holds if the first part is more than half of the total. BPS prints two counts of businesses for 2023, so the thesis computes the split with both and reports both.

The published figures cannot tell a new seller from one counted for the first time, but the survey files can. BPS sold them under a data-use agreement, and Table 4.2 lists them. Each row is a business that sold online in the activity year. Its survey weight shows how many businesses it represents, so the weights add up to the national count. Two checks come before any test. The weighted total of each file must fall within 1 percent of the BPS count. The 2024 file must also reproduce two published shares of sellers who keep complete financial statements, 28.63 and 12.25 percent. All three files pass. The files carry no business identifier across rounds and no area variable below the province. So the rounds compare groups of sellers and not the same sellers over time.

**Table 4.2. The three BPS survey files**

| Survey round | Activity year | Rows | Weighted total | BPS count |
|---|---|---|---|---|
| E-Commerce 2021 | 2020 | 11,848 | 2,361,423 | 2,361,423 |
| E-Commerce 2023 | 2022 | 31,724 | 2,995,986 | 2,995,879* |
| E-Commerce 2024 | 2023 | 39,736 | 3,814,799 | 3,816,750 |

*Implied by the published count for 2023 and its published growth of 27.4 percent.

The entry test follows the rule in Chapter 3. In the 2024 file, the weighted share of businesses that began selling online in 2023 must be at least 21.5 percent. That is 27.4 divided by 127.4, from the published rise of 27.4 percent. If the weights had matched BPS's other count for 2023, the threshold would have been 23.9 percent, but they did not. The test was written down and dated in the project's code archive, called the repository, before the files were opened.

If the test fails, a second question follows: how much of the rise does first-time entry not explain? A cohort is the group of sellers that began selling online by a given year. If two surveys count the same population, a cohort can only shrink between them, because sellers stop and no new seller can join it. The thesis compares the 2023 survey's count of sellers who began before 2023 with the whole 2022 count. It does so twice. The first time it assumes that no seller stopped. The second time it assumes that sellers stopped at about 5 percent a year, the rate at which one cohort shrank between the 2020 and 2022 surveys.

Further checks ask where the extra sellers sit. They look across the 34 provinces, across channels, at sellers' own reports of their sales and at the sampling error that BPS publishes. They also profile who the extra sellers are, look at part-year selling, and test a scenario of returners. The cohort check and these further checks were designed after the entry test failed, so Chapter 5 labels them exploratory. The exception is the median change in sellers' sales, which was registered. A seller who stopped and returned keeps an old start year, so the files cannot rule out returners.

Three further analyses use the same files. The first asks which channels sellers use and how sales divide between them. The published tables split the 2023 to 2024 rise in value between marketplaces and other channels, and BPS counts food and ride apps in its marketplace category. Value by channel rests on revenue brackets, which only the 2021 and 2023 files give. The thesis assigns each bracket a low, a middle and a high amount. The amounts were fixed before the file was opened. A validation rule applies: the middle scenario's 2022 total must lie between half and double BPS's published total of about US$53 billion. The 2023 questionnaire asks for monthly revenue but the bracket limits are annual size classes, so both readings are computed and the one that passes is kept. If the lower brackets alone already exceed the total, value shares are reported as ranges.

The second analysis asks whether a seller keeps complete financial statements. This bears on what platform records can add, because a seller with no statements leaves fewer formal records. The third builds on the first two and is developed in Chapter 6. It counts the marketplace sellers whose revenue is above a bracket line and expresses the count as a share of all online sellers. At the 2022 rate, BPS's brackets divide at about US$20,000 a year. The marketplace tax exempts individual sellers up to about US$34,000. So the count above BPS's line is an upper limit on the sellers the tax can reach. World Bank Enterprise Surveys add a check on records. They cover unregistered firms in six Indonesian cities in 2023, and formal firms with five or more employees in seven countries.

## 4.5 Bringing the two sides together

The third objective compares the platform evidence with national and payment figures. Table 4.3 lists the sources and what each one counts. The sources differ in what they cover, so the comparison follows three rules. It compares growth rates across sources and keeps each source in its own unit. It compares levels only after reconciling the definitions. And it compares sources most closely where their coverage overlaps. The 2023 file lets the thesis separate the part of BPS's marketplace sales that went to final consumers. It compares that part with Bank Indonesia's figure for the same year, in a test written down before the file was opened. The thesis also sets quarterly platform growth beside quarterly household spending growth. It treats payment figures as context, because they show how people pay and not what they buy online.

**Table 4.3. Sources compared in Objective 3**

| Source | What it covers | How it counts |
|---|---|---|
| Platform reports | Everything bought through one platform | The platform's own records |
| BPS online-seller survey | Every business that sold online, including chat and social media | Listing in sampled areas, scaled up by survey weights |
| Bank Indonesia e-commerce statistics | Transactions of large e-commerce firms (Bank Indonesia 2025) | Data sent to the central bank; the method is not public |
| Industry estimates | Shopping marketplaces in Indonesia or Southeast Asia, from the research firm Momentum Works (2024) and the e-Conomy report (Google, Temasek and Bain 2024) | Outside estimates |
| Household spending | All household purchases | BPS national accounts |
| Payment figures | Payments made through systems such as QRIS, the national QR-code system | Payment records, in person and online |

One last analysis asks whether markets value a platform's growth in transaction value differently from growth in its take rate. The data are year-end market values from the financial data service LSEG, under the university licence. The main sample has 28 listed platforms and 138 platform-years, made up of Bukalapak and 27 platforms abroad, and it uses whole-company figures only. A regression relates the yearly change in log market value to the changes in log transaction value and log take rate. It adds a fixed effect for each year and clusters standard errors by company. Each prediction names a direction, so both tests are one-sided. The result is an association, and market value also changes when a company issues shares, so the thesis does not call it a stock return. A second run adds segment series and three more whole companies as a robustness check. The test was written down before the market values were pulled.

## 4.6 Labels, traceability and licensed data

Every number in the thesis follows one path: source document, extract, analytic row, result. Each extract keeps the company's currency and units, and each value carries a label: direct company disclosure, direct segment disclosure, external estimate, derived value, conversion or scenario. The labels are never mixed in one sample. A restatement or a conflict between two reports is reported and never overwritten. A single script rebuilds every table that depends only on committed files, and 272 automatic checks confirm that each recorded result still matches its table.

The thesis also separates tests by when they were written. A registered test was written down, dated and stored in the repository before the data were opened. This applies to the entry test, the scenario rules for value, the comparison with Bank Indonesia and the market-value test, among others. Appendix C lists them with their dates. An exploratory test was designed after some results were seen. The test with the larger groups in Section 4.2 belongs here, because it was set up after a first test on the three marketplaces. A descriptive result reports numbers without a test.

Three sources are licensed and are not in the repository: the BPS survey files, the LSEG market values and the World Bank survey files. The repository records the size and checksum of each file, so anyone who obtains the same files can check them. It holds the code that reads them and the national totals that the code produces, and no business-level record. BPS is cited as the source of every survey figure, in line with the data-use agreement. Chapter 7 states what these data cannot show.
