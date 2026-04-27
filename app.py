from flask import Flask, render_template, request, redirect, url_for
import database as db
from datetime import datetime

app = Flask(__name__)
@app.route('/')
def index():
    day = request.args.get('day', datetime.now().strftime('%A'))
    return render_template('index.html', day=day, inwork=db.get_habits(day, 0), completed=db.get_habits(day, 1))

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    desc = request.form.get('desc', '')
    current = request.form.get('current_day', datetime.now().strftime('%A'))
    if request.form.get('all_days'):
        for d in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            db.add_habit(name, desc, d)
    else:
        day = request.form['day']
        if name and day:
            db.add_habit(name, desc, day)
    return redirect(url_for('index', day=current))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    current = request.form.get('current_day', datetime.now().strftime('%A'))
    db.update_habit(id, request.form['name'], request.form.get('desc', ''), request.form['day'])
    return redirect(url_for('index', day=current))

@app.route('/action/<string:act>/<int:id>')
def action(act, id):
    day = request.args.get('day', datetime.now().strftime('%A'))
    if act == 'delete':
        db.delete_habit(id)
    elif act == 'complete':
        db.complete_habit(id)
    elif act == 'restore':
        db.restore_habit(id)
    return redirect(url_for('index', day=day))

if __name__ == '__main__':
    db.init_db()
    app.run(debug=True)
