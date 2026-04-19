import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/age')
def process_age():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    age_str = request.args.get('age')
    if not age_str or not age_str.isdigit():
        return 'Error: Age must be a whole number.'
    age = int(age_str)
    if not (1 <= age <= 120):
        return 'Age must be between 1 and 120.'
    query = "SELECT * FROM users WHERE age = ?"
    cursor.execute(query, (age,))
    return str(cursor.fetchall())
