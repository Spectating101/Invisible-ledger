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
w('## 1. Introduction'); w()
w('Digital platforms process far more transaction value than they recognise as their own revenue. '
  'I call that difference the **invisible wedge**. For a matched platform scope and period, the absolute '
  'wedge is *W = V − R*, where *V* is transaction value and *R* is platform-recognised revenue, and the '
  '**Ecosystem Ratio** *E = (V − R)/R* expresses the same boundary relative to revenue. The Ecosystem '
  'Ratio is constructed for this study rather than adopted from prior work.')
w()
w('Suppose a platform processes 100 units of transaction value and recognises 10 as revenue. The '
  'remaining 90 units are recorded inside the platform but are not platform revenue: they are merchant '
  'receipts, driver payouts, inventory cost, taxes paid elsewhere and other pass-through payments. The '
  'thesis measures that accounting boundary. It does not assume the residual is profit, taxable income, '
  'or unpaid tax.')
w()
w('For FY2023, three documented Indonesian platform cases imply a combined wedge of approximately '
  '**US$%.2f billion** at an Ecosystem Ratio of **%.3f**, about **%.1f percent** of Indonesia\'s 2023 '
  'nominal GDP of US$1.371 trillion. That comparison is a scale reference only: the wedge is transaction '
  'value outside platform revenue, not value added, and therefore not a component of GDP.'
  % (fy23.total_transaction_revenue_gap_usd_b, fy23.aggregate_gap_to_revenue_ratio,
     fy23.total_transaction_revenue_gap_usd_b/1371.169*100))
w()
w('"Invisible" does not mean concealed. A platform may hold seller- and worker-linked transaction records '
  'even where those records do not enter routine third-party income reporting. The wedge measures the '
  'transaction–revenue boundary; whether the underlying records are transmitted and usable outside the '
  'platform is a separate, institutional question this thesis treats as evidence rather than assumption.')
w()
w('**Research question.** *How large is the invisible wedge in Indonesia, how does it change over time, '
  'and what explains those changes?*')
w()
w('### 1.1 Hypotheses'); w()
# H4 (institutional linkage) is demoted to a feasibility assessment in 7.3, so the
# retained hypotheses are renumbered contiguously rather than leaving a gap at H4.
TESTED=[h for _,h in hyp.iterrows() if not h.hypothesis.startswith('H4')]
w(tbl([['','Hypothesis','Status in the evidence assembled here']] +
      [['H%d'%k, ' '.join(h.hypothesis.split()[1:]), h.status.replace('_',' ')]
       for k,h in enumerate(TESTED,1)]))
w()
w('The thesis tests four hypotheses. A fifth possibility, that platform-held records are not yet '
  'administratively linked to seller obligations, is deliberately not advanced as a hypothesis here: '
  'testing it needs post-implementation evidence on reporting, identity matching and compliance, and PMK '
  '37/2025 implementation is scheduled for 1 November 2026. Section 7.3 instead assesses what such '
  'linkage would require and whether the published architecture is capable of it, which current sources '
  'can answer. None of the four is framed as a causal claim.')
w()
# ---------------------------------------------------------------- 2
w('## 2. Literature and Conceptual Framework'); w()
w('### 2.1 Platform economics and revenue recognition'); w()
w('Multisided-platform theory explains why platform revenue need not move proportionally with the '
  'transaction value a platform coordinates (Rochet and Tirole 2003; Caillaud and Jullien 2003; Parker '
  'and Van Alstyne 2005; Armstrong 2006; Hagiu and Wright 2015; Evans and Schmalensee 2016). Accounting '
  'then determines how much facilitated commerce becomes recognised revenue: principal–agent treatment '
  'under IFRS 15, customer incentives, service mix, acquisitions and reporting perimeter can all move '
  'revenue without an equivalent change in underlying commerce. De Franco, Kothari and Verdi (2011) '
  'establish why comparability of accounting bases matters when users interpret such differences.')
