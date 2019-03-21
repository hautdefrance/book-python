*********
Decorator
*********


Example
=======
.. literalinclude:: src/decorators-function.py
    :language: python
    :caption: Decorator usage


Zastosowanie
============
* Modify arguments
* Modify returned value
* Do things before call
* Do things after call
* Avoid calling
* Modify global state (not a good idea)
* Metadata

Przykład zastosowania
---------------------
- Zagnieżdżone
- wykonywane od góry

.. code-block:: python

    @timeout(seconds=10)
    def calculate(operations=[], collection):
        total = 0

        for operation in operations:
            total += operations(collection)

        return total


Function Decorators
===================

Decorator as function
---------------------
.. code-block:: python

    def my_decorator(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    @my_decorator
    def func(x):
        return x

Decorator as class
------------------
.. code-block:: python

    class memoize(dict):
        def __init__(self, function):
            self.function = function

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            result = self[key] = self.function(*key)
            return result


    @memoize
    def foo(a, b):
        return a * b


    foo(2, 4)       # 8
    foo             # {(2, 4): 8}

    foo('hi', 3)    # 'hihihi'
    foo             # {(2, 4): 8, ('hi', 3): 'hihihi'}


Class Decorators
================
.. literalinclude:: src/decorators-class-decorator.py
    :language: python
    :caption: Class Decorator

@staticmethod
-------------
.. code-block:: python
    :caption: Functions on a high level of a module lack namespace

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b


    add(1, 2)
    sub(8, 4)

.. code-block:: python
    :caption: When ``add`` and ``sub`` are in ``Calculator`` class (namespace) they get instance (``self``) as a first argument. Instantiating Calculator is not needed, as of functions do not read or write to instance variables.

    class Calculator:

        def add(self, a, b):
            return a + b

        def sub(self, a, b):
            return a - b


    Calculator.add(10, 20)  # TypeError: add() missing 1 required positional argument: 'b'
    Calculator.sub(8, 4)    # TypeError: add() missing 1 required positional argument: 'b'

    calc = Calculator()
    calc.add(1, 2)          # 3
    calc.sub(8, 4)          # 4

.. code-block:: python
    :caption: Class ``Calculator`` is a namespace for functions. ``@staticmethod`` remove instance (``self``) argument to method.

    class Calculator:

        @staticmethod
        def add(a, b):
            return a + b

        @staticmethod
        def sub(a, b):
            return a - b


    Calculator.add(1, 2)
    Calculator.sub(8, 4)

@classmethod
------------
- ``@classmethod`` turns a normal method to a factory method.
- first argument for ``@classmethod`` function must always be ``cls`` (class)
- Factory methods, that are used to create an instance for a class using for example some sort of pre-processing.
- Static methods calling static methods: if you split a static methods in several static methods, you shouldn't hard-code the class name but use class methods

.. code-block:: python

    class User:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        def __str__(self):
            return f'{self.first_name} {self.last_name}'

        def to_json(self):
            import json
            return json.dumps(self.__dict__)

        @classmethod
        def from_json(cls, data):
            import json
            data = json.loads(data)
            return cls(**data)


    user = User('Jan', 'Twardowski')
    # Jan Twardowski

    DATA = user.to_json()
    # '{"first_name": "Jan", "last_name": "Twardowski"}'

    user = User.from_json(DATA)
    # Jan Twardowski


``functools``
=============

``@functools.cached_property(func)``
------------------------------------
.. code-block:: python

    class DataSet:
        def __init__(self, sequence_of_numbers):
            self._data = sequence_of_numbers

        @cached_property
        def stdev(self):
            return statistics.stdev(self._data)

        @cached_property
        def variance(self):
            return statistics.variance(self._data)

LRU (least recently used) cache
-------------------------------
.. code-block:: python

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    >>> [fib(n) for n in range(16)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    >>> fib.cache_info()
    CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)

``memoize``
-----------
.. code-block:: python

    def memoize(function):
        from functools import wraps

        memo = {}

        @wraps(function)
        def wrapper(*args):
            if args in memo:
                return memo[args]
            else:
                rv = function(*args)
                memo[args] = rv
                return rv
        return wrapper


    @memoize
    def fibonacci(n):
        if n < 2: return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci(25)


Przykład
========

.. code-block:: python

    import os
    import logging


    def if_file_exists(function):

        def check(filename):
            if os.path.exists(filename):
                function(filename)
            else:
                logging.error('File "%(filename)s" does not exists, will not execute!', locals())

        return check


    @if_file_exists
    def print_file(filename):
        with open(filename) as file:
            content = file.read()
            print(content)


    if __name__ == '__main__':
        print_file('/etc/passwd')
        print_file('/tmp/passwd')

Case Study
----------
.. literalinclude:: src/decorators-case-study-flask.py
    :name: listing-decorators-case-study-flask
    :language: python
    :caption: Case Study wykorzystania dekotatorów do poprawienia czytelności kodu Flask

.. literalinclude:: src/decorators-case-study-django.py
    :name: listing-decorators-case-study-django
    :language: python
    :caption: Case Study wykorzystania dekotatorów do poprawienia czytelności kodu Django

Decorator library
-----------------
- https://wiki.python.org/moin/PythonDecoratorLibrary

Assignments
===========

Prosty dekorator
----------------
* Filename: ``decorator_abspath.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min

* Program przechodzi przez pliki i katalogi wykorzystując ``os.walk``.
* Stwórz funkcję, która wypisuje na ekranie nazwę pliku lub katalogu.
* Stwórz dekorator do funkcji, który przed wyświetleniem jej na ekranie podmieni ścieżkę na bezwzględną (``path`` + ``filename``).

Memoization
-----------
* Filename: ``decorator_memoize.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min

#. Stwórz ``dict`` o nazwie ``CACHE`` z wynikami wyliczenia funkcji

    - klucz: argument funkcji
    - wartość: wynik obliczeń

#. Dodaj dekorator do funkcji ``factorial(n: int)`` z listingu poniżej
#. Decorator ma sprawdzać przed uruchomieniem funkcji, sprawdź czy wynik został już wcześniej obliczony:

    - jeżeli tak, to zwraca dane z ``CACHE``
    - jeżeli nie, to oblicza, aktualizuje ``CACHE``, a następnie zwraca wartość

#. Porównaj prędkość działania z obliczaniem na bieżąco dla parametru 500

:Hints:
    * ``import timeit`` - https://docs.python.org/3/library/timeit.html
    * .. code-block:: python

        def factorial(n: int) -> int:
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
