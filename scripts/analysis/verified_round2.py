#!/usr/bin/env python3
"""Round 2 press-release pass -- GMV/GTV, revenue, net income, announcement
date, and concurrent events for Grab, GoTo, and Sea, direct from earnings
releases per the round-2 handoff instruction ("go straight to IR").

Every row was captured via WebSearch/WebFetch against the company's own
release (or, where noted, an SEC 6-K exhibit hosting the same release
verbatim), not derived or estimated. Figures reported only as YoY deltas
without an absolute in the source text are left blank rather than
back-calculated.

GoTo note (structural break, not just a concurrent event): Tokopedia was
deconsolidated to an associate-company basis effective 2024-02-01 following
the TikTok transaction. GTV/revenue from 2024Q1 onward is not on the same
consolidation basis as 2022-2023 -- flagged per-row, not silently blended.

Grab note: releases report "On-Demand GMV" (mobility segment only), not
total Group GTV (which also includes Deliveries and Financial Services).

Sea note: Shopee GMV and Shopee-segment revenue are reported separately from
Sea's consolidated total revenue (which also includes Garena and Monee).
Recorded here: Shopee GMV, and Sea's *consolidated* GAAP revenue (matches
what round 1 already populated for Q3 2025, for internal consistency).
"""

ROWS = [
    # --- GOTO (all IDR; no in-release USD conversion unless stated) ---
    dict(firm="GOTO", fq="2022Q3", date="2022-11-21", gtv_idr_t=161,
         rev_gross_idr_t=5.9, rev_net_idr_t=None,
         guidance="Y — revised FY22 GTV to Rp613-619T, gross revenue to Rp22.6-23.0T",
         other="On-Demand contribution margin turned positive in September; AA ESG rating (MSCI, provisional)",
         url="https://www.gotocompany.com/en/news/press/goto-reports-third-quarter-financial-results",
         note="Pre-Tokopedia-deconsolidation basis"),
    dict(firm="GOTO", fq="2022Q4", date="2023-03-20", gtv_idr_t=162,
         rev_gross_idr_t=6.3, rev_net_idr_t=None,
         guidance="Y — introduced FY23 Adj. EBITDA guidance Rp(5.3)-(4.6)T; no GTV/gross-rev guidance given for FY23",
         other="GoTo Logistics established as separate segment (Q1 2023); Pertamina EV partnership HoA; Mitsubishi EV pilot",
         url="https://www.gotocompany.com/en/news/press/goto-announces-fourth-straight-quarter-of-improving-adjusted-ebitda-as-it-reports-indicative-2022-fy-and-q4-results",
         note="Pre-Tokopedia-deconsolidation basis. FY22 GTV Rp613T also disclosed."),
    dict(firm="GOTO", fq="2023Q3", date="2023-10-30", gtv_idr_t=151.3,
         rev_gross_idr_t=6.0, rev_net_idr_t=3.6,
         guidance="Y — FY23 Adj. EBITDA guidance Rp(4.5)-(3.8)T, positive Adj. EBITDA expected 4Q23",
         other="Cancelled planned international IPO; cash position Rp25.2T; launched GoPay App, GoPay Tabungan, GoRide Transit",
         url="https://www.gotocompany.com/en/news/press/goto-group-moves-towards-growth-and-improves-profitability-as-company-reports-2023-third-quarter-results",
         note="Pre-Tokopedia-deconsolidation basis"),
    dict(firm="GOTO", fq="2023Q4", date="2024-03-19", gtv_idr_t=163.0,
         rev_gross_idr_t=6.5, rev_net_idr_t=4.3,
         guidance="Y — introduced FY24 guidance: Group Adj. EBITDA breakeven",
         other="TikTok/Tokopedia e-commerce combination completed Jan 2024 (TikTok committing >$1.5B, no dilution); "
               "$200M share buyback plan; first-ever positive quarterly Adj. EBITDA (Rp77B)",
         url="https://www.gotocompany.com/en/news/press/goto-group-turns-adjusted-ebitda-positive-surpassing-full-year-guidance-as-company-reports-2023-fourth-quarter-and-full-year-results",
         note="LAST quarter on pre-deconsolidation basis; major concurrent M&A"),
    dict(firm="GOTO", fq="2024Q1", date="2024-04-29", gtv_idr_t=116.5,
         rev_gross_idr_t=4.2, rev_net_idr_t=3.1,
         guidance="Y — formal FY24 guidance: Group Adj. EBITDA breakeven",
         other="Tokopedia deconsolidated to associate-company basis effective 2024-02-01 (TikTok deal closed Jan 31); "
               "GoTo Logistics divestment agreement signed",
         url="https://www.gotocompany.com/en/news/press/goto-group-reports-strong-group-gtv-and-revenue-growth-as-company-announces-2024-first-quarter-results",
         note="FIRST quarter on post-deconsolidation basis -- not comparable to 2022-2023 rows above"),
    dict(firm="GOTO", fq="2024Q4", date="2025-03-12", gtv_idr_t=144.5,
         rev_gross_idr_t=5.0, rev_net_idr_t=4.2,
         guidance="Y — introduced FY25 Adj. EBITDA guidance Rp1.4-1.6T",
         other="Fintech segment first-ever positive Adj. EBITDA; ~$91M repurchased YTD under buyback; "
               "Alibaba/Tencent cloud migration announced; Sahabat AI launch",
         url="https://www.gotocompany.com/en/news/press/goto-group-beats-guidance-with-record-results-as-it-reports-2024-fourth-quarter-and-full-year-earnings",
         note="Post-deconsolidation basis"),
    dict(firm="GOTO", fq="2025Q1", date="2025-04-29", gtv_idr_t=144.6,
         rev_gross_idr_t=None, rev_net_idr_t=4.2,
         guidance="N — reaffirmed FY25 Adj. EBITDA guidance Rp1.4-1.6T",
         other="Fintech record Adj. EBITDA Rp47B; On-Demand record Adj. EBITDA Rp314B; "
               "$99M of $200M buyback program executed by 2025-03-31; cash Rp21T ($1.3B)",
         url="https://www.gotocompany.com/en/news/press/goto-group-achieves-record-profitability-and-strong-growth-as-it-reports-2025-first-quarter-earnings",
         note="Post-deconsolidation basis. Group Core GTV Rp83.2T also disclosed separately."),
    dict(firm="GOTO", fq="2025Q2", date="2025-08-13", gtv_idr_t=152.9,
         rev_gross_idr_t=None, rev_net_idr_t=4.3,
         guidance="N — reaffirmed FY25 Adj. EBITDA guidance Rp1.4-1.6T",
         other="Completed Alibaba/Tencent cloud migration (>50% cloud cost cut expected); Sahabat-AI 70B model; new Deputy CEO",
         url="https://www.gotocompany.com/en/news/press/goto-group-achieves-record-breaking-performance-as-it-reports-2025-second-quarter-earnings",
         note="Post-deconsolidation basis"),
    dict(firm="GOTO", fq="2025Q3", date="2025-10-29", gtv_idr_t=176.5,
         rev_gross_idr_t=None, rev_net_idr_t=4.7,
         guidance="Y — raised FY25 Adj. EBITDA guidance to Rp1.8-1.9T",
         other="First-ever quarterly adjusted pre-tax profit (Rp62B)",
         url="https://www.gotocompany.com/en/news/press/goto-group-records-first-quarterly-adjusted-pre-tax-profit-and-raises-full-year-guidance-as-it-reports-2025-third-quarter-earnings",
         note="Post-deconsolidation basis"),
    dict(firm="GOTO", fq="2025Q4", date="2026-03-11", gtv_idr_t=211.7,
         rev_gross_idr_t=None, rev_net_idr_t=5.0, rev_net_usd_m=300,
         guidance="Y — FY25 Adj. EBITDA Rp2.0T, beat prior Rp1.8-1.9T guidance",
         other="FY25 GTV Rp685.6T (+32% YoY); FY25 net revenue Rp18.3T ($1.1B); Adj. EBITDA Rp672B (+106% YoY); ATUs 66M",
         url="https://www.gotocompany.com/en/news/press/goto-delivers-strongest-year-yet-in-fourth-quarter-of-2025",
         note="Post-deconsolidation basis. USD figures as stated in release ($300M/$1.1B), implies "
              "~Rp16,650-16,700/USD -- not independently sourced, carried as release states it."),
    dict(firm="GOTO", fq="2026Q1", date="2026-04-28", gtv_idr_t=236.3,
         rev_gross_idr_t=None, rev_net_idr_t=5.341,
         guidance="N — maintained FY26 Adj. EBITDA guidance Rp3.2-3.4T",
         other="First-ever net PROFIT (Rp171B, vs Rp367B net loss prior year); Adj. EBITDA +131% YoY to Rp907B; "
               "ATUs 69M; MSCI ESG upgraded to AA",
         url="https://www.gotocompany.com/en/news/press/goto-delivers-net-profit-for-the-first-time-as-it-reports-2026-first-quarter-earnings",
         note="Post-deconsolidation basis. Beyond the round-2 request's stated end date but publicly available; included."),

    # --- GRAB (On-Demand GMV = mobility segment only, not total Group GTV) ---
    dict(firm="GRAB", fq="2024Q2", date="2024-08-15", gmv_usd_m=4400, rev_usd_m=664,
         guidance="mentioned — FY24 revenue outlook assumes ~3.5pp FX headwind",
         other="10th consecutive quarter of Adj. EBITDA growth; 41M MTUs; GXBank >750K deposit customers, "
               "digital-bank deposits $730M (from $479M prior quarter)",
         url="https://www.grab.com/sg/press/others/grab-reports-second-quarter-2024-results/"),
    dict(firm="GRAB", fq="2024Q3", date="2024-11-07", gmv_usd_m=4700, rev_usd_m=716,
         guidance="", other="Revenue +17% YoY, GMV +15% YoY",
         url="https://www.sec.gov/Archives/edgar/data/1855612/000185561224000004/grab-20240930xex991fx3.htm",
         note="Sourced via SEC 6-K exhibit (official filed copy of the press release)"),
    dict(firm="GRAB", fq="2025Q2", date="2025-08-14", gmv_usd_m=5400, rev_usd_m=819,
         guidance="", other="Revenue +23% YoY, GMV +21% YoY",
         url="https://www.sec.gov/Archives/edgar/data/1855612/000185561225000045/a2025q2-earningspressrelea.htm",
         note="Sourced via SEC 6-K exhibit"),

    # --- SEA (Shopee GMV; Sea consolidated GAAP revenue, includes Garena+Monee too) ---
    dict(firm="SEA", fq="2025Q1", date="2025-05-12", gmv_usd_m=28600, rev_usd_m=3500,
         guidance="", other="Record-high Shopee GMV and gross order volume for the quarter",
         url="https://www.businesswire.com/news/home/20250512899100/en/Sea-Limited-Reports-First-Quarter-2025-Results"),
    dict(firm="SEA", fq="2025Q2", date="2025-08-12", gmv_usd_m=29800, rev_usd_m=3800,
         guidance="", other="Gross orders 3.3B (+28.6% YoY); core marketplace revenue $2.6B (+46.2% YoY)",
         url="https://cdn.sea.com/webmain/static/resource/seagroup/website/investornews/2Q2025/ael196LSsTKP3uVZYuCA/2025.08.12%20Sea%20Second%20Quarter%202025%20Results.pdf"),
    dict(firm="SEA", fq="2025Q4", date="2026-03-03", gmv_usd_m=36700, rev_usd_m=6900,
         guidance="", other="Shopee GAAP revenue $4.3B (Shopee-specific, not the $6.9B consolidated figure); "
               "gross orders 4.0B (+30.5% YoY); FY25 net income $1.6B (>3x YoY)",
         url="https://www.businesswire.com/news/home/20260302039769/en/Sea-Limited-Reports-Fourth-Quarter-and-Full-Year-2025-Results"),
    dict(firm="SEA", fq="2026Q1", date="2026-05-12", gmv_usd_m=37300, rev_usd_m=7097.49,
         guidance="", other="Net income $427.94M; Monee revenue $1.2B (+57.8% YoY); Garena revenue $696.6M (+40.6% YoY, best quarter since 2021)",
         url="https://www.businesswire.com/news/home/20260511833139/en/Sea-Limited-Reports-First-Quarter-2026-Results",
         note="Beyond the round-2 request's stated end date but publicly available; included."),
]
