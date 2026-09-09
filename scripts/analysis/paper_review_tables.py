#!/usr/bin/env python3
"""Selected tables for author review, generated from the longitudinal ledger.

A documented release-selection rule avoids silently resolving competing vintages.
This selection is not admission to an Indonesia-only main sample.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import reviewed_longitudinal as review
import longitudinal_review as core

F22='https://asset-about.blibli.com/2023/03/Earnings-Release-FY22-PT-Global-Digital-Niaga-Tbk-1.pdf'
F24='https://asset-about.blibli.com/2025/03/Earnings-Release-FY24-PT-Global-Digital-Niaga-Tbk.pdf'
F25='https://asset-about.blibli.com/2026/03/Earnings-Release-FY25-PT-Global-Digital-Niaga-Tbk-.pdf'


def select_annual(rows: list[dict]) -> list[dict]:
    choices={2019:None,2020:None,2021:F22,2022:F22,2023:F24,2024:F24,2025:F25}
    out=[]
    for year,url in choices.items():
        hits=[r for r in rows if r['issuer']=='Blibli/GDN' and r['scope']=='3P Retail'
              and r['period']==str(year)+'FY' and
              (r['source_url']==url if url else r['source_csv'].endswith('blibli_prospectus_2019_2020_candidates.csv'))]
        if not hits:raise ValueError('Missing selected 3P annual source: '+str(year))
        if len({(r['tv'],r['revenue'],r['gpbd']) for r in hits})!=1:raise ValueError('Selected source conflict: '+str(year))
        r=sorted(hits,key=lambda x:x['record_id'])[0]
        out.append(dict(year=year,tpv_idr_billion=r['tv'],net_revenue_idr_billion=r['revenue'],
            gpbd_idr_billion=r['gpbd'],revenue_per_tpv=r['monetization_rate'],ecosystem_ratio=r['ecosystem_ratio'],
            ratio_status=r['ratio_status'],source_url=r['source_url'],source_locator=r['source_locator'],
            source_csv=r['source_csv'],source_csv_row=r['source_csv_row'],source_record_id=r['record_id'],
            selection_note='FY2024-release comparative; original FY2023-release TPV differs and remains unresolved' if year==2023 else
               'Prospectus transcription; historical business/geography comparability pending' if year<2021 else
               'Selected issuer release; geography and business comparability pending',
            main_sample_status='not_approved'))
    return out


def paper_text(annual: list[dict], changes: list[dict]) -> str:
    def f(value,places=2):return '' if value=='' else f'{core.number(value):,.{places}f}'
    lines=['# Longitudinal evidence: Blibli third-party retail','',
      'Draft empirical section for author review, 9 September 2026. This is a proposed additional series, not an approved Indonesia-only main sample.','',
      '## Source and scope','',
      'The source collection contains annual transaction value and net revenue for Blibli/GDN third-party retail from 2019 to 2025. The early observations are prospectus transcriptions; later observations are drawn from issuer releases. The segment includes both e-commerce and online travel. It must not be relabelled as a goods-only Indonesian marketplace or pooled with the existing country allocations without a stated eligibility decision.','',
      'The table below retains original currency and an explicit release-selection rule. Its seven years are observations of one business segment, not seven firms. Gross profit before discount (GPBD) is retained separately: the issuer defines its published take rate as GPBD/TPV, which differs from the revenue/TPV measure used here.','',
      '## Annual source records','',
      '| Year | TPV, IDR bn | Net revenue, IDR bn | Revenue / TPV, % | E |',
      '|---|---:|---:|---:|---:|']
    for a in annual:
        rate=f(core.number(a['revenue_per_tpv'])*100,3)
        lines.append(f"| {a['year']} | {f(a['tpv_idr_billion'],3)} | {f(a['net_revenue_idr_billion'],3)} | {rate} | {f(a['ecosystem_ratio']) or 'n.m.'} |")
    lines += ['', 'Notes: E = TPV/net revenue - 1 only with a positive denominator. The negative 2019 net revenue is preserved and E is not interpreted. The FY2023 entry is the FY2024-release comparative (49,912 IDR bn TPV), not a silent replacement of the original FY2023 release (49,917). Source locators and record identifiers are in paper_blibli_3p_annual.csv.', '',
       '## Changes within the same release','',
       'To avoid treating publication differences as growth, the following comparisons use adjacent annual figures printed in the same release. They do not combine annual observations with constituent quarters.','',
       '| Comparison | TPV growth, % | Net revenue growth, % | Change in revenue / TPV, pp |',
       '|---|---:|---:|---:|']
    for c in changes:
        lines.append(f"| {c['from_year']}-{c['to_year']} | {f(c['tv_growth_percent'])} | {f(c['net_revenue_growth_percent'])} | {f(c['revenue_per_tpv_change_pp'],3)} |")
    lines += ['',
      'The direction of transaction growth does not mechanically determine the direction of recorded monetization. In the 2021-2022 pair, transaction value grows faster than net revenue and revenue per transaction value falls. In 2024-2025, transaction value falls while net revenue increases. These are observed changes in reported aggregates, not causal estimates or evidence of tax non-compliance. The available variables do not separately identify the effects of incentives, commissions, and the commerce/travel mix.', '',
      'The first empirical use is therefore a longitudinal comparison of operating scale and recorded revenue within a documented segment. The current evidence does not justify estimating a national transaction-revenue total or treating a change in E as a change in hidden income.', '',
      '## Quarterly checks and remaining coverage','',
      'Fifteen distinct quarterly periods appear in the selected extract files. The Q1 2023 release was originally misread because its first numerical column is FY2022, followed by Q1 2023 and Q1 2022. The review overlay relabels ten source records and recovers five omitted Q1 2022 records, without changing the original CSVs. The corrected 3P quarterly sums reconcile with the available 2022 and 2023 half-year, nine-month and annual values within rounding tolerance.', '',
      'Q4 2024 still has competing TPV vintages, and the rounded Q4 2021 net-revenue figure is zero. Thus fifteen periods are not fifteen usable positive-denominator ratios, and the quarterly collection is not a balanced panel. The broader review also retains two unresolved FY2023 cross-vintage TPV rollups for Group and Institutions. They are not forced to close.', '',
      '## Source references','',
      '- Blibli IPO prospectus: repository transcription, operating metrics printed p.32 and revenue components printed pp.38-39; source CSV retains lineage.',
      '- FY2022 results, p.2: '+F22,
      '- FY2024 results, p.2: '+F24,
      '- FY2025 results, p.2: '+F25,
      '- Q1 2023 results, p.2: https://asset-about.blibli.com/2023/05/Earnings-Release-1Q23-PT-Global-Digital-Niaga-Tbk.pdf',
      '', 'Source review and numerical reproduction are not a decision on thesis sufficiency. Geography, consistent revenue definitions, and an adequate longitudinal main sample still require an explicit research-design decision.','']
    return '\n'.join(lines)


def build(root: Path,output: Path) -> None:
    review.build(root,output)
    rows,_=core.read_rows(output,'source_records_reviewed.csv')
    annual=select_annual(rows)
    changes=[c for c in review.annual_changes(rows) if c['scope']=='3P Retail']
    review.export_csv(output/'paper_blibli_3p_annual.csv',annual)
    review.export_csv(output/'paper_blibli_3p_changes.csv',changes)
    (output/'empirical_section.md').write_text(paper_text(annual,changes),encoding='utf-8')
    print('Paper-facing tables: 7 selected annual segment records; 3 within-release annual comparisons. No main sample approval inferred.')
    for file in ('paper_blibli_3p_annual.csv','paper_blibli_3p_changes.csv'):
        print(file);print((output/file).read_text())

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    p.add_argument('--output',type=Path,default=Path('build/longitudinal'))
    a=p.parse_args()
    try:build(a.repo.resolve(),a.output.resolve())
    except (ValueError,KeyError,OSError) as exc:p.exit(1,f'ERROR: {exc}\n')
