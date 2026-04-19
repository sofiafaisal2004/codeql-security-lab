import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ Vulnerable SQL (string formatting)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()

user_input = "admin' OR 1=1 --"
print(get_user(user_input))
