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
   # lógica
    return render_template('users.html', users=users)
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        #lógica
        return redirect('/users')
    return render_template('register.html')
@app.route('/delete_all')
def delete():
    #lógica
    return redirect('/users')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)