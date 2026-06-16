# marketing-image-reverse-prompt

A reusable workflow for reverse-engineering copy-heavy marketing images into structured prompt templates. It can be used as a Codex skill and adapted for other AI tools that accept prompt schemas, OCR-assisted text slots, or structured prompt payloads.

## What it does

- Analyze marketing posters, banners, cover images, and other text-heavy creatives
- Extract reusable keyword blocks for image generation
- Preserve original copy as editable text slots
- Output English primary prompts and Chinese comparison prompts
- Capture layout, size, color, and ornament constraints
- Support OCR-assisted first-pass extraction and manual revision loops

## Current scope

This repository currently includes:

- the skill definition in `marketing-image-reverse-prompt/`
- reference docs for output schema, prompt rules, model notes, OCR automation, portability, and revision guidance
- adapter prompt templates in `marketing-image-reverse-prompt/templates/adapters/`
- sample structured outputs in `outputs/`

## Quick start

Choose the path that matches your host tool:

1. Codex:
   - use `marketing-image-reverse-prompt/SKILL.md`
   - load the referenced docs as needed
2. Other AI tools:
   - start from `marketing-image-reverse-prompt/templates/adapters/`
   - pair the chosen adapter with the shared references in `marketing-image-reverse-prompt/references/`
3. OCR helper:
   - install `rapidocr-onnxruntime` or provide a local `tesseract` binary
   - run `python marketing-image-reverse-prompt/scripts/ocr_extract.py path/to/image.png`

## Target models

- `gpt-image-2`
- `nano-banana-2`

## Key ideas

- Treat the image as a reusable template, not a one-off caption
- Separate main copy from microcopy and weak OCR regions
- Preserve original text language
- Add layout fidelity controls such as aspect ratio, safe margins, and hero scale
- Add color fidelity controls and ornament extraction for closer reproduction
- Keep the output portable across AI tools, not tied to a single host app

## Repository layout

```text
marketing-image-reverse-prompt/
outputs/
README.md
```

## Notes

- The current version is still design- and schema-first.
- OCR is now assisted by a bundled script, but faint decorative elements and tiny stylized text may still need manual review.
- Future iterations can add richer OCR providers, palette sampling, template storage, and revision assistance.
