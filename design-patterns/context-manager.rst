****************
Context Managers
****************


About Context Managers
======================

How to create
-------------
* ``__enter__()``
* ``__exit__()``

.. literalinclude:: src/context-manager-create.py
    :language: python
    :caption: How to create Context Managers

Zastosowanie
------------
* Pliki
* Połączenia do bazy danych
* Lock
* Stream siecowe

Przykład
--------
.. code-block:: python

    f = open(FILE)
    # ...
    f.close()

.. code-block:: python

    with open(FILE) as file:
        # ...

Lock
----
.. code-block:: python

    import threading


    lock = threading.Lock()

    with lock:
        my_list.append(item)

replaces the more verbose:

.. code-block:: python

    import threading


    lock = threading.Lock()
    lock.acquire()

    try:
        my_list.append(item)
    finally:
        lock.release()

Database
--------
.. code-block:: python

    import sqlite3


    SQL_CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS astronauts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pesel INTEGER UNIQUE,
            firstname TEXT,
            lastname TEXT)"""
    SQL_INSERT = 'INSERT INTO astronauts VALUES (NULL, :pesel, :firstname, :lastname)'
    SQL_SELECT = 'SELECT * from astronauts'


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

        for row in db.execute(SQL_SELECT):
            print(row)

Contextmanager decorator
========================
.. code-block:: python

    from contextlib import contextmanager

    @contextmanager
    def tag(name):
        print(f"<{name}>")
        yield
        print(f"</{name}>")

    with tag("p"):
        print("foo")

    # <p>
    # foo
    # </p>

Dzieli naszą funkcję na bloki przed i po ``yield``.

- Bloki przed traktuje jako ``__enter__()``
- Bloki za traktuje jako ``__exit__()``

.. code-block:: python

    from contextlib import ContextDecorator

    class makeparagraph(ContextDecorator):
        def __enter__(self):
            print('<p>')
            return self

        def __exit__(self, *exc):
            print('</p>')
            return False

    @makeparagraph()
    def generate_html():
        print('Here is some non-HTML')

    generate_html()

.. code-block:: html

    <p>
    Here is some non-HTML
    </p>

timing
------
.. code-block:: python

    from contextlib import contextmanager
    import time


    @contextmanager
    def time_print(task_name):
        start = time.time()

        try:
            yield
        finally:
            duration = time.time() - start
            print(f'{task_name} took {duration} seconds')


    with time_print("processes"):
        [doproc() for _ in range(500)]
    # processes took 15.236166954 seconds


    with time_print("threads"):
        [dothread() for _ in range(500)]
    # threads took 0.11357998848 seconds


Assignments
===========

Buffered file
-------------
#. Stwórz Context Manager dla zapisu do plików
#. Context Manager buforuje dane (nie zapisuje ich na bieżąco
#. Gdy program wyjdzie z bloku context managera, to nastąpi zapisanie do pliku

.. code-block:: python

    FILE = '/tmp/context-manager.txt'

    class File:
        pass


    with File(FILENAME) as file:
        file.append_line(...)
        file.append_line(...)
        file.append_line(...)

    # after block with exits, save to file
