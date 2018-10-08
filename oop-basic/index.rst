.. _Object Oriented Programming:

***************************
Object Oriented Programming
***************************

Object Paradigm
===============
* Odwzorowanie świata na obiekty i relacje między nimi

Classes and Objects
===================
.. literalinclude:: src/oop-class.py
    :language: python
    :caption: Classes and Objects

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


Methods
=======
.. literalinclude:: src/oop-methods-noargs.py
    :language: python
    :caption: Methods

.. literalinclude:: src/oop-methods-args.py
    :language: python
    :caption: Methods

``self`` - Instance as an argument
----------------------------------
* ``self`` - pierwszy argument do metody
* wyjątek to metody z dekoratorem ``@staticmethod`` (o tym będzie później)
* przy uruchomieniu funkcji nie podajemy jawnie argumentu ``self``

.. literalinclude:: src/oop-methods-self.py
    :language: python
    :caption: Methods argument ``self``

``__init__()`` - Initializer Method
-----------------------------------
* ``__init__()`` to nie konstruktor
* Domyślny ``__init__()`` gdy niezdefiniowaliśmy własnego
* Inicjalizacja pól klasy tylko w ``__init__``

.. literalinclude:: src/oop-fields-dynamic.py
    :language: python
    :caption: Fields added dynamically

.. literalinclude:: src/oop-init.py
    :language: python
    :caption: ``__init__()`` - Initializer Method

``__str__()`` - Stringify object
--------------------------------
* print converts it's arguments to ``str()`` automatically before printing

.. literalinclude:: src/oop-str-without.py
    :language: python
    :caption: Print object without ``__str__()`` method overloaded

.. literalinclude:: src/oop-str-with.py
    :language: python
    :caption: Stringify object

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

.. note:: The topic will be continued in :ref:`Advanced OOP` chapter

``super()`` - Calling object parent
-----------------------------------
.. literalinclude:: src/oop-super.py
    :language: python
    :caption: Using ``super()`` on a class

``Enum``
--------
.. literalinclude:: src/oop-enum.py
    :language: python
    :caption: ``enum`` - Support for enumerations

.. literalinclude:: src/oop-enum-example.py
    :language: python
    :caption: ``enum`` - Example usage


One class per file?
===================
* Jeden plik - gdy klasy są małe i czytelne
* Osobne pliki - gdy klasy są duże


More advanced topics
====================
.. note:: The topic will be continued in :ref:`Advanced OOP` chapter


Assignments
===========

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

#. Przesuwając smoka, można podać tylko niektóre kierunki, np: ``right=30, down=50`` lub ``up=20``
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

:About:
    * Filename: ``oop_dragon_easy.py``
    * Lines of code to write: 40 lines
    * Estimated time of completion: 75 min

.. literalinclude:: src/oop_dragon.py
    :name: listing-oop-dragon
    :language: python
    :caption: Dragon API

Dragon (Medium)
-----------------
.. note:: Jeżeli konieczne jest wprowadzenie nowej metody, klasy lub pól to należy to zrobić

#. Zaimportuj smoka z zadania podstawowego rozszerz go przez dziedziczenie
#. Smok nie może wyjść poza obszar ekranu (1024x768)
#. Jeżeli dojdzie do granicy ekranu, to przesuwając dalej, pozycja będzie ustawiona na maks
#. Stwórz bohatera (José Jiménez):

    * losowe punkty życia (100-150)
    * zadaje losowe obrażenia (1-15)
    * klasa postaci (domyślnie "wojownik")

#. Napisz ``doctest`` do funkcji poruszania, sprawdzający wychodzenie poza ekran
#. Dodaj statusy:

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

Address Book (Easy)
-------------------
#. Dla danych z :numref:`listing-oop-addressbook-easy` napisz książkę adresową
#. Wszystkie dane w książce muszą być reprezentowane przez klasy.
#. Klasy powinny wykorzystywać domyślne argumenty w ``__init__``.
#. Użytkownik może mieć wiele adresów.
#. Użytkownik może nie mieć żadnego adresu

:About:
    * Filename: ``oop_addressbook_easy.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 20 min

:The whys and wherefores:
    * myślenie obiektowe i odwzorowanie struktury w programie
    * praca z obiektami
    * zagnieżdżanie obiektów
    * rzutowanie obiektu na stringa oraz jego reprezentacja (które i kiedy użyć)

.. literalinclude:: src/oop-assignment-addressbook-easy.py
    :name: listing-oop-addressbook-easy
    :language: python
    :caption: Address Book

Points and Vectors
------------------
Przekształć swój kod z przykładu z modułu "Matematyka" tak żeby wykorzystywał klasy.

:Zadanie 0:
    Napisz klasę ``ObiektGraficzny``, która implementuje "wirtualną" funkcję ``plot()``. Niech domyślnie ta funkcja podnosi ``NotImplementedError`` (podpowiedź: ``raise NotImplementedError``).

:Zadanie 1:
    Napisz klasę ``Punkt``, która dziedziczy po ``ObiektGraficzny``, która będzie miała "ukryte" pola ``_x``, ``_y``. Konstruktor tej klasy ma przyjmować współrzędne ``x`` oraz ``y`` jako argumenty. Napisz obsługę pól ukrytych ``_x`` oraz ``_y`` jako ``@property`` tej klasy (obsługiwane jako ``x`` oraz ``y``). Dopisz implementacje metod ``__str__`` oraz ``__repr__``. Zaimplementuj metodę ``plot(kolor)``, która wyrysuje ten punkt na aktualnie aktywnym wykresie. Kolor domyślnie powinien przyjmować wartość ``'black'``.

    Dopisz do tej klasy metodę statyczną, która zwróci losowy punkt w podobny sposób jak funkcja ``random_point(center, std)`` zwracała obiekt dwuelementowy.

:Zadanie 2:
    Dopisz do tej klasy dwie metody, które pozwolą obliczyć odległość między dwoma punktami. Jedna z tych metod niech będzie metodą statyczną, która przyjmuje dwa punkty jako argumenty, a zwraca odległość między nimi (przykładowe wywołanie tej metody: ``Punkt.oblicz_odleglosc_miedzy_punktami(punkt_A, punkt_B)``). Druga z tych metod niech będzie zwykłą metodą klasy, która przyjmie jeden punkt jako argument oraz obliczy odległość od tego punktu do punktu na którym jest wykonywana (``punkt_A.oblicz_odleglosc_do(punkt_B)``).

:Zadanie 3:
    Napisz kod, który wykorzystując klasę zaimplementowaną w przykładzie powyżej, wygeneruje listę losowych punktów wokół punktów A i B. Wyrysuj te punkty na wykresie, podobnie jak w przykładzie z modułu "Matematyka".

:Zadanie 4:
    Napisz kod, który zaklasyfikuje te losowo wygenerowane punkty do punktów A oraz B na podstawie odległości. W tym celu wykorzystaj napisane metody do obliczania odległości między punktami. Po klasyfikacji wyrysuj te punkty na wykresie, podobnie jak w przykładzie z modułu "Matematyka".

:About:
    * Filename: ``oop-vector.py``
    * Lines of code to write: 20 lines
    * Estimated time of completion: 30 min
