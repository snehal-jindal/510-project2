# ant.ai — expanded presentation and study notes

10 slides. Aim for 7–8 minutes. Speak only the LIVE SCRIPT; study the explanations for understanding and Q&A.

## Slide 1 — live script (~25 seconds)

Can AI miss something a person can read? Our project, ant.ai, began with document protection and experiments with color and motion. We narrowed that idea to a question we could measure: how accurately do people and one AI model read the same striped codes?

### Study guide and Q&A

HOW TO USE THESE NOTES
The LIVE SCRIPT is the part intended for the presentation. The rest is a study guide, not a script to read aloud. The timing targets sum to about seven and a half minutes before a small amount of transition time; rehearse once and stay below eight minutes.

Five methods form the statistical story: descriptive accuracy, Wilson intervals for each accuracy, an exact paired McNemar test, a paired bootstrap interval for the difference, and an exact-test power-planning calculation. Mean/median/boxplots describe timing; they are not a timing significance test. These methods answer different questions and should not be counted as five independent discoveries.

PURPOSE AND BACKSTORY
The opening image is an invitation to look at a visual puzzle. It is not a scored observation in the 50-pair experiment. Keep this opening short so the statistics receive most of the seven minutes.

The broader ant.ai exploration included colored dots, striped text, motion-revealed text, and word-to-code connections. Those earlier trials helped identify interesting directions, but they were informal and used different inputs and prompts. Do not mix their outcomes into the statistical dataset. This presentation's numerical results concern only the 50 six-character striped-code image pairs.

Motion is useful context: people can integrate changing visual information over time, while a frozen frame can discard the very information that reveals the message. Therefore, an AI failing on a screenshot of moving text does not establish that it cannot read the complete video. Earlier animations were recoverable with tools. Ghost Font by Eric Lu / Mixfont is a design reference for motion-based communication, not an invention claimed by this project. See https://www.mixfont.com/ghost-font .

Striped text is also related to prior adversarial OCR / visual perception work. We are not claiming to have invented stripes or proved novelty. ArmorOCR / AdvSpot provides relevant background: https://arxiv.org/abs/2608.20122 . The contribution here is a small paired human-AI experiment, a documented analysis, and follow-up design questions.

Q&A: Is this an AI model you trained? No. We generated visual inputs and evaluated an existing model. There is no neural-network training or weight update in this study.

Q&A: Why move away from document protection? Some stronger distortions also made human reading effortful. Short CAPTCHA-style tasks create a narrower, measurable use case. A usable CAPTCHA still requires much more than a difficult image.

## Slide 2 — live script (~40 seconds)

CAPTCHAs are checks websites use to separate people from automated programs, or bots. Familiar examples ask us to identify images or read distorted text. If bots can solve those tasks, the visual puzzle becomes a weaker barrier against spam and other automated abuse. Modern defenses also use browser and behavioral signals, so we are not saying all CAPTCHAs are obsolete. We are testing one possible ingredient: a task that people solve more reliably than AI.

### Study guide and Q&A

WHAT CAPTCHA MEANS
The acronym is Completely Automated Public Turing test to tell Computers and Humans Apart. For this audience, the plain-language definition in the live script is enough. A bot is software that automates actions; it does not have to use AI. An AI vision model can be one component of a bot that reads a challenge.

HOW IT WORKS
A conventional visual CAPTCHA presents a challenge, receives an answer, and checks whether it matches an expected answer. Real systems need server-side verification, expiring challenges, limits on retries, resistance to replay, and protection against exposing the expected answer. Some services use risk and browser signals without showing a puzzle to every visitor. A correct response to a picture is therefore not necessarily equivalent to bypassing a deployed security system.

HOW TO USE THE EXISTING SCREENSHOT
The slide's screenshot is motivation, not the evidence for this statistical experiment. Do not repeat the screenshot's exact model-performance or news claims as independently verified facts. A news headline about a CAPTCHA-style game does not establish that all commercial CAPTCHA defenses are broken.

A stronger primary reference is Plesner, Vontobel and Wattenhofer, Breaking reCAPTCHAv2 (2024): https://arxiv.org/abs/2409.08831 . It evaluates an automated visual solver under a particular setup; it does not justify a claim that every CAPTCHA or present-day anti-bot system is obsolete. For modern layered checks, see https://developers.cloudflare.com/cloudflare-challenges/concepts/how-challenges-work/ .

SECURITY AND ACCESSIBILITY
The motivation is reducing automated abuse while allowing legitimate people to access a service. Difficult puzzles can exclude people with low vision, visual-processing differences, or other disabilities. A real deployment needs accessible alternatives. W3C background: https://www.w3.org/TR/turingtest/ .

The F5 article supplied during planning discusses bots attacking LLM applications and OWASP-related risks. It is broad security context, not direct evidence about this striped-code experiment or CAPTCHA performance. The supplied YouTube video was not used as evidence because its contents were not retrieved reliably.

Q&A: Are you demonstrating a production CAPTCHA? No. This is a perception experiment motivated by CAPTCHA design. The website is a research playground, not a secure verification service.

PRE-EXISTING NOTES (preserved)
This slide talks about our motivation for our research question

CAPTCHAs: Can we still separate people from bots?
What: A CAPTCHA is a website check designed to tell people apart from automated programs, called bots.
How: Familiar examples ask you to read distorted text or select images. Websites use these checks to reduce automated spam, fake accounts, and abuse.
The challenge: AI can now solve some visual CAPTCHAs, weakening the assumption that “a person can solve this, but a computer cannot.”
Today: Modern systems also check browser and behavioral signals—protection goes beyond solving a picture.
Our question: Can humans read striped codes more accurately than a selected AI model?

## Slide 3 — live script (~30 seconds)

