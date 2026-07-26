# 180 Visible-Grim Belief Alakazam v18 Final Active

Date: 2026-07-26 UTC

Local generated package (not committed):
`artifacts/submissions/s180-visible-grim-belief-alakazam-v18-final-active.tar.gz`

Reproducibility: exact byte-for-byte rerun of experiment 177

Kaggle submission: `54996685`

Public score: 461.8

Status: complete

Sources:
- [Visible-Grim Belief Alakazam v18](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-visible-grim-belief-alakazam-v18)
- [Kaggle Environments agent loader](https://github.com/Kaggle/kaggle-environments/blob/8418fb28e8a826ca3edff9561cf8e7ba11559e69/kaggle_environments/agent.py)

Summary:
- Re-submitted the exact experiment 177 archive after its independent public
  observation reached 880.8.
- Retained the entrypoint repair that makes Kaggle's loader select
  `submission_entrypoint`.
- Preserved every strategy, deck, runtime, and archive byte.

Validation:
- Archive SHA-256 matched experiment 177 exactly
- Static entrypoint check selected `submission_entrypoint`
- Kaggle's `get_last_callable` selected `submission_entrypoint`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Three loader-aware mirror games completed without errors
- Eight loader-aware games against Observable Meta Router split 4-4
- Eight loader-aware games against current-runtime Steel split 4-4
- The 19-game validation recorded 518 search decisions, zero search failures,
  and a 0.328-second maximum decision latency
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
- Kaggle accepted the package and marked submission `54996685` complete.
- Public evaluation moved from the 600.0 baseline to 461.8 as additional
  validation battles accumulated.
- Score checkpoint: `2026-07-26 09:11 UTC`.
