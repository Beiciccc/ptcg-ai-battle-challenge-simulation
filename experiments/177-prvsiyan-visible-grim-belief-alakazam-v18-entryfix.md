# 177 Visible-Grim Belief Alakazam v18 Entry Fix

Date: 2026-07-26 UTC

Local generated package (not committed):
`artifacts/submissions/s177-prvsiyan-visible-grim-belief-alakazam-v18-entryfix.tar.gz`

Reproducibility: public v18 strategy with a one-line loader entrypoint rename

Kaggle submission: `54996323`

Public score: 880.8

Status: complete

Sources:
- [Visible-Grim Belief Alakazam v18](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-visible-grim-belief-alakazam-v18)
- [Kaggle Environments agent loader](https://github.com/Kaggle/kaggle-environments/blob/8418fb28e8a826ca3edff9561cf8e7ba11559e69/kaggle_environments/agent.py)

Summary:
- Retained every strategy, deck, and runtime byte from experiment 176 except
  for the final wrapper name.
- Renamed the redefined final `agent` wrapper to the fresh global name
  `submission_entrypoint`, ensuring it is last in loader insertion order.
- Preserved the visible Grimmsnarl and Team Rocket Energy response behavior.

Validation:
- Static entrypoint check selected `submission_entrypoint`
- Kaggle's `get_last_callable` selected `submission_entrypoint` at source line
  1149 with two accepted arguments
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Three loader-aware mirror games completed without errors
- Eight loader-aware games against Steel completed 5-3 without errors
- Eight loader-aware games against Mega Lucario Prize-Pressure completed 5-3
  without errors
- The 19-game validation recorded 592 search decisions, zero search failures,
  and a 0.470-second maximum decision latency
- Main SHA-256:
  `a79119ff855566568440ae1c595dc8c5794a6917c028d856c0cac2952de44315`
- Deck SHA-256:
  `0598646548d081832ec311c15fdc369b32c6f5e63175b0cfd1904d21fd082451`
- Windows runtime SHA-256:
  `a3a401d0f5ccc3474b9c8a7a2431920c4b728d28105a510aa6927ad6283e5cf7`
- Linux runtime SHA-256:
  `feafd4046b2f688bdb33a4972c139b78e13e243ab5707ece52c43cf39a34b887`
- Linux ARM64 runtime SHA-256:
  `116750365a1043f0d95e200bb283c042753cdbd44c7d16331827ad0a44df0553`
- macOS runtime SHA-256:
  `00154aee7d3071451096c929c52da9f9af360a2821e686671097f5011e5a5d95`
- Archive SHA-256:
  `2fd5d69ac29283b3c7a6a6532a0dcc16b32e666cba2ca2547cc8bad5b7e2a3cf`

Result:
- Kaggle accepted the package and marked submission `54996323` complete.
- Public evaluation moved from the 600.0 baseline through 705.2 and 796.9
  before reaching 880.8 as additional validation battles accumulated.
- Score checkpoint: `2026-07-26 09:06 UTC`.
