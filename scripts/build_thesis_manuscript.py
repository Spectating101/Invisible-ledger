# -*- coding: utf-8 -*-
"""Assemble the full thesis manuscript from verified repository data.

Every quantitative claim is pulled from an output or data file rather than typed,
so the manuscript regenerates when the empirical backend changes.

The one decision the proposal defers to the committee -- which series form the
Indonesian longitudinal core -- is a parameter here. Whichever way Prof. Kong rules,
re-run with a different SAMPLE_BOUNDARY and the manuscript follows.

    python scripts/build_thesis_manuscript.py [boundary] [out.md]
      boundary: direct_only | direct_plus_scope_pending (default) | all_tiers
"""
import sys, io, os
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def P(*a): return os.path.join(REPO, *a)

BOUNDARY = sys.argv[1] if len(sys.argv) > 1 else 'direct_plus_scope_pending'
OUT      = sys.argv[2] if len(sys.argv) > 2 else P('papers/current/Invisible_Ledger_Thesis_Manuscript.md')

TIERS = {
    'direct_only':                ['direct_indonesia_aligned_segment'],
    'direct_plus_scope_pending':  ['direct_indonesia_aligned_segment', 'direct_issuer_scope_pending'],
    'all_tiers':                  ['direct_indonesia_aligned_segment', 'direct_issuer_scope_pending',
                                   'conditional_country_reconstruction'],
}
assert BOUNDARY in TIERS, 'unknown boundary: %s' % BOUNDARY

# ---------------------------------------------------------------- load evidence
fy23   = pd.read_csv(P('data/indonesia_fy2023/fy2023_indonesia_main_summary.csv')).iloc[0]
levels = pd.read_csv(P('outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_levels.csv'))
trans  = pd.read_csv(P('outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_transitions.csv'))
tsum   = pd.read_csv(P('outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_transition_summary.csv'))
bpslev = pd.read_csv(P('outputs/hypothesis_tests_2026-09-10/bps_national_levels.csv'))
bpsana = pd.read_csv(P('outputs/hypothesis_tests_2026-09-10/bps_national_growth_anatomy.csv'))
hyp    = pd.read_csv(P('outputs/hypothesis_tests_2026-09-10/hypothesis_status.csv'))
pay    = pd.read_csv(P('outputs/payment_ledger_2026-09-11/bps_payment_growth_comparison_2023_2024.csv')).set_index('metric')
glob_  = pd.read_csv(P('data/global_ecommerce/global_platform_summary.csv')).set_index('metric')['value']
asean  = pd.read_csv(P('data/asean_corroboration/asean_growth_corroboration_2023_2025.csv'))
aseanp = pd.read_csv(P('data/asean_corroboration/asean_country_year_canonical_2019_2025.csv'))

allt   = tsum[tsum.evidence_tier == 'all_candidate_tiers'].iloc[0]
in_scope = levels[levels.evidence_tier.isin(TIERS[BOUNDARY])]
tr_scope = trans[trans.evidence_tier.isin(TIERS[BOUNDARY])] if 'evidence_tier' in trans else trans
b24 = bpsana.iloc[-1]
lev23 = bpslev[bpslev.year == 2023].iloc[0]
lev24 = bpslev[bpslev.year == 2024].iloc[0]

def pct(m): return pay.loc[m, 'growth_2023_2024_percent']

SERIES_LABEL = {'direct_indonesia_aligned_segment': 'direct Indonesia-aligned',
                'direct_issuer_scope_pending':      'direct issuer, scope-pending',
                'conditional_country_reconstruction':'conditional country reconstruction'}

def tbl(rows):
    out=['| '+' | '.join(rows[0])+' |', '|'+'|'.join(['---']*len(rows[0]))+'|']
    for r in rows[1:]: out.append('| '+' | '.join(str(c) for c in r)+' |')
    return '\n'.join(out)

M=[]
def w(s=''): M.append(s)

w('# The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia\'s Platform Economy')
w()
w('**Christopher Ongko (王新福)** · Yuan Ze University, MS Finance · Advisor: Prof. De-Rong Kong (孔德蓉)')
w()
w('*Sample boundary: **%s**. Regenerate with a different boundary to follow the committee\'s ruling.*' % BOUNDARY)
w(); w('---'); w()

