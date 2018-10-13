.. _Slice:

*******
Slicing
*******


Accessing element with index
============================

Accessing element from start
----------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[0]             # 'W'
    text[1]             # 'e'
    text[23]            # 'M'

Accessing element from back
---------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[-1]            # '!'
    text[-5]            # 'M'

Accessing not existing element
------------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[100]           # IndexError: string index out of range


Accessing range of elements
===========================

Accessing slice from start
--------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[0:2]             # 'We'
    text[:2]              # 'We'
    text[3:9]             # 'choose'
    text[23:28]           # 'Moon!'

Accessing slice from back
-------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[-5:]             # 'Moon!'
    text[-5:-1]           # 'Moon'
    text[:-6]             # 'We choose to go to the'

Accessing slice not existing elements
-------------------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:100]            # 'We choose to go to the Moon!'
    text[100:]            # ''

Accessing slice from all elements
---------------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:]               # 'We choose to go to the Moon!'

Arithmetic operations on slice indexes
--------------------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'
    lower = 23
    upper = 28

    text[lower:upper]       # 'Moon!'
    text[lower:upper-1]     # 'Moon'


Slice function
==============
.. code-block:: python

    text = 'We choose to go to the Moon!'
    range = slice(23, 28)

    text[range]           # 'Moon!'


Reversing and stepping over elements
====================================

Every ``n``th element
---------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[::2]             # 'W hoet ot h on'

Reversing
---------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[::-1]            # '!nooM eht ot og ot esoohc eW'
    text[::-2]            # '!oMeto go soce'


Assignments
===========

Slicing text
------------
#. Z podanych poniżej ciągów znaków
#. Za pomocą ``[...]`` wydobądź ``Jana III Sobieskiego``
#. Jakie parametry użyłeś dla każdej z linijek?

.. code-block:: python

    a = 'UL. Jana III Sobieskiego 1/2'
    b = 'ulica Jana III Sobieskiego 1 apt 2'
    c = 'os. Jana III Sobieskiego'
    d = 'plac Jana III Sobieskiego 1/2'
    e = 'aleja Jana III Sobieskiego'
    f = 'alei Jana III Sobieskiego 1/2'
    g = 'Jana III Sobieskiego 1 m. 2'
    h = 'os. Jana III Sobieskiego 1 apt 2'

:About:
    * Filename: ``types_slice.py``
    * Lines of code to write: 8 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Wycinanie elementów stringów
    * Indeksacja elemntów
