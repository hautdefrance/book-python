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

.. literalinclude:: src/oop-class-1.py
    :language: python
    :caption: Defining and naming classes with single word names

.. literalinclude:: src/oop-class-2.py
    :language: python
    :caption: Defining and naming classes with ``CamelCase`` names

Classes vs Objects
==================
* Objects, Instances
* ``snake_case`` names

.. literalinclude:: src/oop-objects-1.py
    :language: python
    :caption: Classes and Objects

.. literalinclude:: src/oop-objects-2.py
    :language: python
    :caption: Classes and Objects


Fields
======
* Fields, Properties, Attributes
* ``snake_case`` names

.. literalinclude:: src/oop-fields.py
    :language: python
    :caption: Fields


Methods
=======
* Methods are functions in the class
* ``self`` - Instance as an argument
* przy uruchomieniu funkcji nie podajemy jawnie argumentu ``self``

Simple Methods
--------------
.. literalinclude:: src/oop-methods-1.py
    :language: python
    :caption: Simple Methods

Methods accessing fields
------------------------
.. literalinclude:: src/oop-methods-2.py
    :language: python
    :caption: Methods accessing fields

Methods with default arguments
------------------------------
.. literalinclude:: src/oop-methods-args.py
    :language: python
    :caption: Methods with arguments

Methods with default arguments
------------------------------
.. literalinclude:: src/oop-methods-args-default.py
    :language: python
    :caption: Methods with default arguments

Methods call other methods
--------------------------
.. literalinclude:: src/oop-methods-call-another.py
    :language: python
    :caption: Methods call other methods


Initializer Method
==================
* ``__init__()`` to nie konstruktor
* Domyślny ``__init__()`` gdy niezdefiniowaliśmy własnego
* Inicjalizacja pól klasy tylko w ``__init__``

.. literalinclude:: src/oop-init.py
    :language: python
    :caption: ``__init__()`` - Initializer Method


Stringify object
================
* print converts it's arguments to ``str()`` automatically before printing

.. literalinclude:: src/oop-str-without.py
    :language: python
    :caption: Print object without ``__str__()`` method overloaded

.. literalinclude:: src/oop-str-with.py
    :language: python
    :caption: Stringify object


One class per file?
===================
* Osobne pliki - gdy klasy są duże
* Jeden plik - gdy klasy są małe i czytelne

    .. literalinclude:: src/oop-objects-2.py
        :language: python
        :caption: Classes and Objects


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

Defining Classes
----------------
* Filename: ``oop_iris.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min

#. Stwórz klasy ``Virginica``, ``Versicolor``, ``Setosa``, które będą identyczne do ``Iris``.
#. Klasy ``Virginica``, ``Versicolor``, ``Setosa`` mają mieć pole species wypełnione odpowiednio do nazwy gatunku.
#. Iterując po ``DATA`` z :numref:`listing-oop-classes` twórz obiekty klasy odpowiedniej dla nazwy gatunku (ostatni rekord każdej z krotek).
#. Obiekt inicjalizuj danymi z pomiarów.
#. Na ekranie wyświetlaj nazwę gatunku oraz sumę i średnią z pomiarów.

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

Basic Address Book
------------------
* Filename: ``oop_addressbook_basic.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min

#. Dla danych z listingu poniżej napisz książkę adresową

    .. literalinclude:: assignment/oop_addressbook.json
        :language: json
        :caption: Address Book

#. W zadaniu mamy doczynienia z trzema klasami, wymień je.
#. Zamodeluj problem wykorzystując trzy klasy i relacje między nimi
#. Użytkownik może mieć wiele adresów
#. Użytkownik może nie mieć żadnego adresu

:The whys and wherefores:
    * myślenie obiektowe i odwzorowanie struktury w programie
    * praca z obiektami
    * zagnieżdżanie obiektów
    * rzutowanie obiektu na stringa oraz jego reprezentacja (które i kiedy użyć)


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

#. Smok ma mieć:

    * nazwę smoka
    * pozycja ``x`` na ekranie
    * pozycja ``y`` na ekranie
    * teksturę, domyślnie ``img/dragon/alive.png``
    * punkty życia, domyślnie losowy ``int`` z zakresu od 50 do 100

#. Smok może:

    * otrzymywać obrażenia
    * zadawać komuś losowe obrażenia z przedziału od 5 do 20
    * być ustawiony w dowolne miejsce ekranu
    * być przesuwany o zadaną liczbę punktów w którymś z kierunków

#. Jeżeli konieczne jest wprowadzenie nowej metody, klasy lub pól to należy to zrobić
#. Nie musisz trzymać się kolejności punktów i podpunktów w zadaniu
#. Przyjmij górny lewy róg ekranu za punkt (0, 0)

    * idąc w prawo dodajesz ``x``
    * idąc w lewo odejmujesz ``x``
    * idąc w górę odejmujesz ``y``
    * idąc w dół dodajesz ``y``

#. Przy każdym obrażeniu wypisz na ekranie nazwę smoka, ilość obrażeń i pozostałe punkty życia
#. Nie można zadawać smokowi obrażeń, jeżeli już nie żyje
#. Kiedy punkty życia smoka spadną do, lub poniżej zera:

    * ustaw status obiektu na ``dead``
    * na ekranie ma pojawić się napis 'XXX is dead' gdzie XXX to nazwa smoka
    * zmień teksturę smoka na ``img/dragon/dead.png``
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
