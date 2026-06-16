# Tool Portability

The `SKILL.md` wrapper is Codex-native, but the underlying workflow is portable.

## Portability Strategy

Separate the repository into two layers:

1. Host adapter:
   - Codex skill
   - ChatGPT project instructions
   - Claude project prompt
   - Gemini Gem or system prompt
   - agent framework wrapper
2. Core payload:
   - output schema
   - OCR extraction result
   - text-slot taxonomy
   - prompt assembly rules
   - revision playbook

## What Should Stay Tool-Agnostic

- `text_slots`
- `keyword_blocks`
- `prompt_variants`
- `ornaments`
- `template`
- `ocr`

## What Usually Needs Adapters

- invocation syntax
- file upload conventions
- tool-call permissions
- storage paths
- model naming aliases

## Recommended Packaging

When supporting multiple AI tools, keep one shared schema and maintain small adapter prompts per host instead of rewriting the whole workflow for each platform.

Use the bundled adapter templates in `templates/adapters/` as thin wrappers around the shared schema.
