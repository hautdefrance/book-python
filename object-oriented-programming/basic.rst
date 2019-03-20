.. _OOP Basic:

*********
OOP Basic
*********


Object Paradigm
===============
* Model world as objects that interacts with each other

.. glossary::

    class
        Templates for objects.

    objects
        Instances of a class.

    method
        Function inside the class.

    field
        Variable inside the class.
        Also known as "Properties" or "Attributes"


Classes
=======
* Capitalized ``CamelCase`` name convention
* Classes are templates for objects

.. code-block:: python
    :caption: Defining class. Classes should have capitalized name

    class Iris:
        pass

.. code-block:: python
    :caption: Classes should have ``CamelCase`` names

    class IrisSetosa:
        pass

Classes vs Instances
--------------------
* Instances are also known as Objects
* Two newlines between class and code
* ``snake_case`` names

.. code-block:: python
    :caption: One class and one instance

    class Iris:
        pass


    flower = Iris()

.. code-block:: python
    :caption: One class and three instances

    class Iris:
        pass


    setosa = Iris()
    versicolor = Iris()
    virginica = Iris()

.. code-block:: python
    :caption: Three classes and three instances

    class Setosa:
        pass

    class Versicolor:
        pass

    class Virginica:
        pass


    iris_setosa = Setosa()
    iris_versicolor = Versicolor()
    iris_virginica = Virginica()


Fields
======
* Fields are also known as "Properties" or "Attributes"
* ``snake_case`` name convention
* Fields are defined in ``__init__()`` method
* Fields store information for instances

.. code-block:: python
    :caption: Classes can have multiple fields. All fields should be initialized in ``__init__()`` method.

    class Iris:
        def __init__(self):
            self.sepal_length = 5.1
            self.sepal_width = 3.5
            self.petal_length = 1.4
            self.petal_width = 0.2
            self.species = 'setosa'


    flower = Iris()

    print(flower.sepal_length)  # 5.1
    print(flower.sepal_width)   # 3.5
    print(flower.species)       # 'setosa'


Initializer Method
==================
* ``__init__()`` is not a constructor!
* It's a first method run after object is initiated
* All classes has default ``__init__()``
* Initialize all fields only in ``__init__``

.. code-block:: python
    :caption: Class initialization

    class Iris:
        def __init__(self, species):
            self.species = species


    setosa = Iris(species='setosa')
    print(setosa.species)
    # setosa

    virginica = Iris('virginica')
    print(virginica.species)
    # virginica

    versicolor = Iris()
    # TypeError: __init__() missing 1 required positional argument: 'species'

.. code-block:: python
    :caption: Method argument with default value

    class Iris:
        def __init__(self, species=None):
            self.species = species


    setosa = Iris(species='setosa')
    print(setosa.species)
    # setosa

    virginica = Iris('virginica')
    print(virginica.species)
    # virginica

    versicolor = Iris()
    # None


Methods
=======
* Methods are functions in the class
* First argument is always instance (``self``)
* While calling function you never pass ``self``

Simple Methods
--------------
.. code-block:: python
    :caption: Simple Methods

    class Iris:
        def __init__(self):
            self.species = 'setosa'

        def latin_name(self):
            print(f'Latin name is: Iris setosa')


    flower = Iris()
    flower.latin_name()
    # Latin name is: Iris setosa

Methods accessing fields
------------------------
.. code-block:: python
    :caption: Methods accessing fields

    class Iris:
        def __init__(self):
            self.species = 'setosa'

        def latin_name(self):
            print(f'Latin name is: Iris {self.species}')


    flower = Iris()
    flower.latin_name()
    # Latin name is: Iris setosa

Methods with argument
---------------------
.. code-block:: python
    :caption: Methods with arguments

    class Iris:
        def latin_name(self, species):
            print(f'Iris {species}')


    flower = Iris()

    flower.latin_name(species='setosa')  # Iris setosa
    flower.latin_name('setosa')          # Iris setosa
    flower.latin_name()                  # TypeError: latin_name() missing 1 required positional argument: 'species'

Methods with arguments with default value
-----------------------------------------
.. code-block:: python
    :caption: Methods with default arguments

    class Iris:
        def latin_name(self, species='unknown'):
            print(f'Iris {species}')


    flower = Iris()

    flower.latin_name(species='setosa')  # Iris setosa
    flower.latin_name('setosa')          # Iris setosa
    flower.latin_name()                  # Iris unknown

Methods calling other methods
-----------------------------
.. code-block:: python
    :caption: Methods call other methods

    class Iris:
        def __init__(self):
            self.sepal_length = 5.1
            self.sepal_width = 3.5
            self.petal_length = 1.4
            self.petal_width = 0.2
            self.species = 'setosa'

        def sepal_area(self):
            return self.sepal_length * self.sepal_width

        def petal_area(self):
            return self.petal_length * self.petal_width

        def total_area(self):
            area = self.sepal_area() + self.petal_area()
            print(f'Total area is: {area:.1f}')


    flower = Iris()
    flower.total_area()
    # Total area is: 18.1


One class per file?
===================
* Osobne pliki - gdy klasy są duże
* Jeden plik - gdy klasy są małe i czytelne

.. code-block:: python
    :caption: Classes and Objects

    class Setosa:
        pass

    class Versicolor:
        pass

    class Virginica:
        pass


    setosa = Setosa()
    versicolor = Versicolor()
    virginica = Virginica()


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

#. Przyjmij górny lewy róg ekranu za punkt (``x=0``, ``y=0``)

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