Our null hypothesis is equal accuracy for humans and the selected AI model. Our alternative is that humans are more accurate. We defined success strictly: the entire six-character code must match. Getting most characters right still counts as unsuccessful. Our main question concerns accuracy, not speed. We chose a directional question because we wanted to investigate a possible human advantage.

### Study guide and Q&A

BEGINNER EXPLANATION
A hypothesis is a testable statement. The null, written H0, gives us a reference model to test against. Here the reference is no difference in the probability of correctly reading a code under the two testing protocols. The alternative, H1, is the direction we are investigating: higher human accuracy.

If pH is human success probability and pA is AI success probability, the slide writes H0: pH = pA and H1: pH > pA. More formally, the one-sided null includes pH <= pA; equality is the boundary used to calculate the exact test. Do not get sidetracked by this formal refinement in the seven-minute talk unless asked.

ACCURACY
Accuracy is the number of fully correct responses divided by all 50 trials for that reader type. A correct answer must match all six characters. The analysis ignores letter case and leading/trailing whitespace only; it does not turn a 2 into a Z or a 5 into an S. We do not award partial credit. This makes sense for CAPTCHA-style codes, where one wrong character often prevents acceptance.

Wrong responses, giving up, and reaching the time limit are all unsuccessful for the primary binary outcome. Binary means there are only two values for analysis: correct = 1 and unsuccessful = 0. Detailed outcome labels remain useful for understanding why a response failed.

DIRECTIONAL TESTING
A one-sided test asks about a human advantage specifically. A two-sided test asks about a difference in either direction. The directional hypothesis was stated in our planning before these final results were analyzed. We must not choose a one-sided test merely because it produces a smaller p-value after seeing results. For transparency, the two-sided result is available in the notes for slide 7.

IMPORTANT SCOPE
Our operational comparison is humans with up to 20 seconds versus one model's first response without an equivalent 20-second cutoff. This is not a claim about innate intelligence or all human/AI reading abilities. The particular image settings, prompts, time allowances, and model settings define the question we actually measured.

CLASS CONNECTION
The Statistics workbook, Chapter 3, emphasizes stating hypotheses before collecting and interpreting data, selecting a test that fits the design, and distinguishing failure to reject H0 from accepting it. The central result will follow exactly that logic.

## Slide 4 — live script (~60 seconds)

We recruited 50 volunteers at Duke library, using a convenience sample. Each person saw one unique six-character striped image and had up to 20 seconds to answer. We tested the identical images in fresh GPT-6.1 Sol chats at medium effort, recording the first response. That gives us 50 matched pairs, rather than two unrelated groups. We recorded the code, responses, outcomes, and times. Before analysis, we checked answers against the known codes, retained timeouts as failures, and corrected one AI success label that did not match its recorded answer.

### Study guide and Q&A

EXPERIMENTAL UNIT AND MATCHING
One pair consists of one particular image, one person's response to that image, and one AI response to exactly that image. There are 50 pairs, not 100 independent experimental units. The same model is tested on different images; these are not 50 different AI models. One human saw one image, so we did not test human learning across multiple examples. The intended design uses 50 distinct participants.

The reader type, human or AI, is the comparison condition. The primary dependent variable, or measured result, is whole-code correctness. Recorded response times are secondary and descriptive. Stripe width, code length, font and image settings were intended to stay fixed; code content varied. These settings should be recorded in the final methods and repository. Do not invent pixel values, exact prompt text, random seeds, screen distance, or dates if they were not logged.

SAMPLING AND RANDOMIZATION
Approaching available people walking through a library is convenience recruitment, even if the researcher did not consciously prefer particular people. It is not probability-based random sampling from all Duke students or the public. Randomly generating a code is separate from randomly sampling people. The source of code randomness and exact prompt should be documented as far as the records allow.

PROTOCOL CONFIRMED BY THE RESEARCHER
Model: GPT-6.1 Sol, medium effort. Every image used a fresh chat. Humans had at most 20 seconds. AI timing came from the displayed Worked for label, and no equivalent AI 20-second cutoff was enforced. Fresh chats reduce carryover from prior answers and hints, but they do not guarantee repeatability across model updates or repeated generations. Model details are researcher-reported; this study does not independently verify provider internals.

CLEANING AND AUDIT TRAIL
Compare responses with the known code. Pair 28 has correct code HSX65Z and AI response HSX6HZ. Its original success label was wrong; the analysis counts it as an AI failure. The live sheet was subsequently corrected. Preserve the raw snapshot and document the cleaning rule rather than silently overwriting history.

There are 39 correct human responses, three recorded incorrect attempts whose original answer text is missing (pairs 22, 29 and 41), and eight timeout/give-up outcomes. Those three missing strings cannot be independently rescored, but their explicit recorded incorrect labels support retaining them as failures. Eight human times are missing. Keep the distinction between an absent answer and an unrecorded answer string.

Time limit records should distinguish a confirmed 20-second timeout from an early give-up. Do not fill an early give-up with 20 seconds unless that was the actual stopping time. A 20-second timeout is a stopping time, not a successful solve time.

ASSUMPTIONS
Pairs should be independent across trials, with no repeated participant learning, cross-participant coaching, or shared-chat examples. Matching handles image difficulty within a pair. Convenience recruitment limits generalization even when the test calculation is correct. There is no unstriped control, so this study compares readers on striped inputs rather than estimating the causal effect of adding stripes.

## Slide 5 — live script (~45 seconds)

Humans got 39 of the 50 codes right: 78 percent. AI got 31 right: 62 percent. So the observed gap is 16 percentage points in favor of humans. Each dot is an accuracy estimate; each line is a 95 percent confidence interval, showing uncertainty from having only 50 trials. These are not fixed population scores. We kept wrong answers, giving up and timeouts in the denominator. The important next step is to compare the two responses to each image together, rather than treating them as unrelated groups.

