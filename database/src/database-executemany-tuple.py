import sqlite3


SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        firstname TEXT,
        lastname TEXT)"""

SQL_INSERT_TUPLE = 'INSERT INTO astronauts VALUES (NULL, ?, ?, ?)'


list_of_tuples = [
    (61041212345, 'José', 'Jiménez'),
    (61041212346, 'Jan', 'Twardowski'),
    (61041212347, 'Melissa', 'Lewis'),
    (61041212348, 'Alex', 'Vogel'),
    (61041212349, 'Ryan', 'Stone'),
]


with sqlite3.connect(':memory:') as db:
    db.execute(SQL_CREATE_TABLE)

    try:
        db.executemany(SQL_INSERT_TUPLE, list_of_tuples)
    except sqlite3.IntegrityError:
        print('Pesel need to be UNIQUE')
