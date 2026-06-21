# 023 Crustle Specific High Diversity Reroll

Date: 2026-06-21

Package: `artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Kaggle submission: `53907042`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the historical Crustle-specific policy and wall deck package as
  a high-diversity repair slot after the first 2026-06-21 guard reroll scored
  weakly.
- The submission completed, but the initial public score was also weak.

Validation:
- `python tools/check_submission_entrypoint.py /tmp/ptcg-verify-s010/main.py`
- `python tools/check_deck.py /tmp/ptcg-verify-s010/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `tar -tzf artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
