# Spin-off paper: pre-registration (written 3 Oct 2026, before any new firm's numbers are collected)

The git commit that adds this file is the timestamp. Changes only as dated addenda at the end. This is separate from the thesis; the thesis question, hypotheses and measures do not change.
Already seen before writing (so in-sample, not evidence for the tests below): the thesis panel (Grab, GoTo, Tokopedia, Blibli, Bukalapak, Sea, Uber, Lyft, DoorDash, Instacart, Delivery Hero, Meituan, Talabat, Jumia, MakeMyTrip, eBay, Etsy, Mercado Libre, Rakuten, Shopify, Zalando and the other firms in `../tables/l_panel.csv` and `../tables/peers_quarterly.csv`). Results are reported for the new firms alone and for all firms.

## Sample
- Universe: the core tier of `universe_scan.csv` (marketplaces, ride-hailing and delivery, travel, services marketplaces).
- A firm-year enters when the filing gives both a transaction-value measure (V: GMV, GTV, gross bookings, GOV, GSV) and total revenue (R) for the same fiscal year and scope. One V per firm (the one-V rule); a change in what V covers starts a new series.
- Firm-years where first-party product sales are more than half of revenue are excluded (R is then not a platform's cut). Firm-years where they are 20-50% are kept and flagged; every test is repeated without them.
- Values are taken from annual reports (10-K, 20-F, 40-F, or the firm's own annual report), quote-checked with `check_rows.py`. Currency: each firm's reporting currency, so growth rates are free of exchange-rate effects.

## Measures
m = R / V (the platform's cut). Growth of revenue splits exactly: g_R = g_V + g_m, with g = change in the natural log over one year. g_V is the volume part, g_m the cut part.

## Tests
**S1. Persistence.** Pooled firm-years, 2015-2025: g_R(t+1) = a + b1 g_V(t) + b2 g_m(t) + e, standard errors clustered by firm (wild cluster bootstrap, 999 draws). Prediction: b1 > b2 (revenue growth that comes from a higher cut repeats less than growth that comes from more volume). Falsified if b1 - b2 <= 0. Also reported: the same with rank-transformed growth, and without flagged firm-years. Log changes are winsorised at the 1st and 99th percentiles.

**S2. The 2022 funding shock.** Exposure = free cash flow (operating cash flow minus capital expenditure) divided by revenue in fiscal 2021. Outcome = g_m from fiscal 2021 to fiscal 2023 (change in the log cut over two years). Prediction: firms with negative 2021 free cash flow raised their cut more than firms with positive free cash flow (one-sided Mann-Whitney, one observation per firm), and the rank correlation between exposure and outcome is negative. Placebo: the same rank correlation for 2017 exposure and the 2017-2019 outcome is smaller in absolute size. Falsified if the main rank correlation is zero or positive. With few firms this is descriptive and says so.

**S3. Firms that stop reporting V.** For each firm that stops publishing V (for example Alibaba, JD, Pinduoduo, Bukalapak, Grab's financial-services GMV), compute the share of revenue growth from the cut (g_m / g_R) over the last two years before it stops. Prediction: in at least half of these firms that share is above one half. Falsified otherwise. Descriptive (few cases).

## Not registered
Stock-return and analyst-forecast tests (earlier thesis attempts were null or inconclusive); any test of a cross-country tax rule (to be registered separately, before any outcome series is opened).
