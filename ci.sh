#!/usr/bin/env bash
# Every check that must pass before a commit. Fix formatting with: uv run ruff format src tests
set -euo pipefail
cd "$(dirname "$0")"
uv run ruff format --check src tests
uv run ruff check src tests
uv run mypy src
uv run pytest -q --cov=src --cov-report=term-missing
uv run wp-wiki check
echo "All checks passed."
