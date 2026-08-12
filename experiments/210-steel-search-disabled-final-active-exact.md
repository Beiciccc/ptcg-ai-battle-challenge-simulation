# 210 Steel Search-Disabled Final Active Exact

Date: 2026-08-02 UTC

Local generated package (not committed):
`artifacts/submissions/s210-steel-search-disabled-final-active-exact.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 173, 175, 198, 201, and 208

Kaggle submission: `55174572`

Public score: 679.6

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Re-ran the exact search-disabled Steel archive as the final active complement
  to experiment 209 Garchomp.
- Preserved the documented compatibility flag, strategy, 60-card deck,
  runtime, and archive bytes.
- Selected Steel after experiment 208 matured to 827.9 and the repeated Steel
  family retained a stronger median than the Archaludon alternative.

Validation:
- Archive SHA-256 matched experiments 173, 175, 198, 201, and 208 exactly
- Static and dynamic loader checks selected the final `agent` callable
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Eight fresh seat-alternated games against Crustle completed 5-3 without
  errors or ties
- Steel went 1-3 from seat zero and 4-0 from seat one; the same-seed panel had
  a strong seat-one advantage, so the aggregate was not treated in isolation
- On the same seeds, Archaludon completed 3-5 against Crustle
- Maximum observed decision latency was 0.002 seconds for Steel and 0.001
  seconds for Crustle
- Main SHA-256:
  `4cc4c469d1c5caced0439cb2db32ad4827a87f7dcc698419bef6c07fc64aedcb`
- Deck SHA-256:
  `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b5c7601e843a9f7269513a1ba9489cc1354a8dbff52e0ddd74f93fa8ff165bf2`

Result:
- Kaggle accepted the package as submission `55174572` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 489.7 and then moved through 649.2 to 679.6.
- At this checkpoint, the six byte-identical official rows read 966.4, 773.1,
  673.6, 626.7, 827.9, and 679.6, showing substantial early path variance.
- The final latest-two submissions preserve Garchomp and Steel as distinct
  strategy families.
- Score checkpoint: `2026-08-03 05:28 UTC`.
