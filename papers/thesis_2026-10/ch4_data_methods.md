# Chapter 4. Data and Methods

The figures this thesis compares come from sources that were never designed to be read together. Platforms publish in their own formats, and the answers of individual sellers are released only under a data-use agreement. The methods in this chapter are built around these conditions.

On the platform side, the thesis reads revenue and transaction value from annual reports, audited statements and earnings releases. The extraction tables keep the source file and the quoted passage beside every value. The Indonesian platforms are three online marketplaces, Tokopedia, Bukalapak and Blibli, and GoTo, the group that runs the Gojek app for rides and deliveries. GoTo also controlled Tokopedia until 2024 and still holds a stake in it. Grab, a Singapore company that runs rides and deliveries across Southeast Asia, completes the group. Sea, also based in Singapore, owns the Shopee marketplace and is read with the foreign platforms (Section 4.1). Where a platform does not report Indonesia alone, as with Shopee and Grab, the thesis states what it derives or borrows and labels it.

The national side rests on BPS's survey of online sellers. BPS publishes a few totals, and the thesis obtained the answers behind them for three survey rounds, which show when each seller began selling online and how much it sold. The central bank's own figure has no published method, so it serves only as a point of comparison.

Setting the two sides against each other for one country is what makes the tests possible. Indonesia allows it. Five platform series report revenue and transaction value in the same year, and three of them report what they pay out in incentives. The survey asks every online seller when it began. The tests are built to ask only what these sources can answer, and each limit is stated where it applies.

The chapter describes the evidence on each side and the tests that use it, platforms first (Sections 4.1 to 4.5) and then the survey (Sections 4.6 to 4.8). It ends with the comparison of national figures and with how every number is labelled and traced (Sections 4.9 and 4.10).

## 4.1 The platform data

The basic observation is one platform in one year, which this thesis calls a platform-year. Revenue comes from the company's financial statements and transaction value from its annual report or earnings release. Both refer to the same year and, as closely as the filings allow, the same business.

Companies define transaction value in different ways, and some include shipping charges, digital goods or travel. The thesis keeps each company's own definition and records it. Under the second rule of Section 3.1, the definition cancels out of a take rate's yearly changes. This holds as long as the company keeps both the definition and the mix of its businesses.

Two groups of platforms are compared. The Indonesian and regional group has five platforms, listed in Appendix B. Three are Indonesian marketplaces, and two are the on-demand businesses of Grab and GoTo, which cover rides and deliveries. The foreign group has 27 listed platforms in marketplaces, travel and ticketing, freelance work, resale and food delivery. Eight were chosen first, and 19 were added to widen the comparison. Ten more were examined and left out, six because they sell mostly their own goods and four because they do not disclose transaction value.

Appendix B states the scope of each series because the series differ, and only Tokopedia is an Indonesian segment alone. The thesis never adds the series together, and each platform enters the tests on its own. Sea, whose Shopee business has Indonesia as a main market, sits in the foreign group.

Platform-years are compared in pairs, and three rules keep the pairs comparable. Two consecutive platform-years form a pair, and nothing else does. A missing year stays missing and is never filled in. Annual and quarterly pairs are never pooled. A take rate is a ratio of two amounts in one currency, so the tests need no exchange rate. Amounts in running text are in US dollars at the World Bank's average rate for the year (World Bank 2026).

The third rule of Section 3.1, which keeps out companies that mainly sell their own goods, is applied in two ways. For the 19 platforms added, the thesis drops any year in which own goods exceed half of revenue. For the eight chosen first, it keeps a pair only when the company's reporting scope did not change between the two years.

Two platforms sit close to that line. Zalando is one of the eight and sells part of what it carries, so Appendix C repeats the test without it. One added pair, Ozon from 2021 to 2022, ends in a kept year but starts in a dropped one. Appendix C repeats the test without Ozon as well. The result is 15 pairs for the Indonesian and regional group and 158 for the foreign group.

## 4.2 Measuring the wedge in Indonesia

The first objective, the size of the invisible wedge, needs amounts for Indonesia alone. The thesis sums the transaction value and revenue of three major platforms in Indonesia in 2023: Tokopedia, Shopee and Grab. The wedge and the ecosystem ratio are then computed from the sums.

