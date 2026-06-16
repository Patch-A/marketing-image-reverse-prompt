Analyze the provided marketing visual as a reusable generation template, not as a general caption.

Follow the shared schema:
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

Requirements:
- Keep exact source wording in all final text slots.
- Treat OCR as draft evidence, not final truth.
- Separate headline copy from microcopy and weak OCR zones.
- Include model-facing English prompts plus a Chinese comparison prompt.
- In revision mode, diagnose concrete gaps and emit a revised prompt.
