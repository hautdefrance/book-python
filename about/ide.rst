****************************************
IDE - Integrated Development Environment
****************************************


What is IDE?
============
* Refactoring
* Syntax helping and highlighting
* Type hinting and checking
* VCS support
* Virtualenv support
* Debugging
* Spell checking
* Running code and inspections
* File Scopes and views
* Database explorer
* Support for testing (doctest, unittest)
* Jump to line in exceptions


How to choose?
==============
* Nie ma znaczenia z jakiego IDE skorzystasz!
* Do edycji skryptów Pythona wystarczy sam Notatnik lub Jupyter
* W miarę rośnięcia złożoności projektu oraz ilości plików przyda nam się coś co ułatwi nam pracę
* Dobre IDE pomoże Ci w Refactoringu, podpowiedziach typów, debuggingu oraz pracy z systemem kontroli wersji
* PyCharm ma dwie wersję płatną oraz darmową, wersja darmowa w zupełności nam wystarczy
* Ciekawą alternatywą może być PyDev - plugin do środowiska Eclipse


Which one is the best?
======================

Open Source
-----------
#. `PyCharm Community <https://www.jetbrains.com/pycharm/download/>`_
#. `PyDev <http://www.pydev.org/download.html>`_
#. Spyder
#. Atom
#. Jupyter Notebook
#. Rodeo

Not-free
--------
#. `PyCharm Professional <https://www.jetbrains.com/pycharm/download/>`_
#. Visual Studio Code


PyCharm
=======

Keyboard shortcuts
------------------
.. csv-table:: Keyboard shortcuts
    :header-rows: 1
    :widths: 25, 75

    "Key Combination", "Action"
    "``ctrl`` + ``/``", "Comment multiple lines"
    "``alt`` + ``F12``", "Open Terminal"
    "``shift`` + ``F6``", "Refactor... Rename"
    "``tab``", "Indent (also used on multiple lines)"
    "``shift`` + ``tab``", "Un-indent (also used on multiple lines)"
    "``alt`` + ``1``", "Show file drawer"
    "", "Run"
    "", "Show console"
    "", "Actions"
    "``ctrl`` + ``g``", "Jump to line"
    "``ctrl`` + ``f``", "Search in file"
    "``ctrl`` + ``r``", "Replace in file"


Assignments
===========

Create Project in Pure Python
-----------------------------
* Lines of code to write: 0 lines
* Estimated time of completion: 2 min

#. Stwórz projekt w Twoim IDE
#. Wybierz "Pure Python" (opcja dostępna tylko w Pycharm Professional)
#. Rozwiń listę Project Interpreter i ustaw aby korzystać z "Virtualenv"
#. WAŻNE: Upewnij się, że masz Python 3.7 lub nowszy
#. Po stworzeniu projektu, załóż katalog o nazwie jak twoje nazwisko i imie ``nazwisko_imie``
#. WAŻNE: Już do końca książki w nim będą tworzone rozwiązania do wszystkich zadań

Create Project from GIT
-----------------------
* Lines of code to write: 0 lines
* Estimated time of completion: 2 min

#. Stwórz projekt w Twoim IDE
#. Wykorzystaj opcję 'Create from VCS'
#. WAŻNE: Upewnij się, że masz Python 3.7 lub nowszy
#. Stwórz plik ``.gitignore``
#. Wpisz linię ``.idea/`` do pliku
#. Po stworzeniu projektu, załóż katalog o nazwie jak twoje nazwisko i imie ``nazwisko_imie``
#. WAŻNE: Już do końca książki w nim będą tworzone rozwiązania do wszystkich zadań

Check Python Version
--------------------
* Filename: ``python_version.py``
* Lines of code to write: 0 lines
* Estimated time of completion: 5 min

#. Stwórz skrypt o nazwie ``python_version.py`` (nazwa skryptu będzie zawsze wpisana w sekcji "About")
#. Plik ma mieć zawartość:

    .. code-block:: python

        import sys

        print(sys.version)

#. Uruchom go w swoim IDE (menu ``Run -> Run... -> nazwa Twojego skryptu``)
#. Jaka wersja Python jest zainstalowana?

:The whys and wherefores:
    * Czy Python działa
    * Jaka jest wersja Python
    * Korzystanie z print
    * Umiejętność uruchamiania skryptów
    * Szukanie rozwiązań zadań z książki

Check Python Environment
------------------------
* Filename: ``python_env.py``
* Lines of code to write: 0 lines
* Estimated time of completion: 5 min

#. Stwórz plik o nazwie ``python_env.py``
#. Plik ma mieć zawartość:

    .. code-block:: python

        import sys
        import os

        print(f'Installation: {sys.executable}')
        print(f'Virtualenv: {os.getenv("VIRTUAL_ENV")}')

#. Uruchom go w swoim IDE (menu ``Run -> Run... -> nazwa Twojego skryptu``)
#. Gdzie Python jest zainstalowany?
#. Czy korzystasz z "Virtualenv"?
#. Upewnij się, że w linijce z "Virtualenv" nie masz ``None``

:The whys and wherefores:
    * Czy Python działa
    * Jaka jest wersja Python
    * Czy korzystasz z Virtualenv
    * Korzystanie z print
    * Umiejętność uruchamiania skryptów
    * Szukanie rozwiązań zadań z książki

Know thou IDE
-------------
* Lines of code to write: 0 lines
* Estimated time of completion: 10 min

#. Jak zrobić w Twoim IDE:

    * Run...
    * Run in console
    * Debug...
    * Python Console
    * Terminal
    * Full Screen
    * Distraction Free Mode
    * Reformat Code
    * Scope

#. Jakie są skróty klawiszowe do poszczególnych opcji?
#. Czym się różni ``Run...`` od ``Debug...``?
#. Czym się różni ``Python Console`` od ``Terminal``
#. Czym się różni ``Distraction Free Mode`` od ``Full Screen``
#. Ustaw Scope tak, aby ukryć katalog z Virtualenv

:The whys and wherefores:
    * Korzystanie z IDE
    * Uruchamianie debuggera
    * Znajomość różnicy między uruchamianiem i debuggingiem
    * Znajomość różnicy między terminalem i konsolą

Spellchecker
------------
* Lines of code to write: 0 lines
* Estimated time of completion: 3 min

#. Zainstaluj plugin 'Hunspell'
#. Pobierz z https://github.com/LibreOffice/dictionaries słownik ``.dic`` oraz ``.aff`` dla języka polskiego
#. Skonfiguruj IDE do korzystania z tego słownika

:The whys and wherefores:
    * Korzystanie z IDE
    * Konfiguracja IDE
