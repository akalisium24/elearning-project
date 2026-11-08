"""Репозиторий курсов."""


class CourseRepository:
    def __init__(self, conn):
        self.conn = conn

    def add(self, course):
        # TODO: реализовать сохранение курса в БД
        raise NotImplementedError

    def get_by_id(self, course_id):
        # TODO: реализовать получение курса по id
        raise NotImplementedError