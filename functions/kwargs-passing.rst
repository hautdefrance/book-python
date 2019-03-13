**********************
Passing many arguments
**********************


Operators ``*`` i ``**``
========================
- To nie jest mnożenie i potęgowanie!
- ``*`` zwykle nazywa się ``*args`` (arguments) - argumenty pozycyjne (anonimowe)
- ``**`` zwykle nazywa się ``**kwargs`` (keyword arguments) - argumenty nazwane
- ``*args`` unpack ``tuple`` or ``list``
- ``**kwargs`` unpack ``dict``


``*`` unpacks ``list`` or ``tuple``
===================================
.. code-block:: python

    complex(3, 5)

.. code-block:: python

    args = (3, 5)
    complex(*args)


``**`` unpacks ``dict``
=======================
.. code-block:: python

    complex(real=3, imag=5)

.. code-block:: python

    kwargs = {'real': 3, 'imag': 5}
    complex(**number)


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

Konwersja Temperatury
---------------------
.. code-block:: python

    from typing import List

    def celsius_to_fahrenheit(*degrees) -> List[float]:
        return [x * 1.8 + 32 for x in degrees]


    celsius_to_fahrenheit(1)
    # [33.8]

    celsius_to_fahrenheit(1, 2, 3, 4, 5)
    # [33.8, 35.6, 37.4, 39.2, 41.0]

Podawanie parametrów do funkcji
-------------------------------
.. code-block:: python

    def rysuj_wykres(a, b, color, linia):
        print(locals())


    rysuj_wykres(1, 2, color='czerwony', linia='przerywana')
    rysuj_wykres(3, 4, color='czerwony', linia='przerywana')
    rysuj_wykres(5, 6, color='czerwony', linia='przerywana')

.. code-block:: python

    def rysuj_wykres(a, b, color, linia):
        print(locals())


    parametry = {
        'color': 'czerwony',
        'linia': 'przerywana',
    }

    rysuj_wykres(1, 2, **parametry)
    rysuj_wykres(3, 4, **parametry)
    rysuj_wykres(5, 6, **parametry)


Placeholder class
-----------------
.. code-block:: python

    DATA = [
        {"sepl": 6.0, "sepw": 3.4, "petl":4.5, "petw": 1.6, "species": "versicolor"},
    ]

    class Iris:
        def __init__(self, sepl, sepw, petl, petw):
            self.sepl = sepl
            self.sepw = sepw
            self.petl = petl
            self.petw = petw


    for row in DATA:
        Iris(**row)

.. code-block:: python

    class Kontakt:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    Kontakt(imie='Jan', nazwisko='Twardowski')
    Kontakt(sepal_length=6.0, sepal_width=3.4, nazwisko='Twardowski')

    DATA = {"sepl": 6.0, "sepw": 3.4, "petl":4.5, "petw": 1.6, "species": "versicolor"}
    Kontakt(**DATA)

Print formatting in classes
---------------------------
.. code-block:: python

    class Osoba:
        first_name = 'Jan'
        last_name = 'Twardowski'

        def __str__(self):
            return '{first_name} {last_name}'.format(**self.__dict__)
            return '{first_name} {last_name}'.format(first_name='Jan', last_name='Twardowski')
            return f'{self.first_name} {self.last_name}'


Calling function with all variables from higher order function
--------------------------------------------------------------
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
* Filename: ``kwargs_iris.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Input data: https://raw.githubusercontent.com/AstroMatt/book-python/master/functions/data/iris.csv

#. Otwórz link w przeglądarce i skopiuj zawartość do pliku na dysku o nazwie ``iris.csv``
#. Stwórz funkcję ``print_iris(sepal_length, sepal_width, *args, **kwargs)``, która wyświetli zawartość wszystkich argumentów za pomocą ``locals()``
#. Sparsuj zawartość pliku ``iris.csv`` odrzucając nagłówek
#. Dla każdego rekordu:

    #. Usuń białe spacje
    #. Podziel po przecinku ``,``
    #. Wyniki podziału zapisz do dwóch zmiennych:

        * ``features: List[float]`` - pomiary
        * ``labels: Dict[str, str]`` - key: słowo ``species``, value: nazwa gatunku

    #. Odpalaj funkcję ``print_iris()``, podając wartości ``features`` i ``labels``
    #. Pomiary mają być podane pozycyjnie (``*``), a gatunek nazwanie (``**``)

