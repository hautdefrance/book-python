import sqlite3

with sqlite3.connect('database.sqlite3') as connection:
    connection.execute('SELECT * FROM users')
