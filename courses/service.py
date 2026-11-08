"""Сервис курсов."""
class CourseService:
    def __init__(self, repo):
        self.repo = repo

    def create_course(self, course):
        # TODO: валидация
        return self.repo.add(course)