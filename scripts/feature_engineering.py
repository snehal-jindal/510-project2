"""Explicit, auditable feature engineering for this paired statistical study.

This is not ML model training. Engineered variables turn recorded strings into
scorable outcomes and identify eligible timing pairs. Code composition features
are exploratory only; they were not randomized treatment assignments.
"""
from common import ROOT, read_csv, write_csv, write_json, normalize

def score(response, label, truth, human=False):
    text = normalize(response)
    if text:
        return int(text == normalize(truth))
    # Three human wrong attempts have no original string. Retain their explicit
    # failure labels, but do not pretend the missing strings were independently scored.
    if human and label in {'incorrect','timeout/gave up','timeup','time up','gave up','timed out'}:
        return 0
    raise ValueError('Missing answer without an interpretable unsuccessful outcome')

def edit_distance(a, b):
    """Levenshtein distance for exploratory AI transcription errors only."""
    prev = list(range(len(b)+1))
    for i, ca in enumerate(a, 1):
        row = [i]
        for j, cb in enumerate(b, 1):
            row.append(min(row[-1]+1, prev[j]+1, prev[j-1]+(ca != cb)))
        prev = row
    return prev[-1]

def engineer(row):
    out = dict(row)
    code = row['correct_code']
    h = score(row['human_response'], row['human_recorded_outcome'], code, human=True)
    a = score(row['ai_response'], row['ai_recorded_outcome'], code)
    refusal = normalize(row['ai_response']).replace(' ', '') in {'CANNOTREAD','CANTREAD',"CAN'TREAD"}
    out.update(human_correct=h, ai_correct=a, accuracy_difference=h-a,
        paired_outcome={(1,1):'both_correct',(1,0):'human_only',(0,1):'ai_only',(0,0):'neither_correct'}[(h,a)],
        code_length=len(code), digit_count=sum(c.isdigit() for c in code),
        letter_count=sum(c.isalpha() for c in code),
        human_response_missing=int(not row['human_response']),
        human_time_missing=int(not row['human_time_seconds']),
        human_failure_string_unavailable=int(not row['human_response'] and row['human_recorded_outcome']=='incorrect'),
        human_no_answer=int(not row['human_response'] and row['human_recorded_outcome']!='incorrect'),
        ai_abstained=int(refusal),
        shared_success_timing_eligible=int(h and a and bool(row['human_time_seconds']) and bool(row['ai_time_seconds'])),
        ai_edit_distance='' if refusal else edit_distance(code,normalize(row['ai_response'])))
    return out

def main():
    rows = [engineer(r) for r in read_csv(ROOT / 'data/cleaned/responses_cleaned.csv')]
    write_csv(ROOT / 'data/processed/features.csv', rows)
    audit = {'human_wrong_strings_unavailable':[r['pair_id'] for r in rows if r['human_failure_string_unavailable']],
        'human_missing_times':[r['pair_id'] for r in rows if r['human_time_missing']],
        'label_disagreements':[{'pair_id':r['pair_id'],'reader':who} for r in rows for who in ['human','ai']
            if int(r[who+'_correct']) != int(r[who+'_recorded_outcome']=='correct')]}
    write_json(ROOT / 'results/data_quality.json', audit)

if __name__ == '__main__':
    main()
