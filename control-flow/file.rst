.. _Files:

*****
Files
*****


Path
====

Absolute path
-------------
* Windows
    .. code-block:: python

        FILE = r'C:\Temp\iris.csv'

* Linux, macOS, BSD, *nix

    .. code-block:: python

        FILE = r'/tmp/iris.csv'

Relative path
-------------
* File in the same directory directory

    .. code-block:: python

        FILE = r'iris.csv'

* File in parent directory

    .. code-block:: python

        FILE = r'../data/iris.csv'


Access modes
============
.. csv-table::
    :header-rows: 1
    :widths: 20, 80

    "Character", "Meaning"
    "``'r'``", "open for reading (default)"
    "``'w'``", "open for writing, truncating the file first"
    "``'a'``", "open for writing, appending to the end of the file if it exists"
    "``'rb'``", "read binary mode"
    "``'wb'``", "write binary mode"
    "``'ab'``", "append binary mode"


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

Writing
=======

Writing to file
---------------
* Fails when directory with file cannot be accessed
* Creates file if not exists
* Overwrite old content

.. literalinclude:: src/file-write.py
    :language: python
    :caption: Writing to file


Appending to file
-----------------
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
* ``FILE`` as a raw string ``r'...'`` constant
* ``encoding='utf-8'``
* Use context manager


Assignments
===========

Content of a requested file
---------------------------
* Filename: ``file_content.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

#. Napisz program, który wyświetli na ekranie zawartość pliku o nazwie podanej przez użytkownika.
#. Dopisz obsługę wyjątków dla braku uprawnień oraz tego że plik nie istnieje.

Parsing simple CSV file
-----------------------
* Filename: ``file_iris.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Input data: http://raw.githubusercontent.com/AstroMatt/book-python/master/control-flow/data/iris.csv

#. Skopiuj plik do siebie na dysk i nazwij go ``iris.csv``
#. Dla każdej linii:

    #. Oczyść linię z białych znaków
    #. Podziel linię po przecinku
    #. Zapisz rekordy do:

        - ``X: List[Tuple[float]]`` - features
        - ``y: List[str]`` - labels

:The whys and wherefores:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym

Parsing ``/etc/hosts``
----------------------
* Filename: ``file_hosts.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min

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
