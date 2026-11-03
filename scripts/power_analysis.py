"""Reproduce exact McNemar power calculations for planning and sensitivity analysis."""
import numpy as np
from scipy.stats import binom
from common import ROOT, write_csv

def power_grid(phuman_only,pai_only,max_n=500):
    q=phuman_only+pai_only; conditional=np.zeros(max_n+1)
    for m in range(1,max_n+1):
        k=np.arange(m+1)
        reject=binom.sf(k-1,m,.5)<=.05
        conditional[m]=binom.pmf(k,m,phuman_only/q)[reject].sum()
    # Average over the random number of disagreements, not just its expectation.
    return [float(np.dot(binom.pmf(np.arange(n+1),n,q),conditional[:n+1])) for n in range(max_n+1)]

def main():
    scenarios=[]
    for ph,pa in [(.2,.1),(.25,.1),(.3,.1),(.35,.1)]:
        powers=power_grid(ph,pa)
        scenarios.append(dict(human_only_probability=ph,ai_only_probability=pa,assumed_difference=ph-pa,
            power_at_50=powers[50],minimum_n_for_80_percent=next(i for i,p in enumerate(powers) if p>=.8)))
        if ph==.3:
            write_csv(ROOT/'results/power_curve.csv',[dict(n=n,power=powers[n]) for n in range(10,141)])
    write_csv(ROOT/'results/power_sensitivity.csv',scenarios)

if __name__ == '__main__':
    main()
