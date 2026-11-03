# References, credits and assistance

- SciPy, [`binomtest`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html): exact one-/two-sided binomial probabilities and Clopper–Pearson interval.
- statsmodels, [McNemar test](https://www.statsmodels.org/dev/generated/statsmodels.stats.contingency_tables.mcnemar.html): matched binary-outcome test and exact conditional formulation. Computation here uses SciPy, not an unstated statsmodels dependency.
- SciPy, [bootstrap background](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html): resampling principles. The implementation uses explicit paired multinomial resampling and the percentile method; it does not claim to use SciPy’s default BCa method.
- Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. *JASA*, 22(158), 209–212. [DOI](https://doi.org/10.1080/01621459.1927.10502953).
- Plesner, Vontobel & Wattenhofer (2024), [Breaking reCAPTCHAv2](https://arxiv.org/abs/2409.08831): motivation about particular automated visual solvers, not proof every CAPTCHA is obsolete.
- Cao et al. (2026), [ArmorOCR / AdvSpot](https://arxiv.org/abs/2608.20122): related adversarial OCR / visual-text design background.
- Eric Lu / Mixfont, [Ghost Font](https://www.mixfont.com/ghost-font): motion-text inspiration in the broader ant.ai project, not a method evaluated in this static-image dataset.
- W3C, [Inaccessibility of CAPTCHA](https://www.w3.org/TR/turingtest/): usability and accessible alternatives.
- Cloudflare, [How challenges work](https://developers.cloudflare.com/cloudflare-challenges/concepts/how-challenges-work/): layered anti-bot context.
- Course Statistics workbook: descriptive statistics, hypothesis testing, power and effect size; used for learning and interpretation. No private course markdown is republished here.

Original ant.ai generator/font provenance and third-party notices are preserved under `collection/`. We collected the human responses and recorded the model trials. We used AI assistance for code, analysis checks, documentation and slides. Search-result headlines in slide 2 are motivation screenshots, not verified primary evidence for our statistical findings.
