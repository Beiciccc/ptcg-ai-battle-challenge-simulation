# 224 Archaludon v28 Final Pair Exact

Date: 2026-08-05 UTC

Local generated package (not committed):
`artifacts/submissions/s224-archaludon-v28-final-pair-exact.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 196, 199, 203, 205, 207,
212, 215, 217, 220, and 222

Kaggle submission: `55254689`

Public score: 694.6

Status: complete

Sources:
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Archaludon Metal v28 archive as the fourth 2026-08-05
  submission and first member of the final pair.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Used a fresh balanced direct comparison to confirm the mature Garchomp and
  Archaludon pair before submission.

Validation:
- Archive SHA-256 matched experiments 196, 199, 203, 205, 207, 212, 215, 217,
  220, and 222 exactly
- Kaggle's `get_last_callable` selected the base function named `agent`
- The callable was exposed through loader key `_v28_original_agent`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean root archive with the full Program22 runtime and published helper files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Eight fresh seat-alternated games against Garchomp split 4-4 without errors
  or ties
- Archaludon and Garchomp each went 2-2 from seat zero and 2-2 from seat one;
  winning seats also split 4-4
- Maximum observed decision latency was 0.023 seconds for Archaludon and 0.002
  seconds for Garchomp
- Seeds were `2026080556` through `2026080563`
- Main SHA-256:
  `085f399dadf5e15d0e89c13ad4288e22a727514a5b95f538877eb804f970962e`
- Deck SHA-256:
  `bb3d2c7167975be58701bb5b74b88d83c8eb6510b829b7a73219cafa14ad1ed7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`

Result:
- Kaggle accepted the package as submission `55254689` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 694.6.
- At this checkpoint, the eleven byte-identical official rows read 726.6,
  741.3, 788.1, 738.9, 610.9, 907.3, 650.9, 840.9, 731.8, 714.9, and 694.6.
- The latest two submissions preserve Garchomp and Archaludon as distinct
  complementary strategy families.
- Score checkpoint: `2026-08-05 01:35 UTC`.
