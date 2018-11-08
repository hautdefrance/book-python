import sqlite3


SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS ping (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime DATETIME,
        host TEXT,
        port INTEGER)"""

SQL_INSERT = 'INSERT INTO ping VALUES (NULL, :datetime, :host, :port)'


with sqlite3.connect('injection.sqlite3') as db:
    db.execute(SQL_CREATE_TABLE)
    db.execute(SQL_INSERT, {
        'datetime': '2018-11-08T13:37:00Z',
        'host': '127.0.0.1',
        'port': 8080,
    })