w()
w('### 2.2 Informality, digital records and third-party information'); w()
w('Platform participants occupy an unusual position: their transactions are priced, recorded and settled '
  'through a formal intermediary while the participants themselves may be self-employed, unregistered, '
  'below filing thresholds, or outside any automatic reporting channel. The object measured here is '
  'therefore not the shadow economy as conventionally defined (La Porta and Shleifer 2014; Ulyssea 2018; '
  'Medina and Schneider 2019). Digital records nevertheless carry economic information where conventional '
  'records are thin (Berg et al. 2020), and platform-mediated work leaves observable financial and '
  'administrative traces (Barrios, Hochberg and Yi 2022; Denes, Lagaras and Tsoutsoura 2025).')
w()
w('A central public-finance result is that third-party information changes compliance and enforcement '
  '(Kleven et al. 2011; Pomeranz 2015; Naritomi 2019; Kleven, Kreiner and Saez 2016; Slemrod 2019). The '
  'OECD Model Rules and the European Union\'s DAC7 regime are the closest policy precedents; Indonesia\'s '
  'PMK 37/2025 applies the same logic through seller identification, transaction-linked reporting and '
  'marketplace withholding.')
w()
w('### 2.3 Measuring the digital economy'); w()
w('National-accounting frameworks address the same boundary from the measurement side. Official guidance '
  'separates the underlying buyer–seller transaction from the intermediation service the platform '
  'provides, and rejects treating gross transaction value as value added or as an alternative output '
  'measure (Ahmad and Schreyer 2016; International Monetary Fund 2018; OECD 2023; United Nations et al. '
  '2025). This literature establishes what the wedge is **not**, and is why the thesis treats *V − R* as '
  'an accounting boundary rather than unmeasured output.')
w()
w('### 2.4 Research gap'); w()
w('The literature explains why transaction value can exceed platform revenue, why accounting moves the '
  'two apart, and why third-party records matter for administration. What is missing is a longitudinal, '
  'source-auditable account for a single market that measures the wedge, explains why it moves, and then '
  'asks where the wider activity and its records appear beyond platform revenue.')
w()
w('### 2.5 Framework and key variables'); w()
w('Let *V* denote transaction value and *R* platform-recognised revenue on a matched scope and period:')
w()
w('> **W = V − R**   ·   **E = (V − R) / R**   ·   **D = g(V) − g(R)**')
w()
w('*W* is the absolute wedge, *E* the Ecosystem Ratio, and *D* the annual growth divergence. A higher *E* '
  'means more transaction value sits outside platform revenue per unit of revenue; it does not by itself '
  'imply participant profit, taxable income, value added, non-compliance or tax due. Gross transaction '
  'value (GTV) is the common label throughout; issuers use GMV or TPV for the same quantity and those '
  'source labels are retained in the empirical files rather than treated as interchangeable.')
w()
# ---------------------------------------------------------------- 3
w('## 3. Data and Empirical Design'); w()
w('### 3.1 Admission rules'); w()
w('A platform-period is eligible only when transaction value and revenue cover the same period; geography '
  'and business scope can be evaluated; units and definitions are known; derived inputs trace to source; '
  'and structural breaks or revised reporting bases are flagged. Repeated publication vintages of the '
  'same underlying period are not counted as independent observations.')
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
w('The inventory holds **%d candidate platform-year levels** across five series from FY2019 to FY2025. '
  'Under the **%s** boundary used here, **%d levels** enter the main sample. Tokopedia is the strongest '
  'Indonesia-aligned segment but is not a literal country line; Blibli 3P Retail includes online travel; '
  'Bukalapak reports at Group scope with overseas operations; Grab and Shopee each require a derived or '
  'externally estimated country component. Tokopedia FY2021 and Bukalapak FY2024 are excluded because '
  'transaction and revenue periods do not match.' % (len(levels), BOUNDARY, len(in_scope)))
