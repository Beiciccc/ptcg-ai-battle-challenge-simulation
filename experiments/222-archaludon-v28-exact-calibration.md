# 222 Archaludon v28 Exact Calibration

Date: 2026-08-05 UTC

Local generated package (not committed):
`artifacts/submissions/s222-archaludon-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 196, 199, 203, 205, 207,
212, 215, 217, and 220

Kaggle submission: `55254218`

Public score: 687.6

Status: complete

Sources:
- [Archaludon Metal GPU v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-gpu-v28-agents-only)
- [Grimmsnarl Damage Transfer Control V13](https://www.kaggle.com/code/tetsutani/grimmsnarl-ex-damage-transfer-control?scriptVersionId=340180546)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Archaludon Metal v28 archive as the second 2026-08-05
  calibration and complement to experiment 221 Garchomp.
- Preserved the policy, 60-card deck, selector data, helper files, Program22
  runtime, loader-selected behavior, and archive bytes.
- Retained the mature pair after Grimmsnarl V13 failed its predeclared seat
  balance gate.

Candidate screen:
- Grimmsnarl V13 exact archive completed 9-7 across Garchomp and Archaludon
- V13 split 4-4 against Garchomp and 5-3 against Archaludon without errors
- V13 went 6-2 from seat zero but only 3-5 from seat one; winning seats split
  11-5, below the predeclared minimum of four candidate wins from each seat
- The validation gate was not relaxed after observing the result

Validation:
- Archive SHA-256 matched experiments 196, 199, 203, 205, 207, 212, 215, 217,
  and 220 exactly
- Kaggle's `get_last_callable` selected the base function named `agent`
- The callable was exposed through loader key `_v28_original_agent`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean root archive with the full Program22 runtime and published helper files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- The eight-game Grimmsnarl comparison panel completed without errors or ties
- Maximum observed decision latency was 0.039 seconds for Archaludon and 0.037
  seconds for Grimmsnarl
- Panel seeds were `2026080532` through `2026080539`
- Main SHA-256:
  `085f399dadf5e15d0e89c13ad4288e22a727514a5b95f538877eb804f970962e`
- Deck SHA-256:
  `bb3d2c7167975be58701bb5b74b88d83c8eb6510b829b7a73219cafa14ad1ed7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`

Result:
- Kaggle accepted the package as submission `55254218` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 687.6.
- At this checkpoint, the ten byte-identical official rows read 726.6, 741.3,
  788.1, 738.9, 610.9, 907.3, 650.9, 840.9, 731.8, and 687.6.
- The latest two submissions preserve Garchomp and Archaludon as distinct
  complementary strategy families.
- Score checkpoint: `2026-08-05 01:05 UTC`.
