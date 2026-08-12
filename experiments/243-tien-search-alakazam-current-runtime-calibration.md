# 243 Tien Search Alakazam Current-Runtime Calibration

Date: 2026-08-12 UTC

Local generated package (not committed):
`artifacts/submissions/s150-tien-search-alakazam-strategy-control.tar.gz`

Official upload filename: `s150-tien-search-alakazam-strategy-control.tar.gz`

Reproducibility: exact current-runtime archive from experiment 150

Kaggle submission: `55454375`

Public score: 703.6

Status: complete

Sources:
- [Search-Alakazam strategy](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Mega Lucario Prize-Pressure](https://www.kaggle.com/code/pilkwang/a-mega-lucario-prize-pressure)
- [Starmie Temporal Challenger](https://www.kaggle.com/code/pilkwang/starmie-temporal-challenger-entryfix)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-tested the exact Search-Alakazam archive with the current complete runtime
  against two independently archived strategy families.
- The candidate completed 6-2 against Mega Lucario and 5-3 against Starmie,
  passing 11-5 overall with both candidate seats represented.
- All 24 comparison games completed without runtime errors, draws, or timeouts.

Validation:
- Archive SHA-256:
  `c651ecce49d10aa1975a359c08c179e10b7ecf1e2cb9703af1067c1b515aa1dd`.
- Main SHA-256:
  `235084ae725e0430f700d18fe1f2e3845b8a6209b34f1b5020c07db4ba9974e1`.
- Deck SHA-256:
  `a8c9177354b92abe5fb877f46b792b86f8ec9c4bc3551d5d16d4a89128f00976`.
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`.
- The archive contains 11 members: `main.py`, `deck.csv`, and the complete
  nine-file `cg/` runtime set.
- Fixed seeds were `2026081200-2026081215` against Tomato during screening,
  followed by `2026081232-2026081239` against Mega Lucario and
  `2026081216-2026081223` against Field during the candidate screen. The
  final submission gate used the two independently archived high-score
  anchors, Mega Lucario and Starmie, with 8 games per anchor.
- Maximum observed decision latency was below 0.27 seconds; no error or draw
  occurred in the submitted panel.

Public refresh:
- No newer independently score-bound archive was available after excluding
  the project's own public snapshots. A newer external Grimmsnarl package was
  noted for later byte-level review, but was not used without local identity
  and resolver verification.

Result:
- Kaggle accepted the package as submission `55454375` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline to 703.6.
- Score checkpoint: `2026-08-12 09:20 UTC`.
