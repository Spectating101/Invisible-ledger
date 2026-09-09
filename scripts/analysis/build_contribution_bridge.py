#!/usr/bin/env python3
"""Economic interpretation of existing BPS extracts; supplementary, not a new main sample.

Standard library only. Source files remain immutable. All results are conditional
on the repository's published-estimate transcriptions and specified populations.
No survey-design inference, individual matching, inflation adjustment or causal
identification is performed. The 2023 alternative count is an explicit scenario.
"""
from __future__ import annotations

import argparse
import csv
from decimal import Decimal, localcontext
import hashlib
import json
from pathlib import Path

D = Decimal
BASE = '69f8e3d6ca1af9bef310098d36f5cd0511454acb'
INPUT = 'data/bps_official/bps_ecommerce_national_indicators_2020_2023.csv'
INPUT_BLOB = '6a943e8bdb29f15578a4353fcff96a14af4346eb'
COUNT = 'estimated_number_of_ecommerce_businesses'
VALUE = 'ecommerce_transaction_value'
REPORTS = 'ecommerce_businesses_with_financial_reports'
MARKET = 'marketplace_sales_media_business_share'
MESSAGING = 'instant_messaging_sales_media_business_share'
STATUS = 'conditional_author_review_not_approved_main_sample'
ALTERNATIVE_COUNT = D('3934981')
ALTERNATIVE_SOURCE = 'data/bps_official/README.md: Internal consistency warning'


def number(value: str) -> Decimal:
    try:
        v = D(str(value))
    except Exception as exc:
        raise ValueError(f'Invalid numeric value: {value!r}') from exc
    if not v.is_finite():
        raise ValueError(f'Nonfinite value: {value!r}')
    return v


def probability(v: Decimal) -> Decimal:
    if not v.is_finite() or not D(0) <= v <= D(1):
        raise ValueError('A probability must be finite and between zero and one')
    return v


def blob_hash(content: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest()


def load(path: Path) -> tuple[dict, list[dict]]:
    raw = path.read_bytes()
    if blob_hash(raw) != INPUT_BLOB:
        raise ValueError('Input differs from reviewed snapshot. Reassess source definitions and update the pinned input deliberately.')
    values, lineage = {}, []
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f, strict=True)
        if not reader.fieldnames or len(set(reader.fieldnames)) != len(reader.fieldnames):
            raise ValueError('Missing or duplicate CSV headers')
        for row_number, row in enumerate(reader, 2):
            if None in row or any(v is None for v in row.values()):
                raise ValueError(f'Malformed CSV record {row_number}')
            if row['geography'] != 'Indonesia':
                raise ValueError('National calculation cannot pool other geographies')
            key = (int(row['reference_year']), row['indicator'])
            if key in values:
                raise ValueError(f'Duplicate indicator-year: {key}')
            v = number(row['value'])
            if row['unit'] == 'percent':
                probability(v / 100)
            values[key] = dict(row, value=v, source_ref=f'{INPUT}:record {row_number}')
            lineage.append(dict(indicator_year=f'{key[0]}:{key[1]}', source_record=row_number,
                                source_file=INPUT, source_url=row['source_url'],
                                source_locator=row['source_locator'], question_basis=row['question_basis'],
                                input_value=row['value'], unit=row['unit']))
    return values, lineage


def get(data: dict, year: int, indicator: str, unit: str) -> Decimal:
    row = data[(year, indicator)]
    if row['unit'] != unit:
        raise ValueError(f'Wrong unit for {year}:{indicator}: {row["unit"]}')
    return row['value']


def growth(v0: Decimal, v1: Decimal) -> Decimal:
    if v0 <= 0:
        raise ValueError('Growth requires a positive initial value')
    return (v1 / v0 - 1) * 100


def symmetric_decomposition(v0: Decimal, v1: Decimal, n0: Decimal, n1: Decimal) -> dict:
    """V=N*A: symmetric exact allocation of the change, not behavioral attribution."""
    if min(v0, v1, n0, n1) <= 0:
        raise ValueError('Positive values and counts required')
    a0, a1 = v0 / n0, v1 / n1
    breadth = (n1 - n0) * (a0 + a1) / 2
    average = (a1 - a0) * (n0 + n1) / 2
    residual = (v1 - v0) - breadth - average
    if abs(residual) > D('1e-20'):
        raise ArithmeticError('Decomposition failed to reconcile')
    return dict(value_growth_pct=growth(v0,v1), count_growth_pct=growth(n0,n1),
                average_value_growth_pct=growth(a0,a1),
                average_value_start_idr_million=a0*D(1000000),
                average_value_end_idr_million=a1*D(1000000),
                total_change_idr_trillion=v1-v0,
                count_component_idr_trillion=breadth, average_component_idr_trillion=average,
                count_component_share_pct=breadth/(v1-v0)*100 if v1 != v0 else None,
                reconciliation_residual=residual)