### Study guide and Q&A

HOW THE NUMBERS WERE CALCULATED
Human accuracy = 39 / 50 = 0.78 = 78%. AI accuracy = 31 / 50 = 0.62 = 62%. The absolute difference is 0.78 - 0.62 = 0.16, or 16 percentage points. Percentage points measure the distance between two percentages. Do not say the difference is merely 16 percent: a relative increase would use a different denominator, and is not the effect size presented here.

The dot-and-whisker plot uses the same 0–100% scale for both readers. A dot is the observed accuracy; a whisker is its individual 95% Wilson confidence interval. Each estimate uses all 50 responses. The paired uncertainty interval for the human-minus-AI difference appears on slide 7.

KEEP ALL UNSUCCESSFUL TRIALS
Dropping people who could not read the code would change the question to performance among successful people and artificially improve reported accuracy. For the primary question, wrong answers, giving up, and timeouts count as unsuccessful. There are 11 human failures and 19 AI failures. AI failures include both incorrect guesses and explicit inability to read.

OPTIONAL UNCERTAINTY FOR EACH ACCURACY
Approximate 95% Wilson intervals are 64.8%–87.2% for human accuracy and 48.2%–74.1% for AI accuracy. These individual intervals are not the correct object to subtract or use as an overlap test for the paired comparison. Slide 7 instead estimates uncertainty for the human-minus-AI difference while preserving matching.

WHAT IS THE EFFECT SIZE?
Effect size describes how large an observed difference is, rather than how surprising it is statistically. Here it is 16 percentage points, equivalent to eight additional correct responses per 50 images in this sample. It is an estimate, not a guarantee of eight additional successes in every future set. We do not use Cohen's d for this primary binary outcome; the accuracy difference is more natural and directly interpretable.

Q&A: Did it work? In some cases humans succeeded while AI failed, so the design produced interesting examples. However, AI still solved 31 codes and people failed 11. That is not a demonstrated secure CAPTCHA, nor evidence of universally readable protected documents.

Q&A: Why not declare victory at 78 versus 62? Sampling variability and matching matter. A numerical lead can exist in a sample without sufficiently strong evidence for the population-level directional claim. The next two slides explain this distinction.

READ THIS CHART FROM LEFT TO RIGHT
The horizontal axis is accuracy, not time. Mint is human; peach is AI. The human dot is at 78, with a line extending approximately from 64.8 to 87.2. The AI dot is at 62, with a line extending approximately from 48.2 to 74.1. The longer AI line reflects slightly greater binomial uncertainty at these observed proportions; it is not evidence of less consistent thinking or a measure of variation in individual character predictions.

WHY WILSON INTERVALS?
A proportion is a fraction of trials that succeeded. A naive normal interval uses the sample proportion plus or minus roughly two estimated standard errors. With small samples or extreme proportions, that interval can behave poorly and can extend outside zero to one. Wilson intervals use a score-based calculation that stays within the permissible range and is a useful default for a single binomial proportion. Here the method does not require fitting a neural network or assuming that binary observations themselves are normally distributed.

A worked numerical intuition: 39 successes out of 50 yields 78%, but 39 is not the only success count we might have obtained with a different comparable sample. The interval communicates that we have an estimate, not a perfectly known underlying accuracy. The same applies to AI performance over new codes, even though it is the same model.

DO NOT TEST BY EYEBALLING THE LINES
The two intervals overlap. That overlap alone is not a general rule for accepting or rejecting a difference, particularly when observations are paired. Individual intervals summarize each proportion separately; the inferential question concerns their paired difference. We use the matched image outcomes in the next slide. The picture is descriptive evidence plus uncertainty, not a replacement for the test.

WHAT DOES A CONFIDENCE LEVEL MEAN?
If this interval-building procedure were repeated on many comparable samples under its assumptions, about 95% of the constructed intervals would cover the underlying proportion. It is not a promise that 95% of people will read the codes, nor a statement that an individual response is 95% reliable. Because recruitment was by convenience, the intervals do not magically extend to every demographic or every AI model.

## Slide 6 — live script (~50 seconds)

Each square is one of our 50 images, grouped by outcome. Both readers were correct on 24 images, and both failed on four. The mint squares are the 15 images only the human solved. The peach squares are the seven only AI solved. Those 22 disagreements tell us which side performed better. We use an exact McNemar test because the results are paired and each is either correct or unsuccessful. If accuracy were equal, disagreements should not systematically favor one side. We ask how unusual 15 human wins would be out of 22 disagreements.

### Study guide and Q&A

READING THE PAIRED TABLE
Both correct = 24. Human correct and AI unsuccessful = 15. Human unsuccessful and AI correct = 7. Both unsuccessful = 4. The four counts add to 50. Human successes are 24 + 15 = 39. AI successes are 24 + 7 = 31. This is a useful arithmetic check.

WHY A PAIRED TEST?
Some images may be intrinsically easy or hard. Pairing ensures that a human and AI are compared on the exact same image. Their outcomes on that image may therefore be related. A test for two independent groups would ignore this structure. McNemar's test is designed for two matched binary outcomes. A paired t-test or Wilcoxon test is not needed for this correct/incorrect comparison.

WHY THE DISAGREEMENTS MATTER
When both readers are correct, neither outperforms the other on that image. When both fail, neither wins either. Only the 22 discordant pairs tell us the direction of the accuracy difference: 15 favor humans, seven favor AI. The overall difference is (15 - 7) / 50 = 0.16. Concordant pairs still belong in the denominator and the uncertainty analysis; the conditional exact test focuses on disagreements.

EXACT CALCULATION IN PLAIN LANGUAGE
Imagine that, if there were no accuracy advantage, each disagreement was equally likely to favor humans or AI. With 22 disagreements, the human-win count would follow a binomial distribution with n = 22 and probability 0.5. A binomial distribution describes the number of successes in a fixed number of yes/no trials. The analogy is a fair coin, though the actual observations are reader outcomes.

