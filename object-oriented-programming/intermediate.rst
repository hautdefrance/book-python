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

Dragon (Easy)
-------------
.. note:: Jeżeli konieczne jest wprowadzenie nowej metody, klasy lub pól to należy to zrobić

#. Skopiuj kod gry z listingu :numref:`listing-oop-dragon`
#. Smok ma mieć:

    * nazwę smoka
    * pozycja ``x`` na ekranie
    * pozycja ``y`` na ekranie
    * teksturę, domyślnie ``dragon.png``
    * punkty życia, domyślnie losowy ``int`` z zakresu od 50 do 100

#. Smok może:

    * otrzymywać obrażenia
    * zadawać komuś losowe obrażenia z przedziału od 5 do 20
    * być ustawiony w dowolne miejsce ekranu
    * być przesuwany o zadaną liczbę punktów w którymś z kierunków

#. Przyjmij górny lewy róg ekranu za punkt (0, 0)

    * idąc w prawo dodajesz ``x``
    * idąc w lewo odejmujesz ``x``
    * idąc w górę odejmujesz ``y``
    * idąc w dół dodajesz ``y``

#. Przy każdym obrażeniu wypisz na ekranie nazwę smoka, ilość obrażeń i pozostałe punkty życia
#. Kiedy punkty życia smoka spadną do, lub poniżej zera:

    * ustaw status obiektu na ``dead``
    * na ekranie ma pojawić się napis 'Dragon is dead'
    * zmień teksturę smoka na ``dragon-dead.png``
    * na ekranie pojawi się informacja ile złota smok wyrzucił (losowa 1-100)
    * na ekranie pojawi się informacja o pozycji gdzie smok zginął

#. Nie można zadawać smokowi obrażeń, jeżeli już nie żyje
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

:About:
    * Filename: ``oop_dragon_easy.py``
    * Lines of code to write: 40 lines
    * Estimated time of completion: 75 min

.. literalinclude:: assignment/oop_dragon.py
    :name: listing-oop-dragon
    :language: python
    :caption: Dragon API

Dragon (Medium)
-----------------
.. note:: Jeżeli konieczne jest wprowadzenie nowej metody, klasy lub pól to należy to zrobić

#. Zaimportuj smoka z zadania podstawowego rozszerz go przez dziedziczenie
#. Smok nie może wyjść poza obszar ekranu (1024x768) + ``napis doctest``
#. Jeżeli dojdzie do granicy ekranu, to przesuwając dalej, pozycja będzie ustawiona na maks
#. Zmień smokowi punkty życia na losowy ``int`` z zakresu 100 do 150
#. Stwórz bohatera (José Jiménez):

    * losowe punkty życia (100-150)
    * zadaje losowe obrażenia (1-15)
    * klasa postaci (domyślnie "wojownik")

#. Wszystkie istoty mają statusy:

    * "Pełnia życia" (zastąp status "alive") - gdy punkty życia 100%
    * "Lekko Ranny" - gdy punkty życia 99% - 75%
    * "Poważnie ranny" - gdy punkty życia 75% - 25%
    * "Na skraju śmierci" - gdy punkty życia poniżej 25%

#. Bohater przejmuje złoto smoka, jeżeli go zabije
#. Przeprowadź symulację walki. Kto zginie pierwszy?

:About:
    * Filename: ``oop_dragon_medium.py``
    * Lines of code to write: 100 lines
    * Estimated time of completion: 60 min

:Hint:
    * Aby zaimportować trzeba najpierw w katalogu stworzyć pusty plik ``__init__.py``

Dragon (Advanced)
-----------------
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
    * Filename: ``oop_dragon_advanced.py``
    * Lines of code to write: 50 lines
    * Estimated time of completion: 30 min
