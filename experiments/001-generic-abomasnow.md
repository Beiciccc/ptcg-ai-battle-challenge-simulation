# 001 Generic Abomasnow

Date: 2026-06-17

Local generated package (not committed): `artifacts/submissions/s001-generic-abomasnow.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/99c370eacd00-e92d5717fd04/main.py), [deck.csv](../agent_zoo/sources/99c370eacd00-e92d5717fd04/deck.csv)

Source SHA256: main.py `99c370eacd0097b17a951a875dc49e4721c9024f74911be11dd935a16e4c7c1b`; deck.csv `e92d5717fd04865b0b528307df7a9d9aecc2c7b917bfbd5042fe58e3d1f26997`

Reproducibility: exact source snapshot; Kaggle runtime required

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
