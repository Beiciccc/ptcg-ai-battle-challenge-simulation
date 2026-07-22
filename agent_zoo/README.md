# PTCG Source-only Agent Zoo

This directory stores content-addressed strategy source snapshots recovered from
the historical packages named in `experiments/`. Each snapshot preserves the
source bytes used by one or more experiments while avoiding duplicate copies.

The snapshots are not complete Kaggle submissions. They intentionally exclude
the competition runtime (`cg/`), engine binaries, trained model weights, replay
data, and other competition assets. `main.py` and `deck.csv` are always present;
small source-side dependencies are included only when they are part of the
historical package and pass the explicit source allowlist.

Use `tools/materialize_agents.py --all` from the repository root to create one
local directory per experiment. The generated directories live under ignored
`artifacts/` paths and are not committed.

See `THIRD_PARTY_NOTICES.md` and each snapshot's `ORIGIN.json` for provenance
and license scope. The root MIT license does not replace upstream terms for
third-party snapshots.