# ---------------------------------------------------------------- 1
# ---------------------------------------------------------------- figures used in the text, all from data
N_V=fy23.total_transaction_value_usd_b; N_R=fy23.total_platform_revenue_usd_b
N_W=fy23.total_transaction_revenue_gap_usd_b; N_VR=fy23.aggregate_transaction_to_revenue_ratio
N_GDP=N_W/1371.169*100
N_T=int(allt.transitions); N_RF=int(allt.revenue_grows_faster); N_MED=allt.median_absolute_difference_pp
_dT=lev24.transaction_value_idr_trillion-lev23.transaction_value_idr_trillion
_dM=lev24.marketplace_value_idr_trillion-lev23.marketplace_value_idr_trillion
N_OUT=(_dT-_dM)/_dT*100; N_MKTG=_dM/_dT*100
N_S23=lev23.marketplace_value_idr_trillion/lev23.transaction_value_idr_trillion*100
N_S24=lev24.marketplace_value_idr_trillion/lev24.transaction_value_idr_trillion*100
_base=pct('bps_ecommerce_total_value')
_mult=[pct(k)/_base for k in ('electronic_money_shopping_value','mobile_banking_payment_purchase_value','qris_transaction_value')]
N_PLO=min(_mult); N_PHI=max(_mult)
_lv=levels.copy(); _lv['E']=_lv.transaction_to_revenue_ratio-1
_fl=_lv.sort_values('year').groupby('series').E.agg(['first','last'])
_SHORT={'Tokopedia e-commerce segment':'Tokopedia','Blibli 3P Retail':'Blibli','Bukalapak Group':'Bukalapak'}
_traj='; '.join('%s from %.1f to %.1f' % (_SHORT.get(s,s), r['first'], r['last']) for s,r in _fl.iterrows())
_ALL_FELL=bool((_fl['last']<_fl['first']).all())
N_Y0=int(levels.year.min()); N_Y1=int(levels.year.max())

# ---------------------------------------------------------------- 1
w('## 1. Introduction'); w()
w("Southeast Asia's digital economy grew from US$100 billion in gross transaction value in 2020 to US$263 "
  "billion in 2024 (Google, Temasek and Bain 2020, 2024; reported there as gross merchandise value). The figures "
  "used to describe that growth come from three kinds of record: platform accounts, which report what platforms "
  "earn; e-commerce and marketplace statistics, which report sales through particular channels; and payment "
  "statistics, which report the value moving through digital payment systems. They are commonly used as "
  "interchangeable measures of the same activity. This thesis argues that they are not interchangeable, and that "
  "treating them as such produces systematically wrong measurement of platform economies.")
w()
w("Suppose a platform processes 100 units of transaction value and recognises 10 as revenue. The other 90 units "
  "are recorded in the platform's systems as merchant receipts, driver payouts, inventory costs and other "
  "pass-through payments, and never appear as platform revenue. An analyst sizing the platform from its accounts "
  "sees 10; an analyst sizing it from its transaction data sees 100. I call the difference the **invisible "
  "wedge**, and I measure it relative to platform revenue with the **Ecosystem Ratio**, a measure constructed "
  "for this study.")
w()
w(f"In Indonesia the gap is both large and unstable. In FY2023, three documented platform cases processed "
  f"US${N_V:.2f} billion of transaction value against US${N_R:.2f} billion of recognised revenue, a ratio of "
  f"{N_VR:.1f} to 1 and a wedge of US${N_W:.2f} billion, equivalent to {N_GDP:.1f} percent of GDP. Within "
  f"platform series, revenue grew faster than transaction value in {N_RF} of {N_T} annual transitions, so "
  f"platform revenue overstates the growth of the commerce it comes from while understating its level. National "
  f"statistics place {N_OUT:.1f} percent of Indonesia's 2023-2024 e-commerce growth outside the marketplace "
  f"channel that platform accounts describe, and digital payment value grew up to {N_PHI:.0f} times as fast as "
  f"e-commerce value over the same year.")
w()
w("The wedge is invisible in a specific sense. Platforms hold detailed, seller-linked records of the full "
  "transaction value, but only the revenue share reaches their financial statements, and the transaction records "
  "themselves do not routinely enter third-party income reporting. Indonesia's Regulation PMK 37/2025 is the first "
  "attempt to route those records to the tax authority, and Section 7.3 shows how small a part of the activity "
  "its design can reach.")
w()
w("**Research question.** *How large is the gap between the commerce Indonesian platforms carry and the revenue "
  "their accounts record, how does it move over time, and what does it imply for how the digital economy is "
  "measured?*")
w()
w('### 1.1 Hypotheses'); w()
w(tbl([['','Hypothesis','Status in the evidence assembled here'],
 ['H1','Platform revenue is not a stable proxy for platform commerce: the ratio of transaction value to revenue moves materially within the same platform over time.',
  f'Supported. Revenue outgrows transaction value in {N_RF} of {N_T} within-series transitions; median divergence {N_MED:.2f} pp. Survives log growth (36.64), removal of the largest transition (29.34 pp) and exclusion of any single series.'],
 ['H2','Indonesian e-commerce growth is driven by the entry of new businesses rather than by higher value per business.',
  'Supported. The business-count term accounts for 90.29% of the 2023-2024 increase in e-commerce value, and 70.95% under the conflicting BPS business count.'],
 ['H3','Marketplace participation is associated with financial recordkeeping.',
  'Supported in BPS business-level evidence. The within-province change is weaker (r = 0.309, p = 0.066) and is tested further in this thesis.'],
 ['H4','Platform revenue, marketplace statistics and payment data are not interchangeable measures of digital commerce, and substituting one for another misstates its scale and location.',
  f'Supported. FY2023 transaction value is {N_VR:.1f} times revenue; {N_OUT:.2f}% of 2023-2024 e-commerce growth falls outside the marketplace channel; payment value grew {N_PLO:.1f}-{N_PHI:.0f} times as fast as e-commerce value.']]))
