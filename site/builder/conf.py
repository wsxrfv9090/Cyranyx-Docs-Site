from __future__ import annotations

import os


project = "Cyranyx Documentation"
author = "Davy"
copyright = "2026, Davy"

_current_lang = os.getenv("CYRANYX_DOCS_LANG", "en")
_language_titles = {
    "en": "Cyranyx Documentation",
    "zh": "Cyranyx 文档",
}

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
]

copybutton_prompt_text = r">>> |\.\.\. |\$ |PS [^>]+> "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = False

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

root_doc = "index"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
    "tasklist",
]

myst_enable_checkboxes = True
myst_heading_anchors = 4

html_show_sourcelink = False
html_permalinks = False

html_theme = "furo"
html_title = _language_titles.get(_current_lang, _language_titles["en"])
html_context = {
    "cyranyx_docs_lang": _current_lang,
}

html_static_path = ["static"]
templates_path = ["templates"]

html_css_files = [
    "cyranyx.css",
    "cyranyx-dark.css",
    "cyranyx-light.css",
    "cyranyx-auto.css",
    "lang-switch.css",
]

html_js_files = [
    "lang-switch.js",
]

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#b8003d",
        "color-brand-content": "#006f8f",
    },
    "dark_css_variables": {
        "color-brand-primary": "#ff0055",
        "color-brand-content": "#00ffc8",
        "color-link": "#00ffc8",
        "color-link--hover": "#00a2ff",
        "color-foreground-primary": "#ff8ba8",
        "color-foreground-secondary": "#be4e74",
        "color-foreground-muted": "#ff00557e",
        "color-foreground-border": "#ff00552a",
        "color-background-primary": "#101116",
        "color-background-secondary": "#0a0b0e",
        "color-background-hover": "#182333",
        "color-background-hover--transparent": "#ff005528",
        "color-background-border": "#ff00552a",
        "color-inline-code-background": "#140009",
        "color-inline-code-foreground": "#00ffc8",
        "color-inline-code-border": "#ff00552a",
        "color-api-name": "#00ffc8",
        "color-api-pre-name": "#ff0055",
        "color-api-paren": "#ff8ba8",
        "color-api-keyword": "#d57bff",
        "color-highlight-on-target": "#283593",
    },
}