from pathlib import Path

from wp_wiki.cite import check
from wp_wiki.stats import load_posts

FIXTURES = Path(__file__).parent / "fixtures"
URL = "https://gathering.tweakers.net/forum/list_message"


def test_check(tmp_path: Path) -> None:
    (tmp_path / "a.md").write_text(
        f"- [anna, 2021-01-05]({URL}/1#1): ok\n"
        f"- [anna, 2021-01-05]({URL}/2#2): wrong author\n"
        f"- [bob, 2021-02-01]({URL}/9#9): unknown\n"
        f"- [bob]({URL}/2#2): malformed\n",
        encoding="utf-8",
    )
    errors = check(tmp_path, load_posts(FIXTURES))
    assert len(errors) == 3
    assert errors[0].endswith(":2 2: is bob, 2021-02-01")
    assert errors[1].endswith(":3 9: unknown post or bad anchor")
    assert errors[2].endswith(":4: malformed source link")
