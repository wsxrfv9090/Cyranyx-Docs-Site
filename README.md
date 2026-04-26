# Cyranyx Docs Site

Python-first documentation site for Cyranyx.

## Setup

```powershell
uv sync --extra docs
```

## Build

```powershell
uv run python scripts/build_docs.py
```

## Open

```powershell
start .\docs_conf\build\html\index.html
```

## Structure

```text
docs/
  Markdown content only.

docs_conf/
  Sphinx configuration, static assets, templates, and build output.

scripts/
  Build and publish scripts.
```

## Stack

- Sphinx
- MyST Parser
- Furo
- sphinx-design

## Goal

Build a Python-first documentation frontend for Cyranyx, including Cyranyx-native content and Exitok-related documentation.