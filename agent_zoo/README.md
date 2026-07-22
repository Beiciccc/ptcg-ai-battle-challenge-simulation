# PTCG Source-only Agent Zoo

This directory stores 38 content-addressed strategy source snapshots recovered
from the historical packages named in `experiments/`. The manifest maps those
snapshots to all 162 recorded experiments, 000 through 161, while avoiding
duplicate source copies.

The snapshots are not complete Kaggle submissions. They intentionally exclude
the competition runtime (`cg/`), engine binaries, trained model weights, replay
data, and other competition assets. `main.py` and `deck.csv` are always present;
Python source dependencies are included only when they were part of the
historical package and pass the explicit source allowlist.

Historical package paths are metadata only. The original `.tar.gz` and `.zip`
archives are not committed and are not currently downloadable from this
repository or its releases.

## Materialize All Experiments

Run from the repository root:

```bash
python tools/materialize_agents.py --all
```

The tool reads `manifest.json`, extracts each file from source commit
[`f46b15b`](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)
with `git show`, verifies every byte count and SHA256, and writes one directory
per experiment under `artifacts/agent_zoo/agents/`. Generated files are ignored
by Git.

Use `--experiment 004` instead of `--all` to materialize one entry. Pass
`--force` only to replace a prior Agent Zoo output created by this tool.

## Manifest Fields

`manifest.json` and `manifest.csv` provide the experiment ID, source paths,
source commit, experiment record commit, Kaggle submission reference, public
score checkpoint, archive SHA256, source-file SHA256 values, upstream notebook
URL when recorded, and reproducibility status.

Experiments 133 and 147 retain complete source but require excluded model data.
All entries require the public Kaggle runtime, which users must download
directly after accepting the competition rules.

Source-only tar and zip bundles are available on the
[GitHub Releases page](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/releases).

See `THIRD_PARTY_NOTICES.md` and each snapshot's `ORIGIN.json` for provenance
and license scope. The root MIT license does not replace upstream terms for
third-party snapshots.
