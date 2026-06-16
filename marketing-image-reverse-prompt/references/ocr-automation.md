# OCR Automation

Use OCR as a first-pass helper for text-heavy marketing images.

## Goals

- extract visible copy into structured slots
- keep uncertain microcopy separate from high-confidence text
- support manual review and revision loops
- remain engine-agnostic so it can work with RapidOCR, Tesseract, cloud OCR, or model-native OCR

## Suggested pipeline

1. Run OCR on the source image.
2. Split recognized text into blocks by position and confidence.
3. Normalize candidates into `text_slots`.
4. Mark tiny, stylized, or ambiguous strings with `review_needed: true`.
5. Feed the cleaned slots into prompt generation.

## Bundled Script

Run the included helper:

```bash
pip install -r marketing-image-reverse-prompt/scripts/requirements.txt
```

Then run:

```bash
python marketing-image-reverse-prompt/scripts/ocr_extract.py path/to/image.png
```

The script prefers `RapidOCR` when the Python package is available and falls back to `tesseract` when the CLI is installed.

## Output fields to keep

- `text`
- `language`
- `confidence`
- `bbox`
- `review_needed`
- `source`

## Notes

- Prefer preserving the original wording over guessing corrected copy.
- Keep microcopy separate from headline-level text.
- When the OCR engine is weak on vertical or decorative text, keep the raw image crop for manual confirmation.
- If neither OCR engine is available, keep the workflow moving by preserving an empty OCR payload plus explicit review notes.
