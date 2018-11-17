import sqlite3

connection = sqlite3.connect(':memory:')
connection.execute('SELECT * FROM users')
