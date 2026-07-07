# 082 Archaludon Metal Current Frontier Reroll

Date: 2026-07-07 UTC

Package: `artifacts/submissions/s082-archaludon-metal-current-frontier-reroll.tar.gz`

Kaggle submission: `54410344`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Archaludon metal package after the 2026-07-07 public
  Code/Discussion refresh showed mostly replay/meta-analysis updates rather
  than a newly validated stronger implementation.
- The package remains a historically high-ceiling guard, but this reroll opened
  weak.
- The next slot shifts to the Dragapult pressure profile for a complementary
  current-meta probe.

Validation:
- `tar -tzf artifacts/submissions/s082-archaludon-metal-current-frontier-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py /tmp/ptcg_validate_pkg/s052/main.py`
- `python tools/check_deck.py /tmp/ptcg_validate_pkg/s052/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Public score was 600.0.
