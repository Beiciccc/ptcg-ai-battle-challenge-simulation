# 184 Cynthia Garchomp Current Runtime Entry Fix

Date: 2026-07-27 UTC

Local generated package (not committed):
`artifacts/submissions/s184-masamikobayashi-cynthia-garchomp-current-runtime-entryfix.tar.gz`

Reproducibility: public rule-based strategy, current runtime, and one appended
loader entrypoint

Kaggle submission: `55024691`

Public score: 700.4

Status: complete

Sources:
- [A Sample Cynthia Garchomp ex Deck](https://www.kaggle.com/code/masamikobayashi/a-sample-cynthia-garchomp-ex-deck)
- [Tracking 3,057 teams through six weeks of meta](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/discussion/729926)

Summary:
- Preserved the public Cynthia Garchomp ex strategy and 60-card deck.
- Replaced only the bundled competition runtime with the current official
  binaries and Python interface.
- Appended a fresh final `submission_entrypoint` so Kaggle's loader selects the
  intended agent wrapper.
- Selected the candidate after the public 74,634-game analysis identified
  Garchomp as the strongest current counter to the Grimmsnarl-heavy field.

Validation:
- Static entrypoint check selected the unique final `submission_entrypoint`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Eight loader-aware mirror games completed without errors
- Fifty-six games against replay-trained Grimmsnarl completed 36-20
- Eight games against Visible Templates Alakazam v19 completed 3-5
- Eight games against Static Tusk v24 completed 3-5
- Eight games against current-runtime Steel completed 5-3
- All 88 loader-aware games completed without errors
- Maximum observed Garchomp decision latency was 0.009 seconds
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
- Kaggle accepted the package and marked submission `55024691` complete.
- Public evaluation moved from 600.0 through 700.3, 634.3, 696.4, and 645.1
  to 700.4 as additional validation battles accumulated.
- Score checkpoint: `2026-07-28 02:25 UTC`.