Each platform reaches the sum by its own route. Tokopedia reports both amounts for its segment. Shopee's transaction value is an outside estimate by Momentum Works, a research firm that tracks online commerce in Southeast Asia. Its revenue assumes a take rate of 10 percent, which the thesis varies from 9 to 11 percent. Grab reports its Indonesian revenue, and the thesis derives its Indonesian transaction value from Grab's company-wide ratio of the two amounts. The thesis drops each platform in turn, and it repeats the exercise for every platform-year between 2020 and 2025 that the filings allow.

## 4.3 Testing H1

The test of H1 has two parts, run on the same 32 platforms: the five Indonesian and regional platforms, Tokopedia, Blibli, Bukalapak and the on-demand businesses of Grab and GoTo, and the 27 platforms abroad.

The first part is equation (6). Each observation is a pair of consecutive years of one platform, and a missing year is never filled. Growth is the simple percentage change, and growth rates are capped at their 5th and 95th percentiles (Section 4.4). The regression runs on all platforms with the group interaction, on the foreign group alone and on the Indonesian and regional group alone, with standard errors clustered by platform. The thesis also reports the correlation between revenue growth and transaction value growth for each group. Appendix C gives the rank correlation and the correlation without caps.

The second part asks how far each platform's take rate moves from one year to the next. For each pair of years it takes the simple percentage change in the take rate. Tokopedia's change in 2023 is 68 percent. A move in either direction counts against H1, so the test uses the size of each yearly change. Each platform gets one number, the median size of its yearly changes, because the pairs of one platform are not independent of one another.

The test compares five numbers for the Indonesian and regional group with 27 for the foreign group. It asks whether the first group ranks higher than chance would give, using a one-sided Mann–Whitney test (Mann and Whitney 1947). It repeats the question by shuffling the group labels 9,999 times. The p-value is the chance of a result at least this lopsided if the groups did not differ.

Appendix C lists the checks on this test. Some change the sample. They drop each platform in turn, drop two at a time, treat Tokopedia and GoTo as one company, move Sea to the regional group, keep only the first five years after listing, or narrow the test to the three marketplaces. Others change the measure: the change in logs, which the first version of this test used, growth divergence in points as Chapter 3 defines it, exact tests, and the change in the take rate in percentage points, to see whether a thin take rate explains the result. One repeats the test with quarterly pairs.

## 4.4 What explains the wedge and the ecosystem ratio

Equation (7) is estimated on a panel of 213 platform-years for the same 32 platforms, 20 of them Indonesian and regional platform-years and 193 foreign. A platform-year enters when the company reports both transaction value and revenue for it under the rules of Section 3.1, and a year that fails them stays missing. Amounts are in US dollars at the World Bank's period-average rate for the year (World Bank 2026).

Size is the platform's total assets, taken from annual reports filed with the US Securities and Exchange Commission for 26 platforms (U.S. Securities and Exchange Commission 2026) and from published financial statements for the other six: Tokopedia and GoTo, which share one group statement, Blibli, Bukalapak, Rakuten and Zalando. Total assets are those of the company as a whole. They overstate the platform business at GoTo, Rakuten and Sea. The number of years since listing counts from the year the platform listed on a stock exchange, from public record, and a year before listing counts as zero. The type of platform is the author's classification (Appendix B).

The home market is the country of the platform's main market. It is the United States for most US-listed platforms and Indonesia for the five Indonesian and regional platforms. It is also Indonesia for Sea, whose Shopee business has Indonesia as a main market. GDP growth, inflation and growth in household spending come from the World Bank (2026). The policy rate is the central bank's rate from the Bank for International Settlements (2026), averaged over the year. It is not available for Kazakhstan or Nigeria, so the regressions with macroeconomic variables have 178 platform-years from 30 platforms.

Growth rates and the ecosystem ratio are capped at their 5th and 95th percentiles across all platforms, the rule that Section 4.5 uses for market value. Standard errors are clustered by platform, with the small-sample correction, and p-values use a t distribution with one fewer degrees of freedom than platforms. Only five platforms are Indonesian and regional, so the thesis adds a wild cluster bootstrap p-value for the Indonesia coefficient (Cameron, Gelbach and Miller 2008). Appendix C lists the checks on this coefficient. All of these tests are exploratory, because they were designed after the data were seen.

