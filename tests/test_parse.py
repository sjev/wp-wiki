from pathlib import Path

from wp_wiki.parse import last_page, parse_page

HTML = (Path(__file__).parent / "fixtures" / "page.html").read_text()


def test_parse_page_extracts_posts_with_backlinks() -> None:
    first, reply = parse_page(HTML, 2178982, 3)

    assert first["id"] == 100
    assert first["url"] == "https://gathering.tweakers.net/forum/list_message/100#100"
    assert first["page_url"] == "https://gathering.tweakers.net/forum/list_messages/2178982/3"
    assert first["author"] == "alice"
    assert first["author_id"] == 7
    assert first["date"] == "2023-03-13T21:44:00+00:00"
    assert first["topicstarter"] is True
    assert first["edited"] == "Voor 5% gewijzigd door alice op 14-03-2023 10:00"
    assert first["links"] == ["https://github.com/Egyras/HeishaMon"]
    assert "SetZ1HeatRequestTemperature" in first["text"]
    assert "gewijzigd" not in first["text"]
    assert "<b>SetZ1HeatRequestTemperature</b>" in first["html"]

    assert reply["quotes"] == [100]
    assert reply["topicstarter"] is False
    assert "> Set it via MQTT." in reply["text"]
    assert reply["text"].endswith("Works for me.")


def test_parse_page_skips_incomplete_messages() -> None:
    assert [p["id"] for p in parse_page(HTML, 2178982, 0)] == [100, 101]


def test_last_page() -> None:
    assert last_page(HTML, 2178982, 0) == 105
    assert last_page(HTML, 2178982, 200) == 200
    assert last_page(HTML, 999, 4) == 4
