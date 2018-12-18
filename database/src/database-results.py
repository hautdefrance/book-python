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
    {'pesel': '61041212346', 'firstname': 'Pan', 'lastname': 'Twardowski'},
    {'pesel': '61041212347', 'firstname': 'Melissa', 'lastname': 'Lewis'},
    {'pesel': '61041212348', 'firstname': 'Alex', 'lastname': 'Vogel'},
    {'pesel': '61041212349', 'firstname': 'Ryan', 'lastname': 'Stone'},
]


with sqlite3.connect(':memory:') as db:
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, astronauts)

    for row in db.execute(SQL_SELECT):
        print(row)

# (1, 61041212345, 'José', 'Jiménez')
# (2, 61041212346, 'Pan', 'Twardowski')
# (3, 61041212347, 'Melissa', 'Lewis')
# (4, 61041212348, 'Alex', 'Vogel')
# (5, 61041212349, 'Ryan', 'Stone')
