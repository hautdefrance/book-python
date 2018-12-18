.. _CSV Serialization:

*****************
CSV Serialization
*****************


Reading data from CSV files
===========================
* Good practice is to always set:

    * ``quotechar='"'``
    * ``delimiter=','``

.. literalinclude:: src/csv-read.py
    :name: listing-csv-read
    :language: python
    :caption: Zapis do plików csv używając ``csv.DictReader()``


Writing to CSV files
====================
* Good practice is to always set:

    * ``quoting=csv.QUOTE_ALL``
    * ``quotechar='"'``
    * ``delimiter=','``
    * ``lineterminator='\n'``

.. literalinclude:: src/csv-write.py
    :name: listing-csv-write
    :language: python
    :caption: Zapis do plików csv używając ``csv.DictWriter()``


Parsing non-CSV files with ``csv.DictReader()``
===============================================

Parsing ``/etc/passwd``
-----------------------
.. literalinclude:: src/csv-passwd.py
    :name: listing-csv-passwd
    :language: python
    :caption: Parsing ``/etc/passwd`` file with ``csv.DictReader()``

Parsing Java properties file
----------------------------
.. literalinclude:: src/csv-properties.py
    :language: python
    :caption: Parsing ``sonar-project.properties`` file with  ``csv.DictReader()``


Assignments
===========

Reading ``csv``
---------------
* Filename: ``csv_dictreader.py``
* Lines of code to write: 20 lines
* Estimated time of completion: 10 min
* Input data: https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.csv

#. Otwórz w przeglądarce podany powyżej URL
#. Zapisz jego zawartość na dysku w miejscu gdzie masz skrypty w pliku ``iris.csv``
#. Korzystając z ``csv.DictReader`` wczytaj zawartość pliku
#. Podaj jawnie ``encoding``, ``delimiter`` oraz ``quotechar``
#. Nazwy poszczególnych kolumn:

    * Sepal length
    * Sepal width
    * Petal length
    * Petal width
    * Species

#. Wypisz wiersze na ekranie

Writing ``csv``
---------------
* Filename: ``csv_dictwriter.py``
* Lines of code to write: 8 lines
* Estimated time of completion: 10 min
* Input data: :numref:`listing-csv-dictwriter`

#. Za pomocą ``csv.DictWriter()`` zapisz do pliku CSV dane o zmiennej strukturze
#. Podaj jawnie ``encoding``, ``delimiter``, ``quotechar`` ``quoting``, ``lineterminator``
#. ``fieldnames`` nie może być wymienione wprost w skrypcie (zahardkodowane)

.. code-block:: python
    :name: listing-csv-dictwriter
    :caption: Create ``fieldnames: Set[str]`` with unique keys

    DATA = [
        {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
        {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
        {'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
        {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
    ]

:The whys and wherefores:
    * Umiejętność korzystania z modułu ``csv``
    * Umiejętność iteracji po złożonych strukturach danych
    * Dynamiczne generowanie struktur danych na podstawie innych

:Hints:
    * To jest bardzo często występujący i użyteczny przykład

Object serialization to CSV
---------------------------
* Filename: ``csv_addressbook.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Input data: :numref:`listing-csv-addressbook`

#. Za pomocą ``csv.DictWriter()`` zapisz kontakty z książki adresowej w pliku
#. Wszystkie pola muszą być zawsze w cudzysłowiach i oddzielone średnikami, kodowanie UTF-8.
#. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku

.. literalinclude:: src/csv-addressbook.py
    :name: listing-csv-addressbook
    :language: python
    :caption: Address book

:Hints:
    * powtarzanie rekordów (user pozostaje ten sam) z innymi danymi adresowymi
    * dodawanie kolumn (ulica_1, miasto_1, panstwo_1, ulica_2, miasto_2, panstwo_2) i automatyczne generowanie fieldnames
    * wrzucenie danych jako string do jednego pola adres_1, adres_2, adres_3 i ustalenie separatora (np: średnik - ';')
    * jedno pole adres (w ramach niego wszystkie adresy rozdzielone ";" a dane przecinkami ",")
