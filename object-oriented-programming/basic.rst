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
* ``CamelCase`` names

.. code-block:: python
    :caption: Defining and naming classes with single word names

    class Astronaut:
        pass

.. code-block:: python
    :caption: Defining and naming classes with ``CamelCase`` names

    class CosmonautPilot:
        pass


Classes vs Objects
==================
* Objects, Instances
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
* Fields, Properties, Attributes
* ``snake_case`` names

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
* ``self`` - Instance as an argument
* przy uruchomieniu funkcji nie podajemy jawnie argumentu ``self``

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
* ``__init__()`` to nie konstruktor
* Domyślny ``__init__()`` gdy niezdefiniowaliśmy własnego
* Inicjalizacja pól klasy tylko w ``__init__``

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
* print converts it's arguments to ``str()`` automatically before printing

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


Inheritance
===========
.. code-block:: python

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    class Virginica(Iris):
        pass

    class Setosa(Iris):
        pass

    class Versicolor(Iris):
        pass


    setosa = Setosa(
        sepal_length=5.1,
        sepal_width=3.5,
        petal_length=1.4,
        petal_width=0.2,
        species='setosa'
    )

Relations
=========
.. code-block:: python

    class Address:
        def __init__(self, street=None, city=None, country=None):
            self.street = street
            self.city = city
            self.country = country


    class Contact:
        def __init__(self, first_name, last_name, addresses=()):
            self.first_name = first_name
            self.last_name = last_name
            self.address = addresses


    twardowski = Contact(first_name='Jan', last_name='Twardowski', address=[
        Address(street='Kamienica Pod św. Janem Kapistranem', city='Kraków', country='Poland'),
        Address(street='2101 E NASA Pkwy', city='Houston', country='USA'),
        Address(city='Kennedy Space Center', country='USA'),
    ])


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

Defining Classes
----------------
* Filename: ``oop_iris.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Input data: :numref:`listing-oop-classes`

.. code-block:: python
    :caption: Iris sample dataset
    :name: listing-oop-classes

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (4.6, 3.1, 1.5, 0.2, 'setosa'),
    ]

#. Stwórz ``flowers: list``
#. Stwórz klasy ``Virginica``, ``Versicolor``, ``Setosa``, które będą identyczne do ``Iris``
#. Iterując po ``DATA`` z :numref:`listing-oop-classes`:

    #. Twórz obiekty klasy odpowiedniej dla nazwy gatunku (ostatni rekord każdej z krotek)
    #. Obiekt inicjalizuj danymi z pomiarów
    #. Obiekt dodaj do listy ``flowers``

#. Na ekranie wyświetlaj nazwę gatunku oraz sumę i średnią z pomiarów.

:Dla chętnych:
    #. Wynik sformatuj aby wyglądał jak tabelka:

        .. code-block:: text

            Species    Total   Avg
            ----------------------
             virginica  15.5  3.88
                setosa  10.2  2.55
            versicolor  13.9  3.48
             virginica  16.6  4.15
            versicolor  15.6  3.90
                setosa   9.4  2.35
            versicolor  16.3  4.07
             virginica  19.3  4.83
                setosa   9.5  2.38
                setosa   9.4  2.35

Basic Address Book
------------------
* Filename: ``oop_addressbook_basic.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min

#. Dla danych z listingu poniżej napisz książkę adresową

    .. literalinclude:: assignment/oop_addressbook.json
        :language: json
        :caption: Address Book

#. W zadaniu mamy do czynienia z trzema klasami, wymień je.
#. Zamodeluj problem wykorzystując trzy klasy i relacje między nimi
#. Użytkownik może mieć wiele adresów
#. Użytkownik może nie mieć żadnego adresu

:The whys and wherefores:
    * myślenie obiektowe i odwzorowanie struktury w programie
    * praca z obiektami
    * zagnieżdżanie obiektów
    * rzutowanie obiektu na ``str`` oraz jego reprezentacja (które i kiedy użyć)

Address Book from API
---------------------
* Filename: ``oop_addressbook_api.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min

#. API programu powinno być tak jak na :numref:`listing-oop-addressbook-py`
#. Zrób tak, aby się ładnie wyświetlało zarówno dla jednego wyniku jak i dla wszystkich w książce
#. ``Address`` ma mieć zmienną liczbę argumentów

:The whys and wherefores:
    * Korzystanie z ``.__str__()``

.. literalinclude:: assignment/oop_addressbook.py
    :name: listing-oop-addressbook-py
    :language: python
    :caption: Address Book

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
