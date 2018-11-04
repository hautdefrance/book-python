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
    :caption: Classes

.. literalinclude:: src/oop-class-2.py
    :language: python
    :caption: Classes

Classes vs Objects
==================
* Objects, Instances
* ``snake_case`` names

.. literalinclude:: src/oop-objects.py
    :language: python
    :caption: Classes and Objects


Fields
======
* Fields, Properties, Attributes
* ``snake_case`` names
* Require ``__init__()``

.. literalinclude:: src/oop-fields.py
    :language: python
    :caption: Fields


Methods
=======
* Methods are functions in the class
* ``self`` - Instance as an argument
* przy uruchomieniu funkcji nie podajemy jawnie argumentu ``self``

.. literalinclude:: src/oop-methods.py
    :language: python
    :caption: Methods


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
* Jeden plik - gdy klasy są małe i czytelne
* Osobne pliki - gdy klasy są duże


Assignments
===========

Basic Address Book
------------------
#. Dla danych z :numref:`listing-oop-addressbook-data` napisz książkę adresową
#. Wszystkie dane w książce muszą być reprezentowane przez klasy
#. Użytkownik może mieć wiele adresów
#. Użytkownik może nie mieć żadnego adresu

:About:
    * Filename: ``oop_addressbook_basic.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 20 min

:The whys and wherefores:
    * myślenie obiektowe i odwzorowanie struktury w programie
    * praca z obiektami
    * zagnieżdżanie obiektów
    * rzutowanie obiektu na stringa oraz jego reprezentacja (które i kiedy użyć)

.. literalinclude:: assignment/oop_addressbook.txt
    :name: listing-oop-addressbook-data
    :language: python
    :caption: Address Book

Address Book from API
---------------------
#. Dla danych z listingu
#. API programu powinno być tak jak na :numref:`listing-oop-addressbook-py`
#. Zrób tak, aby się ładnie wyświetlało zarówno dla jednego wyniku jak i dla wszystkich w książce
#. ``Address`` ma mieć zmienną liczbę argumentów
#. Jeżeli argument jest różny od ``None`` powinien być dynamicznie ustawiony (``setattr()``).

:About:
    * Filename: ``oop_addressbook_api.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 20 min

:The whys and wherefores:
    * Korzystanie z ``.__str__()``
    * Dynamiczne tworzenie pól w obiekcie

.. literalinclude:: src/oop_addressbook.py
    :name: listing-oop-addressbook-py
    :language: python
    :caption: Address Book

Bank i Bankomaty
----------------
#. Klient może otworzyć konto w banku
#. Bank może mieć wiele kont dla różnych klientów
#. Każde konto ma unikalny numer, który jest generowany przy zakładaniu
#. Klient może odpytać o swój numer
#. Klient może wpłacić pieniądze na swoje konto
#. Klient może wybrać pieniądze z bankomatu

:About:
    * Filename: ``oop_bank.py``
    * Lines of code to write: 60 lines
    * Estimated time of completion: 20 min
