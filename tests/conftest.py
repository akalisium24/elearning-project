import pytest
import sqlite3
from app import app as flask_app

@pytest.fixture
def app(tmp_path):
    """Создает тестовое приложение с временной БД."""
    flask_app.config.update({
        "TESTING": True,
        "DATABASE": str(tmp_path / "test.db")
    })
    
    # Инициализация схемы БД для тестов
    conn = sqlite3.connect(flask_app.config["DATABASE"])
    conn.executescript("""
        CREATE TABLE courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()
    
    yield flask_app

@pytest.fixture
def client(app):
    """Тестовый клиент для отправки HTTP-запросов."""
    return app.test_client()

@pytest.fixture
def db(app):
    """Соединение с тестовой БД."""
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()