For the directional alternative, calculate the probability of at least 15 human wins out of 22: sum from k = 15 to 22 of choose(22,k) × 0.5^22. It equals 0.0669002533. In Python, the script uses scipy.stats.binomtest(15, 22, p=0.5, alternative='greater'). This is the one-sided exact conditional McNemar calculation.

WHY EXACT?
Exact means using the relevant finite-sample binomial probabilities instead of a large-sample chi-square approximation. With only 22 disagreements, the exact calculation is straightforward and avoids reliance on that approximation. It does not mean the study is free of sampling or measurement limitations.

ASSUMPTIONS TO EXPLAIN IF ASKED
The outcomes must be correctly paired and scored, pairs must be independent across trials, and the data should be meaningful observations for the stated sampling setup. We do not need a normal distribution for binary outcomes and should not run a Shapiro-Wilk normality test on correctness labels. The exact test does not fix convenience recruitment or unequal time budgets.

METHOD REFERENCES
https://www.statsmodels.org/dev/generated/statsmodels.stats.contingency_tables.mcnemar.html
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html

HOW TO PRESENT THE TILE CHART
There are five rows of ten squares. A square is a matched image pair, not one person plus an additional independent AI sample. The squares are sorted by outcome to make the counts visible; their positions are not trial order, code difficulty, participant age or a learning curve. Slate represents both correct; dark squares represent both unsuccessful. Mint and peach identify the disagreements. Do not say the chart shows which person is represented unless you actually join it to the pair ID.

INTUITIVE COIN EXAMPLE
Suppose two equally accurate readers disagree on 22 images. Under the null model, each disagreement is equally likely to favor one reader or the other. Eleven versus eleven is the most likely split, but thirteen versus nine can happen without a systematic advantage. Fifteen versus seven is less common. The exact test adds the probabilities of 15, 16, 17, 18, 19, 20, 21 or 22 human wins to assess how surprising an outcome at least as favorable to humans would be. We do not test only the probability of exactly 15.

WHY NOT MORE FAMILIAR TESTS?
A two-sample proportion test or a standard chi-square independence test assumes a group structure that discards our matching. Fisher’s exact independence test on two unrelated samples is not the matched-reader test either. ANOVA compares means across conditions and adds nothing necessary to this binary, two-reader question. A paired t-test is designed for numerical differences; although binary data can be manipulated into many forms, exact McNemar is the direct method for this design. We should not run many alternatives and select the most favorable p-value.

AN OPTIONAL SECOND EFFECT SIZE FOR Q&A
Among disagreements, human-only to AI-only success has a matched odds ratio of 15/7 = 2.14. An exact conditional 95% interval, obtained by taking an exact binomial interval for the human share of disagreements and converting probability to odds, is approximately 0.82 to 6.21. It includes one, the no-advantage value for a ratio. This is another way to show uncertainty, not a separate confirmation. It does not mean humans are twice as intelligent or twice as accurate overall. The absolute 16-percentage-point accuracy difference is the more understandable main effect size. The odds-ratio estimate is kept in notes to avoid overloading the slide.

INDEPENDENCE IS ACROSS PAIRS
We deliberately allow a human and AI response within one pair to be related through image difficulty. Across pairs, we assume no participant coaching or shared-chat learning and a meaningful set of fresh codes. Convenience recruitment limits representativeness. The exact computation remains conditional on this design and does not remove those limitations.

## Slide 7 — live script (~65 seconds)

This chart shows what the human-win count could look like if neither side had an accuracy advantage, given 22 disagreements. The observed count is 15. The highlighted bars are outcomes at least that favorable to humans; together their probability is 0.067. That is above the five-percent cutoff, so the test is not conclusive. Does that mean the difference is just noise? No. We observed a lead, but cannot confidently separate a repeatable advantage from sampling variation. The estimated gap is 16 points, with an approximate 95 percent paired interval from minus two to plus 34. The honest conclusion is uncertainty—not proven equality, and not proven human superiority.

### Study guide and Q&A

WHAT A P-VALUE IS
Assuming equal accuracy and conditioning on 22 disagreements, p = 0.067 means there is about a 6.7% probability of observing at least 15 of those disagreements favoring humans. It measures how unusual this directional result would be under the null model.

WHAT A P-VALUE IS NOT
It is not a 6.7% probability that H0 is true. It is not a 93.3% probability that humans are better. It is not the probability that the result was caused by chance. It does not measure the size or importance of the difference.

DECISION AND WORDING
The conventional alpha threshold here is 0.05. Because 0.0669 is larger, the decision is fail to reject H0 at that threshold. Do not say accept H0, prove equality, almost significant, or change alpha to 0.10 after seeing results. A nonsignificant result is a legitimate finding and does not make the project a failure. If equal performance were the scientific objective, an equivalence study with a prespecified meaningful margin would be needed; failure to reject a superiority test does not establish equivalence.

ONE-SIDED VERSUS TWO-SIDED
The directional alternative was stated before this final analysis: human accuracy is greater. That supports the one-sided test. The corresponding two-sided exact p-value is 0.1338005066, or 0.134. It asks about a difference in either direction and leads to the same no-rejection conclusion at 0.05. Report both if the instructor prefers a two-sided convention; do not present the smaller number without explaining its direction.

CONFIDENCE INTERVAL
The estimated effect is 16 percentage points. The reported approximate two-sided 95% paired percentile-bootstrap interval is -2 to +34 percentage points. Negative values mean an AI advantage; positive values mean a human advantage. The zero mark means no difference. The interval includes zero. It suggests that this dataset leaves uncertainty about both the direction and magnitude of the difference.

