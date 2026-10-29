from pathlib import Path

from wp_wiki.parse import load_posts
from wp_wiki.read import new_posts, section, show_post, show_replies

FIXTURES = Path(__file__).parent / "fixtures"


def test_show_replies() -> None:
    md = show_replies(load_posts(FIXTURES), [1, 99])
    assert "## 1 · anna · 2021-01-05 · u1" in md
    assert "- 2 · bob · 2021-02-01 · u2\n  Ik krijg foutcode H62" in md
    assert "- 3 · anna" in md
    assert "Mijn stooklijn staat op 35 Ik" not in md  # quote stripped from reply
    assert "## 99: not found" in md


def test_section() -> None:
    text = "TOC: Stooklijn Kamer. Body: Stooklijn uitleg. Kamer tekst."
    assert section(text, "Stooklijn", "Kamer") == "Stooklijn uitleg. "
    assert section(text, "Ontbreekt") == ""
    assert show_post(load_posts(FIXTURES)[0]).startswith("## 1 · anna")


def test_new_posts() -> None:
    md = new_posts(load_posts(FIXTURES), after=1, min_chars=40)
    assert "## 1 ·" not in md
    assert "## 2 · bob · 2021-02-01 · u2\n\nQuotes: 1\n\nIk krijg foutcode H62" in md
    assert "> Mijn stooklijn" not in md
    assert "## 3 · anna" in md
    assert "## 3 ·" not in new_posts(load_posts(FIXTURES), after=1, min_chars=50)
