# Experimental design and collection protocol

## Recorded design

- **Question:** higher human exact-code accuracy than one selected model on striped codes?
- **Units:** 50 distinct human volunteers, each assigned one fresh image; identical images paired with 50 model responses. The image/person pair is the sampling unit.
- **Recruitment:** available volunteers entering/leaving Duke library, a convenience sample. This is not probability sampling. We observed that our sample was mostly young; ages were not formally recorded.
- **Inputs:** six-character mixed letter/number codes. The exact 50 PNGs are supplied, not regenerated approximations. Each is 1000×240 pixels. Original image-to-ID order follows numbered labels in the provided Google Doc.
- **Rendering setting:** we used the maximum stripe-width/spacing setting of 16, described as “16 pts.” The archived browser implementation calls this parameter `pitch` and applies it in canvas pixels; do not interpret it as a verified physical point measurement. Font/rasterization/screen zoom can affect perception.
- **AI:** GPT-6.1 Sol, medium effort; fresh chat for every image; first response recorded. Exact prompt: **“read the random code hidden in the image”**.
- **Human deadline:** 20 seconds. Incorrect, timeout and give-up outcomes remain unsuccessful.
- **AI time:** displayed “Worked for…” value, without an equivalent enforced 20-second cutoff. It is not a validated measure of human-comparable reading time.
- **Primary endpoint:** all six characters correct. Case and surrounding whitespace are ignored; confusions such as 2/Z and 5/S are not corrected.
- **Secondary measures:** descriptive recorded times. Digit mix is exploratory, not a randomized factor.

## What was not recorded or controlled

The exact collection date, display device/zoom, viewing distance, visual acuity, detailed demographic characteristics, assignment seed, exact stopwatch start/stop behavior and any model-internal tools are not established in the supplied records. We leave these details unspecified. Our raw sheet export date is November 2, 2026; that is **not asserted to be the trial date**. No ordinary-text control was collected. More numbers, O/X similarities and U/J confusions were not prospectively randomized interventions.

## Analysis decisions and chronology

The directional human-superiority hypothesis and paired exact-test approach were discussed before the final analysis. There was no formal preregistration. Sample size 50 was a feasible collection target, not justified by a documented prospective calculation. Power calculations were performed after collection and are identified as planning/sensitivity scenarios. Code settings were selected after pilot exploration; pilot anecdotes are not additional final-study observations.

## Collection software versus analysis reproduction

Human and model trials were conducted manually. `scripts/export_data.py` only serializes the frozen recorded table; it is not evidence of automated collection. The relevant source generator from the earlier project is in `collection/`, with pinned upstream provenance and font notices. For an exact replay of the analyzed stimuli, use the supplied original PNG files. New random code generations are new experimental inputs, not a reproduction of these 50 observations.

## A stronger follow-up

Choose code length or digit mix as a controlled factor, preserve per-character geometry, randomize assignment, add unstriped controls if estimating stripe effects, define one comparable time budget, and plan sample size before collection. Use multiple models and prespecified hint/retry/tool conditions on held-out images. Measure usability and accessibility as well as model failures. Do not keep adding trials until a desired p-value appears.
