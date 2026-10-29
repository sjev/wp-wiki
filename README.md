# wp-wiki

Dutch heat pump wiki, built from Tweakers forum threads. Every claim links to its source post.
First brand: Panasonic Aquarea + HeishaMon. Read the wiki: [docs/](docs/_index.md).

## Workflow

Needs [uv](https://docs.astral.sh/uv/) and [Claude Code](https://claude.com/claude-code).

```bash
uv run wp-wiki fetch        # 1. get the latest forum posts into data/
uv run wp-wiki llm-update   # 2. Claude merges posts newer than last-post.txt into docs/
git diff                    # 3. review; discard what you do not want
uv run wp-wiki check        # 4. check pages, links and source links
```

Then commit `docs/` and `last-post.txt` together.

## Layout

| Path | Holds | In git |
|---|---|---|
| `docs/` | Wiki pages (Dutch) | yes |
| `last-post.txt` | Newest post already in `docs/` | yes |
| `CLAUDE.md` | Rules for writing pages; read by Claude | yes |
| `src/wp_wiki/` | Scraper and tools | yes |
| `data/` | Forum pages and posts (copyright; rebuild with `fetch`) | no |

Add a thread: add it to `THREADS` in `src/wp_wiki/__init__.py` and to `docs/sources.md`.
Code changes: run `./ci.sh` (lint, tests, check).
