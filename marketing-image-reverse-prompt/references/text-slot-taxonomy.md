# Text Slot Taxonomy

Normalize extracted copy into reusable slots.

## Preferred Role Values

- `headline`: the main message or dominant title
- `subtitle`: the secondary message directly supporting the headline
- `cta`: the primary call to action
- `badge`: a small promotional label, sticker, or corner flag
- `support_copy`: tertiary supporting text, fine print, or small explanatory text

If a slot does not fit neatly, choose the closest role and explain ambiguity in a note.

## Preferred Position Values

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

Use the smallest accurate value set. Do not invent highly specific coordinates in the first version.

## Layout Relation Examples

- `above hero object`
- `below headline`
- `left of product`
- `inside button area`
- `overlapping background texture`
- `anchored to bottom footer band`

## Language Handling

For every slot, include:
- `text`
- `language`
- `replaceable`

Preserve the original language exactly. Do not auto-translate the source slot text.

## OCR Review

When OCR is uncertain, keep the candidate in a raw OCR list first, then promote it into `text_slots` only after visual confirmation. Mark it `review_needed: true` if the text is tiny, vertical, stylized, or partially occluded.
