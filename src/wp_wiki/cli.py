import json
import logging
import subprocess
import time
from pathlib import Path
from typing import Annotated

import typer

from wp_wiki import THREADS
from wp_wiki.check import check as check_pages
from wp_wiki.cite import check as check_cites
from wp_wiki.dossier import dossier as make_dossier
from wp_wiki.fetch import Fetcher, cached_pages, fetch_thread
from wp_wiki.log import log_errors, setup_logging
from wp_wiki.parse import Post, load_posts, parse_page
from wp_wiki.read import new_posts, show_post, show_replies

log = logging.getLogger(__name__)
app = typer.Typer(no_args_is_help=True, add_completion=False)

DATA = Path("data")
POSTS = DATA / "posts"
LAST_POST = Path("last-post.txt")
PROMPT = "Read CLAUDE.md, then follow its section 'Updating the wiki'. New posts: {path}"
# The prompt must come before --allowedTools, which takes all remaining arguments.
CLAUDE_FLAGS = ["--permission-mode", "acceptEdits", "--allowedTools", "Bash(uv run wp-wiki:*)"]


@app.callback()
def main() -> None:
    """Heat pump wiki. Workflow: fetch, llm-update, review `git diff`, check."""
    setup_logging(DATA / "logs" / "wp-wiki.log")


def _parse(thread_id: int) -> None:
    thread_dir = DATA / "raw" / str(thread_id)
    posts: dict[int, Post] = {}
    for page in cached_pages(thread_dir):
        html = (thread_dir / f"{page:04d}.html").read_text(encoding="utf-8")
        posts.update((p["id"], p) for p in parse_page(html, thread_id, page))
    POSTS.mkdir(parents=True, exist_ok=True)
    out = POSTS / f"{thread_id}.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for post in sorted(posts.values(), key=lambda p: p["id"]):
            f.write(json.dumps(post, ensure_ascii=False) + "\n")
    log.info("%d: %d posts -> %s", thread_id, len(posts), out)


@app.command()
def fetch() -> None:
    """Fetch new forum pages, then rebuild data/posts/*.jsonl."""
    fetcher = Fetcher()
    for thread_id in THREADS:
        start = time.monotonic()
        n = fetch_thread(fetcher, thread_id, DATA / "raw")
        log.info("%d: fetched %d pages in %.0fs", thread_id, n, time.monotonic() - start)
        _parse(thread_id)


@app.command("llm-update")
def llm_update() -> None:
    """Let Claude Code merge the posts after last-post.txt into docs/."""
    posts = load_posts(POSTS)
    after = int(LAST_POST.read_text())
    latest = max(p["id"] for p in posts)
    if latest <= after:
        log.info("no posts after %d; run fetch first", after)
        return
    out = DATA / "new-posts.md"
    out.write_text(new_posts(posts, after), encoding="utf-8")
    log.info("posts %d..%d -> %s; Claude is working", after, latest, out)
    cmd = ["claude", "-p", PROMPT.format(path=out), *CLAUDE_FLAGS]
    if subprocess.run(cmd, check=False).returncode:
        raise typer.Exit(1)
    LAST_POST.write_text(f"{latest}\n")
    log.info("done; review with git diff, then run check")


@app.command()
def check(docs: Annotated[Path, typer.Argument()] = Path("docs")) -> None:
    """Check docs/: front matter, tags, relative links and source links."""
    errors = check_pages(docs) + check_cites(docs, load_posts(POSTS))
    raise typer.Exit(log_errors(errors, "docs"))


# Research commands for the agent. Hidden from --help; documented in CLAUDE.md.

PostIds = Annotated[list[int], typer.Argument(help="Post IDs.")]
Chars = Annotated[int, typer.Option(help="Max characters per post.")]


@app.command(hidden=True)
def dossier(
    topic: Annotated[str, typer.Argument(help="Output name.")],
    pattern: Annotated[str, typer.Argument(help="Regex.")],
    n: Annotated[int, typer.Option(help="Number of posts.")] = 40,
    chars: Chars = 1200,
) -> None:
    """Write the top matching posts for one topic to data/dossiers/<topic>.md."""
    out = DATA / "dossiers" / f"{topic}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(make_dossier(load_posts(POSTS), topic, pattern, n, chars), encoding="utf-8")
    log.info("%s -> %s", topic, out)


@app.command(hidden=True)
def replies(
    ids: PostIds,
    n: Annotated[int, typer.Option(help="Max replies per post.")] = 6,
    chars: Chars = 800,
) -> None:
    """Print each post and the replies that quote it (quotes stripped)."""
    typer.echo(show_replies(load_posts(POSTS), ids, n, chars))


@app.command(hidden=True)
def post(
    post_id: Annotated[int, typer.Argument(help="Post ID.")],
    start: Annotated[str, typer.Option(help="Print from the last match of this text.")] = "",
    end: Annotated[str, typer.Option(help="Stop before this text.")] = "",
    chars: Chars = 20000,
) -> None:
    """Print one full post, or one chapter of it (for the topic-start FAQ posts)."""
    by_id = {p["id"]: p for p in load_posts(POSTS)}
    if post_id not in by_id:
        raise typer.BadParameter(f"post {post_id} not found")
    typer.echo(show_post(by_id[post_id], start, end, chars))
