# 189 Plamen06 Steel Final Active

Date: 2026-07-28 UTC

Local generated package (not committed):
`artifacts/submissions/s189-plamen06-steel-final-active.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 179 and 186

Kaggle submission: `55052024`

Public score: 706.1

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact search-disabled Steel archive from experiment 186 as the
  first final active strategy.
- Preserved the strategy, 60-card deck, loader entrypoint, runtime, and archive
  bytes.
- Retained Steel as a distinct strategy family beside the final Alakazam
  observation.

Validation:
- Archive SHA-256 matched experiments 179 and 186 exactly
- Static and dynamic loader checks selected the final `agent` callable
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Two fresh loader-aware mirror games split 1-1 without errors
- No invalid actions or timeouts occurred
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
- Kaggle accepted the package as submission `55052024` and marked it complete.
- Public evaluation moved from 600.0 through 610.1 before reaching 706.1.
- Score checkpoint: `2026-07-28 10:17 UTC`.
