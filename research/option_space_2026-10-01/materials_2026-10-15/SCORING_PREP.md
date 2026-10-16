# Scoring the 2026 predictions: what to collect and where it goes (prepared 15 Oct 2026)

Predictions: `PREREGISTRATION.md` sections A and C and the 3 Oct addendum. Thesis home: Section 6.5 (Table 6.2 and the results slot) and Appendix C. Nothing below changes a registered range.

## 27 October 2026: GoTo 3Q26 release
Collect from GoTo's 3Q26 results presentation or financial statements (on-demand segment, IDR trillion):
- On-demand GTV, 3Q26
- On-demand net revenue, 3Q26
Run: `python3 score_q3_2026_goto_only.py GTV NET` (from `research/option_space_2026-10-01/`). Scores P1, P3, P5, R1.
Note: P5 has three outcomes as registered: confirmed at 5 percent or more, falsified below 2 percent, neither between 2 and 5. Table 6.2 should say so (pending fix).
Also note any management remarks on the 8% cap, incentives or "growth" in the call; quote with page or timestamp.

## Early November 2026: BPS 3Q26 GDP release
Collect: household plus NPISH final consumption (the series in `three_rulers.py`: BPS national accounts, also via OECD quarterly national accounts, not seasonally adjusted), nominal (current prices), year-on-year percent, 3Q26.
Run: `python3 score_q3_2026_goto_only.py GTV NET HH_YOY`. Scores R2.

## 1 November 2026: marketplace tax start
Registered expectation: the start slips again. Confirmed if DJP announces a postponement or collection does not begin on 1 November; falsified if collection starts on 1 November. Source: DJP announcement (pajak.go.id) and two news reports; record URL and date.

## Mid-November 2026: Grab and Sea 3Q26
Grab (US$ million, 3Q26): Mobility GMV and revenue; Deliveries GMV and revenue. Sea (US$ million): Shopee GMV and marketplace revenue (the series in `tables/shopee_quarterly_take_rate.csv`).
Fill the `IN` dictionary in `score_q3_2026.py` (registered file; only the inputs are filled) and run it. Scores P1 to P5 again (as a check on the GoTo-only run), P2, P4, R3.

## Next BPS e-commerce publication (reference year 2025)
Collect the marketplace share of e-commerce value (exclusive split, as the 15.79 percent for 2024). Registered: at or below 15.79 percent.

## Where each result goes
- Table 6.2, Outcome column: the value and CONFIRMED / FALSIFIED / NEITHER.
- Appendix C, row "P1 to P5, R1 to R3" and the tax and BPS-share row: outcome and date scored.
- Section 6.5 results slot: one paragraph on the cap (P1 to P5, R1), one on fees and the tax (R3, tax start), R2 in one sentence.
- Section 7.5 first step: change from "score" to what the scores showed.
- `EDIT_HISTORY.md`: one row per scoring date.
