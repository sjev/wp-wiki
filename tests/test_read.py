from pathlib import Path

from wp_wiki.read import section, show_post, show_replies
from wp_wiki.stats import load_posts

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