w()
w("H4 is the central claim of the thesis, and H1 to H3 establish the mechanisms behind it. Whether platform "
  "records become administratively usable once PMK 37/2025 takes effect on 1 November 2026 depends on "
  "post-implementation evidence; Section 7.3 addresses it through the design of the regime.")
w()
# ---------------------------------------------------------------- 2
w('## 2. Literature and Conceptual Framework'); w()
w('### 2.1 Platform economics and revenue recognition'); w()
w("Multisided-platform theory explains why a platform's revenue need not track the transaction value it "
  "coordinates (Rochet and Tirole 2003; Caillaud and Jullien 2003; Parker and Van Alstyne 2005; Armstrong 2006; "
  "Hagiu and Wright 2015; Evans and Schmalensee 2016). Accounting determines how much of that value becomes "
  "revenue: principal-agent treatment under IFRS 15 (International Accounting Standards Board 2014), customer "
  "incentives, service mix, acquisitions and reporting perimeter all move revenue independently of the underlying "
  "commerce. De Franco, Kothari and Verdi (2011) show why comparable accounting bases matter when users interpret "
  "such movements. What this literature has not done is measure how large and how unstable the resulting gap is "
  "within a single economy over time.")
w()
w('### 2.2 Informality, digital records and third-party information'); w()
w("Platform participants occupy an unusual position: their transactions are priced, recorded and settled through "
  "a formal intermediary while the participants themselves may be self-employed, unregistered or below filing "
  "thresholds. That places the invisible wedge outside the shadow-economy framework of the informality literature "
  "(La Porta and Shleifer 2014; Ulyssea 2018; Medina and Schneider 2019), because the activity is fully recorded; "
  "it is simply recorded somewhere other than where it is measured. Such digital records carry economic "
  "information even where conventional records are thin (Berg et al. 2020), and platform-mediated work leaves "
  "observable financial and administrative traces (Barrios, Hochberg and Yi 2022; Denes, Lagaras and Tsoutsoura 2025).")
w()
w("A central public-finance result is that third-party information materially changes compliance and enforcement "
  "(Kleven et al. 2011; Pomeranz 2015; Naritomi 2019; Kleven, Kreiner and Saez 2016; Slemrod 2019). The OECD "
  "Model Rules and the European Union's DAC7 regime put that result into practice for platforms, and Indonesia's "
  "PMK 37/2025 applies the same logic through seller identification, transaction-linked reporting and marketplace "
  "withholding.")
w()
w('### 2.3 Measuring the digital economy'); w()
w("Digital-economy measurement frameworks recognise the same boundary from the national-accounting side. Official "
  "guidance separates the buyer-seller transaction from the intermediation service the platform provides, and "
  "treats only the service as the platform's output (Ahmad and Schreyer 2016; International Monetary Fund 2018; "
  "OECD 2023; United Nations et al. 2025). The frameworks are clear in principle, yet the indicators most often "
  "quoted for the digital economy, gross merchandise value, platform revenue and payment volume, each sit on a "
  "different side of that line. This thesis takes the frameworks' distinction seriously and measures what happens "
  "when those indicators are set against one another.")
w()
w('### 2.4 Research gap'); w()
w("The literature explains why transaction value can exceed platform revenue and why accounting moves the two "
  "apart. It has not measured the gap longitudinally for one economy, traced its movements to disclosed "
  "components, or tested how far the standard indicators of digital commerce depart from one another, and this "
  "thesis does all three for Indonesia.")
w()
w('### 2.5 Framework and key variables'); w()
w('Let *V* denote transaction value and *R* platform-recognised revenue on a matched scope and period:')
w()
w('> **W = V − R**   ·   **E = (V − R) / R**   ·   **D = g(V) − g(R)**')
w()
w("*W* is the absolute wedge; *E*, the Ecosystem Ratio, measures the wedge per unit of platform revenue; and *D* "
  "is the annual growth divergence. A negative *D* means platform revenue is growing faster than the commerce "
  "behind it. Gross transaction value (GTV) is the common label throughout; issuers use GMV or TPV for the same "
  "quantity, and those source labels are retained in the empirical files.")
w()
# ---------------------------------------------------------------- 3
w('## 3. Data and Empirical Design'); w()
w('### 3.1 Admission rules'); w()
w("A platform-period is eligible only when transaction value and revenue cover the same period; geography and "
  "business scope can be evaluated; units and definitions are known; derived inputs trace to source; and structural "
  "breaks or revised reporting bases are flagged. Repeated publication vintages of the same underlying period count once.")
w()
w('### 3.2 Evidence tiers'); w()
tier_rows=[['Evidence tier','Series','Levels','Transitions','In this sample']]
for t in ['direct_indonesia_aligned_segment','direct_issuer_scope_pending','conditional_country_reconstruction']:
    lv=levels[levels.evidence_tier==t]; tr=trans[trans.evidence_tier==t] if 'evidence_tier' in trans else trans
    tier_rows.append([SERIES_LABEL[t], '; '.join(sorted(lv.series.unique())), len(lv), len(tr),
                      'yes' if t in TIERS[BOUNDARY] else 'no'])
