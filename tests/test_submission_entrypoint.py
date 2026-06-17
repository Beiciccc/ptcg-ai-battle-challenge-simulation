from pathlib import Path
import subprocess


def test_submission_entrypoint_check() -> None:
    result = subprocess.run(
        ["python", "tools/check_submission_entrypoint.py", "submission/main.py"],
        cwd=Path(__file__).resolve().parents[1],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
