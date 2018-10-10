*********
Databases
*********

SQL Syntax
==========
.. note:: For SQL Syntax refer to :ref:`SQL`

DB API
======
* Database API in Python


``sqlite3``
===========

Connection
----------
.. literalinclude:: src/db-connect-memory.py
    :language: python
    :caption: Connection to in-memory database

.. literalinclude:: src/db-connect-file.py
    :language: python
    :caption: Connection to database file

.. literalinclude:: src/db-connect-context-manager.py
    :language: python
    :caption: Connection

Execute and executemany
-----------------------
.. literalinclude:: src/db-execute.py
    :language: python
    :caption: Execute

.. literalinclude:: src/db-execute-many.py
    :language: python
    :caption: Execute many

Results
-------
.. literalinclude:: src/db-results.py
    :language: python
    :caption: Results

.. literalinclude:: src/db-results-dict.py
    :language: python
    :caption: Results with ``dict``

Cursor
------
.. literalinclude:: src/db-results-cursor.py
    :language: python
    :caption: Results with cursor


``pyMySQL``
===========
.. code-block:: console

    $ pip install PyMySQL

.. literalinclude:: src/db-pymysql.py
    :language: python
    :caption: PyMySQL


``psycopg2``
============
* http://initd.org/psycopg/
* http://initd.org/psycopg/docs/usage.html

.. code-block:: console

    $ pip install psycopg2

.. literalinclude:: src/db-psycopg2.py
    :language: python
    :caption: Psycopg2


``pymongo``
===========
* http://api.mongodb.com/python/current/tutorial.html

.. code-block:: console

    $ pip install pymongo

.. code-block:: python

    import datetime
    from pymongo import MongoClient

    client = MongoClient('mongodb://localhost:27017/')
    db = client.test_database
    posts = db.posts

    data = {
        "name": "José Jiménez",
        "catchphrase": "My name... José Jiménez",
        "tags": ["astronaut", "nasa", "space"],
        "date": datetime.datetime.utcnow()
    }

    posts.insert_one(data).inserted_id
    # ObjectId('...')

.. code-block:: python

    for post in posts.find():
        print(post)

    for post in posts.find({"author": "Mike"}):
        print(post)

``SQLAlchemy``
==============

``Django ORM``
==============


Data exploration
================
* https://superset.incubator.apache.org/

.. code-block:: console

    # Install superset
    pip install superset

    # Create an admin user (you will be prompted to set username, first and last name before setting a password)
    fabmanager create-admin --app superset

    # Initialize the database
    superset db upgrade

    # Load some data to play with
    superset load_examples

    # Create default roles and permissions
    superset init

    # Start the web server on port 8088, use -p to bind to another port
    superset runserver

    # To start a development web server, use the -d switch
    # superset runserver -d

:superset_config.py:
    .. code-block:: python

        import os

        #---------------------------------------------------------
        # Superset specific config
        #---------------------------------------------------------
        ROW_LIMIT = 5000
        SUPERSET_WORKERS = 4

        SUPERSET_WEBSERVER_PORT = 8088
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Flask App Builder configuration
        #---------------------------------------------------------
        # Your App secret key
        SECRET_KEY = '\2\1secretkey\1\2\e\y\y\h'

        # The SQLAlchemy connection string to your database backend
        # This connection defines the path to the database that stores your
        # superset metadata (slices, connections, tables, dashboards, ...).
        # Note that the connection information to connect to the datasources
        #you want to explore are managed directly in the web UI
        SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_GREEN_URL', None)

        # Flask-WTF flag for CSRF
        WTF_CSRF_ENABLED = True
        # Add endpoints that need to be exempt from CSRF protection
        WTF_CSRF_EXEMPT_LIST = []

        # Set this API key to enable Mapbox visualizations
        MAPBOX_API_KEY = ''


.. code-block:: console

    gunicorn \
        -w 10 \
        -k gevent \
        --timeout 120 \
        -b  0.0.0.0:6666 \
        --limit-request-line 0 \
        --limit-request-field_size 0 \
        --statsd-host localhost:8125 \
        superset:app


Case Study
==========
.. literalinclude:: src/database-case-study.py
    :name: listing-database-case-study
    :language: python
    :caption: Zapisywanie do bazy danych wyników pobranych z sensorów podłączonych po USB


Assignments
===========

Iris Database
---------------------
* https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv

#. Bazę pomiarów Irysów przekonwertuj na tabelę w ``sqlite3``
#. Nazwy poszczególnych kolumn:

    * id - ``int``
    * species - ``str``
    * datetime - ``datetime``
    * sepal_length - ``float``
    * sepal_width - ``float``
    * petal_length - ``float``
    * petal_width - ``float``

#. Do połączenia wykorzystaj context manager (``with``)
#. Dane wrzuć do bazy za pomocą ``.executemany()`` podając ``dict``
#. Do bazy danych zapisz ``species`` jako nazwę gatunku (``str``), a nie jego id (``int``) (wersja z gwiazdką: nie korzystaj z if-ów do tego)
#. Dodaj kolumnę ``datetime`` z datą i czasem dodania (UTC)
#. Załóż index na ``datetime``
#. Wyniki wypisz z bazy danych (``SELECT * FROM iris ORDER BY datetime DESC``)
#. Zwracaj dane jako ``sqlite3.Row``

:About:
    * Filename: ``db_iris.py``
    * Lines of code to write: 30 lines
    * Estimated time of completion: 30 min

:The whys and wherefores:
    * Parsowanie plików ``csv``
    * Wykorzystywanie bazy ``sqlite3``
    * Tworzenie bazy danych
    * Zakładanie indeksów na bazie danych
    * Wrzucanie danych do bazy
    * Wyciąganie danych z bazy
    * Konwersja typów
    * Korzystanie z ``datetime``

Tworzenie bazy danych i proste zapytania
----------------------------------------
#. Wykorzystaj kod z listingu :numref:`listing-db-assignment-addressbook-sql` oraz :numref:`listing-db-assignment-addressbook-py`
#. Nie wykorzystuj relacji, a dane adresowe zapisz zserializowane i rozdzielone średnikami ``;``
#. Wykorzystaj ``cursor`` oraz połączenia jako context manager (``with``)
#. Dane powinny być zwracane w postaci listy ``dict``
#. Do wpisywania danych wykorzystaj konstrukcję ``execute`` wykorzystując ``dict`` jako argument

:About:
    * Filename: ``db_addressbook.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 20 min

:Zadanie z gwiazdką:
    * Dodaj obsługę wielu adresów
    * Dodaj obsługę relacji w aplikacji

.. literalinclude:: src/db-assignment-addressbook.sql
    :name: listing-db-assignment-addressbook-sql
    :language: python
    :caption: Address Book SQL queries

.. literalinclude:: src/db-assignment-addressbook.py
    :name: listing-db-assignment-addressbook-py
    :language: python
    :caption: Address Book
