# Indonesia visibility matrix — research checkpoint

**Status:** research design aid, not a claim that any institution lacks information. Updated 10 September 2026.

The purpose is to replace the vague statement that “the ledgers are fragmented” with an observer-specific question:

> **For a digitally mediated commercial event, which records exist, who can observe them, and which linkages are established by evidence?**

A blank or unknown cell is not treated as proof of invisibility.

## Observer-specific matrix

| Economic information | Platform / marketplace | Merchant | Public researcher / investor | BPS | Directorate General of Taxes (DGT) | Current evidentiary status |
|---|---|---|---|---|---|---|
| Platform transaction value / TPV / GMV | Directly observed by the relevant platform; public aggregates vary by issuer and definition | Merchant sees own transactions, not necessarily platform aggregate | Selected issuer aggregates or estimates are public; geography and scope often incomplete | BPS does not use issuer TPV as the same object as its e-commerce sales measure | No repository evidence establishes a historical transaction-level linkage from the issuer series to DGT | **Established public aggregate boundary; participant-level linkage unknown** |
| Platform-recognized revenue | Platform accounting system | Not the merchant's own sales measure | Audited/reported company or segment revenue is often public | Different statistical object from business online-sales revenue | Corporate tax information may exist, but this project does not possess a matched administrative dataset | **Established corporate ledger** |
| Merchant identity for marketplace seller | Platform account information | Merchant supplies account/identity data | Generally not public at transaction level | Survey respondent identity exists inside BPS survey operations but is not available in the public aggregate tables used here | PMK 37/2025 Article 6 specifies NPWP/NIK and correspondence-address information to an appointed marketplace | **Legally specified DGT information channel, but implementation timing matters** |
| Marketplace invoice / transaction document | Marketplace system can generate the document under the PMK architecture | Merchant is responsible for a billing document generated through the marketplace system | Not public at transaction level | Not linked to the issuer records in the current repository | PMK 37/2025 Article 12 specifies invoice fields including date/number, marketplace, merchant account, buyer identity, goods/services, price, discount and PPh 22; Article 15 requires reporting specified information to DGT | **Legally specified future/implemented-then-postponed reporting architecture, not historical coverage evidence** |
| Merchant financial-report ownership | Platform may or may not know; not established here | Merchant knows whether it maintains a financial report | Public BPS aggregates show prevalence, not business identity | BPS asks whether the business has a financial report (`R308` in the **2024 survey / reference-year-2023** microdata dictionary) | No evidence in this project shows DGT receives the BPS response or that financial-report ownership equals tax filing | **Established survey measure; cross-institution linkage unknown** |
| Sales channel used by merchant | A given platform knows activity on itself, not necessarily all other channels | Merchant knows its channel portfolio | BPS publishes aggregates; licensed microdata can identify channels at business level | The **2024 survey / reference-year-2023** dictionary distinguishes website, email, instant messaging, social media and named marketplaces (`R309*`) | Marketplace reporting rules apply to covered marketplace transactions, not automatically to all nonmarketplace digital channels | **Established BPS channel measurement; institutional coverage differs by channel** |
| Share of business revenue from marketplace vs other channels | A platform sees its own transactions, not necessarily merchant total revenue | Merchant is source respondent | Not available as linked public microdata in this project | The **2024 survey / reference-year-2023** dictionary contains monthly revenue shares from offline, marketplace and nonmarketplace sales (`R313A-C`) | No linked DGT/BPS business-level file is available to this project | **Potentially high-value FY2023 licensed-microdata bridge; not yet acquired** |
| Payment-provider record | Payment provider | Merchant/customer | Not established in this repository | BPS asks payment method, but this is not a payment-record linkage | Regulatory/tax access may exist under other authorities/rules, but it has not been established for this thesis | **Unknown for linkage purposes; do not claim** |

## The PMK 37/2025 bridge is institutionally important but temporally interrupted

The regulation specifies an information architecture that is distinct from corporate financial statements:

- **Article 6:** domestic merchants provide NPWP/NIK and correspondence address to an appointed marketplace.
- **Article 12:** the marketplace electronic system supports transaction billing documents containing merchant/buyer/transaction fields and the PPh 22 amount where applicable.
- **Article 15:** the appointed marketplace reports Article 6 information, additional merchant/buyer information, billing-document information, and PPh 22 collected/remitted to DGT.

