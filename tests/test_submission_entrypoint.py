from pathlib import Path
import subprocess
import sys


def test_submission_entrypoint_check() -> None:
    result = subprocess.run(
        [sys.executable, "tools/check_submission_entrypoint.py", "submission/main.py"],
        cwd=Path(__file__).resolve().parents[1],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def run_entrypoint_check(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "tools/check_submission_entrypoint.py", str(path)],
        cwd=Path(__file__).resolve().parents[1],
        text=True,
        capture_output=True,
    )


def test_redefined_final_function_is_rejected(tmp_path: Path) -> None:
    source = tmp_path / "main.py"
    source.write_text(
        "def agent(obs):\n"
        "    return [0]\n"
        "\n"
        "def helper(obs):\n"
        "    return [0]\n"
        "\n"
        "def agent(obs):\n"
        "    return helper(obs)\n"
    )

    result = run_entrypoint_check(source)

    assert result.returncode == 1
    assert "final function name was bound earlier" in result.stdout


def test_fresh_final_function_name_is_accepted(tmp_path: Path) -> None:
    source = tmp_path / "main.py"
    source.write_text(
        "def agent(obs):\n"
        "    return [0]\n"
        "\n"
        "def submission_entrypoint(obs):\n"
        "    return agent(obs)\n"
    )

    result = run_entrypoint_check(source)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "loader-safe final function: submission_entrypoint" in result.stdout


def test_later_top_level_binding_is_rejected(tmp_path: Path) -> None:
    source = tmp_path / "main.py"
    source.write_text(
        "def submission_entrypoint(obs):\n"
        "    return [0]\n"
        "\n"
        "later_alias = submission_entrypoint\n"
    )

    result = run_entrypoint_check(source)

    assert result.returncode == 1
    assert "top-level names are bound after the final function" in result.stdout