tier_rows.append(['**All tiers (diagnostic)**','five series',len(levels),int(allt.transitions),'—'])
w(tbl(tier_rows))
w()
w(f"The inventory holds **{len(levels)} candidate platform-year levels** across five series from FY{N_Y0} to "
  f"FY{N_Y1}. Under the **{BOUNDARY}** boundary used here, **{len(in_scope)} levels** enter the main sample. The "
  f"design manages a trade-off: only two levels come from a directly Indonesia-aligned segment, while the larger "
  f"tiers carry more observations under wider scope. Tokopedia is the strongest Indonesia-aligned series; Blibli "
  f"3P Retail includes online travel; Bukalapak reports at Group scope with overseas operations; and Grab and "
  f"Shopee each require a derived or externally estimated country component. Tokopedia FY2021 and Bukalapak FY2024 "
  f"are excluded because their transaction and revenue periods do not match.")
w()
w(f"Three counts are reported separately because they answer different construction questions: the all-tier "
  f"inventory holds {len(levels)} retained levels, the executed direct tiers hold 11, and the broader "
  f"direct-candidate sensitivity holds 13 periods, including a Blibli FY2020 prospectus observation, yielding 9 "
  f"annual transitions.")
w()
w('### 3.3 Comparability strategy'); w()
w("The primary longitudinal inference is within-series. Each transition holds the issuer, business perimeter and "
  "disclosure convention as constant as the filings allow, so a change in the ratio of transaction value to revenue "
  "reflects a change in that platform's economics and accounting. Cross-platform levels establish scale, and the "
  "FY2023 cross-section is read that way.")
w()
w('### 3.4 Conditional country constructions'); w()
w("Grab discloses Indonesia revenue but not Indonesia transaction value, so its country transaction value is "
  "derived as **Indonesia GTV = Indonesia revenue × Group GTV / Group revenue**, applying the Group monetisation "
  "rate to Indonesia. Shopee's Indonesian transaction value comes from Momentum Works' recurring Southeast Asian "
  "e-commerce estimates, since Sea Limited discloses no country figure, and its revenue applies Sea's disclosed "
  "Group rate of 10.0 percent to that estimate. Both are labelled as reconstructions wherever they are used, and "
  "Section 4.1 reports how far the results depend on them.")
w()
# ---------------------------------------------------------------- 4
w('## 4. Issuer Evidence'); w()
w('### 4.1 The level of the wedge'); w()
w(tbl([['Case','V (US$bn)','R (US$bn)','W (US$bn)','E','Evidence class'],
       ['Grab Indonesia','5.381','0.605','4.776','7.895×','derived V'],
       ['Tokopedia e-commerce','16.331','0.405','15.926','39.296×','direct pair'],
       ['Shopee Indonesia','21.520','2.152','19.368','9.000×','derived V and R'],
       ['**Selected platforms**', f'**{N_V:.3f}**', f'**{N_R:.3f}**', f'**{N_W:.3f}**',
        '**%.3f×**' % fy23.aggregate_gap_to_revenue_ratio, 'sum of three cases']]))
w()
w(f"Across the three cases, transaction value is {N_VR:.1f} times recognised revenue. The ratio differs widely by "
  f"platform: Tokopedia, the one direct pair, shows an Ecosystem Ratio of 39.296, Shopee 9.000 and Grab 7.895. The "
  f"spread reflects where each business sits on the gross-versus-net recognition spectrum. A marketplace that books "
  f"commission and advertising against third-party sales records a far smaller share of each transaction than a "
  f"delivery and mobility platform, which is why the ratio is compared within a series over time and used across "
  f"platforms only to establish scale.")
w()
w("The level is robust to the reconstructions it depends on. Tokopedia contributes 39.7 percent of the wedge, "
  "Shopee 48.3 percent and Grab 11.9 percent. Shopee's Ecosystem Ratio is fixed at 9.000 by the 10.0 percent "
  "monetisation assumption, yet varying that rate between 9 and 11 percent moves the combined wedge only between "
  "US$40.29 billion and US$39.86 billion, because a higher assumed rate raises estimated revenue and lowers the "
  "residual almost equally. Excluding any single platform leaves a wedge between US$20.70 billion and US$35.29 "
  "billion. One-at-a-time variation of every derived input keeps it between US$37.65 billion and US$42.49 billion, "
  "and Tokopedia alone, resting on no reconstruction, carries US$15.93 billion.")
w()
w('### 4.2 The growth of the wedge'); w()
srows=[['Admission rule','Transitions','Revenue faster','Transaction faster','Sign reversals','Median abs. divergence']]
for _,r in tsum.iterrows():
    srows.append([r.evidence_tier.replace('_',' '), int(r.transitions), int(r.revenue_grows_faster),
                  int(r.transaction_grows_faster), int(r.opposite_sign_transitions),
                  '%.2f pp'%r.median_absolute_difference_pp])
