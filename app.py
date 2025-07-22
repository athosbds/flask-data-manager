from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
def init_db():
    database = sqlite3.connect('users.db')
    database_cursor = database.cursor()
    database_cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name text NOT NULL, 
    age text NOT NULL,
    email VARCHAR(254) NOT NULL UNIQUE)''')
    database.commit()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/users')
def listar_usuarios():
    database = sqlite3.connect('users.db')
    database_cursor = database.cursor()
    database_cursor.execute("SELECT * FROM user")
    users = database_cursor.fetchall()
    return render_template('users.html', users=users)
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        database = sqlite3.connect('users.db')
        database_cursor = database.cursor()
        database_cursor.execute("INSERT INTO user(name, age, email) VALUES(?, ?, ?)", (name, age, email))
        database.commit()
        return redirect('/users')
    return render_template('register.html')
@app.route('/delete_all')
def delete_all():
    database = sqlite3.connect('users.db')
    database_cursor = database.cursor()
    database_cursor.execute("DELETE FROM user")
    database_cursor.execute("DELETE FROM sqlite_sequence WHERE name='user'")
    database.commit()
    return redirect('/users')
@app.route('/delete_id/<int:user_id>')
def delete_id(user_id):
    database = sqlite3.connect('users.db')
    database_cursor = database.cursor()
    database_cursor.execute("DELETE FROM user WHERE id = ?", (user_id,))
    database.commit()
    database.close()
    return redirect(url_for('listar_usuarios'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    database = sqlite3.connect('users.db')
    database_cursor = database.cursor()
    user = database_cursor.execute("SELECT * FROM user WHERE id= ?", (id,)).fetchone()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        database_cursor.execute("UPDATE user SET name = ?, age = ?, email = ? WHERE id = ?", (name, age, email, id))
        database.commit()
        database.close()
        return redirect('/users')
    database.close()
    return render_template('update.html', user=user)
if __name__ == "__main__":
    init_db()
    app.run(debug=True)