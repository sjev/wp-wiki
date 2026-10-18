"""Print single posts and their replies, so a writer reads answers without loading the whole corpus."""

from wp_wiki.parse import Post
from wp_wiki.stats import _strip_quotes


def _flat(text: str, max_chars: int) -> str:
    out = " ".join(_strip_quotes(text).split())
    return out if len(out) <= max_chars else out[:max_chars] + " …"


def _head(p: Post) -> str:
    return f"{p['id']} · {p['author']} · {p['date'][:10]} · {p['url']}"


def section(text: str, start: str = "", end: str = "") -> str:
    """Slice from the last `start` match (FAQ posts list headings twice: TOC, then body) to `end`."""
    i = text.rfind(start) if start else 0
    if i < 0:
        return ""
    j = text.find(end, i + len(start)) if end else -1
    return text[i:j] if j >= 0 else text[i:]


def show_post(p: Post, start: str = "", end: str = "", max_chars: int = 20000) -> str:
    body = section(p["text"], start, end)
    return f"## {_head(p)}\n\n{body[:max_chars]}\n"


def show_replies(posts: list[Post], ids: list[int], n: int = 6, max_chars: int = 800) -> str:
    by_id = {p["id"]: p for p in posts}
    quoted_by: dict[int, list[Post]] = {}
    for p in posts:
        for q in set(p["quotes"]):
            quoted_by.setdefault(q, []).append(p)
    out: list[str] = []
    for pid in ids:
        target = by_id.get(pid)
        if target is None:
            out.append(f"## {pid}: not found\n")
            continue
        out += [f"## {_head(target)}", "", _flat(target["text"], max_chars), ""]
        for r in quoted_by.get(pid, [])[:n]:
            out.append(f"- {_head(r)}\n  {_flat(r['text'], max_chars)}")
        out.append("")
    return "\n".join(out)