def neither_bounds(p: Decimal, q: Decimal) -> tuple[Decimal,Decimal]:
    """Sharp probability bounds on neither event; no independence assumption."""
    probability(p); probability(q)
    return max(D(0), 1-p-q), min(1-p, 1-q)


def witnesses(p: Decimal, q: Decimal) -> list[dict]:
    """Endpoint 2x2 tables prove attainability of the neither-event bounds."""
    low, high = neither_bounds(p,q)
    out=[]
    for label, neither in [('lower',low),('upper',high)]:
        both = neither - 1 + p + q
        cells = dict(both=both, only_first=p-both, only_second=q-both, neither=neither)
        if any(v < 0 for v in cells.values()) or sum(cells.values()) != 1:
            raise ArithmeticError('Invalid witness table')
        out.append(dict(endpoint=label, **cells))
    return out


def joint_bounds(data: dict) -> tuple[list[dict],list[dict]]:
    out, proof = [], []
    # The first event below is the complement of the desired channel condition;
    # the second is financial-report ownership. Their 'neither' cell is the target.
    for year in (2023,2024):
        f = get(data,year,REPORTS,'percent')/100
        n = get(data,year,COUNT,'businesses')
        for name, indicator, complement in [
            ('no_marketplace_and_no_financial_reports',MARKET,False),
            ('marketplace_and_no_financial_reports',MARKET,True),
            ('instant_messaging_and_no_financial_reports',MESSAGING,True),
        ]:
            share = get(data,year,indicator,'percent')/100
            p = 1-share if complement else share
            lo,hi = neither_bounds(p,f)
            # 0.005 percentage points = half the last displayed two-decimal digit.
            eps=D('0.00005')
            pl,pu=max(D(0),p-eps),min(D(1),p+eps)
            fl,fu=max(D(0),f-eps),min(D(1),f+eps)
            rounding_lo=neither_bounds(pu,fu)[0]
            rounding_hi=neither_bounds(pl,fl)[1]
            out.append(dict(year=year,target=name,first_event_share=p,financial_reports_share=f,
                lower_pct=lo*100,upper_pct=hi*100,
                rounding_outer_lower_pct=rounding_lo*100,rounding_outer_upper_pct=rounding_hi*100,
                implied_lower_businesses=n*lo,implied_upper_businesses=n*hi,
                input_keys=f'{year}:{indicator};{year}:{REPORTS};{year}:{COUNT}',
                status=STATUS,interpretation='Plug-in identification bounds; not survey confidence intervals or a transaction-value share'))
            for witness in witnesses(p,f):
                proof.append(dict(year=year,target=name,**witness))
    return out,proof


