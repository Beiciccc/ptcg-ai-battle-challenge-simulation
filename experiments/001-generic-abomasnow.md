# 001 Generic Abomasnow

Date: 2026-06-17

Package: `artifacts/submissions/s001-generic-abomasnow.tar.gz`

Kaggle submission: `53783585`

Status: error

Summary:
- Kept the sample Mega Abomasnow deck.
- Replaced the first baseline policy with a generic heuristic policy.

Result:
- Kaggle validation returned `SubmissionStatus.ERROR`.
- Validation logs showed the runtime called the last helper function instead of
  `agent()`.

Fix:
- Keep `agent()` as the final top-level function in `submission/main.py`.
- Added `tools/check_submission_entrypoint.py`.
