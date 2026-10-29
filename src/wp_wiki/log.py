"""Console (colored) and rotating file logging for the CLI."""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

import coloredlogs

FMT = "%(asctime)s %(levelname)s %(name)s: %(message)s"
FILE_FMT = "%(asctime)s %(levelname)s %(name)s %(funcName)s:%(lineno)d: %(message)s"


class _ConsoleFilter(logging.Filter):
    """Hide httpx request lines on the console; the file keeps them."""

    def filter(self, record: logging.LogRecord) -> bool:
        return not record.name.startswith("httpx") or record.levelno >= logging.WARNING


def setup_logging(log_file: Path) -> None:
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    log_file.parent.mkdir(parents=True, exist_ok=True)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5_000_000, backupCount=3, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(FILE_FMT))
    root.addHandler(file_handler)
    coloredlogs.install(level=logging.INFO, fmt=FMT, logger=root)
    for handler in root.handlers:
        if handler is not file_handler:
            handler.addFilter(_ConsoleFilter())
    # httpcore DEBUG is per-socket noise even in the file.
    logging.getLogger("httpcore").setLevel(logging.INFO)
    logging.getLogger("httpx").setLevel(logging.INFO)


def log_errors(errors: list[str], kind: str) -> int:
    """Log each error and a count; return the exit code."""
    log = logging.getLogger(__name__)
    for e in errors:
        log.error(e)
    log.info("%d %s errors", len(errors), kind)
    return 1 if errors else 0
