# Hypothesis extension: participant records and institutional linkage

**Status:** source-verified extension to the research agenda. It adds official
business-level and institutional evidence. It does not approve a final sample,
estimate a causal effect, or replace the certified issuer results.

## Why this extension matters

The earlier agenda treated the relationship between marketplace participation
and financial recordkeeping as unresolved because the repository only had
province marginals. That was correct for those data, but it was not the end of
the available evidence. BPS has since published its own business-level analysis
of the 2024 E-Commerce Survey, describing 2023 activity.

This changes two hypotheses materially:

1. the participant-side relationship can now be discussed using official
   business-level evidence rather than ecological province correlations; and
2. Indonesia's marketplace tax framework documents a legal bridge between
   seller identity, marketplace turnover, withholding, and reporting, although
   its operation and effects are not yet observable as of 10 September 2026.

The extension supports a more precise central idea:

> Digitalization produces **uneven or selective legibility**. Structured
> marketplace participation is associated with stronger business records and
> more traceable payment methods, and appointed marketplaces can in principle
> connect seller identity to transaction-linked reporting. But these features
> do not cover every digital sales channel, do not establish causal
> formalization, and do not prove that separate records are successfully linked
> in practice.

## Evidence now established

### Business-level marketplace differences

BPS reports the following comparisons for businesses in its 2024 survey of 2023
e-commerce activity:

| Indicator | Marketplace users | Non-marketplace users |
|---|---:|---:|
| Legal entity | 17.40% | 7.68% |
| Complete financial statements | 28.63% | 12.25% |
| Information-technology training | 8.49% | 2.83% |
| Cash payment use | 37.74% | 83.29% |

In BPS's multivariate logistic model, financial-statement ownership is
associated with higher odds of marketplace use: odds ratio 1.8463, 95% CI
1.7083--1.9955, p<0.001. The outcome is marketplace use, not financial
statements. The result therefore does not establish that marketplaces cause
recordkeeping. More formal businesses may select into marketplaces, platforms
may induce formalization, or both may reflect firm size, capabilities, or other
features not fully captured by the model.

BPS uses a demanding definition of financial statements: a separable set of
business accounts including income, assets, and liabilities. It is not merely a
sales log. Even so, the indicator is not tax filing, tax payment, audited
quality, or evidence that government agencies can access the firm's records.

The transcribed published results are preserved in:

- `data/bps_official/bps_marketplace_business_level_published_evidence_2026-09-10.csv`

### Channel composition remains economically important

The certified national BPS series shows that from 2023 to 2024:

- total e-commerce value rose 17.08%;
- marketplace value rose 1.45%; and
- non-marketplace value rose 20.57%.

The 2024 publication's **exclusive marketplace/non-marketplace decomposition**
places approximately 15.79% of total e-commerce value in the marketplace
component. This is not the same statistic as BPS's multiple-response/attributed
sales-media measure, which reports a different marketplace share. It is also a
pre-implementation statistical composition, not an estimate of the 2026 tax
rule's coverage. It does show that a marketplace-only information mechanism
cannot be assumed to describe the whole e-commerce economy.

Nothing in this comparison establishes that non-marketplace transactions are
untaxed, unrecorded, or inaccessible. Messaging, social media, direct websites,
payments, bank accounts, and merchant records may create other traces. The
claim is channel heterogeneity, not universal invisibility.

### A legal participant-reporting bridge exists

PMK 37/2025 establishes a framework under which designated marketplaces collect,
deposit, and report Article 22 income tax associated with domestic sellers'
PMSE income. Official guidance describes seller NPWP/NIK and address fields,
turnover declarations, and a 0.5% withholding rate applied to invoice gross
turnover excluding VAT and luxury-goods sales tax.

The Directorate General of Taxes appointed Blibli, Shopee Indonesia, Tokopedia,
and Lazada on 1 July 2026. This is institutionally important for *Invisible
Ledger*: the seller-side reporting base is transaction-linked gross turnover,
not the platform's own corporate revenue.

However, the Directorate General of Taxes subsequently postponed application
until 31 October 2026 and stated that amounts already withheld under the
appointments would be returned. As of this document's date, the regulation and
appointments establish **legal architecture**, not an operating post-policy
dataset or demonstrated compliance effect.

The institutional evidence is preserved in:

- `data/institutional/indonesia_marketplace_reporting_architecture_2025_2026.csv`

## Revised hypothesis statuses

| Hypothesis | Revised status | What is established | What remains unresolved |
|---|---|---|---|
| H3: marketplace participation and conventional recordkeeping differ | **Supported as an official business-level association** | Marketplace users have higher published financial-statement ownership; BPS's adjusted model also reports a positive association | Causal direction, time ordering, survey-design replication, and whether records reach tax/statistical systems |
| H4a: Indonesia has a legal mechanism linking marketplace activity to seller identity and reporting | **Established institutionally** | PMK 37/2025 and the appointment documents specify identity, turnover, withholding, and reporting roles | Completeness, matching quality, data use, enforcement, and effects |
| H4b: the mechanism is operationally linking the records | **Not yet testable as of 10 September 2026** | The implementation timetable and postponement are documented | Actual coverage and effectiveness after implementation |
| H4c: visibility differs by sales channel | **Supported descriptively, interpretation bounded** | Marketplace and non-marketplace components evolve differently and marketplace firms show different record/payment characteristics | Whether and how non-marketplace traces are linked to official systems |

