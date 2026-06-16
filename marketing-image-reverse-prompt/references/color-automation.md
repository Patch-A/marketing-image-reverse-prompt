# Color Automation

Use color sampling as a helper when palette fidelity matters.

## Goals

- capture dominant poster colors before writing prompts
- separate background, typography, hero-object, and footer tones
- reduce vague color wording such as `green background`
- support reuse across Codex and non-Codex hosts

## Bundled Script

Install optional dependencies:

```bash
pip install -r marketing-image-reverse-prompt/scripts/requirements.txt
```

Then run:

```bash
python marketing-image-reverse-prompt/scripts/sample_palette.py path/to/image.png -o palette.json
```

## Output Fields

- `image_size`
- `swatches`
- `dominant_hex`

Each swatch contains:
- `hex`
- `rgb`
- `ratio`

## Suggested Usage

1. sample the dominant palette
2. map swatches into `summary.color_fidelity`
3. decide which colors correspond to:
   - background
   - hero object
   - typography
   - footer or accent system
4. feed the clarified colors into prompt generation

## Notes

- Dominant palette sampling is a guide, not a semantic color parser.
- For posters with large solid backgrounds, the dominant swatch may mostly reflect the background color.
- For highly textured images, manually name the most important semantic colors even if the raw ratios differ.
