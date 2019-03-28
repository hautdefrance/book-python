.. _Iterators:

*********
Iterators
*********


What is iterator?
=================
* ``__iter__()``
* ``__next__() -> raise StopIteration``


Iterowanie po obiektach
=======================

Iterowanie po ``str``
---------------------
.. code-block:: python

    for character in 'hello':
        print(character)

    # h
    # e
    # l
    # l
    # o


Iterowanie po ``list()``, ``dict()``, ``set()``, ``tuple()``
------------------------------------------------------------
.. code-block:: python

    for liczba in [1, 2, 3, 4]:
        print(liczba)

.. code-block:: python

    for key, value in [('a',1), ('b',2), ('c',3)]:
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3

.. code-block:: python

    my_dict = {'a': 1, 'b': 2, 'c': 3}

    for key in my_dict:
        value = my_dict.get(key)
        print(value)

    # 1
    # 2
    # 3


    for key, value in my_dict.items():
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3


Własny iterator
===============

.. code-block:: python

    class ListaFigurGeometrycznych:
        lista = []
        aktualny_elemtent = 0

        def __iter__(self):
            self.aktualny_elemtent = 0
            return self

        def push(self, figura):
            self.lista.append(figura)

        def __next__(self):
            if self.aktualny_elemtent >= len(self.lista):
                raise StopIteration

            element = self.lista[self.aktualny_elemtent]
            self.aktualny_elemtent += 1
            return element


    figury = ListaFigurGeometrycznych()

    figury.push('kwadrat')
    figury.push('prostokat')
    figury.push('trojkat')

    for figura in figury:
        print(figura)

.. code-block:: python

    class Parking:
        def __init__(self):
            self.zaparkowane_samochody = []
            self.index = 0

        def zaparkuj(self, samochod):
            self.zaparkowane_samochody.append(samochod)

        def __iter__(self):
            self.index = 0
            return self

        def __next__(self):
            if self.index >= len(self.zaparkowane_samochody):
                raise StopIteration

            samochod = self.zaparkowane_samochody[self.index]
            self.index += 1
            return samochod


    parking = Parking()
    parking.zaparkuj('Mercedes')
    parking.zaparkuj('Maluch')
    parking.zaparkuj('Toyota')


    for samochod in parking:
        print(samochod)


``itertools``
=============
.. code-block:: python

    from itertools import cycle

    DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
    ]

    def get_species(species):
        for record in DATA:
            if record[4] == species:
                yield record

    data = get_species('setosa')

    cycle(data)



Przykład
========

.. code-block:: python

    def parzyste_f4():
        for x in range(0, 30):
            if x % 2 == 0:
                yield float(x)


    print(parzyste_f4())
    a = parzyste_f4()

    try:
        print('next1', a.__next__())
        print('next2', a.__next__())
        print('next3', a.__next__())
        print('next4', a.__next__())
    except StopIteration:
        pass


    for liczba in parzyste_f4():
        print(liczba)


Assignments
===========

Range
-----
* Filename: ``iterator_range.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min

#. Zaimplementuj własne rozwiązanie ``range()`` wykorzystując iterator.
#. Początek, koniec, krok (step)

Książka adresowa
----------------
* Filename: ``iterator_addressbook.py``
* Lines of code to write: 20 lines
* Estimated time of completion: 15 min
* Input data: :numref:`listing-iterators-ksiazka-adresowa`

#. spraw aby można było iterować w książce adresowej z poprzednich zadań po adresach użytkownika.

.. literalinclude:: src/iterators-ksiazka-adresowa.py
    :name: listing-iterators-ksiazka-adresowa
    :language: python
    :caption: Struktury danych książki adresowej
