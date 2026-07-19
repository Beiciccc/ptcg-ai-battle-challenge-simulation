# 143 Tien Search Alakazam Current Anchor

Date: 2026-07-19 UTC

Package: `artifacts/submissions/s143-tien-search-alakazam-current-anchor.tar.gz`

Kaggle submission: `54819548`

Validation episode: `86795281`

Public score: 729.6

Status: complete

Source:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)

Summary:
- Re-submitted the exact latest-engine archive from experiment 136 as the
  current-day Alakazam anchor.
- Selected this profile after its two prior fixed-engine submissions reached
  828.7 and 840.2 and the local comparison beat four current profiles.
- Preserved every archive byte so the new observation changes only the public
  evaluation window.

Validation:
- Exact-byte match with experiment 136
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck return
- Archive-root smoke battles completed in 193, 46, and 171 steps
- Main SHA-256: `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`
- Deck SHA-256: `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`
- Archive SHA-256: `f66cfe7e6bdf06656b7d61265ff959309d20117a729de2cb6cf3117d651a1c76`

Result:
- Kaggle accepted the package and marked submission `54819548` complete.
- Validation episode `86795281` reached the completed terminal state with
  reward `[1, -1]`.
- The first two public-score reads were the 600.0 baseline; later public
  evaluation raised the score to 729.6 at the 2026-07-19 01:48 UTC checkpoint.
- This remains the stable reference while additional public battles accrue.
