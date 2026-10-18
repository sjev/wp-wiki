# type: ignore
from invoke import task


@task
def venv(c):
    """Sync dependencies."""
    c.run("uv sync --all-groups")


@task
def format(c):
    """Format code."""
    c.run("uv run ruff format src tests")


@task
def lint(c):
    """Run linters."""
    c.run("uv run ruff check src tests")
    c.run("uv run ruff format --check src tests")
    c.run("uv run mypy src")


@task
def test(c):
    """Run tests with coverage."""
    c.run("uv run pytest --cov=src --cov-report=term-missing")


@task
def ci(c):
    """Run lint, tests and a strict docs build."""
    lint(c)
    test(c)
    build(c)
    cite(c)
    print("All checks passed!")


@task(help={"thread": "Thread ID (default: all known)", "refresh": "Re-fetch all pages"})
def scrape(c, thread="", refresh=False):
    """Fetch new forum pages, then rebuild data/posts/*.jsonl."""
    flag = " --refresh" if refresh else ""
    c.run(f"uv run wp-wiki fetch {thread}{flag}", pty=True)
    c.run(f"uv run wp-wiki parse {thread}")


@task
def stats(c):
    """Summarize scraped posts into data/stats.md."""
    c.run("uv run wp-wiki stats")


@task(help={"topic": "Dossier name or TOPICS key", "pattern": "Regex", "n": "Number of posts"})
def dossier(c, topic, pattern="", n=40):
    """Dump the top posts for one topic into data/dossiers/<topic>.md."""
    flag = f" --pattern '{pattern}'" if pattern else ""
    c.run(f"uv run wp-wiki dossier {topic}{flag} --n {n}")


@task
def cite(c):
    """Check that source links in docs/ match post author and date."""
    c.run("uv run wp-wiki cite")


@task
def serve(c):
    """Serve docs locally with live reload."""
    c.run("uv run mkdocs serve", pty=True)


@task
def build(c):
    """Build docs; fail on warnings such as broken links."""
    c.run("uv run mkdocs build --strict")


@task
def clean(c):
    """Preview files to delete (safe mode). Keeps scraped data/."""
    c.run("git clean -nfdx -e data")
    if input("Delete? [y/N] ").lower() == "y":
        c.run("git clean -fdx -e data")
