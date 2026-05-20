---
name: nature_publication_figures
description: Use when generating or revising publication figures in Python for a Nature-style manuscript.
---

# Nature Publication Figures

Import and run `from nature_plot_skills import set_nature_style; set_nature_style()` before generating or revising Nature-style figures.

## Stack

- Must use Python plotting code.
- Must prefer Matplotlib and Seaborn.
- Consider raster layers only when the content is intrinsically image-based.

## Layout

- Must size figures in 1.5 inch by 1.5 inch units.
- Must keep total width within 5 units and total height within 7 units.
- Consider 2 or 3 width units when category labels are dense or rotated.
- Consider the full 5-unit width for dense heatmaps or multi-panel comparisons that would otherwise become unreadable.
- Must share one legend across subplots when the mapping is the same.
- Must place legends above the plot in a single row when there are fewer than 5 legend entries.
- Must place legends to the right in a single column when there are more than 5 legend entries.
- Never add an overall title.
- Never add methodological descriptions inside the figure.
- Consider terse subplot subtitles only when panel differences are not obvious from axes and labels.
- Must label multi-panel figures with bold lowercase panel letters.

## Graph rules

- Must include axis lines and tick marks.
- Must label every axis and put units in parentheses.
- Must use an accessible palette with strong contrast under color-vision deficiency.
- Never add decorative icons, drop shadows, or patterns.
- Never use colored text to encode groups; use marks, boxes, or keylines instead.
- Consider direct labeling only when it reduces eye travel more than a legend would.

## Text and annotation

- Must keep all text editable.
- Panel letters should be 8 pt bold.
- Never outline text.
- Never place text on busy backgrounds.
- Never allow labels to overlap each other or the plotted data.
- Must use black text with keylines or swatches instead of colored label text.
- Consider `textalloc` for scatter labels, dense point annotations, and any direct-label layout that would otherwise overlap.

## Statistics

- Consider whether the figure is making an inferential comparison rather than only showing descriptive structure.
- Must choose a statistical test that matches the design, sample pairing, distributional assumptions, and number of groups.
- Must correct multiple hypothesis tests with FDR.
- Must annotate significance in a restrained Nature-style form, using brackets or compact comparison marks rather than prose.
- Never add significance marks without naming the underlying test and correction in the caption or accompanying text.

## Export

- Must export line art, text, arrows, boxes, and scale bars as editable vector elements.
- Must prefer PDF or EPS for final vector export.
- Must keep artwork in RGB color space.

## Agent behavior

- When asked for a publication figure, Consider whether a simpler chart form communicates the claim more clearly.
- When many categories or annotations compete for space, Must solve readability first, even if that means expanding the figure to more size units or splitting into panels.
- Never optimize for decorative style over legibility, editability, and export correctness.