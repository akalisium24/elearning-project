"""Точка входа приложения онлайн-обучения."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "E-learning project is running!"


if __name__ == "__main__":
    app.run(debug=True)