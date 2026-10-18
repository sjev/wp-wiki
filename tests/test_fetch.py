from pathlib import Path

import httpx

from wp_wiki.fetch import Fetcher, fetch_thread

CONSENT = (
    "<script>const callbackUrl = new URL(decodeURIComponent("
    "'https%3A%2F%2Fgathering.tweakers.net%2Fprivacygate-confirm%3FauthId%3Dabc'))</script>"
)


def page(n: int, last: int) -> str:
    return (
        f'<a href="/forum/list_messages/1/{last}">x</a>'
        f'<div class="message" data-message-id="{n}"></div>'
    )


def make_fetcher(pages: dict[int, str], log: list[str]) -> Fetcher:
    consented = False
    requested = ""

    def handler(req: httpx.Request) -> httpx.Response:
        nonlocal consented, requested
        log.append(req.url.path)
        if req.url.host == "myprivacy.dpgmedia.nl":
            return httpx.Response(200, text=CONSENT)
        if req.url.path == "/privacygate-confirm":
            consented = True
            return httpx.Response(303, headers={"Location": requested})
        if not consented:
            requested = req.url.path
            return httpx.Response(302, headers={"Location": "https://myprivacy.dpgmedia.nl/c"})
        return httpx.Response(200, text=pages[int(req.url.path.rsplit("/", 1)[1])])

    client = httpx.Client(transport=httpx.MockTransport(handler), follow_redirects=True)
    return Fetcher(delay=0, client=client)


def test_fetch_thread_accepts_consent_and_resumes(tmp_path: Path) -> None:
    log: list[str] = []
    fetcher = make_fetcher({0: page(0, 2), 1: page(1, 2), 2: page(2, 2)}, log)

    assert fetch_thread(fetcher, 1, tmp_path) == 3
    assert log.count("/forum/list_messages/1/0") == 2  # once before consent, once via redirect
    assert sorted(p.name for p in (tmp_path / "1").iterdir()) == [
        "0000.html",
        "0001.html",
        "0002.html",
    ]

    log.clear()
    fetcher = make_fetcher({2: page(2, 3), 3: page(3, 3)}, log)
    assert fetch_thread(fetcher, 1, tmp_path) == 2
    assert log[-2:] == ["/forum/list_messages/1/2", "/forum/list_messages/1/3"]
