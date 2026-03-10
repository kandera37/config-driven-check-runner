# Config-Driven Check Runner

## Why I built this

I wanted to build a small config-driven automation tool inspired by infrastructure and code-quality workflows.
This project reads a YAML configuration file, prepares scan jobs, and runs my Git secret scanner automatically.

## What it does

- Loads scan jobs from a YAML config file
- Iterates through configured instances
- Runs a secret scanning tool with parameters from config
- Saves scan results to the specified output file

## Project structure

- `src/main.py` — CLI entry point
- `src/config_loader.py` — YAML config loading
- `src/runner.py` — scan job execution logic
- `config.yaml` — example configuration file

## Example config

```yaml
instances:
  - name: local-secret-scan
    repo_path: /Users/kveit/git-secret-clean
    check: secret_scan
    output_file: report.json
    commits: 5
```

## Environment variables

Create a `.env` file in the project root:

```dotenv
SECRET_SCANNER_PATH=/absolute/path/to/git-secret-clean/main.py
```

## How to run

```bash
python3 src/main.py --config config.yaml
```

## Requirements
- Python 3.10+
- PyYAML
- python-dotenv (if .env loading is used)

## Notes

Right now the project supports one check type:
- secret_scan

Future improvements may include:
- support for multiple check types
- better validation of config structure
- richer status reporting