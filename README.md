# Document Segmenter

Turn PDF, DOCX and TXT documents into structured JSON or CSV segments ready for search, analytics and RAG pipelines.

## Why this project

Long documents are easier to retrieve when their hierarchy is preserved. This package extracts headings, paragraphs and tables behind a small Python API and CLI, without requiring a hosted service.

```text
PDF / DOCX / TXT → format adapter → normalized segments → JSON / CSV
```

## Quick start

```bash
python -m venv .venv
pip install -e .
document-segmenter examples/sample.txt --output build/segments.json
```

Example output:

```json
[{"text":"Project overview","type":"title","level":1,"source":"sample.txt"}]
```

Install PDF and DOCX support with `pip install -e .[documents]`.

## Python API

```python
from document_segmenter import segment_file

segments = segment_file("examples/sample.txt")
for segment in segments:
    print(segment.type, segment.text)
```

## Design choices

- one normalized, typed model across all formats;
- adapters isolate optional PDF/DOCX dependencies;
- no network calls and no data retained;
- synthetic fixtures keep the repository safe to publish;
- deterministic JSON and CSV exports are easy to test.

## Development

```bash
pip install -e .[dev]
pytest
ruff check .
```

## Limitations

PDF heading detection relies on Markdown emitted by `pymupdf4llm`; scanned PDFs require OCR before segmentation. TXT headings use Markdown-style `#` prefixes.

## License

Released under the [MIT License](LICENSE).
