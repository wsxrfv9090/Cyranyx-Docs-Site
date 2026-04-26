# Cyranyx Color Check

This page is used to test the current Cyranyx visual system under the Sphinx + Furo + MyST stack.

It intentionally includes a small amount of inline HTML because Markdown alone cannot render color swatches. This file is a diagnostic page, not a normal writing template.

<style>
.color-grid {
  display: grid;
  grid-template-columns: minmax(180px, 260px) minmax(110px, 160px) 1fr;
  gap: 0.65rem 0.9rem;
  align-items: center;
  margin: 1rem 0 1.5rem 0;
}

.color-row {
  display: contents;
}

.color-name {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 0.92rem;
}

.color-value {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  opacity: 0.82;
}

.color-swatch {
  min-height: 2.2rem;
  border-radius: 0.8rem;
  border: 1px solid var(--cyranyx-border-hot);
  box-shadow: var(--cyranyx-glow-pink);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.35rem 0.65rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.preview-panel {
  border: 1px solid var(--cyranyx-border-hot);
  border-radius: 1rem;
  padding: 1rem;
  margin: 1rem 0;
  box-shadow: var(--cyranyx-glow-pink);
  background:
    linear-gradient(
      135deg,
      rgba(255, 79, 216, 0.08),
      rgba(32, 246, 255, 0.04)
    );
}

.preview-title {
  display: inline-flex;
  padding: 0.2rem 0.65rem;
  border: 1px solid var(--cyranyx-border-cyan);
  border-radius: 0.75rem;
  color: var(--cyranyx-accent-cyan);
  box-shadow: var(--cyranyx-glow-cyan);
  font-weight: 700;
}

.preview-chip {
  display: inline-block;
  margin: 0.15rem 0.25rem 0.15rem 0;
  padding: 0.12rem 0.48rem;
  border-radius: 0.6rem;
  border: 1px solid var(--cyranyx-border-hot);
  color: var(--cyranyx-accent-pink);
  background: rgba(255, 79, 216, 0.06);
}
</style>

## 1. Current Cyranyx design variables

These variables come from `docs_conf/static/cyranyx.css`.

<div class="color-grid">

<div class="color-row">
  <div class="color-name"><code>--cyranyx-bg-0</code></div>
  <div class="color-value"><code>#070812</code></div>
  <div class="color-swatch" style="background: var(--cyranyx-bg-0); color: var(--cyranyx-accent-pink);">background 0</div>
</div>

<div class="color-row">
  <div class="color-name"><code>--cyranyx-bg-1</code></div>
  <div class="color-value"><code>#101225</code></div>
  <div class="color-swatch" style="background: var(--cyranyx-bg-1); color: var(--cyranyx-accent-cyan);">background 1</div>
</div>

<div class="color-row">
  <div class="color-name"><code>--cyranyx-accent-pink</code></div>
  <div class="color-value"><code>#ff4fd8</code></div>
  <div class="color-swatch" style="background: var(--cyranyx-bg-1); color: var(--cyranyx-accent-pink);">accent pink</div>
</div>

<div class="color-row">
  <div class="color-name"><code>--cyranyx-accent-cyan</code></div>
  <div class="color-value"><code>#20f6ff</code></div>
  <div class="color-swatch" style="background: var(--cyranyx-bg-1); color: var(--cyranyx-accent-cyan);">accent cyan</div>
</div>

<div class="color-row">
  <div class="color-name"><code>--cyranyx-border-hot</code></div>
  <div class="color-value"><code>rgba(255, 79, 216, 0.42)</code></div>
  <div class="color-swatch" style="background: var(--cyranyx-bg-0); border: 2px solid var(--cyranyx-border-hot); color: var(--cyranyx-accent-pink);">hot border</div>
</div>

<div class="color-row">
  <div class="color-name"><code>--cyranyx-border-cyan</code></div>
  <div class="color-value"><code>rgba(32, 246, 255, 0.36)</code></div>
  <div class="color-swatch" style="background: var(--cyranyx-bg-0); border: 2px solid var(--cyranyx-border-cyan); color: var(--cyranyx-accent-cyan);">cyan border</div>
</div>

<div class="color-row">
  <div class="color-name"><code>--cyranyx-glow-pink</code></div>
  <div class="color-value"><code>0 0 24px rgba(255, 79, 216, 0.22)</code></div>
  <div class="color-swatch" style="background: var(--cyranyx-bg-1); color: var(--cyranyx-accent-pink); box-shadow: var(--cyranyx-glow-pink);">pink glow</div>
</div>

<div class="color-row">
  <div class="color-name"><code>--cyranyx-glow-cyan</code></div>
  <div class="color-value"><code>0 0 24px rgba(32, 246, 255, 0.16)</code></div>
  <div class="color-swatch" style="background: var(--cyranyx-bg-1); color: var(--cyranyx-accent-cyan); box-shadow: var(--cyranyx-glow-cyan);">cyan glow</div>
</div>

</div>

## 2. Preview panels

<div class="preview-panel">
  <span class="preview-title">Cyberpunk surface preview</span>

  <p>
    This panel checks whether the current surface color, border, glow, and text contrast feel close to the intended Cyranyx cyberpunk style.
  </p>

  <span class="preview-chip">modeling</span>
  <span class="preview-chip">tokenizer</span>
  <span class="preview-chip">time-series</span>
  <span class="preview-chip">docs-system</span>
</div>

<div class="preview-panel">
  <span class="preview-title">Link / inline code / emphasis preview</span>

  <p>
    This paragraph contains a <a href="#current-cyranyx-design-variables">local link</a>, some <code>inline_code</code>, some <strong>bold text</strong>, and some <em>italic text</em>.
  </p>
</div>

## 3. sphinx-design card check

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} Pink energy
This card checks the default `.sd-card` style from `cyranyx.css`.

It should show a soft pink border and glow.
:::

:::{grid-item-card} Cyan hover
Move the cursor over this card.

The hover state should shift toward cyan.
:::

:::{grid-item-card} Technical writing
Cards should remain readable for long technical text.

Use this card to check line height, text contrast, and visual density.
:::

:::{grid-item-card} Future design token
Later, old MkDocs cyberpunk variables can be mapped into the new `--cyranyx-*` token system.
:::

::::

## 4. Table color check

| Token | Role | Expected feeling |
|---|---|---|
| `--cyranyx-bg-0` | page/deep background | deep, dark, low-noise |
| `--cyranyx-bg-1` | secondary surface | dark blue-purple surface |
| `--cyranyx-accent-pink` | hot accent | cyberpunk energy |
| `--cyranyx-accent-cyan` | cold accent | neon technical contrast |
| `--cyranyx-border-hot` | card border | visible but not too noisy |
| `--cyranyx-glow-pink` | card glow | soft luminous frame |

## 5. Code block color check

```python
from __future__ import annotations

def estimate_signal_strength(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    return sum(abs(x) for x in values) / len(values)
```

```text
Expected:
- code block background should be readable
- inline code should not be too bright
- border radius should be visible
- text contrast should remain comfortable
```

## 6. Blockquote check

> This blockquote checks whether quoted technical notes feel visually distinct.
>
> It should not overpower the main text, but it should be easy to notice.

## 7. Final visual notes

Use this page to decide:

- whether the current color contrast is readable;
- whether the glow is too strong or too weak;
- whether cards feel like Cyranyx;
- whether code blocks are comfortable for long technical reading;
- whether the old MkDocs cyberpunk palette should be migrated as-is or simplified.