The second objective, to reconcile large movements in revenue with disclosed changes in fees, discounts and scope, rests on company reports. Where a company discloses both its gross fees and its incentives, the thesis splits the growth of revenue over a window into more commerce, a change in the fee rate and a change in the incentive rate (equation (5)). The split is exact only in logs, so Appendix B keeps the log definition for these windows. A change in the mix of businesses is recorded from the company's reports.

The sources differ by company. Tokopedia's audited segment note gives gross revenue, incentives and net revenue, and the thesis checks them against the audited consolidated statements. For Tokopedia the thesis also reports the change line by line in rupiah, the usual way to read accounts, and says where the two views differ. Grab is read from its annual filings and GoTo from its audited statements. Blibli does not report incentives, so its split rests on a proxy built from its releases. Seven windows are traced, and Appendix B lists them. The thesis also records where accounting treatment or reporting scope matters, such as the deduction of incentives from revenue and the travel business inside Blibli's retail segment. Company explanations are read as reports and are not tested.

## 4.5 Market values

The market-value analysis of Section 3.6 uses year-end market values from the data service of the London Stock Exchange Group (LSEG), under the university licence. The main sample has 28 listed platforms and 138 platform-years, made up of Bukalapak and 27 platforms abroad, and it uses whole-company figures only. It is not the list of 27 used for H1. It adds Airbnb, Booking, DoorDash, Lyft and Uber, and it lacks Despegar, Mercado Libre, Ozon, Rakuten and Sea.

Equation (9) is estimated with a fixed effect for each year, which removes what all platforms share in that year. Standard errors are clustered by company, which allows for the repeated observations of one company. Each prediction names a direction, so both tests are one-sided. The test was written down before the market values were pulled, with changes measured in logs, and it keeps that definition. The result is an association, and market value also changes when a company issues shares, so the thesis does not call it a stock return. A second run adds five segment series and Mercado Libre as a robustness check. Grab, GoTo and Sea enter only there, because their reported transaction value covers only part of the business that the market value prices.

## 4.6 The survey files and H2

The national evidence comes from the survey of online sellers that BPS runs. BPS publishes the number of businesses selling online, their total online sales and the shares by channel (BPS 2025a, 2025b). The survey rounds are named for the survey year, but their questions refer to the year before. The thesis names a file by its round and a year by the year of activity, so the file for the 2024 round describes 2023. Each round lists businesses in sampled areas and updates its sampling frame, so a change in who is found can change the count.

H2 uses the published figures and the split of equation (8). BPS prints two counts of businesses for 2023, so the thesis computes the 2023 to 2024 split with both and reports both. The 2022 to 2023 split uses the count that the survey weights match.

The published figures cannot tell a new seller from one counted for the first time, but the survey files can. The three files are the E-Commerce rounds of 2021, 2023 and 2024, which describe the activity years 2020, 2022 and 2023.[^files] Each row is a business that sold online in the activity year. Its survey weight shows how many businesses it represents, so the weights add up to the national count.

Two checks come before any test. The weighted total of each file must fall within 1 percent of the BPS count. The 2024 file must also reproduce two published shares of sellers who keep complete financial statements, 28.63 and 12.25 percent. All three files pass. The files carry no business identifier across rounds and no area variable below the province. So the rounds compare groups of sellers and not the same sellers over time.

[^files]: The files hold 11,848, 31,724 and 39,736 rows. Each weighted total is within 0.1 percent of the BPS count: 2,361,423; 2,995,879, implied by the 2023 count and its growth of 27.4 percent; and 3,816,750.

## 4.7 The entry test and the extra sellers

The entry test asks whether at least 21.5 percent of the 2023 sellers in the 2024 file began selling online in 2023, a threshold that Chapter 3 derives. BPS also prints a second count for 2023, but the survey weights match the first, so the threshold stays at 21.5 percent. The test was written down and dated in the project's code archive, called the repository, before the files were opened.

A failed entry test raises a second question: how much of the rise does first-time entry not explain? The sellers behind that part are called the extra sellers. A cohort is the group of sellers that began selling online by a given year. If two surveys count the same population, a cohort can only shrink between them, because sellers stop and no new seller can join it.

