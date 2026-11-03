"""Shared paths and small file helpers; no network access or hidden credentials."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_csv(path):
    with Path(path).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def write_csv(path, rows, fields=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields or list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')

def normalize(value):
    # Do not collapse meaningful character differences such as 2/Z or 5/S.
    return (value or '').strip().upper()

def load_features():
    return read_csv(ROOT / 'data/processed/features.csv')
