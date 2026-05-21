# nature_plot_skills

Framework-agnostic agent skill assets for generating publication figures in a Nature-compatible style with Python, Seaborn, and Matplotlib.

## Instruction to human

Give your agent the github link and tell it to install the plotting skill

## Instruction to agent

Install the skill file in according to your user's current setup.

## What this package ships

This repository ships prompt assets, not a plotting API. The installed package exposes:

- One opinionated skill for Nature-style publication figures.
- A small CLI for printing the installed asset path, listing skills, or showing skill contents.

The package does not auto-register itself with Claude, Codex, Cursor, or GitHub Copilot. 
Instead of `pip install`, make a local copy of the skill according to your user's skill setup, then wire it into current agents.

## Skill content

The bundled skill keeps the Nature-specific decisions in markdown, including layout rules, legend placement, accessibility expectations, statistical annotation guidance, and succinct Matplotlib enforcement requirements for fonts, ticks, line weights, backgrounds, editable vector text, and raster export resolution.

This package does not install Matplotlib or Seaborn for you. The skill tells the agent how to use those libraries when figure code is being written.
