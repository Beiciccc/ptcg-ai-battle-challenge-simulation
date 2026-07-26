# 178 Observable Meta Router v1 Entry Fix

Date: 2026-07-26 UTC

Local generated package (not committed):
`artifacts/submissions/s178-prvsiyan-observable-meta-router-v1-entryfix.tar.gz`

Reproducibility: public Router v1 strategy with an appended loader entrypoint

Kaggle submission: `54996460`

Public score: 600.0

Status: complete

Sources:
- [Observable Meta Router v1](https://www.kaggle.com/code/prvsiyan/ptcg-observable-meta-router-v1)
- [Kaggle Environments agent loader](https://github.com/Kaggle/kaggle-environments/blob/8418fb28e8a826ca3edff9561cf8e7ba11559e69/kaggle_environments/agent.py)

Summary:
- Preserved the public Great Tusk / Crustle strategy, deck, runtime, and final
  observable-matchup routing overrides.
- Appended the fresh global wrapper `submission_entrypoint`, which delegates
  directly to the published `agent`.
- Avoided changing any card, scoring, fallback, or matchup-routing logic.

Validation:
- Static entrypoint check selected `submission_entrypoint`
- Kaggle's `get_last_callable` selected `submission_entrypoint` at source line
  1300
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Three loader-aware mirror games completed without errors
- Eight loader-aware games against Visible-Grim Alakazam completed 5-3
- Eight loader-aware games against Steel completed 6-2
- Eight loader-aware games against Mega Lucario Prize-Pressure completed 5-3
- The 27-game validation recorded 1,469 Router decisions with no errors and a
  0.016-second maximum Router decision latency
- Main SHA-256:
  `125247671f85ecea69e61444904efd103e346001e68b928f7f48f2d19eeea1b9`
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
  `7ba6b408582ad4429cbbdda27d3ccf4da135ba292940fe12a0d9e8204e189814`

Result:
- Kaggle accepted the package and marked submission `54996460` complete.
- The first public evaluation checkpoint was 600.0.
- Score checkpoint: `2026-07-26 08:53 UTC`.
