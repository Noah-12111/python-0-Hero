"""Week 14: a manager that contains and uses Task objects (composition)."""

from study_app.models import Task


class TaskManager:
    def __init__(self, tasks: list[Task] | None = None):
        self.tasks = tasks if tasks is not None else []

    def add(self, task: Task) -> None:
        self.tasks.append(task)

    def show_all(self) -> None:
        if not self.tasks:
            print("No tasks yet. Add one with the 'add' command.")
            return

        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def complete(self, number: int) -> None:
        if number < 1 or number > len(self.tasks):
            raise IndexError("task number does not exist")
        self.tasks[number - 1].complete()
