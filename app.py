from flask import Flask, render_template, request, redirect, url_for
import database as db

app = Flask(__name__)
@app.route('/')
def index():
    habits = db.get_all_habits()
    return render_template('index.html',habits=habits)
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    if name:
        db.add_habit(name)
    return redirect(url_for('index'))
@app.route('/update', methods=['POST'])
def update():
    habit_id = request.form['id']
    new_name = request.form['new_name']
    db.update_habit(habit_id, new_name)
    return redirect(url_for('index'))
@app.route('/delete/<habit_id>')
def delete(habit_id):
    habit_id = int(habit_id)
    db.delete_habit(habit_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.init_db()
    app.run(debug=True)
