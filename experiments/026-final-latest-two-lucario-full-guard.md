# 026 Final Latest-Two Lucario Full Guard

Date: 2026-06-21

Package: `artifacts/submissions/s009-resubmit-lucario-full.tar.gz`

Kaggle submission: `53907370`

Public score: 632.7

Status: complete

Summary:
- Re-submitted the historical full Lucario guard package as the final
  latest-two slot for the 2026-06-21 batch.
- The submission completed, and the refreshed public score stayed below the
  strongest 2026-06-21 run.

Validation:
- `python tools/check_submission_entrypoint.py /tmp/ptcg-verify-s009/main.py`
- `python tools/check_deck.py /tmp/ptcg-verify-s009/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `tar -tzf artifacts/submissions/s009-resubmit-lucario-full.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 632.7.
