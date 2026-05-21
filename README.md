# nature_plot_skills

Framework-agnostic agent skill assets for generating publication figures in a Nature-compatible style with Python, Seaborn, and Matplotlib.

## Note to human user

Give your agent the link to this repo and tell it to install the skill 😄

## Install from GitHub

```bash
pip install "git+https://github.com/fyng/nature_plot_skills.git"
```

## What this package ships

This repository ships prompt assets, not a plotting API. The installed package exposes:

- One opinionated skill for Nature-style publication figures.
- A tiny Python API for locating and reading packaged assets.
- A small CLI for printing the installed asset path, listing skills, or showing skill contents.

The package does not auto-register itself with Claude, Codex, Cursor, or GitHub Copilot. `pip install` only makes the skill available on disk. You still need to wire that asset into each tool's instruction or skills mechanism.

## Skill content

The bundled skill keeps the Nature-specific decisions in markdown, including layout rules, legend placement, accessibility expectations, statistical annotation guidance, and succinct Matplotlib enforcement requirements for fonts, ticks, line weights, backgrounds, editable vector text, and raster export resolution.

This package does not install Matplotlib or Seaborn for you. The skill tells the agent how to use those libraries when figure code is being written.

## Quick start

Show the installed asset directory:

```bash
python -m nature_plot_skills path
```

List bundled skills:

```bash
python -m nature_plot_skills list
```

Print the Nature figure skill:

```bash
python -m nature_plot_skills show nature_publication_figures
```

Use the Python API:

```python
from nature_plot_skills import asset_root, list_skills, read_skill

print(asset_root())
print(list_skills())
print(read_skill("nature_publication_figures"))
```

## Integration guidance

### GitHub Copilot

Use the skill text as repository instructions or a prompt asset. A practical pattern is to render the skill into a repo-local file that Copilot can read alongside your codebase:

```bash
python -m nature_plot_skills show nature_publication_figures > copilot-instructions.md
```

If you already maintain `copilot-instructions.md`, merge the skill content into the plotting section instead of replacing the file.

### Cursor

Load the skill into your project rules or custom instructions. The simplest path is to paste the rendered markdown into the rule that governs figure generation tasks:

```bash
python -m nature_plot_skills show nature_publication_figures
```

### Claude

Add the rendered skill text to the project instructions, system prompt, or any local skill mechanism you use around Claude. Keep the content verbatim where possible so the Nature-specific constraints survive summarization.

### Codex and other coding agents

Place the rendered skill text in the instruction surface the agent already reads, such as `AGENTS.md`, a repo policy file, or the system prompt used by your orchestration layer.
