from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
BUILDER_DIR = SCRIPT_PATH.parents[1]
SITE_DIR = BUILDER_DIR.parent
REPO_ROOT = SITE_DIR.parent

LANG = "en"

CONTENT_DIR = SITE_DIR / "docs" / LANG
CONF_DIR = BUILDER_DIR
BUILD_ROOT = BUILDER_DIR / "build" / "html"
BUILD_DIR = BUILD_ROOT / LANG


def main() -> int:
    if BUILD_ROOT.exists():
        shutil.rmtree(BUILD_ROOT)

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
    print(f"[docs] repo_root   : {REPO_ROOT}")
    print(f"[docs] site_dir    : {SITE_DIR}")
    print(f"[docs] content_dir : {CONTENT_DIR}")
    print(f"[docs] config_dir  : {CONF_DIR}")
    print(f"[docs] build_dir   : {BUILD_DIR}")
    print("[docs]", " ".join(cmd))

    subprocess.run(cmd, check=True)

    write_root_redirect()

    print(f"[docs] built: {BUILD_ROOT}")
    return 0


def write_root_redirect() -> None:
    BUILD_ROOT.mkdir(parents=True, exist_ok=True)

    index_html = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=en/index.html">
    <link rel="canonical" href="en/index.html">
    <title>Cyranyx Documentation</title>
  </head>
  <body>
    <p>Redirecting to <a href="en/">English documentation</a>.</p>
  </body>
</html>
"""

    (BUILD_ROOT / "index.html").write_text(index_html, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())