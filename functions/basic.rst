.. _Function Basics:

***************
Function Basics
***************


Function definition
===================
* Wielokrotne używanie tego samego kodu
* Poprawiają czytelność kodu
* Porządkują kod
* Pozwalają na łatwiejszy refactoring

.. code-block:: python

    def hello():
        print('My name... José Jiménez')

    hello()
    # My name... José Jiménez

Returning values
================
* Słowo kluczowe ``return`` wskazuje funkcji jaką wartość ma dana funkcja zwrócić.
* Wykonanie linii ze słowem kluczowym ``return`` kończy wykonywanie funkcji.

.. code-block:: python

    def hello():
        return 'ehlo world'

    output = hello()

    print(output)
    # 'ehlo world'

.. code-block:: python

    def hello():
        return 'ehlo world'
        print('This will not be executed')

    output = hello()

    print(output)
    # 'ehlo world'

Returning simple types
----------------------
.. code-block:: python

    def function():
        return 42

    def function():
        return 13.37

    def function():
        return 'José Jiménez'

    def function():
        return (42, 13.37, 'José Jiménez')

    def function():
        return 42, 13.37, 'José Jiménez'

    def function():
        return [42, 13.37, 'foobar']

    def function():
        return {42, 13.37, 'José Jiménez'}

    def function():
        return {'first_name': 'José', 'last_name': 'Jiménez'}

    def function():
        return True

    def function():
        return None

    def function():
        print('ehlo world')
        # implicit ``return None``

    def function():
        pass
        # implicit ``return None``

Returning nested types
----------------------
.. code-block:: python

    def function():
        return [
            ('Mark', 'Watney'),
            {'Kowalski', 'Lewis'},
            {'astro': 'Иванович', 'agency': {'name': 'roscosmos'}},
            {'astro': 'Jiménez', 'missions': ('mercury', 'apollo')},
        ]


Function arguments
==================

Passing arguments
-----------------
.. code-block:: python

    def add(a, b):
        return a + b

    add(1, 2)
    # 3

Type annotations
----------------
* Od Python 3.5
* Kod w języku python wykona się nawet jeśli typ nie zgadza się z adnotacją!
* Twoje IDE porówna typy oraz poinformuje cię jeżeli wykryje niezgodność
* Użyj ``mypy`` lub ``pyre-check`` do sprawdzania typów

.. code-block:: python

    def add(a: int, b: float) -> float:
        return a + b

    add(1, 2.5)
    # 3.5

.. code-block:: python

    def add(a: int, b: float) -> float:
        return a + b

    add('José', 'Jiménez')
    # 'JoséJiménez'

.. note:: więcej na ten temat w rozdziale dotyczącym :ref:`Type Annotation`

Named arguments
---------------
* Każdy argument ma swoją nazwę przez którą uzyskujemy dostęp do wartości argumentu w ciele funkcji.
* Ta nazwa może też być używana do przypisania wartości przy wywołaniu funkcji.

.. code-block:: python

    def minus(a, b):
        return a - b

    minus(2, 1)      # 1
    minus(1, 2)      # -1
    minus(a=2, b=1)  # 1
    minus(b=1, a=2)  # 1
    minus(2, b=1)    # 1
    minus(a=2, 1)    # SyntaxError: positional argument follows keyword argument

Arguments with default value
----------------------------
* Argument funkcji może mieć wartość domyślną.
* Funkcja przyjmie tą wartość jeżeli użytkownik nie zdefiniuje tego argumentu.
* Argumenty z wartością domyślną muszą być skrajnie po prawej stronie.

.. code-block:: python

    def hello(name='José Jiménez'):
         print(f'My name... {name}')

    hello('Иван Иванович')        # My name... Иван Иванович
    hello(name='Иван Иванович')   # My name... Иван Иванович
    hello()                       # My name... José Jiménez

.. code-block:: python

    def server(username, password, host='127.0.0.1', port=80, ssl=False, keep_alive=1, persistent=False):
        print('Connecting...')

    server('admin', 'admin', 'localhost', 80, False, 1, True)

    server(host='localhost', username='admin', password='admin', ssl=True, keep_alive=1, persistent=True)

    server(
        host='localhost',
        username='admin',
        password='admin',
        port=443,
        ssl=True,
        persistent=True,
    )

