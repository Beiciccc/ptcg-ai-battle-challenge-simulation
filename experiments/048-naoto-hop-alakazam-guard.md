# 048 Naoto Hop Alakazam Guard

Date: 2026-06-28 UTC

Package: `artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`

Kaggle submission: `54152792`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the historical Naoto Hop/Alakazam guard package after the new
  2026-06-28 Option C candidate underperformed.
- The package remains the strongest historical local result, with prior public
  runs reaching 1027.6, 854.6, 835.2, and 822.1 after refresh.
- The accepted submission opened weakly, so the next slot should include a
  different archetype or guard package rather than another immediate repeat.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
