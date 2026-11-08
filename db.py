"""Подключение к БД."""
import sqlite3

def get_connection(db_path: str = "elearning.db"):
    return sqlite3.connect(db_path)