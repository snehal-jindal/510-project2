# Collection renderer provenance

`source/generator.js` is copied without modification from [ant.ai](https://github.com/snehal-jindal/xai-project1-ant.ai/blob/a4321261d4097adf885d9938a364045c98711cb1/src/generator.js), commit `a4321261d4097adf885d9938a364045c98711cb1`. Its `stripes` function renders horizontal background stripes and vertical stripes inside a text mask on a 1000×240 canvas. `pitch` controls the pattern period in pixels. We used UI setting 16 for this study.

The bundled Bitstream Vera Bold font and its license are preserved. Upstream notices are in `UPSTREAM_NOTICE.md`. The module imports `gifenc` and `jspdf`; it is archival source, not a standalone browser entry point. To run the complete original playground, use the pinned upstream repository and its README (`npm ci`, `npm run build`, `npm run preview` under its Node >=20 requirement). The already-published [playground](https://snehal-jindal.github.io/xai-project1-ant.ai/) is convenient but not a frozen source version.

The authoritative study inputs are the **50 supplied PNGs**. Random phases/codes and browser font rendering mean generating new images is not guaranteed to produce byte-identical stimuli. No claims are made that the archived repository can recover the original random seed. Earlier motion, color and connection examples are contextual work, not extra observations in this study.
