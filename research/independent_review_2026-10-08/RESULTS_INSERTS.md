# Draft inserts for the thesis — 8 October 2026

These are separate working passages for Claude and the researcher. They are not the active manuscript. Use them in the proposal's existing framework, methods and results sections. Numerical statements below were checked through [measurement_checks.py](measurement_checks.py) and the recorded source inputs. The source notes are drafting controls; place them in the final captions, citations or appendix as appropriate.

## Framework: what the platform measures describe

Transaction value records the sales a platform carries during the period. Revenue records the income it recognises from its own services and sales. The take rate is revenue divided by transaction value for the same scope. Revenue and transaction value grow together when that share stays constant.

The invisible wedge is transaction value minus revenue, expressed in currency units. Growth divergence measures how far their annual percentage growth rates differ. The wedge answers the question of size. Growth divergence answers whether revenue follows the growth of the commerce carried.

For the same scope, revenue equals transaction value multiplied by the take rate. Changes in the take rate can reflect fees, incentives, business mix or accounting treatment. Each explanation needs evidence from the relevant issuer and period.

**Method note for the appendix.** Write the exact additive decomposition as `Δln R = Δln V + Δln m`. For ordinary fractional growth, retain `gR = gV + gm + gV × gm`. The approved measure remains `D = gR − gV`. This note does not redefine D or H1. Transaction-value definitions and revenue bases remain issuer-specific in the methods table.

## Results: Tokopedia's revenue rose while transaction value fell

Tokopedia shows how revenue and the commerce carried can give opposite growth conclusions. Its transaction value fell by 8.9% in 2023, while net revenue rose by 53.2%. Its take rate rose from 1.48% to 2.48% over the same period.

The segment accounts explain the net revenue increase through two components. Lower customer incentives accounted for 60.6% of the increase in net revenue. Higher third-party gross revenue accounted for the remaining 39.4% of that increase. These components reconcile the reported change in the segment's net revenue.

Revenue growth described the platform's increased income while transaction value described declining commerce. The choice between those measures changed the direction of the growth conclusion.

**Source and scope note.** GoTo 2023 annual report: operating metrics, printed page 142 (PDF page 144); Note 29, financial-statement pages 5/111 and 12 (PDF pages 475–476). The sample is the Indonesia-aligned e-commerce segment; it is not an explicit country line. The 2022 figures use the restated comparison in the same annual report. The component calculation uses third-party gross and net revenue and the disclosed customer incentive deduction. Original IDR-million values remain in the source-check table in [the audit](CONCEPT_AND_LITERATURE_AUDIT.md). No FX conversion enters this percentage calculation. The annual-report pages were checked as text and images.

**Editorial action.** Use the proposal's 60.6%. The later 60.5% figure comes from rounded analytical inputs. Preserve the original sources and record this source-precision reconciliation when incorporated.

## Results: separate the size of divergence from its direction

The median absolute growth gap was 38.9 percentage points across the main comparisons. It was 7.1 percentage points across the original clean foreign benchmark comparisons. This comparison describes the size of the gap without cancelling positive and negative differences.

**Sample and measure note.** Three main series contribute eight transitions. Eight foreign series contribute 29 clean transitions. These are the existing `IDN_main` and `EXT_clean` rows, with their original scope qualifications. Their signed median differences are different quantities. Do not attach the expanded five-versus-27 test's p-value to this descriptive comparison.

## Methods and results: explain the movement statistic

We divide log revenue change into transaction growth and the change in take rate. A log change measures proportional movement and makes the two components add exactly. We compare the sizes of these components before they offset each other.

Take-rate changes formed 66.5% of their combined size at the median main comparison. The corresponding share was 26.7% in the original clean foreign benchmark. This describes movement in the accounting identity; it does not estimate a causal effect.

**Definition and sample note.** The share is `|Δln m| / (|Δln V| + |Δln m|)`, summarised by the median across transitions. It is not `Δln m / Δln R`. The samples are the same three main series/eight transitions and eight foreign series/29 transitions above. The check independently reproduces `wedge_split_summary.json`. Negative transaction growth can offset a positive take-rate component; a net-growth share can then exceed the whole net increase.

## Literature and contribution: connect to the closest work

Existing work separates platform intermediation from the sales carried through it (OECD, 2023). UNCTAD (2024) already reports business e-commerce sales alongside transaction values through major platforms. Accounting research also shows why clear and stable measure definitions matter (Givoly et al., 2019).

This study examines when the choice of measure changes the conclusion about growth in Indonesia. It matches platform disclosures over time and reconciles large movements with the issuer's accounts. It then examines national participation and channel evidence through a separate statistical source. The result identifies where these views agree and where the available records leave the comparison unresolved.

**Citation controls.** [OECD handbook](https://www.oecd.org/en/publications/2023/11/oecd-handbook-on-compiling-digital-supply-and-use-tables_b127cb7a.html); [UNCTAD report](https://unctad.org/publication/business-e-commerce-sales-and-role-online-platforms); [Givoly et al.](https://link.springer.com/article/10.1007/s11142-019-09514-y). Givoly supplies a general information principle; its public notes exclude technology KPIs from its sample. This paragraph makes an empirical contribution claim and no global priority claim. Full references and the audited support limits appear in [the literature map](CONCEPT_AND_LITERATURE_AUDIT.md).

## Discussion: connect the two links without pooling their levels

The two links require different evidence because they answer different questions. A stable take rate lets revenue follow the commerce carried inside a platform. A stable covered share lets platform commerce follow the growth of wider online commerce. The national seller count adds another question: how much estimated participation growth reflects first-time entry?

The thesis examines these links separately using issuer disclosures and the national survey evidence. A result at one link does not establish the condition at the other. Agreement between headline growth rates can also arise when different share changes offset each other.

**Boundary for the limitations chapter.** The issuer and survey definitions are not harmonised enough to compute a national wedge. The explanatory share identity in the audit is not an instruction to combine their ratios. Keep coverage attribution conditional on the existing returning-seller and survey qualifications.
