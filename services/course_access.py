"""Функция проверки доступа к курсу."""

def get_course_access(is_paid: bool, is_trial: bool) -> bool:
    """
    Возвращает True, если доступ разрешен.
    Доступ разрешен, если курс оплачен ИЛИ если это пробный период.
    """
    if is_paid or is_trial:
        return True
    return False