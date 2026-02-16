---
globs: "**/*.py"
paths:
  - "**/*.py"
  - "requirements.txt"
  - "pyproject.toml"
  - "Makefile"
description: "Python 3.13 environment and coding conventions"
alwaysApply: false
---

# Python 3.13 Environment

## Version
- Enforce **Python 3.13** for this project
- `.python-version` and `pyproject.toml` pin to 3.13 (`>=3.13,<3.14`)

## Execution
- Always use the venv Python: `.venv/bin/python`
- Run scripts via `make` targets or `.venv/bin/python scripts/...`

## Dependencies
- Pin dependencies to exact versions in `requirements.txt`
- Verify Python 3.13 compatibility before upgrading any package

## Shebangs
- Use `#!/usr/bin/env python3` for executable Python scripts
