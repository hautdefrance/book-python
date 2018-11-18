.. _OOP Advanced:

************
OOP Advanced
************


``__str__()`` and ``__repr__()``
================================
* ``__repr__`` jest dla developerów (być jednoznacznym),
* ``__str__`` dla użytkowników (być czytelnym).

.. literalinclude:: src/oop-repr.py
    :language: python
    :caption: Using ``__repr__()`` on a class

.. code-block:: python

    import datetime

    datetime.datetime.now()  # ``__repr__``
    # datetime.datetime(2018, 7, 3, 11, 32, 51, 684972)

    print(datetime.datetime.now())  # ``__str__``
    # 2018-07-03 11:32:58.927387


What should be in the class and what not?
=========================================
* Jeżeli metoda w swoim ciele ma ``self`` i z niego korzysta to powinna być w klasie
* Jeżeli metoda nie ma w swoim ciele ``self`` to nie powinna być w klasie
* Jeżeli metoda nie ma w swoim ciele ``self`` ale wybitnie pasuje do klasy, to można ją tam zamieścić oraz dodać dekorator ``@staticmethod``

.. literalinclude:: src/oop-staticmethod-without.py
    :language: python
    :caption: Case Study uzasadnionego użcycia ``@staticmethod``

.. literalinclude:: src/oop-staticmethod-with.py
    :language: python
    :caption: Case Study uzasadnionego użcycia ``@staticmethod``

.. literalinclude:: src/oop-staticmethod-decorator.py
    :language: python
    :caption: Case Study uzasadnionego użcycia ``@staticmethod``


``@staticmethod``
-----------------
* Using class as namespace
* Will not pass instance as a first argument
* ``self`` is not required

.. literalinclude:: src/oop-staticmethod.py
    :language: python
    :caption: Using ``@staticmethod``


Dynamically creating fields
===========================
.. literalinclude:: src/oop-init-dynamic.py
    :language: python
    :caption: Funkcja inicjalizująca, która automatycznie dodaje pola do naszej klasy w zależności od tego co zostanie podane przy tworzeniu obiektu


Setter and Getter
=================

Accessing class fields
----------------------
.. literalinclude:: src/oop-accessor-fields.py
    :language: python
    :caption: Accessing class fields

.. literalinclude:: src/oop-getter.py
    :language: python
    :caption: Case Study uzasadnionego użycia gettera w kodzie

``@property``, ``@x.setter``, ``@x.deleter``
--------------------------------------------
* ``@propery`` - for defining getters
* ``@kola.setter`` - for defining setter
* ``@kola.deleter`` - for defining deleter
* Blokowanie możliwości edycji pola klasy
* Dodawanie logowania przy ustawianiu wartości

.. literalinclude:: src/oop-property.py
    :language: python
    :caption: ``@property``, ``@x.setter``, ``@x.deleter``


Hash
====
* ``set()`` można zrobić z dowolnego hashowalnego obiektu
* ``dict()`` może mieć klucze, które są dowolnym hashowalnym obiektem

.. literalinclude:: src/oop-hash-dict.py
    :language: python
    :caption: ``dict()`` może mieć klucze, które są dowolnym hashowalnym obiektem

.. literalinclude:: src/oop-hash-set.py
    :language: python
    :caption: ``set()`` można zrobić z dowolnego hashowalnego obiektu

.. literalinclude:: src/oop-hash-generate-bad.py
    :language: python
    :caption: Generating hash and object comparision

.. literalinclude:: src/oop-hash-generate-good.py
    :language: python
    :caption: Generating hash and object comparision


``is``
======
* ``is`` porównuje czy dwa obiekty są tożsame
* Najczęściej służy do sprawdzania czy coś jest ``None``

.. code-block:: python

    if name is None:
        print('Name is not set')
    else:
        print('You have set your name')

Bardzo kuszący jest następujący przykład:

 .. code-block:: python

     if name is 'Mark Watney':
        print('You are Space Pirate!')
     else:
        print('You are not pirate at all!')

**Nie jest on jednak do końca poprawny. Słowo kluczowe ``is`` porównuje czy dwa obiekty są tym samym obiektem, nie czy mają taką samą wartość.**
* Poniższy przykład ilustruje, że pomimo że dwa obiekty przechowują takiego samego stringa to nie są sobie tożsame, mimo że są sobie równe.

 .. code-block:: python

    a = 'hello'
    b = 'hello'

    print(f'a is {a}, b is {b}')        # a is hello, b is hello
    print(f'a == b returns: {a==b}')    # a == b returns: True
    print(f'a is b returns: {a is b}')  # a is b returns: True


    print(id(a))  # 4640833352
    print(id(b))  # 4640833352

.. code-block:: python

    a = 'hello'
    b = ''.join('hello')

    print(f'a is {a}, b is {b}')        # a is hello, b is hello
    print(f'a == b returns: {a==b}')    # a == b returns: True
    print(f'a is b returns: {a is b}')  # a is b returns: False

    print(id(a))  # 4640833352
    print(id(b))  # 4662440600



Monkey Patching
===============
.. literalinclude:: src/oop-monkey-patching-1.py
    :language: python
    :caption: Monkey Patching

.. literalinclude:: src/oop-monkey-patching-2.py
    :language: python
    :caption: Monkey Patching

.. literalinclude:: src/oop-monkey-patching-3.py
    :language: python
    :caption: Monkey Patching


Method Resolution Order
=======================
.. figure:: img/inherintace-diamond.jpg
    :scale: 100%
    :align: center

    Inherintace Diamond

.. literalinclude:: src/oop-mro.py
    :language: python
    :caption: Method Resolution Order


Objects and instances
=====================
.. literalinclude:: src/oop-objects-and-instances.py
    :language: python
    :caption: Objects and instances


Metaclass
=========
* Można zmienić, że obiekt nie dziedziczy po ``object``
* Każdy obiekt klasy jest instancją tej klasy
* Każda napisana klasa jest instancją obiektu, który nazywa się metaklasą
* Na 99% tego nie potrzebujesz

.. warning:: więcej na ten temat w rozdziale :ref:`Metaclass`

.. literalinclude:: src/oop-metaclass.py
    :language: python
    :caption: Metaclass


Assignments
===========

Dragon (Part 3)
---------------
#. Dodaj możliwość poruszania się smoka i bohatera w 3 wymiarach
#. Bohater może należeć do drużyny, który może składać się maks z 6 postaci (różnych klas)
#. Żadna z istot na planszy nie może wyjść poza zakres ekranu
#. Bohater może dodatkowo założyć ekwipunek i może być to wiele obiektów na raz
#. Każdy z przedmiotów ma swoją nazwę, typ oraz modyfikator

    * zbroję (dodatkowe punkty obrony, np. +10%)
    * tarczę (dodatkowe punkty obrony, np. +5%)
    * miecz (dodatkowe punkty ataku, np. +5%)

#. Zbroja i tarcza chroni przed uderzeniami obniżając ilość obrażeń o wartość obrony
#. Miecz zwiększa ilość zadawanych obrażeń
#. Obrażenia smoka maleją z sześcianem odległości (zianie ogniem)
#. Bohater nie może zadawać obrażeń jak jest dalej niż 50 punktów od przeciwnika
#. Wszystkie istoty mogą lewelować a bazowe punty życia i obrażeń się zmieniają z poziomem
#. Przeprowadź symulację walki. Kto zginie pierwszy?

:About:
    * Filename: ``oop_dragon_3.py``
    * Lines of code to write: 50 lines
    * Estimated time of completion: 30 min
