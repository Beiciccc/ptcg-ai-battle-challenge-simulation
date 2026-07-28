# 186 Plamen06 Steel Current Runtime Exact Control

Date: 2026-07-28 UTC

Local generated package (not committed):
`artifacts/submissions/s186-plamen06-steel-current-runtime-control.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiment 179

Kaggle submission: `55050538`

Public score: 797.6

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact search-disabled Steel strategy, deck, entrypoint, and current
  competition runtime from experiment 179.
- Used the independent observation to measure whether the strategy's strong
  historical public results persisted in the current field.
- Preserved the archive bytes so score differences reflect evaluation
  variance rather than implementation changes.

Validation:
- Archive SHA-256 matched experiment 179 exactly
- Static and dynamic loader checks selected the final `agent` callable
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Four fresh mirror games completed 3-1 without errors
- Twenty-four fresh games against replay-trained Grimmsnarl completed 15-9
- Maximum observed Steel decision latency was 0.001 seconds
- Main SHA-256:
  `4cc4c469d1c5caced0439cb2db32ad4827a87f7dcc698419bef6c07fc64aedcb`
- Deck SHA-256:
  `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Windows runtime SHA-256:
  `a3a401d0f5ccc3474b9c8a7a2431920c4b728d28105a510aa6927ad6283e5cf7`
- Linux runtime SHA-256:
  `feafd4046b2f688bdb33a4972c139b78e13e243ab5707ece52c43cf39a34b887`
- Linux ARM64 runtime SHA-256:
  `116750365a1043f0d95e200bb283c042753cdbd44c7d16331827ad0a44df0553`
- macOS runtime SHA-256:
  `00154aee7d3071451096c929c52da9f9af360a2821e686671097f5011e5a5d95`
- Archive SHA-256:
  `c401237a7034426d11800a7fde3c1c239a4168830ea5f99b30b9001c250d4835`

Result:
- Kaggle accepted the package as submission `55050538` and marked it complete.
- Public evaluation moved from 600.0 through 692.6 before reaching 797.6.
- Score checkpoint: `2026-07-28 09:18 UTC`.
