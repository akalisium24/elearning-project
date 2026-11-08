"""Модуль работы с курсами."""
from courses.models import Course
from courses.service import CourseService

__all__ = ["Course", "CourseService"]