*********
Decorator
*********


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

    @permission_required(uid=0)
    @modyfikuj_sciezke_w_zaleznosci_od_systemu_operacyjnego
    @timeout(seconds=10, error_message='za dlugo')
    def instaluj_oprogramowanie(sciezka, nazwa_oprogramowania, wersja_paczki):
        pass


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
    :name: listing-decorators-class-decorator
    :language: python
    :caption: Class Decorator

@staticmethod
-------------
.. code-block:: python

    class Foo:
        def __init__(self, tekst='Jose'):
            self.tekst = tekst

        def hello(self):
            print(f'hello {self.tekst}')

        @staticmethod
        def ehlo():
            print('hello')


    # intuicyjna implementacja
    def staticmethod(method):
        def wrapper(*args, **kwargs):
            args = (x for x in args if not instanceof(arg, Foo))
            return method(*args, **kwargs)
        return wrapper

@classmethod
------------
- ``@classmehtod`` turns a normal method to a factory method.
- first argument for ``@classmethod`` function must always be ``cls`` (class)
- Factory methods, that are used to create an instance for a class using for example some sort of pre-processing.
- Static methods calling static methods: if you split a static methods in several static methods, you shouldn't hard-code the class name but use class methods

.. code-block:: python

    class Hero:

      @staticmethod
      def say_hello():
         print("Helllo...")

      @classmethod
      def say_class_hello(cls):
         if cls.__name__ == "HeroSon":
            print("Hi Kido")
         elif cls.__name__ == "HeroDaughter":
            print("Hi Princess")


    class HeroSon(Hero):
      def say_son_hello(self):
         print("test hello")


    class HeroDaughter(Hero):
      def say_daughter_hello(self):
         print("test hello daughter")


    testson = HeroSon()
    testson.say_class_hello()       # "Hi Kido"
    testson.say_hello()             # "Helllo..."

    testdaughter = HeroDaughter()
    testdaughter.say_class_hello()  # "Hi Princess"
    testdaughter.say_hello()        # "Helllo..."

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
* Program przechodzi przez pliki i katalogi wykorzystując ``os.walk``.
* Stwórz funkcję, która wypisuje na ekranie nazwę pliku lub katalogu.
* Stwórz dekorator do funkcji, który przed wyświetleniem jej na ekranie podmieni ścieżkę na bezwzględną (``path`` + ``filename``).

:About:
    * Filename: ``decorator_abspath.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 15 min

Memoization
-----------
#. Stwórz ``dict`` o nazwie ``CACHE`` z wynikami wyliczenia funkcji

    - klucz: argument funkcji
    - wartość: wynik obliczeń

#. Zmodyfikuj funkcję ``factorial(n: int)`` z listingu poniżej
#. Przed uruchomieniem funkcji, sprawdź czy wynik został już wcześniej obliczony:

    - jeżeli tak, to zwraca dane z ``CACHE``
    - jeżeli nie, to oblicza, aktualizuje ``CACHE``, a następnie zwraca wartość

#. Porównaj prędkość działania z obliczaniem na bieżąco dla parametru 500

:About:
    * Filename: ``decorator_memoize.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 15 min

:Hints:
    * ``import timeit`` - https://docs.python.org/3/library/timeit.html
    * .. code-block:: python

        def factorial(n: int) -> int:
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
