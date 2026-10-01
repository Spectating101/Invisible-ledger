> **READ FIRST (1 Oct 2026).** This atlas is a research reference, not the thesis plan. Its frames F1 to F10 and the "pivot map" were options explored before the researcher ruled out a concept pivot; the thesis executes the 27 September proposal (see `AGENTS.md`). Use it for the recomputed numbers, the audit erratum and the data-source notes only.

# Invisible Ledger: thesis option-space atlas

Compiled 1 October 2026, the day the proposal passed. Purpose: every number recomputed, every plausible frame laid out with its evidence, so the thesis can be built, or re-pivoted, without redoing the groundwork.

**Reproduce:** `PYTHONPATH=/home/phyrexian/.local/lib/python3.13/site-packages python3 build_numbers.py` in this folder. It reads only committed repo CSVs and writes `tables/`. Statistics are exploratory and small-N. Web facts are from news or summary pages and are graded in §6; verify them against primary sources before they enter a manuscript.

---

## ⚠ Audit erratum (1 Oct 2026, after independent review by Grok; accepted by Claude Opus)

Sections 2–3 below overreach in the following ways. Where this erratum and the body disagree, **this erratum wins**.

1. **Observation-level p-values are not evidence.** The Mann–Whitney, Fisher and sign tests treat firm-years as independent, ignore the shared 2022–23 shock (all three Indonesian firms move together), and were chosen from a battery of ~20 comparisons. The surviving statement is descriptive: *three disclosing Indonesian firms show much larger take-rate movements than most listed reporters, concentrated in 2022–23.*
2. **The cluster-bootstrap "95% intervals" are invalid.** Resampling 3 firms, then taking a row-level median, is not a valid interval. Delete [4.9, 57.9] and [0.05, 0.45].
3. **The firm-level permutation test** uses the mean of firm medians, so Tokopedia's single transition counts as a "median". It does not test the reported 38.92 vs 7.10.
4. **"Tracking" and the story classifier need fixing.** Small opposite-sign moves (Etsy 2023–24, Zalando 2021–22, eBay 2022–23) are counted as tracking. Rows where both measures fell are labelled "R outruns V". The rule is to classify the sign pattern first, then the size.
5. **Scope asymmetry.** Indonesian rows are all treated as clean while 7 of 8 are geography- or scope-pending. Blibli 2022–23 (+1.43 log-points) may be a definitional or business-mix jump and must be checked against the filing before it is used.
6. **"Abroad, revenue outgrowing commerce is the norm" is Sea-driven.** Excluding Sea, it is 15 of 22 (p = 0.13).
7. **"Young-subsidised vs mature" is NOT identified.** Stage was read off the outcome itself, and no subsidy measure exists independently of |Δln m|. It is a hypothesis, not a finding.
8. **The within-firm decay is Sea alone.** Excluding Sea, the slope is −0.032 (permutation p = 0.20). "Age" is time since first disclosure, so the slope is a calendar trend. Drop F8 as a finding.
9. **Leverage via E fails** (unchanged): firm-level ρ = 0.07.
10. **Variance decomposition of revenue growth** (new, descriptive): the share explained by the slice is Indonesia 0.86, external 0.65, external ex-Sea −0.07, Sea alone 0.77, Indonesia without Blibli 2022–23 0.27. It is outlier-dominated, so it is not a headline.
11. **The F2 profit-pivot mechanism is evidenced only for Tokopedia** (incentive split). Its extension to Blibli and Bukalapak requires their incentive data.

**What survives intact:** all 55 ledger numbers; the Tokopedia incentive bridge; the BPS facts; the hidden-value-added ceiling arithmetic; the policy facts at their stated grades; the decomposition m = τ − ι (§11).

**Consequence:** the current Indonesian sample cannot carry an inferential claim. The thesis needs an empirical engine in which the mechanism variable, incentive intensity, is measured **independently of the outcome** on a larger platform panel. See §11.

---

## 11. Theory spine proposed after the audit (Opus): slice = fee − voucher

