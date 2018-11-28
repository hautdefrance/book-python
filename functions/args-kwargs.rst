.. _Function Args and KWargs:

**************************
``*args`` and ``**kwargs``
**************************


Operator ``*`` i ``**``
=======================
- ``*`` zwykle nazywa się ``*args`` (arguments) - argumenty pozycyjne (anonimowe)
- ``**`` zwykle nazywa się ``**kwargs`` (keyword arguments) - argumenty nazwane


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


Przyjmowanie z funkcji zmiennej ilości argumentów (Rozpakowywanie)
==================================================================
.. code-block:: python

    line = 'jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash'
    line.split(':')
    # ['jimenez', 'x', '1001', '1001', 'José Jiménez', '/home/jimenez', '/bin/bash']

.. code-block:: python

    username, password, uid, gid, name, home, shell = line.split(':')
    username    # jimenez
    password    # x

.. code-block:: python

    username, password, *others = line.split(':')
    username    # jimenez
    password    # x
    others      # ['1001', '1001', 'José Jiménez', '/home/jimenez', '/bin/bash']

.. code-block:: python

    *others, home, shell = line.split(':')
    others      # ['jimenez', 'x', '1001', '1001', 'José Jiménez']
    home        # '/home/jimenez'
    shell       # '/bin/bash'

.. code-block:: python

    *a, b, *c = [1, 2, 3, 4, 5, 6, 7]
    # SyntaxError: two starred expressions in assignment

.. code-block:: python

    # if you're not using ``others`` later in your code
    username, *_ = line.split(':')

.. code-block:: python

    class Point:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def get_position(self):
            return self.x, self.y, self.z

    p = Point(10, 20)
    p.get_position()    # 10, 20
    x, y, z = p.get_position()
    x, *_ = p.get_position()

.. code-block:: python

    def sensor_temperatury():
        # ładniej byłoby gdyby programista napisał
        # {'napiecie': 10, 'natezenie': 20, 'rezystancja': 30, 'czas': 5, 'location': 'laboratorium'}
        # ale programiści niskopoziomowi zwykle zwracają jako list...
        return (10, 20.6, 30, 5, 'laboratorium')

    napiecie, natezenie, *_ = sensor_temperatury()


Definiowanie funkcji ze zmienną ilością parametrów
==================================================
- ``args`` - pozycyjne
- ``kwargs``- nazwane

.. code-block:: python

    def wyswietl_argumenty(a, b, c=0, *pozycyjne, **nazwane):
        print(f'argument a: {a}')                   # 1
        print(f'argument b: {b}')                   # 2
        print(f'argument c: {c}')                   # 3
        print(f'argumenty pozycyjne: {pozycyjne}')  # (4, 5, 6)
        print(f'argumenty nazwane: {nazwane}')      # {'d':7, 'e': 8}


    wyswietl_argumenty(1, 2, 3, 4, 5, 6, d=7, e=8)

.. code-block:: python

    def wyswietl_argumenty(a, b, c=0, *args, **kwargs):
        print(f'argument a: {a}')                   # 1
        print(f'argument b: {b}')                   # 2
        print(f'argument c: {c}')                   # 3
        print(f'argumenty args: {args}')            # (4, 5, 6)
        print(f'argumenty kwargs: {kwargs}')        # {'d':7, 'e': 8}


    wyswietl_argumenty(1, 2, 3, 4, 5, 6, d=7, e=8)

Kiedy to się przydaje
---------------------
.. code-block:: python

    def celsius_to_fahrenheit(*degrees):
        return [degree*1.8+32 for degree in degrees]

    celsius_to_fahrenheit(1)
    # [33.8]

    celsius_to_fahrenheit(1, 2, 3, 4, 5)
    # [33.8, 35.6, 37.4, 39.2, 41.0]


Przekazywanie do funkcji zmiennej ilości parametrów
===================================================
Przykładowe zastosownaie operatorów ``*`` i ``**`` polega na wykorzystaniu ich przy wywołaniu funkcji. Wtedy, wykorzystując operator ``*``, kolejne elementy listy albo krotki będą przekazane jako kolejne argumenty funkcji, a wykorzystując operator ``**`` kolejne elementy zmiennej słownikowej będą przekazane jako nazwane argumenty. Oznacza to, że na przykład argument ``x`` funkcji, przyjmie wartość ``vector['x']``.

.. code-block:: python

    def my_function(x, y, z):
        print(x, y, z)

    vector = (1, 0, 1)
    my_function(*vector)   # my_function(1, 0, 1)
    # 1, 0, 1

    vector = {'y': 1, 'x': 0, 'z': 1}
    my_function(**vector)  # my_function(y=1, x=0, z=1)
    # 0, 1, 1

