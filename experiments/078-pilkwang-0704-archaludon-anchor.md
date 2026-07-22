# 078 Pilkwang 0704 Archaludon Anchor

Date: 2026-07-06 UTC

Local generated package (not committed): `artifacts/submissions/s078-pilkwang-0704-archaludon-anchor.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/a4c53101be30-fbe6ab599922/main.py), [deck.csv](../agent_zoo/sources/a4c53101be30-fbe6ab599922/deck.csv)

Source SHA256: main.py `a4c53101be301c181bd477204a72c0e5cba65fddd34d8cd0ec4d36e4b41c9518`; deck.csv `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54379422`

Public score: 682.6

Status: complete

Summary:
- Tested the 2026-07-04 public meta snapshot's Archaludon Metal Tempo anchor.
- This was selected after the Library-Out complement underperformed, because
  the snapshot described the anchor as a near-top field-weighted reference.
- The public score stayed below guard range, so the next slot spent only one
  more probe on the distinct pressure profile before returning to known guards.

Validation:
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/package_submission.py --name s078-pilkwang-0704-archaludon-anchor`
- `python tools/smoke_battle.py --games 1 --max-steps 400`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 682.6.
