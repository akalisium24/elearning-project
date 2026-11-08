"""Тесты для CourseService."""
from courses import Course, CourseService

class FakeCourseRepository:
    def __init__(self):
        self.courses = []
    def add(self, course):
        self.courses.append(course)

def test_create_course():
    repo = FakeCourseRepository()
    service = CourseService(repo)
    service.create_course(Course(1, "Python"))
    assert len(repo.courses) == 1