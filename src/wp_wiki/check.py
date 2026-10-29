"""Check that every page in docs/ has title and weight, allowed tags, and working relative links."""

import re
from pathlib import Path

from wp_wiki import TAGS

LINK = re.compile(r"\]\(([^)\s]+)\)")
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)


def front_matter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n") or "\n---\n" not in text[3:]:
        return None
    head = text[4 : text.index("\n---\n", 3)]
    return dict(line.split(":", 1) for line in head.splitlines() if ":" in line)


def check_page(page: Path) -> list[str]:
    text = page.read_text(encoding="utf-8")
    meta = front_matter(text)
    if meta is None:
        return [f"{page}: no front matter"]
    errors = [f"{page}: no {key}" for key in ("title", "weight") if not meta.get(key, "").strip()]
    weight = meta.get("weight", "").strip()
    if weight and not weight.isdigit():
        errors.append(f"{page}: weight is not a number")
    tags = [t.strip() for t in meta.get("tags", "").strip().strip("[]").split(",")]
    errors += [f"{page}: unknown tag {t!r}" for t in tags if t and t not in TAGS]
    for target in LINK.findall(FENCE.sub("", text)):
        path = target.split("#")[0]
        if path and ":" not in path and not (page.parent / path).is_file():
            errors.append(f"{page}: broken link {target}")
    return errors


def check(docs: Path) -> list[str]:
    return [e for page in sorted(docs.rglob("*.md")) for e in check_page(page)]