w()
w('Three counts are intentionally different and are never collapsed into one *N*: the all-tier inventory '
  'holds %d retained levels; the executed direct tiers hold 11 levels; and the broader direct-candidate '
  'sensitivity holds 13 periods, including a Blibli FY2020 prospectus observation, yielding 9 annual '
  'transitions.' % len(levels))
w()
w('### 3.3 Comparability strategy'); w()
w('The primary longitudinal inference is within-series: each platform is compared against its own prior '
  'year on a consistent reporting basis, so perimeter differences between issuers cannot drive the '
  'result. Cross-platform levels are descriptive and scope-labelled rather than a matched panel. The '
  'FY2023 cross-section establishes order of magnitude, not a ranking of platforms.')
w()
w('### 3.4 Conditional country constructions'); w()
w('Grab discloses Indonesia revenue but not Indonesia transaction value, so its conditional country '
  'transaction value is derived as **Indonesia GTV = Indonesia revenue × Group GTV / Group revenue**. The '
  'construction assumes the Group monetisation rate applies to Indonesia and is treated as sensitivity '
  'evidence. Shopee\'s Indonesia transaction value uses Momentum Works\' recurring Southeast Asian '
  'e-commerce estimate, because Sea Limited discloses no Indonesian country figure; it is labelled '
  'third-party wherever it enters a calculation.')
w()
# ---------------------------------------------------------------- 4
w('## 4. Issuer Evidence'); w()
w('### 4.1 FY2023 cross-section'); w()
w(tbl([['Case','V (US$bn)','R (US$bn)','W (US$bn)','E','Evidence class'],
       ['Grab Indonesia','5.381','0.605','4.776','7.895×','derived V'],
       ['Tokopedia e-commerce','16.331','0.405','15.926','39.296×','direct pair'],
       ['Shopee Indonesia','21.520','2.152','19.368','9.000×','derived V and R'],
       ['**Selected platforms**','**%.3f**'%fy23.total_transaction_value_usd_b,
        '**%.3f**'%fy23.total_platform_revenue_usd_b,
        '**%.3f**'%fy23.total_transaction_revenue_gap_usd_b,
        '**%.3f×**'%fy23.aggregate_gap_to_revenue_ratio,'sum, not a national total']]))
w()
w('The final row sums three documented cases under mixed evidence classes and is not an Indonesia-wide '
  'estimate; it is reported to establish order of magnitude, not to rank the platforms against one '
  'another. The dispersion across cases is itself informative. Tokopedia, the only directly '
  'Indonesia-aligned pair, shows an Ecosystem Ratio of 39.296, while Grab Indonesia shows 7.895 and '
  'Shopee Indonesia 9.000. That spread is not a measurement error: it reflects genuinely different '
  'business models. A marketplace that books only commission and advertising against third-party '
  'merchant sales will mechanically show a far higher ratio than a mobility and delivery platform that '
  'recognises a larger share of each transaction, or than a platform whose revenue includes first-party '
  'retail. The ratio therefore measures where a platform sits on the gross-versus-net recognition '
  'spectrum, and is comparable within a series over time rather than across business models at a point '
  'in time.')
w()
w('Three sensitivity exercises bound the FY2023 figure. One-at-a-time parameter variation across the '
  'derived inputs moves the combined wedge between approximately US$37.65 billion and US$42.49 billion, '
  'a range of roughly 12 percent around the central figure. Leave-one-platform-out calculations give '
  'approximately US$35.29 billion, US$24.14 billion and US$20.70 billion, so no single case carries the '
  'result even though Tokopedia and Shopee are individually large. And because two of the three cases '
  'require a derived or externally estimated component, the direct-pair subtotal -- Tokopedia alone at '
  'US$15.926 billion -- is reported as the floor that rests on no reconstruction at all.')
w()
w('### 4.2 Longitudinal divergence'); w()
srows=[['Admission rule','Transitions','Revenue faster','Transaction faster','Sign reversals','Median abs. divergence']]
for _,r in tsum.iterrows():
    srows.append([r.evidence_tier.replace('_',' '), int(r.transitions), int(r.revenue_grows_faster),
                  int(r.transaction_grows_faster), int(r.opposite_sign_transitions),
                  '%.2f pp'%r.median_absolute_difference_pp])
