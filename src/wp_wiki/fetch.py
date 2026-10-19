"""Polite, resumable download of GoT thread pages into a raw HTML cache."""

import logging
import random
import re
import time
from pathlib import Path
from urllib.parse import unquote

import httpx

from wp_wiki.parse import last_page, page_url

log = logging.getLogger(__name__)

USER_AGENT = "wp-wiki/0.1 (forum knowledge archive, low-rate)"
CONSENT_HOST = "myprivacy.dpgmedia.nl"
# The consent wall embeds its functional-only callback URL in inline JS.
CONSENT_CALLBACK = re.compile(r"decodeURIComponent\('([^']+)'\)")
RETRY_STATUS = {429, 500, 502, 503, 504}


class FetchError(RuntimeError):
    pass


class Fetcher:
    def __init__(
        self, delay: float = 3.0, retries: int = 4, client: httpx.Client | None = None
    ) -> None:
        self.client = client or httpx.Client(
            headers={"User-Agent": USER_AGENT}, follow_redirects=True, timeout=30
        )
        self.delay = delay
        self.retries = retries
        self._last_request = 0.0

    def _throttle(self) -> None:
        wait = self.delay * random.uniform(1.0, 1.5) - (time.monotonic() - self._last_request)
        if wait > 0:
            time.sleep(wait)
        self._last_request = time.monotonic()

    def _accept_consent(self, html: str) -> httpx.Response:
        """Follow the callback; it redirects back to the requested page."""
        match = CONSENT_CALLBACK.search(html)
        if not match:
            raise FetchError("Consent page without callback URL; page layout changed?")
        self._throttle()
        return self.client.get(unquote(match.group(1)))

    def get(self, url: str) -> str:
        return self.get_response(url).text

    def get_response(self, url: str) -> httpx.Response:
        for attempt in range(1, self.retries + 1):
            self._throttle()
            try:
                resp = self.client.get(url)
            except httpx.TransportError as exc:
                log.warning("attempt %d: %s", attempt, exc)
                time.sleep(self.delay * 2**attempt)
                continue
            if resp.url.host == CONSENT_HOST:
                log.info("accepting functional consent")
                resp = self._accept_consent(resp.text)
            if resp.status_code in RETRY_STATUS:
                wait = float(resp.headers.get("Retry-After", self.delay * 2**attempt))
                log.warning("attempt %d: HTTP %d, waiting %.0fs", attempt, resp.status_code, wait)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp
        raise FetchError(f"Giving up on {url} after {self.retries} attempts")


def cached_pages(thread_dir: Path) -> list[int]:
    return sorted(int(p.stem) for p in thread_dir.glob("*.html"))


def fetch_thread(fetcher: Fetcher, thread_id: int, raw_dir: Path, refresh: bool = False) -> int:
    """Download new pages. Always re-fetches the newest cached page, since it may have grown."""
    thread_dir = raw_dir / str(thread_id)
    thread_dir.mkdir(parents=True, exist_ok=True)
    cached = cached_pages(thread_dir)
    page = 0 if refresh or not cached else cached[-1]
    last = page
    fetched = 0
    while page <= last:
        html = fetcher.get(page_url(thread_id, page))
        if "data-message-id" not in html:
            raise FetchError(f"No posts on page {page} of {thread_id}; blocked or layout changed?")
        (thread_dir / f"{page:04d}.html").write_text(html, encoding="utf-8")
        last = last_page(html, thread_id, page)
        log.info("thread %d: page %d/%d", thread_id, page, last)
        fetched += 1
        page += 1
    return fetched
