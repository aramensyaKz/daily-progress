"""Create a structured daily-progress journal entry."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


def parse_date(value: str) -> date:
    """Parse an ISO date and report a useful argparse error."""
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD format") from exc


def slugify(value: str) -> str:
    """Convert a topic into a stable filename component."""
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("topic must contain at least one Latin letter or digit")
    return slug


def create_entry(root: Path, entry_date: date, topic: str, summary: str) -> Path:
    """Create one new journal entry without overwriting existing work."""
    journal = root / "journal"
    journal.mkdir(parents=True, exist_ok=True)
    destination = journal / f"{entry_date.isoformat()}-{slugify(topic)}.md"

    content = (
        f"# {entry_date.isoformat()}: {topic}\n\n"
        "## Summary\n\n"
        f"{summary.strip()}\n\n"
        "## Result\n\n"
        "- Describe the concrete output.\n\n"
        "## Verification\n\n"
        "- Record how the result was checked.\n"
    )
    with destination.open("x", encoding="utf-8", errors="strict") as output:
        output.write(content)
    return destination


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", type=parse_date, default=date.today())
    parser.add_argument("--topic", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    return parser


def main() -> None:
    args = build_parser().parse_args()
    path = create_entry(args.root, args.date, args.topic, args.summary)
    print(path)


if __name__ == "__main__":
    main()
