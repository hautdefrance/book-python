.. _OOP Intermediate:

****************
OOP Intermediate
****************


Fields
======

Static Fields
-------------
* Simple to use
* Must have default values
* Share state

.. literalinclude:: src/oop-fields-static.py
    :language: python
    :caption: Static Fields

Dynamic Fields
--------------
* Require ``__init__()``

.. literalinclude:: src/oop-fields-dynamic.py
    :language: python
    :caption: Dynamic fields

Static vs. Dynamic Fields
-------------------------
.. literalinclude:: src/oop-fields-static-vs-dynamic.py
    :language: python
    :caption: Static vs. Dynamic fields

``__dict__`` - Getting dynamic fields and values
------------------------------------------------
.. literalinclude:: src/oop-fields-dict.py
    :language: python
    :caption: ``__dict__`` - Getting dynamic fields and values


Initial arguments mutability and shared state
=============================================
.. literalinclude:: src/oop-init-shared-state.py
    :language: python
    :caption: Initial arguments mutability and shared state


Inheritance
===========
.. literalinclude:: src/oop-inheritance.py
    :language: python
    :caption: Inheritance

Multilevel Inheritance
----------------------
.. literalinclude:: src/oop-inheritance-multilevel.py
    :language: python
    :caption: Multilevel Inheritance

Multiple Inheritance
--------------------
.. literalinclude:: src/oop-inheritance-multiple.py
    :language: python
    :caption: Multiple Inheritance

``super()`` - Calling object parent
-----------------------------------
.. literalinclude:: src/oop-super.py
    :language: python
    :caption: Using ``super()`` on a class


More advanced topics
====================
.. note:: The topic will be continued in :ref:`OOP Advanced` chapter


Assignments
===========

Dragon (Part 2)
---------------
.. figure:: img/dragon.gif
    :scale: 100%
    :align: center

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn

#. Zaimportuj smoka z poprzedniej części zadania ("Part 1")
#. Wykorzystaj mechanizm dziedziczenia dla Smoka
#. Nie modyfikuj klasy smoka z poprzedniej części
#. Smok nie może wyjść poza obszar ekranu (1024x768) + napisz ``doctest``
#. Jeżeli dojdzie do granicy ekranu, to przesuwając dalej, pozycja będzie ustawiona na maks
#. Zmień smokowi punkty życia na losowy ``int`` z zakresu 100 do 150
#. Stwórz bohatera (José Jiménez):

    * losowe punkty życia (200-250)
    * zadaje losowe obrażenia (1-15)
    * klasa postaci (domyślnie "Warrior")
    * Bohater może przyjmować obrażenia
    * Bohater może zginąć
    * Bohater może poruszać się po planszy

#. Wszystkie istoty mają statusy:

    * "Full Health" - gdy punkty życia 100% (zastąp status "alive")
    * "Injured" - gdy punkty życia 99% - 75%
    * "Badly Wounded" - gdy punkty życia 75% - 25%
    * "Near Death" - gdy punkty życia 25% - 1%
    * "Dead" - gdy punkty życia poniżej lub równe 0%

#. Bohater przejmuje złoto smoka, jeżeli go zabije
#. Przeprowadź walkę, tak długo aż ktoś pierwszy nie zginie
#. Jeżeli konieczne jest wprowadzenie nowej metody, klasy lub pól to należy to zrobić

:About:
    * Filename: ``oop_dragon_2.py``
    * Lines of code to write: 120 lines
    * Estimated time of completion: 60 min
    * Don't delete code, assignment will be continued

:Hint:
    * Aby zaimportować trzeba najpierw w katalogu stworzyć pusty plik ``__init__.py``

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
