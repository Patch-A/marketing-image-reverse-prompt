from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image


def rgb_to_hex(color: tuple[int, int, int]) -> str:
    return "#{:02X}{:02X}{:02X}".format(*color)


def load_image(image_path: Path, max_size: int = 512) -> Image.Image:
    image = Image.open(image_path).convert("RGB")
    image.thumbnail((max_size, max_size))
    return image


def sample_palette(image_path: Path, color_count: int) -> dict[str, object]:
    image = load_image(image_path)
    quantized = image.quantize(colors=color_count, method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette() or []
    total_pixels = image.width * image.height
    colors = quantized.getcolors() or []
    colors.sort(key=lambda item: item[0], reverse=True)

    swatches: list[dict[str, object]] = []
    for count, palette_index in colors[:color_count]:
        offset = palette_index * 3
        rgb = tuple(palette[offset : offset + 3])
        if len(rgb) != 3:
            continue
        swatches.append(
            {
                "hex": rgb_to_hex(rgb),  # type: ignore[arg-type]
                "rgb": list(rgb),
                "ratio": round(count / max(total_pixels, 1), 4),
            }
        )

    return {
        "image_size": {"width": image.width, "height": image.height},
        "swatches": swatches,
        "dominant_hex": swatches[0]["hex"] if swatches else None,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sample a compact dominant color palette from an image.")
    parser.add_argument("image", type=Path, help="Path to the source image.")
    parser.add_argument("-o", "--output", type=Path, help="Optional output JSON path.")
    parser.add_argument(
        "--colors",
        type=int,
        default=5,
        help="Number of dominant colors to extract. Defaults to 5.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = json.dumps(sample_palette(args.image, args.colors), ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
