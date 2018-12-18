*******************
Unpacking sequences
*******************


Unpacking values
================
.. code-block:: python

    a, b, c = 1, 2, 3

.. code-block:: python

    a, b, c = (1, 2, 3)
    a, b, c = [1, 2, 3]
    a, b, c = {1, 2, 3}

Too many values to unpack
-------------------------
.. code-block:: python

    a, b, c = [1, 2, 3, 4]
    # ValueError: too many values to unpack (expected 3)

Not enough values to unpack
---------------------------
.. code-block:: python

    a, b, c, d = [1, 2, 3]
    # ValueError: not enough values to unpack (expected 4, got 3)


Unpacking arbitrary number of arguments
=======================================

Unpacking values at the right side
----------------------------------
.. code-block:: python

    a, b, *others = [1, 2, 3, 4]

    a           # 1
    b           # 2
    others      # [3, 4]

Unpacking values at the left side
---------------------------------
.. code-block:: python

    *others, a, b = [1, 2, 3, 4]

    a           # 3
    b           # 4
    others      # [1, 2]

Cannot unpack from both sides at once
-------------------------------------
.. code-block:: python

    *a, b, *c = [1, 2, 3, 4]
    # SyntaxError: two starred expressions in assignment


More advanced topics
====================
.. note:: The topic will be continued in Intermediate and Advanced part of the book


Assignments
===========

Simple collections
------------------
* Filename: ``sequences_simple.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

#. Stwórz ``a: tuple`` z cyframi 0, 1, 2, 3
#. Stwórz ``b: list`` z cyframi 2, 3, 4, 5
#. Stwórz ``c: set``, który będzie zawierał co drugie elementy z ``a`` i ``b``
#. Wyświetl ``c`` na ekranie

:The whys and wherefores:
    * Definiowanie i korzystanie z ``list``, ``tuple``, ``set``
    * Slice zbiorów danych
    * Rzutowanie i konwersja typów

Iris dataset
------------
* Filename: ``unpacking_iris.py``
* Lines of code to write: 30 lines
* Estimated time of completion: 20 min

#. Mając dane z listingu poniżej

    .. code-block:: python

        DATA = (
            5.8, 2.7, 5.1, 1.9, 'virginica',
            5.1, 3.5, 1.4, 0.2, 'setosa',
            5.7, 2.8, 4.1, 1.3, 'versicolor',
            6.3, 2.9, 5.6, 1.8, 'virginica',
            6.4, 3.2, 4.5, 1.5, 'versicolor',
            4.7, 3.2, 1.3, 0.2, 'setosa',
        )

#. Za pomocą slice wyodrębnij zmienną ``features: List[Tuple[float]]`` z wynikami pomiarów

    .. code-block:: python

        features = [
            (5.8, 2.7, 5.1, 1.9),
            (5.1, 3.5, 1.4, 0.2),
            (5.7, 2.8, 4.1, 1.3),
            (6.3, 2.9, 5.6, 1.8),
            (6.4, 3.2, 4.5, 1.5),
            (4.7, 3.2, 1.3, 0.2),
        ]

#. Za pomocą slice wyodrębnij zmienną ``labels: List[str]``, która będzie zawierała w kolejności wszystkie nazwy gatunków

    .. code-block:: python

        labels = [
            'virginica',
            'setosa',
            'versicolor',
            'virginica',
            'versicolor',
            'setosa',
        ]

#. Za pomocą slice wyodrębnij zmienną ``species: Set[str]``, która jest unikalnym zbiorem gatunków (na podstawie ``labels``)

    .. code-block:: python

        species = {
            'versicolor',
            'setosa',
            'virginica',
        }

#. Nie używaj slice, ani żadnych instrukcji, które nie zostały dotychczas omówione

:The whys and wherefores:
    * Definiowanie i korzystanie z ``list``, ``tuple``, ``set``
    * Slice zbiorów danych
    * Rzutowanie i konwersja typów
