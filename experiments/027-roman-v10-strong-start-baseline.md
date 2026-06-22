# 027 Roman V10 Strong Start Baseline

Date: 2026-06-22

Package: `artifacts/submissions/s027-roman-v10-strong-start-baseline.tar.gz`

Kaggle submission: `53945192`

Public score: 652.0

Status: complete

Summary:
- Tested the public Roman V10 Strong Start baseline after the 2026-06-22 code
  refresh identified it as a high-signal updated baseline.
- The package validated successfully, but the refreshed public score stayed
  below the strongest guard candidates.

Validation:
- `python tools/check_submission_entrypoint.py /tmp/ptcg-source-roman_v10/main.py`
- `python tools/check_deck.py /tmp/ptcg-source-roman_v10/deck.csv`
- `python tools/package_submission.py --source /tmp/ptcg-source-roman_v10 --name s027-roman-v10-strong-start-baseline`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 652.0.
