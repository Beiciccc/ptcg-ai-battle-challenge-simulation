# 228 Archaludon v28 Exact Calibration

Date: 2026-08-07 UTC

Local generated package (not committed):
`artifacts/submissions/s228-archaludon-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 196, 199, 203, 205, 207,
212, 215, 217, 220, 222, 224, and 226

Kaggle submission: `55324816`

Public score: 789.7

Status: complete

Sources:
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Grimmsnarl V16](https://www.kaggle.com/code/tetsutani/grimmsnarl-ex-damage-transfer-control?scriptVersionId=340409708)
- [Leaderboard deck meta](https://www.kaggle.com/code/myso1987/ptcg-ai-battle-leaderboard-deck-meta-by-score-band)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Archaludon Metal v28 archive as the first 2026-08-07
  calibration and complement to experiment 227 Steel.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Re-evaluated Grimmsnarl V16 with a corrected low-overhead harness before
  retaining the mature Archaludon fallback.

Public refresh:
- A newly published PPO output was rejected because its archive omitted the
  claimed trained checkpoint and its policy used random initialization
- Its score-bound checkpoint was 191.5, far below the mature references
- A newly surfaced Great Tusk / Crustle output was byte-identical to an already
  reviewed strategy and did not establish a new behavior
- Rules, evaluation, data, and the CABT environment files remained unchanged

Candidate screen:
- Grimmsnarl V16 archive SHA-256 was
  `46bb3180e7b15e41aff60f52b18300aad1ca65d1840464d15e4d30fcac9b57ba`
- Its published output was bound to completed submission `55275925` and a
  773.2 public-score checkpoint
- Sixteen fresh games completed 9-7: 5-3 against Archaludon and 4-4 against
  Steel, without errors, ties, timeouts, invalid actions, or retries
- Grimmsnarl went 5-3 from seat zero and 4-4 from seat one; winning seats split
  9-7
- Maximum Grimmsnarl decision latency was 0.007 seconds, and the global maximum
  was 0.020 seconds
- The fixed aggregate gate required at least 11-5, so the candidate failed and
  no expansion panel was run
- Screen seeds were `2026080740` through `2026080755`

Validation:
- Archive SHA-256 matched experiments 196, 199, 203, 205, 207, 212, 215, 217,
  220, 222, 224, and 226 exactly
- Kaggle's `get_last_callable` selected the base function named `agent`
- The callable was exposed through loader key `_v28_original_agent`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean root archive with the full Program22 runtime and published helper files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Main SHA-256:
  `085f399dadf5e15d0e89c13ad4288e22a727514a5b95f538877eb804f970962e`
- Deck SHA-256:
  `bb3d2c7167975be58701bb5b74b88d83c8eb6510b829b7a73219cafa14ad1ed7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`

Result:
- Kaggle accepted the package as submission `55324816` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 526.8 and later moved to 789.7.
- At this checkpoint, the thirteen byte-identical official rows read 726.6,
  741.3, 788.1, 738.9, 610.9, 907.3, 650.9, 840.9, 731.8, 714.9, 653.0,
  779.5, and 789.7.
- The latest two submissions preserve Steel and Archaludon as distinct
  complementary strategy families.
- Score checkpoint: `2026-08-07 13:04 UTC`.
