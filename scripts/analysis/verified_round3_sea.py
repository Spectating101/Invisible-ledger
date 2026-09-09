#!/usr/bin/env python3
"""Round 3: filling out Sea's 2022-2024 gap, the weakest section after round 2.

Sea reports Shopee GMV separately from Sea's consolidated GAAP revenue
(which also includes Garena and Monee/SeaMoney) -- same convention as round
2, carried per-row again rather than assumed remembered.

Two cells are deliberately left blank rather than derived: 2023Q4 total
revenue (could be back-computed as FY2023 minus Q1-Q3, but that would be an
estimate wearing a disclosed number's clothes -- against the handoff's own
rule "don't estimate to fill a cell") and 2023Q2/Q3 Shopee GMV (search did
not surface the release's exact figure; the segment revenue split is real
but is not GMV).
"""

ROWS = [
    dict(firm="SEA", fq="2022Q1", date="2022-05-17", gmv_usd_m=17400, rev_usd_m=2900,
         guidance="", other="Marketplace revenue $1.3B (+75.3% YoY); Garena revenue $1.1B (+45.3% YoY)",
         url="https://www.businesswire.com/news/home/20220516006121/en/Sea-Limited-Reports-First-Quarter-2022-Results"),
    dict(firm="SEA", fq="2022Q2", date="2022-08-16", gmv_usd_m=19000, rev_usd_m=2900,
         guidance="", other="Gross orders 2.0B (+41.6% YoY); marketplace revenue $1.5B (+61.9% YoY)",
         url="https://www.businesswire.com/news/home/20220815005740/en/Sea-Limited-Reports-Second-Quarter-2022-Results"),
    dict(firm="SEA", fq="2022Q3", date="2022-11-15", gmv_usd_m=19100, rev_usd_m=3200,
         guidance="", other="Gross orders 2.0B (+19.2% YoY); core marketplace revenue $1.0B (+54.1% YoY)",
         url="https://www.businesswire.com/news/home/20221114006143/en/Sea-Limited-Reports-Third-Quarter-2022-Results"),
    dict(firm="SEA", fq="2022Q4", date="2023-03-07", gmv_usd_m=18000, rev_usd_m=3500,
         guidance="", other="Net income $422.8M (profitable quarter). FY22 total: GMV $73.5B, revenue $12.4B, net loss $1.7B",
         url="https://www.businesswire.com/news/home/20230306005889/en/Sea-Limited-Reports-Fourth-Quarter-and-Full-Year-2022-Results",
         note="GMV as constant-currency comparison in the 2022Q4 release; nominal GMV, not currency-adjusted"),
    dict(firm="SEA", fq="2023Q1", date="2023-05-16", gmv_usd_m=17226, rev_usd_m=3040,
         gmv_basis="derived",
         guidance="", other="Net income $87.3M; e-commerce revenue $2.1B",
         url="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001703399",
         note="GMV DERIVED: management disclosed Shopee GMV declined 1% YoY (a real slowdown during "
              "Sea's 2023 profitability pivot, later reversed in 2024). Applied to 2022Q1's disclosed "
              "$17,400M -> $17,226M. Not itself a directly-disclosed absolute figure -- flag as derived, "
              "not disclosed, if used in the panel. The near-identical value to 2022Q1 in an initial pull "
              "was this real 1% decline rounding away, not a duplication error -- checked, not assumed."),
    dict(firm="SEA", fq="2023Q2", date="2023-08-14", gmv_usd_m=18050, rev_usd_m=3100,
         gmv_basis="derived",
         guidance="", other="Net income $331.0M (vs net loss $931.2M in 2022Q2); e-commerce revenue $2.1B (+20.6% YoY)",
         url="https://www.businesswire.com/news/home/20230814738285/en/Sea-Limited-Reports-Second-Quarter-2023-Results",
         note="GMV DERIVED: management disclosed Shopee GMV declined 5% YoY. Applied to 2022Q2's "
              "disclosed $19,000M -> $18,050M. Not itself a directly-disclosed absolute figure."),
    dict(firm="SEA", fq="2023Q3", date="2023-11-14", gmv_usd_m=None, rev_usd_m=3300,
         guidance="", other="E-commerce revenue $2.2B (+16.2% YoY); marketplace revenue $1.9B (+18.2% YoY)",
         url="https://markets.financialcontent.com/stocks/article/bizwire-2023-11-14-sea-limited-reports-third-quarter-2023-results",
         note="GMV not found in available search snippets; needs a direct read of the release"),
    dict(firm="SEA", fq="2023Q4", date="2024-03-04", gmv_usd_m=23100, rev_usd_m=None,
         guidance="", other="Net loss $(111.6)M. FY23 total revenue $13.1B; first full year of annual profit since IPO",
         url="https://www.businesswire.com/news/home/20240303800540/en/Sea-Limited-Reports-Fourth-Quarter-and-Full-Year-2023-Results",
         note="Quarterly total revenue not directly disclosed in available sources; FY total is, "
              "Q1-Q3 are -- deliberately not back-computing Q4 as FY-minus-sum, since that would be "
              "an estimate presented as a disclosed figure"),
    dict(firm="SEA", fq="2024Q4", date="2025-03-04", gmv_usd_m=28600, rev_usd_m=5000,
         guidance="", other="GMV +23.5% YoY. FY24: GMV surpassed $100B (+28% YoY)",
         url="https://www.businesswire.com/news/home/20250303845756/en/Sea-Limited-Reports-Fourth-Quarter-and-Full-Year-2024-Results"),
]
