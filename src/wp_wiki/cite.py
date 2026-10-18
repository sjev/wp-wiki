"""Check that every source link in docs/ points to a real post with the stated author and date."""

import re
from pathlib import Path

from wp_wiki.parse import Post

CITE = re.compile(
    r"\[([^\]]+?), (\d{4}-\d{2}-\d{2})\]"
    r"\(https://gathering\.tweakers\.net/forum/list_message/(\d+)#(\d+)\)"
)


def check(docs: Path, posts: list[Post]) -> list[str]:
    by_id = {p["id"]: p for p in posts}
    errors: list[str] = []
    for page in sorted(docs.rglob("*.md")):
        for n, line in enumerate(page.read_text(encoding="utf-8").splitlines(), 1):
            found = CITE.findall(line)
            if line.count("list_message/") > len(found) and "<id>" not in line:
                errors.append(f"{page}:{n}: malformed source link")
            for author, date, pid, anchor in found:
                where = f"{page}:{n} {pid}"
                p = by_id.get(int(pid))
                if p is None or pid != anchor:
                    errors.append(f"{where}: unknown post or bad anchor")
                elif (p["author"], p["date"][:10]) != (author, date):
                    errors.append(f"{where}: is {p['author']}, {p['date'][:10]}")
    return errors
