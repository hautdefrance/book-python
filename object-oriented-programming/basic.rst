.. _OOP Basic:

*********
OOP Basic
*********


Object Paradigm
===============
* Odwzorowanie świata na obiekty i relacje między nimi
* Class
* Objects, Instances
* Fields, Properties, Attributes
* Methods


Classes
=======
* ``CamelCase`` name convention
* Classes are templates for objects

.. code-block:: python
    :caption: Defining and naming classes with single word names

    class Astronaut:
        pass

.. code-block:: python
    :caption: Defining and naming classes with ``CamelCase`` names

    class CosmonautPilot:
        pass

Classes vs Objects
------------------
* Objects also known as Instances
* ``snake_case`` names

.. code-block:: python
    :caption: Classes and Objects

    class Astronaut:
        pass


    twardowski = Astronaut()
    mark_watney = Astronaut()


.. code-block:: python
    :caption: Classes and Objects

    class Astronaut:
        pass


    class Cosmonaut:
        pass


    mark = Astronaut()
    ivan = Cosmonaut()


Fields
======
* Fields are also known as "Properties" or "Attributes"
* ``snake_case`` name convention
* Fields are defined in ``__init__()`` method
* Fields store information for instances

.. code-block:: python
    :caption: Fields

    class Astronaut:
        def __init__(self):
            self.first_name = 'Jan'
            self.last_name = 'Twardowski'
            self.agency = 'POLSA'


    twardowski = Astronaut()

    print(twardowski.first_name)  # Jan
    print(twardowski.last_name)   # Twardowski
    print(twardowski.agency)      # POLSA


Methods
=======
* Methods are functions in the class
* First argument is always ``self`` (instance)
* While calling function you never pass ``self``

Simple Methods
--------------
.. code-block:: python
    :caption: Simple Methods

    class Astronaut:
        def say_something(self):
            print("That's one small step for [a] man, one giant leap for mankind.")


    neil = Astronaut()
    neil.say_something()
    # That's one small step for [a] man, one giant leap for mankind.

Methods accessing fields
------------------------
.. code-block:: python
    :caption: Methods accessing fields

    class Astronaut:
        def __init__():
            self.name = 'José Jiménez'

        def say_something(self):
            print(f'My name... {self.name}')


    jose = Astronaut()
    jose.say_hello()
    # My name... José Jiménez!

Methods with default arguments
------------------------------
.. code-block:: python
    :caption: Methods with arguments

    class Astronaut:
        def say_hello(self, text):
            print(text)


    jose = Astronaut()

    jose.say_hello(text='Privyet')     # Privyet
    jose.say_hello('Hello')            # Hello
    jose.say_hello()                   # TypeError: say_text() missing 1 required positional argument: 'text'

Methods with default arguments
------------------------------
.. code-block:: python
    :caption: Methods with default arguments

    class Astronaut:
        def say_hello(self, text='Ehlo World!'):
            print(text)


    jose = Astronaut()

    jose.say_hello(text='Privyet')     # Privyet
    jose.say_hello('Hello')            # Hello
    jose.say_hello()                   # Ehlo World!

Methods call other methods
--------------------------
.. code-block:: python
    :caption: Methods call other methods

    class Astronaut:
        def say_hello(self):
            name = self.get_name()
            print(f'My name... {name}')

        def get_name(self):
            return 'José Jiménez'


    jose = Astronaut()

    jose.say_hello()    # My name... José Jiménez!
    jose.get_name()     # 'José Jiménez!'


Initializer Method
==================
* ``__init__()`` is not a constructor!
* All classes has default ``__init__()``
* Initialize all fields only in ``__init__``

.. code-block:: python
    :caption: ``__init__()`` - Initializer Method

    class Astronaut:
        def __init__(self):
            self.first_name = 'Jan'
            self.last_name = 'Twardowski'
            self.agency = 'POLSA'


    twardowski = Astronaut()

    print(twardowski.first_name)  # Jan
    print(twardowski.last_name)   # Twardowski
    print(twardowski.agency)      # POLSA

.. code-block:: python
    :caption: ``__init__()`` - Initializer Method

    class Astronaut:
        def __init__(self, first_name, last_name, agency='NASA'):
            self.first_name = first_name
            self.last_name = last_name
            self.agency = agency


    jose = Astronaut(first_name='José', last_name='Jiménez')
    ivan = Astronaut(first_name='Иван', last_name='Иванович', agency='Roscosmos')

    print(jose.first_name)  # José
    print(jose.last_name)   # Jiménez
    print(jose.agency)      # NASA

    print(ivan.first_name)  # Иван
    print(ivan.last_name)   # Иванович
    print(ivan.agency)      # Roscosmos


