# 203 Archaludon v28 Exact Control

Date: 2026-08-01 UTC

Local generated package (not committed):
`artifacts/submissions/s203-archaludon-v28-exact-control.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 196 and 199

Kaggle submission: `55154604`

Public score: 788.1

Status: complete

Sources:
- [Archaludon Metal GPU v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Archaludon Metal v28 public archive as the stable control
  after the first two 2026-08-01 observations opened below 700.
- Preserved the policy, 60-card deck, selector data, helper files, Program22
  runtime, loader-selected behavior, and archive bytes.
- Reused the current comparison evidence against Alakazam v23 rather than
  introducing an unvalidated archive change.

Validation:
- Archive SHA-256 matched experiments 196 and 199 exactly
- Kaggle's `get_last_callable` selected the base function named `agent`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean root archive with the full Program22 runtime and published helper files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- The original 96-game Program22 panel completed 54-42 without errors
- Eight fresh seat-alternated games against experiment 202 Alakazam v23 split
  4-4 without errors
- Main SHA-256:
  `085f399dadf5e15d0e89c13ad4288e22a727514a5b95f538877eb804f970962e`
- Deck SHA-256:
  `bb3d2c7167975be58701bb5b74b88d83c8eb6510b829b7a73219cafa14ad1ed7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`

Result:
- Kaggle accepted the package as submission `55154604` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline through
  695.8, 797.1, 806.5, and 852.7 before reaching 788.1.
- At this checkpoint, the three byte-identical official rows read 726.6,
  741.3, and 788.1.
- Score checkpoint: `2026-08-02 01:23 UTC`.
