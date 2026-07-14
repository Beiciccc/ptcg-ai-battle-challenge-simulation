# 117 Tien Search Alakazam Hardened

Date: 2026-07-14 UTC

Package: `artifacts/submissions/s117-tien-search-alakazam-hardened.tar.gz`

Kaggle submission: `54676655`

Validation episode: `85886634`

Public score: 704.7

Status: complete

Source:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)
- The published checkpoint reports a 1034.6 ladder result from 2026-07-05 and
  identifies itself as an older, superseded checkpoint.

Summary:
- Rebuilt the published 60-card Alakazam checkpoint with the standard
  cross-platform competition runtime.
- Added the missing `sys` import used by search fallback diagnostics. No
  strategy weights, search parameters, or deck entries changed.
- Later score refreshes recovered above 700 but remained below the 800-point
  final-active threshold.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- Final top-level function: `agent`
- 60-card deck check
- Missing-template and missing-search-input fallback checks
- Three seeded archive-root smoke battles completed in 168, 181, and 159 steps
- Maximum observed main-decision wall time: 0.808 seconds
- Archive SHA-256: `766fe6a21ee6f73b58f857a8cfefc6b43028b7f157face837c342d5d47a36798`

Result:
- Kaggle validation episode `85886634` completed.
- Latest refreshed public score was 704.7.
