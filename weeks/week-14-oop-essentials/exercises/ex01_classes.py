"""Exercise 01: class, object and methods."""


class Progress:
    """Lưu số bài đã hoàn thành và tính phần trăm tiến độ."""

    def __init__(self, completed: int, total: int):
        if total <= 0:
            raise ValueError("total must be positive")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


progress = Progress(3, 4)
print(progress.percentage())  # 75.0
print(progress)  # Progress: 3/4 (75%)
