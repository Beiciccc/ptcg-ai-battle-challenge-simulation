# 022 Guard Lucario Full Reroll

Date: 2026-06-21

Package: `artifacts/submissions/s009-resubmit-lucario-full.tar.gz`

Kaggle submission: `53906929`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the historical full Lucario policy and original Mega Lucario
  deck package as the first 2026-06-21 guard repair slot.
- The submission completed, but the initial public score was weak relative to
  the original run and to the refreshed 2026-06-20 guard runs.

Validation:
- `python tools/check_submission_entrypoint.py /tmp/ptcg-verify-s009/main.py`
- `python tools/check_deck.py /tmp/ptcg-verify-s009/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `tar -tzf artifacts/submissions/s009-resubmit-lucario-full.tar.gz`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
