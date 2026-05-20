from __future__ import annotations

from pathlib import Path


def asset_root() -> Path:
    return Path(__file__).resolve().parent / "assets"


def skills_root() -> Path:
    return asset_root() / "skills"


def list_skills() -> list[str]:
    root = skills_root()
    if not root.exists():
        return []
    return sorted(path.name for path in root.iterdir() if path.is_dir() and (path / "SKILL.md").exists())


def skill_path(name: str) -> Path:
    path = skills_root() / name / "SKILL.md"
    if not path.exists():
        raise FileNotFoundError(f"Unknown skill: {name}")
    return path


def read_skill(name: str) -> str:
    return skill_path(name).read_text(encoding="utf-8")