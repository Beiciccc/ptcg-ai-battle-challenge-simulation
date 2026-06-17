.PHONY: download-light check test package clean

download-light:
	python tools/download_assets.py --light

check:
	python tools/check_deck.py submission/deck.csv
	python tools/check_submission_entrypoint.py

test:
	pytest -q

package:
	python tools/package_submission.py --name baseline

clean:
	rm -rf artifacts/submissions/*.zip artifacts/reports/*
