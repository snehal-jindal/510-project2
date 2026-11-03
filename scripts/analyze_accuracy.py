"""Primary paired inference, effect sizes, intervals and labeled exploration."""
import numpy as np
from scipy.stats import binomtest
from common import ROOT, load_features, write_csv, write_json

def wilson(k,n):
    z=1.959963984540054; p=k/n; den=1+z*z/n
    center=(p+z*z/(2*n))/den
    half=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return [float(center-half),float(center+half)]

def analyze(rows):
    h=np.array([int(r['human_correct']) for r in rows]);a=np.array([int(r['ai_correct']) for r in rows])
    counts=[int(sum((h==x)&(a==y))) for x,y in [(1,1),(1,0),(0,1),(0,0)]]
    both,b,c,neither=counts;n=len(rows);m=b+c
    if not m:
        p1=p2=1.; odds=None; odds_ci=[None,None]
    else:
        p1=float(binomtest(b,m,.5,alternative='greater').pvalue)
        p2=float(binomtest(b,m,.5).pvalue)
        # Conditional matched odds interval; distinct from a marginal risk interval.
        ci=binomtest(b,m).proportion_ci(method='exact')
        odds=b/c if c else None
        odds_ci=[ci.low/(1-ci.low),ci.high/(1-ci.high) if ci.high<1 else None]
    rng=np.random.default_rng(20261102)
    bootstrap=rng.multinomial(n,np.array(counts)/n,size=200000)
    risk_ci=np.quantile((bootstrap[:,1]-bootstrap[:,2])/n,[.025,.975]).tolist()
    return dict(n_pairs=n,human_correct=int(h.sum()),ai_correct=int(a.sum()),
        human_accuracy=float(h.mean()),ai_accuracy=float(a.mean()),
        paired_counts=dict(zip(['both_correct','human_only','ai_only','neither_correct'],counts)),
        accuracy_difference=float((h-a).mean()),paired_bootstrap_95_ci=risk_ci,
        human_accuracy_wilson_95=wilson(int(h.sum()),n),ai_accuracy_wilson_95=wilson(int(a.sum()),n),
        exact_mcnemar_one_sided_p=p1,exact_mcnemar_two_sided_p=p2,
        matched_odds_ratio=odds,matched_odds_ratio_exact_95_ci=odds_ci,
        alpha=.05,decision='fail_to_reject' if p1>.05 else 'reject',
        bootstrap_resamples=200000,bootstrap_seed=20261102)

def main():
    rows=load_features();result=analyze(rows)
    write_json(ROOT/'results/statistical_results.json',result)
    write_csv(ROOT/'results/accuracy_summary.csv',[
        dict(reader=who,correct=result[who+'_correct'],trials=result['n_pairs'],accuracy=result[who+'_accuracy'],
             ci_lower=result[who+'_accuracy_wilson_95'][0],ci_upper=result[who+'_accuracy_wilson_95'][1]) for who in ['human','ai']])
    write_csv(ROOT/'results/paired_outcomes.csv',[dict(outcome=k,count=v) for k,v in result['paired_counts'].items()])
    # Describe post hoc digit groups; do not test or claim a causal digit effect.
    digit=[]
    for k in sorted({int(r['digit_count']) for r in rows}):
        group=[r for r in rows if int(r['digit_count'])==k]
        digit.append(dict(digit_count=k,n=len(group),human_correct=sum(int(r['human_correct']) for r in group),ai_correct=sum(int(r['ai_correct']) for r in group)))
    write_csv(ROOT/'results/exploratory_digit_groups.csv',digit)

if __name__ == '__main__':
    main()
