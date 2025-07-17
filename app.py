from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)
def init_db():
    database = sqlite3.connect('users.db')
    database_cursor = database.cursor()
    database_cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name text NOT NULL, 
    age text NOT NULL)''')
    database.commit()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/users')
def listar_usuarios():
    database = sqlite3.connect('users.db')
    cursor = database.cursor()
    cursor.execute('SELECT * FROM user')
    users = cursor.fetchall()
    database.close()
    return render_template('usuarios.html', users=users)
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        database = sqlite3.connect('users.db')
        cursor = database.cursor()
        cursor.execute('INSERT INTO user (name, age) VALUES (?, ?)', (name, age))
        database.commit()
        database.close()
        return redirect('/users')
    return render_template('cadastrar.html')
@app.route('/delete_all')
def delete():
    database = sqlite3.connect('users.db')
    cursor = database.cursor()
    cursor.execute("DELETE FROM user")
    database.commit()
    database.close()
    return redirect('/users')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)