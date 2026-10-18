# sift

A CLI tool that sifts through structured log files (JSON lines), filters by level, and prints matching entries. Cuts through the noise to find what broke.

## Install

For development:

```bash
uv sync
uv run python main.py test.log --level ERROR
```

## Usage

```bash
# Show only ERROR lines (default)
python main.py test.log

# Filter by level (case-insensitive)
python main.py test.log --level INFO
python main.py test.log -l warn

# See all options
python main.py --help
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

