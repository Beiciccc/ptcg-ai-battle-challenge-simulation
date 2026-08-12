# 244 Grimmsnarl Damage-Transfer Control

Date: 2026-08-12 UTC

Local generated package (not committed):
`artifacts/submissions/s244-grimmsnarl-ex-damage-transfer-control-exact.tar.gz`

Kaggle submission: `55454687`

Public score: 524.6

Status: complete

Sources:
- [Grimmsnarl EX Damage Transfer Control](https://www.kaggle.com/code/tetsutani/grimmsnarl-ex-damage-transfer-control)
- [Search-Alakazam strategy](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Tomato Archaludon](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Downloaded the completed external Code output and verified its exact
  archive, strategy, deck, and current runtime bytes before testing.
- Grimmsnarl completed 5-3 against Search-Alakazam and 6-2 against Tomato
  Archaludon, passing 11-5 overall with no errors or draws.
- The exact downloaded archive was submitted without repackaging changes.

Validation:
- Archive SHA-256:
  `04f9779b77d17417570189d06a1b7ff5b0016797639a2a45f4b53bc02e945712`.
- Main SHA-256:
  `c61e540bcb45aa2e8184ae912e7e17efaa900dba3df4536468da41899b09dcd8`.
- Deck SHA-256:
  `92b92bac9f9163ecff933b3dc39294d2cc154c8684f3c8497877661419ebc59d`.
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`.
- The external archive contains 197 members, including embedded policy
  assets, a fixed 60-card deck, and the full runtime support files.
- The fixed panel used eight games per anchor with alternating candidate
  seats. All sixteen games reached terminal states on first execution;
  maximum observed decision latency stayed below 0.32 seconds.

Public refresh:
- The external Code output was the only new actionable distinct archive after
  excluding this project's own public snapshot. Discussion supplied current
  deck-validation and later-round information; no contract change was used.
- Public snapshot v107 initially encountered Kaggle's competition-source
  publication restriction. Removing the competition source metadata allowed
  the factual snapshot to publish as v107 and complete.

Result:
- Kaggle accepted the exact archive as submission `55454687` and marked it
  complete.
- Public evaluation moved from the 600.0 initialization baseline to 524.6.
- Score checkpoint: `2026-08-12 09:28 UTC`.
