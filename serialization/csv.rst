.. _CSV Serialization:

*****************
CSV Serialization
*****************


Reading data from CSV files
===========================
* Good practice is to always set:

    * ``encoding='utf-8'``
    * ``quotechar='"'``
    * ``delimiter=','``

.. literalinclude:: src/csv-read.py
    :name: listing-csv-read
    :language: python
    :caption: Zapis do plików csv używając ``csv.DictReader()``


Writing to CSV files
====================
* Good practice is to always set:

    * ``encoding='utf-8'``
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
* https://raw.githubusercontent.com/AstroMatt/book-python/master/database/data/iris.csv

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

#. Kolumna species ma mieć wartość nazwy gatunku a nie cyfry 0, 1, 2 jak to jest w pliku
#. Do wygenerowania słownika gatunków użyj pierwszej linijki z pliku (ale nie wyświetlaj jej)
#. Wypisz wiersze na ekranie

:About:
    * Filename: ``csv_dictreader.py``
    * Lines of code to write: 20 lines
    * Estimated time of completion: 15 min

Writing ``csv``
---------------
#. Za pomocą ``csv.DictWriter()`` zapisz do pliku dane o zmiennej strukturze
#. Podaj jawnie ``encoding``, ``delimiter``, ``quotechar`` ``quoting``, ``lineterminator``
#. ``fieldnames`` nie może być wymienione wprost w skrypcie (zahardkodowane)

.. code-block:: python

    DATA = [
        {'first_name': 'José'},
        {'last_name': 'Jiménez'},
        {'first_name': 'Иван', 'last_name': 'Иванович'},
        {'first_name': 'Mark', 'last_name': 'Watney', 'born': 1961},
        {'first_name': 'José', 'born': 1961, 'first_step': 1969},
    ]

:About:
    * Filename: ``csv_dictwriter.py``
    * Lines of code to write: 8 lines
    * Estimated time of completion: 15 min

:Hints:
    * To jest bardzo często występujący i użyteczny przykład

:The whys and wherefores:
    * Umiejętność korzystania z modułu ``csv``
    * Umiejętność iteracji po złożonych strukturach danych
    * Dynamiczne generowanie struktur danych na podstawie innych

Object serialization to CSV
---------------------------
#. Użyj obiektu ``książka_adresowa`` z listingu :numref:`listing-address-book`
#. Za pomocą ``csv.DictWriter()`` zapisz kontakty z książki adresowej w pliku
#. Wszystkie pola muszą być zawsze w cudzysłowiach i oddzielone średnikami, kodowanie UTF-8.
#. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku

:Hints:
    - powtarzanie rekordów (user pozostaje ten sam) z innymi danymi adresowymi
    - dodawanie kolumn (ulica_1, miasto_1, panstwo_1, ulica_2, miasto_2, panstwo_2) i automatyczne generowanie fieldnames
    - wrzucenie danych jako string do jednego pola adres_1, adres_2, adres_3 i ustalenie separatora (np: średnik - ';')
    - jedno pole adres (w ramach niego wszystkie adresy rozdzielone ";" a dane przecinkami ",")

.. literalinclude:: src/csv-addressbook.py
    :name: listing-address-book
    :language: python
    :caption: Address book

:About:
    * Filename: ``csv_addressbook.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 20 min
