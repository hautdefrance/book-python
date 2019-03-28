****************
Context Managers
****************


About Context Managers
======================

Zastosowanie
------------
* Pliki
* Buforowanie danych
* Połączenia do bazy danych
* Transakcje w bazie danych
* Cursory w bazie danych
* Lock
* Stream sieciowe
* Komunikacja po socketach

How to create
-------------
* ``__enter__(self, *args, **kwargs) -> self``
* ``__exit__(self, *args, **kwargs) -> None``

.. code-block:: python
    :caption: How to create Context Managers

    class MyClass:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def hello(self):
            print('hello')


    with MyClass() as cls:
        cls.hello()


Examples
========

Files
-----
.. code-block:: python

    f = open(FILE)
    # ...
    f.close()

.. code-block:: python

    with open(FILE) as file:
        # ...

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
        {'pesel': '61041212346', 'firstname': 'Jan', 'lastname': 'Twardowski'},
        {'pesel': '61041212347', 'firstname': 'Melissa', 'lastname': 'Lewis'},
        {'pesel': '61041212348', 'firstname': 'Alex', 'lastname': 'Vogel'},
        {'pesel': '61041212349', 'firstname': 'Ryan', 'lastname': 'Stone'},
    ]


    with sqlite3.connect(':memory:') as db:
        db.execute(SQL_CREATE_TABLE)
        db.executemany(SQL_INSERT, astronauts)

        for row in db.execute(SQL_SELECT):
            print(row)

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


Contextmanager decorator
========================
* Dzieli naszą funkcję na bloki przed i po ``yield``
* Bloki przed traktuje jako ``__enter__()``
* Bloki za traktuje jako ``__exit__()``

``contextmanager`` decorator
----------------------------
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

``ContextDecorator`` class
--------------------------
.. code-block:: python

    from contextlib import ContextDecorator


    class makeparagraph(ContextDecorator):
        def __enter__(self):
            print('<p>')
            return self

        def __exit__(self, *exc):
            print('</p>')


    @makeparagraph()
    def generate_html():
        print('Here is some non-HTML')

    generate_html()
    # <p>
    # Here is some non-HTML
    # </p>

timing
------
.. code-block:: python

    from contextlib import contextmanager
    import time


    @contextmanager
    def timeit(task_name):
        start = time.time()
        yield
        duration = time.time() - start
        print(f'{task_name} took {duration} seconds')


    def exec_as_process():
        return 9999 ** 1e99999999


    def exec_as_thread():
        return 9999 ** 1e99999999

    TRIES = int(1e8)

    with timeit("processes"):
        [exec_as_process() for _ in range(TRIES)]
    # processes took 15.236166954 seconds


    with timeit("threads"):
        [exec_as_thread() for _ in range(TRIES)]
    # threads took 0.11357998848 seconds


Assignments
===========

Buffered file
-------------
* Filename: ``context_manager_file.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min

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
