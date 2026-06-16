# Platform Adapters

Use these adapters as thin host-specific wrappers around the shared workflow.

## Available Adapter Templates

- `templates/adapters/chatgpt.md`
- `templates/adapters/claude.md`
- `templates/adapters/gemini.md`
- `templates/adapters/generic-agent.md`

## Adapter Design Rules

- Keep the shared schema unchanged across platforms.
- Adjust only invocation style, platform terminology, and output framing.
- Avoid rewriting the core extraction logic per host.
- Reuse the same OCR and revision rules everywhere.

## Recommended Usage

- ChatGPT: use the adapter as project instructions or a reusable prompt starter.
- Claude: use the adapter as a project prompt or task template.
- Gemini: use the adapter as Gem instructions or a reusable system prompt.
- Generic agents: use the adapter as the top-level task contract while keeping the shared references beside it.

For every adapter, pair the host-specific prompt with:
- `references/output-schema.md`
- `references/prompt-rules.md`
- `references/text-slot-taxonomy.md`
- `references/revision-playbook.md`
- `references/ocr-automation.md` when OCR is available