def economic_tables(data: dict) -> tuple[list[dict],list[dict],list[dict]]:
    expansion=[]; report_counts=[]
    for variant in ('repository_selected_count','alternative_2023_count_scenario'):
        counts={y:get(data,y,COUNT,'businesses') for y in (2022,2023,2024)}
        if variant.startswith('alternative'):
            counts[2023]=ALTERNATIVE_COUNT
        for y0,y1 in ((2022,2023),(2023,2024)):
            v0,v1=(get(data,y,VALUE,'IDR_trillion') for y in (y0,y1))
            expansion.append(dict(count_basis=variant,start_year=y0,end_year=y1,
                initial_businesses=counts[y0],final_businesses=counts[y1],
                **symmetric_decomposition(v0,v1,counts[y0],counts[y1]),
                input_keys=f'{y0}:{VALUE};{y1}:{VALUE};{y0}:{COUNT};{y1}:{COUNT}',
                extra_input=ALTERNATIVE_SOURCE if variant.startswith('alternative') else '',
                interpretation='Nominal aggregate identity; not same-firm growth, real productivity or causal contribution',status=STATUS))
        f0,f1=(get(data,y,REPORTS,'percent')/100 for y in (2023,2024))
        yes0,yes1=counts[2023]*f0,counts[2024]*f1
        no0,no1=counts[2023]-yes0,counts[2024]-yes1
        report_counts.append(dict(count_basis=variant,have_2023_implied_businesses=yes0,have_2024_implied_businesses=yes1,
            have_growth_pct=growth(yes0,yes1),not_have_2023_implied_businesses=no0,not_have_2024_implied_businesses=no1,
            not_have_growth_pct=growth(no0,no1),ownership_change_pp=(f1-f0)*100,
            input_keys=f'2023:{COUNT};2024:{COUNT};2023:{REPORTS};2024:{REPORTS}',
            extra_input=ALTERNATIVE_SOURCE if variant.startswith('alternative') else '',
            interpretation='Products of published estimates, not counts of identified respondents or transitions',status=STATUS))
    v0,v1=(get(data,y,VALUE,'IDR_trillion') for y in (2023,2024))
    m0=get(data,2023,'marketplace_transaction_value','IDR_trillion')
    nm0=get(data,2023,'nonmarketplace_transaction_value','IDR_trillion')
    if abs(v0-m0-nm0)>D('0.015'):
        raise ValueError('2023 exclusive channel partition does not reconcile')
    share=get(data,2024,'marketplace_share_of_transaction_value','percent')/100
    m1=v1*share; nm1=v1-m1
    channels=[]
    for channel,a,b in [('marketplace',m0,m1),('nonmarketplace',nm0,nm1)]:
        channels.append(dict(channel=channel,value_2023_idr_trillion=a,value_2024_derived_idr_trillion=b,
            growth_pct=growth(a,b),change_idr_trillion=b-a,share_of_total_change_pct=(b-a)/(v1-v0)*100,
            share_basis='exclusive_channel_value_not_multiple_response_business_use',
            input_keys='2023:marketplace_transaction_value;2023:nonmarketplace_transaction_value;2023:ecommerce_transaction_value;2024:ecommerce_transaction_value;2024:marketplace_share_of_transaction_value',
            interpretation='Conditional on compatible BPS channel/value definitions across years; 2024 amount uses rounded reported share',status=STATUS))
    return expansion,report_counts,channels


def value_string(value) -> str:
    if value is None:return ''
    if isinstance(value,D):return format(value,'f')
    return str(value)


def write_csv(path: Path, rows: list[dict]):
    fields=list(rows[0]) if rows else ['status']
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader()
        w.writerows({k:value_string(v) for k,v in row.items()} for row in rows)


