# Cleaning and audit decisions

1. Freeze the supplied Google Sheet as `data/raw/responses.json`; preserve all 50 rows and original labels. Export it to CSV without network access during reproduction.
2. Standardize IDs and numerical representation. Normalize code letter case and outer whitespace only. Do not repair confusable characters or award partial credit.
3. Derive correctness from recorded response against ground truth. Pair 28 is `HSX65Z`; AI returned `HSX6HZ`, so it is incorrect. An earlier analysis found this mislabeled correct. The current live export already reflects the correction. Our current snapshot retains the corrected label.
4. Human pairs 22, 29 and 41 are marked incorrect but the answer strings are missing. Retain those explicit failures, flag the missing strings and disclose that they cannot be independently rescored. Do not silently exclude them.
5. Eight human response/time records indicate timeout or give-up; the combined labels do not consistently distinguish those events. Retain failures and missing times. Do not fill every give-up with 20 seconds or count it as a successful solve.
6. AI inability-to-read statements are abstentions, not verified timeouts. No model 20-second deadline was enforced.
7. Timing summaries use explicitly named shared-success or own-success subsets. The presentation uses the 24 shared successes.
8. Derived data-quality issues are written to `results/data_quality.json`. No observations are deleted for looking unusual. No source document or live Sheet is modified by the reproduction pipeline.
