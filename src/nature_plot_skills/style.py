from __future__ import annotations

import matplotlib as mpl
import seaborn as sns


def set_nature_style() -> None:
    """Configure Matplotlib defaults for Nature-style figures."""
    sns.set_style("white")
    sns.set_context("paper", font_scale=1.0)

    rc_params = {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica"],
        "font.size": 6,
        "axes.labelsize": 7,
        "axes.titlesize": 8,
        "xtick.labelsize": 6,
        "ytick.labelsize": 6,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "legend.fontsize": 5,
        "legend.title_fontsize": 6,
        "axes.linewidth": 0.5,
        "xtick.major.width": 0.5,
        "ytick.major.width": 0.5,
        "xtick.major.size": 2,
        "ytick.major.size": 2,
        "lines.linewidth": 0.75,
        "axes.grid": False,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "savefig.dpi": 450,
        "savefig.transparent": False,
        "savefig.facecolor": "white",
        "savefig.edgecolor": "none",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": "black",
        "axes.labelcolor": "black",
        "xtick.color": "black",
        "ytick.color": "black",
        "text.color": "black",
    }

    mpl.rcParams.update(rc_params)


__all__ = ["set_nature_style"]