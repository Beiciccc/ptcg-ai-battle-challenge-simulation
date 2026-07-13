# 116 Tomato Archaludon Final Active

Date: 2026-07-13 UTC

Package: `artifacts/submissions/s116-tomato-archaludon-final-active.tar.gz`

Kaggle submission: `54626933`

Validation episode: `85660609`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the validated Tomato Archaludon package as the second final
  active profile after the current-day probe rose above 900.
- Local validation passed for the nine-file archive layout, entrypoint,
  60-card deck, and three smoke battles. The Linux archive remained unchanged
  while local engine compatibility was used for macOS smoke validation.
- The validation episode completed successfully and the first public score
  opened at 600.0.

Validation:
- `tar -tzf artifacts/submissions/s116-tomato-archaludon-final-active.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- Three seeded smoke battles using the matching local engine binary
- Archive SHA-256 matched experiment 110: `e7e1e346054f6d482e1b890b8a67eb68fd7bc167a6a5642bbe516287c2eb2486`

Result:
- Kaggle validation episode `85660609` completed.
- First public score was 600.0.
