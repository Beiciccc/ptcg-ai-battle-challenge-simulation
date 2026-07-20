# 148 Makthanithin Archaludon Cinderace Current Code

Date: 2026-07-20 UTC

Package: `artifacts/submissions/s148-makthanithin-archaludon-cinderace-current-code.tar.gz`

Kaggle submission: `54843847`

Public score: 660.9

Status: complete

Source:
- [Pokemon TCG AI Battle Meta Snapshot 06-29](https://www.kaggle.com/code/makthanithin/pok-mon-tcg-ai-battle-meta-snapshot-06-29)

Summary:
- Tested the current public Archaludon ex and Cinderace policy as a distinct
  rule-based challenger to the V9 behavior-cloning probe.
- Preserved the published `main.py` and `deck.csv` bytes, paired them with the
  current competition runtime, and omitted generated Python cache files from
  the published output archive.
- The deck uses Cinderace's setup and acceleration route to develop Duraludon
  before evolving into Archaludon ex.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Three isolated extracted-archive smoke battles completed in 46, 125, and 139
  steps
- Sixteen two-orientation comparison games against experiment 147 completed
  without runtime errors; this candidate won all 16 in 47 to 154 steps
- Packaged engine binaries match the current competition sample
- Published output SHA-256: `9c949edabb9d55d6bc755f32d1f3e30f58a483cb5d57e0708d66dd67215e8ec3`
- Main SHA-256: `a4c53101be301c181bd477204a72c0e5cba65fddd34d8cd0ec4d36e4b41c9518`
- Deck SHA-256: `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Archive SHA-256: `c7d2ad2b4cd369b997380b70168207a2e673f1b5ce34a4f45ac2752d1b4f4f37`

Result:
- Kaggle accepted the package and marked submission `54843847` complete.
- Public evaluation moved from the 600.0 baseline through 716.9 and 628.8 to
  660.9; the local matchup result is retained as validation evidence rather
  than a leaderboard claim.
- Score checkpoint: `2026-07-20 03:44 UTC`.
