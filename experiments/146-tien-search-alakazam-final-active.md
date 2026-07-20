# 146 Tien Search Alakazam Final Active

Date: 2026-07-19 UTC

Package: `artifacts/submissions/s146-tien-search-alakazam-final-active.tar.gz`

Kaggle submission: `54819874`

Validation episode: `86798534`

Public score: 763.8

Status: complete

Source:
- [Search-Augmented Heuristic Agent (Alakazam)](https://www.kaggle.com/code/tientrum/search-augmented-heuristic-agent-alakazam)

Summary:
- Re-submitted the exact latest-engine Search-Augmented Alakazam archive as
  the second and final member of the active pair.
- Retained Alakazam after its current-day probe reached 729.6 with a 3-1
  public record and its prior fixed-engine runs reached 828.7 and 840.2.
- Preserved every archive byte so the new observation changes only the active
  public evaluation window.

Validation:
- Exact-byte match with experiments 136, 140, and 143
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck return
- Archive-root smoke battles completed in 204, 171, and 153 steps
- Main SHA-256: `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`
- Deck SHA-256: `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`
- Archive SHA-256: `f66cfe7e6bdf06656b7d61265ff959309d20117a729de2cb6cf3117d651a1c76`

Result:
- Kaggle accepted the package and marked submission `54819874` complete.
- Validation episode `86798534` reached the completed terminal state with
  reward `[-1, 1]`.
- Later public evaluation recovered from the 600.0 baseline to 763.8.
- The final active pair is Tomato Archaludon followed by Search-Augmented
  Alakazam.
- Score checkpoint: `2026-07-20 03:04 UTC`.