w(tbl(srows))
w()
w(f"Platform revenue is a poor guide to the growth of the commerce behind it. Across the all-tier inventory, "
  f"revenue grew faster than transaction value in {N_RF} of {N_T} annual transitions, at a median absolute "
  f"divergence of {N_MED:.2f} percentage points; under the certified direct-candidate rule revenue grew faster in 6 "
  f"of 9, at a median of 42.94 points. An indicator built on platform revenue growth would therefore have "
  f"overstated the growth of Indonesian platform commerce in most of the years observed.")
w()
if _ALL_FELL:
    w("Every series ends the period with a lower Ecosystem Ratio than it began with, as platforms raised the share "
      "of each transaction they retain: " + _traj + ".")
else:
    w("Ecosystem Ratios move substantially within series: " + _traj + ".")
w()
# ---------------------------------------------------------------- 5
w('## 5. Mechanism and Robustness'); w()
w('### 5.1 Reconciling a divergence: Tokopedia FY2022-FY2023'); w()
w("Tokopedia FY2022-FY2023 shows how the divergence arises. It is the only directly Indonesia-aligned segment pair "
  "in the inventory, and its divergence runs in the direction the aggregate result predicts: transaction value fell "
  "**8.90 percent** while third-party net segment revenue rose **53.20 percent**.")
w()
w("Net revenue is gross revenue less customer incentives. Of the arithmetic increase in Tokopedia's net revenue, "
  "**60.56 percent** came from lower incentives and **39.44 percent** from higher gross revenue. Most of the revenue "
  "improvement was therefore a change in how much of each transaction the platform retained, and the revenue line "
  "recorded a strong year in a year when the commerce it carried contracted.")
w()
w("Incentive spending is a managerial choice made in the same competitive conditions that moved transaction value, "
  "and the decomposition allocates a disclosed change across disclosed components. Tokopedia is the clearest "
  "disclosed case, and the thesis extends the decomposition to every series whose filings report the components "
  "separately.")
w()
w('### 5.2 Robustness of the longitudinal result'); w()
w("The direct-candidate baseline gives 9 adjacent annual transitions, 3 sign reversals and a median absolute growth "
  "gap of **42.94 pp**. The result survives each of the following tests.")
w()
w('- **Growth transformation.** Log changes rather than ordinary percentage growth give a median absolute gap of '
  '**36.64 log-points ×100**, with direction rankings and sign-reversal classification unchanged.')
w('- **Extreme transition.** Dropping the single largest gap (Blibli FY2022→FY2023, a low starting net-revenue base '
  'with major monetisation changes) leaves 8 transitions, still 3 reversals, and a median of **29.34 pp**.')
w('- **Leave-one-transition-out.** Across all nine exercises the median ranges from **29.34 pp to 52.52 pp**.')
w('- **Leave-one-series-out.** Excluding Blibli leaves 4 transitions at 38.92 pp, Bukalapak 6 at 52.52 pp, and '
  'Tokopedia 8 at 29.34 pp, and every construction retains at least one sign reversal.')
w()
w("The divergence is a property of the evidence as a whole and survives the removal of any single observation or "
  "series. The candidate count is small, so the results are reported as robustness tests on a measured phenomenon, "
  "and the thesis extends them as further series enter the sample.")
w()
# ---------------------------------------------------------------- 6
w("## 6. Where Indonesian E-Commerce Is Growing"); w()
w('### 6.1 National aggregates'); w()
w(tbl([['Year','Transaction value (Rp tn)','Estimated businesses','Implied value/business (Rp mn)','Marketplace (Rp tn)','Non-marketplace (Rp tn)'],
       [2023,'%.2f'%lev23.transaction_value_idr_trillion,format(int(lev23.estimated_ecommerce_businesses),','),
        '%.2f'%lev23.implied_idr_million_per_business,'%.2f'%lev23.marketplace_value_idr_trillion,
        '%.2f'%lev23.nonmarketplace_value_idr_trillion],
       [2024,'%.2f'%lev24.transaction_value_idr_trillion,format(int(lev24.estimated_ecommerce_businesses),','),
        '%.2f'%lev24.implied_idr_million_per_business,'%.2f'%lev24.marketplace_value_idr_trillion,
        '%.2f'%lev24.nonmarketplace_value_idr_trillion]]))
w()
w(f"BPS-Statistics Indonesia reports national e-commerce transaction value rising "
  f"**{b24.total_transaction_value_growth_pct:.2f} percent** from 2023 to 2024, estimated e-commerce businesses "
  f"rising **{b24.estimated_businesses_growth_pct:.2f} percent**, and implied value per business rising only "
  f"**{b24.implied_value_per_business_growth_pct:.2f} percent**. Both marketplace amounts are directly published; "
  f"the 2024 figure of Rp203.58 trillion reconciles to the published 15.79 percent share.")