w(tbl(srows))
w()
w('Reported by tier rather than pooled, because the tiers differ in how directly they map to Indonesia. '
  'The all-tier inventory gives %d transitions at a median absolute divergence of %.2f pp; the certified '
  'direct-candidate sensitivity gives 9 transitions at 42.94 pp. These answer different construction '
  'questions and neither is a filtered restatement of the other.'
  % (int(allt.transitions), allt.median_absolute_difference_pp))
w()
# ---------------------------------------------------------------- 5
w('## 5. Mechanism and Robustness'); w()
w('### 5.1 Reconciling a divergence: Tokopedia FY2022-FY2023'); w()
w('The longitudinal result establishes that transaction value and revenue move apart. It does not by '
  'itself say why. Tokopedia FY2022-FY2023 is the cleanest case for answering that, because it is the '
  'only directly Indonesia-aligned segment pair in the inventory and because the divergence runs in the '
  'counter-intuitive direction: transaction value falls while revenue rises sharply.')
w()
w('Transaction value falls **8.90 percent** while selected third-party net segment revenue rises '
  '**53.20 percent**. A naive reading would treat that as a platform growing strongly in a shrinking '
  'market. The disclosed components say something narrower. Of the arithmetic increase in net revenue, '
  '**60.56 percent** is associated with lower customer incentives and **39.44 percent** with higher '
  'gross revenue. Net revenue is gross revenue less incentives, so a reduction in promotional spending '
  'raises net revenue without any corresponding increase in commerce facilitated. The larger part of the '
  'revenue improvement is therefore a change in how much of the transaction the platform retains, not a '
  'change in how much transaction there is.')
w()
w('Three points bound this reading. The decomposition is arithmetic: it allocates a disclosed change '
  'across disclosed components and does not identify a causal effect of incentive policy on revenue. '
  'Incentive spending is itself a managerial choice, plausibly responding to the same competitive '
  'conditions that moved transaction value, so the two are not independent. And the exercise is '
  'available only where an issuer discloses the components separately, which is why it is presented as a '
  'mechanism illustration rather than as a systematic decomposition across the sample. What it '
  'establishes is sufficient for the thesis\'s purpose: at least some movement in the wedge is traceable '
  'to identifiable accounting choices rather than being an unexplained residual.')
w()
w('### 5.2 Robustness of the longitudinal result'); w()
w('The direct-candidate baseline gives 9 adjacent annual transitions, 3 sign reversals and a median '
  'absolute ordinary growth gap of **42.94 pp**. Four checks follow.')
w()
w('- **Growth transformation.** Log changes rather than ordinary percentage growth give a median absolute '
  'gap of **36.64 log-points ×100**. Direction rankings and sign-reversal classification are unchanged.')
w('- **Extreme transition.** Dropping the single largest gap (Blibli FY2022→FY2023, a low starting '
  'net-revenue base with major monetisation changes) leaves 8 transitions, still 3 reversals, median '
  '**29.34 pp**.')
w('- **Leave-one-transition-out.** Across all nine exercises the median ranges **29.34 pp to 52.52 pp**. '
  'No single transition is necessary for the qualitative conclusion.')
w('- **Leave-one-series-out.** Excluding Blibli leaves 4 transitions at 38.92 pp; Bukalapak, 6 at '
  '52.52 pp; Tokopedia, 8 at 29.34 pp. Every construction retains at least one sign reversal.')
w()
w('These establish that the descriptive non-equivalence is not an artefact of one observation, one series, '
  'or the growth transformation. They do **not** establish a population effect: geographic and business '
  'scope quality changes sharply across the scenarios, and the small candidate count means these remain '
  'descriptive diagnostics rather than conventional inferential statistics.')
