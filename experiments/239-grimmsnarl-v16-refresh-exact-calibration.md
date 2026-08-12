# 239 Grimmsnarl v16 Refresh Exact Calibration

Date: 2026-08-11 UTC

Local generated package (not committed):
`artifacts/submissions/s239-grimmsnarl-v16-refresh.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: exact public Code output refreshed on 2026-08-11

Kaggle submission: `55420825`

Public score: 510.4

Status: complete

Sources:
- [Grimmsnarl EX Damage Transfer Control](https://www.kaggle.com/code/tetsutani/grimmsnarl-ex-damage-transfer-control)
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Tested a newly completed public Grimmsnarl archive that was byte-distinct
  from the previously screened Grimmsnarl package and had no earlier official
  score binding.
- Preserved the public policy, 60-card deck, current runtime, and archive
  bytes exactly as downloaded.
- The candidate passed the fixed local panel and was submitted as the new
  strategy family for this cycle.

Public refresh:
- The new public Code run completed with a packaged top-level submission,
  fixed deck, and full runtime.
- Other Code outputs did not provide a newer distinct archive with an
  official score binding.
- Discussion, Rules, Evaluation, competition data, and the CABT runtime
  supplied no material contract change before the panel was fixed.

Candidate screen:
- Grimmsnarl archive SHA-256 was
  `04f9779b77d17417570189d06a1b7ff5b0016797639a2a45f4b53bc02e945712`.
- The fixed panel used seeds `2026081116` through `2026081131`, with
  Grimmsnarl in seat zero on even seeds and seat one on odd seeds.
- Grimmsnarl completed 6-2 against Sol and 8-0 against Archaludon, for 14-2
  overall.
- Against Sol, Grimmsnarl went 3-1 from seat zero and 3-1 from seat one.
- Against Archaludon, Grimmsnarl went 4-0 from seat zero and 4-0 from seat one.
- Across both anchors, Grimmsnarl went 7-1 from seat zero and 7-1 from seat
  one.
- All sixteen games completed on their first execution without errors, ties,
  timeouts, invalid actions, random fallbacks, or retries.
- Maximum Grimmsnarl decision latency was 0.009 seconds, and the global
  maximum was 0.445 seconds.
- The fixed gate required at least 11-5 overall, at least 5-3 against each
  anchor, at least 2-2 from every anchor and candidate-seat cell, and at least
  5-3 from each candidate seat overall.
- Grimmsnarl passed every declared gate and was selected for submission.

Validation:
- Official resolver key was `agent` and loader-selected initialization
  returned the exact submitted 60-card deck.
- Clean root archive with `main.py`, `deck.csv`, published helper files, and
  the full current runtime.
- No duplicate members, links, unsafe paths, or nested archive root.
- Main SHA-256:
  `c61e540bcb45aa2e8184ae912e7e17efaa900dba3df4536468da41899b09dcd8`
- Deck SHA-256:
  `92b92bac9f9163ecff933b3dc39294d2cc154c8684f3c8497877661419ebc59d`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `04f9779b77d17417570189d06a1b7ff5b0016797639a2a45f4b53bc02e945712`

Result:
- Kaggle accepted the package as submission `55420825` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 510.4.
- Score checkpoint: `2026-08-11 02:22 UTC`.