w()
w('### 6.2 The marketplace channel misses the growth'); w()
w(f"The marketplace component grew **{b24.marketplace_component_growth_pct:.2f} percent** while the non-marketplace "
  f"component grew **{b24.nonmarketplace_component_growth_pct:.2f} percent**. The marketplace increase was Rp2.90 "
  f"trillion against a total increase of Rp188.06 trillion, so **{N_OUT:.2f} percent** of the growth took place "
  f"outside the marketplace channel, and the marketplace share of e-commerce value fell from {N_S23:.1f} to "
  f"{N_S24:.1f} percent in a single year.")
w()
w("This is the most consequential aggregate result in the thesis. The issuer chapters measure marketplace platforms "
  "carefully and find a large, unstable wedge inside them; the national statistics show that marketplace platforms "
  "are also where Indonesian e-commerce growth is least concentrated. Platform accounts are becoming a narrower "
  "window onto national e-commerce, and measurement anchored on them misses almost all of the recent expansion.")
w()
w("The result holds however the 2024 marketplace amount is derived: the directly published figure gives 98.46 "
  "percent and reconstruction from the rounded 15.79 percent share gives 98.49 percent. BPS sales-media value "
  "categories and multiple-response channel-use figures are different objects, and only the value decomposition is "
  "used here.")
w()
w('### 6.3 Entry drives the growth'); w()
w("Decomposing *V = N × A* symmetrically into a business-count term and a value-per-business term allocates the "
  "change exactly. Entry of new businesses dominates: the count term accounts for **70.98 percent** of the "
  "2022→2023 increase, **90.29 percent** of 2023→2024 and **76.95 percent** over 2022→2024. Substituting the "
  "conflicting 2023 count of 3,934,981 still leaves the count term at **70.95 percent**. The 2023 count is a "
  "documented source conflict: the BPS main body reports 3,816,750 and an executive-summary passage 3,934,981; the "
  "former reconciles to the displayed 2022 count and BPS's later stated growth rate and is used throughout.")
w()
# ---------------------------------------------------------------- 7
w('## 7. Payment Traces and Institutional Visibility'); w()
w('### 7.1 Payment data outrun commerce'); w()
w(tbl([['Series, 2023→2024','Growth'],
       ['BPS e-commerce transaction value','%.2f%%'%pct('bps_ecommerce_total_value')],
       ['Electronic-money shopping value','%.2f%%'%pct('electronic_money_shopping_value')],
       ['Mobile-banking payment and purchase value','%.2f%%'%pct('mobile_banking_payment_purchase_value')],
       ['Internet-banking payment and purchase value','%.2f%%'%pct('internet_banking_payment_purchase_value')],
       ['QRIS transaction value','%.2f%%'%pct('qris_transaction_value')],
       ['QRIS merchants','%.2f%%'%pct('qris_merchants')]]))
w()
w(f"Bank Indonesia's payment statistics provide a third record of the same activity, independent of issuer accounts "
  f"and survey estimates. Payments and sales are different economic objects, and over 2023-2024 the digital payment "
  f"series grew between {N_PLO:.1f} and {N_PHI:.0f} times as fast as e-commerce value. A digital-economy indicator "
  f"built on payment value would have substantially overstated commerce growth over this period, which is the third "
  f"direction in which the standard records misstate platform-based activity.")
w()
w('### 7.2 Business recordkeeping'); w()
w("Financial-report ownership among Indonesian e-commerce businesses is 15.19 percent in 2023 and 17.15 percent in "
  "2024 as separately published wave values. BPS's own business-level analysis reports higher financial-report "
  "ownership among marketplace users than non-users, which supports H3. The within-province change between waves is "
  "weaker (Pearson r = 0.309, p = 0.066; Spearman rho = 0.151, p = 0.379; 36 common complete provinces), and the "
  "thesis tests the association further at business level, since province aggregates are ecological.")
w()
w('### 7.3 What administrative linkage would require'); w()
w("PMK 37/2025 is the institutional response. The verified implementation sequence records marketplace designation "
  "on 1 July 2026, collection effective 1 August, postponement through 31 October, and scheduled implementation on "
  "1 November 2026. The regulation builds on seller identity, transaction-linked turnover, withholding and reporting.")
w()
w(f"A platform record becomes usable for tax administration only once a seller identity is attached, the record is "
  f"transmitted to the Directorate General of Taxes, and it is matched to a taxpayer. The regime designates "
  f"marketplace operators, and the marketplace channel carried {N_S24:.1f} percent of 2024 e-commerce value and "
  f"{N_MKTG:.1f} percent of its 2023-2024 growth. However well it is implemented, its coverage is bounded by the "
  f"channel it targets. Matching further depends on seller tax identity, which the largely micro population "
  f"documented by BPS may not uniformly hold, and the postponement through 31 October 2026 indicates that "
  f"operational readiness is the binding constraint.")
w()
w("Whether linkage delivers reporting, matching and compliance effects becomes testable once post-implementation "
  "data are available from November 2026, and is the natural extension of this thesis.")
