# Cyranyx Docs Site

Python-first documentation site for Cyranyx.

## Setup

```powershell
uv sync --extra docs
```

## Build

```powershell
uv run python site\builder\scripts\build_docs.py
```

## Open

```powershell
start .\site\builder\build\html\index.html
```

or directly:

```powershell
start .\site\builder\build\html\en\index.html
```

## Structure

```text
site/
  docs/
    en/
      English Markdown content.
    zh/
      Chinese Markdown content.

  builder/
    Sphinx configuration, static assets, templates, build output,
    and site-specific scripts.
```

## Stack

- Sphinx
- MyST Parser
- Furo
- sphinx-design
- sphinx-copybutton

## Goal

Build a Python-first static documentation frontend for Cyranyx, including Cyranyx-native content and Exitok-related documentation.