from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
BUILD_DIR = DOCS_DIR / "_build" / "html"


def main() -> int:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)

    cmd = [
        sys.executable,
        "-m",
        "sphinx",
        "-b",
        "html",
        str(DOCS_DIR),
        str(BUILD_DIR),
    ]

    print("[docs] building Sphinx site")
    print("[docs]", " ".join(cmd))

    subprocess.run(cmd, check=True)

    print(f"[docs] built: {BUILD_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())