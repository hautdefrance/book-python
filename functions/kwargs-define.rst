*****************************
Functions with many arguments
*****************************


Operands ``*`` and ``**``
=========================
- This is not multiplication or power!
- ``*args`` - positional arguments
- ``**kwargs`` - keyword arguments
- ``*args`` unpacks to ``tuple``
- ``**kwargs`` unpacks to ``dict``


Recap information about function parameters
===========================================
.. code-block:: python

    def add(a, b):
        return a + b


    add(1, 2)       # pozycyjne
    add(a=1, b=2)   # nazwane, kolejność nie ma znaczenia
    add(b=2, a=1)   # nazwane, kolejność nie ma znaczenia
    add(1, b=2)     # pozycyjne i nazwane


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

        return total


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
    show(first_name='Jan', last_name='Twardowski')  # {'first_name': 'Jan', 'last_name': Twardowski}

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

.. code-block:: python

    def html_list(*args):
        print('<ul>')

        for element in args:
            print(f'<li>{element}</li>')

        print('</ul>')

    print_everything('apple', 'banana', 'cabbage')
    # <ul>
    # <li>apple</li>
    # <li>banana</li>
    # <li>cabbage</li>
    # </ul>

.. code-block:: python

    def print(*values, sep=' ', end='\n', ...):
        return sep.join(values) + end

.. code-block:: python

    class Point2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    class Point3D(Point2D):
        def __init__(self, z, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.z = z

.. code-block:: python

    mynum = 1000
    mystr = 'Hello World!'
    print "{mystr} New-style formatting is {mynum}x more fun!".format(**locals())

.. code-block:: python

    from functools import wraps

    def login_required(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if user.is_logged():
                return f(*args, **kwargs)
            else:
                print('Permission denied')
        return wrapper


Assignment
==========

Numeric Values
--------------
* Filename: ``kwargs_numeric.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min

#. Stwórz funkcję ``is_numeric``
#. Funkcja może przyjmować dowolną ilość argumentów
#. Za pomocą funkcji ``isinstance()`` sprawdź czy wszystkie argumenty są ``int`` albo ``float``:

    - Jeżeli wszystkie są ``int`` albo ``float``, to zwróć ``True``
    - Jeżeli którykolwiek nie jest, to zwróć ``False``

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Rzutowanie i konwersja typów
