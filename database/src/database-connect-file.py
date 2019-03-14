import sqlite3

with sqlite3.connect('database.sqlite3') as db:
    db.execute('SELECT * FROM users')
