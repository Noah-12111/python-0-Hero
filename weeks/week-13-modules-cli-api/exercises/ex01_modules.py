"""Exercise 01: imports, modules and main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Print a small everyday example: moving toward a target."""
    action = choose_action(position=1, goal=4)
    print(f"Current position: 1, goal: 4, action: {action}")


if __name__ == "__main__":
    main()
