# 024 Alakazam Psychic Control

Date: 2026-06-21

Package: `artifacts/submissions/s024-alakazam-psychic-control.tar.gz`

Kaggle submission: `53907175`

Public score: 600.0

Status: complete

Summary:
- Tested a public Alakazam psychic-control candidate after the latest public
  code and discussion scan suggested that control-style decks were becoming
  more relevant than older Lucario-only baselines.
- The candidate validated successfully but did not improve the current public
  result.

Validation:
- `python tools/check_submission_entrypoint.py /tmp/ptcg-alakazam-source/main.py`
- `python tools/check_deck.py /tmp/ptcg-alakazam-source/deck.csv`
- `python tools/package_submission.py --source /tmp/ptcg-alakazam-source --name s024-alakazam-psychic-control`
- `tar -tzf artifacts/submissions/s024-alakazam-psychic-control.tar.gz`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
