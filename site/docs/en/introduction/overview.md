# System Overview

Cyranyx documentation is designed around three constraints:

1. Python-first configuration.
2. Markdown-first writing.
3. Minimal custom frontend code.

## Why this prototype exists

The goal is not to build a frontend application.  
The goal is to build a long-term maintainable technical documentation system.

## Design boundary

We prefer:

- theme configuration over custom CSS
- Sphinx extensions over custom JavaScript
- Markdown components over raw HTML
- static deployment over server maintenance

## Component Test

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} Python-first
Most site-level behavior should be controlled from `conf.py`.
:::

:::{grid-item-card} Markdown-first
Most content should be written in `.md` files using MyST Markdown.
:::

:::{grid-item-card} LaTeX-ready
Mathematical notes and model documentation should render cleanly.
:::

:::{grid-item-card} Static deploy
The final output should remain plain static HTML.
:::

::::