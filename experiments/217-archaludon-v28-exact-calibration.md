# 217 Archaludon v28 Exact Calibration

Date: 2026-08-04 UTC

Local generated package (not committed):
`artifacts/submissions/s217-archaludon-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 196, 199, 203, 205, 207,
212, and 215

Kaggle submission: `55225070`

Public score: 746.4

Status: complete

Sources:
- [Archaludon Metal GPU v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-gpu-v28-agents-only)
- [Crustle v29](https://www.kaggle.com/code/jazivxt/crustle-v29-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Archaludon Metal v28 archive as the second 2026-08-04
  calibration and complement to experiment 216 Garchomp.
- Preserved the policy, 60-card deck, selector data, helper files, Program22
  runtime, loader-selected behavior, and archive bytes.
- Retained the mature Garchomp and Archaludon combination after the incremental
  public refresh produced no new executable strategy.

Validation:
- Archive SHA-256 matched experiments 196, 199, 203, 205, 207, 212, and 215
  exactly
- Kaggle's `get_last_callable` selected the base function named `agent`
- The callable was exposed through loader key `_v28_original_agent`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean root archive with the full Program22 runtime and published helper files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Eight fresh seat-alternated games against Crustle v29 split 4-4 without
  errors or ties
- Archaludon went 3-1 from seat zero and 1-3 from seat one; the panel recorded
  six wins from seat zero and two from seat one
- Maximum observed decision latency was 0.025 seconds for Archaludon and 0.001
  seconds for Crustle
- Seeds were `2026080424` through `2026080431`
- Main SHA-256:
  `085f399dadf5e15d0e89c13ad4288e22a727514a5b95f538877eb804f970962e`
- Deck SHA-256:
  `bb3d2c7167975be58701bb5b74b88d83c8eb6510b829b7a73219cafa14ad1ed7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`

Result:
- Kaggle accepted the package as submission `55225070` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 746.4.
- At this checkpoint, the eight byte-identical official rows read 726.6, 741.3,
  788.1, 738.9, 610.9, 907.3, 650.9, and 746.4.
- The latest two submissions preserve Garchomp and Archaludon as distinct
  complementary strategy families.
- Score checkpoint: `2026-08-04 00:53 UTC`.
