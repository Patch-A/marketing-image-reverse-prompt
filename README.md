# marketing-image-reverse-prompt

A Codex skill for reverse-engineering copy-heavy marketing images into reusable prompt templates.

## What it does

- Analyze marketing posters, banners, cover images, and other text-heavy creatives
- Extract reusable keyword blocks for image generation
- Preserve original copy as editable text slots
- Output English primary prompts and Chinese comparison prompts
- Capture layout, size, color, and ornament constraints
- Support manual revision loops after a first-pass generated result

## Current scope

This repository currently includes:

- the skill definition in `marketing-image-reverse-prompt/`
- reference docs for output schema, prompt rules, model notes, and revision guidance
- sample structured outputs in `outputs/`

## Target models

- `gpt-image-2`
- `Nano Banana 2`

## Key ideas

- Treat the image as a reusable template, not a one-off caption
- Separate main copy from microcopy and weak OCR regions
- Preserve original text language
- Add layout fidelity controls such as aspect ratio, safe margins, and hero scale
- Add color fidelity controls and ornament extraction for closer reproduction

## Repository layout

```text
marketing-image-reverse-prompt/
outputs/
work/
README.md
```

## Notes

- The current version is design- and schema-first.
- Tiny text and faint decorative elements are explicitly modeled, but OCR automation is not implemented yet.
- Future iterations can add scripts for OCR, palette sampling, template storage, and revision assistance.
