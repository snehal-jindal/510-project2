# Feature engineering: explicitly implemented

**Script:** [`scripts/feature_engineering.py`](../scripts/feature_engineering.py). Run it after `clean_data.py`, or use `run_analysis.py` for dependency order. Output: [`data/processed/features.csv`](../data/processed/features.csv).

Feature engineering is relevant even though this is not an ML training project. It converts recorded strings and outcome labels into variables needed for paired inference and transparent exploratory analysis. No model is trained, no preprocessing is fit on the test outcomes, and no train/test performance claim is made.

| Derived feature | Purpose |
| --- | --- |
| `human_correct`, `ai_correct` | Entire normalized response matches known code; explicit wrong/no-answer human records retained as failures |
| `accuracy_difference` | Human correctness minus AI correctness; values −1, 0, +1; mean is the marginal accuracy gap |
| `paired_outcome` | Both correct, human only, AI only, neither correct; builds matched table and exact test |
| `shared_success_timing_eligible` | Both correct and both times present; prevents silently comparing different success subsets |
| `code_length`, `digit_count`, `letter_count` | Checks code length and describes post hoc composition groups; not randomized causal predictors |
| `human_response_missing`, `human_time_missing` | Data-quality indicators; missing values not zero-filled |
| `human_failure_string_unavailable` | Three recorded incorrect answers have no original string, limiting independent rescoring |
| `human_no_answer` | Missing response with a recorded timeout/give-up outcome; distinct from a missing wrong string |
| `ai_abstained` | Explicit inability to read; does not imply an AI deadline was enforced |
| `ai_edit_distance` | Exploratory Levenshtein distance for actual AI transcriptions, blank for abstentions |

Only case and surrounding whitespace are normalized. Visually confusable characters remain distinct. The raw sheet and recorded labels remain available for audit. Missing human strings remain missing. Ages were not collected, and partial character accuracy is not used for the human–AI comparison.
