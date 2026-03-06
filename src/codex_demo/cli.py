"""CLI entry point for the Codex demo project."""

from __future__ import annotations

import argparse

from .core import calculate_stats, greet


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Codex Python capability demo")
    parser.add_argument("--name", default="World", help="Name to greet")
    parser.add_argument(
        "--numbers",
        nargs="*",
        type=float,
        help="Optional list of numbers to summarize",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    print(greet(args.name))
    if args.numbers:
        stats = calculate_stats(args.numbers)
        print(
            "Stats -> "
            f"count: {int(stats['count'])}, "
            f"sum: {stats['sum']}, "
            f"avg: {stats['average']:.2f}, "
            f"median: {stats['median']}, "
            f"min: {stats['min']}, "
            f"max: {stats['max']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