.. code-block:: python

    read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal=b'.', lineterminator=None, quotechar='"', quoting=0, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True, skipfooter=0, doublequote=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)

    data = read_csv('iris.csv', encoding='utf-8', usecols=['Petal lenght', 'Species'])


Naming convention
=================
* Używanie ``_`` w nazwach (snake_case) - // Python - snake ;)

    .. code-block:: python

        def add_numbers(a, b):
            return a + b

* Nie robimy camelCase

    .. code-block:: python

        def addNumbers(a, b):
            return a + b

* Nazwy opisowe funkcji zamiast komentarza

    .. code-block:: python

        def fabs(a, b):
            return float(abs(a + b))

        def float_absolute_value(a, b) -> float:
            return float(abs(a + b))

* ``_`` at the end of name when name collision

    .. code-block:: python

        def print_(text1, text2):
            print(values, sep=';', end='\n')


Variable scope
==============
* ``globals()``
* ``locals()``

.. code-block:: python

    def add(a, b=2):
        c = 3
        print(locals())

    add(1, 2)
    # {'a': 1, 'b': 2, 'c': 3}


Recurrence
==========
* Aby zrozumieć rekurencję – musisz najpierw zrozumieć rekurencję
* Maksymalny limit rekurencji = 1000
* Zmiana limitu ``sys.setrecursionlimit(limit)``
* CPython implementation doesn't optimize tail recursion, and unbridled recursion causes stack overflows.
* Python isn't a functional language and tail recursion is not a particularly efficient technique
* Rewriting the algorithm iteratively, if possible, is generally a better idea.

.. code-block:: python

    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


More advanced topics
====================
.. note:: The topic will be continued in :ref:`Advanced Functions` chapter


Assignments
===========

Aviation numbers
----------------
#. Napisz funkcję ``aviation_numbers``
#. Funkcja zamieni dowolnego ``int`` lub ``float`` na formę tekstową w mowie pilotów

.. csv-table:: Aviation Phonetic Numbers
    :header-rows: 1
    :file: data/aviation-numbers.csv

.. code-block:: python

    aviation_numbers(1969)       # 'one niner six niner'
    aviation_numbers(31337)      # 'tree one tree tree seven'
    aviation_numbers(13.37)      # 'one tree and tree seven'
    aviation_numbers(31.337)     # 'tree one and tree tree seven'
    aviation_numbers(-1969)      # 'minus one niner six niner'
    aviation_numbers(-31.337)    # 'minus tree one and tree tree seven
    aviation_numbers(-49.35)     # 'minus fower niner and tree fife'

:About:
    * Filename: ``functions_aviation_numbers.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Przypadek zaawansowany: argumenty pozycyjne i domyślne
    * Rzutowanie i konwersja typów

Number to human readable
------------------------
#. Napisz funkcję ``number_to_str``
#. Funkcja zamieni dowolnego ``int`` lub ``float`` na formę tekstową
#. Funkcja musi zmieniać wartości na poprawną gramatycznie formę
#. Max 6 cyfr przed przecinkiem
#. Max 5 cyfr po przecinku

    .. code-block:: python

        number_to_str(1969)      # 'one thousand nine hundred sixty nine'
        number_to_str(13.37)     # 'thirteen and thirty seven hundredths'
        number_to_str(31337)     # 'thirty one thousand three hundred thirty seven'
        number_to_str(31.337)    # 'thirty one three hundreds thirty seven thousands'
        number_to_str(-1969)     # 'minus one thousand nine hundred sixty nine'
        number_to_str(-31.337)   # 'minus thirty one three hundreds thirty seven thousands'

:About:
    * Filename: ``functions_numstr_human.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Przypadek zaawansowany: argumenty pozycyjne i domyślne
    * Rzutowanie i konwersja typów

Roman numbers
-------------
#. Napisz program, który przeliczy wprowadzoną liczbę rzymską na jej postać dziesiętną.
#. Napisz drugą funkcję, która dokona procesu odwrotnego.

:About:
    * Filename: ``functions_roman.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Sprawdzanie czy element istnieje w ``dict``
    * Rzutowanie i konwersja typów
