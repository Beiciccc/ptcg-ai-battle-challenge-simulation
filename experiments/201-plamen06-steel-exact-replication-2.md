# 201 Plamen06 Steel Exact Replication 2

Date: 2026-08-01 UTC

Local generated package (not committed):
`artifacts/submissions/s201-steel-search-disabled-exact-replication-2.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 173, 175, and 198

Kaggle submission: `55154344`

Public score: 626.7

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Re-ran the exact search-disabled Steel archive as the first 2026-08-01
  observation.
- Preserved the documented compatibility flag, strategy, 60-card deck,
  runtime, and archive bytes.
- Used Steel to form a distinct Garchomp and Steel active pair while retaining
  coverage against Crustle-oriented strategies.

Validation:
- Archive SHA-256 matched experiments 173, 175, and 198 exactly
- Static and dynamic loader checks selected the final `agent` callable
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Eight fresh seat-alternated games against experiment 200 Garchomp split 4-4
  without errors
- Both strategies went 3-1 from seat zero and 1-3 from seat one, exposing a
  material seat effect rather than a clear strategy advantage
- Main SHA-256:
  `4cc4c469d1c5caced0439cb2db32ad4827a87f7dcc698419bef6c07fc64aedcb`
- Deck SHA-256:
  `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b5c7601e843a9f7269513a1ba9489cc1354a8dbff52e0ddd74f93fa8ff165bf2`

Result:
- Kaggle accepted the package as submission `55154344` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline through 736.1
  and 576.6 before reaching 626.7.
- At this checkpoint, the four byte-identical official rows read 966.4, 773.1,
  673.6, and 626.7.
- Score checkpoint: `2026-08-01 05:35 UTC`.
