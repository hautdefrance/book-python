import sqlite3
from datetime import datetime, timezone


DATA = """4.3,3.0,1.1,0.1,0
5.8,4.0,1.2,0.2,0
5.7,4.4,1.5,0.4,1
5.4,3.9,1.3,0.4,2
5.1,3.5,1.4,0.3,1
5.7,3.8,1.7,0.3,0
5.1,3.8,1.5,0.3,0
5.4,3.4,1.7,0.2,1
5.1,3.7,1.5,0.4,0
4.6,3.6,1.0,0.2,0
5.1,3.3,1.7,0.5,2
4.8,3.4,1.9,0.2,0
5.0,3.0,1.6,0.2,1
5.0,3.4,1.6,0.4,2
5.2,3.5,1.5,0.2,1
5.2,3.4,1.4,0.2,2
4.7,3.2,1.6,0.2,0"""

SPECIES = {
    '0': 'setosa',
    '1': 'versicolor',
    '2': 'virginica',
}

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS iris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        species TEXT,
        datetime DATETIME,
        sepal_length REAL,
        sepal_width REAL,
        petal_length REAL,
        petal_width REAL
    )
"""

SQL_CREATE_INDEX = """
    CREATE INDEX IF NOT EXISTS
        iris_datetime_index ON iris (datetime);
"""

SQL_INSERT = """
    INSERT INTO iris VALUES (
        NULL,
        :species,
        :datetime,
        :sepal_length,
        :sepal_width,
        :petal_length,
        :petal_width
    )
"""

SQL_SELECT = 'SELECT * FROM iris ORDER BY datetime DESC'

data = []


for rekord in DATA.split():
    pomiary = rekord.split(',')

    data.append({
        'datetime': datetime.now(tz=timezone.utc),
        'sepal_length': float(pomiary[0]),
        'sepal_width': float(pomiary[1]),
        'petal_length': float(pomiary[2]),
        'petal_width': float(pomiary[3]),
        'species': SPECIES[pomiary[4]],
    })


with sqlite3.connect('iris.sqlite3') as db:
    db.row_factory = sqlite3.Row

    db.execute(SQL_CREATE_TABLE)
    db.execute(SQL_CREATE_INDEX)
    db.executemany(SQL_INSERT, data)

    for row in db.execute(SQL_SELECT):
        print(dict(row))

