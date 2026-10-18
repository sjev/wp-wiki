# CLAUDE.md

Dutch heat pump wiki (`wp-wiki`), built from Tweakers (GoT) forum threads. First brand: Panasonic Aquarea + HeishaMon.

## Architecture

```
src/wp_wiki/                        scraper + parser (Python)
data/raw/<thread>/<page:04d>.html   raw page cache                 (gitignored)
data/posts/<thread>.jsonl           one post per line              (gitignored)
docs/general/                       knowledge valid for any heat pump
docs/<brand>/                       brand-, model- or firmware-specific knowledge
```

- Pipeline: `inv scrape` = `wp-wiki fetch` (HTTP → raw HTML) then `wp-wiki parse` (raw HTML → JSONL).
- Raw data never goes in `docs/`. Curated pages never go in `data/`.
- Known threads: `THREADS` in `src/wp_wiki/__init__.py` (thread ID → brand, title). A post's brand follows from its thread.
- Post record: `Post` in `src/wp_wiki/parse.py`. `url` is the post permalink; use it for citations.
- The scraper is source-specific (GoT), not brand-specific. A new forum gets its own module.

## Scraping rules

- Fetch only `/forum/list_messages/<thread>/<page>` (allowed in robots.txt). Pages are 0-based.
- Keep the default delay (3 s + jitter). Do not run fetches in parallel.
- Fetch is incremental: it re-fetches the newest cached page and continues. Use `--refresh` only when needed.
- If the HTML layout changes, verify the new markup on a saved page before you change selectors.
- Do not commit `data/`. Forum content is copyrighted; the wiki quotes and summarizes only.

## Python

- Python 3.12, strict mypy, ruff. Run `inv lint` and `inv test` before you commit.
- Max 150 lines per file. Flat modules. No new dependencies without a reason.
- Tests use small hand-made fixtures in `tests/fixtures/`, never full forum pages.

## Languages

- Wiki pages, nav labels, site texts: **Dutch**. Short sentences, active voice, plain words
  (ASD-STE100 principles; its English word list does not apply).
- Code, comments, `CLAUDE.md`, README, commits: English.
- Folder and file names (URLs): English, e.g. `general/heating-curve.md`.
- Keep MQTT topics, parameter names and error codes verbatim (`SetZ1HeatRequestTemperature`, `H62`).

## Docs and citations

- Every technical claim needs a footnote to its source post:
  `[^<post-id>]: [<author>, <YYYY-MM-DD>](https://gathering.tweakers.net/forum/list_message/<id>#<id>)`
- Read the full post text in `data/posts/*.jsonl` before you cite it. Do not cite from memory.
- Do not invent settings, MQTT topics, wiring, or values. If no post supports a claim, leave it out.
- Placement: valid for any heat pump → `general/`; depends on brand, model or firmware → `<brand>/`.
  Do not copy general content into brand sections; link to it.
- For HeishaMon topics and rules, also link the upstream [HeishaMon docs](https://github.com/Egyras/HeishaMon).
- State model, firmware, and date when a claim depends on them. Show disagreements; do not pick a side silently.
- Safety-related content (electrical, refrigerant, legionella) gets a `!!! warning` admonition.
- Add each new page to `nav` in `mkdocs.yml`. `inv build` runs `--strict` and must pass.

## Planned taxonomy

```
general/      heating curve, hydraulics, buffer tank, legionella, COP, sizing
panasonic/    hardware/ (models, installation, wiring) · heishamon/ (setup, MQTT, rules)
              home-assistant/ · troubleshooting/ (error codes)
```
Create a section only when it has cited content. Add a brand folder only with its first sourced page.
