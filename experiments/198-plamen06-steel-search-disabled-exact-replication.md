# 198 Plamen06 Steel Search-Disabled Exact Replication

Date: 2026-07-31 UTC

Local generated package (not committed):
`artifacts/submissions/s198-plamen06-steel-search-disabled-exact-replication.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 173 and 175

Kaggle submission: `55124190`

Public score: 710.4

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Re-ran the exact search-disabled Steel archive for a third independent
  public-score observation.
- Preserved the documented compatibility flag, strategy, 60-card deck,
  runtime, and archive bytes.
- Added a fresh comparison against the three most recent exact public archives
  before submission.

Validation:
- Archive SHA-256 matched experiments 173 and 175 exactly
- Static and dynamic loader checks selected the final `agent` callable
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Twenty-four fresh seat-alternated games completed 11-13 without errors
- Fresh results: 3-5 against experiment 197 Garchomp, 3-5 against experiment
  196 Archaludon, and 5-3 against experiment 195 Crustle
- Main SHA-256:
  `4cc4c469d1c5caced0439cb2db32ad4827a87f7dcc698419bef6c07fc64aedcb`
- Deck SHA-256:
  `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b5c7601e843a9f7269513a1ba9489cc1354a8dbff52e0ddd74f93fa8ff165bf2`

Result:
- Kaggle accepted the package as submission `55124190` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline to 710.4.
- The three byte-identical observations reached 966.4, 721.7, and 710.4 at
  their recorded checkpoints.
- Score checkpoint: `2026-07-31 02:01 UTC`.