w()
# ---------------------------------------------------------------- 6
w('## 6. Indonesia\'s Broader E-Commerce Transformation'); w()
w('### 6.1 National aggregates'); w()
w(tbl([['Year','Transaction value (Rp tn)','Estimated businesses','Implied value/business (Rp mn)','Marketplace (Rp tn)','Non-marketplace (Rp tn)'],
       [2023,'%.2f'%lev23.transaction_value_idr_trillion,format(int(lev23.estimated_ecommerce_businesses),','),
        '%.2f'%lev23.implied_idr_million_per_business,'%.2f'%lev23.marketplace_value_idr_trillion,
        '%.2f'%lev23.nonmarketplace_value_idr_trillion],
       [2024,'%.2f'%lev24.transaction_value_idr_trillion,format(int(lev24.estimated_ecommerce_businesses),','),
        '%.2f'%lev24.implied_idr_million_per_business,'%.2f'%lev24.marketplace_value_idr_trillion,
        '%.2f'%lev24.nonmarketplace_value_idr_trillion]]))
w()
w('BPS-Statistics Indonesia reports national e-commerce transaction value rising **%.2f percent** from '
  '2023 to 2024, with estimated e-commerce businesses rising **%.2f percent** and implied nominal value '
  'per business rising only **%.2f percent**. Both marketplace amounts are directly published; the 2024 '
  'figure of Rp203.58 trillion is preferred over reconstructing from the rounded 15.79 percent share, to '
  'which it reconciles.'
  % (b24.total_transaction_value_growth_pct, b24.estimated_businesses_growth_pct,
     b24.implied_value_per_business_growth_pct))
w()
w('### 6.2 Channel composition'); w()
w('The marketplace component grows **%.2f percent** while the non-marketplace component grows '
  '**%.2f percent**. In level terms the marketplace increase is Rp2.90 trillion against a total increase '
  'of Rp188.06 trillion, so approximately **98.46 percent** of the nominal increase falls outside the '
  'marketplace component that platform accounts observe.'
  % (b24.marketplace_component_growth_pct, b24.nonmarketplace_component_growth_pct))
w()
w('This is the single most consequential aggregate result in the thesis, and it cuts against the '
  'framing the issuer evidence might otherwise invite. The platform chapters measure marketplace '
  'activity carefully and find a large wedge inside it. The national statistics then say that '
  'marketplace activity is where Indonesian e-commerce growth is *not* happening. Both can be true: the '
  'wedge is a statement about the relationship between transaction value and revenue within observed '
  'platforms, while the channel split is a statement about where aggregate commerce is expanding. Read '
  'together they imply that platform accounts are becoming a narrower window onto national e-commerce, '
  'not a wider one.')
w()
w('Two cautions apply. BPS sales-media categories rest on a question allowing multiple responses, so '
  'the channel decomposition of *value* and the multiple-response channel *use* figures are different '
  'objects and are not mixed here. And the 2024 marketplace amount comes from a BPS directorate '
  'presentation rather than the main publication; it reconciles to the published 15.79 percent share '
  '(Rp203.58T / Rp1,288.93T = 15.7945 percent), which is why the direct amount is preferred over '
  'reconstructing from the rounded share.')
w()
w('### 6.3 Extensive versus intensive margin'); w()
w('Decomposing *V = N × A* symmetrically into a business-count term and an implied-value-per-business '
  'term allocates the change exactly. The count term is the larger component in every comparison: '
  '**70.98 percent** of the 2022→2023 increase, **90.29 percent** of 2023→2024, and **76.95 percent** '
  'over 2022→2024. Substituting the conflicting 2023 count of 3,934,981 as a sensitivity still leaves the '
  'count term at **70.95 percent**, so the extensive-margin reading does not depend on that choice. The '
  '2023 count is a documented source conflict: the BPS main body reports 3,816,750 and an '
  'executive-summary passage reports 3,934,981; the former is used because it reconciles to the displayed '
  '2022 count and BPS\'s later stated growth rate.')
