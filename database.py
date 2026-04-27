import sqlite3

DB_NAME = 'habits.db'
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS habits (id INTEGER PRIMARY KEY, name TEXT, description TEXT, day TEXT, status INTEGER DEFAULT 0)')
def get_habits(day, status):
    conn = sqlite3.connect(DB_NAME)
    data = conn.execute('SELECT id, name, description, day FROM habits WHERE day=? AND status=?', (day, status)).fetchall()
    conn.close()
    return data
def add_habit(name, desc, day):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('INSERT INTO habits (name, description, day, status) VALUES (?,?,?,0)', (name, desc, day))
def update_habit(id, name, desc, day):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('UPDATE habits SET name=?, description=?, day=? WHERE id=?', (name, desc, day, id))
def delete_habit(id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('DELETE FROM habits WHERE id=?', (id,))
def complete_habit(id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('UPDATE habits SET status=1 WHERE id=?', (id,))
def restore_habit(id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('UPDATE habits SET status=0 WHERE id=?', (id,))
