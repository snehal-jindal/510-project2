"""Turn the frozen connector export into CSV; this did not collect human trials.

The raw JSON snapshot preserves original labels and nulls. No Google login is
needed for reproduction. See docs/study_protocol.md for manual collection.
"""
import csv
import json
from common import ROOT

def main():
    values = json.loads((ROOT / 'data/raw/responses.json').read_text())
    with (ROOT / 'data/raw/responses.csv').open('w', newline='') as f:
        csv.writer(f).writerows(values)
    print(f'Exported {len(values)-1} recorded pairs to raw CSV')

if __name__ == '__main__':
    main()
