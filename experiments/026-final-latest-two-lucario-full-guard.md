# 026 Final Latest-Two Lucario Full Guard

Date: 2026-06-21

Package: `artifacts/submissions/s009-resubmit-lucario-full.tar.gz`

Kaggle submission: `53907370`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the historical full Lucario guard package as the final
  latest-two slot for the 2026-06-21 batch.
- The submission completed, but the initial public score was weak. The strongest
  refreshed score in this five-submission batch was experiment 023.

Validation:
- `python tools/check_submission_entrypoint.py /tmp/ptcg-verify-s009/main.py`
- `python tools/check_deck.py /tmp/ptcg-verify-s009/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `tar -tzf artifacts/submissions/s009-resubmit-lucario-full.tar.gz`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
