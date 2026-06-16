Task: reverse-engineer a copy-heavy marketing image into a reusable prompt template.

Core output contract:
- `analysis`
- `ocr`
- `subjects`
- `text_slots`
- `ornaments`
- `keyword_blocks`
- `prompt_variants`
- `template`

Behavior:
- Use OCR as a first pass if tools are available.
- Preserve exact source text in final reviewed slots.
- Keep layout hierarchy, safe margins, and relative scale explicit.
- Produce one English prompt per target model and one Chinese comparison prompt.
- If the input is a generated attempt, switch to revision mode and return concrete correction guidance.
