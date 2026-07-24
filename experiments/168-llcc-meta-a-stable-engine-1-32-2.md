# 168 LLCC Meta A Stable Engine 1.32.2

Date: 2026-07-24 UTC

Local generated package (not committed): `artifacts/submissions/s168-llcc-meta-a-stable-engine-1-32-2.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/6d2c8efc2243-fbe6ab599922/main.py), [deck.csv](../agent_zoo/sources/6d2c8efc2243-fbe6ab599922/deck.csv)

Source SHA256: main.py `6d2c8efc224392dcc439fa7ce20669daf279aa0208b23f87a7bab988b93561e2`; deck.csv `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`

Reproducibility: exact strategy snapshot with Kaggle Environments 1.32.2 runtime binaries

Kaggle submission: `54939275`

Public score: 699.1

Status: complete

Sources:
- [Experiment 135](135-llcc-meta-a-stable-latest-engine-final-active.md)
- [Minor Engine update](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/discussion/728587)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Preserved the Stable LLCC strategy and deck bytes while migrating the four
  platform binaries to Kaggle Environments 1.32.2.
- Selected the package as a non-Alakazam diagnostic after the first two
  1.32.2 anchors opened below their mature historical distributions.
- Retained the search-capable competition sample Python API to keep all
  current-runtime packages on the same wrapper and binary baseline.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Runtime import exposed 1,267 cards and 1,556 attacks without fallback
- Three isolated extracted-archive battles completed normally in 109, 125,
  and 87 steps
- Four seat-alternated battles against the 1.32.2 Tien package completed 1-3
  in 53, 189, 119, and 147 steps with zero errors
- Four seat-alternated battles against the 1.32.2 Tomato package completed 2-2
  in 134, 164, 144, and 60 steps with zero errors
- Main SHA-256: `6d2c8efc224392dcc439fa7ce20669daf279aa0208b23f87a7bab988b93561e2`
- Deck SHA-256: `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Windows runtime SHA-256: `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256: `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256: `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256: `62836f6f6b9a4d27a621c3719d1ee0ce8534cb1a8e9a716b2bed874fa72f0304`

Result:
- Kaggle accepted the package and marked submission `54939275` complete.
- Two spaced official reads remained at the 600.0 baseline before later
  evaluation moved to 699.1.
- Score checkpoint: `2026-07-24 00:44 UTC`.
