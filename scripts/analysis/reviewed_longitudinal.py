#!/usr/bin/env python3
"""Source-reviewed overlay for longitudinal development; no main-sample approval.

Builds review tables from immutable repository CSVs plus an explicit correction
ledger. No source value is silently overwritten and no quarter is interpolated.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from collections import defaultdict
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import longitudinal_review as core
D, num, fmt = core.D, core.number, core.fmt
REVIEW = 'research/longitudinal/blibli_q123_source_review.csv'
BASE = 'c2bced48df1cd7a968267d75bda0dfd046012c08'


def measurement_key(r: dict) -> tuple:
    basis = 'pro_forma' if 'pro-forma' in r.get('source_basis','').lower() else 'reported'
    return core.key(r) + (basis,)


def apply_review(rows: list[dict], decisions: list[dict], digest: str) -> tuple[list[dict], list[dict]]:
    result=copy.deepcopy(rows); logs=[]; targets=set()
    for i, decision in enumerate(decisions, 2):
        expected=tuple(num(decision[x]) for x in ('tv','revenue','gpbd'))
        target=(decision['scope'],decision['original_period'],decision['source_url'])
        if target in targets: raise ValueError('Duplicate review decision: '+str(target))
        targets.add(target)
        if decision['action']=='relabel':
            matches=[r for r in rows if r['issuer']=='Blibli/GDN' and (r['scope'],r['period'],r['source_url'])==target]
            if len(matches)!=1: raise ValueError('Review target not unique: '+str(target))
            old=matches[0]
            if tuple(num(old[x]) for x in ('tv','revenue','gpbd')) != expected:
                raise ValueError('Review precondition changed: '+str(target))
            new=next(r for r in result if r['record_id']==old['record_id'])
            p,f,m=core.period_info(decision['reviewed_period'])
            new.update(period=p,frequency=f,tv_months=m,revenue_months=m)
            new['flags']+=';source_reviewed_period_label'
            new['source_status']='period_label_corrected_against_issuer_table'
            new['original_record_id']=old['record_id']
            new['review_decision']=REVIEW+':'+str(i)
            new['record_id']=hashlib.sha256((old['record_id']+'|'+digest+'|'+str(i)).encode()).hexdigest()[:16]
            logs.append(dict(action='relabel',scope=new['scope'],old_period=old['period'],new_period=p,
                             tv=new['tv'],revenue=new['revenue'],source_csv=old['source_csv'],
                             source_csv_row=old['source_csv_row'],source_url=new['source_url'],
                             old_record_id=old['record_id'],new_record_id=new['record_id'],reason=decision['review_note']))
        elif decision['action']=='recover':
            raw=dict(platform='Blibli/GDN',scope=decision['scope'],period=decision['reviewed_period'],
                     unit='IDR billion',tpv=decision['tv'],revenue=decision['revenue'],gpbd=decision['gpbd'],
                     source_url=decision['source_url'],source_page=decision['source_page'],
                     source_file='issuer_Q1_2023_release',status='recovered_reported_column',_line=i)
            new=core.normalize(raw,REVIEW,digest)
            new['flags']+=';recovered_omitted_source_column'
            new['review_decision']=REVIEW+':'+str(i);new['original_record_id']=''
            result.append(new)
            logs.append(dict(action='recover',scope=new['scope'],old_period='',new_period=new['period'],
                             tv=new['tv'],revenue=new['revenue'],source_csv=REVIEW,source_csv_row=i,
                             source_url=new['source_url'],old_record_id='',new_record_id=new['record_id'],reason=decision['review_note']))
        else: raise ValueError('Unknown review action: '+decision['action'])
    for row in result:
        row.setdefault('original_record_id',row['record_id']);row.setdefault('review_decision','')
    return result,logs


def reconcile(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    groups=defaultdict(list)
    for r in rows:
        if r['technical_status']=='period_matched_candidate': groups[measurement_key(r)].append(r)
    candidates=[];conflicts=[]
    for k, group in sorted(groups.items()):
        variants={(num(r['tv']),num(r['revenue'])) for r in group}
        chosen=sorted(group,key=lambda r:(r['source_url'],r['source_csv'],r['source_csv_row']))[0]
        c=dict(chosen,reporting_basis_key=k[-1],source_records=len(group),
               all_record_ids=';'.join(r['record_id'] for r in group),main_admission='not_approved')
        c['value_status']='agree_at_recorded_precision' if len(variants)==1 else 'unresolved_value_conflict'
        if len(variants)>1:
            conflicts.extend(dict(r,conflict_key='|'.join(map(str,k))) for r in group)
            for field in ('tv','revenue','gpbd','difference','monetization_rate','ecosystem_ratio'):c[field]=''
            c['ratio_status']='blocked_by_value_conflict';c['record_id']=''
        elif len({num(r['gpbd']) for r in group if r['gpbd']})>1:
            c['gpbd']='';c['flags']+=';gpbd_vintage_conflict'
        candidates.append(c)
    return candidates,conflicts


def rollups(rows: list[dict]) -> list[dict]:
    """Cross-vintage arithmetic screen, not an assumption of economic comparability.

