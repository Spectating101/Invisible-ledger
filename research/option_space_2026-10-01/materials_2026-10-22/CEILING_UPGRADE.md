# Ceiling upgrade: what was done, what is prepared, what is left (22 October 2026)

Scope rule kept: nothing here adds a dataset or a hypothesis. Every item deepens a test the thesis already has. Everything is exploratory (designed after the registered results were known), and the registration record says so (`PREREGISTRATION.md`, addendum of 22 Oct).

## 1. Done in the cloud session (committed tables only)

| Item | Script | Result | In the thesis |
|---|---|---|---|
| H1 exact inference over all 201,376 splits | `h1_exact_inference.py` | exact Mann-Whitney p = 0.0038, exact permutation p = 0.0214. The approximations in Table 5.3 (0.0038, 0.0221) were right | 5.2, Appendix B |
| Size of the H1 gap | same | typical gap 0.117 in |yearly change in log take rate| (exact 95% interval 0.039 to 0.223); ratio of medians 3.3 (bootstrap 1.4 to 8.5, loose with five platforms) | Appendix B |
| Sea in the regional group (6 against 26) | same | exact p = 0.0004 (stronger) | Appendix B |
| Drop any two of the five | same | exact p from 0.003 to 0.058. One case above 0.05: without Blibli and Tokopedia, the two largest movers | 5.2, 7.4, Appendix B |
| Young platforms only (first 5 years after listing) | same | 0.169 against 0.069, exact p = 0.059 (4 against 18 platforms) | 7.4, Appendix B |
| Power of the registered market-value test | `claims_ledger_v13.py` | standard error of b1 - b2 is 0.31, so the design flags only gaps above about 0.8. A failed M1 means "cannot tell" | 5.4 |
| Announcement returns on the committed panels | `event_study_panel_check.py` | nothing detectable (191 announcements). The revenue surprise itself is not detected (p = 0.20), so the sample cannot show whether the take-rate part is priced differently | registration record only; 7.5 keeps it as future work |
| Ledger | `claims_ledger_v13.py` | 42 claims, all PASS. It also covers the H2 coverage numbers that Table 5.1, 5.7, 7.1 and the abstract cite and no ledger had checked | |

Two of the H1 results weaken the claim (drop two, young platforms). They are in the thesis next to the ones that strengthen it. The honest reading: the H1 result is clear on the registered test and on exact inference, and it leans on the larger movers.

## 2. Tried and not useful

