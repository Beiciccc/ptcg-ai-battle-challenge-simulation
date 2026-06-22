# 025 Final Latest-Two Strongstart Guard

Date: 2026-06-21

Package: `artifacts/submissions/s011-final-strongstart-retuned.tar.gz`

Kaggle submission: `53907297`

Public score: 778.0

Status: complete

Summary:
- Re-submitted the retuned Strong Start guard package as the first final
  latest-two slot after the Alakazam exploration did not improve the public
  result.
- The submission completed, and the refreshed public score recovered from the
  initial result.

Validation:
- `python tools/check_submission_entrypoint.py /tmp/ptcg-verify-s011/main.py`
- `python tools/check_deck.py /tmp/ptcg-verify-s011/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `tar -tzf artifacts/submissions/s011-final-strongstart-retuned.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 778.0.
