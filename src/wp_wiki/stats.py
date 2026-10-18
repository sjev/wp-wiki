"""Deterministic corpus summary of parsed posts, to plan the wiki structure without reading posts."""

import json
import re
from collections import Counter
from collections.abc import Iterable
from itertools import pairwise
from pathlib import Path
from urllib.parse import urlparse

from wp_wiki.parse import Post

# Topic -> regex on lowercase text. Keys follow the planned taxonomy in CLAUDE.md.
TOPICS: dict[str, str] = {
    "stooklijn": r"stooklijn|heating curve|watertemperatuur",
    "hydraulica": r"hydraul|open verdeler|low loss|bypass|flow|debiet|circulatiepomp",
    "buffervat": r"buffervat|buffer",
    "legionella": r"legionella|steriliz|sterilis",
    "tapwater": r"tapwater|boiler|dhw|sww",
    "cop": r"\bcop\b|\bscop\b|rendement",
    "dimensionering": r"warmteverlies|dimensioner|vermogen|kw\b",
    "ontdooien": r"ontdooi|defrost|defrosting",
    "koelen": r"koelen|koeling|cooling",
    "geluid": r"geluid|herrie|\bdb\b|bromt",
    "installatie": r"installateur|install|montage|plaatsing",
    "bekabeling": r"bekabel|kabel|aardlek|groep|zekering|bedrading",
    "heishamon": r"heishamon",
    "mqtt": r"\bmqtt\b|topic",
    "rules": r"\brules?\b|regels|script",
    "home-assistant": r"home assistant|homeassistant|\bha\b",
    "cz-taw1": r"cz-taw1|cz taw1|smart cloud|comfort cloud|taw1",
    "storing": r"storing|foutcode|error|\b[hf]\d{2}\b",
    "subsidie": r"subsidie|isde",
    "energieprijs": r"dynamisch|tarief|kwh prijs|stroomprijs",
}
ERROR_CODE = re.compile(r"\b[HF]\d{2}\b")
MODEL = re.compile(r"\bW[HC]-[A-Z0-9]{6,}\b")
MQTT_NAME = re.compile(r"\b(?:Set|main/|panasonic_heat_pump/)[A-Za-z_/]*[A-Z][A-Za-z0-9_]+")
WORD = re.compile(r"[a-zà-ÿ][a-zà-ÿ0-9-]{2,}")
_STOP = (
    "een het van dat die met voor niet maar ook als dan wel nog bij naar heb hebt heeft dit zijn"
    " wat kan wordt worden was waren zou zal kun kunt moet hij zij wij jij ben bent jouw mijn zo"
    " hier daar dus toch nu al uit om op aan er te tot door over meer veel geen echt gewoon even"
    " erg iets alleen ik je we ze de en in is of en mij me hem haar ons hun deze welke wie waar"
    " hoe omdat want zelf weer had heel goed toen wel quote"
)
STOPWORDS = set(_STOP.split())


def load_posts(posts_dir: Path) -> list[Post]:
    return [
        json.loads(line)
        for f in sorted(posts_dir.glob("*.jsonl"))
        for line in f.open(encoding="utf-8")
    ]


def _table(header: str, rows: Iterable[tuple[object, ...]]) -> list[str]:
    cols = header.split("|")
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    return lines + ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]


def _counts(title: str, counter: Counter[str], n: int) -> list[str]:
    return [f"\n## {title}\n", ", ".join(f"`{k}` {v}" for k, v in counter.most_common(n))]


def _strip_quotes(text: str) -> str:
    return "\n".join(ln for ln in text.splitlines() if not ln.startswith(">"))


def _snippet(post: Post) -> str:
    return " ".join(_strip_quotes(post["text"]).split())[:80].replace("|", "/")


def report(posts: list[Post]) -> str:
    by_id = {p["id"]: p for p in posts}
    quoted = Counter(q for p in posts for q in set(p["quotes"]) if q in by_id)
    years = Counter((p["thread_id"], p["date"][:4]) for p in posts)
    texts = {p["id"]: _strip_quotes(p["text"]) for p in posts}
    lower = {i: t.lower() for i, t in texts.items()}

    out = [f"# Corpus stats\n\n{len(posts)} posts, {len({p['author'] for p in posts})} authors.\n"]
    out += ["## Posts per thread per year\n", *_table("thread|year|posts", sorted(years.items()))]
    authors = Counter(p["author"] for p in posts)
    out += ["\n## Top authors\n", *_table("author|posts", authors.most_common(15))]

    def top(ids: Iterable[int], n: int) -> list[tuple[object, ...]]:
        ranked = sorted(ids, key=lambda i: -quoted[i])[:n]
        return [
            (i, quoted[i], by_id[i]["author"], by_id[i]["date"][:10], _snippet(by_id[i]))
            for i in ranked
        ]

    out += ["\n## Most-quoted posts\n", *_table("id|quoted|author|date|start", top(quoted, 30))]

    topic_ids = {t: [i for i, s in lower.items() if re.search(rx, s)] for t, rx in TOPICS.items()}
    out += ["\n## Topics\n"]
    out += _table(
        "topic|posts|quoted refs",
        ((t, len(ids), sum(quoted[i] for i in ids)) for t, ids in topic_ids.items()),
    )
    for t, ids in topic_ids.items():
        out += [f"\n### {t}\n", *_table("id|quoted|author|date|start", top(ids, 5))]

    out += _counts(
        "Error codes", Counter(m for t in texts.values() for m in ERROR_CODE.findall(t)), 30
    )
    out += _counts("Models", Counter(m for t in texts.values() for m in MODEL.findall(t)), 30)
    out += _counts(
        "MQTT / parameter names",
        Counter(m for t in texts.values() for m in MQTT_NAME.findall(t)),
        40,
    )
    domains = Counter(urlparse(u).netloc.removeprefix("www.") for p in posts for u in p["links"])
    out += _counts("Link domains", domains, 25)

    bigrams: Counter[str] = Counter()
    for s in lower.values():
        words = [w for w in WORD.findall(s) if w not in STOPWORDS]
        bigrams.update(f"{a} {b}" for a, b in pairwise(words))
    out += _counts("Top bigrams", bigrams, 60)
    return "\n".join(out) + "\n"