def result_text(expansion,records,channels,bounds) -> str:
    def f(x):return f'{x:,.2f}'
    e=next(x for x in expansion if x['count_basis']=='repository_selected_count' and x['start_year']==2023)
    alt=next(x for x in expansion if x['count_basis'].startswith('alternative') and x['start_year']==2023)
    r=records[0]
    lines=['# Economic contribution checkpoint','',f'Input snapshot: `{BASE}`. Supplementary author-review results; no main-sample approval or manuscript replacement.','',
      '## 1. The channel lens changes the growth story','',
      '| BPS channel | 2023, IDR tn | 2024 derived, IDR tn | Growth, % | Share of total value increase, % |',
      '|---|---:|---:|---:|---:|']
    for c in channels:lines.append(f"| {c['channel']} | {f(c['value_2023_idr_trillion'])} | {f(c['value_2024_derived_idr_trillion'])} | {f(c['growth_pct'])} | {f(c['share_of_total_change_pct'])} |")
    lines += ['',f"Total nominal value growth is {f(e['value_growth_pct'])}%. The exclusive marketplace component grows much less. This is a concrete comparison between two economic views, not a finding that nonmarketplace sales are missing from official statistics. The latter component includes other online business channels, not only informal messaging sellers. All calculations remain conditional on the BPS cross-year scope concordance. The 2024 channel amounts are derived from total value and a rounded share.",'',
      '## 2. Breadth of participation versus average nominal activity','',
      f"Estimated business numbers rise {f(e['count_growth_pct'])}%, while implied nominal value per estimated business rises {f(e['average_value_growth_pct'])}%. A symmetric arithmetic decomposition allocates {f(e['count_component_share_pct'])}% of the total nominal increase to the business-count term. This is not a panel of continuing firms, an estimate of market entry, real productivity, or causal attribution.",'',
      f"Using the separately flagged alternative 2023 count ({ALTERNATIVE_COUNT:,}) changes business-count growth to {f(alt['count_growth_pct'])}% and implied average-value growth to {f(alt['average_value_growth_pct'])}%. The alternative is a source-conflict sensitivity, not an additional observation or a silent correction.",'',
      '## 3. More recordkeeping and more businesses without statements can coexist','',
      f"Financial-report ownership rises by {f(r['ownership_change_pp'])} percentage points. With the selected counts, the implied number with reports rises {f(r['have_growth_pct'])}% and the implied number without reports rises {f(r['not_have_growth_pct'])}%. These are products of aggregate estimates. Neither an individual transition nor a statistically significant trend has been established.",'',
      '## 4. Information in the marginals without inventing a joint dataset','',
      '| Year | Target business group | Lower, % | Upper, % |',
      '|---|---|---:|---:|']
    for b in bounds:lines.append(f"| {b['year']} | {b['target']} | {f(b['lower_pct'])} | {f(b['upper_pct'])} |")
    lines += ['',
      'These are sharp bounds on possible joint shares conditional on the two published marginal point estimates describing the same business population. For marketplace-use share m and financial-report share f, the share with neither lies between max(0,1-m-f) and min(1-m,1-f). No independence, monotonicity or individual-level association is assumed. Endpoint 2x2 tables demonstrate attainability. Rounding-only outer bounds are supplied separately; sampling error is not included. These are not confidence intervals, transaction-value bounds, lack of all records, or evidence that authorities cannot observe a business.', '',
      'The interpretation is reach: a view restricted to marketplace participants or businesses owning financial reports does not cover a substantial part of the population in these published estimates. It does not follow that such businesses lack payment records or appear in no administrative system. BPS is already estimating them. Before paper promotion, the precise questionnaire population and the definition of financial reports must be confirmed; available direct cross-tabulations take precedence over bounds.', '',
      '## Contribution to the original question','',
      'These calculations ask what changes when the commercial ecosystem is viewed through a broader set of observations. They add three comparisons: channel-specific growth versus total growth; participation breadth versus average nominal activity; and joint coverage limits implied by observed marginals. They do not establish hidden wealth, superior productivity or investor mispricing. The methods are standard and no first-in-literature claim is made. The empirical question is whether the applications add something to the closest Indonesian work.', '',
      '## Source and readiness','',
      f'All numerical inputs except the labelled count-conflict scenario come from `{INPUT}` at the pinned snapshot. `source_lineage.csv` gives original publisher URLs, locators, values and question bases. `source_manifest.json` hashes the exact input bytes. Original publisher catalogues were checked in this pass; original PDF downloads failed, so this is not a fresh cell-level verification of all BPS tables.', '',
      'Unresolved before manuscript inclusion: BPS wave/denominator concordance; the conflicting 2023 count; joint-table availability; survey uncertainty; the role of this module relative to the issuer main sample; closest-study overlap. This branch changes neither the existing sample census nor its outstanding Tokopedia exclusion discrepancy.', '']
    return '\n'.join(lines)


def build(root: Path,output: Path) -> dict:
    path=(root/INPUT).resolve();output=output.resolve()
    if path.is_relative_to(output):raise ValueError('Output must not contain source inputs')
    raw=path.read_bytes(); data,lineage=load(path)
    with localcontext() as ctx:
        ctx.prec=40
        expansion,records,channels=economic_tables(data)
        bounds,proof=joint_bounds(data)
    output.mkdir(parents=True,exist_ok=True)
    for name,rows in [('growth_decomposition',expansion),('financial_report_counts',records),
                      ('channel_change',channels),('joint_coverage_bounds',bounds),
                      ('joint_bound_witnesses',proof),('source_lineage',lineage)]:
        write_csv(output/(name+'.csv'),rows)
    manifest=dict(base_commit=BASE,input_path=INPUT,input_git_blob=blob_hash(raw),
                  input_sha256=hashlib.sha256(raw).hexdigest(),source_records=len(lineage),
                  alternative_count=dict(year=2023,value=str(ALTERNATIVE_COUNT),source=ALTERNATIVE_SOURCE,
                                         status='source_conflict_scenario_not_replacement'),
                  sampling_uncertainty_included=False,status=STATUS)
    (output/'source_manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    (output/'RESULTS.md').write_text(result_text(expansion,records,channels,bounds),encoding='utf-8')
    if path.read_bytes()!=raw:raise RuntimeError('Source changed during execution')
    return manifest


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output',type=Path,default=Path('build/contribution_bridge'))
    a=parser.parse_args()
    try:
        result=build(a.repo,a.output)
    except (ValueError,KeyError,OSError,ArithmeticError,csv.Error) as exc:
        parser.exit(1,f'ERROR: {exc}\n')
    print(json.dumps(result,indent=2));print((a.output/'RESULTS.md').read_text())
