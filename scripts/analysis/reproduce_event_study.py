"""Recompute Invisible Ledger CARs and Table 10 from auditable inputs.

Fail-closed design:
- QoQ exists only when the immediately preceding CALENDAR quarter exists.
- Event date is taken from event_session_ledger_working.csv; missing session dates abort.
- Excluding-contaminated specifications abort while any required contamination flag is unknown/candidate.
- No old Table 10 number is hard-coded.

Requires: pandas, numpy, scipy
"""
from pathlib import Path
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr

ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'data'; M=ROOT/'market_data'
panel=pd.read_csv(D/'clean_event_panel_accounting.csv')
events=pd.read_csv(D/'event_session_ledger_working.csv')
cont=pd.read_csv(D/'contamination_ledger_working.csv')

# Join event information.
df=panel.merge(events, on=['platform','fiscal_year','quarter'], how='left')
df=df.merge(cont, on=['platform','fiscal_year','quarter'], how='left')

if df['event_session_date'].isna().any() or (df['event_session_date'].fillna('').str.strip()=='').any():
    missing=df.loc[df['event_session_date'].fillna('').str.strip()=='',['platform','fiscal_year','quarter']]
    raise RuntimeError('Event-session dates still missing; verify before CAR calculation:\n'+missing.to_string(index=False))

mapping={'Grab':('GRAB.csv','IXIC.csv'),'Sea':('SE.csv','GSPC.csv'),'GoTo':('GOTO.JK.csv','JKSE.csv')}

def load_close(path):
    x=pd.read_csv(path)
    x.columns=[c.lower() for c in x.columns]
    if 'date' not in x: raise ValueError(f'{path}: no date column')
    close_col='close' if 'close' in x else None
    if close_col is None: raise ValueError(f'{path}: no close column')
    x['date']=pd.to_datetime(x['date']).dt.normalize()
    x=x[['date',close_col]].dropna().drop_duplicates('date').sort_values('date')
    x['ret']=x[close_col].pct_change()
    return x

cars=[]
for plat,(sf,bf) in mapping.items():
    s=load_close(M/sf).rename(columns={'close':'stock_close','ret':'stock_ret'})
    b=load_close(M/bf).rename(columns={'close':'bench_close','ret':'bench_ret'})
    z=s.merge(b,on='date',how='inner').sort_values('date').reset_index(drop=True)
    z['ar']=z['stock_ret']-z['bench_ret']
    for _,r in df[df.platform==plat].iterrows():
        d=pd.Timestamp(r.event_session_date).normalize()
        hits=z.index[z.date==d].tolist()
        if not hits: raise RuntimeError(f'{plat} {r.fiscal_year}Q{r.quarter}: event session {d.date()} not in merged market data')
        i=hits[0]
        if i<1 or i+1>=len(z): raise RuntimeError('Insufficient +/-1 window')
        win=z.loc[i-1:i+1]
        cars.append({'platform':plat,'fiscal_year':r.fiscal_year,'quarter':r.quarter,
                     'event_session_date':d.date().isoformat(),'CAR_m1_p1':win.ar.sum(),
                     'AR_m1':win.ar.iloc[0],'AR_0':win.ar.iloc[1],'AR_p1':win.ar.iloc[2]})
car=pd.DataFrame(cars)
df=df.merge(car,on=['platform','fiscal_year','quarter','event_session_date'],how='left')
df.to_csv(D/'event_study_results_recomputed.csv',index=False)

# Build post-break indicator (legacy Table 10 design: 2024Q1+).
df['period_num']=df.fiscal_year*4+df.quarter
df['post_break']=df.period_num >= 2024*4+1

# Use decimal CAR, not percentage points.
def corr_frame(xvar, mask, name):
    z=df.loc[mask,[xvar,'CAR_m1_p1']].dropna()
    if len(z)<3: return {'specification':name,'N':len(z),'pearson_r':np.nan,'pearson_p':np.nan,'spearman_r':np.nan,'spearman_p':np.nan}
    pr,pp=pearsonr(z[xvar],z.CAR_m1_p1)
    sr,sp=spearmanr(z[xvar],z.CAR_m1_p1)
    return {'specification':name,'N':len(z),'pearson_r':pr,'pearson_p':pp,'spearman_r':sr,'spearman_p':sp}

# Contamination-dependent rows are not allowed until every row is decisively yes/no.
flags=df['guidance_contaminated_working'].astype(str).str.lower()
if flags.isin(['unknown','candidate','nan','']).any():
    unresolved=df.loc[flags.isin(['unknown','candidate','nan','']),['platform','fiscal_year','quarter','guidance_contaminated_working']]
    print('CAR output written, but final Table 10 contamination subsets are BLOCKED. Resolve:\n', unresolved.to_string(index=False))
    # still produce all-event rows only
    specs=[corr_frame('ecosystem_ratio',pd.Series(True,index=df.index),'Level — all'),
           corr_frame('ratio_qoq',df['ratio_qoq'].notna(),'QoQ — all'),
           corr_frame('ecosystem_ratio',df.post_break,'Level — post-break'),
           corr_frame('ratio_qoq',df.post_break & df['ratio_qoq'].notna(),'QoQ — post-break')]
else:
    clean=flags.eq('no')
    specs=[
      corr_frame('ecosystem_ratio',pd.Series(True,index=df.index),'Level — all'),
      corr_frame('ecosystem_ratio',clean,'Level — excluding contaminated'),
      corr_frame('ratio_qoq',df['ratio_qoq'].notna(),'QoQ — all'),
      corr_frame('ratio_qoq',clean & df['ratio_qoq'].notna(),'QoQ — excluding contaminated'),
      corr_frame('ecosystem_ratio',df.post_break,'Level — post-break'),
      corr_frame('ratio_qoq',df.post_break & df['ratio_qoq'].notna(),'QoQ — post-break'),
      corr_frame('ecosystem_ratio',df.post_break & clean,'Level — post-break + uncontaminated'),
      corr_frame('ratio_qoq',df.post_break & clean & df['ratio_qoq'].notna(),'QoQ — post-break + uncontaminated'),
    ]
pd.DataFrame(specs).to_csv(D/'table10_recomputed.csv',index=False)
print(pd.DataFrame(specs).to_string(index=False))