HOW BOOTSTRAPPING WORKS
Treat the 50 complete human-AI pairs as the units to resample. Draw 50 pairs with replacement, meaning an original pair can appear more than once. Recalculate the accuracy difference. Repeat 200,000 times using NumPy random seed 20261102. The 2.5th and 97.5th percentiles of those differences form the interval. The script implements equivalent multinomial resampling of the four paired categories, preserving the pairing exactly. It does not resample human and AI outcomes independently.

This is an approximate percentile interval, not an exact McNemar confidence interval. It is a two-sided 95% interval, while the main p-value is one-sided. They are complementary summaries and are not mathematically exact inverses. The small, discrete dataset makes interval endpoints coarse. The interval assumes the empirical pairs reasonably represent the sampling process; convenience sampling limits population generalization. A confidence interval quantifies sampling uncertainty under assumptions, not every possible source of bias.

A frequentist 95% interval method is designed to cover the true parameter in about 95% of repeated comparable studies. It does not assign a 95% probability to a fixed parameter after observing the interval.

CLASS CONNECTION
Statistics workbook Chapters 3–4 distinguish hypotheses, significance, p-values, effect sizes and power. The point estimate answers how large; the interval answers how uncertain; the test answers how incompatible with a null model. See also SciPy bootstrap documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html .

READING THE NEW DISTRIBUTION FIGURE
The horizontal axis counts human-only wins out of the 22 disagreements. The vertical axis is the probability of each count under equal accuracy. This is a theoretical null distribution, not a histogram of 50 people’s scores and not a display of model confidence. The center is 11: half the disagreements. The observed count is 15. Peach bars from 15 through 22 form the upper tail. Their heights add to 0.0669002533, shown as 0.067. The bar at 15 alone is smaller; a p-value includes outcomes at least as extreme in the specified direction.

DOES THIS RESULT MEAN THE GAP IS JUST NOISE?
No. The observed gap is an arithmetic fact about the recorded sample. What is uncertain is whether that gap estimates a stable advantage on new comparable trials. A sample difference can contain both a genuine underlying difference and sampling variation; they are not mutually exclusive stories. These data alone do not reveal exactly how much is each. A p-value above 0.05 is not a detector that labels an observation as noise.

Imagine the underlying accuracies were equal. We could still get a 15-versus-seven disagreement split sometimes. Imagine humans really did have an advantage. A sample of only 50 could still produce evidence that fails the cutoff. Both situations are compatible with a nonsignificant result. Distinguishing them reliably requires a stronger, prospectively planned experiment, not a stronger adjective.

WHAT THE 6.7% NUMBER ACTUALLY CONDITIONS ON
It conditions on the equal-accuracy null model and on observing 22 disagreements. It asks about at least 15 favoring humans, under that model. It does not tell us the probability that the null is true, the probability that our result is fake, or the probability that a new experiment will succeed. Calling it a 6.7% chance the results are noise would reverse the conditional statement.

WHY 0.05 IS NOT A CLIFF IN REALITY
The cutoff is a decision convention that should be chosen before analysis. Results just above it should not be described as proven noise, and results just below it should not be described as certain truth. At the chosen threshold our formal decision is no rejection. Keep the estimate, uncertainty, design limitations and practical meaning alongside that binary decision. Do not switch to a 10% cutoff now to obtain a different headline.

THE FINAL INTERPRETATION TO MEMORIZE
We observed a 16-point human lead. The uncertainty interval ranges from a small AI advantage to a substantial human advantage. The directional exact test did not meet the 5% threshold. We therefore have a promising observation, not established superiority. We also have no evidence of equality, because equality was not demonstrated by an equivalence design.

ANALYSIS QUALITY VERSUS POSITIVE RESULTS
Adding more tests would not make the evidence stronger. The academic strength is a correctly matched test, explicit assumptions, an effect size, a confidence interval, transparent missing-data rules and an honest conclusion. The two-sided p-value and optional odds-ratio interval are robustness/interpretation aids, not opportunities to change which result is called primary.

## Slide 8 — live script (~45 seconds)

The dots show recorded times for the same 24 images both readers solved correctly. The boxes summarize their distributions; the line inside each box is the median. Human median time was 8.11 seconds and AI median time was 18.50; the table also shows means. But the clocks differ. Human time was measured directly, while AI time came from the interface label. Humans also stopped at 20 seconds and AI did not. We therefore describe these numbers without treating them as a fair reading-speed contest or adding a misleading speed-test p-value.

### Study guide and Q&A

WHY ONLY 24 IMAGES IN THIS TABLE?
Both readers correctly solved the same 24 images. Restricting to this shared subset makes the image set identical for this descriptive comparison. However, it conditions on successful outcomes for both readers, so it is not representative of all 50 trials and can introduce selection bias. Do not claim the table estimates typical performance on every challenge or all participants.

EXACT NUMBERS
For the 24 shared successes, human mean = 9.9779166667 s and median = 8.105 s. AI mean = 19.5416666667 s and median = 18.5 s. The slide rounds to two decimals: 9.98, 8.11, 19.54 and 18.50. Human sample SD = 5.25 s; AI sample SD = 8.54 s. We omit SD from the visual table to keep the slide minimal. The average AI-minus-human recorded-time difference is 9.56 s; its median is 9.99 s. The difference of the two medians is 10.40 s, which is a different quantity from the median of paired differences. Do not interchange them.

MEAN AND MEDIAN, FROM ZERO
The mean is the arithmetic average: add all recorded times and divide by the number of observations. The median is the middle of the ordered times; with an even count, it is the average of the two central times. A few long observations can move a mean substantially, while the median is less sensitive. Neither number is automatically the correct answer to every question, so reporting both helps describe the data. This follows the descriptive-statistics section of the Statistics workbook, Chapter 1.

