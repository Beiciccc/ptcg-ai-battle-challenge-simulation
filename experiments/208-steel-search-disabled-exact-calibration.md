# 208 Steel Search-Disabled Exact Calibration

Date: 2026-08-02 UTC

Local generated package (not committed):
`artifacts/submissions/s208-steel-search-disabled-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 173, 175, 198, and 201

Kaggle submission: `55174222`

Public score: 827.9

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Re-ran the exact search-disabled Steel archive as the single 2026-08-02
  exploration calibration.
- Preserved the documented compatibility flag, strategy, 60-card deck,
  runtime, and archive bytes.
- Retained Steel after a newly published Mega Lopunny archive completed only
  3-13 against the current Garchomp and Archaludon anchors.

Validation:
- Archive SHA-256 matched experiments 173, 175, 198, and 201 exactly
- Static and dynamic loader checks selected the final `agent` callable
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Eight fresh seat-alternated games against Garchomp completed 5-3 without
  errors or ties
- Steel went 2-2 from seat zero and 3-1 from seat one; the panel recorded five
  wins from seat one and three from seat zero
- Maximum observed decision latency was 0.001 seconds for Steel and 0.002
  seconds for Garchomp
- Main SHA-256:
  `4cc4c469d1c5caced0439cb2db32ad4827a87f7dcc698419bef6c07fc64aedcb`
- Deck SHA-256:
  `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b5c7601e843a9f7269513a1ba9489cc1354a8dbff52e0ddd74f93fa8ff165bf2`

Result:
- Kaggle accepted the package as submission `55174222` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 487.9, then moved through 603.4 and 678.8 to
  783.1 and 827.9.
- At this checkpoint, the five byte-identical official rows read 966.4, 773.1,
  673.6, 626.7, and 827.9.
- The matured reading keeps Steel under consideration for the final active
  pair, subject to the last-cycle robustness comparison.
- Score checkpoint: `2026-08-02 01:29 UTC`.
