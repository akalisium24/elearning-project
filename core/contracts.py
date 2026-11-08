"""Контракты между модулями."""
from typing import Protocol

class CourseRepository(Protocol):
    def add(self, course): ...