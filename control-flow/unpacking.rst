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

.. note:: Note, that ``set`` is unordered collection!

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

    others      # [1, 2]
    a           # 3
    b           # 4

Unpacking values at the left side
---------------------------------
.. code-block:: python

    first, *middle, last = [1, 2, 3, 4]

    first       # 1
    middle      # [2, 3]
    last        # 4

Cannot unpack from both sides at once
-------------------------------------
.. code-block:: python

    *a, b, *c = [1, 2, 3, 4]
    # SyntaxError: two starred expressions in assignment


Unpacking values from function
==============================

Recap of assignment information
-------------------------------
.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    line.split(',')
    # ['4.9', '3.1', '1.5', '0.1', 'setosa']

.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    sepal_length, sepal_width, petal_length, petal_width, species = line.split(',')

    sepal_length    # '4.9'
    sepal_width     # '3.1'
    petal_length    # '1.5'
    petal_width     # '0.1'
    species         # 'setosa'

Unpacking values at the right side
----------------------------------
.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    sepal_length, sepal_width, *others = line.split(',')

    sepal_length    # '4.9'
    sepal_width     # '3.1'
    others          # ['1.5', '0.1', 'setosa']

Unpacking values at the left side
---------------------------------
.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    *features, species = line.split(',')

    features        # ['4.9', '3.1', '1.5', '0.1']
    species         # 'setosa'

Cannot unpack from both sides at once
-------------------------------------
.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    *a, b, *c = line.split(',')
    # SyntaxError: two starred expressions in assignment

Naming convention
-----------------
* if you're not using ``features`` later in your code

.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    *_, species = line.split(',')


Example
=======
.. code-block:: python

    def get_iris():
        """
        Would be nice, if you can get ``dict``...
        but most programmers will return ``tuple``
        because it's a bit faster

        return {
            'sepal_length': 4.9,
            'sepal_width': 3.1,
            'petal_length': 1.5,
            'petal_width': 0.1,
            'species': 'setosa'
        }
        """
        return 4.9, 3.1, 1.5, 0.1, 'setosa'

    *features, species = get_iris()


More advanced topics
====================
.. note:: The topic will be continued in Intermediate and Advanced part of the book


Assignments
===========

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

#. Za pomocą slice (co piąty element) wyodrębnij zmienną ``labels: List[str]``, która będzie zawierała w kolejności wszystkie nazwy gatunków:

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

Hosts
-----
* Filename: ``kwargs_hosts.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Input data: :numref:`controlflow-kwargs-hosts`

#. Skopiuj zawartość listingu poniżej do pliku ``hosts.txt``
#. Stwórz pusty ``dict`` o nazwie ``hosts``
#. Czytając plik pomiń puste linie lub zaczynające się od komentarza ``#``
#. Do ``hosts`` dla klucza IP dodaj listę hostname
#. Przy parsowaniu linii skorzystaj z konstrukcji z gwiazdką ``*``

.. literalinclude:: src/etc-hosts.txt
    :name: controlflow-kwargs-hosts
    :language: python
    :caption: Listing pliku ``/etc/hosts``
