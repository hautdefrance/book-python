.. _Files:

*****
Files
*****


Path
====

Absolute path
-------------
.. code-block:: python

    FILE = r'C:\Temp\iris.csv'

.. code-block:: python

    FILE = r'/tmp/iris.csv'

Relative path
-------------
.. code-block:: python

    FILE = r'iris.csv'

.. code-block:: python

    FILE = r'../data/iris.csv'


Access modes
============
.. csv-table::
    :header-rows: 1
    :widths: 20, 80
    :file: data/file-open-modes.csv


Read from file
==============
* Works with both relative and absolute path
* Uses context manager

Reading file line by line
-------------------------
* Fails when directory with file cannot be accessed
* Fails when file cannot be accessed

.. literalinclude:: src/file-iterate-lines.py
    :language: python
    :caption: ``file`` can be iterated line by line

Reading whole file content
--------------------------
.. literalinclude:: src/file-read.py
    :language: python
    :caption: Read whole file as a text to ``content`` variable

Reading file as ``list`` with lines
-----------------------------------
.. literalinclude:: src/file-readlines.py
    :language: python
    :caption: Convert file to list by line

Read selected lines from file
-----------------------------
.. literalinclude:: src/file-readlines-slice.py
    :language: python
    :caption: Convert file to list by line, select 1-30 lines


Writing to file
===============
* Fails when directory with file cannot be accessed
* Creates file if not exists
* Overwrite old content

.. literalinclude:: src/file-write.py
    :language: python
    :caption: Writing to file


Appending to file
=================
* Fails when directory with file cannot be accessed
* Creates file if not exists
* Append to the end of file

.. literalinclude:: src/file-append.py
    :language: python
    :caption: Appending to file


Exception handling
==================
.. literalinclude:: src/file-exception.py
    :language: python
    :caption: Exception handling while accessing files


Good Engineering Practises
==========================
* ``FILENAME`` as a raw string ``r'...'`` constant
* ``encoding='utf-8'``
* Use context manager


Assignments
===========

Parsing simple CSV file
-----------------------
* http://raw.githubusercontent.com/AstroMatt/book-python/master/control-flow/data/iris.csv

#. Skopij plik do siebie na dysk i nazwij go ``iris.csv``
#. Dla każdej linii:

    #. Oczyść linię z białych znaków
    #. Podziel linię po przecinku
    #. Zapisz rekordy do:

        - ``X: List[Tuple[float]]`` - features
        - ``y: List[str]`` - labels

:About:
    * Filename: ``file_iris.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 20 min

:The whys and wherefores:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym

Content of a requested file
---------------------------
#. Napisz program, który wyświetli na ekranie zawartość pliku o nazwie podanej przez użytkownika.
#. Dopisz obsługę wyjątków dla braku uprawnień oraz tego że plik nie istnieje.

:About:
    * Filename: ``file_content.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 5 min

Parsing ``/etc/hosts``
----------------------
#. Utwórz plik tekstowy ``hosts.txt``
#. Do pliku skopiuj kod z listingu:

    .. literalinclude:: src/etc-hosts.txt
        :language: text
        :caption: Zawartość pliku ``hosts.txt``

#. Ważne, żeby przepisać zawartość zawierającą komentarze, białe spacje i linie przerwy
#. Sparsuj plik i dla każdej linii:

    #. Pomiń linię jeżeli jest pusta, jest białym znakiem lub zaczyna się od komentarza
    #. Podziel linię po dowolnej ilości białych znaków (spacja, taby, itp)
    #. Wydziel ip i hosty
    #. Wykorzystaj jednolinikowego ``if`` do sprawdzenia czy jest kropka w adresie IP (to IPv4) w przeciwnym przypadku IPv6
    #. Do listy wynikowej dopisz słownik z ip, hostami i protokołem

#. Po zakończeniu parsowania przedstaw listę wynikową w formie ``List[Dict[str, Union[str, List[str]]]`` jak poniżej:

    .. literalinclude:: src/file-hosts.py
        :language: python
        :caption: ``/etc/hosts`` example

#. Dla zaawansowanych: scal listy hostname'ów dla wpisów o tym samym IP

:About:
    * Filename: ``file_hosts.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 20 min

:The whys and wherefores:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym

:Hints:
    * ``str.isspace()``
    * ``value = True if ... else False``
