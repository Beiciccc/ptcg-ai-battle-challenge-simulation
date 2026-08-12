# 176 Visible-Grim Belief Alakazam v18 Loader Error

Date: 2026-07-26 UTC

Local generated package (not committed):
`artifacts/submissions/s176-prvsiyan-visible-grim-belief-alakazam-v18-current-official-runtime.tar.gz`

Reproducibility: exact public Code output archive

Kaggle submission: `54996107`

Public score: n/a

Status: error

Sources:
- [Visible-Grim Belief Alakazam v18](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-visible-grim-belief-alakazam-v18)
- [Kaggle Environments agent loader](https://github.com/Kaggle/kaggle-environments/blob/8418fb28e8a826ca3edff9561cf8e7ba11559e69/kaggle_environments/agent.py)

Summary:
- Selected the public v18 strategy after current-runtime local comparisons
  supported its visible Team Rocket Energy response over the v19 extension.
- Preserved the public notebook's strategy, deck, runtime, and archive bytes.
- The official validation episode failed before a battle began because the
  loader bound to a helper instead of the intended wrapper.

Validation:
- Exact public Code archive SHA-256:
  `17c52e7cea62f36bc0bd79e104e064943e8d48daaf6f487d2bbf7a36694cc3e8`
- Clean 12-member archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Main SHA-256:
  `2049ef51dcd837d8f6f5426b9c78cb16cbbd1c74d36da9b3ebe3141cdf0a52f1`
- Deck SHA-256:
  `0598646548d081832ec311c15fdc369b32c6f5e63175b0cfd1904d21fd082451`
- Thirty-nine direct-engine games completed without runtime or action errors
- The candidate went 6-2 against Steel, 6-2 against Mega Lucario
  Prize-Pressure, 5-3 against Great Tusk Router, and 2-6 against Grimmsnarl
- Direct-engine validation recorded 1,125 search decisions, zero search
  failures, and a 0.389-second maximum decision latency

Failure analysis:
- Kaggle reported `Validation Episode failed.` for validation episode
  `88219620`.
- Both validation seats selected `_rocket_energy_hammer_scores` as the entry
  callable and raised `AttributeError` on the initial `select=None` phase.
- Kaggle selects the last callable in the executed module global dictionary.
  The final wrapper reused the existing name `agent`, which updated the old
  dictionary key without moving it after the later helper definitions.
- The entrypoint checker now rejects a final function name that was bound
  earlier, and rejects later top-level bindings that could displace it.

Result:
- The official row is recorded as an error with no public score.
- The next package uses a fresh final entrypoint name and must pass the actual
  Kaggle loader selection check before upload.
