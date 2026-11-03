"""Descriptive timing only: a significance test cannot repair different clocks."""
import numpy as np
from common import ROOT, load_features, write_csv

def summary(values):
    x=np.asarray(values,dtype=float)
    return dict(n=len(x),mean=float(x.mean()),median=float(np.median(x)),sd=float(x.std(ddof=1)),
        q1=float(np.quantile(x,.25)),q3=float(np.quantile(x,.75)),minimum=float(x.min()),maximum=float(x.max()))

def main():
    rows=load_features();output=[]
    for subset in ['shared_success','own_success']:
        for who in ['human','ai']:
            eligible=[r for r in rows if r[who+'_time_seconds'] and (int(r['shared_success_timing_eligible']) if subset=='shared_success' else int(r[who+'_correct']))]
            output.append(dict(subset=subset,reader=who,**summary([r[who+'_time_seconds'] for r in eligible])))
    write_csv(ROOT/'results/timing_summary.csv',output)

if __name__ == '__main__':
    main()
