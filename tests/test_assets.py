from __future__ import annotations

import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from nature_plot_skills import asset_root, list_skills, read_skill, skill_path


class AssetTests(unittest.TestCase):
    def test_asset_root_exists(self) -> None:
        self.assertTrue(asset_root().is_dir())

    def test_skill_is_discoverable(self) -> None:
        self.assertIn("nature_publication_figures", list_skills())

    def test_skill_can_be_read(self) -> None:
        content = read_skill("nature_publication_figures")
        self.assertIn("Nature Publication Figures", content)
        self.assertIn("Must use concise publication defaults", content)
        self.assertIn("Must size figures in 1.5 inch by 1.5 inch units.", content)

    def test_skill_path_points_to_skill_markdown(self) -> None:
        self.assertEqual(skill_path("nature_publication_figures").name, "SKILL.md")


class CliTests(unittest.TestCase):
    def run_module(self, *args: str) -> subprocess.CompletedProcess[str]:
        env = dict(os.environ)
        env["PYTHONPATH"] = str(SRC)
        return subprocess.run(
            [sys.executable, "-m", "nature_plot_skills", *args],
            cwd=ROOT,
            env=env,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_cli_lists_skills(self) -> None:
        result = self.run_module("list")
        self.assertEqual(result.returncode, 0)
        self.assertIn("nature_publication_figures", result.stdout)

    def test_cli_prints_asset_path(self) -> None:
        result = self.run_module("path")
        self.assertEqual(result.returncode, 0)
        self.assertIn("nature_plot_skills/assets", result.stdout)

    def test_cli_prints_skill(self) -> None:
        result = self.run_module("show", "nature_publication_figures")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Must use concise publication defaults", result.stdout)
        self.assertIn("Must choose a statistical test", result.stdout)


if __name__ == "__main__":
    unittest.main()