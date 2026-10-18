import json
import logging
import time
from pathlib import Path
from typing import Annotated

import typer

from wp_wiki import THREADS
from wp_wiki.fetch import Fetcher, cached_pages, fetch_thread
from wp_wiki.log import setup_logging
from wp_wiki.parse import Post, parse_page
from wp_wiki.stats import load_posts, report

log = logging.getLogger(__name__)
app = typer.Typer(no_args_is_help=True)

DataDir = Annotated[Path, typer.Option(help="Root of raw/ and posts/ data.")]
ThreadIds = Annotated[list[int] | None, typer.Argument(help="Thread IDs; default: all known.")]


@app.callback()
def main(
    verbose: bool = False,
    log_file: Annotated[Path, typer.Option(help="Debug log file.")] = Path("data/logs/wp-wiki.log"),
) -> None:
    """Heat pump wiki tooling."""
    setup_logging(verbose, log_file)


@app.command()
def fetch(
    threads: ThreadIds = None,
    data: DataDir = Path("data"),
    delay: Annotated[float, typer.Option(help="Seconds between requests.")] = 3.0,
    refresh: Annotated[bool, typer.Option(help="Re-fetch all pages, not only new ones.")] = False,
) -> None:
    """Download thread pages into data/raw/<thread>/<page>.html."""
    fetcher = Fetcher(delay=delay)
    for thread_id in threads or THREADS:
        start = time.monotonic()
        n = fetch_thread(fetcher, thread_id, data / "raw", refresh=refresh)
        log.info("%d: fetched %d pages in %.0fs", thread_id, n, time.monotonic() - start)


@app.command()
def parse(threads: ThreadIds = None, data: DataDir = Path("data")) -> None:
    """Parse cached pages into data/posts/<thread>.jsonl, one post per line, deduplicated by ID."""
    out_dir = data / "posts"
    out_dir.mkdir(parents=True, exist_ok=True)
    for thread_id in threads or THREADS:
        thread_dir = data / "raw" / str(thread_id)
        posts: dict[int, Post] = {}
        for page in cached_pages(thread_dir):
            html = (thread_dir / f"{page:04d}.html").read_text(encoding="utf-8")
            posts.update((p["id"], p) for p in parse_page(html, thread_id, page))
        out = out_dir / f"{thread_id}.jsonl"
        with out.open("w", encoding="utf-8") as f:
            for post in sorted(posts.values(), key=lambda p: p["id"]):
                f.write(json.dumps(post, ensure_ascii=False) + "\n")
        log.info("%d: %d posts -> %s", thread_id, len(posts), out)


@app.command()
def stats(data: DataDir = Path("data")) -> None:
    """Summarize data/posts/*.jsonl into data/stats.md."""
    posts = load_posts(data / "posts")
    out = data / "stats.md"
    out.write_text(report(posts), encoding="utf-8")
    log.info("%d posts -> %s", len(posts), out)
