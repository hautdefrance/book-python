import sqlite3

with sqlite3.connect(':memory:') as db:
    db.execute('SELECT * FROM users')
