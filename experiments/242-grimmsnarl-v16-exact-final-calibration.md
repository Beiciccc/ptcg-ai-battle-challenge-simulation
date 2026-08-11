# 242 Grimmsnarl v16 Exact Final Calibration

Date: 2026-08-11 UTC

Local generated package (not committed):
`artifacts/submissions/s239-grimmsnarl-v16-refresh.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: exact current-runtime final calibration

Kaggle submission: `55421330`

Public score: 736.9

Status: complete

Sources:
- [Grimmsnarl EX Damage Transfer Control](https://www.kaggle.com/code/tetsutani/grimmsnarl-ex-damage-transfer-control)
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-tested the exact Grimmsnarl v16 package against current exact Sol and
  Archaludon anchors using a fresh 16-game fixed panel.
- Grimmsnarl completed 6-2 against each anchor, passing 12-4 overall with
  balanced seats and no faults.
- The candidate was submitted as the fifth and final official row in the
  requested cycle.

Public refresh:
- No new external Code, Discussion, rules, evaluation, data, or runtime
  change established a distinct actionable candidate before the panel was
  fixed.
- Older proposals without current archive-level identity were excluded.

Candidate screen:
- Grimmsnarl archive SHA-256: `04f9779b77d17417570189d06a1b7ff5b0016797639a2a45f4b53bc02e945712`.
- Sol archive SHA-256: `78dde4d68910a7c841a4c989a7e39fe8ae4ec15b0ba278f28b7ba43cdec5476b`.
- Archaludon archive SHA-256: `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`.
- The panel used seeds `2026081166` through `2026081181`, alternating the
  candidate seat on even and odd seeds.
- Grimmsnarl completed 6-2 against Sol and 6-2 against Archaludon, with no
  errors or draws. The maximum observed decision latency was below one second.
- The fixed gate required at least 11-5 overall, at least 5-3 against each
  anchor, at least 2-2 from every anchor-seat cell, and at least 5-3 from each
  candidate seat overall. Grimmsnarl passed every gate.

Validation:
- The exact archive passed the required entrypoint, 60-card deck, current
  Linux runtime, safe-member, duplicate-member, and link checks.
- Main SHA-256: `c61e540bcb45aa2e8184ae912e7e17efaa900dba3df4536468da41899b09dcd8`.
- Deck SHA-256: `92b92bac9f9163ecff933b3dc39294d2cc154c8684f3c8497877661419ebc59d`.
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`.
- Archive SHA-256: `04f9779b77d17417570189d06a1b7ff5b0016797639a2a45f4b53bc02e945712`.

Result:
- Kaggle accepted the package as submission `55421330` and marked it
  complete. This was the fifth and final new official row in the cycle.
- Public evaluation moved from the 600.0 initialization baseline to 736.9.
- Score checkpoint: `2026-08-11 02:53 UTC`.
