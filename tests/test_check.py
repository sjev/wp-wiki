from pathlib import Path

from wp_wiki.check import check


def test_check(tmp_path: Path) -> None:
    (tmp_path / "ok.md").write_text(
        "---\ntitle: Ok\nweight: 10\ntags: [R290, Storing]\n---\n\n"
        "[a](bad.md#x) [b](https://x.nl/y.md) [c](#top)\n\n```mermaid\nA[x](missing.md)\n```\n",
        encoding="utf-8",
    )
    (tmp_path / "bad.md").write_text(
        "---\ntitle: Bad\ntags: [Foo]\n---\n\n[x](missing.md)\n", encoding="utf-8"
    )
    (tmp_path / "none.md").write_text("# No front matter\n", encoding="utf-8")
    errors = check(tmp_path)
    assert [e.split(": ", 1)[1] for e in errors] == [
        "no weight",
        "unknown tag 'Foo'",
        "broken link missing.md",
        "no front matter",
    ]
