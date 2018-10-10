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
4.7,3.2,1.6,0.2,0""".split('\n')

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS iris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime DATETIME,
        sepal_length REAL,
        sepal_width REAL,
        petal_length REAL,
        petal_width REAL,
        species TEXT)"""

SQL_INSERT = """
    INSERT INTO iris VALUES (
        NULL,
        :datetime,
        :sepal_length,
        :sepal_width,
        :petal_length,
        :petal_width,
        :species)"""

SQL_SELECT = 'SELECT * FROM iris'

species = {
    0: 'setosa',
    1: 'virginica',
    2: 'versicolor'
}

with sqlite3.connect(':memory:') as db:
    db.execute(SQL_CREATE_TABLE)
    data = []

    for line in DATA:
        record = line.split(',')
        data.append({
            'datetime': datetime.now(tz=timezone.utc),
            'sepal_length': record[0],
            'sepal_width': record[1],
            'petal_length': record[2],
            'petal_width': record[3],
            'species': species[int(record[4])],
        })

    db.executemany(SQL_INSERT, data)

    db.row_factory = sqlite3.Row

    for row in db.execute(SQL_SELECT):
        print(dict(row))

# {'id': 1, 'datetime': '2018-10-10 13:37:16.661803+00:00', 'sepal_length': 4.3, 'sepal_width': 3.0, 'petal_length': 1.1, 'petal_width': 0.1, 'species': 'setosa'}
# {'id': 2, 'datetime': '2018-10-10 13:37:16.661815+00:00', 'sepal_length': 5.8, 'sepal_width': 4.0, 'petal_length': 1.2, 'petal_width': 0.2, 'species': 'setosa'}
# {'id': 3, 'datetime': '2018-10-10 13:37:16.661818+00:00', 'sepal_length': 5.7, 'sepal_width': 4.4, 'petal_length': 1.5, 'petal_width': 0.4, 'species': 'virginica'}
# {'id': 4, 'datetime': '2018-10-10 13:37:16.661820+00:00', 'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'versicolor'}
# {'id': 5, 'datetime': '2018-10-10 13:37:16.661822+00:00', 'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.3, 'species': 'virginica'}
# {'id': 6, 'datetime': '2018-10-10 13:37:16.661824+00:00', 'sepal_length': 5.7, 'sepal_width': 3.8, 'petal_length': 1.7, 'petal_width': 0.3, 'species': 'setosa'}
# {'id': 7, 'datetime': '2018-10-10 13:37:16.661826+00:00', 'sepal_length': 5.1, 'sepal_width': 3.8, 'petal_length': 1.5, 'petal_width': 0.3, 'species': 'setosa'}
# {'id': 8, 'datetime': '2018-10-10 13:37:16.661828+00:00', 'sepal_length': 5.4, 'sepal_width': 3.4, 'petal_length': 1.7, 'petal_width': 0.2, 'species': 'virginica'}
# {'id': 9, 'datetime': '2018-10-10 13:37:16.661830+00:00', 'sepal_length': 5.1, 'sepal_width': 3.7, 'petal_length': 1.5, 'petal_width': 0.4, 'species': 'setosa'}
# {'id': 10, 'datetime': '2018-10-10 13:37:16.661832+00:00', 'sepal_length': 4.6, 'sepal_width': 3.6, 'petal_length': 1.0, 'petal_width': 0.2, 'species': 'setosa'}
# {'id': 11, 'datetime': '2018-10-10 13:37:16.661834+00:00', 'sepal_length': 5.1, 'sepal_width': 3.3, 'petal_length': 1.7, 'petal_width': 0.5, 'species': 'versicolor'}
# {'id': 12, 'datetime': '2018-10-10 13:37:16.661836+00:00', 'sepal_length': 4.8, 'sepal_width': 3.4, 'petal_length': 1.9, 'petal_width': 0.2, 'species': 'setosa'}
# {'id': 13, 'datetime': '2018-10-10 13:37:16.661838+00:00', 'sepal_length': 5.0, 'sepal_width': 3.0, 'petal_length': 1.6, 'petal_width': 0.2, 'species': 'virginica'}
# {'id': 14, 'datetime': '2018-10-10 13:37:16.661840+00:00', 'sepal_length': 5.0, 'sepal_width': 3.4, 'petal_length': 1.6, 'petal_width': 0.4, 'species': 'versicolor'}
# {'id': 15, 'datetime': '2018-10-10 13:37:16.661842+00:00', 'sepal_length': 5.2, 'sepal_width': 3.5, 'petal_length': 1.5, 'petal_width': 0.2, 'species': 'virginica'}
# {'id': 16, 'datetime': '2018-10-10 13:37:16.661843+00:00', 'sepal_length': 5.2, 'sepal_width': 3.4, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'versicolor'}
# {'id': 17, 'datetime': '2018-10-10 13:37:16.661845+00:00', 'sepal_length': 4.7, 'sepal_width': 3.2, 'petal_length': 1.6, 'petal_width': 0.2, 'species': 'setosa'}
