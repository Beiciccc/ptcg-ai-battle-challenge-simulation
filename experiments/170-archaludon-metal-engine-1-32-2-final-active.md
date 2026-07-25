# 170 Archaludon Metal Engine 1.32.2 Final Active

Date: 2026-07-24 UTC

Local generated package (not committed): `artifacts/submissions/s170-archaludon-metal-engine-1-32-2-final-active.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/a4c53101be30-fbe6ab599922/main.py), [deck.csv](../agent_zoo/sources/a4c53101be30-fbe6ab599922/deck.csv)

Source SHA256: main.py `a4c53101be301c181bd477204a72c0e5cba65fddd34d8cd0ec4d36e4b41c9518`; deck.csv `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`

Reproducibility: exact public strategy snapshot with Kaggle Environments 1.32.2 runtime binaries

Kaggle submission: `54939559`

Public score: 713.1

Status: complete

Sources:
- [Meta Snapshot 06-29](https://www.kaggle.com/code/makthanithin/pok-mon-tcg-ai-battle-meta-snapshot-06-29)
- [Minor Engine update](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/discussion/728587)
- [Kaggle Environments runtime fix](https://github.com/Kaggle/kaggle-environments/commit/03ab2cc235b719e5a3bd0d19e2d2c62c65a4c303)

Summary:
- Preserved the exact Archaludon Metal strategy and deck bytes while migrating
  the four platform binaries to Kaggle Environments 1.32.2.
- Selected the package as the final non-Alakazam profile after 15 historical
  observations had a 719.2 median and 767.8 mean.
- Kept Search-Audited Alakazam V12 and Archaludon Metal as the final two
  distinct strategy families.

Validation:
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check and exact deck-return check
- Runtime import exposed 1,267 cards and 1,556 attacks without fallback
- Three isolated extracted-archive battles completed normally in 143, 124,
  and 142 steps with zero option-scoring errors or random fallback
- Four seat-alternated battles against the 1.32.2 V12 package completed 1-3
  in 190, 158, 107, and 134 steps with zero errors
- Four seat-alternated battles against the V11 strategy on the 1.32.2 runtime
  completed 1-3 in 96, 100, 118, and 73 steps with zero errors
- Main SHA-256: `a4c53101be301c181bd477204a72c0e5cba65fddd34d8cd0ec4d36e4b41c9518`
- Deck SHA-256: `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Windows runtime SHA-256: `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256: `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256: `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256: `5ba0aacf6de996443016be9df7b16dbad563adf3abfce3de86b27fe7f5119d02`

Result:
- Kaggle accepted the package and marked submission `54939559` complete.
- Two spaced official reads remained at the 600.0 baseline before later
  evaluation moved through 728.7 and 616.7 to 713.1.
- Score checkpoint: `2026-07-25 07:51 UTC`.
