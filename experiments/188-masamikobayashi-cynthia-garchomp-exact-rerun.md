# 188 Cynthia Garchomp Exact Rerun

Date: 2026-07-28 UTC

Local generated package (not committed):
`artifacts/submissions/s188-masamikobayashi-cynthia-garchomp-exact-rerun.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiment 184

Kaggle submission: `55051685`

Public score: 602.3

Status: complete

Sources:
- [A Sample Cynthia Garchomp ex Deck](https://www.kaggle.com/code/masamikobayashi/a-sample-cynthia-garchomp-ex-deck)
- [Tracking 3,057 teams through six weeks of meta](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/discussion/729926)

Summary:
- Re-ran the exact current-runtime Cynthia Garchomp archive from experiment
  184 as an independent public-score observation.
- Preserved the strategy, 60-card deck, loader entrypoint, runtime, and archive
  bytes so evaluation variance is isolated from implementation changes.
- Retained the strategy as a targeted response to the replay-trained
  Grimmsnarl profile.

Validation:
- Archive SHA-256 matched experiment 184 exactly
- Static and dynamic loader checks selected `submission_entrypoint`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Four fresh loader-aware mirror games completed 2-2 without errors
- The byte-identical archive retained experiment 184's 36-20 validation result
  against replay-trained Grimmsnarl
- Maximum observed Garchomp decision latency remained below 0.010 seconds
- Main SHA-256:
  `f823aa1e5a275ea45c439513cc1cd808c12b689876efb016ddf2ffeba77a6019`
- Deck SHA-256:
  `f6fe420cb34f07dd9445a6b6eef6043e67487a2fc1869b923cf5617443a8ecdd`
- Windows runtime SHA-256:
  `a3a401d0f5ccc3474b9c8a7a2431920c4b728d28105a510aa6927ad6283e5cf7`
- Linux runtime SHA-256:
  `feafd4046b2f688bdb33a4972c139b78e13e243ab5707ece52c43cf39a34b887`
- Linux ARM64 runtime SHA-256:
  `116750365a1043f0d95e200bb283c042753cdbd44c7d16331827ad0a44df0553`
- macOS runtime SHA-256:
  `00154aee7d3071451096c929c52da9f9af360a2821e686671097f5011e5a5d95`
- Archive SHA-256:
  `e58885ec8addb3f4b690f8be6c58251423d9a66b6c93b89a1cd6667184703857`

Result:
- Kaggle accepted the package as submission `55051685` and marked it complete.
- Public evaluation moved from 600.0 through 705.8 before reaching 602.3.
- Score checkpoint: `2026-07-28 10:04 UTC`.