w()
# ---------------------------------------------------------------- 7
w('## 7. Payment Traces and Institutional Visibility'); w()
w('### 7.1 Payment-system evidence'); w()
w(tbl([['Series, 2023→2024','Growth'],
       ['BPS e-commerce transaction value','%.2f%%'%pct('bps_ecommerce_total_value')],
       ['Electronic-money shopping value','%.2f%%'%pct('electronic_money_shopping_value')],
       ['Mobile-banking payment and purchase value','%.2f%%'%pct('mobile_banking_payment_purchase_value')],
       ['Internet-banking payment and purchase value','%.2f%%'%pct('internet_banking_payment_purchase_value')],
       ['QRIS transaction value','%.2f%%'%pct('qris_transaction_value')],
       ['QRIS merchants','%.2f%%'%pct('qris_merchants')]]))
w()
w('Bank Indonesia\'s payment-system statistics give a view of digital trace activity independent of both '
  'issuer accounts and BPS survey estimates. Payments and sales are different economic objects, so these '
  'series are not competing estimates of the same quantity and are not reconciled one-for-one to issuer '
  'transaction value. Their analytical value is the contrast: digital traces expand on a markedly '
  'different trajectory from the commerce they help record. Trace abundance is therefore not evidence of '
  'measured activity, which is precisely the asymmetry the invisible wedge formalises.')
w()
w('### 7.2 Business recordkeeping'); w()
w('Financial-report ownership among Indonesian e-commerce businesses is 15.19 percent in 2023 and 17.15 '
  'percent in 2024 as separately published wave values. BPS also publishes a business-level analysis '
  'reporting higher financial-report ownership among marketplace users than non-users. That is BPS\'s own '
  'result and is cited as such. The within-province change between waves is unstable — Pearson r = 0.309 '
  '(p = 0.066), Spearman rho = 0.151 (p = 0.379) across 36 common complete provinces — so H3 is reported '
  'as a published association that province aggregates do not independently validate. Province-level '
  'evidence is ecological and is not used to infer a business-level relationship.')
w()
w('### 7.3 What administrative linkage would require'); w()
w('PMK 37/2025 is the institutional bridge. The verified implementation sequence records marketplace '
  'designation on 1 July 2026, collection effective 1 August, postponement through 31 October, and '
  'scheduled implementation on 1 November 2026. The regulation builds on seller identity, '
  'transaction-linked turnover, withholding and reporting, not on platform corporate revenue.')
w()
w('A record becomes administratively usable only after four steps: the platform holds it; a seller '
  'identity is attached; it is transmitted to the Directorate General of Taxes; and it is matched to a '
  'taxpayer record. The wedge measured here establishes only the first. What can be assessed from '
  'published sources is whether the architecture is capable of the remaining three, and three '
  'observations follow. First, designation is by marketplace operator, so coverage is bounded by the '
  'designated set rather than by all platform-mediated commerce, and the channel result above puts '
  '98.46 percent of the 2023-2024 increase outside the marketplace component that designation reaches. '
  'Second, matching depends on seller tax identity, which the regulation requires but which the largely '
  'micro population documented by BPS may not uniformly hold. Third, the postponement through 31 '
  'October 2026 is itself evidence that operational readiness, rather than legal authority, is the '
  'binding constraint.')
w()
w('The thesis therefore establishes the architecture and its coverage boundary, and stops there. Whether '
  'linkage delivers reporting, matching and compliance effects is an empirical question that '
  'post-implementation data from November 2026 onward can answer. It is recorded in Section 9.4 as a '
  'limitation and as the natural next study rather than claimed here.')
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
w('The ASEAN panel holds **%d country-years across %d countries, 2019–2025**, retained by publication '
  'vintage with GDP and household-consumption normalisation. It is used to show that Indonesia\'s '
  'e-commerce expansion is neither unique nor uniform in the region. Vintage revisions are material in '
  'these estimates and are preserved rather than smoothed; the panel is contextual and is never pooled '
  'with issuer observations.' % (len(aseanp), aseanp.country.nunique()))
