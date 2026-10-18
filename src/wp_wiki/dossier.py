"""Select the most relevant posts for one wiki topic, so a page is written from a short extract."""

import re
from collections import Counter

from wp_wiki.parse import Post
from wp_wiki.stats import _strip_quotes

MIN_CHARS = 150


def _excerpt(text: str, rx: re.Pattern[str], max_chars: int) -> str:
    """Matching paragraphs first, so long posts (e.g. the topic-start FAQ) shrink to the relevant part."""
    paras = [" ".join(p.split()) for p in re.split(r"\n\s*\n|\n", text) if p.strip()]
    hits = [p for p in paras if rx.search(p)] or paras
    out = " … ".join(hits)
    return out if len(out) <= max_chars else out[:max_chars] + " …"


def dossier(posts: list[Post], title: str, pattern: str, n: int = 40, max_chars: int = 1200) -> str:
    rx = re.compile(pattern, re.IGNORECASE)
    by_id = {p["id"]: p for p in posts}
    quoted = Counter(q for p in posts for q in set(p["quotes"]) if q in by_id)
    scored: list[tuple[int, Post, str]] = []
    for p in posts:
        text = _strip_quotes(p["text"])
        hits = len(rx.findall(text))
        if hits and len(text) >= MIN_CHARS:
            scored.append((min(hits, 10) + 3 * quoted[p["id"]], p, text))
    scored.sort(key=lambda s: -s[0])
    out = [f"# Dossier: {title}\n", f"Pattern `{pattern}`: {len(scored)} posts, top {n}.\n"]
    for score, p, text in scored[:n]:
        head = f"## {p['id']} · {p['author']} · {p['date'][:10]} · score {score}"
        out += [head, p["url"], "", _excerpt(text, rx, max_chars), ""]
    return "\n".join(out)
