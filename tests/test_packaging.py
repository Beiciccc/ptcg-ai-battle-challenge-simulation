from pathlib import Path
from zipfile import ZipFile

from ptcg_battle.packaging import build_submission_zip


def test_build_submission_zip(tmp_path: Path) -> None:
    source = tmp_path / "submission"
    source.mkdir()
    (source / "main.py").write_text("def agent(obs):\n    return []\n")
    (source / "deck.csv").write_text("1\n")

    output = tmp_path / "out.zip"
    package = build_submission_zip(source, output, require_support_files=False)

    assert package.path == output
    assert package.file_count == 2
    with ZipFile(output) as archive:
        assert sorted(archive.namelist()) == ["deck.csv", "main.py"]
