"""Integration checks: identity, scoring, source-image integrity and deck agreement."""
import hashlib
import json
import math
from common import ROOT, load_features, read_csv

def main():
    rows=load_features();assert len(rows)==50
    assert {int(r['pair_id']) for r in rows}==set(range(1,51))
    manifest=json.loads((ROOT/'data/image_manifest.json').read_text())
    assert len(manifest)==50
    for image in manifest:
        p=ROOT/image['image_file']
        assert hashlib.sha256(p.read_bytes()).hexdigest()==image['sha256'],p
    assert all(len(r['correct_code'])==6 for r in rows)
    assert sum(int(r['human_correct']) for r in rows)==39
    assert sum(int(r['ai_correct']) for r in rows)==31
    assert sum(int(r['shared_success_timing_eligible']) for r in rows)==24
    assert sum(int(r['human_failure_string_unavailable']) for r in rows)==3
    r=json.loads((ROOT/'results/statistical_results.json').read_text())
    # Exact independent integer arithmetic verifies the conditional binomial tail.
    exact=sum(math.comb(22,k) for k in range(15,23))/2**22
    assert abs(r['exact_mcnemar_one_sided_p']-exact)<1e-12
    assert abs(r['accuracy_difference']-.16)<1e-12
    assert r['paired_bootstrap_95_ci']==[-.02,.34]
    times=read_csv(ROOT/'results/timing_summary.csv')
    for who,mean,median in [('human',9.977916666666667,8.105),('ai',19.541666666666668,18.5)]:
        item=next(t for t in times if t['subset']=='shared_success' and t['reader']==who)
        assert abs(float(item['mean'])-mean)<1e-10
        assert abs(float(item['median'])-median)<1e-10
    assert (ROOT/'presentation/slides.pdf').read_bytes().startswith(b'%PDF')
    assert (ROOT/'presentation/slides.pptx').read_bytes().startswith(b'PK')
    print('Validated 50 images/pairs, scoring, exact p-value, intervals and slide statistics.')

if __name__ == '__main__':
    main()
