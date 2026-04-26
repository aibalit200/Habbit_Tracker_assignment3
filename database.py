import sqlite3
DB_NAME = 'habits.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS habits (id INTEGER PRIMARY KEY, name TEXT)')

def get_all_habits():
    conn = sqlite3.connect(DB_NAME)
    habits = conn.execute('SELECT * FROM habits').fetchall()
    conn.close()
    return habits

def add_habit(name):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('INSERT INTO habits (name) VALUES (?)', (name,))

def update_habit(habit_id, new_name):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('UPDATE habits SET name = ? WHERE id = ?', (new_name, habit_id))

def delete_habit(habit_id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('DELETE FROM habits WHERE id = ?', (habit_id,))