# The narrative arc (frozen 9 Oct 2026)

**Status: FROZEN** (git tag `narrative-arc-2026-10-09`). The order and the job of each part of the thesis story: wide (A), into Indonesia (A-B), the evidence (B), what travels (B-C), wide again (C). Voice and tone follow `GOLDEN_PITCH.md`. Wording here is working text, not final prose; the order, the jobs and the claims are what is frozen. Changes only as dated notes at the end.

Why this shape: the proposal's own problem is that different users read different numbers and reach opposite conclusions about the same activity (investors on platform revenue, statistics agencies on national figures, tax authorities on marketplace records). The arc opens on that problem, tests each user's number in Indonesia, and closes by answering each user. No new hypothesis; the entry test (registered 2 Oct before the survey files were opened, coded E5) closes a limit the proposal itself named ("does not by itself establish causal business entry").

## A. The global problem

Everywhere, people judge the online economy through a few numbers: what platforms report about themselves, surveys of the people selling, and the records platforms keep for the tax office. Investors, statistics offices and tax authorities all lean on them. None measures the activity directly; each is a stand-in.

More decisions now rest on these stand-ins. Investors value platforms on them, and governments are starting to track and tax online sellers through the platforms: the OECD's model rules, the EU since 2023, the Philippines since 2024, Viet Nam since 2025 (`tables/src/platform_seller_rules_intl.csv`). The stand-ins can tell opposite stories about the same year.

## A-B. Into Indonesia

To see whether these numbers can be trusted, you need a place where they are likely to break and where you can check them against something underneath. Indonesia is that place. Its platforms keep a very thin slice of each sale, so ordinary price changes swing their income hard. Most of its online sellers do not use marketplaces; they sell through chat apps and social media. In 2023 it had a public argument about online growth, which ended with TikTok Shop being shut.

Indonesia also lets us look underneath. The platforms report both what passes through them and what they keep, and BPS asks sellers directly how their year went and when they started selling. So each number can be checked against the activity it stands for: platform revenue (H1), the national seller count (H2), and the marketplace records the tax office will use.

The proposal expected national growth to come from new sellers outside the platforms, which platform figures would miss.

## B. The evidence (Indonesia)

- **B1. The year in question.** In 2023 platform revenue grew fast, and BPS later reported a jump in online sales and sellers, while market traders complained and TikTok Shop was shut. What were the rising numbers measuring?
- **B2. How thin the platforms' slice is.** A platform keeps about 7 rupiah in every 100 that pass through it: the invisible wedge is the rest. With a slice that thin, a small change in what it keeps makes its income jump with no extra buying.
- **B3. H1: did platform income follow buying?** No (H1 rejected). Indonesian platforms changed their slice far more than platforms abroad, by cutting discounts and raising fees, mostly in 2022-24. Income climbed while buying through the apps stalled; in 2023 several measures of it fell. Market value followed buying.
- **B4. The obvious answer: the boom moved off the apps.** Most sellers sell through chat and social media; if growth was out of the apps' sight, it would be there.
- **B5. What sellers said.** Most said their online sales were flat or down; the most common complaint was a lack of customers.
- **B6. H2: where did official growth come from?** More sellers, on the published numbers (H2 holds). The proposal read that as new businesses off the platforms, and named the limit: the published numbers cannot tell new sellers from newly counted ones.
- **B7. The entry test.** Written before the survey answers were opened: if the extra sellers are new, enough will say they started that year. Not enough did. About half the jump were sellers already in business who were not in the previous count. Too large to be chance; concentrated where the survey grew; the next year looks normal. Open alternative: sellers who paused and came back.
- **B8. Who they are (exploratory).** Long-running small businesses, older owners, often outside Java, often food or small manufacturing, selling only through chat and social media. There all along; counted in 2023.
- **B9. Why the two state offices disagreed.** On the marketplaces they agree growth was slow; they split outside them, where BPS looks and Bank Indonesia's figure does not, and where BPS had just started seeing more sellers.
- **B10. The tax office's number.** The marketplace tax collects from roughly 1 in 20 online sellers and puts every marketplace seller on record, fewer than one in five of all sellers. The chat sellers of B8 sit outside it; the 2026 census will reach further into the same group.
- **B11. What 2023 was.** Every number read as "booming" measured something narrower: platform income measured prices, the seller count partly measured counting, the tax records cover a minority. The sellers said it was a hard year, and the evidence backs them.

## B-C. What travels

Some of this is Indonesian. The thin slice is: Indonesia's marketplaces keep far less of each sale than most platforms abroad, so ordinary price changes swing their revenue hard; the follow-up tests show not every platform's revenue swings like this. The survey finding is: one country's survey, one year.

What travels is the check. A platform's revenue tracks buying only while its prices hold, and across listed platforms in several countries market value followed buying. A count of online sellers tracks new businesses only while the survey keeps reaching the same people, and one question about the year a seller started tests it. A rule built on platform records reaches only the sellers on the platforms, and several countries are now building such rules.

## C. Back to everyone

- **Investors:** ask whether platform growth came from more buying or from charging more.
- **Statistics offices:** when a count of online sellers jumps, ask whether the sellers are new. Where selling runs through chat apps, a survey can find people who were always there, and the people missed tend to be older owners of long-running small businesses.
- **Tax authorities:** before building on platform records, ask how many sellers work outside the platforms. In Indonesia it is most of them.
- **Closing:** the numbers we use to see the digital economy are stand-ins that hold only while prices and counting stay the same. Indonesia in 2023 shows both shifting at once: a year every number read as a boom, while the people selling said it was hard.

## Anchor numbers kept up front

41% (BPS's 2023 online sales growth), 7 in 100 (the platforms' slice), about half (the 2023 seller jump not explained by first-time entry), 1 in 20 (marketplace tax reach). Everything else stays in the evidence underneath (FINDINGS.md, Parts 3-6).

## Dated notes

- **9 Oct 2026, two layers.** The arc is the narrative layer (the order in which the reader understands the thesis); the chapters are the written layer (the containers a thesis is expected to have). They do not map one to one. The full arc appears compressed in the abstract, the end of chapter 1 and the conclusion; elsewhere its parts are spread across chapters, with chapter openings and closings carrying the thread. Rule: write in chapters, read in arc; a section that cannot say which arc part it serves goes to the appendix. The defence slides can follow the arc directly.
- **9 Oct 2026, B3 corrected (`h1_points_vs_log.py`, exploratory).** In points of transaction value, Indonesian platforms changed the share they keep by about as much as platforms abroad (median about 1 point a year in both; p = 0.65); the threefold difference is relative (p = 0.003) and comes from a much thinner slice (median 1.6% of transaction value vs 16.9%). B3 now reads: same-size price changes on a far thinner slice. This gives the wedge its job in the story: the larger the wedge next to revenue, the more an ordinary price change swings revenue growth (D = change in m / m). A-B and B-C wording changed to match; the golden pitch is unaffected.
