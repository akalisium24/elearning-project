"""Сервис курсов."""


class CourseService:
    def __init__(self, repo):
        self.repo = repo

    def create_course(self, course):
        # TODO: валидация + вызов repo.add
        raise NotImplementedError