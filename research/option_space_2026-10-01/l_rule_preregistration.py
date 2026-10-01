"""Discount-leverage rule: pre-registration (written 2 Oct 2026, BEFORE the out-of-sample data were opened).

Definitions (per firm or segment s, year t):  V = transaction value, R = revenue after incentives,
  m = R / V,  iota = incentives / V,  L = iota / m  (discounts per dollar of revenue kept; L is infinite when R <= 0).
Identity: m = tau - iota, so a cut in incentives of x% of iota moves ln m by about  L * x%.

In-sample episodes (used to form the rule, so NOT evidence for it): Grab on-demand 2022Q1-2026Q1, GoTo on-demand 2022-2025,
Tokopedia 2022-2023, MakeMyTrip 2019-2025, Grab 2019-2021 segments (seen before this file was written).
Out-of-sample (not yet opened): Sea/Shopee 2017-2022, Uber 2016-2018, Lyft 2016-2018, DoorDash 2018-2020, Instacart 2021-2023,
Blibli 2022-2025 segments, Bukalapak 2019-2024, Delivery Hero 2019-2025.

Prediction P1 (the rule): the next-year move in take rate is larger when L_t is high.
  Bucket firm-years by L_t:  <0.5 | 0.5-1 | 1-2 | >2 (R <= 0 counts as >2).
  Outcome: |ln m_{t+1} - ln m_t| greater than eps (headline eps = 0.10; also report 0.05 and 0.20); both m > 0.
  P1 holds if the share exceeding eps is higher for L_t >= 1 than for L_t < 1, in the out-of-sample set alone.
Prediction P2 (mechanism): when L_t >= 1 and m rises, incentives fall (iota down) by more than the gross fee rate tau rises.
Prediction P3 (stability): where L_t < 0.5, the typical |Delta ln m| is within eps.
Unit of inference is the firm-segment, not the observation; with few units this is descriptive and says so.
Anything not tested here is exploration, not evidence.
"""
