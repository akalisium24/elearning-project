"""Модульные тесты проверки доступа к курсам."""
import pytest
from services.course_access import get_course_access


@pytest.mark.unit
@pytest.mark.parametrize("is_paid, is_trial, expected", [
    (True, False, True),
    (False, True, True),
    (True, True, True),
    (False, False, False),
])
def test_get_course_access(is_paid, is_trial, expected):
    """Проверка всех комбинаций условий доступа к курсу."""
    assert get_course_access(is_paid, is_trial) == expected
