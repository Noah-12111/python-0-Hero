"""Week 13: command-line interface for the study task manager."""

import argparse

from study_app.manager import TaskManager
from study_app.models import HomeworkTask, Task
from study_app.storage import load_tasks, save_tasks


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage your study tasks")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="add a task")
    add.add_argument("title", help="task title in quotes if it has spaces")
    add.add_argument("--subject", help="optional subject, e.g. Python")

    commands.add_parser("list", help="show all tasks")

    done = commands.add_parser("done", help="mark a task as complete")
    done.add_argument("number", type=int, help="task number shown by list")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        manager = TaskManager(load_tasks())

        if args.command == "add":
            if args.subject:
                task = HomeworkTask(args.title, args.subject)
            else:
                task = Task(args.title)
            manager.add(task)
            save_tasks(manager.tasks)
            print(f"Added: {task}")
            return 0

        if args.command == "list":
            manager.show_all()
            return 0

        if args.command == "done":
            manager.complete(args.number)
            save_tasks(manager.tasks)
            print(f"Marked task {args.number} as complete.")
            return 0

    except (OSError, ValueError, IndexError) as error:
        print(f"Error: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
