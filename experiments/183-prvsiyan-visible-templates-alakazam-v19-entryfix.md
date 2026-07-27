# 183 Visible Templates Alakazam v19 Entry Fix

Date: 2026-07-27 UTC

Local generated package (not committed):
`artifacts/submissions/s183-prvsiyan-visible-templates-alakazam-v19-entryfix.tar.gz`

Reproducibility: public v19 strategy with one appended loader entrypoint

Kaggle submission: `55024382`

Public score: 600.0

Status: complete

Source:
- [Visible Templates Alakazam v19](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-visible-templates-alakazam-v19)

Summary:
- Preserved the public v19 strategy and Alakazam deck.
- Appended a fresh final `submission_entrypoint` so Kaggle's loader selects the
  intended agent wrapper.
- Evaluated the visible Great Tusk / Crustle response template added after the
  earlier visible-Grim belief policy.

Validation:
- Static entrypoint check selected the unique final `submission_entrypoint`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Four loader-aware mirror games completed without errors
- Eight games against experiment 177 Visible-Grim Alakazam completed 4-4
- Eight games against Static Tusk v24 completed 3-5
- Eight games against Visible Field Router v3 completed 3-5
- All 836 observed search calls completed without failures
- Maximum observed v19 decision latency was 0.595 seconds
- Main SHA-256:
  `ae30636e0d3b0ea4b4791af4fa20c9ffdcc509813daa2ceb008b757d75c7ffba`
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
  `05aac54f1ebbe73043fdf726e402be0425c659c5d4274a9fbc494334224ddfef`

Result:
- Kaggle accepted the package and marked submission `55024382` complete.
- Two spaced reads remained at the 600.0 initial public checkpoint.
- Score checkpoint: `2026-07-27 09:19 UTC`.
