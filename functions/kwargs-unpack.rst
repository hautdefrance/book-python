*************************
Unpacking return elements
*************************


``*`` and ``**`` operators
==========================
* This is not multiplication and power
* ``*`` zwykle nazywa się ``*args`` (arguments) - argumenty pozycyjne (anonimowe)
* ``**`` zwykle nazywa się ``**kwargs`` (keyword arguments) - argumenty nazwane
* ``*args`` unpack ``tuple`` or ``list``
* ``**kwargs`` unpack ``dict``


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


Assignments
===========

Hosts
-----
* Filename: ``kwargs_hosts.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Input data: :numref:`lang-functions-kwargs-hosts`

#. Skopiuj zawartość listingu poniżej do pliku ``hosts.txt``
#. Stwórz pusty ``dict`` o nazwie ``hosts``
#. Czytając plik pomiń puste linie lub zaczynające się od komentarza ``#``
#. Do ``hosts`` dla klucza IP dodaj listę hostname
#. Przy parsowaniu linii skorzystaj z konstrukcji z gwiazdką ``*``

.. literalinclude:: assignment/etc-hosts.txt
    :name: lang-functions-kwargs-hosts
    :language: python
    :caption: Listing pliku ``/etc/hosts``
