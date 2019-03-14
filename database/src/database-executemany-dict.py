import sqlite3


SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        firstname TEXT,
        lastname TEXT)"""

SQL_INSERT_DICT = 'INSERT INTO astronauts VALUES (NULL, :pesel, :firstname, :lastname)'


list_of_dicts = [
    {'pesel': '61041212345', 'firstname': 'José', 'lastname': 'Jiménez'},
    {'pesel': '61041212346', 'firstname': 'Jan', 'lastname': 'Twardowski'},
    {'pesel': '61041212347', 'firstname': 'Melissa', 'lastname': 'Lewis'},
    {'pesel': '61041212348', 'firstname': 'Alex', 'lastname': 'Vogel'},
    {'pesel': '61041212349', 'firstname': 'Ryan', 'lastname': 'Stone'},
]


with sqlite3.connect(':memory:') as db:
    db.execute(SQL_CREATE_TABLE)

    try:
        db.executemany(SQL_INSERT_DICT, list_of_dicts)
    except sqlite3.IntegrityError:
        print('Pesel need to be UNIQUE')
