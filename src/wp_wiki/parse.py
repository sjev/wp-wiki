"""Parse GoT thread pages into post records. Selectors verified against live HTML, 2026-10."""

import re
from datetime import UTC, datetime
from typing import TypedDict

from bs4 import BeautifulSoup, Tag

FORUM = "https://gathering.tweakers.net/forum"
QUOTE_LINK = re.compile(r"/forum/list_message/(\d+)")


class Post(TypedDict):
    id: int
    thread_id: int
    page: int
    url: str
    page_url: str
    author: str
    author_id: int
    timestamp: int
    date: str
    topicstarter: bool
    edited: str | None
    quotes: list[int]
    links: list[str]
    text: str
    html: str


def post_url(post_id: int) -> str:
    return f"{FORUM}/list_message/{post_id}#{post_id}"


def page_url(thread_id: int, page: int) -> str:
    return f"{FORUM}/list_messages/{thread_id}/{page}"


def last_page(html: str, thread_id: int, current: int) -> int:
    """Highest 0-based page number linked from this page's pagination."""
    pages = re.findall(rf"/forum/list_messages/{thread_id}/(\d+)", html)
    return max([current, *map(int, pages)])


def _to_text(content: Tag) -> str:
    # Work on a copy so the stored HTML stays untouched.
    node = BeautifulSoup(str(content), "lxml")
    for br in node.find_all("br"):
        br.replace_with("\n")
    for block in node.find_all(["h5", "h6", "li", "p", "div"]):
        block.insert_after("\n")
    # Reverse order handles nested quotes innermost first, giving "> > " prefixes.
    for quote in reversed(node.find_all("blockquote")):
        lines = quote.get_text().strip().splitlines()
        quote.replace_with("\n" + "\n".join(f"> {ln}" for ln in lines) + "\n")
    text = re.sub(r"[ \t]+\n", "\n", node.get_text())
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _parse_message(msg: Tag, thread_id: int, page: int) -> Post | None:
    content = msg.select_one(".messagecontent")
    stamp = msg.select_one(".date [data-timestamp]")
    author = msg.select_one(".userheader .username a")
    if content is None or stamp is None or author is None:
        return None
    post_id = int(str(msg["data-message-id"]))
    edit = content.select_one("p.edit")
    edited = " ".join(edit.get_text().split()).strip("[] ") if edit else None
    if edit:
        edit.decompose()
    quotes = [
        int(m.group(1))
        for a in content.select("blockquote a.messagelink")
        if (m := QUOTE_LINK.search(str(a.get("href", ""))))
    ]
    links = sorted(
        {
            href
            for a in content.find_all("a", href=True)
            if (href := str(a["href"])).startswith("http") and "/forum/list_message/" not in href
        }
    )
    timestamp = int(str(stamp["data-timestamp"]))
    return Post(
        id=post_id,
        thread_id=thread_id,
        page=page,
        url=post_url(post_id),
        page_url=page_url(thread_id, page),
        author=author.get_text(strip=True),
        author_id=int(str(msg.get("data-owner-id", "0"))),
        timestamp=timestamp,
        date=datetime.fromtimestamp(timestamp, UTC).isoformat(),
        topicstarter="topicstarter" in (msg.get("class") or []),
        edited=edited,
        quotes=quotes,
        links=links,
        text=_to_text(content),
        html=content.decode_contents().strip(),
    )


def parse_page(html: str, thread_id: int, page: int) -> list[Post]:
    soup = BeautifulSoup(html, "lxml")
    posts = (
        _parse_message(m, thread_id, page) for m in soup.select("div.message[data-message-id]")
    )
    return [p for p in posts if p is not None]
