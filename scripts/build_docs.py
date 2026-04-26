from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

CONTENT_DIR = REPO_ROOT / "docs"
CONF_DIR = REPO_ROOT / "docs_conf"
BUILD_DIR = CONF_DIR / "build" / "html"


def main() -> int:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)

    cmd = [
        sys.executable,
        "-m",
        "sphinx",
        "-b",
        "html",
        "-c",
        str(CONF_DIR),
        str(CONTENT_DIR),
        str(BUILD_DIR),
    ]

    print("[docs] building Sphinx site")
    print(f"[docs] content_dir : {CONTENT_DIR}")
    print(f"[docs] config_dir  : {CONF_DIR}")
    print(f"[docs] build_dir   : {BUILD_DIR}")
    print("[docs]", " ".join(cmd))

    subprocess.run(cmd, check=True)

    print(f"[docs] built: {BUILD_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())