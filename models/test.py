"""Модель теста."""


class Test:
    def __init__(self, test_id: int, lesson_id: int, title: str, time_limit: int = 0, pass_score: int = 60):
        self.test_id = test_id
        self.lesson_id = lesson_id
        self.title = title
        self.time_limit = time_limit
        self.pass_score = pass_score

    def __repr__(self):
        return f"Test(id={self.test_id!r}, title={self.title!r})"