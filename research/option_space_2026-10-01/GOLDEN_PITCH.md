# The golden pitch (frozen 8 Oct 2026)

**Status: FROZEN** (git tag `golden-pitch-2026-10-08`). This is the bar for hook, tone and plainness. Every abstract, chapter opening, slide and summary is checked against it: if a passage reads more technical, more abstract or more polished than this, it is rewritten down to this level. Changes only as dated notes at the end.

## The pitch

> In 2023 Indonesia argued about whether online selling was growing so fast it was hurting market traders, and the government shut TikTok Shop. The official figures for that year later said online sales rose 41%. I looked inside the survey behind those figures. Most sellers said their sales were flat or down, and their main complaint was a lack of customers. About half the new sellers weren't new: they were older, long-running small businesses, selling through WhatsApp and social media, that were only counted that year. On the big platforms, revenue grew mostly because they charged more, not because people bought more.

## Why it works (what the rest of the writing must keep)

- It starts from a moment readers lived through, not from a concept.
- The researcher looks, in first person; the evidence is the sellers' own answers.
- Few numbers, rounded, each one doing a job.
- No flourish lines, no lists of what is not claimed, no terms that need a definition.
- Every sentence is backed by a result below.

## Evidence behind each sentence

| Sentence | Evidence |
|---|---|
| 2023 debate; TikTok Shop shut | Permendag 31/2023 signed 26 Sep 2023 (primary text, `../../sources/policy_primary/`); TikTok Shop closed 4 Oct 2023 (`tables/src/policy_timeline_web.csv`). **Open: one news citation for the market traders' complaints behind the rule.** |
| Official figures later said +41% | BPS e-commerce value 2023, +40.6% (FINDINGS, verdict for 2023), published in 2024, after the ban |
| Most sellers flat or down; main complaint lack of customers | 2023 activity (2024 file): 24% up, 44% same, 32% down; lack of demand the top obstacle, 41% (FINDINGS; `bps_microdata_tests.py`) |
| About half the new sellers weren't new | 37-56% of the 819 thousand rise not explained by first-time entry (`bps_rise_accounting.py`, Part 4) |
| Older, long-running, WhatsApp and social media, only counted that year | `bps_newly_counted_profile.py` (exploratory): business opened before 2010 41% of the excess vs 18% of the 2022 count; owner 50+ 41% vs 29%; almost all chat or social only. Wider coverage vs sellers returning after a break is not separated (Part 4) |
| Platforms charged more | Two thirds of each revenue change came from the take rate, vs a quarter abroad (`wedge_split.py`); H1 rejected (Part 3) |

## Wording fixed at freeze

- "had sold through WhatsApp for years" became "selling through WhatsApp and social media": the businesses are long-running, but much of the extra count started selling online in 2022 (`tables/bps_cohort_check.json`), and the channel data cover chat and social media, not WhatsApp alone.

## Dated notes

- **8 Oct 2026, open citation closed.** Market traders' complaints behind the rule: AFP, "'Regulate them': hard-up Indonesia traders urge TikTok sales ban", 25 Sep 2023 (Tanah Abang sellers blame TikTok Shop prices for falling sales and ask for it to be closed or regulated; https://techxplore.com/news/2023-09-hard-up-indonesia-traders-urge-tiktok.html); ANTARA, "Minister visits Tanah Abang Market following social commerce ban", 28 Sep 2023 (traders say income fell because they cannot compete with social-commerce sellers; the minister: transactions not allowed on social media; https://en.antaranews.com/news/294768/minister-visits-tanah-abang-market-following-social-commerce-ban). Both describe the complaints; neither measures market-wide sales, and the pitch does not claim they do.
- **8 Oct 2026, general frame around the pitch (not part of the frozen pitch).** One paragraph before it (most of what we know about the digital economy comes from what platforms report and from surveys of sellers; Indonesia 2023 shows both shifting at once) and one after it (governments now see online sellers through the platforms: OECD model rules 2020, goods module 2021; EU DAC7 reporting from 2023; Philippines withholding from early 2024; Viet Nam from July 2025; Indonesia due November 2026; a platform rule reaches platform sellers, fewer than one in five of Indonesia's online sellers). Rules checked in `tables/src/platform_seller_rules_intl.csv` (secondary sources where official sites block scripts).
