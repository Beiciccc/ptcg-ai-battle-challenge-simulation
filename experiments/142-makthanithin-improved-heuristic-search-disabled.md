# 142 Makthanithin Improved Heuristic Search Disabled

Date: 2026-07-19 UTC

Package: `artifacts/submissions/s142-makthanithin-improved-heuristic-search-disabled.tar.gz`

Kaggle submission: `54819384`

Public score: 665.3

Status: complete

Source:
- [Improved Probabilistic agent](https://www.kaggle.com/code/makthanithin/improved-probabilistic-agent)

Summary:
- Tested the published anti-stall Lucario heuristic with the July 17 engine.
- Disabled the optional search branch because its calls did not match the
  current SDK return types and required hidden-card arguments. The published
  implementation therefore fell back to the deterministic heuristic.
- Preserved the published heuristic, deck, and runtime bytes to isolate that
  compatibility change.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck return
- Candidate and archive-root smoke battles completed three of three games each
- Published and search-disabled variants made identical choices in 441
  observed decisions across three games
- Eighteen cross-profile games completed without runtime errors: 2-4 against
  Search-Augmented Alakazam, 2-4 against the prior Lucario policy, and 3-3
  against Tomato Archaludon
- Main SHA-256: `a003528e417b48771e780c0bc1147e86953168c3e4d53625fb39e36ecc72dd08`
- Deck SHA-256: `2a541d7bf3d9e6b36037123f53f4dfef6348223f79fd27095dafc602a5357c19`
- Archive SHA-256: `498f96d2af5a3b97f076a0f7fb2ceaec8cf0613db94576e09dcdb466ac836fe6`

Result:
- Kaggle accepted the package and marked submission `54819384` complete.
- The first public score was the 600.0 baseline at 01:18 UTC. It later reached
  796.5 before later movement reached 665.3 at the 2026-07-19 01:48 UTC
  checkpoint.
- The local comparisons support treating this as an exploratory anti-stall
  profile rather than replacing the stronger Alakazam anchor.
- Final audit checkpoint: `2026-07-19 01:56 UTC`.
