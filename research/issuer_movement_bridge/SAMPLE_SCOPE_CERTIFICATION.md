# Indonesia longitudinal sample-scope certification

**Status:** empirical admission review for Kong's dataset-first decision. No sample is represented as advisor-approved.

## Certification result

The available longitudinal evidence does **not** support treating every direct issuer pair as equally Indonesia-specific. The clean hierarchy is:

1. **Tokopedia e-commerce FY2022–FY2023 — strongest Indonesia-aligned direct segment.**
2. **Blibli 3P Retail FY2020–FY2025 — direct longitudinal evidence, but mixed e-commerce + online-travel business perimeter.**
3. **Bukalapak Group FY2020–FY2023 — direct longitudinal evidence, but geographically mixed because overseas operations are disclosed and no matched country allocation has been recovered.**
4. **Grab/Shopee Indonesia reconstructions — explicit/estimated country focus but conditional rather than direct matched issuer pairs.**

This hierarchy is stricter than simply counting “direct” rows. Directness and geographic/business-scope fitness are separate dimensions.

## Tokopedia: strongest core candidate, but still not a literal country line

The FY2022–FY2023 e-commerce series is a direct matched business-segment pair. GoTo's 2023 disclosures identify the business as Tokopedia's e-commerce marketplace, and GoTo's FY2023 results describe the subsequent Tokopedia/TikTok e-commerce combination under PT Tokopedia as strategic partners **in Indonesia**. The annual-report subsidiary context also distinguishes a Tokopedia India support entity whose activity is software development / IT services rather than an Indian Tokopedia marketplace.

This materially strengthens the geography interpretation:

> **Tokopedia is a strong Indonesia-aligned operating segment, not merely an arbitrary Group segment.**

However, the annual GTV/revenue line itself is not printed as an explicit “Indonesia” geographic line. Therefore the correct admission label remains:

`strong_indonesia_aligned_direct_segment_pending_advisor_acceptance`

rather than `direct_country`.

Primary company entry points:

- GoTo 2023 annual-report archive: <https://gotocompany.com/investor-relations/en/annual-reports>
- GoTo FY2023 results / Tokopedia–TikTok Indonesia partnership: <https://www.gotocompany.com/en/news/press/goto-group-turns-adjusted-ebitda-positive-surpassing-full-year-guidance-as-company-reports-2023-fourth-quarter-and-full-year-results>

## Blibli 3P: excellent longitudinal mechanics, mixed economic perimeter

Blibli 3P Retail supplies unusually useful direct TPV/net-revenue/GPBD histories and source-level mechanisms. It is therefore valuable for the thesis regardless of whether it becomes core.

The problem is not data quality; it is **scope**:

- the 3P segment includes online commerce **and online travel through tiket.com / OTA**;
- the issuer's prospectus source review describes historical revenue as arising from Indonesian operations, but the economic location of the underlying 3P transaction value is not shown to be exclusively Indonesian;
- travel bookings can concern services outside the domestic goods-marketplace perimeter;
- the issuer's own published “take rate” uses GPBD/TPV, not net revenue/TPV.

The FY2025 issuer material also makes clear that the Group ecosystem spans Blibli and tiket.com and that OTA mix can materially affect 3P economics.

Therefore the certified treatment is:

`direct_mixed_scope_candidate`

with a binary advisor choice:

- **admit** if the intended main object is an Indonesia-based digital-platform business segment whose transaction activity can include OTA; or
- **keep as mechanism/supporting evidence** if the main object must be a pure Indonesia marketplace-commerce segment.

The data do not justify silently relabelling Blibli 3P as “Indonesia goods marketplace.”

Primary issuer sources/locators are preserved in `mechanism_source_extract.csv`, `blibli_prospectus_2019_2020_candidates.csv`, and the Blibli earnings releases.

## Bukalapak: direct but geographically mixed

Bukalapak supplies four matched 12-month Group TPV/revenue pairs for FY2020–FY2023. FY2024 is correctly excluded because TPV covers nine months while revenue covers twelve months.

For the retained years, the binding problem is geography. The annual-report source review identifies operations in Indonesia **and four other countries**. No country-level allocation has been recovered that would establish that the matched Group TPV and revenue lines are Indonesia-only.

This means the series is useful for a within-issuer recurrence question—transaction activity and revenue can be compared directly through time—but is not yet defensible as an Indonesia-isolated main observation.

Certified treatment:

`direct_group_supporting_pending_country_allocation`

Unless a source establishes that overseas activity is either separately removable or immaterial under a documented rule, the conservative main-sample treatment is **supporting rather than core**.

## Grab and Shopee: country focus is not enough to make them direct

Grab and Shopee are the opposite problem from Bukalapak:

- their intended geography is Indonesia;
- but one or more quantities in the pair are derived or externally estimated.

They should therefore remain `conditional_sensitivity` cases. Their role is to test whether the main findings survive the original Indonesia-country reconstruction logic, not to provide independent direct validation.

## What this means for Kong's choice

There are three defensible boundaries worth putting in front of the advisor:

### Boundary A — strongest geography discipline

Core: **Tokopedia only**.  
Result: too little longitudinal breadth by itself.

### Boundary B — Indonesia-aligned operating segments

Core candidates: **Tokopedia + Blibli 3P**.  
Interpretation: Indonesia-based/aligned digital platform segments, with Blibli's OTA perimeter stated explicitly.  
Current movement evidence: six adjacent transitions, three opposite-sign movements.

### Boundary C — all direct issuer/segment candidates

Core candidates: **Tokopedia + Blibli 3P + Bukalapak Group**.  
Interpretation: direct issuer evidence from Indonesia-centred platform businesses, not strictly Indonesia-only geography.  
Current movement evidence: nine adjacent transitions, three opposite-sign movements.

Conditional Grab/Shopee remain outside the direct core under every boundary.

## Recommended empirical presentation before advisor decision

Do **not** choose B or C on the advisor's behalf. Present:

- exact source and period coverage;
- scope caveat beside each platform;
- the sensitivity of the movement result to Boundary B versus C;
- hard exclusions separately;
- Grab/Shopee as a conditional layer.

The important improvement is that the unresolved question is now explicit. Kong is no longer being asked “is this data enough?” in the abstract; she can decide **which documented scope boundary she accepts for the Indonesia main analysis**.
