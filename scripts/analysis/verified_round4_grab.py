#!/usr/bin/env python3
"""Round 4: Grab's 2022-2023 gap.

Terminology note, checked rather than assumed: 2022-2023 releases say "Total
GMV," while 2024+ releases say "On-Demand GMV." The Q1 2023 release itself
states On-Demand GMV "is the sum of Mobility and Deliveries GMV" -- so this
looks like a label change, not a scope change (Financial Services GMV was
never included either way), but that is inferred from one release's wording,
not independently confirmed across all of them. Flagged as an open question,
not asserted as settled.

Cross-check: Grab's FY2022 revenue here ($1,433M) matches round-1's SEC XBRL
figure for 2022FY exactly -- same number from two unrelated sources (XBRL vs
press release), which is the kind of agreement that makes both more credible.
"""

ROWS = [
    dict(firm="GRAB", fq="2022Q1", date="2022-05-19", gmv_usd_m=4800, rev_usd_m=228,
         guidance="", other="GMV +32% YoY, Revenue +6% YoY",
         url="https://investors.grab.com/news-and-events/news-details/2022/Grab-Reports-First-Quarter-2022-Results/default.aspx",
         note="Release terms this 'Total GMV,' not 'On-Demand GMV' (later terminology)"),
    dict(firm="GRAB", fq="2022Q2", date="2022-08-15", gmv_usd_m=5100, rev_usd_m=321,
         guidance="", other="Record quarterly revenue at the time; GMV +30% YoY",
         url="https://investors.grab.com/news-and-events/news-details/2022/Grab-Reports-Second-Quarter-2022-Results/default.aspx",
         note="'Total GMV' terminology"),
    dict(firm="GRAB", fq="2022Q3", date="2022-11-16", gmv_usd_m=5100, rev_usd_m=382,
         guidance="", other="Record quarterly revenue at the time; GMV +26% YoY",
         url="https://www.businesswire.com/news/home/20221116005478/en/Grab-Reports-Third-Quarter-2022-Results",
         note="'Total GMV' terminology"),
    dict(firm="GRAB", fq="2022Q4", date="2023-02-23", gmv_usd_m=5000, rev_usd_m=502,
         guidance="Y — brought forward Group Adj. EBITDA breakeven guidance to 4Q23 from 2H24",
         other="Revenue +310% YoY (comping a low prior-year base); FY22 GMV $19.9B (+24% YoY), "
               "FY22 revenue $1,433M -- matches round-1 SEC XBRL figure for 2022FY exactly, "
               "cross-validating both sources",
         url="https://www.businesswire.com/news/home/20230223005467/en/Grab-Reports-Fourth-Quarter-and-Full-Year-2022-Results",
         note="'Total GMV' terminology"),
    dict(firm="GRAB", fq="2023Q1", date="2023-05-18", gmv_usd_m=4958, rev_usd_m=525,
         guidance="", other="GMV +3% YoY (+7% constant currency, softer Deliveries demand from CNY/Ramadan timing); "
               "MTUs 33.3M (+8% YoY)",
         url="https://www.grab.com/sg/press/others/grab-reports-first-quarter-2023-results/"),
    dict(firm="GRAB", fq="2023Q3", date="2023-11-09", gmv_usd_m=5341, rev_usd_m=615,
         guidance="", other="GMV +5% YoY (+6% constant currency); MTUs +7% YoY",
         url="https://www.businesswire.com/news/home/20231109083952/en/Grab-Reports-Third-Quarter-2023-Results"),
    dict(firm="GRAB", fq="2023Q4", date="2024-02-22", gmv_usd_m=None, rev_usd_m=653,
         guidance="Y — first-ever $500M share repurchase program announced",
         other="GMV +9% YoY (absolute not found in available sources; Deliveries GMV specifically "
               "was $2,648M, +13% YoY). Repaid outstanding Term Loan B balance. "
               "FY23 GMV $20,983M (disclosed directly, +5% YoY / +7% constant currency)",
         url="https://investors.grab.com/news-and-events/news-details/2024/Grab-Reports-Fourth-Quarter-and-Full-Year-2023-Results-and-Announces-Inaugural-Share-Repurchase-Program-of-Up-to-500-Million/default.aspx",
         note="Total GMV absolute not directly found for this quarter -- left blank rather than "
              "estimated from the YoY %, per the handoff's own rule against filling cells with estimates"),
]