* Net take rate **m = τ − ι**, where τ is the gross commission or fee rate and ι is incentive intensity (contra-revenue vouchers and subsidies as a share of V). Revenue R = (τ − ι)·V.
* Wedge **W = V − R = (1 − τ)·V + ι·V**: sellers' and drivers' gross receipts plus buyers' subsidies, the money the platform passes to everyone else. This is gross receipts, not income or value added.
* **Leverage.** d ln m = (τ/m)·d ln τ − (ι/m)·d ln ι. When ι is large relative to m, small voucher changes swing revenue. Tokopedia 2022: ι/τ ≈ 0.50, so τ/m ≈ 2.0. The predictor of instability is **ι/m**, not E.
* **Three actors, three levers:** investors and funding conditions on ι (the profit pivot); the state on τ (the 8% cap) and on the visibility of V (PMK 37 withholding); competition on both.
* **Fingerprint.** A strategy shift (growth to profit) moves m up and V down together, producing reversals. A demand shock moves V with m roughly fixed. So corr(Δln V, Δln m) < 0 marks strategy-driven periods.
* **Testable once ι is measured:** (P1) |Δln m| rises with ι/m; (P2) Δι < 0 when funding tightens, explaining Δm > 0 with flat or falling V; (P3) after the cap, m on capped services falls by less than the mechanical Δτ because ι is cut and buyer fees rise (waterbed); (P4) taxing visible V shifts marginal sellers to unrecorded channels (future work after Nov 2026).

---

## 0. Working rules for this phase

