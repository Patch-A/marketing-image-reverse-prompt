Use the shared `marketing-image-reverse-prompt` workflow to analyze the uploaded marketing image.

Return structured output with these sections when applicable:
- `task`
- `model_targets`
- `analysis`
- `summary`
- `ocr`
- `subjects`
- `text_slots`
- `ornaments`
- `keyword_blocks`
- `prompt_variants`
- `template`

Rules:
- Preserve original copy exactly.
- Prefer OCR-assisted extraction first, then correct by visual review.
- Produce English primary prompts and one full Chinese comparison prompt.
- Keep reusable layout, color, and ornament constraints explicit.
- If the upload is a generated result rather than a reference, switch to revision mode and return `differences`, `revision_strategy`, and `revised_prompt`.
