from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)
def init_db():
    database = sqlite3.connect
    database_cursor = database.cursor()
    database_cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY, 
    name text NOT NULL, 
    age text NOT NULL)''')
    database.commit()
@app.route('/')
def index():
    return render_template('index.html')
#ADD method
@app.route('/add', methods=['POST'])
# USERS METHOD
@app.route('/usuarios')

if __name__ == "__main__":
    app.run(debug=True)