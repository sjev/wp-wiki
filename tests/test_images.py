from pathlib import Path
from typing import cast

import httpx

from wp_wiki.fetch import Fetcher
from wp_wiki.images import fetch_images
from wp_wiki.parse import Post


def test_fetch_images_caches_by_post_and_index(tmp_path: Path) -> None:
    requested: list[str] = []

    def handler(req: httpx.Request) -> httpx.Response:
        requested.append(req.url.path)
        return httpx.Response(404 if "gone" in req.url.path else 200, content=b"PNG")

    client = httpx.Client(transport=httpx.MockTransport(handler))
    fetcher = Fetcher(delay=0, client=client)
    post = cast(
        Post,
        {
            "id": 7,
            "images": [
                "https://t.net/i/x/a.png?f=l",
                "https://t.net/i/gone.png",
                "https://t.net/i/b.jpg",
            ],
        },
    )

    paths = fetch_images(fetcher, post, tmp_path)
    fetch_images(fetcher, post, tmp_path)

    assert [p.name for p in paths] == ["7-1.png", "7-3.jpg"]
    assert paths[0].read_bytes() == b"PNG"
    assert requested == ["/i/x/a.png", "/i/gone.png", "/i/b.jpg", "/i/gone.png"]