All tested release cells are rounded in IDR billion. The rounding tolerance is
0.5 times the number of terms including the total. Differences above this bound
remain visible; they are NOT automatically corrected or attributed to error.
"""
    series=defaultdict(lambda:defaultdict(list))
    for r in rows:
        if r['issuer']=='Blibli/GDN' and r['technical_status']=='period_matched_candidate':
            series[(r['scope'],r['currency'])][r['period']].append(r)
    out=[]
    specs=[('H1',['Q1','Q2']),('9M',['Q1','Q2','Q3']),('FY',['Q1','Q2','Q3','Q4'])]
    for (scope,currency), periods in sorted(series.items()):
        for year in sorted({p[:4] for p in periods}):
            for total_suffix,components in specs:
                names=[year+total_suffix]+[year+x for x in components]
                if not all(n in periods for n in names): continue
                for metric in ('tv','revenue','gpbd'):
                    sets=[{num(r[metric]) for r in periods[n] if r[metric]!=''} for n in names]
                    common=dict(scope=scope,year=year,total_period=names[0],component_periods=';'.join(names[1:]),
                                metric=metric,currency=currency,unit='billion',tolerance=fmt(D(len(names))/2))
                    if not all(len(s)==1 for s in sets):
                        out.append(dict(common,total='',component_sum='',residual='',status='blocked_by_missing_or_conflicting_vintage'));continue
                    v=[next(iter(s)) for s in sets];res=v[0]-sum(v[1:]);tol=D(len(names))/2
                    out.append(dict(common,total=fmt(v[0]),component_sum=fmt(sum(v[1:])),residual=fmt(res),
                                    status='within_rounding_tolerance' if abs(res)<=tol else 'unreconciled_above_rounding_tolerance'))
    return out


def annual_changes(rows: list[dict]) -> list[dict]:
    """Only comparisons printed in the same release; conflicting same-source rows block."""
    groups=defaultdict(lambda:defaultdict(list))
    for r in rows:
        if r['issuer']=='Blibli/GDN' and r['frequency']=='annual' and r['source_url'] and r['technical_status']=='period_matched_candidate':
            groups[(r['scope'],r['source_url'])][int(r['period'][:4])].append(r)
    out=[]
    for (scope,url),years in sorted(groups.items()):
        for year,bb in sorted(years.items()):
            aa=years.get(year-1)
            if not aa:continue
            if len({(num(r['tv']),num(r['revenue'])) for r in aa})!=1 or len({(num(r['tv']),num(r['revenue'])) for r in bb})!=1:continue
            a,b=aa[0],bb[0];v0,v1,r0,r1=map(num,[a['tv'],b['tv'],a['revenue'],b['revenue']])
            if None in (v0,v1,r0,r1) or min(v0,v1)<=0:continue
            out.append(dict(issuer='Blibli/GDN',scope=scope,from_year=year-1,to_year=year,
                tv_growth_percent=fmt(100*(v1/v0-1)),net_revenue_change_billion=fmt(r1-r0),
                net_revenue_growth_percent=fmt(100*(r1/r0-1)) if r0>0 else '',
                revenue_per_tpv_change_pp=fmt(100*(r1/v1-r0/v0)),source_url=url,
                from_record=a['record_id'],to_record=b['record_id'],interpretation='descriptive_within_release_not_country_or_causal_validation'))
    return out


def coverage(rows: list[dict], candidates: list[dict]) -> list[dict]:
    result=[]
    for issuer,scope,freq in sorted({(r['issuer'],r['scope'],r['frequency']) for r in rows}):
        rs=[r for r in rows if (r['issuer'],r['scope'],r['frequency'])==(issuer,scope,freq)]
        cs=[r for r in candidates if (r['issuer'],r['scope'],r['frequency'])==(issuer,scope,freq)]
        allperiods=sorted({r['period'] for r in rs});matched=sorted({r['period'] for r in cs})
        result.append(dict(issuer=issuer,scope=scope,frequency=freq,source_records=len(rs),
            unique_periods=len(allperiods),period_matched_periods=len(matched),basis_variant_keys=len(cs),
            conflicting_value_keys=sum(c['value_status']=='unresolved_value_conflict' for c in cs),
            nonpositive_ratio_keys=sum(c['ratio_status']=='nonpositive_denominator_or_tv' for c in cs),
            excluded_records=sum(r['technical_status'].startswith('exclude') for r in rs),periods=';'.join(matched),
            main_sample_status='not_approved'))
    return result


def export_csv(path: Path, rows: list[dict], empty_fields=('status',)) -> None:
    fields=list(dict.fromkeys(k for r in rows for k in r)) or list(empty_fields)
    core.write_csv(path,rows,fields)


def build(root: Path, output: Path) -> dict:
    root=root.resolve();output=output.resolve()
    files=core.FILES+(REVIEW,)
    if output==root or any((root/p).is_relative_to(output) for p in files):raise ValueError('Output overlaps inputs')
    rows=[];hashes=[]
    for path in core.FILES:
        records,digest=core.read_rows(root,path)
        hashes.append(dict(path=path,sha256=digest,source_rows=len(records)))
        rows.extend(core.normalize(r,path,digest) for r in records)
    decisions,digest=core.read_rows(root,REVIEW)
    hashes.append(dict(path=REVIEW,sha256=digest,source_rows=len(decisions)))
    before_rollups=rollups(rows)
    reviewed,log=apply_review(rows,decisions,digest)
    candidates,conflicts=reconcile(reviewed)
    after_rollups=rollups(reviewed);cov=coverage(reviewed,candidates);changes=annual_changes(reviewed)
    output.mkdir(parents=True,exist_ok=True)
    tables={'source_records_original':rows,'source_records_reviewed':reviewed,'review_changes':log,
            'candidate_periods':candidates,'value_conflicts':conflicts,'coverage':cov,
            'rollup_checks_before':before_rollups,'rollup_checks_after':after_rollups,
            'within_release_annual_changes':changes,'input_hashes':hashes,
            'excluded_records':[r for r in reviewed if r['technical_status'].startswith('exclude')]}
    tables['blibli_3p_annual_vintages']=[r for r in reviewed if r['issuer']=='Blibli/GDN' and r['scope']=='3P Retail' and r['frequency']=='annual']
    tables['blibli_3p_quarter_vintages']=[r for r in reviewed if r['issuer']=='Blibli/GDN' and r['scope']=='3P Retail' and r['frequency']=='quarter']
    for name,table in tables.items():export_csv(output/(name+'.csv'),table)
    summary=dict(base_commit=BASE,original_input_records=len(rows),reviewed_source_records=len(reviewed),
        relabelled_records=sum(r['action']=='relabel' for r in log),recovered_reported_records=sum(r['action']=='recover' for r in log),
        distinct_measurement_keys=len(candidates),unresolved_value_conflicts=sum(c['value_status']=='unresolved_value_conflict' for c in candidates),
        excluded_period_pairs=len(tables['excluded_records']),main_sample_approved=False,
        rollup_unreconciled_before=sum(r['status']=='unreconciled_above_rounding_tolerance' for r in before_rollups),
        rollup_unreconciled_after=sum(r['status']=='unreconciled_above_rounding_tolerance' for r in after_rollups),
        coverage=cov,note='Measurement keys include overlapping groups and segments and alternative reporting bases. Not an independent sample N. Unreconciled cross-vintage totals require source investigation.')
    (output/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    for entry in hashes:
        if hashlib.sha256((root/entry['path']).read_bytes()).hexdigest()!=entry['sha256']:raise RuntimeError('Input changed: '+entry['path'])
    return summary


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2]);p.add_argument('--output',type=Path,default=Path('build/longitudinal'));a=p.parse_args()
    try:s=build(a.repo,a.output)
    except (ValueError,OSError,KeyError) as exc:p.exit(1,f'ERROR: {exc}\n')
    print(json.dumps({k:v for k,v in s.items() if k!='coverage'},indent=2))
    for f in ('coverage.csv','review_changes.csv','rollup_checks_after.csv','within_release_annual_changes.csv'):
        print('REVIEW_BEGIN '+f);print((a.output/f).read_text());print('REVIEW_END '+f)

if __name__=='__main__':main()
