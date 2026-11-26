"""Точка входа приложения онлайн-обучения."""
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = 'elearning.db'

def get_db():
    conn = sqlite3.connect(app.config.get('DATABASE', DATABASE))
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return "E-learning project is running!"

@app.route("/courses/", methods=['GET', 'POST'])
def courses():
    db = get_db()
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'title' not in data or not data['title']:
            return jsonify({"error": "Title is required"}), 400
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO courses (title) VALUES (?)", (data['title'],))
        db.commit()
        return jsonify({"id": cursor.lastrowid, "title": data['title']}), 201
    
    # GET
    cursor = db.execute("SELECT * FROM courses")
    courses = [dict(row) for row in cursor.fetchall()]
    return jsonify(courses), 200

if __name__ == "__main__":
    app.run(debug=True)