Primary rule: <https://pajak.go.id/id/peraturan/penunjukan-pihak-lain-sebagai-pemungut-pajak-penghasilan-serta-tata-cara-pemungutan>

DGT announced appointment of four marketplaces on 1 July 2026, but on 5 August 2026 it **postponed application through 31 October 2026**, with collection scheduled to begin 1 November 2026. DGT also said the previous appointment decisions would be cancelled/reissued and amounts already collected would be returned.

Appointment announcement: <https://www.pajak.go.id/index.php/en/node/120146>  
Postponement announcement: <https://www.pajak.go.id/id/pengumuman/penundaan-waktu-pemberlakuan-ketentuan-pemungutan-pph-pasal-22-oleh-marketplace>

Therefore the thesis can use PMK 37 as evidence that **participant-level marketplace information and platform corporate revenue are institutionally different data objects**, and that the state has designed a bridge between them. It cannot use the rule as evidence that FY2023 transactions were all visible to DGT through this mechanism, nor as evidence that pre-rule transactions were invisible.

## BPS supplies a different bridge

The official SILASTIK catalogue labels the dataset **Survei Usaha/Perusahaan E-Commerce 2024** and states that its survey universe is businesses using the internet to accept orders or sell goods/services. The dictionary, however, explicitly contains an item referring to constraints experienced in online-selling activity **during 2023** (`R325`). This is therefore treated here as a **2024 survey whose economic reference year is 2023**, consistent with the BPS *Statistik E-Commerce 2023* publication rather than as microdata for economic year 2024.

Its dictionary includes, among others:

- `R308` — whether the business has a financial report;
- `R309*` — sales channels, including instant messaging, social media and named marketplaces such as Tokopedia, Shopee, Bukalapak, Gojek, Grab and Lazada;
- `R313A-C` — monthly revenue shares from offline, marketplace and nonmarketplace sales;
- `R314` — average online-sales transaction frequency;
- `R315/R315B` — business revenue relative to the previous year and percentage change;
- `R320/R320A` — online exports and export-sales share;
- `W_FINAL` — survey weight.

Catalogue: <https://silastik.bps.go.id/v3/index.php/mikrodata/detail/ODdXeUNNcW5vcVVGVWhTUERuTGNTQT09>

### Consequence for the empirical design

This timing clarification is useful rather than merely cosmetic:

1. the licensed dataset is potentially a **business-level participant-side complement to the FY2023 platform evidence**;
2. it does **not** by itself provide a 2023→2024 enterprise panel or a business-level replication of the 2024 published aggregates;
3. a later survey/microdata release corresponding to economic year 2024 would be required for a genuine repeated-business-data extension, if such a file becomes available and is comparable;
4. until then, the 2023/2024 BPS comparison remains based on published aggregate/province estimates, not linked microdata.

The catalogue lists the file as province-level, DBF format, and subject to an abstract, signed data-use agreement, and dissemination fee. If acquired, the 2023-reference microdata could test joint business-level relationships among channel use, financial reports, revenue composition, growth, size, sector and geography instead of inferring them from aggregate marginals or province correlations.

## What this matrix establishes now

1. **Corporate revenue is only one observer-specific record.** It is not the participant's sales ledger and it is not the same object as BPS online-sales estimates.
2. **Digital transaction traceability and conventional financial documentation are different dimensions.** BPS measures financial-report ownership separately from digital channel use.
3. **A participant-level tax information bridge is explicitly specified by PMK 37/2025,** which itself demonstrates that marketplace corporate accounts and seller-level tax reporting are not interchangeable.
4. **The existence of separate ledgers does not prove institutional failure.** BPS is already measuring businesses through surveys, and DGT has designed a marketplace reporting/collection channel.
5. **The strongest unresolved empirical question is linkage and coverage:** how much economically important activity is captured by each observer, and what additional inference becomes possible when the records are reconciled.

## Promotion rule

Use this matrix to discipline claims, not as a table of assumed missing information. Every final-paper visibility claim should name the observer and one of four statuses:

- `directly observed / reported`;
- `survey-estimated`;
- `legally specified but not established for the historical period`;
- `unknown / unlinked in the available evidence`.
