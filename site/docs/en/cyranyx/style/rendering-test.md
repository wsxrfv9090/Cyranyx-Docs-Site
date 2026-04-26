# Rendering Test

This page tests Markdown, MyST, LaTeX, tables, code blocks, admonitions, cards, dropdowns, tabs, footnotes, and other common documentation formats.

## 1. Heading levels

The page title `# Rendering Test` is the only H1 on this page.

Use H2-H4 for normal documentation structure.

### H3 heading

Used for subsections.

#### H4 heading

Used for deeper local structure.

##### H5 heading

Usually avoid unless the page is very structured.

###### H6 heading

Usually avoid in normal documentation.

---

## 2. Paragraphs and inline styles

This is a normal paragraph. It should be readable for long technical explanations.

This sentence contains **bold text**, *italic text*, `inline code`, and a [local link](#1-heading-levels).

This sentence contains English terms with Chinese explanations: tokenizer（分词器/离散化器）, confidence interval（置信区间）, causal preprocessing（因果预处理）.

This sentence contains Chinese concepts with English translations: 批维度（batch dimension）, 独立同分布（i.i.d., independent and identically distributed）, 滚动窗口（rolling window）.

---

## 3. Unordered list

- Data layer
- Preprocessing layer
- Tokenization layer
- Modeling layer
- Evaluation layer
- Deployment layer

Nested list:

- Cyranyx
  - Documentation system
  - Visual system
  - Publishing workflow
- Exitok
  - Financial time-series modeling
  - Tokenizer experiments
  - API documentation

---

## 4. Ordered list

1. Define the content boundary.
2. Build the documentation site.
3. Check visual rendering.
4. Add structured navigation.
5. Add API reference.
6. Publish static HTML.

Nested ordered list:

1. Prepare data.
   1. Validate schema.
   2. Clean invalid rows.
   3. Persist processed output.
2. Train model.
   1. Load dataset.
   2. Run training loop.
   3. Save checkpoints.
3. Evaluate model.
   1. Compute metrics.
   2. Inspect failure modes.
   3. Generate report.

---

## 5. Task list

- [x] Create Python-first documentation prototype
- [x] Separate `docs/` content from `docs_conf/` configuration
- [x] Test Markdown rendering
- [ ] Migrate old Cyranyx color system
- [ ] Add publication script
- [ ] Add bilingual build strategy

---

## 6. Markdown table

| Component | Current role | Future direction |
| --- | --- | --- |
| `docs/` | Markdown content only | Cyranyx, Exitok, Research, API |
| `docs_conf/` | Sphinx configuration and build output | Theme, CSS, templates, build artifacts |
| `scripts/` | Build and publish entry points | Build, publish, validate links |
| `pyproject.toml` | Python dependency declaration | Keep docs stack reproducible |
| `README.md` | Project operation guide | Keep commands minimal and stable |

Alignment test:

| Left | Center | Right |
| :--- | :---: | ---: |
| alpha | beta | 1.234 |
| gamma | delta | 56.78 |
| epsilon | zeta | 9000 |

---

## 7. Definition list

Cyranyx
: A Python-first documentation and system-design project.

Exitok
: A financial time-series modeling and research-oriented Python project.

MyST
: A Markdown dialect that supports Sphinx directives, roles, math, cross references, and technical documentation features.

Sphinx
: A Python documentation generator that can build static HTML, PDF, ePub, and other documentation outputs.

---

## 8. Blockquote

> A documentation system should reduce cognitive overhead.
>
> If every visual adjustment requires direct frontend engineering, the documentation system is too expensive to maintain.

Nested quote:

> Outer quote.
>
> > Inner quote.
> >
> > Useful for quoted explanations or preserved notes.

---

## 9. Code blocks

Python:

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DocsBuildConfig:
    content_dir: str
    config_dir: str
    build_dir: str


def describe_config(config: DocsBuildConfig) -> str:
    return (
        f"content={config.content_dir}, "
        f"config={config.config_dir}, "
        f"build={config.build_dir}"
    )
```

PowerShell:

```powershell
uv sync --extra docs
uv run python scripts/build_docs.py
start .\docs_conf\build\html\index.html
```

TOML:

```toml
[project]
name = "cyranyx"
version = "0.1.0"
requires-python = ">=3.13"

[project.optional-dependencies]
docs = [
  "sphinx>=8,<9",
  "myst-parser>=4,<5",
  "furo>=2024.8.6",
  "sphinx-design>=0.6,<1",
]
```

JSON:

```json
{
  "project": "cyranyx",
  "docs_stack": ["sphinx", "myst-parser", "furo", "sphinx-design"],
  "python": ">=3.13"
}
```

---

## 10. Inline math

Daily log return:

$r_t = \log(P_t) - \log(P_{t-1})$

Causal z-score:

$z_t = \frac{x_t - \mu_t}{\sigma_t + \epsilon}$

Conditional probability:

$p_\theta(y_t \mid x_{\le t})$

---

## 11. Block LaTeX

Loss function:

$$
\mathcal{L}(\theta)
=
-\sum_{t=1}^{T}
\log p_\theta(y_t \mid x_{\le t})
$$

Causal exponential moving average:

$$
\mu_t
=
\alpha x_t + (1-\alpha)\mu_{t-1}
$$

Variance update:

$$
\sigma_t^2
=
\alpha (x_t - \mu_t)^2
+
(1-\alpha)\sigma_{t-1}^2
$$

Matrix shape check:

$$
X \in \mathbb{R}^{B \times T \times C}
$$

where:

- $B$ is batch size（批大小）;
- $T$ is sequence length（序列长度）;
- $C$ is channel count（通道数）.

---

## 12. Admonitions

```{note}
This is a note. Use it for neutral supporting information.
```

```{tip}
This is a tip. Use it for recommended workflows.
```

```{important}
This is important. Use it for constraints that should not be missed.
```

```{warning}
This is a warning. Use it for fragile steps, migration risks, or potentially destructive operations.
```

```{danger}
This is danger. Use it only when an operation can cause serious loss, such as deleting files or overwriting remote state.
```

```{seealso}
This is seealso. Use it for related pages or concepts.
```

---

## 13. Dropdown

```{dropdown} Click to expand implementation notes
This content is hidden by default.

Use dropdowns for optional details, long derivations, historical notes, or low-priority implementation explanations.
```

```{dropdown} Click to expand a math derivation
Starting from:

$$
r_t = \log(P_t) - \log(P_{t-1})
$$

we can write:

$$
r_t = \log\left(\frac{P_t}{P_{t-1}}\right)
$$

This is useful because log returns are additive over time.
```

---

## 14. Grid and cards

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} Content layer
`docs/`

Only Markdown content should live here.
:::

:::{grid-item-card} Configuration layer
`docs_conf/`

Sphinx configuration, static assets, templates, and build output.
:::

:::{grid-item-card} Operation layer
`scripts/`

Build, publish, and validation scripts.
:::

:::{grid-item-card} Dependency layer
`pyproject.toml`

Python version and docs dependencies.
:::

::::

---

## 15. Tabs

::::{tab-set}

:::{tab-item} English
Cyranyx is a Python-first documentation system.
:::

:::{tab-item} 中文
Cyranyx 是一个 Python-first 的文档系统。
:::

:::{tab-item} Notes
This tab test is only for local rendering checks. It is not the recommended long-term bilingual architecture.
:::

::::

---

## 16. Badges and buttons

Badges:

```{button-link} https://www.sphinx-doc.org/
:color: primary
:outline:
Sphinx
```

```{button-link} https://myst-parser.readthedocs.io/
:color: secondary
:outline:
MyST Parser
```

Button test:

```{button-link} ../index.html
:color: primary
Open local index
```

---

## 17. Images placeholder

No image is included yet.

Later, test:

```markdown
![Architecture diagram](../assets/architecture.png)
```

Recommended future path:

```text
docs/assets/
```

If an image is content-specific, keep it near the content page. If it is theme/static UI asset, keep it under `docs_conf/static/`.

---

## 18. Footnotes

This sentence has a footnote.[^first]

This sentence has another footnote.[^second]

[^first]: This is the first footnote.
[^second]: This is the second footnote, useful for citations or side notes.

---

## 19. Horizontal rule

Above the rule.

---

Below the rule.

---

## 20. Stress test paragraph

This paragraph is intentionally longer. It is used to check line width, font rendering, paragraph spacing, text contrast, and reading comfort. A documentation site for modeling, system design, and research notes must remain readable under long technical explanations. If the visual style is too bright, too dense, or too contrast-heavy, long-form reading will become tiring even if the page looks impressive at first glance.

---

## 21. Final checklist

- [ ] Headings are visually clear.
- [ ] Paragraphs are comfortable to read.
- [ ] Inline code is readable.
- [ ] Code blocks are readable.
- [ ] Tables are readable.
- [ ] LaTeX renders correctly.
- [ ] Admonitions render correctly.
- [ ] Cards render correctly.
- [ ] Tabs render correctly.
- [ ] Dropdowns render correctly.
- [ ] Links are visible.
- [ ] Current color style feels close enough to continue.
