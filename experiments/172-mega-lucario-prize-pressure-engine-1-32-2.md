# 172 Mega Lucario Prize-Pressure Engine 1.32.2

Date: 2026-07-25 UTC

Local generated package (not committed): `artifacts/submissions/s172-mega-lucario-prize-pressure-engine-1-32-2.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/459cf970d9ff-2a541d7bf3d9/main.py), [deck.csv](../agent_zoo/sources/459cf970d9ff-2a541d7bf3d9/deck.csv)

Source SHA256: main.py `459cf970d9ffc28fcb13473cff216750f17d53a35fa990fcab1805e00e78a848`; deck.csv `2a541d7bf3d9e6b36037123f53f4dfef6348223f79fd27095dafc602a5357c19`

Reproducibility: exact public strategy snapshot with Kaggle Environments 1.32.2 runtime binaries

Kaggle submission: `54970593`

Public score: 875.5

Status: complete

Sources:
- [Pokemon TCG AI Battle Meta Snapshot 18 July](https://www.kaggle.com/code/pilkwang/pok-mon-tcg-ai-battle-meta-snapshot-18-july)
- [Minor Engine update](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/discussion/728587)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Preserved the exact Mega Lucario Prize-Pressure strategy and deck used by
  experiments 134 and 141 while migrating all runtime binaries to 1.32.2.
- Revisited the strategy because its two prior public observations reached
  854.0 and 736.4 and it remained under-sampled on the current engine.
- Used repeated games in one process to verify that its turn plan and ability
  state reset correctly across battles.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact initial deck-return check
- Six same-process mirror battles completed in 145, 138, 117, 158, 124, and
  140 steps without errors
- Eight seat-alternated battles against Search-Audited Alakazam V12 completed
  3-5 in 130, 147, 148, 121, 144, 50, 105, and 154 steps without errors
- Eight seat-alternated battles against Archaludon Metal completed 8-0 in 28,
  121, 93, 28, 117, 108, 138, and 146 steps without errors
- Eight seat-alternated battles against the Great Tusk / Crustle V11 control
  completed 8-0 in 80, 73, 70, 66, 50, 20, 90, and 32 steps without errors
- Main SHA-256: `459cf970d9ffc28fcb13473cff216750f17d53a35fa990fcab1805e00e78a848`
- Deck SHA-256: `2a541d7bf3d9e6b36037123f53f4dfef6348223f79fd27095dafc602a5357c19`
- Windows runtime SHA-256: `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256: `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256: `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256: `f37da75bf56dc34bfc0dc21cf74430df9ce4f336669bc3a2a0fcac2d07a5d574`

Result:
- Kaggle accepted the package and marked submission `54970593` complete.
- Public evaluation moved from the 600.0 baseline to 875.5.
- Score checkpoint: `2026-07-25 08:08 UTC`.