WHY THE MEASUREMENTS ARE NOT EQUIVALENT
The human measure is researcher-recorded elapsed time; its exact start/stop and whether answering includes speech or typing must be documented from actual procedure. The AI values are the displayed Worked for labels. Those labels are not a validated equivalent of human reading time or a precisely measured end-to-end stopwatch latency. Do not assume they include or exclude particular server, tool, or network stages unless the interface documentation establishes that. They are also rounded to whole seconds here.

Humans stopped at 20 seconds; some AI values exceeded 20. Thus the accuracy comparison is operationally human-within-20-seconds versus AI-first-response, not a matched-time contest. Do not retrospectively discard long AI responses to improve the conclusion. The recorded labels are not sufficiently comparable for that rescue.

WHY NO TIMING P-VALUE?
A paired t-test or Wilcoxon test can be calculated from numbers, but it cannot make different clocks and unequal budgets comparable. A significant result could be about measurement procedures rather than reading ability. Keeping timing descriptive is a deliberate methodological choice, not a missing analysis to conceal.

MISSING AND UNSUCCESSFUL TRIALS
Do not replace missing solve times with zero or assign 20-second successful solve times to failed participants. Confirmed 20-second timeouts can be stored as stopping times, with an explicit timeout indicator. An early give-up has its actual stopping time if measured. Survival/time-to-event methods might support a carefully designed future study, but the current mixed labels and clocks do not support a clean time-to-correct-answer inference.

HOW TO READ THE NEW BOX-AND-DOT PLOT
Each dot is one recorded time, and there are 24 dots per reader type. A small vertical offset prevents repeated values from hiding each other; vertical position within a row has no meaning. The horizontal position is the time. The box runs from the 25th percentile to the 75th percentile: the middle half of recorded values. The strong vertical line inside the box is the median. Whiskers follow the usual rule of extending to observations within 1.5 interquartile ranges of the box; all actual observations are shown as dots whether or not they fall beyond a whisker.

A percentile tells us where a value sits in an ordered list. The 25th percentile has roughly one quarter of observations at or below it. The interquartile range is the distance between the 25th and 75th percentiles; it is a measure of spread. A wide box indicates more spread in these recorded times, not greater uncertainty about the population mean. A boxplot is not a confidence-interval plot; contrast this with slide 5.

MEAN, MEDIAN, STANDARD DEVIATION, STANDARD ERROR
The mean is the average observation; the median is the middle ordered value. Standard deviation describes the spread of individual observations. Standard error describes the sampling uncertainty of an estimator such as a mean and typically shrinks as sample size grows. They are not interchangeable. None resolves the different-clock problem in this study.

WHY WE DO NOT ADD A T-TEST JUST TO LOOK STATISTICAL
The 24 shared-success times form matched observations, but the two clocks measure different processes and the subset excludes failures. A paired t-test could test a numerical difference between these recorded quantities, yet that would not establish a meaningful cognitive reading-speed advantage. A Wilcoxon signed-rank test would not repair comparability either. Good statistical procedure includes declining an unsupported inferential claim.

WHAT A BETTER TIMING STUDY WOULD NEED
Define the same event boundary, such as image available to complete final answer received, and record it consistently. Use the same deadline or explicitly model different deadlines. Decide how early give-ups and wrong answers are handled. Measure correct-answer times together with success probability, because a fast wrong answer is not equivalent to a fast correct one. Record unsuccessful trials as such rather than converting them into successful 20-second solves.

READY ANSWER IF ASKED WHETHER HUMANS WERE FASTER
Their recorded times were lower on the shared-success subset. Our measurement procedures do not support claiming they read faster than the model. This distinction protects the accuracy findings from an exaggerated secondary claim.

## Slide 9 — live script (~45 seconds)

Power asks how often a study would detect a specified real advantage. This curve is an illustrative future-planning scenario, not another result from the participants. If human-only success occurred on 30 percent of images and AI-only success on ten percent—a 20-point advantage—50 pairs would have about 68 percent power. Around 67 pairs would reach 80 percent power under those assumptions. This calculation happened after collection, so it cannot justify our sample size in advance. It explains why sample size deserves planning, rather than promising that more data would prove our hypothesis.

### Study guide and Q&A

POWER IN PLAIN ENGLISH
Power is the probability that a study detects an effect, using its prespecified test and significance threshold, if a particular effect really exists. An 80% power target means that, in repeated comparable studies with the assumed effect, about eight in ten would reject the null. It does not mean that this particular result has an 80% probability of being true, or that 80% of participants succeed.

WHAT WE CAN HONESTLY SAY ABOUT N = 50
The sample size was a feasible target under the collection deadline. We do not have a documented completed prospective power calculation justifying 50 before collection. Therefore, do not label the current calculation a priori or imply that a power target was met in advance. This is a retrospective sensitivity/planning analysis with explicitly hypothetical assumptions. It is a useful component of the project, but it does not erase the design limitation.

SPECIFIC ASSUMPTIONS
Assume independent pairs and probabilities 0.30 for human-only success and 0.10 for AI-only success. The remaining 0.60 are agreements; for this exact test's power, their allocation between both correct and both unsuccessful is not needed. The implied human-minus-AI difference is 0.20, or 20 percentage points. The disagreement probability is 0.40. Conditional on a disagreement, the probability it favors humans is 0.30 / 0.40 = 0.75. Use the same one-sided exact McNemar test at alpha = 0.05.

CALCULATION
For each possible number m of disagreements among n pairs, m follows Binomial(n, 0.40). For each possible human-win count k among those disagreements, k follows Binomial(m, 0.75) under this assumed alternative. Determine whether the exact null tail P[Binomial(m,0.5) >= k] is at most 0.05. Sum the probabilities of all such rejection cases. This exact enumeration gives power 0.6785 for n = 50. Searching sample sizes gives the first n with at least 80% power as 67, under these specific assumptions.

