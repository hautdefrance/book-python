********
``dict``
********


Defining ``dict``
=================
* ``dict`` items order changes!
* ``dict`` are key-value storage
* Comma after last element is optional

.. note:: Since Python 3.7: The insertion-order preservation nature of dict objects is now an official part of the Python language spec.

Empty ``dict``
--------------
.. code-block:: python

    my_dict = {}
    my_dict = dict()

``dict`` with multiple values
-----------------------------
.. code-block:: python

    my_dict = {
        'first_name': 'José',
        'last_name': 'Jiménez'
    }

Duplicating items are overridden by latter
------------------------------------------
.. code-block:: python

    my_dict = {
        'name': 'José',
        'name': 'Иван',
    }
    # {'name': 'Иван'}

Key can be any hashable object
------------------------------
.. code-block:: python

    my_dict = {
        'first_name': 'José',
        'last_name': 'Jiménez',
    }

.. code-block:: python

    my_dict = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon',
    }

.. code-block:: python

    my_dict = {
        (1, 2): 'hello',
        (3, 4, 5): 'ehlo',
    }

Value can be any object
-----------------------
.. code-block:: python

    my_dict = {
        'date': '1969-07-21',
        'age': 42,
        'astronaut': {'name': 'José Jiménez', 'medals': {'Medal of Honor', 'Purple Heart'}},
        'agency': ['NASA', 'Roscosmos', 'ESA'],
        'location': ('Bajkonur', 'KSC Florida'),
    }


Adding elements
===============
* Adds if value not exist
* Updates if value exist

Adding using ``[...]`` syntax
-----------------------------
.. code-block:: python

    data = {
        'first_name': 'José',
        'last_name': 'Jiménez',
    }

    data['agency'] = 'NASA'

    print(data)
    # {
    #   'first_name': 'José',
    #   'last_name': 'Jiménez',
    #   'agency': 'NASA'
    # }

Adding using ``.update()`` method
---------------------------------
.. code-block:: python

    data = {
        'name': 'José Jiménez',
    }

    data.update(age=42, location=['Bajkonur', 'Florida'])
    data.update({'agency': 'NASA'})

    print(data)
    # {
    #   'name': 'José Jiménez',
    #   'age': 42,
    #   'location': ['Bajkonur', 'Florida'],
    #   'agency': 'NASA'
    # }


Accessing elements
==================

Accessing values with ``[...]``
-------------------------------
* ``[...]`` throws ``KeyError`` exception if key not found in ``dict``

.. code-block:: python

    data = {
        'first_name': 'José',
        'last_name': 'Jiménez',
        'age': 42,
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon',
    }

    data['last_name']          # 'Jiménez'
    data[1961]                 # 'First Human Space Flight'
    data['agency']             # KeyError: 'agency'

Accessing values with ``.get(...)``
-----------------------------------
* ``.get(...)`` returns ``None`` if key not found
* ``.get(...)`` can have default value, if key not found

.. code-block:: python

    data = {
        'first_name': 'José',
        'last_name': 'Jiménez',
        'age': 42,
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon',
    }

    data.get('last_name')      # 'Jiménez'
    data.get(1961)             # 'First Human Space Flight'
    data.get('agency')         # None
    data.get('agency', 'n/a')  # 'n/a'


Accessing ``dict`` keys, values and key-value pairs
---------------------------------------------------
.. code-block:: python

    my_dict = {
        'first_name': 'José',
        'last_name': 'Jiménez',
        'age': 42,
    }

    my_dict.keys()      # ['first_name', 'last_name', 'age']
    my_dict.values()    # ['José', 'Jiménez', 42]
    my_dict.items()     # [('first_name', 'José'), ('last_name', 'Jiménez'), ('age', 42)]


Length of a ``dict``
====================
.. code-block:: python

    my_dict = {
        'first_name': 'José',
        'last_name': 'Jiménez',
        'age': 42,
    }

    len(my_dict)                # 3
    len(my_dict.keys())         # 3
    len(my_dict.values())       # 3
    len(my_dict.items())        # 3


Assignments
===========

Aviation Language
-----------------
* Filename: ``dict_alphabet.py``
* Lines of code to write: 30 lines
* Estimated time of completion: 15 min

#. Stwórz słownik języka pilotów
#. Pojedynczym literom przyporządkuj ich fonetyczne odpowiedniki
#. Do przekonwertowania tabelki poniżej, wykorzystaj zaznaczanie wielu linijek za pomocą klawisza ``alt`` w Twoim IDE
#. Wczytaj od użytkownika literę
#. Użytkownik zawsze poda przynajmniej jedną literę, cyfrę lub znak specjalny
#. Wypisz na ekranie nazwę fonetyczną litery
#. Jeżeli użytkownik podał więcej niż jedną literę, to wybierz z ciągu tylko pierwszą
#. Słownik ma wyświetlić kod bez względu na to czy użytkownik podał dużą czy małą literę
#. Jeżeli wpisał znak, który nie jest w alfabecie, to wypisz "Pilots don't say that"
#. Nie używaj konstrukcji ``if``, ani ``try`` i ``except``

:The whys and wherefores:
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Rzutowanie i konwersja typów

.. csv-table:: Aviation Alphabet
    :header-rows: 1

    "Letter", "Pronounce"
    "A", "Alfa"
    "B", "Bravo"
    "C", "Charlie"
    "D", "Delta"
    "E", "Echo"
    "F", "Foxtrot"
    "G", "Golf"
    "H", "Hotel"
    "I", "India"
    "J", "Juliet"
    "K", "Kilo"
    "L", "Lima"
    "M", "Mike"
    "N", "November"
    "O", "Oscar"
    "P", "Papa"
    "Q", "Quebec"
    "R", "Romeo"
    "S", "Sierra"
    "T", "Tango"
    "U", "Uniform"
    "V", "Victor"
    "W", "Whisky"
    "X", "X-Ray"
    "Y", "Yankee"
    "Z", "Zulu"
