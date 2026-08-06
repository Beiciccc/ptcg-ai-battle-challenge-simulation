# 225 Steel Search-Disabled Final Active Exact

Date: 2026-08-05 UTC

Local generated package (not committed):
`artifacts/submissions/s225-steel-search-disabled-final-active-exact.tar.gz`

Official upload filename:
`s225-steel-search-disabled-final-active-exact.tar.gz`

Reproducibility: byte-identical rerun of experiments 173, 175, 198, 201, 208,
and 210

Kaggle submission: `55255010`

Public score: 757.4

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Re-ran the exact search-disabled Steel archive as the fifth 2026-08-05
  submission and final active complement to experiment 224 Archaludon.
- Preserved the documented compatibility flag, strategy, 60-card deck,
  runtime, and archive bytes.
- No new executable Code, Discussion, rules, data, or CABT runtime change was
  available at the final evidence checkpoint.

Selection evidence:
- The Garchomp alternative required two distinct post-experiment-224 score
  readings at or above 699.9
- Its distinct readings of 625.5 and 558.7 both failed that fixed threshold
- The threshold was not relaxed after observing the result, leaving exact
  Steel as the unique mature alternative

Validation:
- Archive SHA-256 matched experiments 173, 175, 198, 201, 208, and 210 exactly
- Static and dynamic loader checks selected the final `agent` callable
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Search compatibility remained explicitly disabled with `ENABLE_SEARCH=False`
- Eight fresh seat-alternated games against Archaludon split 4-4 without
  errors or ties
- Steel went 2-2 from seat zero and 2-2 from seat one; Archaludon had the same
  split, and winning seats also split 4-4
- The panel completed exactly eight games with no retries using seeds
  `2026080564` through `2026080571`
- Maximum observed decision latency was 0.001 seconds for Steel and 0.023
  seconds for Archaludon
- Main SHA-256:
  `4cc4c469d1c5caced0439cb2db32ad4827a87f7dcc698419bef6c07fc64aedcb`
- Deck SHA-256:
  `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b5c7601e843a9f7269513a1ba9489cc1354a8dbff52e0ddd74f93fa8ff165bf2`

Result:
- Kaggle accepted the package as submission `55255010` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 744.1, later reached 761.8, and moved to 757.4.
- At this checkpoint, the seven byte-identical official rows read 966.4,
  721.7, 673.6, 626.7, 827.9, 679.6, and 757.4.
- The latest two submissions preserve Archaludon and Steel as distinct
  complementary strategy families.
- Score checkpoint: `2026-08-06 18:35 UTC`.
