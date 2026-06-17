# Submission Notes

Submission packages are built from `submission/`:

```bash
python tools/download_assets.py --light
python tools/check_deck.py submission/deck.csv
python tools/package_submission.py --name baseline
```

The package zip is written to `artifacts/submissions/`. Before uploading, check
that the archive contains `main.py`, `deck.csv`, and the `cg/` support files.

Submit a package with:

```bash
python tools/submit_package.py artifacts/submissions/baseline.zip --message "baseline"
```

Use `tools/list_recent_submissions.py` to review recent Kaggle submission rows.
