"""Модель курса."""
class Course:
    def __init__(self, course_id: int, title: str):
        self.course_id = course_id
        self.title = title