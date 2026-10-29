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

- Workflow: `wp-wiki fetch` (HTTP → raw HTML → JSONL), `wp-wiki llm-update` (new posts → `docs/`),
  human reviews `git diff`, `wp-wiki check`.
- `last-post.txt` (in git): ID of the newest post already merged into `docs/`.
- Raw data never goes in `docs/`. Curated pages never go in `data/`.
- Known threads: `THREADS` in `src/wp_wiki/__init__.py` (thread ID → brand, title). A post's brand follows from its thread.
- Post record: `Post` in `src/wp_wiki/parse.py`. `url` is the post permalink; use it for citations.
- The scraper is source-specific (GoT), not brand-specific. A new forum gets its own module.

## Scraping rules

- Fetch only `/forum/list_messages/<thread>/<page>` (allowed in robots.txt). Pages are 0-based.
- Keep the default delay (3 s + jitter). Do not run fetches in parallel.
- Fetch is incremental: it re-fetches the newest cached page and continues.
- If the HTML layout changes, verify the new markup on a saved page before you change selectors.
- Do not commit `data/`. Forum content is copyrighted; the wiki quotes and summarizes only.

## Research tools

All print Markdown and read `data/posts/*.jsonl`. Quoted lines (`> `) are stripped.
`[afbeelding]` marks a user image. Images are not downloaded; ignore them.

| Command | Use |
|---|---|
| `uv run wp-wiki dossier <topic> '<regex>' [--n 40] [--chars 1200]` | Top posts for a topic → `data/dossiers/<topic>.md`. Mostly questions. |
| `uv run wp-wiki replies <id> [<id> …] [--n 6] [--chars 800]` | Post + the replies that quote it. This is where the answers are. |
| `uv run wp-wiki post <id> [--start '<text>'] [--end '<text>'] [--chars N]` | Full post or one chapter of it. |
| `uv run wp-wiki check [docs]` | Check front matter, tags, relative links and source links (author, date). |

Topic-start FAQs (curated, ~53k chars): `74751460` (thread #2) and `65288280` (thread #1).
`wp-wiki post 74751460 --chars 2500` prints the chapter list; `--start` takes a chapter title.

## Writing a page

1. Read the FAQ chapter on the topic, if there is one.
2. `dossier` with a narrow regex. Pick 10–20 relevant question posts.
3. `replies` on those IDs. Extract rules, values, causes, steps. Note who disagrees.
4. Check every value against the full post text before you use it.
5. Write the page. Reference examples: `docs/general/heating-curve.md`, `docs/panasonic/troubleshooting.md`.
6. Link only to pages that exist. `uv run wp-wiki check` must report 0 errors.
7. Panasonic facts found while writing a general page: add them to `wip/panasonic-findings.md`.

## Updating the wiki

`wp-wiki llm-update` runs this section headless. It writes the posts after `last-post.txt` to
`data/new-posts.md`: oldest first, quotes stripped, short posts left out. `Quotes:` lists the
IDs a post replies to.

1. Read `data/new-posts.md` in full.
2. Skip chatter and questions without an answer. Keep new rules, values, causes, fixes and disagreements.
3. Need context? `replies <id>` or `post <id>` on the quoted IDs. Check each value in the full post.
4. Add each fact to the page that fits (see Taxonomy). Change existing text when a new post
   corrects or extends it. A new page only when the taxonomy lists it.
5. Add a `## Bronnen` line for each post you use.
6. `uv run wp-wiki check` must report 0 errors.
7. Do not commit. Do not edit `last-post.txt`. End with a short list: page → what changed.

## Python

- Python 3.12, strict mypy, ruff. Run `./ci.sh` before you commit.
- Max 150 lines per file. Flat modules. No new dependencies without a reason.
- Tests use small hand-made fixtures in `tests/fixtures/`, never full forum pages.

## Languages

- Wiki pages and page titles: **Dutch**. Short sentences, active voice, plain words
  (ASD-STE100 principles; its English word list does not apply).
- Code, comments, `CLAUDE.md`, README, commits: English.
- Folder and file names (URLs): English, e.g. `general/heating-curve.md`.
- Keep MQTT topics, parameter names and error codes verbatim (`SetZ1HeatRequestTemperature`, `H62`).

## Docs and citations

- Pages hold extracted knowledge in our own words: rules, values, causes, steps.
  Do not retell posts ("user X wrote …"). Merge what many posts say into one statement.
- Sources go in a `## Bronnen` list at the end of the page, or at the end of each `##` section
  on long pages. No per-sentence footnotes. One line per post:
  `- [<author>, <YYYY-MM-DD>](https://gathering.tweakers.net/forum/list_message/<id>#<id>): <what it supports>`
- Write a page from its dossier: `uv run wp-wiki dossier <topic> '<regex>'` → `data/dossiers/<topic>.md`.
  Read the full post in `data/posts/*.jsonl` when the excerpt is not enough.
- Do not invent settings, MQTT topics, wiring, or values. If no post supports a claim, leave it out.
- Placement: valid for any heat pump → `general/`; depends on brand, model or firmware → `<brand>/`.
  Do not copy general content into brand sections; link to it.
- For HeishaMon topics and rules, also link the upstream [HeishaMon docs](https://github.com/Egyras/HeishaMon).
- State model, firmware, and date when a claim depends on them. Show disagreements under a
  bold lead-in paragraph `**Meningen verschillen.**`; do not pick a side silently.
- Safety-related content (electrical, refrigerant, legionella) gets a bold lead-in paragraph
  `**Let op: <title>.**`. The text follows as normal paragraphs or a list, without indent.
- Never copy, hotlink or embed forum images. Draw own visuals in Mermaid; a human adds other images by hand.
  Existing Bronnen lines may carry an image kind: `(foto)`, `(schema)`, `(grafiek)`, `(screenshot)`. Keep it.
- Visuals: Mermaid only. Each value and node comes from the page or a cited post. Dutch labels,
  max ~12 nodes. `xychart-beta` has no legend: name each line by colour below the chart.
  Never draw electrical wiring unless a cited image shows that exact wiring.
- Format: plain CommonMark, tables and fenced `mermaid`. No site-specific syntax (no admonitions).
- Front matter `title:` and `weight:` (10, 20, …; order within the folder). No `# H1` in the body.
- A folder is a section. Its `_index.md` holds the section `title` and `weight`.
- `./ci.sh` runs lint, test and check. It must pass.

## Tags

- Front matter `tags: [...]`. Only tags from `TAGS` in `src/wp_wiki/__init__.py`:
  model series (`J-serie` `K-serie` `L-serie` `M-serie` `T-CAP` `R290`),
  control (`HeishaMon` `Home Assistant` `Cloud`),
  type (`Veiligheid` `Installatie` `Optimalisatie` `Storing`).
- A model tag needs a cited source that names that model. No tags for topics that have their own page.

## Taxonomy

```
general/    sizing, heating-curve, hydraulics, buffer-tank, cycling, defrost,
            hot-water, legionella, cop, cooling, noise
panasonic/  index (models) · settings · troubleshooting
            hardware/ (installation, wiring, backup-heater, sensors)
            control/ (cloud, heishamon, home-assistant)
```
Create a page only when it has cited content. Out of scope: subsidies, energy prices.
