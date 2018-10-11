.. _Slice:

*******
Slicing
*******


Accessing element with index
============================

.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[0]             # 'W'
    text[1]             # 'e'
    text[2]             # ' '
    text[-1]            # '!'
    text[-3]            # '0'
    text[100]           # IndexError: string index out of range


Accessing range of elements
===========================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[0:2]             # 'We'
    text[:2]              # 'We'
    text[3:9]             # 'choose'
    text[23:28]           # 'Moon!'
    text[-5:]             # 'Moon!'
    text[-5:-1]           # 'Moon'
    text[:-6]             # 'We choose to go to the'
    text[:100]            # 'We choose to go to the Moon!'
    text[100:]            # ''

.. code-block:: python

    text = 'We choose to go to the Moon!'
    lower = 23
    upper = 28

    text[lower:upper]       # 'Moon!'
    text[lower:upper-1]     # 'Moon'


Slice
=====
.. code-block:: python

    text = 'We choose to go to the Moon!'
    RANGE = slice(23, 28)

    text[RANGE]           # 'Moon!'


Reversing and stepping over elements
====================================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[::2]             # 'W hoet ot h on'
    text[::-1]            # '!nooM eht ot og ot esoohc eW'
    text[::-2]            # '!oMeto go soce'


Assignments
===========

Slicing text
------------
#. Z podanych poniżej ciągów znaków wytnij ``Jana III Sobieskiego``
#. Jakie parametry użyłeś dla każdej z linijek?

.. code-block:: python

    a = 'UL. Jana III Sobieskiego 1/2'
    b = 'ulica Jana III Sobieskiego 1/2'
    c = 'os. Jana III Sobieskiego 1/2'
    d = 'plac Jana III Sobieskiego 1/2'
    e = 'aleja Jana III Sobieskiego 1/2'
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
