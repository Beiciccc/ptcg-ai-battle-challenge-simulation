# 084 Yaminh Lucario Challenge

Date: 2026-07-07 UTC

Local generated package (not committed): `artifacts/submissions/s084-yaminh-lucario-challenge.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/d627fa239976-dc2b68464064/main.py), [deck.csv](../agent_zoo/sources/d627fa239976-dc2b68464064/deck.csv)

Source SHA256: main.py `d627fa239976dc9841989e7ad42872faa97235abfbca94b3604a118adba912c8`; deck.csv `dc2b68464064ae885ad04704dc032853526584afa9bec408984e23cc4840bd5e`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54410567`

Validation episode: `84493517`

Public score: 647.6

Status: complete

Summary:
- Tested a newly refreshed public Lucario/Fighting candidate after two
  current-meta rerolls opened low.
- The candidate passed local package and smoke validation, including a
  one-game self-play smoke battle.
- The latest refresh stayed below the leading guard packages, so the next slot
  returned to the Archaludon metal high-ceiling package.

Validation:
- `tar -tzf artifacts/submissions/s084-yaminh-lucario-challenge.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 800`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84493517` completed.
- Latest refreshed public score was 647.6.
