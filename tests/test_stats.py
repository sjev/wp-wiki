from pathlib import Path

from wp_wiki.stats import load_posts, report

FIXTURES = Path(__file__).parent / "fixtures"


def test_report() -> None:
    posts = load_posts(FIXTURES)
    md = report(posts)
    assert "3 posts, 2 authors." in md
    assert "| 1 | 2 | anna | 2021-01-05 | Mijn stooklijn" in md
    assert "`H62` 1" in md
    assert "`WH-MDC05J3E5` 1" in md
    assert "`SetZ1HeatRequestTemperature` 1" in md
    assert "`github.com` 1" in md
    assert "| stooklijn | 1 | 2 |" in md  # quoted line in post 2 is excluded from matching
