# Pokemon TCG AI Battle

Public project space for the Kaggle competition:
[Pokemon TCG AI Battle](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle).

The repository keeps reproducible code, data notes, submission packaging tools,
and experiment records. Raw competition files and generated submissions are not
committed; use the scripts below to recreate them locally.

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

## Project Layout

```text
configs/              Experiment configuration files
data/metadata/         Public schema notes and small metadata files
docs/                  Data notes, submission notes, and experiment log
experiments/           Human-readable experiment records
kaggle/notebooks/      Notebook handoff notes
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
notes live under `experiments/`. Each submitted package should be tied to a
dated experiment note with the public leaderboard result once available.

## License

Code in this repository is released under the MIT License. Competition data is
governed by Kaggle and competition-specific terms.
