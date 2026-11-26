"""Сквозные тесты сценариев онлайн-обучения."""
import pytest


@pytest.mark.e2e
def test_get_courses_empty(client):
    """Проверяем получение пустого каталога курсов."""
    response = client.get("/courses/")

    assert response.status_code == 200
    assert response.get_json() == []


@pytest.mark.e2e
def test_create_course_success(client):
    """Проверяем успешное создание нового курса."""
    payload = {"title": "Python для начинающих"}

    response = client.post("/courses/", json=payload)

    assert response.status_code == 201
    assert response.get_json()["title"] == "Python для начинающих"


@pytest.mark.e2e
def test_create_course_invalid(client):
    """Проверяем отказ при создании курса с пустым названием."""
    payload = {"title": ""}

    response = client.post("/courses/", json=payload)

    assert response.status_code == 400
