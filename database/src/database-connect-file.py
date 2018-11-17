import sqlite3

connection = sqlite3.connect('database.sqlite3')
connection.execute('SELECT * FROM users')
