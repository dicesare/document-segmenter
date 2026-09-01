import json

import pytest

from document_segmenter import segment_file
from document_segmenter.cli import _write


def test_markdown_headings_and_paragraphs(tmp_path):
    source = tmp_path / "brief.txt"
    source.write_text("# Overview\nA short paragraph.\n\n## Scope\nSafe synthetic data.", encoding="utf-8")

    segments = segment_file(source)

    assert [segment.type for segment in segments] == ["title", "paragraph", "subtitle", "paragraph"]
    assert segments[0].level == 1
    assert segments[-1].text == "Safe synthetic data."


def test_json_export(tmp_path):
    source = tmp_path / "sample.txt"
    source.write_text("Hello world", encoding="utf-8")
    output = tmp_path / "segments.json"

    _write(segment_file(source), output)

    assert json.loads(output.read_text(encoding="utf-8"))[0]["text"] == "Hello world"


def test_rejects_unknown_format(tmp_path):
    source = tmp_path / "sample.bin"
    source.write_bytes(b"data")
    with pytest.raises(ValueError, match="Unsupported"):
        segment_file(source)
