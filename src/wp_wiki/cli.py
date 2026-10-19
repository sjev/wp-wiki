import json
import logging
import time
from pathlib import Path
from typing import Annotated

import typer

from wp_wiki import THREADS
from wp_wiki.cite import check as check_cites
from wp_wiki.dossier import dossier as make_dossier
from wp_wiki.fetch import Fetcher, cached_pages, fetch_thread
from wp_wiki.images import fetch_images
from wp_wiki.log import setup_logging
from wp_wiki.parse import Post, parse_page
from wp_wiki.read import show_post, show_replies
from wp_wiki.stats import TOPICS, load_posts, report

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


@app.command()
def dossier(
    topic: Annotated[str, typer.Argument(help="Output name; also a TOPICS key if no --pattern.")],
    pattern: Annotated[str | None, typer.Option(help="Regex; default: TOPICS[topic].")] = None,
    n: Annotated[int, typer.Option(help="Number of posts.")] = 40,
    chars: Annotated[int, typer.Option(help="Max characters per post.")] = 1200,
    data: DataDir = Path("data"),
) -> None:
    """Write the top matching posts for one topic to data/dossiers/<topic>.md."""
    rx = pattern or TOPICS.get(topic)
    if rx is None:
        raise typer.BadParameter(f"unknown topic {topic!r}; pass --pattern")
    out = data / "dossiers" / f"{topic}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(make_dossier(load_posts(data / "posts"), topic, rx, n, chars), encoding="utf-8")
    log.info("%s -> %s", topic, out)


PostIds = Annotated[list[int], typer.Argument(help="Post IDs.")]


@app.command()
def replies(
    ids: PostIds,
    n: Annotated[int, typer.Option(help="Max replies per post.")] = 6,
    chars: Annotated[int, typer.Option(help="Max characters per post.")] = 800,
    data: DataDir = Path("data"),
) -> None:
    """Print each post and the replies that quote it (quotes stripped)."""
    typer.echo(show_replies(load_posts(data / "posts"), ids, n, chars))


@app.command()
def post(
    post_id: Annotated[int, typer.Argument(help="Post ID.")],
    start: Annotated[str, typer.Option(help="Print from the last match of this text.")] = "",
    end: Annotated[str, typer.Option(help="Stop before this text.")] = "",
    chars: Annotated[int, typer.Option(help="Max characters.")] = 20000,
    data: DataDir = Path("data"),
) -> None:
    """Print one full post, or one chapter of it (for the topic-start FAQ posts)."""
    by_id = {p["id"]: p for p in load_posts(data / "posts")}
    if post_id not in by_id:
        raise typer.BadParameter(f"post {post_id} not found")
    typer.echo(show_post(by_id[post_id], start, end, chars))


@app.command()
def images(ids: PostIds, data: DataDir = Path("data")) -> None:
    """Download the images of these posts into data/images/ and print the file paths."""
    by_id = {p["id"]: p for p in load_posts(data / "posts")}
    fetcher = Fetcher()
    for pid in ids:
        if pid not in by_id:
            raise typer.BadParameter(f"post {pid} not found")
        for path in fetch_images(fetcher, by_id[pid], data / "images"):
            typer.echo(path)


@app.command()
def cite(
    docs: Annotated[Path, typer.Argument()] = Path("docs"), data: DataDir = Path("data")
) -> None:
    """Verify that every source link in docs/ matches a post's author and date."""
    errors = check_cites(docs, load_posts(data / "posts"))
    for e in errors:
        log.error(e)
    log.info("%d citation errors", len(errors))
    raise typer.Exit(1 if errors else 0)
