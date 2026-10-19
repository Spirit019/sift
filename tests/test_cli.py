from pathlib import Path

from typer.testing import CliRunner

from log_analyzer.cli import app

runner = CliRunner()


def _write_log(path: Path) -> None:
    path.write_text(
        '{"timestamp": "2024-01-15 10:30:45", "level": "ERROR", "message": "DB failed", "service": "api"}\n'
        '{"timestamp": "2024-01-15 10:31:02", "level": "INFO", "message": "User logged in", "service": "auth"}\n'
    )


def test_filter_by_level(tmp_path: Path) -> None:
    log_file = tmp_path / "test.log"
    _write_log(log_file)

    result = runner.invoke(app, [str(log_file), "--level", "ERROR"])

    assert result.exit_code == 0
    assert "DB failed" in result.output
    assert "User logged in" not in result.output


def test_broken_lines_are_skipped(tmp_path: Path) -> None:
    log_file = tmp_path / "test.log"
    _write_log(log_file)
    with log_file.open("a") as f:
        f.write("this is not json\n")

    result = runner.invoke(app, [str(log_file), "--level", "ERROR"])

    assert result.exit_code == 0
    assert "DB failed" in result.output
