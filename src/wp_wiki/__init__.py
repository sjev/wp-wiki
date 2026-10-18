"""Scrape and curate Tweakers forum knowledge on heat pumps."""

from typing import NamedTuple


class Thread(NamedTuple):
    brand: str
    title: str


THREADS: dict[int, Thread] = {
    2039982: Thread("panasonic", "Panasonic Warmtepomp 101: Installatie en Optimalisatie #1"),
    2178982: Thread("panasonic", "Panasonic Warmtepomp 101: Installatie en Optimalisatie #2"),
}
