from __future__ import annotations

project = "Cyranyx Documentation"
author = "Davy"
copyright = "2026, Davy"

extensions = [
    "myst_parser",
    "sphinx_design",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
]

html_theme = "furo"
html_title = "Cyranyx Documentation"

html_static_path = ["_static"]
templates_path = ["_templates"]

html_css_files = [
    "cyranyx.css",
]

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#7c3aed",
        "color-brand-content": "#7c3aed",
    },
    "dark_css_variables": {
        "color-brand-primary": "#ff4fd8",
        "color-brand-content": "#ff4fd8",
        "color-background-primary": "#070812",
        "color-background-secondary": "#101225",
        "color-sidebar-background": "#090a16",
        "color-sidebar-background-border": "#2c1f46",
        "color-sidebar-link-text--top-level": "#f4eaff",
        "color-link": "#20f6ff",
        "color-link--hover": "#ff4fd8",
    },
}