The cohort check compares the 2024 file's count of sellers who began before 2023 with the whole 2022 count. It does so twice. The first time it assumes that no seller stopped. The second time it assumes that sellers stopped at about 5 percent a year, the rate at which one cohort shrank between the 2020 and 2022 surveys.

Further checks ask where the extra sellers sit and who they are. They compare provinces and channels using rank correlations, look at sellers' own reports of their sales, and use the sampling error that BPS publishes. They compare each group's count in 2023 with what its own yearly change in 2020 to 2022 would give. They also look at part-year selling and test a scenario of returners.

The cohort check and the further checks were designed after the entry test failed, so Chapter 5 labels them exploratory. The exception is the median change in sellers' sales, which was registered. The files cannot rule out returners, because a seller who stopped and returned keeps an old start year.

## 4.8 Channels, records and reach

Three analyses beyond the entry test also use the survey files. One asks which channels sellers use and how sales divide between them. The published tables split the 2023 to 2024 rise in value between marketplaces and other channels, and BPS counts food and ride apps in its marketplace category.

Value by channel needs revenue brackets, and only the 2021 and 2023 files have them. The thesis gives each bracket a low, a middle and a high amount, fixed before the file was opened. A check follows: the middle scenario's 2022 total must fall between half and double BPS's published total of about US$53 billion.

The 2023 questionnaire asks for monthly revenue but the bracket limits are annual size classes, so both readings are computed and the one that passes is kept. If the lower brackets alone already exceed the total, value shares are reported as ranges.

Whether a seller keeps complete financial statements is the subject of a second analysis. It bears on what platform records can add, because a seller with no statements leaves fewer formal records. World Bank Enterprise Surveys add a check on records. They cover unregistered firms in six Indonesian cities in 2023, and formal firms with five or more employees in seven countries.

A third analysis builds on the first two and is developed in Chapter 6. It counts the marketplace sellers whose revenue is above a bracket line and expresses the count as a share of all online sellers. At the 2022 rate, BPS's brackets divide at about US$20,000 a year. The marketplace tax exempts individual sellers up to about US$34,000. So the count above BPS's line is an upper limit on the sellers the tax can reach.

Chapter 6 also sets each recent rule against the part of the figures it acts on. The thesis reads each legal text where it is published. It labels each rule by the status of its text: primary text read, announced, or reported in the news only.

## 4.9 Comparing national figures

The third objective, to compare the platform evidence with national and payment figures, rests on the sources that Appendix A lists, with what each one counts. Beyond the rules of Section 3.1, the comparison is closest where the coverage of two sources overlaps. Payment figures serve as context, because they show how people pay and not what they buy online.

The 2023 file, which describes 2022, lets the thesis separate the part of BPS's marketplace sales that went to final consumers. It compares that part with Bank Indonesia's figure for the same year, in a test written down before the file was opened. The thesis sets the 2023 growth of six measures of buying through platforms beside household spending, each in its own unit. It does the same with quarterly platform growth.

## 4.10 Labels, traceability and licensed data

Every number in the thesis follows one path: source document, extract, analytic row, result. Each extract keeps the company's currency and units, and each value carries a label: direct company disclosure, direct segment disclosure, external estimate, derived value, conversion or scenario. The labels are never mixed in one sample. A restatement or a conflict between two reports is reported and never overwritten. A single script rebuilds every table that depends only on committed files, and 314 automatic checks confirm that each recorded result still matches its table.

The thesis also separates tests by when they were written. A registered test was written down, dated and stored in the repository before the data were opened. This applies to the entry test, the scenario rules for value, the comparison with Bank Indonesia and the market-value test, among others. Appendix D lists them with their dates. An exploratory test was designed after some results were seen. The test with the larger groups in Section 4.3 belongs here, because it was set up after a first test on the three marketplaces. A descriptive result reports numbers without a test.

The World Bank indicators, the Bank for International Settlements policy rates and the total assets from the filings with the US Securities and Exchange Commission are public. The repository holds the downloaded values and the scripts that fetched them. Three sources are licensed and are not in the repository: the BPS survey files, the LSEG market values and the World Bank survey files. The repository records the size and checksum of each file, so anyone who obtains the same files can check them. It holds the code and the national totals it produces, and no business-level record. BPS is cited as the source of every survey figure, in line with the data-use agreement. Chapter 7 states what these data cannot show.