Stringify object
================
* ``print`` converts it's arguments to ``str()`` before printing

.. code-block:: python
    :caption: Print object without ``__str__()`` method overloaded

    class Astronaut:
        def __init__(self, name):
            self.name = name


    jose = Astronaut(name='José Jiménez')

    str(jose)       # <__main__.Astronaut object at 0x01E3FDF0>
    print(jose)     # <__main__.Astronaut object at 0x01E3FDF0>

.. code-block:: python
    :caption: Stringify object

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f'My name... {self.name}'


    jose = Astronaut(name='José Jiménez')

    str(jose)       # My name... José Jiménez
    print(jose)     # My name... José Jiménez


One class per file?
===================
* Osobne pliki - gdy klasy są duże
* Jeden plik - gdy klasy są małe i czytelne

.. code-block:: python
    :caption: Classes and Objects

    class Astronaut:
        pass


    class Cosmonaut:
        pass


    jose = Astronaut()
    ivan = Cosmonaut()


Assignments
===========

Defining Classes
----------------
* Filename: ``oop_iris.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min

#. Stwórz klasę ``Iris`` z polami:

    - ``sepal_length: float``,
    - ``sepal_width: float``,
    - ``petal_length: float``,
    - ``petal_width: float``,
    - ``species: str``.

#. Napisz metodę ``total()`` wyliczającą sumę dla pól numerycznych
#. Napisz metodę ``average()`` wyliczającą średnią dla pól numerycznych
#. Stwórz obiekt ``setosa`` z pomiarami:

    * sepal_length: 5.4
    * sepal_width: 3.9
    * petal_length: 1.3
    * petal_width: 0.4

#. Wyświetl na ekranie nazwę gatunku oraz sumę i średnią z pomiarów.

Dragon (Part 1)
---------------
* Filename: ``oop_dragon_1.py``
* Lines of code to write: 100 lines
* Estimated time of completion: 75 min
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif
    :scale: 100%
    :align: center

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn

#. Nie musisz trzymać się kolejności punktów i podpunktów w zadaniu
#. Jeżeli konieczne jest wprowadzenie nowej metody, klasy lub pól to należy to zrobić
#. Smok ma mieć:

    * nazwę
    * pozycję ``x`` na ekranie
    * pozycję ``y`` na ekranie
    * nazwę pliku tekstury, domyślnie ``img/dragon/alive.png``
    * punkty życia, domyślnie losowy ``int`` z zakresu od 50 do 100

#. Smok może:

    * być ustawiony w dowolne miejsce ekranu
    * zadawać komuś losowe obrażenia z przedziału od 5 do 20
    * otrzymywać obrażenia
    * być przesuwany o zadaną liczbę punktów w którymś z kierunków

#. Przyjmij górny lewy róg ekranu za punkt (0, 0)

    * idąc w prawo dodajesz ``x``
    * idąc w lewo odejmujesz ``x``
    * idąc w górę odejmujesz ``y``
    * idąc w dół dodajesz ``y``

#. Przy każdym obrażeniu wypisz na ekranie nazwę smoka, ilość obrażeń i pozostałe punkty życia
#. Nie można zadawać smokowi obrażeń, jeżeli już nie żyje
#. Kiedy punkty życia smoka spadną do, lub poniżej zera:

    * ustaw status obiektu na ``dead``
    * na ekranie ma pojawić się napis ``XXX is dead`` gdzie XXX to nazwa smoka
    * zmień nazwę pliku tekstury na ``img/dragon/dead.png``
    * na ekranie pojawi się informacja ile złota smok wyrzucił (losowa 1-100)
    * na ekranie pojawi się informacja o pozycji gdzie smok zginął

#. Przeprowadź grę:

    * Stwórz smoka w pozycji x=50, y=120 i nazwij go Wawelski
    * Ustaw nową pozycję na x=10, y=20
    * Przesuń smoka o 10 w lewo i 20 w dół
    * Przesuń smoka o 10 w lewo i 15 w prawo
    * Przesuń smoka o 15 w prawo i 5 w górę
    * Przesuń smoka o 5 w dół
    * Zadaj 10 obrażeń smokowi
    * Zadaj 5 obrażeń smokowi
    * Zadaj 3 obrażeń smokowi
    * Zadaj 2 obrażeń smokowi
    * Zadaj 15 obrażeń smokowi
    * Zadaj 25 obrażeń smokowi
    * Zadaj 75 obrażeń smokowi
