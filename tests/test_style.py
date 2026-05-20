from __future__ import annotations

import sys
import unittest
from pathlib import Path

import matplotlib as mpl


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from nature_plot_skills import set_nature_style


class StyleTests(unittest.TestCase):
    def test_style_helper_is_importable_from_package_root(self) -> None:
        self.assertTrue(callable(set_nature_style))

    def test_style_helper_updates_representative_rcparams(self) -> None:
        original_font_size = mpl.rcParams["font.size"]
        original_pdf_fonttype = mpl.rcParams["pdf.fonttype"]
        original_axes_grid = mpl.rcParams["axes.grid"]

        try:
            set_nature_style()

            self.assertEqual(mpl.rcParams["font.family"], ["sans-serif"])
            self.assertEqual(mpl.rcParams["font.sans-serif"][:2], ["Arial", "Helvetica"])
            self.assertEqual(mpl.rcParams["font.size"], 6)
            self.assertEqual(mpl.rcParams["axes.labelsize"], 7)
            self.assertEqual(mpl.rcParams["xtick.direction"], "out")
            self.assertEqual(mpl.rcParams["axes.grid"], False)
            self.assertEqual(mpl.rcParams["pdf.fonttype"], 42)
            self.assertEqual(mpl.rcParams["savefig.dpi"], 450)
            self.assertEqual(mpl.rcParams["figure.facecolor"], "white")
        finally:
            mpl.rcParams["font.size"] = original_font_size
            mpl.rcParams["pdf.fonttype"] = original_pdf_fonttype
            mpl.rcParams["axes.grid"] = original_axes_grid


if __name__ == "__main__":
    unittest.main()