*********************
Key-Value Collections
*********************


``dict``
========
* ``dict()`` items order changes!
* Declaring with ``dict()`` is more readable, but ``{}`` is used more often:

    .. code-block:: python

        my_dict = {}
        my_dict = dict()

* Key - Value storage:

    .. code-block:: python

        my_dict = {
            'first_name': 'José',
            'last_name': 'Jiménez'
        }

* Comma after last element is optional:

    .. code-block:: python

        my_dict = {
            'first_name': 'José',
            'last_name': 'Jiménez',
        }

* Duplicating items are overridden by latter:

    .. code-block:: python

        my_dict = {
            'name': 'José',
            'name': 'Иван',
        }
        # {'name': 'Иван'}

* Key can be any hashable object:

    .. code-block:: python

        my_dict = {
            1961: 'First Human Space Flight',
            1969: 'First Step on the Moon',
        }

* Value can be any object:

    .. code-block:: python

        my_dict = {
            'astronaut': {'first_name': 'José', 'last_name': 'Jiménez'},
            'agency': ['NASA', 'Roscosmos', 'ESA'],
            'age': 42,
        }

Accessing ``dict`` values
=========================

Setting ``dict`` values
-----------------------
.. code-block:: python

    data = {
        'first_name': 'José',
        'last_name': 'Jiménez',
    }

    data['agency'] = 'NASA'

    print(data)
    # {'first_name': 'José', 'last_name': 'Jiménez', 'agency': 'NASA'}

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


Accessing ``dict`` values in bulk
=================================
.. code-block:: python

    my_dict = {
        'first_name': 'José',
        'last_name': 'Jiménez',
        'age': 42,
    }

    my_dict.keys()    # ['first_name', 'last_name', 'age']
    my_dict.values()  # ['José', 'Jiménez', 42]
    my_dict.items()   # [('first_name', 'José'), ('last_name', 'Jiménez'), ('age', 42)]


``dict`` vs. ``set``
====================
* ``set()`` and ``dict()`` both use the same (``{`` and ``}``) braces:

    .. code-block:: python

        {}                                # dict
        {1}                               # set
        {1, 2}                            # set
        {1: 2}                            # dict
        {1:1, 2:2}                        # dict

* Despite similar syntax, they are different types:

    .. code-block:: python

        my_data = {}
        isinstance(my_data, (set, dict))  # True
        isinstance(my_data, dict)         # True
        isinstance(my_data, set)          # False

        my_data = {1}
        isinstance(my_data, dict)         # False
        isinstance(my_data, set)          # True

        my_data = {1: 1}
        isinstance(my_data, dict)         # True
        isinstance(my_data, set)          # False


Assignments
===========

Aviation Language
-----------------
#. Stwórz słownik języka pilotów
#. Pojedynczym literom przyporządkuj ich fonetyczne odpowiedniki
#. Do przekonwertowania tabelki poniżej, wykorzystaj zaznaczanie wielu linijek za pomocą klawisza ``alt`` w Twoim IDE
#. Wczytaj od użytkownika literę
#. Użytkownik zawsze poda przynajmniej jedną literę, cyfrę lub znak specjalny
#. Wypisz na ekranie nazwę fonetyczną litery
#. Jeżeli użytkownik podał więcej niż jedną literę, to wybierz z ciągu tylko pierwszą
#. Słownik ma wyświetlić kod bez względu na to czy użytkownik podał dużą czy małą literę
#. Jeżeli wpisał znak, k†óry nie jest w alfabecie, to wypisz "Pilots don't say that"
#. Nie używaj konstrukcji ``if``, ani ``try`` i ``except``

.. csv-table:: Aviation Alphabet
    :header-rows: 1
    :file: data/aviation-alphabet.csv

:About:
    * Filename: ``collections_aviation_alphabet.py``
    * Lines of code to write: 30 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Rzutowanie i konwersja typów
