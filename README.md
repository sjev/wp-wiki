# wp-wiki

Dutch heat pump wiki, built from Tweakers forum threads. Each claim links back to its source post.
First brand: Panasonic Aquarea with HeishaMon. Other brands can be added under `docs/<brand>/`.

## Setup

```bash
source ./init.sh   # installs uv if missing, syncs the environment
inv venv           # sync all dependency groups (dev + docs)
inv --list
```

## Workflow

| Task | Action |
|---|---|
| `inv scrape` | Fetch new pages to `data/raw/`, parse to `data/posts/<thread>.jsonl` |
| `inv scrape --thread 2178982 --refresh` | Re-fetch one thread completely |
| `inv ci` | Lint, tests, citation check |

The scraper waits 3 s or more between requests and accepts only the functional cookie consent.
`data/` is not in git. Rebuild it with `inv scrape`.

To add a thread, add it to `THREADS` in `src/wp_wiki/__init__.py` and to `docs/sources.md`.

See [CLAUDE.md](CLAUDE.md) for project rules and [Bijdragen](docs/contributing.md) for the citation format.
