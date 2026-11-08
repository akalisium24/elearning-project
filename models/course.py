"""Модель курса."""


class Course:
    def __init__(self, course_id: int, title: str, description: str, status: str = "draft"):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.status = status

    def __repr__(self):
        return f"Course(id={self.course_id!r}, title={self.title!r})"

    def __eq__(self, other):
        return isinstance(other, Course) and self.course_id == other.course_id

    def __hash__(self):
        return hash(self.course_id)