"""Репозиторий тестов."""


class TestRepository:
    def __init__(self, conn):
        self.conn = conn

    def add(self, test):
        # TODO: реализовать сохранение теста в БД
        raise NotImplementedError