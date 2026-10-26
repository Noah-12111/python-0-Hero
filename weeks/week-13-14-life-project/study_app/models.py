"""Week 14: classes and objects for study tasks."""


class Task:
    def __init__(self, title: str, done: bool = False):
        self.title = title
        self.done = done

    def complete(self) -> None:
        self.done = True

    def __str__(self) -> str:
        status = "x" if self.done else " "
        return f"[{status}] {self.title}"

    def to_dict(self) -> dict[str, object]:
        return {
            "kind": "task",
            "title": self.title,
            "done": self.done,
        }


class HomeworkTask(Task):
    """A homework item is a kind of task and also has a subject."""

    def __init__(self, title: str, subject: str, done: bool = False):
        super().__init__(title, done)
        self.subject = subject

    def __str__(self) -> str:
        return f"[{self.subject}] {super().__str__()}"

    def to_dict(self) -> dict[str, object]:
        data = super().to_dict()
        data["kind"] = "homework"
        data["subject"] = self.subject
        return data


def task_from_dict(data: dict[str, object]) -> Task:
    """Rebuild the correct task object from saved JSON data."""
    title = str(data["title"])
    done = bool(data.get("done", False))

    if data.get("kind") == "homework":
        return HomeworkTask(title, str(data.get("subject", "")), done)

    return Task(title, done)
