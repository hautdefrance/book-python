import sqlite3


SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        firstname TEXT,
        lastname TEXT)"""
SQL_INSERT = 'INSERT INTO astronauts VALUES (NULL, :pesel, :firstname, :lastname)'
SQL_SELECT = 'SELECT * FROM astronauts'


astronauts = [
    {'pesel': '61041212345', 'firstname': 'José', 'lastname': 'Jiménez'},
    {'pesel': '61041212346', 'firstname': 'Matt', 'lastname': 'Kowalski'},
    {'pesel': '61041212347', 'firstname': 'Melissa', 'lastname': 'Lewis'},
    {'pesel': '61041212348', 'firstname': 'Alex', 'lastname': 'Vogel'},
    {'pesel': '61041212349', 'firstname': 'Ryan', 'lastname': 'Stone'},
]


with sqlite3.connect(':memory:') as db:
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, astronauts)

    db.row_factory = sqlite3.Row

    for row in db.execute(SQL_SELECT):
        print(dict(row))

# {'id': 1, 'pesel': 61041212345, 'firstname': 'José', 'lastname': 'Jiménez'}
# {'id': 2, 'pesel': 61041212346, 'firstname': 'Matt', 'lastname': 'Kowalski'}
# {'id': 3, 'pesel': 61041212347, 'firstname': 'Melissa', 'lastname': 'Lewis'}
# {'id': 4, 'pesel': 61041212348, 'firstname': 'Alex', 'lastname': 'Vogel'}
# {'id': 5, 'pesel': 61041212349, 'firstname': 'Ryan', 'lastname': 'Stone'}
