Use the shared `marketing-image-reverse-prompt` method on the uploaded marketing image.

Output a structured result with:
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

Priorities:
- reproduce the layout as a reusable template
- preserve original copy language
- extract color, size, safe-margin, and ornament constraints
- use OCR first when available, then mark uncertain text with `review_needed: true`
- if comparing a generated result to a reference, output revision guidance and a revised prompt
