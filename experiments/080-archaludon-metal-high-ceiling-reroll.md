# 080 Archaludon Metal High Ceiling Reroll

Date: 2026-07-06 UTC

Package: `artifacts/submissions/s080-archaludon-metal-high-ceiling-reroll.tar.gz`

Kaggle submission: `54379739`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Archaludon metal high-ceiling package after the new
  2026-07-04 public snapshot profiles failed to reach guard range.
- The package has the best historical public result in this workspace, but this
  reroll opened weak.
- The final slot should use the stronger Tomato Archaludon guard profile.

Validation:
- `tar -tzf artifacts/submissions/s080-archaludon-metal-high-ceiling-reroll.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Public score was 600.0.