1. **Translate, don't police.** When the framing is loose ("hidden GDP", "not recorded", "they play with numbers"), the job is to find the strongest version of that idea the evidence supports and use it. §4 is the translation table. A difference is flagged once, only where it would change a conclusion.
2. **Every claim carries a grade** (§6): **A** recomputed from repo source; **B** primary source seen; **C** news/summary only, needs a primary check; **D** inference or hypothesis.
3. **Kid test.** Every frame has a one-line explanation a kid or a dog could follow (night-market picture: platform = market owner, transaction value = all till receipts, revenue = the owner's cut, incentives = vouchers the owner hands out).

---

## 1. The whole thing in four sentences

An app lets people sell. People spend a lot through it (transaction value, V) and the app keeps a slice (revenue, R); the slice is the take rate m = R / V. Most of what looks like "the app grew" or "the app shrank" is really "the slice changed", and who changes the slice is the interesting question: the company (through discounts and definitions), the state (through caps and taxes) and time (young apps are unstable, mature ones settle). The wedge W = V − R is the pile the slice does not cover; it is what everyone is fighting over and what a revenue-only reader cannot see.

---

## 2. What the numbers say now (all in `tables/`)

### 2.1 Ledger: every proposal and deck number reproduces

`tables/claims_ledger.csv`: **55 of 55 claims PASS** when recomputed from source CSVs (median |D| 38.92 pp, 6 of 8, Tokopedia −8.9 / +53.2 / 60.6%, BPS 17.08 / 1.45 / 20.57 / 98.46, count shares 90.29 and 70.95 by the symmetric decomposition, FY2023 totals, wedge 2.92% of GDP, payments multiples, and the deck's Mann–Whitney and correlation figures). Nobody can fairly say these numbers are inaccurate. The remaining issues are about *interpretation*, below.

Identity check: Δln m computed from growth rates equals ln(m₁/m₀) from the level tables to 4×10⁻¹⁶.

### 2.2 The honest strength of the headline (grade A)

| Question | Result | Reading |
|---|---|---|
| Does revenue grow faster than commerce more often in Indonesia? | 6 of 8 in Indonesia (sign test p = 0.29). **22 of 29 abroad (p = 0.008).** | Direction is *not* what distinguishes Indonesia. Abroad, revenue outgrowing commerce is the norm. |
| Do reversals (one up, one down) distinguish Indonesia? | 2 of 8 vs 4 of 29, Fisher p = 0.59 | No. Reversals are dramatic, not unusual. |
| **Is the take rate stable within ±10 log-points?** | Indonesia **1 of 8** (12.5%); abroad **20 of 29** (69%); abroad ex-Sea 82%. Fisher p = 0.012. | **This is the real contrast: size and stability, not direction.** |
| Size of drift, median \|Δln m\| | Indonesia 0.252; abroad 0.055; abroad ex-Sea 0.033 | Indonesia's take rate moves about 5–8× more. |
| Same, in the proposal's units (median \|D\|) | 38.92 pp vs 7.10 pp (4.19 pp ex-Sea) | Matches the proposal. |
| Observation-level test | Mann–Whitney p = 0.002 (D), 0.004 (Δln m); ex-Sea < 0.0002 for both | Treats 8 and 29 transitions as independent. |
| **Firm-level test (firms as the unit)** | Exact relabeling over firms: **p = 0.061 (D), 0.030 (Δln m)**, ex-Sea **0.008 / 0.017** | Honest strength is *moderate*. 3 firms vs 8. |
| Effect size, cluster bootstrap | Difference in median \|D\|: 95% interval **[4.9, 57.9] pp**; Δln m **[0.05, 0.45]** | Large and clearly positive; precise size uncertain. |
| Drop the 2022–23 cluster | MW p = 0.025 (D) / 0.036 (Δln m); firm-level p = 0.22 / 0.11 | Survives at observation level, **not** at firm level. |
| Include constructed Grab/Shopee (12 vs 29) | MW p = 0.0006; firm-level 0.023 (D) / 0.012 | Stronger, but those 4 rows are mechanically tied to Group ratios. |

**What this does and does not support.** It supports: *Indonesian platforms' take rates are far less stable than other listed platforms'.* It does not support: "Indonesia is special" (see 2.3) or "revenue usually outgrows commerce here" as a distinguishing fact.

### 2.3 What explains the difference? Candidate drivers

| Candidate | Evidence | Status |
|---|---|---|
| **Growth stage / subsidy phase** | Sea/Shopee (growth-stage, EM) median \|Δln m\| 0.25, identical to Indonesia; Jumia 0.16; mature Zalando/Rakuten/eBay 0.02–0.03. A gradient, not a border. | Strong fit; confounds "Indonesia" with "stage". Grade A (descriptive). |
| **Within-firm decay over time** | Fixed-effects slope −0.128 log-pts per year; permutation p = 0.002 (8 firms, 33 obs). Sea: 2.48 → 0.59 → 0.25 → 0.29 → 0.14 → 0.07 → 0.055. Six of eight firms decline; Bukalapak and Etsy rise on n = 3. | Real pattern, **but "age" and calendar year are not separable** in this design (age = year − first year; firm fixed effects absorb the start year). Needs firms of different ages in the same year. Grade A pattern / D mechanism. |
| **Common 2022–23 shock** | All three Indonesian firms are positive in 2022–23 (+0.52 median, share positive 100%); every Indonesian transition from 2022 on is positive. External 2022 transitions: 80% positive but small (median 0.08). | Effective Indonesian evidence ≈ one regime shift plus Blibli follow-ons. Consistent with a post-funding-winter profit pivot (hypothesis D). |
| **Incentive leverage (mechanism)** | Revenue is net of incentives: R = G − I. Tokopedia 2022: incentives 50.5% of gross revenue, so G/R ≈ 2.02: net revenue moves about twice as hard as gross. 2023: incentives 31.3%, G/R 1.45. Grab Q2 2026 (6-K via summary, grade C): incentives 10.9% of on-demand GMV against a 13.3% net take, so incentives are about 45% of gross take. | Strong mechanism, but only Tokopedia and Grab have the data. Needs incentive series for other issuers. |
| **Wedge size E predicts instability** | Firm-level ρ = 0.07 (external, n = 8). With Indonesian firms added, ρ = 0.52, p = 0.10 (n = 11); pooled rows ρ = 0.58 but non-independent. | **Not established.** Shopify (E ≈ 34, stable) breaks it. My earlier "suggestive" read was cluster-inflated. Retract as a stand-alone claim. |

### 2.4 D versus the take-rate log change

D = g(R) − g(V) is mechanically scaled by V growth (D = g_m·(1+g_V)); |D| vs |g_V| gives ρ = 0.52 externally. Δln m is the exact, scale-free version. The headline survives the switch. Recommendation: Δln m as primary object, D reported as the proposal's familiar number.

### 2.5 Level facts (grade A)

* Take rates (R/V) by firm (`cross_platform_take_rates.csv`): Zalando ~70% (owns inventory), Jumia 18–23%, Mercado Libre 16–25%, Etsy 16–24%, Rakuten 15–16%, eBay 10–14%, Sea/Shopee 0.2% → 13% over 2017–2025, Shopify 2.6–3.1%, **Indonesian issuers 0.5–3%** (Tokopedia 1.5→2.5, Blibli 0.8→2.9, Bukalapak 1.6→2.7), Grab Indonesia (constructed) 4→11%.
* Every issuer-reported take rate rises over its window (all E ends below its start, 3 of 3). The *level* creeps up while the *variance* decays; this matches the wider platform story that fees creep upward (Amazon's effective take rate reported rising from ~26% to ~34% 2020–2026, grade C, secondary).
* 2023 visibility ladder (`visibility_ladder_2023.csv`): GDP US$1,371bn; BPS e-commerce US$72.3bn (5.3% of GDP); BPS marketplace category US$13.2bn (0.96%); outside the marketplace category US$59.1bn (4.3%); three-platform V US$43.2bn (3.15%); their revenue US$3.16bn (0.23%); wedge US$40.07bn (2.92%). **Levels are not like-for-like**: Tokopedia + Shopee V (US$37.9bn) alone exceeds BPS's marketplace category.
* **Hidden-value-added ceiling** (`hidden_value_added_scenarios.csv`, scenarios not estimates): if the *entire* wedge were informal sales and sellers' value added were 5 / 10 / 20 / 30% of sales, the hidden value added would be 0.15 / 0.29 / 0.58 / 0.88% of GDP. For the whole BPS outside-marketplace sales: 0.22 / 0.43 / 0.86 / 1.29%. The 2.9% is a gross-sales number; the GDP-comparable number is a fraction of it.
* BPS 2023→24 (grade A): total +17.08%; businesses +15.31%; sales per business +1.54%; count accounts for 90.29% (70.95% under the alternative 2023 count); marketplace category +1.45%, other channels +20.57%; 98.46% of the increase outside the marketplace category; 2022→23 total +40.60%, count ≈ 71%.
* Tokopedia 2022→23: V −8.9%, net revenue +53.2%; revenue change = gross revenue +39.4% share + incentive reduction 60.6% share (arithmetic, not causal).

---

## 3. The frames (any can be the spine; most can be chapters)

Grades: evidence readiness today (A–D); **Cost** = work to make it thesis-grade.

### F1. The Slice (take-rate drift is the object): *recommended core*
* **Kid line:** "The market owner keeps a slice of every sale. The slice keeps changing, so the owner's book tells you less about the market than you think."
* **Claim:** Revenue is a reliable stand-in for commerce only while the take rate holds still; in Indonesian platforms it does not (12.5% tracking vs 69% abroad).
* **Numbers:** §2.2, §2.4, §2.5. Wedge = the stake; W, E retained as notation, D as the familiar statistic.
* **Strength:** B+. Large effect, moderate firm-level inference, reproducible.
* **Needs:** per-issuer bridges for every big move (Blibli 2022–23 +1.43 log-pts, Blibli 2021–22, Bukalapak 2021–22); a larger firm panel (§7).
* **Kill risk:** with so few Indonesian firms, a reviewer says "this is three firms". Mitigated by §7 expansion.
* **Pivot cost:** none, it is the base.

### F2. The Profit Pivot (firms choose the slice)
* **Kid line:** "The owner handed out fewer vouchers, so his book jumped even though stall sales fell."
* **Claim:** In 2022–23, after the funding winter, platforms shifted from growth to profitability; because revenue is net of incentives, cutting incentives raised reported revenue while commerce fell.
* **Numbers:** Tokopedia 60.6% of net-revenue rise from lower incentives; incentives 50.5% → 31.3% of gross revenue; net +53%, gross +10%. All three Indonesian firms positive in 2022–23. GoTo Q2 2026 (grade C): net revenue +20% vs GTV +2%, repeating the pattern.
* **Testable predictions:** (a) more positive Δln m when funding tightens or profit targets bind; (b) Δln m correlates with change in incentive intensity; (c) metric redefinitions cluster at pressure points (Grab changed its GMV basis after FY2023; Blibli's take-rate definition is GPBD/TPV).
* **Strength:** C+. One firm is fully diagnosed; the time clustering is real but untested.
* **Needs:** incentive series (Grab discloses incentives/GMV; GoTo/Tokopedia annual notes; Blibli/Bukalapak unknown); funding-conditions proxy; definition-change log.
* **Honest boundary:** the repo shows disclosed accounting choices, not manipulation. The defensible claim is "managers choose incentive spending, and the accounting converts that choice into reported revenue."
* **Kill risk:** one regime episode; alternative explanation = post-COVID normalization (external 2021–22 also positive).

### F3. The State Moves the Slice (policy shocks to m)
* **Kid line:** "The city told the owner he can keep only 8 of every 100. His book shrinks even if the stalls sell the same."
* **Facts (grade B/C):** Perpres 27/2026 (Protection of Online Transport Workers) caps commissions at **8% (from 20%)**, drivers get ≥92%, motorcycle drivers (more than 4 million) reclassified as micro-entrepreneurs; effective **1 July 2026**; applies to **two-wheel only**, still excluding four-wheelers and all deliveries (GoTo call, 2026 Q2). GoTo cut FY on-demand EBITDA guidance by **IDR 300bn**; GoRide ≈ 7% of group net revenue; management calls the unit economics negative and plans "pricing, platform fees and surge" offsets (a waterbed response). Grab's Q2 6-K (summary, grade C) did not mention the cap and raised guidance.
* **Precedents:** card interchange caps (Durbin: debit interchange revenue per transaction fell from ~44¢ to ~24¢; waterbed: free checking down ~40 pp; small-ticket merchants' costs rose), grade C; NYC 2020 delivery fee caps (15%/5%; DoorDash and Grubhub quarterly cost estimates; a Wisconsin–Delaware study finds chains benefit and small restaurants lose orders), grade C; China's Meituan 2021: commission guidance and a RMB 3.44bn fine, commissions cut for ~1m small merchants, grade C.
* **Why it matters here:** a real, dated, politically visible policy shock acting on the revenue side while the transaction side is not directly changed. The tax side (PMK 37/2025, 0.5% of seller turnover above Rp500m) acts on the *transaction* side. The wedge is where the two meet.
* **Scale warning:** two-wheel is ~7% of GoTo net revenue and <6% of Grab Mobility. At group level the take-rate change will be small. A clean test needs segment- or service-level data (GoRide), which may not be disclosed.
* **Timing:** first post-cap quarter (Q3 2026) results are expected around Nov 2026 (typical cadence, unconfirmed). Q2 2026 (Apr–Jun) is pre-cap.
* **Strength:** B for relevance, D for evidence (no post-cap data yet).
* **Needs:** primary text of Perpres 27/2026 and the transport-ministry regulation; Q3 2026 and Q4 2026 releases; pre-registered predictions now (revenue take rate ↓ on two-wheel; offsetting fees/fares ↑; incentives ↓).
* **Kill risk:** effect diluted to noise; data timing outruns the defense date.

### F4. The Shadow-Economy Window (what your "hidden economy" instinct becomes)
* **Kid line:** "The big recorded things in the market are the owner's cut. Most of the small stalls and WhatsApp sellers don't keep books at all. The market's till receipts are the nearest thing to a record of them."
* **Facts:** World Bank PRWP 10608: informal economy averaged **36% of GDP** (2011–19) and ~**75% of employment** (2019); other estimates range 22–40% of GDP and ~59% of workers (grade B/C, definition-dependent). BPS: 95.33% of e-commerce businesses use instant messaging; complete financial statements 28.63% of marketplace users vs 12.25% of non-users; 98.46% of the 2023→24 growth is outside the marketplace category. Tax: ~1.6m small-business taxpayers in e-commerce vs ~653k filed in 2024 (grade C, secondary, and based on a Rp487tn e-commerce figure that conflicts with BPS's Rp1,289tn: another definition mismatch). PMK 37/2025 withholds 0.5% of seller gross turnover above Rp500m via four designated marketplaces (Tokopedia, Shopee, Lazada, Blibli), start **1 Nov 2026** after a one-month then three-month deferral (DJP; grade B/C).
* **What the data can say:** (i) platforms hold transaction records of sellers and drivers that formal books mostly lack; (ii) growth is concentrating where no platform ledger exists (messaging, social); (iii) states are already using platform records to bring sellers into the tax net (PMK, DAC7-style regimes).
* **What it cannot say:** that V − R is hidden GDP. The hidden-value-added ceiling is 0.15–0.9% of GDP under the wedge scenarios (§2.5), a number worth stating because it is the *defensible* version.
* **Strength:** B for context, D for a quantified hidden-economy estimate.
* **Needs (to upgrade):** BPS marketplace study microdata (licensed) or published breakdowns of sellers by size/formality; a defensible seller-margin range; Bank Indonesia QRIS data as a second visibility layer (already in repo).
* **Kill risk:** reviewers will challenge any "hidden GDP" number. Present it as a bound, not an estimate.

### F5. The Tangled Incentives (political economy, the "dual pull")
* **Kid line:** "The owner wants his book to look good to investors. The city wants to see all the sales to tax them. They are looking at different columns of the same notebook."
* **Dated facts (grade B/C):** 2025 revenue shortfall; 2026 tax revenue forecast ~IDR 46.9tn below target, deficit forecast widened to 2.85% of GDP; yet the marketplace tax was **delayed twice** (1 Jul → 1 Aug → 1 Nov) and collector appointments revoked and collected amounts refunded, citing purchasing power; industry asks for Jan 2027. Presidential driver measures (cap, micro-entrepreneur status) arrived the same quarter.
* **Reading:** the state's goals conflict (revenue vs consumption vs worker populism), so the stake W is contested by three actors with different goals. This is a framing for *why now*, not an empirical test.
* **Honest boundary:** nothing in the repo shows firms or the state acting in bad faith. The accurate claim is incentive-driven choices about which number to emphasize, each individually legitimate.
* **Strength:** B for timeliness, D as a testable hypothesis.
* **Needs:** a short institutional chapter with a dated policy timeline (§8); a conceptual model (F9).

### F6. Does the Market Price the Slice? (the investor-use test)
* **Kid line:** "When the owner reports, do shareholders cheer the book or the sales?"
* **Claim to test:** past a threshold of incentive leverage or take-rate instability, prices respond to transaction-value news more than to revenue news, or the reverse.
* **Prior art (grade C, verify):** Trueman, Wong & Zhang (2000, JAR) on web traffic and Internet stock prices; Davis (2001, JAR) on value relevance of grossed-up and barter revenue; Bowen, Davis & Rajgopal (2002, CAR) on revenue-reporting practices. These make the accounting-finance home concrete.
* **Existing data:** 47 company-quarters (GoTo 16, Grab 17, Sea 14) with announcement dates; daily prices for GOTO.JK, GRAB, SE, BUKA.JK, BELI.JK, BABA and indices (2010–2026). Preliminary CAR correlations are null (r = −0.13, p = 0.37, N = 47). **31 of 47 events are still unclassified for contamination**; the event study is formally blocked. Group-level GTV for GoTo and Grab dilutes Indonesia.
* **Strength:** D. Needs the contamination ledger finished, cleaner event windows, and many more firm-quarters (§7).
* **Kill risk:** low power; null results are likely and would be a weak thesis spine but a fine chapter.

### F7. The Comparability Atlas (Kong's question)
* **Kid line:** "Every market counts 'sales' differently: some include shipping and tax, some count cancelled orders, some mix in travel. 'Transaction value' is not one thing."
* **Material in repo:** `global_platform_definition_map.csv` (8 issuers: GMS vs GMV, net of refunds or not, VAT, shipping, travel, B2B). Indonesian issuers: Tokopedia GTV vs net revenue after incentives; Blibli GPBD/TPV with travel; Bukalapak Group with overseas; Grab group GMV with financial services through FY2023.
* **Claim:** cross-platform comparisons of transaction value and take rate are unsafe without a definition map; within-firm comparison is the only safe one. This is the "terms" problem made into a deliverable.
* **Strength:** B. Cheap, adds clarity, answers Kong directly. Natural appendix or chapter.
* **Needs:** extend the map to Indonesian issuers and any new firms.

### F8. The Life Cycle of the Slice (level creeps up, variance decays)
* **Kid line:** "New markets change their cut all the time. Old markets settle, but the cut slowly creeps up."
* **Numbers:** §2.3 (decay) and §2.5 (all issuer take rates rise).
* **Strength:** B- as a pattern, D as a mechanism (age vs calendar confound).
* **Needs:** firms of different ages observed in the same years (more Indonesian and Southeast Asian issuers; earlier histories).

### F9. A small model (optional theory spine)
* **Kid line:** "The owner chooses his cut and his vouchers while the city, the shareholders and rival markets pull on him."
* **Idea:** platform picks fee m and incentives I to maximize value subject to an investor profit constraint, a regulatory cap, and competition; predictions: cap binds → fees on uncapped services rise (waterbed); profit pressure → I falls, reported R rises relative to V; maturity → lower variance. Gives the empirical work something to confirm or refute, which is how a master's paper reads like a real paper.
* **Strength:** n/a (design choice). **Needs:** a couple of pages of formal setup; no new data.

### F10. Fallback: the proxy-adequacy framework (the passed proposal)
* Defensible but abstract; keep as the closing "what this means for anyone using a revenue number". Cost: none.

---

## 4. Translation table (your phrasing → the strongest version the evidence supports)

| You say | What I take you to mean | Strongest supported statement |
|---|---|---|
| "Hidden GDP / shadow economy" | A lot of platform-linked activity is not captured in formal books or statistics, and platform data can reveal it. | "The platform's transaction records are the nearest record of small sellers' and drivers' sales, which mostly sit outside formal books. The wedge is the size of that commerce; the genuinely hidden value added is a fraction of it (0.15–0.9% of GDP in the scenarios)." |
| "H2 connects to the hidden economy, not recorded" | National growth is happening in places no one is keeping a ledger. | "98.46% of 2023→24 e-commerce growth is outside the marketplace category, mostly from more sellers (90%). Only 12–29% of e-commerce businesses keep complete financial statements. Growth sits where there is no platform ledger and little bookkeeping." |
| "Firms play with numbers to look good" | Managers choose what gets reported and how. | "Revenue is net of incentives that managers choose; cutting them raises revenue while commerce falls (Tokopedia 60.6%). Firms also choose and change metric definitions." |
| "Government needs money, so tax pressure" | The state wants more of the commerce visible. | "The 2026 deficit forecast is wider and the marketplace tax targets seller turnover, but the state also delayed it twice for purchasing power: it is torn between revenue and consumption." |
| "Past a threshold, use transaction value, not revenue" | When revenue is unreliable, don't use it. | "When incentives are large relative to gross revenue (Tokopedia 2022: 50%), revenue is a levered residual: small incentive changes make it swing about twice as hard. That is a testable threshold." |
| "The wedge is important" | The gap is the thing at stake. | "W is what the revenue line cannot see and what policy acts on: caps on the revenue side, withholding on the transaction side." |
| "Why D instead of W?" | W is just subtraction. | "W is the size, m is how it is shared, Δln m is whether the sharing moved. Only the last is a result." |

---

## 5. The comparison the proposal never made (and the data to make it)

* **Indonesia vs abroad** is really **young-subsidised vs mature** (§2.3). The thesis should say so; Indonesia is where the cleanest young-subsidised platforms are observable and where policy is acting.
* Sea/Shopee is the pivotal firm: it is the most Indonesia-like abroad. Excluding it raises significance; including it dilutes it. Both views should be reported.

---

## 6. Evidence grades and open contradictions

| Item | Grade | Note |
|---|---|---|
| All repo-derived numbers (§2) | A | 55/55 ledger pass. |
| Cap: 20% → 8%, 1 Jul 2026, two-wheel only, Perpres 27/2026, >4m drivers | C→B | Several news reports + GoTo call summary; the Star article names a presidential regulation but no date. Need the regulation text. |
| GoTo Q2 2026: net revenue IDR 3.6tn (+20%), GTV IDR 16.7tn (+2%), "take rate 24%", guidance cut IDR 300bn, GoRide ~7% of net revenue | C | Transcript summary. 3.6 / 16.7 = 21.6%, not 24%: the "24%" may use another base. Check the primary release. |
| Grab Q2 2026: on-demand GMV US$6.5bn, mobility rev $331m / GMV $2,214m, deliveries rev $531m / GMV $4,249m, incentives $706m, incentives 10.9% of on-demand GMV | C | SEC 6-K via summary; verify raw. Cap not mentioned in the summary. |
| PMK 37/2025: 0.5% of seller turnover > Rp500m; start 1 Nov 2026 | B/C | Matches DJP deferral as reported by multiple outlets; the earlier 1 Jul / 1 Aug dates are superseded. The proposal's date is current. |
| 2026 tax shortfall / deficit 2.85% | C | Reported forecasts; confirm with Ministry of Finance. |
| WB informality 36% of GDP, ~75% employment | B | WB PRWP 10608 abstract; other sources 22–40% and ~59–60% of workers. Definition-dependent. |
| 1.6m small taxpayers vs 653k filed; Rp487tn e-commerce | C | Secondary; conflicts with BPS Rp1,289tn (different definition). |
| Durbin, NYC caps, Meituan, Amazon take rate | C | Search summaries. The JFE paper "Price regulation in two-sided markets: Empirical evidence from debit cards" is the nearest finance-journal parent (confirm authors/year). |
| Trueman–Wong–Zhang 2000; Davis 2001; Bowen–Davis–Rajgopal 2002 | B/C | Citations located; read before citing. |

Inconsistency to resolve: BPS's national e-commerce value (Rp1,289tn, 2024) vs Rp487tn used in the tax context; and platform V > BPS marketplace category. These are the "definitions don't line up" facts the proposal already flags, now with a second example.

---

## 7. Data expansion map

| Source | What it adds | Effort | Value |
|---|---|---|---|
| **Quarterly panel (47 rows in repo)** | Many more transitions; mostly Group-level and gapped | Low (exists) | Medium; scope dilution |
| **GoTo on-demand segment, quarterly (2022–2026)** | Indonesia-aligned service series, direct cap test from Q3 2026 | Medium (extract from releases) | High for F3 |
| **Grab segments and incentives, quarterly (SEC 6-K)** | Incentive intensity series (F2) | Medium | High for F2 |
| **Other listed platforms disclosing GMV/GTV + revenue**: Uber, Lyft, DoorDash, Airbnb, Booking, Delivery Hero, Meituan, Swiggy, Zomato/Eternal, MakeMyTrip, Coupang, others | Panel of ~20–30 firms × 5–10 years, many with cap/regulation episodes | High (manual KPI extraction) | Very high for F1/F8 power; yields real external validity |
| Tokopedia/TikTok Shop post-2024, Lazada | Fill the Indonesian gap | Blocked (no matched series; Lazada group-level only) | n/a |
| BPS 2025 e-commerce statistics (when published), BPS microdata | Third BPS year; seller-level formality | Low (publication) / High (microdata licence) | Medium |
| Bank Indonesia payments through 2026 | Payment growth vs BPS growth update | Low | Low-medium |
| Funding-conditions proxy (global tech funding / VC index) | F2 timing test | Low | Medium |
| Primary texts: Perpres 27/2026, PMK 37/2025, DJP deferral letter | Source-grade the policy chapter | Low | High |

---

## 8. Calendar (dated events that shape the thesis)

| Date | Event | Source grade |
|---|---|---|
| 2021–22 | Meituan commission guidance and fine; US/NYC delivery caps (2020) as precedents | C |
| 2022–23 | Funding winter; all Indonesian firms show take-rate jumps; Tokopedia −8.9% V / +53.2% R | A |
| 31 Jan 2024 | Tokopedia combined with TikTok Shop under PT Tokopedia; GoTo then reports a contractual fee | B |
| 2025 | Indonesian revenue shortfall; PMK 37/2025 issued | C |
| 1 May 2026 | Prabowo announces the 8% cap | C |
| 1 Jul 2026 | Cap in force (two-wheel); four marketplaces designated for withholding | C |
| 1 Aug 2026 | Marketplace tax start (deferred) | C |
| Aug–Sep 2026 | Marketplace tax delayed to 1 Nov; appointments revoked; refund pledge | B/C |
| 1 Oct 2026 | Proposal oral passed | known |
| ~Nov 2026 | Q3 2026 results: first post-cap quarter for GoTo and Grab (expected, unconfirmed) | D |
| 1 Nov 2026 | PMK 37 marketplace withholding start (scheduled; industry asks for Jan 2027) | B/C |
| ~Feb–Mar 2027 | FY2026 annual results | D |

---

## 9. Pivot map (which spine, which chapters)

| If the thesis is... | Spine | Supporting chapters | Biggest need |
|---|---|---|---|
| **A. "The Slice"** (default) | F1 | F2 profit pivot, F3 cap, F7 atlas, F10 closing | Panel expansion; bridges |
| **B. "Who moves the slice" (political economy)** | F3 + F5 | F1 evidence, F9 model, F2 | Q3/Q4 2026 data; regulation texts |
| **C. "What platforms show about informality"** | F4 | F1, F5, BPS H2/H3, PMK | Seller-level data; careful bounds |
| **D. "Which number do investors use"** | F6 | F1, F2 | Event study rebuilt; more firm-quarters |
| **E. "Terms and comparability"** | F7 | F1 | Wide definition atlas |
| **F. The passed proposal** | F10 | all | Rewrite for readability only |

Frames combine well: A + B + C is the "full on" version; D is a separate paper.

---

## 10. What would make it publishable rather than just passable (my judgment)

1. A single headline fact: *"In 2022–23 the revenue of Indonesia's three reporting platforms grew faster than the commerce they carried by a median of X points, mostly because incentives were cut; in 2026 the state cut the slice on one side and taxed the sale on the other."*
2. A larger, cleaner comparison group (§7) so "Indonesia vs abroad" becomes "young-subsidised vs mature" with a stage variable.
3. A policy event with pre-registered predictions (F3).
4. A model that makes the predictions non-arbitrary (F9).
5. Prose in plain, claim-first sentences (kid test) with the proxy-adequacy framework as the last chapter's lesson, not the first page's thesis.

*Not yet done:* source-grade verification of grade-C facts; primary-source text of the regulations; incentive series beyond Tokopedia and Grab; extraction for the expanded panel; contamination classification for the event study; the formatting/YZU-template audit.
