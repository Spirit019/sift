# sift

A CLI tool that sifts through structured log files (JSON lines), filters by level, and prints matching entries. Cuts through the noise to find what broke.

## Install

For development:

```bash
uv sync
uv run sift test.log --level ERROR
```

Or install globally:

```bash
uv build
pipx install ./dist/*.whl --force
sift /path/to/app.log --level ERROR
```

## Usage

```bash
# Show only ERROR lines (default)
sift test.log

# Filter by level (case-insensitive)
sift test.log --level INFO
sift test.log -l warn

# See all options
sift --help
```

## Log format

Each line in the log file must be JSON:

```json
{"timestamp": "2024-01-15 10:30:45", "level": "ERROR", "message": "DB failed", "service": "api"}
```

Broken lines are skipped silently. The `service` field is optional.

## What I learned

- **typer**: `Argument` vs `Option`, short flags (`-l`), auto-generated `--help`
- **pydantic**: `BaseModel`, `model_validate_json`, skipping invalid lines with try/except
- **Case-insensitive filtering** with `.upper()` on both sides of the comparison
- **rich**: `Table`, `add_column`/`add_row`, `Console().print` for bordered output
- **Packaging**: `src/` layout, `[project.scripts]` entry points, `uv build` + `pipx install`
- **Testing**: `pytest` + `typer.testing.CliRunner` + `tmp_path` for isolated CLI tests

