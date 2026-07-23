# Pokemon TCG AI Battle

Public project space for the Kaggle competition:
[Pokemon TCG AI Battle](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle).

The repository keeps strategy source snapshots, data notes, submission
packaging tools, and experiment records. Raw competition files and generated
submissions are not committed.

## Archive Availability

Historical `.tar.gz` and `.zip` submission archives are **not committed and are
not currently downloadable** from this repository or its releases. Package
paths in experiment notes are local generated locations, not links to hosted
files.

The public download is a source-only Agent Zoo. It excludes `cg/`, engine
binaries, model data, replay data, and raw competition assets. Full submission
archives will only be published after the original artifacts are recovered and
the applicable competition and upstream terms are confirmed to permit
redistribution.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"

python tools/download_assets.py --light
python tools/check_deck.py submission/deck.csv
python tools/package_submission.py --name baseline
```

The generated package is written under `artifacts/submissions/`.

## Source-only Agent Zoo

The version 1.0.0 [Agent Zoo](agent_zoo/README.md) is a frozen snapshot covering
experiments 000 through 161 with 162 experiment entries and 38
content-addressed source snapshots. Every entry records `main.py`, `deck.csv`,
the source commit, Kaggle submission reference, public-score checkpoint,
archive hash, and source-file SHA256 values.

Materialize one directory per experiment directly from Git history:

```bash
python tools/materialize_agents.py --all
```

The result is written to `artifacts/agent_zoo/`. Download the public competition
runtime yourself after accepting the Kaggle rules:

```bash
python tools/download_assets.py --light
```

Add the downloaded `submission/cg/` directory to a materialized agent before
using `tools/package_submission.py --source ...` to build a local submission
archive. Experiments 133 and 147 also require model data that is deliberately
not included in the source-only package.

Prebuilt source-only bundles are published on the
[GitHub Releases page](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/releases).

## Project Layout

```text
configs/              Experiment configuration files
data/metadata/         Public schema notes and small metadata files
docs/                  Data notes, submission notes, and experiment log
experiments/           Human-readable experiment records
agent_zoo/             Content-addressed strategy source and manifests
notebooks/             Local exploration notebooks
src/ptcg_battle/       Reusable Python utilities
submission/            Kaggle submission entrypoint and deck file
tests/                 Sanity tests for reusable utilities
tools/                 CLI helpers for data, validation, packaging, and submit
```

## Data

Competition data is downloaded through the Kaggle CLI and stored in
`data/raw/competition/`, which is intentionally ignored by git. See
`docs/data_notes.md` for the current file inventory and schema summary.

## Experiments

Experiment summaries are recorded in `docs/experiment_log.md` and detailed
notes live under `experiments/`. Public scores are recorded checkpoints and may
change on the live leaderboard.

## License

Project-authored tooling is released under the MIT License. Third-party strategy
snapshots retain their upstream terms; see
`agent_zoo/THIRD_PARTY_NOTICES.md`. Competition data and runtime files are
governed by Kaggle and competition-specific terms.
