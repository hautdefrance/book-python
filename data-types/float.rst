*********
``float``
*********


Defining ``float``
==================
.. code-block:: python

    value = 10.5

Notation without leading or trailing zero
-----------------------------------------
* Used by ``numpy``

.. code-block:: python

    value = 10.     # 10.0
    value = .44     # 0.44

Engineering notation
--------------------
.. code-block:: python

    million = 1e6
    million = 1E6

.. code-block:: python

    float(+1E6)            # 1000000.0
    float(-1E3)            # -1000.0

.. code-block:: python

    float(1e-4)            # 0.0001
    float(1E-3)            # 0.001

    float(1e-5)            # 1e-05
    float(1E-5)            # 1E-05

Infinity representation
-----------------------
.. code-block:: python

    1e308
    # 1e+308

    1e309
    # inf

.. code-block:: python

    float('-inf')          # -inf
    float('-Infinity')     # -inf

.. code-block:: python

    float('inf')           # inf
    float('Infinity')      # inf

Maximal and minimal ``float`` values
------------------------------------
.. code-block:: python

    import sys

    sys.float_info.min
    # 2.2250738585072014e-308

    sys.float_info.max
    # 1.7976931348623157e+308


Converting to ``float``
=======================
* Also known as "type casting"
* ``float()`` converts argument to ``float``

.. code-block:: python

    float(10.5)            # 10.5
    float(10)              # 10.0

.. code-block:: python

    float(1.23)            # 1.23
    float(-1.23)           # -1.23

.. code-block:: python

    float('+1.23')         # 1.23
    float('-1.23')         # -1.23


Numeric Functions
=================

Rounding numbers
----------------
.. code-block:: python

    pi = 3.14159265359

    round(pi)       # 3
    round(pi, 2)    # 3.14
    round(pi, 4)    # 3.1416

Absolute value
--------------
.. code-block:: python

    abs(1.5)        # 1.5
    abs(1)          # 1
    abs(-1)         # 1
    abs(-1.5)       # 1.5

Number to the ``n-th`` power
----------------------------
.. code-block:: python

    pow(2, 2)       # 4
    pow(3, 4)       # 81
    pow(-1, 2)      # 1
    pow(2, -1)      # 0.5
    pow(2.888, 3)   # 24.087491072

.. code-block:: python

    2 ** 2          # 4
    3 ** 4          # 81
    -1 ** 2         # 1
    2 ** -1         # 0.5
    2.888 ** 3      # 24.087491072


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

    print(f'Meters: {...}')                              # int
    print(f'Kilometers: {...}')                          # int
    print(f'Miles: {...}')                               # float
    print(f'Nautical Miles: {...}')                      # float
    print(f'm: {...}, km: {...}, mi: {...}, nm: {...}')  # int, int, float, float

:About:
    * Filename: ``types_casting.py``
    * Lines of code to write: 4 lines
    * Estimated time of completion: 5 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Nazewnictwo zmiennych
    * Korzystanie z print formatting
    * Konwersja typów
    * Operacje matematyczne na zmiennych
    * Oddzielenie logiki biznesowej od warstwy widoku

:Hints:
    * 1000 m = 1 km
    * 1608 m = 1 mila
    * 1852 m = 1 mila morska
    * Literka ``f'...'`` włącza tryb interpolacji:

        .. code-block:: python

            age = 30
            print(f'My age is: {age}')
