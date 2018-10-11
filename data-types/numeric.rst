.. _Numerical Types:

***************
Numerical Types
***************


``int``
=======
* Python 3 dynamically extends ``int``, when it's too big
* In Python 3 there is not maximal ``int`` value
* Defining ``int``:

    .. code-block:: python

        value = 30
        value: int = 30

* For large numbers you can use ``_`` as thousands separator, or engineering notation:

    .. code-block:: python

        million = 1000000
        million = 1_000_000
        million = 1e6
        million = 1E6

* ``int()`` converts argument to ``int``:

    .. code-block:: python

        int(10)                 # 10
        int(10.0)               # 10
        int(10.9)               # 10
        int('10')               # 10
        int('10.5')             # ValueError: invalid literal for int() with base 10: ' 10.5'


``float``
=========
* Defining ``float``:

    .. code-block:: python

        value = 10.5
        value: float = 10.5

* ``float()`` converts argument to ``float``:

    .. code-block:: python

        float(10)              # 10.0

        float('+1.23')         # 1.23
        float('-1.23')         # -1.23

        float('1E-003')        # 0.001
        float('1e-003')        # 0.001
        float('+1E6')          # 1000000.0

* Min i max ``float``:

    .. code-block:: python

        import sys

        sys.float_info.min
        # 2.2250738585072014e-308

        sys.float_info.max
        # 1.7976931348623157e+308

    .. code-block:: python

        1e308
        # 1e+308

        1e309
        # inf

* Infinity representation in Python:

    .. code-block:: python

        float('-inf')          # -inf
        float('-Infinity')     # -inf
        float('inf')           # inf
        float('Infinity')      # inf


``complex``
===========
* Complex number with real and imaginary parts
* Engineering notation ``j`` not mathematical ``i``
* No space inside the expression
* Defining ``complex``:

    .. code-block:: python

        complex()               # 0j

        complex(1)              # (1+0j)
        complex(1, 2)           # (1+2j)
        complex(1.12, 2.34)     # (1.12+2.34j)
        complex(1, 2.34)        # (1+2.34j)

        complex(1+2j)           # (1+2j)
        complex(1+2j, 3+4j)     # (-3+5j)

        complex('1+2j')         # (1+2j)
        complex('1 + 2j')       # ValueError: complex() arg is a malformed string


Assignments
===========

Handling user input and type casting
------------------------------------
#. Użytkownik wprowadził odległość w metrach równą ``1337``
#. Wyświetl wartość na ekranie w różnych jednostkach
#. Do wyświetlania skorzystaj z kodu poniżej
#. Dane przy wyświetlaniu muszą być przekonwertowane do typów podanych w komentarzu
#. W miejsce ``...`` podstaw wyliczone i przekonwertowane zmienne

.. code-block:: python

    print(f'Meters: {...}')                    # int
    print(f'Kilometers: {...}')                # int
    print(f'Miles: {...}')                     # float
    print(f'Nautical Miles: {...}')            # float
    print(f'All: {...}, {...}, {...}, {...}')  # int, int, float, float

:About:
    * Filename: ``types_casting.py``
    * Lines of code to write: 4 lines
    * Estimated time of completion: 5 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Konwersja typów
    * Operacje matematyczne na zmiennych

:Hints:
    * Aby podzielić liczbę użyj ``/``, np: ``10 / 2``
    * 1000 m = 1 km
    * 1608 m = 1 mila
    * 1852 m = 1 mila morska
    * Literka ``f'...'`` włącza tryb interpolacji:

        .. code-block:: python

            age = 30
            print(f'My age is: {age}')
