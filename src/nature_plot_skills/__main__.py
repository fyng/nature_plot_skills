from __future__ import annotations

import argparse
import sys

from ._assets import asset_root, list_skills, read_skill


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="nature-plot-skills",
        description="Inspect packaged Nature figure skill assets.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("path", help="Print the installed asset directory.")
    subparsers.add_parser("list", help="List bundled skill names.")

    show_parser = subparsers.add_parser("show", help="Print a bundled skill.")
    show_parser.add_argument("name", help="Skill name, for example nature_publication_figures.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "path":
        print(asset_root())
        return 0

    if args.command == "list":
        for name in list_skills():
            print(name)
        return 0

    if args.command == "show":
        try:
            print(read_skill(args.name))
        except FileNotFoundError as error:
            print(str(error), file=sys.stderr)
            return 1
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())