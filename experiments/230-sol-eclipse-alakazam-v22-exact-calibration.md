# 230 Sol Eclipse Alakazam v22 Exact Calibration

Date: 2026-08-07 UTC

Local generated package (not committed):
`artifacts/submissions/s230-sol-eclipse-alakazam-v22-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiment 193

Kaggle submission: `55325658`

Public score: 790.8

Status: complete

Sources:
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Sol Eclipse Alakazam v22 archive as the third 2026-08-07
  calibration and a distinct complement to experiment 229 Steel.
- Preserved the published policy, 60-card deck, loader entrypoint, current
  runtime, and archive bytes.
- Required a new two-anchor panel under the official callable resolver before
  selecting the candidate.

Public refresh:
- A new Great Tusk / Crustle run was cancelled with exit code 137, no saved
  version, and zero bytes of output
- Its subsequent run was still executing with zero bytes of output and no
  score-bound submission at the decision checkpoint
- The latest published PPO candidate remained unchanged and still lacked its
  claimed trained checkpoint
- Recent Discussion, Rules, Evaluation, Data Description, competition data,
  and CABT runtime checks produced no verified update

Candidate screen:
- The fixed panel used seeds `2026080780` through `2026080795`, with Sol in
  seat zero on even seeds and seat one on odd seeds
- Sol completed 6-2 against Archaludon and 5-3 against Steel, for 11-5 overall
- Against Archaludon, Sol went 4-0 from seat zero and 2-2 from seat one
- Against Steel, Sol went 3-1 from seat zero and 2-2 from seat one
- Across both anchors, Sol went 7-1 from seat zero and 4-4 from seat one;
  winning seats split 9-7
- All sixteen games completed without errors, ties, timeouts, invalid actions,
  or retries
- Maximum Sol decision latency was 0.145 seconds, and the global maximum was
  also 0.145 seconds
- The fixed gate required at least 11-5 overall, at least 5-3 against each
  anchor, at least 2-2 from each candidate seat within each anchor, zero
  faults, and sub-second decisions; every condition passed

Validation:
- Archive SHA-256 matched experiment 193 exactly
- The official resolver selected key `codex_sol_eclipse_alakazam_v22`
- Resolver keys for the Archaludon and Steel anchors were
  `_v28_original_agent` and `agent`
- Loader-selected initialization returned each exact submitted 60-card deck
- Clean root archive with `main.py`, `deck.csv`, published metadata, and the
  full current runtime
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Main SHA-256:
  `f31eba2e819ee2b3d46765b4195ea7dab8f32d0b5d09cafd39b3823661f6b5aa`
- Deck SHA-256:
  `8eccc69c3bf7d499f38c6116c33c5fac837050bf0ec71a5a1883f0f20f41ddbc`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `78dde4d68910a7c841a4c989a7e39fe8ae4ec15b0ba278f28b7ba43cdec5476b`

Result:
- Kaggle accepted the package as submission `55325658` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before
  moving through 716.6, 814.0, and 797.2 to 790.8.
- At this checkpoint, the two byte-identical official rows read 592.8 and
  790.8.
- The latest two submissions preserve Steel and Sol Eclipse Alakazam as
  distinct complementary strategy families.
- Score checkpoint: `2026-08-07 18:02 UTC`.
