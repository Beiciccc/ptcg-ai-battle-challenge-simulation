# 179 Steel Search-Disabled Current Official Runtime

Date: 2026-07-26 UTC

Local generated package (not committed):
`artifacts/submissions/s179-plamen06-steel-search-disabled-current-official-runtime.tar.gz`

Reproducibility: exact experiment 173 strategy and deck with current
competition binaries

Kaggle submission: `54996594`

Public score: 655.2

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Public 46 + Sample 4 Roster Update](https://www.kaggle.com/code/makimakiai/ptcg-public-28-plus-sample-4-roster-update)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Preserved the exact search-disabled Steel strategy, deck, and Python runtime
  wrappers from experiment 173.
- Replaced only `cg.dll`, `libcg.so`, `libcg-arm64.so`, and `libcg.dylib` with
  the current competition sample binaries.
- Used the migration to test whether the historical matrix-leading profile
  retained its public-rating behavior under the refreshed engine.

Validation:
- Strategy and deck SHA-256 values matched experiment 173 exactly
- Static entrypoint check selected `agent`
- Kaggle's `get_last_callable` selected `agent` at source line 1218
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Three loader-aware mirror games completed without errors
- Eight loader-aware games against Visible-Grim Alakazam completed 2-6
- Eight loader-aware games against Observable Meta Router completed 1-7
- Eight loader-aware games against Mega Lucario Prize-Pressure completed 5-3
- The 27-game validation recorded 1,709 Steel decisions with no errors and a
  0.025-second maximum Steel decision latency
- Search remained disabled throughout the validation
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
- Kaggle accepted the package and marked submission `54996594` complete.
- Public evaluation moved from the 600.0 baseline through 472.9 before reaching
  655.2 as additional validation battles accumulated.
- Score checkpoint: `2026-07-26 09:11 UTC`.
