"""Download the images of single posts, so a writer can look at screenshots and diagrams."""

import logging
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse

import httpx

from wp_wiki.fetch import Fetcher
from wp_wiki.parse import Post

log = logging.getLogger(__name__)


def image_path(out_dir: Path, post_id: int, n: int, url: str) -> Path:
    ext = PurePosixPath(urlparse(url).path).suffix or ".img"
    return out_dir / f"{post_id}-{n}{ext}"


def fetch_images(fetcher: Fetcher, post: Post, out_dir: Path) -> list[Path]:
    """Cache each image as <post>-<n>.<ext>; files already on disk are not fetched again."""
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for n, url in enumerate(post["images"], 1):
        path = image_path(out_dir, post["id"], n, url)
        if not path.exists():
            try:
                path.write_bytes(fetcher.get_response(url).content)
            except httpx.HTTPStatusError as exc:
                # Deleted uploads return 404; skip them, keep the rest.
                log.warning("post %d image %d: HTTP %d", post["id"], n, exc.response.status_code)
                continue
            log.debug("%s -> %s", url, path)
        paths.append(path)
    return paths
