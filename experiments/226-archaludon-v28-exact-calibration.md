# 226 Archaludon v28 Exact Calibration

Date: 2026-08-06 UTC

Local generated package (not committed):
`artifacts/submissions/s226-archaludon-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 196, 199, 203, 205, 207,
212, 215, 217, 220, 222, and 224

Kaggle submission: `55304476`

Public score: 779.5

Status: complete

Sources:
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Grimmsnarl V15](https://www.kaggle.com/code/tetsutani/grimmsnarl-ex-damage-transfer-control?scriptVersionId=340390255)
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Archaludon Metal v28 archive as the first 2026-08-06
  calibration and complement to experiment 225 Steel.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Screened the newly score-bound Grimmsnarl V15 output before retaining the
  mature Archaludon fallback.

Candidate screen:
- Grimmsnarl V15 archive SHA-256 was
  `79b8036b8f03b128141bcf13c6618b5d3c770a1f284a1f9ccf923976ac0cc2c1`
- Its published output was bound to completed submission `55273327` and an
  804.3 public-score checkpoint
- Sixteen fresh games completed 10-6: 5-3 against Archaludon and 5-3 against
  Steel, without errors, ties, timeouts, invalid actions, or retries
- Grimmsnarl went 5-3 from each candidate seat and winning seats split 8-8
- The fixed aggregate gate required at least 11-5, so the candidate missed by
  one game and no expansion panel was run
- The threshold was not relaxed after observing the result

Validation:
- Archive SHA-256 matched experiments 196, 199, 203, 205, 207, 212, 215, 217,
  220, 222, and 224 exactly
- Kaggle's `get_last_callable` selected the base function named `agent`
- The callable was exposed through loader key `_v28_original_agent`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean root archive with the full Program22 runtime and published helper files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- A separate eight-game Steel versus Garchomp diagnostic completed 2-6 with
  both profiles splitting their results evenly across seats
- Maximum observed decision latency was 0.023 seconds in the candidate screen
- Candidate-screen seeds were `2026080608` through `2026080623`
- Main SHA-256:
  `085f399dadf5e15d0e89c13ad4288e22a727514a5b95f538877eb804f970962e`
- Deck SHA-256:
  `bb3d2c7167975be58701bb5b74b88d83c8eb6510b829b7a73219cafa14ad1ed7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`

Result:
- Kaggle accepted the package as submission `55304476` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before
  moving through 710.5, 636.0, 618.0, 631.3, 607.7, and 773.8 to 779.5.
- At this checkpoint, the twelve byte-identical official rows read 726.6,
  741.3, 788.1, 738.9, 610.9, 907.3, 650.9, 840.9, 731.8, 714.9, 653.0, and
  779.5.
- The latest two submissions preserve Steel and Archaludon as distinct
  complementary strategy families.
- Score checkpoint: `2026-08-07 12:41 UTC`.
