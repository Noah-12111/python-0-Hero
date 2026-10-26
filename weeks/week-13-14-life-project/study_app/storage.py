"""Week 13: read and write task data as JSON."""

import json
from pathlib import Path

from study_app.models import Task, task_from_dict

TASK_FILE = Path.home() / ".study_app_tasks.json"


def load_tasks() -> list[Task]:
    if not TASK_FILE.exists():
        return []

    try:
        raw_data = json.loads(TASK_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Cannot read task file: {error}") from error

    if not isinstance(raw_data, list):
        raise ValueError("Task file must contain a JSON list")

    tasks = []
    for item in raw_data:
        if not isinstance(item, dict) or "title" not in item:
            raise ValueError("Each saved task must be an object with a title")
        tasks.append(task_from_dict(item))
    return tasks


def save_tasks(tasks: list[Task]) -> None:
    data = [task.to_dict() for task in tasks]
    TASK_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