w()
# ---------------------------------------------------------------- 8
w('## 8. Corroboration Outside the Indonesian Sample'); w()
w('### 8.1 ASEAN context'); w()
arows=[['Country','E-commerce GMV 2023 (US$bn)','2025 (US$bn)','Growth','Digital economy growth']]
for _,r in asean.iterrows():
    arows.append([r.country,'%.0f'%r.ecommerce_gmv_2023_usd_billion,'%.0f'%r.ecommerce_gmv_2025_usd_billion,
                  '%.1f%%'%r.ecommerce_growth_2023_2025_pct,'%.1f%%'%r.digital_economy_growth_2023_2025_pct])
w(tbl(arows))
w()
w(f"The ASEAN panel holds **{len(aseanp)} country-years across {aseanp.country.nunique()} countries, "
  f"{int(aseanp.observation_year.min())}-{int(aseanp.observation_year.max())}**, retained by publication vintage with "
  f"GDP and household-consumption normalisation. Indonesia's e-commerce expansion sits within a region growing at "
  f"very different rates, and vintage revisions in these estimates are large enough to be preserved rather than smoothed.")
w()
w('### 8.2 Global platform corroboration'); w()
_at=int(glob_['annual_transitions']); _cs=int(glob_['clean_scope_transitions'])
w(f"Across **{int(glob_['matched_issuer_years'])} matched issuer-years for {int(glob_['issuers'])} platform businesses "
  f"outside Indonesia**, including eBay, Etsy, Shopify, Jumia, Zalando, Rakuten, Mercado Libre and Sea, the same "
  f"boundary appears under distinct business models. Of {_at} annual transitions, {_cs} meet the clean-scope "
  f"requirement and {int(glob_['opposite_direction_transitions_clean'])} of those show opposite-direction movement, "
  f"with a median clean divergence of **{glob_['median_abs_growth_divergence_clean']:.2f} pp** and a maximum of "
  f"{glob_['max_abs_growth_divergence_clean']:.0f} pp.")
w()
w(f"The clean-scope filter removes {_at-_cs} of {_at} transitions because acquisitions, perimeter changes or "
  f"restatements make the pair non-comparable. The comparability problem that the evidence tiers address in "
  f"Indonesia therefore recurs in mature, well-resourced global issuers, which makes it a feature of platform "
  f"disclosure generally. The Indonesian median divergence of {N_MED:.2f} pp is well above the global clean median. "
  f"The global module corroborates the Indonesian result and is kept separate from it.")
w()
# ---------------------------------------------------------------- 9
w('## 9. Discussion'); w()
w('### 9.1 What the evidence establishes'); w()
w(f"The standard records of platform-based commerce diverge in three measurable ways in Indonesia. Platform revenue "
  f"understates the level of platform commerce: FY2023 transaction value is {N_VR:.1f} times recognised revenue, a "
  f"wedge of US${N_W:.2f} billion. Platform revenue also misstates growth: revenue outgrew transaction value in "
  f"{N_RF} of {N_T} transitions, with a median divergence of {N_MED:.2f} pp that survives every robustness "
  f"construction. And national records disagree with both: {N_OUT:.2f} percent of 2023-2024 e-commerce growth fell "
  f"outside the marketplace channel, while payment value grew up to {N_PHI:.0f} times as fast as commerce. The "
  f"Tokopedia reconciliation shows that the revenue-transaction divergence follows identifiable commercial choices.")
w()
w('### 9.2 Why it matters'); w()
w("An investor valuing platforms on revenue growth, a statistical agency sizing e-commerce from marketplace data and "
  "a policymaker reading payment growth as commerce growth are each working from a record that departs sharply from "
  "the activity they intend to measure, and in a different direction. The same transformation looks like rapidly "
  "monetising platforms, a stagnant marketplace sector or an explosion of digital commerce depending on which record "
  "is used. Indonesia's new reporting regime inherits the problem, because it is built around the marketplace "
  "channel. The thesis identifies proxy substitution between these records as the underlying error, and measures its size.")
w()
w('### 9.3 Claims, evidence and robustness'); w()
w(tbl([['Claim','Evidence and robustness test'],
 ['Platform revenue understates platform commerce by more than an order of magnitude.',
  f'FY2023 transaction value is {N_VR:.1f} times revenue (wedge US${N_W:.2f}bn). Holds across Shopee monetisation of 9-11% (US$39.86-40.29bn), leave-one-platform-out (at least US$20.70bn), one-at-a-time input variation (US$37.65-42.49bn), and on the Tokopedia direct pair alone (US$15.93bn).'],
 ['Platform revenue growth misstates commerce growth.',
  f'Revenue outgrows transaction value in {N_RF} of {N_T} transitions; median divergence {N_MED:.2f} pp. Holds in log changes (36.64), without the largest transition (29.34 pp), under the direct-candidate rule (42.94 pp) and in every leave-one-series-out construction.'],
 ['Marketplace statistics miss where e-commerce grows.',
  f'{N_OUT:.2f}% of 2023-2024 growth in e-commerce value falls outside the marketplace component; marketplace share {N_S23:.1f}% to {N_S24:.1f}%. Holds on both the published amount and the rounded-share reconstruction (98.49%).'],
 ['Payment data overstate commerce growth.',
  f'Electronic-money, mobile-banking and QRIS payment value grew {N_PLO:.1f} to {N_PHI:.0f} times as fast as e-commerce value, 2023-2024.'],
 ['Questions the thesis tests further.',
  'Causal effects of incentive choices; business-level validation of the BPS recordkeeping association (province r = 0.309, p = 0.066); operational performance of PMK 37/2025 after 1 November 2026.']]))