The older province analysis remains valid as a negative methodological result:
province marginals did not recover the business-level association reliably.
That demonstrates why ecological correlations are a poor substitute for joint
microdata; it no longer determines the substantive H3 conclusion.

## The expanded economic mechanism

```text
digital sale
   |
   +-- structured marketplace route
   |      |
   |      +-- platform transaction record
   |      +-- seller identity / payment fields
   |      +-- stronger observed association with formal business records
   |      +-- legally designed tax-reporting bridge
   |
   +-- non-marketplace digital route
          |
          +-- substantial and faster-growing BPS value component
          +-- possible merchant, bank, payment, website, or messaging traces
          +-- no single comparable linkage demonstrated by current evidence

public company revenue observes only the issuer's accounting perimeter;
BPS estimates activity across channels; tax rules target defined actors and
transactions. None is a complete substitute for the others.
```

This gives the platform-accounting results a clearer role. Transaction value
and corporate revenue can diverge because monetization, incentives, and
business models change. Participant evidence then shows that structured channel
use is associated with different recordkeeping and payment characteristics.
Institutional evidence shows why a government may seek transaction-linked
seller reporting rather than infer seller activity from platform revenue.

The combined finding is not that digital commerce disappears from national
accounts. It is that the economic and administrative interpretation changes
with the observation layer, and the ability to connect those layers is
channel- and institution-specific.

## Strong alternatives and falsification tests

### Selection rather than formalization

More capable, larger, or already formal businesses may choose marketplaces.
The BPS association would then reflect selection, not a marketplace-induced
improvement in records. A credible causal claim would require timing,
longitudinal linkage, an external adoption shock, or another identification
strategy. Until then the paper should say **associated with**, not **caused by**.

### Marketplace reporting may work well once implemented

If post-implementation evidence shows broad, accurate, timely seller matching
and effective integration, the "linkage failure" version of H4 weakens. The
paper should then study the coverage boundary and measurement consequences of a
working linkage rather than insist that fragmentation persists.

### Non-marketplace channels may be visible elsewhere

The large non-marketplace component may leave strong bank, payment, merchant,
or other administrative traces. Evidence of comprehensive linkage through those
systems would weaken any claim that channel composition creates an information
blind spot. It would not erase the distinction between corporate revenue and
underlying merchant activity.

### BPS groups may not be perfectly comparable

Question wording, survey eligibility, weighting, and reporting error may affect
the published comparisons. The BPS analysis is authoritative published
evidence, but replication from licensed microdata would allow survey-design
checks, alternative controls, and harmonized cross-wave analysis.

## What this contributes beyond the existing BPS publication

BPS has already published the business-level marketplace comparisons and model.
*Invisible Ledger* must not claim to discover that relationship.

The potential contribution is the reconciliation across three observation
layers:

1. issuer transaction measures and corporate revenue;
2. business participation, records, payments, and sales channels; and
3. a legal architecture that connects selected marketplace turnover to seller
   identity and reporting.

The research contribution would be showing how conclusions about digital
commercial scale and visibility change across these layers, where the bridges
are documented, and where they remain empirically unverified. Whether this
cross-layer reconciliation is novel relative to the closest literature still
requires a targeted literature review.

## Immediate empirical work implied by this extension

1. Treat the BPS business-level publication as the primary participant-side
   evidence; demote the province correlation to an ecological robustness and
   aggregation-warning exercise.
2. Obtain the BPS questionnaire and, if approved, microdata to replicate the
   adjusted association with survey weights and design variables.
3. Build the visibility matrix with separate columns for legal obligation,
   operational implementation, observed coverage, and verified linkage.
4. After 31 October 2026, check whether implementation actually began before
   designing any post-policy analysis.
5. Investigate what administrative or payment traces exist for non-marketplace
   channels; do not classify them as invisible by residual.
6. Keep the Indonesia issuer sample and BPS business population separate. They
   answer connected questions but are not one pooled dataset.

## Primary sources

- BPS, *Menimbang Manfaat dan Risiko Penggunaan Marketplace dalam E-Commerce
  di Indonesia*: <https://www.bps.go.id/id/publication/2025/09/30/3bc481a585782813cc894636/cerita-data-statistik-untuk-indonesia-menimbang-manfaat-dan-risiko-penggunaan-marketplace-dalam-e-commerce-di-indonesia.html>
- Ministry of Finance, PMK 37/2025: <https://www.jdih.kemenkeu.go.id/dok/pmk-37-tahun-2025/files>
- Directorate General of Taxes, marketplace guidance:
  <https://pajak.go.id/marketplace>
- Directorate General of Taxes, appointment announcement:
  <https://pajak.go.id/id/siaran-pers/pemerintah-implementasi-pmk-372025-melalui-penunjukan-empat-marketplace-sebagai>
- Directorate General of Taxes, postponement announcement:
  <https://www.pajak.go.id/id/pengumuman/penundaan-waktu-pemberlakuan-ketentuan-pemungutan-pph-pasal-22-oleh-marketplace>