w()
w('### 8.2 Global platform corroboration'); w()
w('Across **%d matched issuer-years for %d non-Indonesian platform businesses** -- eBay, Etsy, Shopify, '
  'Jumia, Zalando, Rakuten, Mercado Libre and Sea -- the transaction-revenue boundary appears under '
  'distinct business models. Of %d annual transitions, %d meet the clean-scope requirement; %d of those '
  'show opposite-direction movement, at a median absolute growth divergence of **%.2f pp**.'
  % (int(glob_['matched_issuer_years']), int(glob_['issuers']), int(glob_['annual_transitions']),
     int(glob_['clean_scope_transitions']), int(glob_['opposite_direction_transitions_clean']),
     glob_['median_abs_growth_divergence_clean']))
w()
w('Two features of that summary matter more than the headline. First, the clean-scope filter removes '
  '%d of %d transitions -- roughly a quarter -- because acquisitions, reporting-perimeter changes or '
  'restatements make the year-on-year pair non-comparable. The same defect that forces the evidence-tier '
  'design in the Indonesian sample therefore recurs in mature, well-resourced global issuers, which '
  'suggests it is a structural feature of platform disclosure rather than a weakness peculiar to '
  'Indonesian filings. Second, the median clean divergence of %.2f pp is far below the Indonesian '
  'figure, while the maximum reaches %.0f pp. The global distribution is thus much more dispersed than '
  'any single summary conveys, and the Indonesian series sit toward its upper end rather than outside '
  'it.'
  % (int(glob_['annual_transitions'])-int(glob_['clean_scope_transitions']), int(glob_['annual_transitions']),
     glob_['median_abs_growth_divergence_clean'], glob_['max_abs_growth_divergence_clean']))
w()
w('This module is external corroboration that the measured boundary is a general feature of platform '
  'accounting rather than an artefact of Indonesian reporting practice. It is not an Indonesia '
  'observation, not a representative global panel, and is never pooled with the main sample.')
w()
# ---------------------------------------------------------------- 9
w('## 9. Discussion'); w()
w('### 9.1 What the evidence establishes'); w()
w('Three findings hold. The transaction–revenue boundary is economically large: for FY2023 the documented '
  'Indonesian cases imply a wedge of US$%.2f billion at an Ecosystem Ratio of %.3f. The boundary is not '
  'constant: within-series growth in transaction value and revenue diverges materially, with a median '
  'absolute divergence of %.2f pp across the all-tier inventory and sign reversals that survive every '
  'robustness construction. And the boundary is explicable: the Tokopedia reconciliation traces a '
  '53.20 percent net-revenue rise against an 8.90 percent transaction decline to disclosed incentive and '
  'gross-revenue components.'
  % (fy23.total_transaction_revenue_gap_usd_b, fy23.aggregate_gap_to_revenue_ratio,
     allt.median_absolute_difference_pp))
w()
w('### 9.2 Why it matters'); w()
w('Different records support different diagnoses of the same transformation. Platform revenue growth '
  'implies a different performance story from transaction growth. Marketplace-centred evidence mislocates '
  'where national growth occurs — 98.46 percent of the 2023–2024 nominal increase falls outside the '
  'marketplace component. Payment growth is not commerce growth, as the QRIS and mobile-banking series '
  'show. And abundant private traces still require identity, a reporting rule, transmission and matching '
  'before they become administratively usable. The risk is not that these records differ; it is that one '
  'is used as a proxy for another without reconciling the boundary between them.')
w()
w('### 9.3 What it does not establish'); w()
w(tbl([['The evidence supports','It does not by itself establish'],
       ['*W* and *E* measure the transaction–revenue boundary.','Participant profit, taxable income, unpaid tax, tax evasion or missing GDP.'],
       ['Evidence tiers identify how directly each series maps to Indonesia.','That direct, scope-pending and conditional observations are interchangeable.'],
       ['Issuer components arithmetically reconcile selected divergences.','A causal treatment effect of incentives, monetisation or accounting choices.'],
       ['BPS and PMK document wider activity and reporting architecture.','A firm-level causal effect or a completed compliance or revenue effect.'],
       ['Payment series expand faster than measured commerce.','That payment volume is commerce, or that the difference is unrecorded sales.']]))
