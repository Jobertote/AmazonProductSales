from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def build_paths() -> dict[str, Path]:
    return {
        "root": ROOT,
        "data": ROOT / "data",
        "raw": ROOT / "data" / "raw",
        "processed": ROOT / "data" / "processed",
    }