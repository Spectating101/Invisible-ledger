#!/usr/bin/env python3
"""Build a non-destructive longitudinal review ledger; never an approved main sample.

Standard library only. Source CSVs are immutable. Conflicting values block a
canonical choice. Annual, quarterly and cumulative periods remain separate.
Run: python scripts/analysis/longitudinal_review.py --output build/longitudinal
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

D = Decimal
MISSING = {'', 'NA', 'N/A', 'None', 'nan', '-', 'null'}
BLIBLI_FILES = (
    'data/longitudinal/blibli_reported_pairs_all_vintages.csv',
    'data/longitudinal/blibli_additional_reported_pairs.csv',
)
FILES = BLIBLI_FILES + (
    'data/longitudinal/blibli_prospectus_2019_2020_candidates.csv',
    'data/longitudinal/bukalapak_annual_candidates.csv',
    'data/longitudinal/indonesia_platform_year_extension.csv',
    'data/longitudinal/annual_extension_panel_preliminary.csv',
    'data/quarterly/clean_event_panel_accounting.csv',
)
SCOPES = ('1P Retail', '3P Retail', 'Institutions', 'Physical Stores')
FIELDS = ('record_id','issuer','scope','period','frequency','tv_months','revenue_months',
          'currency','unit','tv','revenue','gpbd','difference','monetization_rate',
          'ecosystem_ratio','ratio_status','directness','geography_status','source_status',
          'technical_status','flags','source_url','source_locator','source_file',
          'source_csv','source_csv_row','source_csv_sha256','source_basis')


def number(value: str | int | float | Decimal | None) -> Decimal | None:
    if value is None or str(value).strip() in MISSING:
        return None
    text = str(value).strip().replace(',', '')
    if text.startswith('(') and text.endswith(')'):
        text = '-' + text[1:-1]
    try:
        result = D(text)
    except InvalidOperation as exc:
        raise ValueError(f'Not a number: {value!r}') from exc
    if not result.is_finite():
        raise ValueError(f'Nonfinite number: {value!r}')
    return result


def fmt(value: Decimal | None) -> str:
    return '' if value is None else format(value, 'f')


def period_info(period: str) -> tuple[str, str, int]:
    text = re.sub(r'[\s_-]', '', period.upper())
    match = re.fullmatch(r'(?:FY)?(20\d{2})(?:FY)?', text)
    if match:
        return match[1] + 'FY', 'annual', 12
    match = re.fullmatch(r'(20\d{2})Q([1-4])', text)
    if match:
        return text, 'quarter', 3
    match = re.fullmatch(r'Q([1-4])(20\d{2})', text)
    if match:
        return match[2]+'Q'+match[1], 'quarter', 3
    match = re.fullmatch(r'(20\d{2})(?:H1|1H|6M|M6)', text)
    if match:
        return match[1]+'H1', 'cumulative', 6
    match = re.fullmatch(r'(?:H1|1H|6M)(20\d{2})', text)
    if match:
        return match[1]+'H1', 'cumulative', 6
    match = re.fullmatch(r'(20\d{2})(?:9M|M9)', text)
    if match:
        return match[1]+'9M', 'cumulative', 9
    match = re.fullmatch(r'9M(20\d{2})', text)
    if match:
        return match[1]+'9M', 'cumulative', 9
    raise ValueError(f'Unsupported period label (must be reviewed): {period!r}')


def read_rows(root: Path, relative: str) -> tuple[list[dict], str]:
    path = root / relative
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f, strict=True)
        if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError(f'Empty or duplicate header: {relative}')
        result = []
        for i, row in enumerate(reader, 2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f'Column-count mismatch: {relative}, record {i}')
            row['_line'] = i
            result.append(row)
    return result, digest


def metrics(tv: Decimal | None, revenue: Decimal | None) -> dict:
    if tv is None or revenue is None:
        return dict(difference='',monetization_rate='',ecosystem_ratio='',ratio_status='missing_pair')
    if tv <= 0 or revenue <= 0:
        return dict(difference=fmt(tv-revenue),monetization_rate=fmt(revenue/tv) if tv > 0 else '',
                    ecosystem_ratio='',ratio_status='nonpositive_denominator_or_tv')
    return dict(difference=fmt(tv-revenue),monetization_rate=fmt(revenue/tv),
                ecosystem_ratio=fmt((tv-revenue)/revenue),ratio_status='positive_denominator')


def normalize(raw: dict, relative: str, digest: str) -> dict:
    issuer = raw.get('platform', '')
    scope = raw.get('scope', '')
    period = raw.get('period') or str(raw.get('year', ''))
    unit = raw.get('unit', '')
    tv = raw.get('tpv')
    revenue = raw.get('revenue')
    gpbd = raw.get('gpbd')
    directness = 'source_reported_extraction'
    geography = 'not_country_isolated_pending_review'
    flags = []
    if relative.endswith('blibli_prospectus_2019_2020_candidates.csv'):
        unit = 'IDR million'; tv = raw['tpv_idr_million']; revenue = raw['net_revenue_idr_million']; gpbd = raw['gpbd_idr_million']
    elif relative.endswith('bukalapak_annual_candidates.csv'):
        scope = 'Group'; unit = 'IDR million'; tv = raw['tpv_idr_million']; revenue = raw['revenue_idr_million']
        geography = 'group_overseas_operations_unallocated'
    elif relative.endswith('indonesia_platform_year_extension.csv'):
        tv = raw['transaction_value_native']; revenue = raw['platform_revenue_native']
        scope = 'Indonesia construction' if issuer in ('Grab','Shopee') else 'E-commerce segment'
        issuer = 'Tokopedia' if 'Tokopedia' in issuer else issuer
        geography = 'Indonesia_target_model_dependent' if issuer in ('Grab','Shopee') else 'Indonesia_aligned_segment'
        directness = 'derived_country_construction' if issuer in ('Grab','Shopee') else 'source_reported_segment'
        if issuer == 'Tokopedia' and period == 'FY2021':
            flags.append('full_year_tv_post_acquisition_revenue')
    elif relative.endswith('annual_extension_panel_preliminary.csv'):
        tv = raw['gmv_or_gtv']; revenue = raw['matched_revenue']; unit = raw['currency']+' '+raw['unit']
        scope = {'Grab':'Mobility + Deliveries','Sea':'Shopee e-commerce','GoTo':'Group'}[issuer]
        directness = 'preserved_analytic_output_not_reaudited'
    elif relative.endswith('clean_event_panel_accounting.csv'):
        period = f"{raw['fiscal_year']}Q{raw['quarter']}"
        tv = raw['gmv_or_gtv']; revenue = raw['matched_revenue']; unit = raw['currency']+' '+raw['unit']
        scope = {'Grab':'Mobility + Deliveries','Sea':'Shopee e-commerce','GoTo':'Group'}[issuer]
        directness = 'preserved_analytic_output_source_mapped'
    if issuer == 'Blibli/GDN' and scope == '3P Retail':
        flags.append('commerce_and_OTA_not_goods_only')
    if issuer == 'Blibli/GDN' and scope == 'Group':
        flags.append('group_overlaps_segments')
    normalized_period, frequency, months = period_info(period)
    tv_months = int(raw.get('tpv_months', months)); revenue_months = int(raw.get('revenue_months', months))
    if tv_months != revenue_months:
        flags.append('unequal_measurement_periods')
    if issuer == 'GoTo' and normalized_period.startswith(('2024','2025','2026')):
        flags.append('post_Tokopedia_deconsolidation_or_comparable_basis')
    unit_lower = unit.lower().replace('_', ' ')
    currency = 'IDR' if 'idr' in unit_lower else 'USD' if 'usd' in unit_lower else raw.get('currency','')
    if 'trillion' in unit_lower:
        factor = D(1000)
    elif 'billion' in unit_lower:
        factor = D(1)
    elif 'million' in unit_lower:
        factor = D('0.001')
    elif 'thousand' in unit_lower:
        factor = D('0.000001')
    else:
        raise ValueError(f'Unknown unit: {unit!r} in {relative}')
    values = [number(v) for v in (tv,revenue,gpbd)]
    values = [v*factor if v is not None else None for v in values]
    tv,revenue,gpbd = values
    technical = 'period_matched_candidate'
    if 'full_year_tv_post_acquisition_revenue' in flags or tv_months != revenue_months:
        technical = 'exclude_period_mismatch'
    if tv is None or revenue is None:
        technical = 'exclude_missing_pair'
    result = dict(issuer=issuer,scope=scope,period=normalized_period,frequency=frequency,
                  tv_months=tv_months,revenue_months=revenue_months,currency=currency,unit='billion',
                  tv=fmt(tv),revenue=fmt(revenue),gpbd=fmt(gpbd),directness=directness,
                  geography_status=geography,source_status=raw.get('status',raw.get('use_status','')),
                  technical_status=technical,flags=';'.join(flags),source_url=raw.get('source_url',''),
                  source_locator=raw.get('source_page',raw.get('pdf_page',raw.get('locator',raw.get('tpv_locator','')))),
                  source_file=raw.get('source_file',''),source_csv=relative,source_csv_row=raw['_line'],
                  source_csv_sha256=digest,source_basis=raw.get('basis',raw.get('comparability_note',raw.get('geography_note',''))))
    result.update(metrics(tv,revenue))
    if technical.startswith('exclude'):
        result.update(difference='',monetization_rate='',ecosystem_ratio='',ratio_status='excluded_pair')
    seed = json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    result['record_id'] = hashlib.sha256(seed).hexdigest()[:16]
    return result


def key(row: dict) -> tuple:
    return tuple(row[k] for k in ('issuer','scope','period','frequency','currency','tv_months','revenue_months'))


def reconcile(rows: list[dict]) -> tuple[list[dict],list[dict]]:
    groups = defaultdict(list)
    for row in rows:
        if row['technical_status']=='period_matched_candidate': groups[key(row)].append(row)
    candidates, conflicts = [], []
    for _, group in sorted(groups.items()):
        signatures = {(number(r['tv']),number(r['revenue'])) for r in group}
        chosen = sorted(group,key=lambda r:(r['source_url'],r['source_csv'],r['source_csv_row']))[0]
        item = dict(chosen)
        item['source_records'] = len(group)
        item['all_record_ids'] = ';'.join(r['record_id'] for r in group)
        item['main_admission'] = 'pending_researcher_and_advisor_review'
        item['value_status'] = 'agree_at_recorded_precision' if len(signatures)==1 else 'unresolved_value_conflict'
        if len(signatures)>1:
            for row in group:
                conflicts.append(dict(row,conflict_key='|'.join(str(x) for x in key(row))))
            for field in ('tv','revenue','gpbd','difference','monetization_rate','ecosystem_ratio'):
                item[field]=''
            item['ratio_status']='blocked_by_value_conflict'
            item['record_id']=''
        elif len({number(r['gpbd']) for r in group if r['gpbd']})>1:
            item['gpbd']='';item['flags']+=';gpbd_vintage_conflict'
        candidates.append(item)
    return candidates,conflicts


def coverage_table(rows: list[dict], candidates: list[dict]) -> list[dict]:
    groups = defaultdict(list)
    for row in rows: groups[(row['issuer'],row['scope'],row['frequency'])].append(row)
    result=[]
    for group_key, group in sorted(groups.items()):
        can=[r for r in candidates if (r['issuer'],r['scope'],r['frequency'])==group_key]
        periods=sorted(set(r['period'] for r in group))
        result.append(dict(zip(('issuer','scope','frequency'),group_key),source_records=len(group),
            unique_reported_periods=len(periods),periods=';'.join(periods),period_matched_keys=len(can),
            uncontested_value_keys=sum(r['value_status']=='agree_at_recorded_precision' for r in can),
            conflicting_value_keys=sum(r['value_status']=='unresolved_value_conflict' for r in can),
            nonpositive_ratio_keys=sum(r['ratio_status']=='nonpositive_denominator_or_tv' for r in can),
            excluded_source_records=sum(r['technical_status'].startswith('exclude') for r in group),
            main_sample_approved=False))
    return result


def within_release_changes(rows: list[dict]) -> list[dict]:
    """Only adjacent annual pairs explicitly present in the same source release."""
    groups=defaultdict(dict)
    for row in rows:
        if row['issuer']=='Blibli/GDN' and row['frequency']=='annual' and row['source_url'] and row['technical_status']=='period_matched_candidate':
            groups[(row['issuer'],row['scope'],row['source_url'])][int(row['period'][:4])]=row
    output=[]
    for (_,scope,url), years in sorted(groups.items()):
        for year,b in sorted(years.items()):
            a=years.get(year-1)
            if not a: continue
            v0,v1,r0,r1=(number(a['tv']),number(b['tv']),number(a['revenue']),number(b['revenue']))
            if any(x is None for x in (v0,v1,r0,r1)) or v0<=0 or v1<=0: continue
            output.append(dict(issuer='Blibli/GDN',scope=scope,from_year=year-1,to_year=year,
                tv_growth_percent=fmt((v1/v0-1)*100),net_revenue_change_billion=fmt(r1-r0),
                net_revenue_growth_percent=fmt((r1/r0-1)*100) if r0>0 else '',
                revenue_per_tpv_change_pp=fmt((r1/v1-r0/v0)*100),
                source_url=url,from_record=a['record_id'],to_record=b['record_id'],
                interpretation='within_release_descriptive_change_not_causal_or_Indonesia_isolated'))
    return output


def write_csv(path: Path, rows: list[dict], fields=None) -> None:
    fields=list(fields or (rows[0].keys() if rows else ['no_records']))
    with path.open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');writer.writeheader();writer.writerows(rows)


def build(root: Path, output: Path) -> dict:
    root=root.resolve();output=output.resolve()
    if output==root or any(output==root/p or (root/p).is_relative_to(output) for p in FILES):
        raise ValueError('Output must not contain the input source files')
    output.mkdir(parents=True,exist_ok=True)
    rows=[];snapshots=[]
    for relative in FILES:
        values,digest=read_rows(root,relative)
        snapshots.append(dict(path=relative,sha256=digest,source_rows=len(values)))
        rows.extend(normalize(row,relative,digest) for row in values)
    candidates,conflicts=reconcile(rows)
    coverage=coverage_table(rows,candidates)
    changes=within_release_changes(rows)
    write_csv(output/'source_records.csv',rows,FIELDS)
    write_csv(output/'candidate_periods.csv',candidates)
    write_csv(output/'value_conflicts.csv',conflicts,FIELDS+('conflict_key',))
    write_csv(output/'coverage.csv',coverage)
    write_csv(output/'excluded_records.csv',[r for r in rows if r['technical_status'].startswith('exclude')],FIELDS)
    write_csv(output/'within_release_annual_changes.csv',changes)
    write_csv(output/'input_hashes.csv',snapshots)
    summary=dict(source_records=len(rows),candidate_period_keys=len(candidates),
                 conflicting_period_keys=sum(c['value_status']=='unresolved_value_conflict' for c in candidates),
                 excluded_source_records=sum(r['technical_status'].startswith('exclude') for r in rows),
                 approved_main_sample_records=0,coverage=coverage,
                 note='Counts are by series, period and scope, not an additive independent sample N. This audit does not certify original source cells or geographic comparability.')
    (output/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    for snapshot in snapshots:
        if hashlib.sha256((root/snapshot['path']).read_bytes()).hexdigest()!=snapshot['sha256']:
            raise RuntimeError('Input changed during build: '+snapshot['path'])
    return summary


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output',type=Path,default=Path('build/longitudinal'))
    parser.add_argument('--print-review',action='store_true')
    args=parser.parse_args()
    try:
        summary=build(args.repo,args.output)
    except (ValueError,OSError,KeyError,csv.Error) as exc:
        parser.exit(1,f'ERROR: {exc}\n')
    print(json.dumps(summary,indent=2))
    if args.print_review:
        for name in ('coverage.csv','within_release_annual_changes.csv'):
            print('REVIEW_FILE_BEGIN '+name);print((args.output/name).read_text());print('REVIEW_FILE_END '+name)
        print('BLIBLI_3P_ALL_RECORDS_BEGIN')
        records,_=read_rows(args.output,'source_records.csv')
        compact=[{k:r[k] for k in ('issuer','scope','period','tv','revenue','gpbd','technical_status','source_url','source_csv','source_csv_row')} for r in records if r['issuer']=='Blibli/GDN' and r['scope']=='3P Retail']
        print(json.dumps(compact,separators=(',',':')))
        print('BLIBLI_3P_ALL_RECORDS_END')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