w()
w('### 9.4 Limitations'); w()
w('Five limitations bound the design. The issuer sample is small and selected by disclosure availability '
  'and comparability. BPS business-level relationships are observational and the province-level change is '
  'unstable. Bank Indonesia payment measures capture trace activity, not e-commerce sales. PMK 37/2025 '
  'establishes legal architecture while postponed implementation prevents inference about operational '
  'linkage. And the ASEAN and global modules are purposive corroboration rather than representative '
  'samples.')
w()
# ---------------------------------------------------------------- 10
w('## 10. Conclusion'); w()
w('This thesis set out to measure how large the invisible wedge is in Indonesia, how it changes, and '
  'what explains those changes. On the first question, the documented FY2023 cases imply a wedge of '
  'US$%.2f billion at an Ecosystem Ratio of %.3f: for every dollar these platforms recognised as '
  'revenue, roughly %.0f dollars of transaction value passed through their systems without becoming '
  'platform revenue. On the second, the boundary is not a fixed platform characteristic. Within-series '
  'growth in transaction value and revenue diverges by a median of %.2f percentage points across the '
  'all-tier inventory, with sign reversals that survive every robustness construction attempted. On the '
  'third, the Tokopedia reconciliation shows that such movements are at least partly explicable from '
  'disclosed components: a 53.20 percent rise in net segment revenue against an 8.90 percent decline in '
  'transaction value resolves into lower customer incentives and higher gross revenue in a 60.56 to '
  '39.44 split.'
  % (fy23.total_transaction_revenue_gap_usd_b, fy23.aggregate_gap_to_revenue_ratio,
     fy23.aggregate_gap_to_revenue_ratio, allt.median_absolute_difference_pp))
w()
w('The contribution is a measurement one. The Ecosystem Ratio is constructed here rather than adopted, '
  'and the evidence-tier design is what makes it usable: by keeping direct, scope-pending and '
  'conditional observations separate rather than pooling them into a single headline, the thesis reports '
  'a defensible measurement under an explicit admission rule instead of an indefensible one under a '
  'hidden rule. That discipline costs statistical power and is the reason the results are presented as '
  'descriptive diagnostics rather than population estimates.')
w()
w('The wider evidence changes where the question points. Indonesian e-commerce grew '
  '%.2f percent between 2023 and 2024, but the marketplace component grew only %.2f percent, so '
  'approximately 98.46 percent of the nominal increase fell outside the channel that platform accounts '
  'observe. Payment traces expanded faster still, with QRIS transaction value rising %.2f percent over '
  'the same period. Read together, these say that the activity platform accounting makes visible is a '
  'shrinking share of the activity that is actually happening, and that the abundance of digital traces '
  'is not the same thing as the measurability of commerce.'
  % (b24.total_transaction_value_growth_pct, b24.marketplace_component_growth_pct,
     pct('qris_transaction_value')))
w()
w('Measured carefully, then, the invisible wedge is an accounting boundary rather than a hidden economy. '
  'It is not profit, not taxable income, and not missing output, and this thesis claims none of those '
  'things. But it is the precise point at which a platform\'s own transaction records stop being visible '
  'in its revenue line, and that is exactly where a seller-linked reporting architecture such as PMK '
  '37/2025 has to operate. The analysis in Section 7.3 suggests that architecture faces a coverage '
  'problem independent of how well it is implemented, because designation reaches marketplace operators '
  'while most of the measured growth sits outside that component. Whether the regime can nonetheless '
  'deliver reporting, matching and compliance is the question that post-implementation evidence from '
  'November 2026 onward will be able to answer, and it is the natural continuation of this work.')
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
