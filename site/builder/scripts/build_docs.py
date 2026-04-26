from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
BUILDER_DIR = SCRIPT_PATH.parents[1]
SITE_DIR = BUILDER_DIR.parent
REPO_ROOT = SITE_DIR.parent

DOCS_ROOT = SITE_DIR / "docs"
CONF_DIR = BUILDER_DIR
BUILD_ROOT = BUILDER_DIR / "build" / "html"

DEFAULT_LANG = "en"
LANGS = ("en", "zh")
LANG_LABELS = {"en": "English", "zh": "中文"}


def main() -> int:
    if BUILD_ROOT.exists():
        shutil.rmtree(BUILD_ROOT)

    languages = discover_languages()
    if DEFAULT_LANG not in languages:
        raise FileNotFoundError(DOCS_ROOT / DEFAULT_LANG / "index.md")

    print("[docs] building Cyranyx documentation site")
    print(f"[docs] repo_root : {REPO_ROOT}")
    print(f"[docs] site_dir  : {SITE_DIR}")
    print(f"[docs] config_dir: {CONF_DIR}")
    print(f"[docs] build_root: {BUILD_ROOT}")
    print(f"[docs] languages : {', '.join(languages)}")

    for lang in languages:
        build_language(lang)

    write_root_redirect(DEFAULT_LANG)
    write_language_map(languages)

    print(f"[docs] built: {BUILD_ROOT}")
    return 0


def discover_languages() -> list[str]:
    return [lang for lang in LANGS if (DOCS_ROOT / lang / "index.md").is_file()]


def build_language(lang: str) -> None:
    content_dir = DOCS_ROOT / lang
    build_dir = BUILD_ROOT / lang

    env = os.environ.copy()
    env["CYRANYX_DOCS_LANG"] = lang

    cmd = [
        sys.executable,
        "-m",
        "sphinx",
        "-b",
        "html",
        "-c",
        str(CONF_DIR),
        str(content_dir),
        str(build_dir),
    ]

    print(f"[docs:{lang}] content_dir: {content_dir}")
    print(f"[docs:{lang}] build_dir  : {build_dir}")
    print(f"[docs:{lang}] {' '.join(cmd)}")
    subprocess.run(cmd, check=True, env=env)


def write_root_redirect(default_lang: str) -> None:
    BUILD_ROOT.mkdir(parents=True, exist_ok=True)
    target = f"{default_lang}/index.html"
    content = (
        "<!doctype html>\n"
        "<html lang=\"en\">\n"
        "  <head>\n"
        "    <meta charset=\"utf-8\">\n"
        f"    <meta http-equiv=\"refresh\" content=\"0; url={target}\">\n"
        f"    <link rel=\"canonical\" href=\"{target}\">\n"
        "    <title>Cyranyx Documentation</title>\n"
        "  </head>\n"
        "  <body>\n"
        f"    <p>Redirecting to <a href=\"{target}\">Cyranyx Documentation</a>.</p>\n"
        "  </body>\n"
        "</html>\n"
    )
    (BUILD_ROOT / "index.html").write_text(content, encoding="utf-8")


def write_language_map(languages: list[str]) -> None:
    sources_by_lang = {lang: collect_markdown_sources(lang) for lang in languages}
    all_sources = sorted(set().union(*sources_by_lang.values()), key=lambda p: p.as_posix())

    lang_map: dict[str, str] = {}
    for lang in languages:
        for rel_source in all_sources:
            source_key = f"{lang}/{html_relpath_for_source(rel_source).as_posix()}"
            for target_lang in languages:
                if target_lang == lang:
                    continue
                target_source = rel_source
                if target_source not in sources_by_lang[target_lang]:
                    target_source = Path("index.md")
                target_value = f"{target_lang}/{html_relpath_for_source(target_source).as_posix()}"
                lang_map[source_key] = target_value

        for target_lang in languages:
            if target_lang != lang:
                lang_map[f"{lang}/"] = f"{target_lang}/index.html"
                lang_map[f"{lang}/index.html"] = f"{target_lang}/index.html"

    payload = {
        "default_language": DEFAULT_LANG,
        "languages": [{"code": lang, "label": LANG_LABELS.get(lang, lang)} for lang in languages],
        "map": lang_map,
    }
    encoded = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)

    for lang in languages:
        static_dir = BUILD_ROOT / lang / "_static"
        static_dir.mkdir(parents=True, exist_ok=True)
        (static_dir / "lang-map.json").write_text(encoded, encoding="utf-8")

    root_static_dir = BUILD_ROOT / "_static"
    root_static_dir.mkdir(parents=True, exist_ok=True)
    (root_static_dir / "lang-map.json").write_text(encoded, encoding="utf-8")

    print(f"[docs] wrote language map for: {', '.join(languages)}")


def collect_markdown_sources(lang: str) -> set[Path]:
    source_root = DOCS_ROOT / lang
    return {path.relative_to(source_root) for path in source_root.rglob("*.md") if path.is_file()}


def html_relpath_for_source(rel_source: Path) -> Path:
    return rel_source.with_suffix(".html")


if __name__ == "__main__":
    raise SystemExit(main())
