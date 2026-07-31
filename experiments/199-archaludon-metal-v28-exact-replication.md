# 199 Archaludon Metal v28 Exact Replication

Date: 2026-07-31 UTC

Local generated package (not committed):
`artifacts/submissions/s199-archaludon-metal-v28-exact-replication.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiment 196

Kaggle submission: `55124341`

Public score: 518.9

Status: complete

Sources:
- [Archaludon Metal GPU v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact experiment 196 Archaludon Metal v28 public archive for a
  second independent public-score observation.
- Preserved the policy, 60-card deck, selector data, helper files, current
  runtime, loader-selected behavior, and archive bytes.
- Added a fresh direct comparison against the exact Steel archive before
  submission.

Validation:
- Archive SHA-256 matched experiment 196 exactly
- Kaggle's `get_last_callable` selected the base function named `agent`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean root archive with the full current runtime and published helper files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Eight fresh seat-alternated games against experiment 198 Steel completed
  3-5 without errors
- The prior 96-game comparison panel completed 54-42 without errors
- Main SHA-256:
  `085f399dadf5e15d0e89c13ad4288e22a727514a5b95f538877eb804f970962e`
- Deck SHA-256:
  `bb3d2c7167975be58701bb5b74b88d83c8eb6510b829b7a73219cafa14ad1ed7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`

Result:
- Kaggle accepted the package as submission `55124341` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline through 514.9
  before reaching 518.9.
- The two byte-identical observations reached 726.6 and 518.9 at the same
  checkpoint, confirming substantial public-path variance.
- Score checkpoint: `2026-07-31 02:21 UTC`.
