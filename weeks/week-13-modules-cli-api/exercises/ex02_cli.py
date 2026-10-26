"""Exercise 02: add one argparse option to a small CLI."""

import argparse


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Demo CLI for a study turn"
    )
    result.add_argument(
        "--turn",
        type=int,
        required=True,
        help="current turn number",
    )
    return result


def main() -> None:
    """Parse learner arguments and display the resulting namespace."""
    args = parser().parse_args()
    print(f"Current turn: {args.turn}")


if __name__ == "__main__":
    main()