The announcement-return test (the proposal's Section 8 extension) cannot lift the ceiling with these platforms. Ten firms and 191 announcements give no detectable reaction to anything, including the revenue surprise. More work on this panel will not change that. The path to a real return test is more firms or more years, which the Indonesian platforms cannot supply. Keep it as future work and say why.

## 3. Prepared, needs your machine (licensed LSEG data)

`m1_upgrade.py` adds to the registered market-value test, on the same panel: wild cluster bootstrap p-values (28 clusters), leave-one-firm-out, an outcome net of share issuance, a levels version with firm and year effects, a segment treatment for Grab, GoTo and Sea, and the power note. It was tested on synthetic panels with known coefficients: size under the null 3.7% (M1) and 6.3% (M2) over 300 panels, 5.0% over 600 for M2, and the full pipeline builds the same 28-firm main panel as the registered test.

Run, from `research/option_space_2026-10-01/`:

```
python3 m1_upgrade.py <_local/licensed_data/lseg/mcap_reporting_ccy.csv> \
    --prices <year-end closing prices: firm,date,close> \
    --group-revenue <firm,year,group_revenue>
```

What you need to pull or compile (university licence; credentials and any payment are yours, not mine):
1. `--prices`: year-end closing prices adjusted for splits, same firms and years as the market values, columns `firm,date,close`, firm names exactly as in the market-value file. This gives the outcome net of share issuance.
2. `--group-revenue`: group revenue for Grab, GoTo and Sea for each year used, columns `firm,year,group_revenue`, in the same currency and unit as that firm's `R` in `tables/l_panel.csv` (Grab and GoTo) or the global matched annual file (Sea). The filings give it. Segments at least 70% of group revenue enter the main sample; the rest stay out.
3. Both options are optional. Without them the script still runs U1, U2, U4 and U6.

Bring back only `tables/m1_upgrade_results.json` (coefficients, counts, p-values; no market values). Do not commit the price or market-value files. I then add the numbers to the ledger and the thesis.

## 4. How the results go into the thesis (rules fixed before the run)

Fixed in `PREREGISTRATION.md` (22 Oct): the registered verdicts stand whatever the checks show; M2 is "robust" only if the wild-bootstrap p < 0.05, the worst leave-one-out p < 0.10 and the levels elasticity on volume is positive; M1 is "supported" only if its wild-bootstrap p < 0.05; the price-change outcome and the segment run are reported in full; no specification is added afterwards.

Text to use, by outcome. Numbers come from `m1_upgrade_results.json`.
- M2 passes every rule: "The result holds in small-sample checks: wild-bootstrap p = [x], at most [y] when any one firm is dropped, and the same sign in levels and in price changes."
- M2 fails a rule: "The result holds on the registered test but is sensitive to [the failing check]; Section 7.4 states this."
- M1 not supported (expected, given the power): leave as in 5.4, which already says the test could not tell.
- Price-change outcome disagrees with market-value change: say so plainly in 5.4 and in 7.4 (share issuance matters).

## 5. Where the ceiling stands after this

| Dimension | Before | Now | After the LSEG run |
|---|---|---|---|
| Rigour and integrity | 8.5 | 8.7 | 8.9 |
| Finance contribution | 5.5 | 6.0 | 6.5 to 7.0, depending on outcomes |
| Defensibility | 7.5 | 8.0 | 8.3 |
| Originality | 6 | 6 | 6 (capped) |

Why finance moves only a little: the market-value test is an association with 28 clusters and no stock-return layer, and the return test cannot be built (section 2). What the run can add is credible small-sample inference and an outcome net of issuance. That is worth running, but it will not turn the finance part into a strength. The thesis's strength is rigour and honesty. Do not try to oversell the finance link.

## 6. Defence answers

**What is new?** "I did not invent a method. I put two simple checks, one on platform accounts and one on a national survey, side by side for Indonesia, and tried to break my own results in many ways. One registered prediction failed, and that failure shows the survey's seller count moved for reasons other than first-time entry."

**Isn't this just brute force?** "The effort is large, but it serves a point: every number traces to a source and every failure is reported. The one clever piece is cheap. The entry test needs a single survey question and some arithmetic."

**Five platforms is small.** "Yes, and the thesis says so. Exact tests over every possible split give p = 0.004. Dropping any one platform keeps p at 0.016 or below. Dropping the two largest movers leaves p = 0.058, so the result leans on the larger movers. The ratio of medians is 3.3, but a bootstrap interval of 1.4 to 8.5 shows how loosely five platforms fix its size."

**Your market-value prediction failed. What did you learn?** "The data cannot separate how markets price the two sources of growth. The standard error of the gap is 0.31, so the design could flag only a gap above about 0.8. The volume coefficient of 0.6 is clear. A failed M1 means the test could not tell."

**Why no stock-return test?** "I tried the announcement-return version on 191 announcements. It could not detect any reaction, even to the revenue surprise itself. With ten firms that is a power limit, not a finding about markets, so I left it as future work."

**Is the 2022–24 result permanent?** "No. Quarterly pairs do not reject H1, and the thesis describes the rejection as a period, 2022 to 2024. Young platforms alone give p = 0.059, the same direction with less power."

**Is H2 right?** "H2 holds on BPS's published figures. If the unexplained 306 to 458 thousand sellers are wider survey coverage, with their sales removed too, more businesses account for about 42 to 54 percent of growth. That sits on the 50 percent line. This is exploratory."
