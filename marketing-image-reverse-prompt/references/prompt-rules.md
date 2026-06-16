# Prompt Rules

Build prompts for reproducibility first, elegance second.

## Prompt Outputs

Always produce:
- an English primary prompt for each requested target model
- a pure Chinese comparison prompt

## Assembly Order

Prefer this order when building prompts:
1. scene type and marketing intent
2. hero subject
3. supporting elements
4. style and art direction
5. composition, layout, and aspect ratio
6. safe margins, relative scale, and footer or header proportions
7. color fidelity and palette control
8. lighting, texture, and ornament detail
9. text rendering instructions
10. negative constraints

## English Prompt Guidance

- Use direct, production-style wording.
- State the overall image type clearly, such as `clean commercial marketing poster`.
- Call out the hero subject early.
- Describe copy hierarchy and placement explicitly.
- If the image contains Chinese text, instruct the model to render the exact Chinese text rather than translating it.

## Chinese Prompt Guidance

- Keep it fully in Chinese.
- Preserve the original copy as-is.
- Mirror the same structure and constraints as the English prompt.
- Use it as a comparison and editing aid, not as the only prompt unless the user requests it.

## Text Rendering Rules

When text is important:
- describe the role of each slot
- describe approximate placement
- keep the original wording in the slot data
- mention layout hierarchy if it affects the design

Example:
- headline at the top center
- smaller subtitle beneath the headline
- CTA inside a button-like area near the bottom

## Size Optimization Rules

When the user cares about matching the original layout, explicitly include:
- target aspect ratio
- portrait or landscape orientation
- safe margins around text
- relative size of the hero subject
- relative height of footer or header bands

Prefer concrete wording such as:
- `use a 3:4 vertical poster layout`
- `keep the hero object occupying roughly 55% to 60% of the canvas height`
- `reserve a bottom information band around 16% to 18% of the canvas height`
- `keep top corner vertical labels inside the outer 5% margin`

Do not rely on generic wording like `similar size` or `same composition` when layout fidelity is important.

## Color Optimization Rules

When color mismatch is likely, explicitly describe:
- background hue family
- saturation level
- typography tone
- hero subject dark/light contrast
- footer or accent band darkness

Prefer concrete wording such as:
- `use a muted yellow-olive background rather than a fresh bright green`
- `keep the typography warm off-white instead of pure white`
- `make the footer blocks dark olive green, almost black-green`

If available, include compact swatch-like targets in analysis output so the prompt builder can preserve them.

If a palette helper is available, use sampled swatches to anchor:
- dominant background
- hero object darks and mids
- typography tone
- footer or accent darkness

## Ornament and Faint-Element Rules

If the reference includes faint lines, guide marks, soft ghost text, or low-opacity structures:
- name them explicitly
- keep their placement relative to the main text block
- mention whether they should remain subtle or prominent

These elements are easy for models to omit unless they are called out directly.

## Negative Constraints

Include only constraints that matter to reproduction quality, such as:
- no clutter
- no extra products
- no distorted text
- no unrelated props

Avoid bloating the prompt with dozens of negatives unless the image clearly requires it.

## OCR Integration

If OCR is available, use it as a draft input only. Preserve exact source text in the final slot data, and do not let noisy OCR override visual confirmation for hero headlines or tiny microcopy.
