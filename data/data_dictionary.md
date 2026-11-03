# Data dictionary

Each row is one matched image/person/AI trial. Pair IDs are study IDs, not names. No participant names or demographics were collected in this table.

| Cleaned column | Meaning / units |
| --- | --- |
| `pair_id` | Integer study identifier 1–50 |
| `image_id` | Same identifier used in numbered image document and PNG filename |
| `correct_code` | Researcher-supplied six-character ground truth; uppercase |
| `human_response` | Exact recorded human code apart from case/outer whitespace normalization; blank if absent/unrecorded |
| `human_time_seconds` | Recorded human elapsed seconds; blank when not recorded |
| `human_recorded_outcome` | Original success/failure/timeout/give-up label, lowercased |
| `ai_response` | Recorded first model answer or inability-to-read text |
| `ai_time_seconds` | Displayed “Worked for…” seconds, not equivalent to human elapsed time |
| `ai_recorded_outcome` | Researcher-entered model outcome, retained even if a response requires rescoring |

All additional columns in `data/processed/features.csv` are specified in [feature engineering](../docs/feature_engineering.md). Correctness is 1/0; flag fields are 1/0; absent numeric values stay empty. Whole-code failure is not the same as a missing observation: a recorded timeout is an observed unsuccessful attempt and remains in the accuracy denominator.

The raw JSON is the connector's header-plus-values array. Its nulls are preserved; raw CSV represents nulls as empty cells. Raw and cleaned data are both provided. The image manifest records original PNG paths, pixel dimensions and SHA-256 checksums; the correct-code join is `pair_id` to `correct_code` in the response table.
