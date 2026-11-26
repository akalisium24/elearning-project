"""Интеграционные тесты работы с базой данных курсов."""
import pytest


@pytest.mark.integration
def test_course_repository_add_and_get(db):
    """Проверяем сохранение и чтение курса из БД."""
    db.execute(
        "INSERT INTO courses (title) VALUES (?)",
        ("Интеграционный курс",)
    )
    db.commit()

    cursor = db.execute(
        "SELECT * FROM courses WHERE title = ?",
        ("Интеграционный курс",)
    )
    row = cursor.fetchone()

    assert row is not None
    assert row["title"] == "Интеграционный курс"


@pytest.mark.integration
def test_course_update(db):
    """Проверяем обновление названия курса в БД."""
    db.execute(
        "INSERT INTO courses (title) VALUES (?)",
        ("Старый курс",)
    )
    db.commit()

    db.execute(
        "UPDATE courses SET title = ? WHERE title = ?",
        ("Новый курс", "Старый курс")
    )
    db.commit()

    cursor = db.execute(
        "SELECT * FROM courses WHERE title = ?",
        ("Новый курс",)
    )
    row = cursor.fetchone()

    assert row is not None
    assert row["title"] == "Новый курс"