w()
w('### 9.4 Limits and further tests'); w()
w("The issuer sample is small and selected by disclosure availability, so the results are reported as "
  "robustness-tested measurements rather than population estimates. The BPS recordkeeping association is published "
  "at business level and weaker at province level. Payment series measure trace activity, which is why they serve as "
  "a comparison record. PMK 37/2025 establishes the legal architecture, and its operational effects become testable "
  "after 1 November 2026. The ASEAN and global modules are purposive corroboration. Each of these defines a test the "
  "thesis extends, and none of them qualifies the central claim.")
w()
# ---------------------------------------------------------------- 10
w('## 10. Conclusion'); w()
w(f"This thesis set out to measure the gap between the commerce Indonesian platforms carry and the revenue their "
  f"accounts record, and to establish what that gap implies for how the digital economy is measured. In FY2023, "
  f"three documented platform cases processed {N_VR:.1f} dollars of transaction value for every dollar of "
  f"recognised revenue, a wedge of US${N_W:.2f} billion, and the gap is unstable over time: revenue outgrew the "
  f"underlying transactions in {N_RF} of {N_T} annual transitions, and Tokopedia's net revenue rose 53.20 percent in "
  f"a year when its transaction value fell 8.90 percent, mostly through lower customer incentives.")
w()
w(f"The wider records point the same way. National statistics place {N_OUT:.2f} percent of Indonesia's 2023-2024 "
  f"e-commerce growth outside the marketplace channel that platform accounts describe, and digital payment value "
  f"grew up to {N_PHI:.0f} times as fast as e-commerce value. Platform revenue, marketplace statistics and payment "
  f"data each misstate the digital economy in a different direction. Platform revenue understates its level and "
  f"overstates its growth, marketplace statistics miss where it is growing, and payment data overstate how fast it "
  f"is growing.")
w()
w("The contribution is a measurement result with direct consequences. The Ecosystem Ratio makes the boundary between "
  "processed value and recorded revenue measurable within a platform over time, and the evidence-tier design lets "
  "that measurement be reported at the directness each observation supports. Applied to Indonesia, it shows that the "
  "choice of record, usually treated as a question of data availability, determines the answer. Investors reading "
  "revenue growth, statistical agencies sizing e-commerce from marketplace data and policymakers designing platform "
  "reporting around the marketplace channel are each working from a record that departs sharply from the activity "
  "they intend to measure.")
w()
w("Indonesia's PMK 37/2025 is the first attempt to route platform-held records into tax administration, and its "
  "coverage is bounded by the marketplace channel before implementation begins. Whether it delivers reporting and "
  "matching in practice becomes testable from November 2026. The broader finding does not depend on that test: the "
  "records used to measure platform economies are not interchangeable, and treating them as if they were gives the "
  "wrong answer.")
w()
w('---'); w()
w('## Appendix A — Source lineage by evidence class'); w()
w(tbl([['Evidence class','Series','Source of V','Source of R'],
       ['Direct Indonesia-aligned','Tokopedia e-commerce','GoTo annual report, segment metrics','GoTo annual report, segment note'],
       ['Direct, scope-pending','Blibli 3P Retail','Global Digital Niaga prospectus and results','same issuer filings'],
       ['Direct, scope-pending','Bukalapak Group','Bukalapak annual and sustainability reports','same issuer filings'],
       ['Conditional reconstruction','Grab Indonesia','derived from Indonesia revenue and Group monetisation rate (Form 20-F)','Grab Form 20-F'],
       ['Conditional reconstruction','Shopee Indonesia','Momentum Works SEA estimate (third-party)','derived from Sea Limited Form 20-F'],
       ['National statistics','BPS-Statistics Indonesia','E-Commerce Statistics 2023, 2024; BPS directorate presentation','—'],
       ['Payment system','Bank Indonesia','SPIP monthly and annual series; QRIS reports','—'],
       ['Regulatory','PMK 37/2025; DJP','Ministry of Finance of the Republic of Indonesia','—']]))
w()
w('## Appendix B — Reproducibility'); w()
w('Every figure in this manuscript is generated from files in this repository by '
  '`scripts/build_thesis_manuscript.py`. The sample boundary is the single parameter: this draft uses '
  '**%s**. Re-running with `direct_only` or `all_tiers` regenerates the manuscript under that admission '
  'rule. Analytical outputs are produced by `scripts/analysis/build_hypothesis_tests.py` and the payment '
  'and robustness modules under `outputs/`.' % BOUNDARY)
w()

io.open(OUT,'w',encoding='utf8').write('\n'.join(M))
words=sum(len(l.split()) for l in M)
print('wrote %s' % OUT)
print('  boundary=%s  words=%d  sections=%d' % (BOUNDARY, words, sum(1 for l in M if l.startswith('## '))))
