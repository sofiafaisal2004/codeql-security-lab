import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/user')
def get_user():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    username = request.args.get('username')
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return str(cursor.fetchall())
