import argparse
import csv
import json
from pathlib import Path

from .core import segment_file


def _write(segments: list, output: Path) -> None:
    rows = [segment.to_dict() for segment in segments]
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() == ".csv":
        with output.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=["text", "type", "level", "source"])
            writer.writeheader()
            writer.writerows(rows)
    else:
        output.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Segment PDF, DOCX or TXT documents.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", "-o", type=Path, default=Path("segments.json"))
    args = parser.parse_args()
    _write(segment_file(args.input), args.output)
