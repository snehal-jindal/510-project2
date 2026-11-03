"""Normalize representation while retaining all 50 trials and recorded labels.

Scoring rules belong in feature_engineering.py, not manual spreadsheet edits.
Missing times remain empty: a missing time is not a zero-second solve.
"""
from common import ROOT, read_csv, write_csv, normalize

FIELDS = ['pair_id','image_id','correct_code','human_response','human_time_seconds',
          'human_recorded_outcome','ai_response','ai_time_seconds','ai_recorded_outcome']

def main():
    rows = read_csv(ROOT / 'data/raw/responses.csv')
    clean = []
    for row in rows:
        values = list(row.values())
        item = dict(zip(FIELDS, values))
        for key in ['pair_id','image_id']:
            item[key] = str(int(item[key]))
        for key in ['correct_code','human_response']:
            item[key] = normalize(item[key])
        item['ai_response'] = item['ai_response'].strip()  # retain free-text refusal
        for key in ['human_recorded_outcome','ai_recorded_outcome']:
            item[key] = item[key].strip().lower()
        for key in ['human_time_seconds','ai_time_seconds']:
            item[key] = str(float(item[key])) if item[key].strip() else ''
        clean.append(item)
    write_csv(ROOT / 'data/cleaned/responses_cleaned.csv', clean)

if __name__ == '__main__':
    main()
