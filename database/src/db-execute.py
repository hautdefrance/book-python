import sqlite3


SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        firstname TEXT,
        lastname TEXT)"""


data = {'pesel': '61041212345', 'firstname': 'José', 'lastname': 'Jiménez'},


with sqlite3.connect(':memory:') as db:
    db.execute(SQL_CREATE_TABLE)

    try:
        db.execute('INSERT INTO astronauts VALUES (NULL, :pesel, :firstname, :lastname)', data)
    except sqlite3.IntegrityError:
        print('Pesel need to be UNIQUE')
