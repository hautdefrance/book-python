******
SQLite
******

* Database API in Python


SQL Syntax
==========
.. note:: For SQL Syntax refer to :ref:`SQL`

Data Types
----------
.. csv-table:: SQLite data types
    :header-rows: 1
    :file: data/sql-types.csv

Constrains
----------
.. csv-table:: SQL Constraints
    :header-rows: 1
    :file: data/sql-constraints.csv


Connection
==========
.. literalinclude:: src/database-connect-memory.py
    :language: python
    :caption: Connection to in-memory database

.. literalinclude:: src/database-connect-file.py
    :language: python
    :caption: Connection to database file


Execute
=======
.. literalinclude:: src/database-execute.py
    :language: python
    :caption: Execute


Executemany
===========

``List[tuple]``
---------------
.. literalinclude:: src/database-executemany-tuple.py
    :language: python
    :caption: Execute many

``List[dict]``
--------------
.. literalinclude:: src/database-executemany-dict.py
    :language: python
    :caption: Execute many


Results
=======

Fetch as ``List[tuple]``
------------------------
.. literalinclude:: src/database-results.py
    :language: python
    :caption: Results

Fetch as ``List[dict]``
-----------------------
.. literalinclude:: src/database-results-dict.py
    :language: python
    :caption: Results with ``dict``


Cursor
======
.. literalinclude:: src/database-cursor.py
    :language: python
    :caption: Results with cursor


Case Study
==========
.. literalinclude:: src/database-case-study.py
    :name: listing-database-case-study
    :language: python
    :caption: Zapisywanie do bazy danych wyników pobranych z sensorów podłączonych po USB


Assignments
===========

Iris Database
-------------
* Filename: ``database_iris.py``
* Lines of code to write: 30 lines
* Estimated time of completion: 30 min
* Input data: :numref:`listing-database-iris.csv`

.. literalinclude:: assignment/database-iris.csv
    :name: listing-database-iris.csv
    :language: python
    :caption: Iris Database

#. Skopiuj dane z listingu :numref:`listing-database-iris.csv` i zapisz je w pliku ``iris-db.csv``
#. Wczytaj dane z pliku ``iris-db.csv``
#. Stwórz ``species: Dict[int, str]`` o strukturze:

    * 0 - setosa
    * 1 - versicolor
    * 2 - virginica

#. Bazę pomiarów Irysów przekonwertuj na tabelę w ``sqlite3``
#. Do połączenia wykorzystaj context manager (``with``)
#. Dane wrzuć do bazy za pomocą ``.executemany()`` podając ``dict``
#. Nazwy poszczególnych kolumn:

    * id - ``int``
    * species - ``str`` - podmień ``int`` na ``str`` ze słownika ``species``
    * datetime - ``datetime`` - z datą i czasem dodania w UTC
    * sepal_length - ``float``
    * sepal_width - ``float``
    * petal_length - ``float``
    * petal_width - ``float``

#. Przy dodawaniu danych ``species`` podmień ``int`` na ``str`` ze słownika ``species``
#. Dodaj kolumnę ``datetime`` z datą i czasem dodania (UTC)
#. Załóż index na ``datetime``
#. Wyniki wypisz z bazy danych (``SELECT * FROM iris ORDER BY datetime DESC``)
#. Zwracaj dane jako ``sqlite3.Row``

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
* Filename: ``database_addressbook.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min

#. Wykorzystaj kod z listingu :numref:`listing-database-addressbook.sql` oraz :numref:`listing-database-addressbook.txt`
#. Wykorzystaj ``cursor`` oraz połączenia jako context manager (``with``)
#. Dane powinny być zwracane w postaci listy ``dict``
#. Do wpisywania danych wykorzystaj konstrukcję ``execute`` wykorzystując ``dict`` jako argument

:Zadanie z gwiazdką:
    * Dodaj obsługę wielu adresów
    * Dodaj obsługę relacji w aplikacji

.. literalinclude:: assignment/database-addressbook.sql
    :name: listing-database-addressbook.sql
    :language: sql
    :caption: Address Book SQL queries

.. literalinclude:: assignment/database-addressbook.txt
    :name: listing-database-addressbook.txt
    :language: text
    :caption: Address Book data

Dane w jednej tabeli
--------------------
* Lines of code to write: 0 lines
* Estimated time of completion: 5 min
* Input data: :numref:`listing-database-addressbook.txt`

#. Jak zapisać w jednej tabeli bez wykorzystania relacji?
#. Przeprowadź dyskusję na temat zalet i wad podejść:

    - jedno pole adresy i dane rozdzielone separatorem (``;``)
    - wiele adresów i dane rozdzielone separatorem (``;``)
    - wiele kolumn dla każdego pola

#. Które podejście jest najlepsze?
#. Które podejście jest zgodne z ACID?
