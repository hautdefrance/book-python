*****************************
Functions with many arguments
*****************************


Operators ``*`` i ``**``
========================
- To nie jest mnożenie i potęgowanie!
- ``*`` zwykle nazywa się ``*args`` (arguments) - argumenty pozycyjne (anonimowe)
- ``**`` zwykle nazywa się ``**kwargs`` (keyword arguments) - argumenty nazwane
- ``*args`` unpack ``tuple`` or ``list``
- ``**kwargs`` unpack ``dict``


Przypomnienie wiadomości o parametrach
======================================
.. code-block:: python

    def add(a, b):
        return a + b


    add(1, 2)       # pozycyjne
    add(a=1, b=2)   # nazwane, kolejność nie ma znaczenia
    add(b=2, a=1)   # nazwane, kolejność nie ma znaczenia
    add(1, b=2)     # pozycyjne i nazwane

.. code-block:: python

    a, b = 1, 2
    # a == 1
    # b == 2

    a, b = (1, 2)
    # a == 1
    # b == 2

    a, b = [1, 2]
    # a == 1
    # b == 2

.. code-block:: python

    def numbers():
        return [1, 2]

    a, b = numbers()
    # a == 1
    # b == 2


Defining function with many arguments
=====================================

Many positional arguments
-------------------------
.. code-block:: python

    def show(*args):
        print(args)


    show()                        # ()
    show(1)                       # (1,)
    show(2, 3)                    # (2, 3)
    show('red', 2)                # ('red', 2)
    show('red', 'green', 'blue')  # ('red', 'green', 'blue')

.. code-block:: python

    def add(*args):
        total = 0

        for arg in args:
            total += arg

        return arg


    add()            # 0
    add(1)           # 1
    add(1, 4)        # 5
    add(3, 1)        # 4
    add(1, 2, 3, 4)  # 10

Many named arguments
--------------------
.. code-block:: python

    def show(**kwargs):
        print(kwargs)


    show(a=10)                                      # {'a': 10}
    show(color='red')                               # {'color': 'red'}
    show(first_name='Pan', last_name='Twardowski')  # {'first_name': 'Pan', 'last_name': Twardowski}

Many named and positional arguments
-----------------------------------
.. code-block:: python

    def show(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)
        print(kwargs)  # {}


    show(1, 2, 3, 4, 5, 6)

.. code-block:: python

    def show(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 0
        print(args)    # ()
        print(kwargs)  # {'d':7, 'e': 8}


    show(1, 2, d=7, e=8)

.. code-block:: python

    def show(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)
        print(kwargs)  # {'d':7, 'e': 8}


    show(1, 2, 3, 4, 5, 6, d=7, e=8)


Case Study
==========
.. code-block:: python

    def celsius_to_fahrenheit(*degrees):
        return [degree*1.8+32 for degree in degrees]

    celsius_to_fahrenheit(1)
    # [33.8]

    celsius_to_fahrenheit(1, 2, 3, 4, 5)
    # [33.8, 35.6, 37.4, 39.2, 41.0]


Assignments
===========

Numeric Values
--------------
#. Stwórz funkcję ``is_numeric``
#. Funkcja może przyjmować dowolną ilość argumentów
#. Jeżeli, któryś z argumentów nie jest ``int`` albo ``float`` to zwróć ``False``
#. Jeżeli, wszystkie argumenty to ``int`` albo ``float``, to zwróć True

:About:
    * Filename: ``kwargs_numeric.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Rzutowanie i konwersja typów

:Hint:
    * ``isinstance()``
