#!/usr/bin/env python3
from __future__ import annotations
import csv, math
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[2]

def read_csv(path):
    with Path(path).open('r', encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def pct(n,o): return (n/o-1)*100

# Advisor-facing row inventory
rows = read_csv(ROOT/'data/longitudinal/kong_empirical_candidate_table_2026-09-10.csv')
direct = [r for r in rows if r['certified_admission'] in {'candidate_scope_pending','candidate_geography_pending','strongest_direct_candidate'}]
assert len(direct) == 13
assert sum(r['ratio_status']=='eligible_direct_pair' for r in direct) == 12
ext = [r for r in rows if r['platform'] in {'Grab','Shopee','Tokopedia'} and not r['certified_admission'].startswith('exclude')]
assert len(ext) == 8
assert sum(r['certified_admission']=='conditional_sensitivity' for r in ext) == 6
assert {(r['platform'],r['period']) for r in rows if r['certified_admission'].startswith('exclude')} == {('Tokopedia','FY2021'),('Bukalapak','FY2024')}

# Direct-candidate scope sensitivity
groups={}
for r in direct: groups.setdefault((r['platform'],r['business_scope']),[]).append(r)
trans=[]
for key,g in groups.items():
    g=sorted(g,key=lambda r:int(r['period'][2:]))
    for a,b in zip(g,g[1:]):
        ya,yb=int(a['period'][2:]),int(b['period'][2:])
        if yb!=ya+1: continue
        tv0,tv1=float(a['transaction_value']),float(b['transaction_value'])
        rv0,rv1=float(a['revenue_value']),float(b['revenue_value'])
        if min(tv0,tv1,rv0,rv1)<=0: continue
        tg,rg=pct(tv1,tv0),pct(rv1,rv0)
        trans.append((key,ya,yb,tg,rg,abs(rg-tg)))
assert len(trans)==9
assert sum((t[3]<0)!=(t[4]<0) for t in trans)==3
assert sum(t[4]>t[3] for t in trans)==6
assert sum(t[3]>t[4] for t in trans)==3
assert math.isclose(median(t[5] for t in trans),42.9401737278,abs_tol=1e-5)

# Box first all-tier H1 execution
box = read_csv(ROOT/'outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_transitions.csv')
assert len(box)==12
assert sum(str(r['opposite_sign']).lower()=='true' for r in box)==2
assert sum(float(r['revenue_minus_transaction_growth_pp'])>0 for r in box)==10
assert sum(float(r['revenue_minus_transaction_growth_pp'])<0 for r in box)==2
assert math.isclose(median(float(r['absolute_growth_difference_pp']) for r in box),42.0165205690,abs_tol=1e-5)

# BPS certification
bps={r['item']:r for r in read_csv(ROOT/'data/bps_official/bps_certification_status_2026-09-10.csv')}
assert bps['2023_to_2024_total_transaction_growth']['value_or_result']=='17.08%'
assert bps['2024_marketplace_component_value']['value_or_result']=='Rp203.58 trillion'
assert bps['2023_to_2024_marketplace_component_growth']['value_or_result']=='1.45%'
assert bps['2023_to_2024_nonmarketplace_component_growth']['value_or_result']=='20.57%'
assert bps['financial_report_ownership_cross_wave_trend']['status']=='guarded_cross_wave_interpretation'
assert bps['province_marketplace_recordkeeping_relationship']['status']=='negative_or_unstable_aggregate_result'

# Blibli vintage sensitivity
v={r['item']:r for r in read_csv(ROOT/'data/longitudinal/blibli_vintage_sensitivity_2026-09-10.csv')}
assert v['FY2023_3P_TPV']['canonical_value']=='49912' and v['FY2023_3P_TPV']['alternative_value']=='49917'
assert abs(float(v['FY2022_to_FY2023_3P_TPV_growth']['difference']))<0.02
assert abs(float(v['FY2023_to_FY2024_3P_TPV_growth']['difference']))<0.02

# Global corroboration
summary={r['metric']:float(r['value']) for r in read_csv(ROOT/'data/global_ecommerce/global_platform_summary.csv')}
assert int(summary['matched_issuer_years'])==48
assert int(summary['annual_transitions'])==40
assert int(summary['clean_scope_transitions'])==29
assert int(summary['opposite_direction_transitions_clean'])==4

# Findings ledger must state both universes and certification boundary
text=(ROOT/'docs/EMPIRICAL_FINDINGS_2026-09-10.md').read_text(encoding='utf-8')
for phrase in [
    '**13 economic periods**', '**12 consecutive transitions**', '**9 direct transitions**',
    '**+1.45%**', '**+20.57%**', '**48 matched issuer-years**',
    'The difference between 12/2/42.02 and 9/3/42.94 is evidence admission'
]:
    assert phrase in text, phrase

print('empirical certification v2 OK')
print({'direct_periods':13,'direct_transitions':9,'direct_reversals':3,'box_all_tier_transitions':12,'box_all_tier_reversals':2})
print({'bps_marketplace_growth':'1.45%','bps_nonmarketplace_growth':'20.57%'})
print({'global_issuer_years':48,'global_clean_transitions':29,'global_clean_reversals':4})
