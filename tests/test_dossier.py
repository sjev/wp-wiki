from pathlib import Path

from wp_wiki.dossier import dossier
from wp_wiki.stats import load_posts

FIXTURES = Path(__file__).parent / "fixtures"


def test_dossier() -> None:
    posts = load_posts(FIXTURES)
    for p in posts:
        p["text"] += "\n\n" + "opvulling " * 20
    md = dossier(posts, "storing", r"\b[hf]\d{2}\b")
    assert "Pattern `\\b[hf]\\d{2}\\b`: 1 posts, top 40." in md
    assert "## 2 · bob · 2021-02-01 · score 4" in md  # 1 hit + 3 per quote
    assert "Ik krijg foutcode H62" in md
    assert "Mijn stooklijn staat op 35" not in md  # quoted line is excluded
    assert "opvulling" not in md  # non-matching paragraph is dropped
