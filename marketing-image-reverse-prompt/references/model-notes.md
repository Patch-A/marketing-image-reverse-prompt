# Model Notes

Use these notes as working heuristics for prompt shaping.

## OpenAI Image

- User-facing label: `OpenAI Image`
- Canonical model id: `gpt-image-2`
- Treat this as the explicit OpenAI target for first-version prompt variants.

Prompt guidance:
- be direct and concrete
- describe layout and hierarchy explicitly
- keep text rendering instructions near the end, after scene and composition

## Nano Banana 2

- User-facing label: `Nano Banana 2`
- Canonical model id: `nano-banana-2`
- If a concrete internal API id is available in the implementation environment, map this user-facing label to that id without changing the visible label in user-facing output.

Prompt guidance:
- keep subject and composition constraints clear
- preserve a strong hero-object instruction
- restate major layout anchors if the model tends to drift

## Bilingual Output Policy

- English is the primary prompt language.
- Chinese is the comparison prompt language.
- Original slot text keeps its source language.

## Output Consistency

For both targets:
- preserve the same text slot inventory
- preserve the same normalized keyword blocks
- adapt wording rather than changing the creative intent
