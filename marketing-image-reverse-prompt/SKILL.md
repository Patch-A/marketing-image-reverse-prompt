---
name: marketing-image-reverse-prompt
description: Reverse-engineer copy-heavy marketing images into reusable prompt templates, bilingual prompts, editable text slots with role and position metadata, and iterative revision guidance. Use when Codex needs to analyze posters, banners, covers, or other marketing visuals with embedded text; extract image-generation-ready keywords; preserve original copy; produce prompts for gpt-image-2 or Nano Banana 2; save reusable templates; or refine prompts after a user uploads a first-pass generated result.
---

# Marketing Image Reverse Prompt

Analyze the reference image as a reusable marketing creative template rather than as a one-off caption.

Prioritize reproducibility over literary description. The goal is to output keywords and prompts that can be fed back into an image model, preserve original copy as structured slots, and support a manual closed loop where the user uploads a generated result for further correction.

## Scope

Focus on:
- posters
- banners
- social creatives
- cover images
- marketing visuals with clear text hierarchy

Do not optimize for:
- generic image captioning
- pure photography datasets
- multi-page graphic design files
- production-grade visual editing
- automatic similarity scoring in the first pass

## Workflow

1. Identify the request type:
   - `reverse_from_reference`: analyze a reference marketing image and build a reusable template.
   - `revise_generated_result`: compare a first-pass generated image against the reference and produce a revised prompt.
2. Confirm the image is a marketing visual with meaningful embedded copy. If it is not, still help, but state that the output is optimized for copy-heavy layouts.
3. Analyze the image in layers:
   - scene type and marketing intent
   - main subject and supporting elements
   - style, color palette, texture, lighting, and composition
   - aspect ratio, canvas orientation, safe margins, and relative scale
   - decorative guides, faint lines, translucent overlays, and microcopy
   - text hierarchy and layout relationships
4. Extract every visible text slot and preserve the original text exactly as shown.
5. Build structured keyword blocks for subject, style, layout, lighting, and negative constraints.
6. Generate:
   - English primary prompts
   - a fully Chinese comparison prompt
   - a structured template object
7. Save or update the template record when a storage path or template store is available.
8. If the user provides a generated result, compare it to the reference, classify the gaps, and produce a revised prompt and revision notes.

Read [references/output-schema.md](references/output-schema.md) before producing machine-readable output.

## Output Priorities

Always prefer these outputs over a single long paragraph:
- `analysis`: visual summary and design logic
- `keyword_blocks`: reusable image-generation keywords
- `prompt_variants`: English model prompts plus a Chinese comparison prompt
- `text_slots`: editable copy with role and position metadata
- `ornaments`: non-copy graphic elements such as guide lines, faint rules, footer shapes, and low-opacity decorations
- `template`: reusable template object with history hooks

If the user asks for "keywords," still include the structured blocks. Do not collapse everything into prose unless the user explicitly wants prose only.

## Text Slot Rules

For each text slot, always output:
- `slot_id`
- `role`
- `text`
- `language`
- `position`
- `layout_relation`
- `replaceable`

Also capture weak or uncertain text honestly:
- mark tiny or stylized text with lower `ocr_confidence`
- use `review_needed: true` when the slot is visually ambiguous
- keep likely but uncertain microcopy separate from high-confidence main copy

Prefer these role values:
- `headline`
- `subtitle`
- `cta`
- `badge`
- `support_copy`

Prefer these position values when they fit:
- `top_left`
- `top_center`
- `top_right`
- `center_left`
- `center`
- `center_right`
- `bottom_left`
- `bottom_center`
- `bottom_right`
- `full_width_top`
- `full_width_bottom`

Use `layout_relation` to describe how the copy relates to the hero subject or nearby blocks, such as `above hero object`, `inside button area`, or `left of product`.

Read [references/text-slot-taxonomy.md](references/text-slot-taxonomy.md) for normalization rules.

## Prompt Rules

Use English as the default prompt language for model-facing output.

Also output a pure Chinese comparison prompt so the user can compare phrasing and reuse it in Chinese-first workflows.

Preserve original copy verbatim in `text_slots`. If the source image contains Chinese text:
- keep the Chinese text in the slot record
- mention in the English prompt that the image should render the exact Chinese text
- keep the Chinese comparison prompt fully in Chinese

Separate these concerns whenever possible:
- subject
- style
- layout
- size and aspect-ratio constraints
- color fidelity constraints
- lighting or texture
- typography or copy placement
- ornaments and faint graphic guides
- negative constraints

If the user names a target model, generate a model-specific prompt. In this skill, treat:
- `OpenAI Image` as `gpt-image-2`
- `Nano Banana 2` as the Google image-model target configured for the user's workflow

Read [references/prompt-rules.md](references/prompt-rules.md) and [references/model-notes.md](references/model-notes.md) before finalizing prompts.

## Color Fidelity

When the user wants closer reproduction, describe color with more discipline than generic phrases like `green background`.

Capture:
- dominant background hue
- hero object hue family
- typography color
- footer or accent block color
- whether the palette is flat, muted, warm, cool, olive, lime, cream, or desaturated

If possible, record a compact palette summary that can later be turned into exact tokens or sampled swatches.

## Ornament Handling

Treat faint lines, guide marks, footer shapes, translucent overlays, and decorative rules as first-class layout elements.

Do not merge them into generic layout prose when they materially affect the design.

When present, output ornament records with:
- type
- approximate position
- opacity strength
- color
- relation to nearby text or hero object

## Template Storage

Save reusable outputs as template objects whenever possible.

When a template store exists, update:
- template metadata
- keyword blocks
- prompt variants
- text slots
- revision history
- quality notes

Read [references/output-schema.md](references/output-schema.md) for field definitions.

## Revision Mode

When the user uploads a generated result, do not merely say it is "different." Identify concrete gaps such as:
- hero subject too small
- headline hierarchy weaker than reference
- background more cluttered than reference
- palette drift
- copy placement drift
- text rendering issues

Then produce:
- a concise differences list
- a revision strategy
- a revised prompt

Read [references/revision-playbook.md](references/revision-playbook.md) for common correction patterns.

## Self-Optimization

Treat each revision as new learning data.

When a revision succeeds or reveals a recurring failure mode:
- append the failure type to revision history
- record the correction strategy used
- note whether the correction appears model-specific

Prefer explicit, inspectable iteration over hidden automatic learning. The first version should evolve through saved history and reusable correction patterns.
