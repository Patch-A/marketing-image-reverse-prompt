# Output Schema

Use structured output whenever the task goes beyond casual brainstorming.

## Required Top-Level Sections

- `task`
- `model_targets`
- `summary`
- `subjects`
- `text_slots`
- `ornaments`
- `keyword_blocks`
- `prompt_variants`
- `template`

Add `differences`, `revision_strategy`, and `revised_prompt` for revision-mode tasks. Add OCR metadata when extraction is used.

## Core Shape

```json
{
  "task": "reverse_from_reference",
  "model_targets": [
    { "label": "OpenAI Image", "model_id": "gpt-image-2" },
    { "label": "Nano Banana 2", "model_id": "nano-banana-2" }
  ],
  "summary": {
    "scene_type": "marketing_poster",
    "marketing_intent": "seasonal product promotion",
    "style": ["clean commercial", "soft premium lighting"],
    "layout": ["top headline", "center hero subject", "bottom CTA"],
    "color_fidelity": {
      "background_hex": "#9CAF47",
      "hero_primary_hex": "#3D5421",
      "type_hex": "#F4F0D8",
      "footer_hex": "#2F3B1A",
      "palette_note": "muted olive green poster with warm off-white typography"
    },
    "size_constraints": {
      "aspect_ratio": "3:4",
      "orientation": "portrait",
      "canvas_size_px": {
        "width": 690,
        "height": 920
      },
      "safe_margins_norm": {
        "top": 0.04,
        "right": 0.05,
        "bottom": 0.06,
        "left": 0.05
      },
      "hero_scale_norm": 0.58,
      "footer_band_height_norm": 0.17
    }
  },
  "subjects": [
    {
      "name": "iced coffee cup",
      "role": "hero",
      "attributes": ["transparent cup", "ice cubes", "cream foam"]
    }
  ],
  "ocr": {
    "engine": "tesseract",
    "language": "chi_sim+eng",
    "items": [
      {
        "text": "headline",
        "confidence": 0.98,
        "bbox": [12, 18, 140, 30],
        "review_needed": false
      }
    ]
  },
  "text_slots": [
    {
      "slot_id": "headline",
      "role": "headline",
      "text": "夏日新品",
      "language": "zh",
      "position": "top_center",
      "layout_relation": "above hero object",
      "replaceable": true
    }
  ],
  "ornaments": [
    {
      "ornament_id": "diag_line_left",
      "type": "guide_line",
      "position": "upper_left_to_center",
      "color": "#F4F0D8",
      "opacity_strength": "medium",
      "bbox_norm": {
        "x": 0.06,
        "y": 0.19,
        "w": 0.18,
        "h": 0.24
      },
      "layout_relation": "diagonal line pointing toward the top headline block"
    }
  ],
  "keyword_blocks": {
    "subject": ["premium cold drink", "hero product", "centered product shot"],
    "style": ["minimal poster", "commercial branding", "premium lifestyle ad"],
    "layout": ["top headline", "clear visual hierarchy", "center composition"],
    "lighting": ["soft light", "gentle shadows", "subtle reflections"],
    "negative": ["no clutter", "no extra objects", "no distorted text"]
  },
  "prompt_variants": {
    "gpt-image-2": {
      "language": "en",
      "prompt": "..."
    },
    "nano-banana-2": {
      "language": "en",
      "prompt": "..."
    },
    "zh_comparison": {
      "language": "zh",
      "prompt": "..."
    }
  },
  "template": {
    "template_id": "tpl_001",
    "template_name": "summer-drink-poster",
    "scene_type": "marketing_poster",
    "editable_slots": ["headline"],
    "preserve_style": true,
    "preserve_layout": true,
    "revision_history": []
  }
}
```

## Field Rules

- Keep `text_slots[].text` exactly as it appears in the source image unless the user explicitly asks for rewritten copy.
- If OCR is used, retain raw OCR candidates in `ocr.items` and promote only reviewed text into `text_slots`.
- Keep `prompt_variants` separate by model.
- Always include the Chinese comparison prompt in `prompt_variants.zh_comparison`.
- Prefer short arrays of normalized tags over long prose paragraphs in `summary.style` and `summary.layout`.
- Include `summary.size_constraints` when layout fidelity matters.
- Include `summary.color_fidelity` when palette matching matters.
- Use `template.revision_history` to track iterative fixes.

## Revision Mode Additions

Add these fields in revision mode:

```json
{
  "differences": [
    "main subject too small",
    "headline emphasis weaker than reference"
  ],
  "revision_strategy": [
    "increase hero subject prominence",
    "strengthen top headline hierarchy"
  ],
  "revised_prompt": "..."
}
```

Make each difference concrete and actionable.

## OCR Notes

- Keep OCR candidates and final slots separate.
- Use `review_needed` for tiny, stylized, vertical, or ambiguous text.
- Record the OCR engine and language when available.
