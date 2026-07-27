# 181 Visible Field Router v3 Entry Fix

Date: 2026-07-27 UTC

Local generated package (not committed):
`artifacts/submissions/s181-prvsiyan-visible-field-router-v3-entryfix.tar.gz`

Reproducibility: public Router v3 strategy with one appended loader entrypoint

Kaggle submission: `55024028`

Public score: 600.0

Status: complete

Sources:
- [Visible Field Router v3](https://www.kaggle.com/code/prvsiyan/ptcg-visible-field-router-v3)
- [Leaderboard deck meta by score band](https://www.kaggle.com/code/myso1987/ptcg-ai-battle-leaderboard-deck-meta-by-score-band)
- [Kaggle Environments agent loader](https://github.com/Kaggle/kaggle-environments/blob/8418fb28e8a826ca3edff9561cf8e7ba11559e69/kaggle_environments/agent.py)

Summary:
- Preserved the public Great Tusk / Crustle deck, strategy, and current
  competition runtime.
- Retained visible-field routing for Alakazam, Grimmsnarl, and water-tempo
  matchups without using opponent identity or external services.
- Appended the fresh global wrapper `submission_entrypoint` so Kaggle selects
  the intended final policy.

Validation:
- Static entrypoint check selected `submission_entrypoint`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Four loader-aware mirror games completed without errors
- Eight games against Visible-Grim Alakazam completed 6-2
- Eight games against current-runtime Steel completed 7-1
- Eight games against replay-trained Grimmsnarl completed 7-1
- Eight games against Mega Lucario Prize-Pressure completed 5-3
- Maximum observed Router decision latency was 0.065 seconds
- Submitted main SHA-256:
  `fdd8794a042e110739797086a58eb3911bafc226e24a167453f11647c653e7af`
- Deck SHA-256:
  `6415396d35c0f4b3d69ee6c231337968cc9f2d5d0767de801346d6f412c18e62`
- Windows runtime SHA-256:
  `a3a401d0f5ccc3474b9c8a7a2431920c4b728d28105a510aa6927ad6283e5cf7`
- Linux runtime SHA-256:
  `feafd4046b2f688bdb33a4972c139b78e13e243ab5707ece52c43cf39a34b887`
- Linux ARM64 runtime SHA-256:
  `116750365a1043f0d95e200bb283c042753cdbd44c7d16331827ad0a44df0553`
- macOS runtime SHA-256:
  `00154aee7d3071451096c929c52da9f9af360a2821e686671097f5011e5a5d95`
- Archive SHA-256:
  `2b7de631a7c36f45de4fc267434416a106440483357002275d9b56c51b4c9165`

Result:
- Kaggle accepted the package and marked submission `55024028` complete.
- Two spaced reads remained at the 600.0 initial public checkpoint.
- Score checkpoint: `2026-07-27 09:06 UTC`.
