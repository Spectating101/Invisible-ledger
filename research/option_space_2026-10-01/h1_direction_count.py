"""Direction of take-rate moves for the thesis groups (15 Indonesian and regional pairs, 158 foreign pairs).
Same inputs and pair rules as h1_extended.py. Run from this folder: python3 h1_direction_count.py "$PWD".
Result on 13 Oct 2026: take rate rose in 13 of 15 Indonesian and regional pairs, revenue and transaction value moved in
opposite directions in 2 (Tokopedia 2022-23, Blibli 2024-25); abroad the take rate rose in 103 of 158 pairs (65 percent)."""
import sys, numpy as np, pandas as pd
base=sys.argv[1]
T=pd.read_csv(base+"/tables/transitions_master.csv"); P=pd.read_csv(base+"/tables/l_panel.csv"); S=pd.read_csv(base+"/tables/spinoff_panel.csv")
def trans(df):
    df=df.sort_values(["firm","year"]).copy(); df["m"]=df.R/df.V
    ok=df.groupby("firm").year.diff()==1
    df["dlnm"]=np.where(ok,np.log(df.m)-np.log(df.groupby("firm").m.shift()),np.nan)
    df["gV"]=np.where(ok,df.V/df.groupby("firm").V.shift()-1,np.nan); df["gR"]=np.where(ok,df.R/df.groupby("firm").R.shift()-1,np.nan)
    return df.dropna(subset=["dlnm"])
idn=T[T.set=="IDN_main"][["firm","y1","dlnm","gV","gR"]].rename(columns={"y1":"year"}); idn["gV"]/=100; idn["gR"]/=100
grab=P[P.firm=="Grab"].groupby("year")[["V","R"]].sum().reset_index().assign(firm="Grab on-demand")
goto=P[(P.firm=="GoTo")&(P.seg=="On-demand")][["year","V","R"]].assign(firm="GoTo on-demand")
reg=trans(pd.concat([grab,goto])[lambda d:d.R>0])[["firm","year","dlnm","gV","gR"]]
ind=pd.concat([idn,reg]); 
ext=T[T.set=="EXT_clean"][["firm","y1","dlnm"]]; new=S[(S.flag_1p!="exclude")&S.g_m.notna()].rename(columns={"entity":"firm","g_m":"dlnm"})[["firm","dlnm"]]
fo=pd.concat([ext,new])
print("Indonesian/regional pairs:",len(ind),"firms",ind.firm.nunique())
print("  take rate rose (revenue faster):",int((ind.dlnm>0).sum()))
print("  opposite directions:",int((np.sign(ind.gV)!=np.sign(ind.gR)).sum()))
print(ind.assign(up=ind.dlnm>0,opp=np.sign(ind.gV)!=np.sign(ind.gR))[["firm","year","dlnm","gV","gR","up","opp"]].round(3).to_string(index=False))
print("Foreign pairs:",len(fo),"firms",fo.firm.nunique(),"take rate rose:",int((fo.dlnm>0).sum()), f"share {(fo.dlnm>0).mean():.2f}")
