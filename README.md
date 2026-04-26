# Cyranyx Docs Prototype

Python-first documentation prototype for Cyranyx.

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
start .\docs\_build\html\index.html
```

## Stack

- Sphinx
- MyST Parser
- Furo
- sphinx-design

## Goal

Validate whether Cyranyx documentation can move from a frontend-heavy MkDocs/Material setup to a Python-first documentation workflow.