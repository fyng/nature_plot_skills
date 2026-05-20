from pathlib import Path

from setuptools import find_packages, setup


ROOT = Path(__file__).parent


setup(
    name="nature-plot-skills",
    version="0.1.0",
    description="Agent skill assets for Nature-style publication figures",
    long_description=(ROOT / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Feiyang Huang",
    license="MIT",
    python_requires=">=3.9",
    url="https://github.com/fyng/nature_plot_skills",
    project_urls={
        "Homepage": "https://github.com/fyng/nature_plot_skills",
        "Repository": "https://github.com/fyng/nature_plot_skills",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["matplotlib>=3.8", "seaborn>=0.13"],
    include_package_data=True,
    package_data={
        "nature_plot_skills": [
            "assets/*.md",
            "assets/skills/*.md",
            "assets/skills/*/*.md",
        ]
    },
    entry_points={
        "console_scripts": [
            "nature-plot-skills=nature_plot_skills.__main__:main",
        ]
    },
)