.. code-block:: python

    def wyswietl(a, b, c=0):
        print(locals())

    wyswietl(1, 2, 3)
    # {'a': 1, 'b': 2, 'c': 3}

    dane = (1, 2, 3)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 3}

    dane = (1, 2)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 0}

.. code-block:: python

    def wyswietl(a, b, c=0, *args):
        print(locals())

    dane = (1, 2, 3, 4)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4,)}

    dane = (1, 2, 3, 4, 5, 6, 7)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6, 7)}

    wyswietl(1, 2)
    # {'a': 1, 'b': 2, 'c': 0, 'args': ()}

.. code-block:: python

    def wyswietl(a, b, c=0, *args, **kwargs):
        print(locals())

    wyswietl(1, 2, x=77, y=99)
    # {'a': 1, 'b': 2, 'c': 0, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

    wyswietl(1, 2, x=77, y=99, c=7)
    # {'a': 1, 'b': 2, 'c': 7, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

    dane = {'x': 77, 'y': 99}
    wyswietl(1, 2, 3, **dane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

    dane = {'a': 1, 'b': 2, 'x': 77, 'y': 99}
    wyswietl(**dane)
    # {'a': 1, 'b': 2, 'c': 0, 'args': (), 'kwargs': {'x': 77, 'y': 99}}


.. code-block:: python

    def wyswietl(a, b, c=0, *args, **kwargs):
        print(locals())

    dane = {'x': 77, 'y': 99, 'a': 7}
    wyswietl(1, 2, 3, **dane)
    # TypeError: wyswietl() got multiple values for argument 'a'

.. code-block:: python

    def wyswietl(a, b, c=0, *args, **kwargs):
        print(locals())

    wyswietl(1, 2, 3, 4, 5, 6, x=77, y=99)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6), 'kwargs': {'x': 77, 'y': 99}}

    pozycyjne = (4, 5, 6)
    nazwane = {'x': 77, 'y': 99}
    wyswietl(1, 2, 3, *pozycyjne, **nazwane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6), 'kwargs': {'x': 77, 'y': 99}}


Przykładowe zastosowanie
========================
.. code-block:: python

    from typing import List

    def celsius_to_fahrenheit(*degrees) -> List[float]:
        return [x * 1.8 + 32 for x in degrees]


    celsius_to_fahrenheit(1)
    # [33.8]

    celsius_to_fahrenheit(1, 2, 3, 4, 5)
    # [33.8, 35.6, 37.4, 39.2, 41.0]

.. code-block:: python

    class Kontakt:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    Kontakt(imie='Matt', nazwisko='Kowalski')

.. code-block:: python

    class Osoba:
        first_name = 'Matt'
        last_name = 'Kowalski'

        def __str__(self):
            return '{first_name} {last_name}'.format(**self.__dict__)
            return '{first_name} {last_name}'.format(first_name='Matt', last_name='Kowalski')
            return f'{self.first_name} {self.last_name}'

.. code-block:: python

    def wyswietl(*args, **kwargs):
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')

    def function(a, b, c=0):
        x = 4
        y = 5

        wyswietl(**locals())

    function(1, 2)
    # args: ()
    # kwargs: {'a': 1, 'b': 2, 'c': 0, 'x': 4, 'y': 5}


Assignments
===========

Iris
----
#. Dane dostępne są pod adresem: https://raw.githubusercontent.com/AstroMatt/book-python/master/database/data/iris.csv
#. Otwórz link w przeglądarce i skopiuj zawartość do pliku ``kwargs_iris.csv`` na dysku
#. Sparsuj zawartość odrzucając nagłówek
#. Dla każdego rekordu, usuń białe spacje i podziel go po przecinku ``,``
#. Wyniki podziału odbierz do dwóch zmiennych:

    * ``features: Tuple[float]`` - pomiary
    * ``labels: str`` - nazwa gatunku

#. Stwórz funkcję ``print_iris(sepal_length, sepal_width, *args, **kwargs)``, która wyświetli zawartość wszystkich argumentów
#. Odpalaj funkcję ``print_iris()``, podając wartości ``features`` i ``labels``
#. Pomiary mają być podane pozycyjnie (``*``), a gatunek nazwanie (``**``)

:About:
    * Filename: ``kwargs_iris.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 15 min

Hosts
-----
#. Skopiuj zawartość listingu poniżej do pliku ``hosts.txt``

    .. literalinclude:: assignment/etc-hosts.txt
        :language: python
        :caption: Listing pliku ``/etc/hosts``

#. Stwórz pusty ``dict`` o nazwie ``hosts``
#. Czytając plik pomiń puste linie lub zaczynające się od komentarza ``#``
#. Do ``hosts`` dla klucza IP dodaj listę hostname
#. Przy parsowaniu linii skorzystaj z konstrukcji z gwiazdką ``*``

:About:
    * Filename: ``kwargs_hosts.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 15 min
