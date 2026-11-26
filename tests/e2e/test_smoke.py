"""Проверка запуска приложения онлайн-обучения."""
import pytest


@pytest.mark.e2e
def test_index_returns_200(client):
    """Проверяем доступность главной страницы."""
    response = client.get("/")

    assert response.status_code == 200
