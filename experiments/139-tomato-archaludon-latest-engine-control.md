# 139 Tomato Archaludon Latest-Engine Control

Date: 2026-07-18 UTC

Package: `artifacts/submissions/s139-tomato-archaludon-latest-engine-control.tar.gz`

Kaggle submission: `54797915`

Validation episode: `86614292`

Public score: 573.1

Status: complete

Summary:
- Migrated the reproducible Tomato Archaludon strategy from experiment 130 to
  the official July 17 engine update.
- Preserved the parent `main.py` and `deck.csv` bytes to isolate the runtime
  update from strategy changes.
- Used this run to compare a second Archaludon strategy with the existing
  latest-engine references.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck return
- Candidate smoke battles completed in 127, 161, and 58 steps with no scoring
  exception or random fallback
- Archive-root smoke battle completed in 155 steps with no scoring exception
  or random fallback
- Official replay completed in 130 steps; exact-byte replay checks reported no
  scoring exception, generic fallback, random fallback, timeout, or runtime error
- Main SHA-256: `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`
- Deck SHA-256: `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`
- Archive SHA-256: `97de047d4f4cad11ac77378b1cbc52da3d11b0989f032be02ed3dce7eb8ff0f0`

Result:
- Kaggle validation episode `86614292` completed normally in 130 steps with
  reward `[-1, 1]` and both players in the DONE state.
- The score moved from the 600.0 baseline through 467.1 to the current 573.1.
- The current result does not meet the threshold to replace the Lucario and
  Search-Augmented Alakazam final-pair candidates.