SENSITIVITY
With a 10-point advantage and assumed human-only/AI-only probabilities 0.20/0.10, power at n = 50 is about 28%, and about 199 pairs are needed for 80%. For 0.25/0.10, a 15-point advantage, power is about 49%, with about 103 pairs needed. For 0.35/0.10, a 25-point advantage, power is about 82%, with about 48 pairs needed. These are scenarios, not facts about the population. Do not compute observed power from the exact observed effect and treat it as new evidence.

DO NOT COLLECT UNTIL SIGNIFICANT
The next study should choose its sample size and analysis before starting. Do not keep adding participants to this dataset until p drops below 0.05. That changes the false-positive behavior unless a valid sequential design is planned. A larger follow-up can still return nonsignificant results, and a larger sample does not repair biased recruitment or incomparable timing.

OTHER LIMITATIONS
Library volunteers are a convenience sample, observed to be mostly young; formal age measurements were not provided. This limits generalization to older adults, people with low vision and the broader public. There is one reported model and effort setting; no inference across all LLMs is possible. Fresh chats reduce context carryover but do not test informed attackers, hints or retries. Stripe width was selected after pilot exploration, so the conclusion is limited to that selected design. Without an unstriped control, the study does not isolate the causal effect of the pattern.

CLASS CONNECTION
Statistics workbook Chapter 4 covers the dependence of power on sample size, assumed effect and alpha. Use a paired binary-outcome power calculation here, not TTestPower or a Cohen's d formula for continuous means.

HOW TO READ THE POWER CURVE
The horizontal axis is a proposed number of matched image pairs, not a code length. The vertical axis is the probability of rejecting equal accuracy if the hypothetical advantage in the scenario is real. Each point is computed from the exact test, not observed in a new human sample. The mint point marks n = 50 and about 68% power. The white point marks n = 67 and about 80%. The horizontal dashed line is the conventional 80% planning target.

POWER IS NOT THE SAME AS A P-VALUE
A p-value looks at the observed result under a null model. Power looks at the chance of a future decision under a specified alternative. A confidence interval estimates a range of effect sizes compatible with sample uncertainty. These are three different questions. None is the probability our scientific idea is true.

WHY AN ILLUSTRATIVE 20-POINT ADVANTAGE WHEN WE OBSERVED 16?
Twenty points is a transparent hypothetical design target, not a replacement for the observed result. We chose it for a planning illustration. Its assumptions are human-only success on 30% and AI-only success on 10% of images. Many populations could have a 20-point difference with different disagreement rates, so a difference alone is not enough to calculate paired-test power. Both assumptions are needed. A future justified sample-size plan should specify a practically meaningful target using pilot or external evidence before collecting that study’s data.

WHAT CAN AND CANNOT BE SAID ABOUT INSUFFICIENT POWER
We can say 50 pairs give limited precision, as seen in the broad confidence interval, and that power under plausible scenarios can be modest. We cannot say lack of power proves a real human advantage exists. We cannot guarantee that 17 more pairs would make this particular finding significant. Adding data until significance appears is a different, potentially invalid stopping rule. A new planned study could find a smaller advantage, equality, or an AI advantage.

FOR THE CLASS RUBRIC
This is an explicit, reproducible power sensitivity analysis, with assumptions and software documented. Because it was completed after collection, it is not a prospective sample-size justification. Acknowledge that limitation openly in the report. The correct remedy is to use the pilot information to plan the next study, not to rewrite the chronology.

CONNECTION TO THE COURSE WORKBOOK
The workbook’s power chapter links sample size, effect size, significance threshold and power. The common t-test power examples in that chapter concern continuous means. Our data are paired binary outcomes, so the exact binomial/McNemar calculation is appropriate instead of inserting a Cohen’s d into a t-test calculator.

## Slide 10 — live script (~45 seconds)

What do we actually know? Humans led in these 50 trials, but we have not established a reliable advantage. We also have a usability problem: 22 percent of people were unsuccessful, while AI solved most codes. The next study should test six-, seven- and eight-character codes, other models, and recovery with hints and tools. We should vary one feature at a time, measure the human cost, and plan the sample size first. The contribution is a transparent experiment and a clearer next question—not a claim that we have solved CAPTCHA security.

### Study guide and Q&A

WHAT THE STUDY CONTRIBUTES
The result is not universally AI-proof text. It is a small paired experiment with transparent successes and failures: 78% human accuracy, 62% AI accuracy, a 16-point difference, and p = 0.067 for the directional exact test. It documents uncertainty rather than hiding it. A valid statistical project can produce an inconclusive primary test. Quality comes from matching the test to the design, maintaining an audit trail, and communicating limits honestly.

LONGER CODES
A sensible follow-up compares six-, seven- and eight-character codes. Call them characters, not digits, because the codes mix letters and numbers. More characters may lower exact-match success for both humans and AI simply because there are more opportunities for error. It may also increase human frustration. Do not assume that longer means a better CAPTCHA. Randomly assign length conditions, preserve per-character size and spacing, and avoid silently shrinking longer strings to the same width; otherwise length and legibility change together. Use fresh codes for final evaluation and reserve pilot examples for design selection.

DO THE CURRENT RESULTS SHOW THAT MORE NUMBERS FOOL AI?
No consistent pattern is visible in this small observational breakdown. With zero digits, AI solved 5/11 (45.5%); one digit, 12/17 (70.6%); two digits, 8/13 (61.5%); three digits, 6/8 (75%); five digits, 0/1. There were no four-digit codes. Human counts were 9/11, 15/17, 7/13, 7/8 and 1/1 respectively. These uneven, small groups do not show a steady decrease in AI accuracy as the number of digits increases. The one five-digit case cannot justify a rule. This analysis was suggested after seeing results and is exploratory, not a new confirmed hypothesis test.

