from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


TESSERACT_LANG_FALLBACKS = ["chi_sim+eng", "chi_tra+eng", "eng"]


@dataclass
class OcrItem:
    text: str
    confidence: float | None
    bbox: list[float]
    review_needed: bool
    source: str


def normalize_bbox(points: list[list[float]]) -> list[float]:
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    left = min(xs)
    top = min(ys)
    width = max(xs) - left
    height = max(ys) - top
    return [round(left, 2), round(top, 2), round(width, 2), round(height, 2)]


def rapidocr_available() -> bool:
    try:
        from rapidocr_onnxruntime import RapidOCR  # noqa: F401
    except ImportError:
        return False
    return True


def run_rapidocr(image_path: Path, review_threshold: float) -> dict[str, Any]:
    from rapidocr_onnxruntime import RapidOCR

    engine = RapidOCR()
    result, _ = engine(image_path)
    items: list[OcrItem] = []

    for entry in result or []:
        points, text, score = entry
        text = str(text).strip()
        if not text:
            continue
        confidence = float(score) if score is not None else None
        items.append(
            OcrItem(
                text=text,
                confidence=confidence,
                bbox=normalize_bbox(points),
                review_needed=confidence is None or confidence < review_threshold,
                source="rapidocr",
            )
        )

    return {
        "engine": "rapidocr",
        "language": "auto",
        "items": [asdict(item) for item in items],
        "errors": [],
    }


def tesseract_available() -> bool:
    return shutil.which("tesseract") is not None


def run_tesseract_once(image_path: Path, lang: str, review_threshold: float) -> dict[str, Any]:
    if not tesseract_available():
        raise RuntimeError("tesseract not found on PATH")

    output_base = image_path.parent / f"{image_path.stem}.ocr"
    cmd = ["tesseract", str(image_path), str(output_base), "-l", lang, "tsv"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"tesseract exited with {result.returncode}")

    tsv_path = output_base.with_suffix(".tsv")
    rows = tsv_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    cleanup_tesseract_artifacts(output_base)

    if not rows:
        return {"engine": "tesseract", "language": lang, "items": [], "errors": []}

    headers = rows[0].split("\t")
    items: list[OcrItem] = []

    for line in rows[1:]:
        cols = line.split("\t")
        if len(cols) != len(headers):
            continue

        row = dict(zip(headers, cols, strict=True))
        if row.get("level") != "5":
            continue

        text = row.get("text", "").strip()
        if not text:
            continue

        raw_conf = row.get("conf", "-1")
        confidence = None if raw_conf in {"", "-1"} else float(raw_conf) / 100.0
        items.append(
            OcrItem(
                text=text,
                confidence=confidence,
                bbox=[
                    float(row.get("left", 0)),
                    float(row.get("top", 0)),
                    float(row.get("width", 0)),
                    float(row.get("height", 0)),
                ],
                review_needed=confidence is None or confidence < review_threshold,
                source="tesseract",
            )
        )

    return {
        "engine": "tesseract",
        "language": lang,
        "items": [asdict(item) for item in items],
        "errors": [],
    }


def cleanup_tesseract_artifacts(output_base: Path) -> None:
    for suffix in (".tsv", ".txt"):
        artifact = output_base.with_suffix(suffix)
        try:
            artifact.unlink()
        except OSError:
            pass


def extract(image_path: Path, engine_name: str, review_threshold: float) -> dict[str, Any]:
    errors: list[str] = []

    if engine_name in {"auto", "rapidocr"}:
        if rapidocr_available():
            try:
                return run_rapidocr(image_path, review_threshold)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"rapidocr: {exc}")
        elif engine_name == "rapidocr":
            errors.append("rapidocr: package not installed")

    if engine_name in {"auto", "tesseract"}:
        for lang in TESSERACT_LANG_FALLBACKS:
            try:
                result = run_tesseract_once(image_path, lang, review_threshold)
                result["errors"] = errors
                return result
            except Exception as exc:  # noqa: BLE001
                errors.append(f"tesseract[{lang}]: {exc}")

    return {
        "engine": None,
        "language": None,
        "items": [],
        "errors": errors or ["no OCR engine available"],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract OCR text from an image as JSON.")
    parser.add_argument("image", type=Path, help="Path to the source image.")
    parser.add_argument("-o", "--output", type=Path, help="Optional output JSON path.")
    parser.add_argument(
        "--engine",
        choices=["auto", "rapidocr", "tesseract"],
        default="auto",
        help="OCR engine preference. Defaults to auto.",
    )
    parser.add_argument(
        "--review-threshold",
        type=float,
        default=0.75,
        help="Confidence threshold below which OCR items are marked review_needed.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = extract(args.image, args.engine, args.review_threshold)
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