To test digit mix properly, deliberately balance codes by digit count while holding length, character size and stripe settings fixed. Plan the comparison before collecting fresh data. Changing several factors and searching for a significant subgroup would create a multiple-comparisons problem.

AMBIGUOUS CHARACTERS
The idea of keeping shapes that confuse AI while reducing shapes that confuse people is a design hypothesis. The current dataset contains no letter O, so it cannot establish an O-versus-X effect. The missing original human strings for three wrong answers also prevent a complete human character-confusion analysis, including U versus J. Use fresh controlled examples and record exact responses to build separate human and model confusion matrices. A character-level confusion matrix records which true character was read as which other character. It needs careful alignment when answers insert or omit characters; simple position matching can misattribute errors. Do not optimize and evaluate on the same examples.

ROBUSTNESS AND SECURITY
Evaluate multiple models on the same fresh image bank, with a fixed prompt and effort setting. Add prespecified hint/no-hint and retry conditions with a fixed budget. The same model may improve through information in the chat; this is using context, not retraining its weights. Test resizing, thresholding, rotation and other permitted image tools. For motion, evaluate complete videos, not only frozen frames. More models and conditions create dependence and multiple-testing issues, so plan the analysis and power accordingly.

A production CAPTCHA also needs server-side answer checking, expiring challenges, replay resistance, rate limits, and accessible alternatives. A client-side visual generator that contains the answer is not a secure verifier. The research playground is appropriate for demonstrating the perceptual idea, not for deployment as a security product.

REFERENCES AND CREDITS
Data: https://docs.google.com/spreadsheets/d/1it_X73i8QzBLfrHUhJeDa-VhcEuyRD9-aHdU9xETyU0/edit
Exact McNemar reference: https://www.statsmodels.org/dev/generated/statsmodels.stats.contingency_tables.mcnemar.html
Directional binomial implementation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html
Bootstrap background: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html
Cao et al., ArmorOCR / AdvSpot, related adversarial OCR and striped-text design background: https://arxiv.org/abs/2608.20122
Eric Lu / Mixfont, Ghost Font, motion design inspiration: https://www.mixfont.com/ghost-font
Plesner et al., Breaking reCAPTCHAv2, 2024: https://arxiv.org/abs/2409.08831
Cloudflare, layered challenge mechanisms: https://developers.cloudflare.com/cloudflare-challenges/concepts/how-challenges-work/
W3C, Inaccessibility of CAPTCHA: https://www.w3.org/TR/turingtest/
Course Statistics workbook, Chapters 1, 3 and 4: descriptive statistics, hypothesis testing, power and effect size.

AI ASSISTANCE AND PROJECT DELIVERABLES
Analysis scripts and presentation preparation used AI assistance. The researcher collected the human responses and reported the AI protocol. For the class submission, the written report must explain methods and limitations in full. The repository needs scripts rather than notebooks, raw and cleaned data, reproduction instructions, and genuine contributions through branches/PRs by both partners. These collaboration actions are required deliverables and are not claimed to have been completed merely because the slides are finished. The brief allows up to eight minutes; this deck targets seven.

THE END RESULT, IN THREE SENTENCES
There was an observed human advantage on the collected images. This study did not establish that the advantage is reliable on new comparable trials. It also did not establish that the observed difference is merely noise or that humans and AI perform equally.

WHAT THIS MEANS FOR A CAPTCHA
A CAPTCHA needs both usability and resistance to automated solving. Here human success was only 78%, while the AI succeeded on 62%. Even a statistically significant 16-point advantage would not automatically make that security tradeoff acceptable. Statistical significance and practical suitability are different. A repeatable small gap may still be an unsuitable product. Security testing must consider retries, trained or adapted solvers, answer leakage, replay, and accessible alternatives.

THE NEXT EXPERIMENT SHOULD ANSWER ONE CLEAR QUESTION
For example: does increasing code length from six to seven characters reduce model success more than human success? Randomly assign fresh examples to conditions, keep per-character size and stripe settings stable, and include an ordinary-text control if the goal is to isolate the role of striping. Do not assume longer is better: exact-match accuracy can fall for both readers simply because there are more chances to make one error. Record exact human strings, not only a correct/incorrect label, so error patterns can be studied.

WHAT WE LEARNED VERSUS WHAT WE WANT TO TEST
The observed data support further investigation, not a declaration that a specific number mix, O/X resemblance or U/J difference caused errors. The digit-count breakdown is observational and inconsistent; it does not establish a digit effect. There were no letter-O codes, so an O-versus-X claim is untested here. User observations are useful hypothesis generators, not controlled causal findings.

TEST GENERALIZATION AND RECOVERY
A fresh chat is a clean first-attempt benchmark, not the strongest possible attacker. Give separate, prespecified budgets for hints, retries and image tools. A model using hints in a chat is adapting through context; that is different from retraining its underlying weights. Test multiple model families on the same image bank, account for repeated measurements and multiple comparisons, and keep a held-out set that was not used to choose the design.

IF THE INSTRUCTOR ASKS WHETHER THE PROJECT SUCCEEDED
It succeeded as a small exploratory statistical investigation with a valid paired design and a measured but uncertain effect. It did not establish the stronger product claim of a secure, AI-proof CAPTCHA. The main lesson is that a collection of striking failures is weaker evidence than a complete, prospectively planned evaluation that counts successes too.

The presentation is intentionally concise. The written report should retain the full assumptions, missing-response handling, limitations, exact p-values, interval method, power chronology, code versions and references. The repository should contain the raw snapshot, cleaned data and scripts, plus genuine partner PR/review activity. Do not claim those collaboration requirements are fulfilled by this deck alone.

