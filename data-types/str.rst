.. _Character Types:

***************
Character Types
***************


``str``
=======

Defining ``str``
----------------
* ``"`` and ``'`` works the same

.. code-block:: python

    name = ''
    name = ""

.. code-block:: python

    name = 'Pan Twardowski'       # 'Pan Twardowski'
    name = "Pan Twardowski"       # 'Pan Twardowski'

Multiline ``str``
-----------------
.. code-block:: python

    text = """First line
    Second line
    Third line
    """
    # 'First line\nSecond line\nThird line\n'

.. code-block:: python

    text = """
        First line
        Second line
        Third line
    """
    # '\n        First line\n        Second line\n        Third line\n    '

Type casting to ``str``
-----------------------
.. code-block:: python

    str('hello')        # 'hello'
    str(1969)           # '1969'
    str(13.37)          # '13.37'

Print converts argument to ``str`` before printing
--------------------------------------------------
.. code-block:: python

    print('hello')      # str('hello') -> 'hello'
    # 'hello'

.. code-block:: python

    print(10)           # str(10) -> '10'
    # '10'


Single or double quote?
=======================
* ``"`` and ``'`` works the same
* Choose one and keep consistency in code
* Python console uses ``'``
* I use ``'`` in this book to be consistent with Python
* ``doctest`` uses single quotes and throws error on double quotes

When use double quotes?
-----------------------
    .. code-block:: python

        my_str = 'It\'s Twardowski\'s Moon.'
        my_str = "It's Twardowski's Moon."

When use single quotes?
-----------------------
* HTML and XML uses double quotes

.. code-block:: python

    my_str = '<a href="http://python.astrotech.io">Python and Machine Learning</a>'

When use multiline?
-------------------
.. code-block:: python

    my_str = """My name's "José Jiménez""""
    my_str = '''My name's "José Jiménez"'''


Escape characters
=================

New lines
---------
.. code-block:: text

    \n
    \r\n

.. figure:: img/type-machine.jpg
    :scale: 25%
    :align: center

    Why we have '\\r\\n' on Windows?

Other escape characters
-----------------------
.. csv-table:: Escape characters
    :header-rows: 1
    :file: data/str-escape-characters.csv

.. code-block:: text

    \x1F680     # after \x goes hexadecimal number
    \U0001F680  # after \u goes four hexadecimal numbers

.. code-block:: python

    print('\U0001F680')     # 🚀


Characters before strings
=========================

Format String
-------------
* String interpolation (variable substitution)
* Since Python 3.6

.. code-block:: python

    name = 'José Jiménez'

    print(f'My name... {name}')
    # My name... José Jiménez

Unicode literals
----------------
* In Python 3 ``str`` is Unicode
* In Python 2 ``str`` is Bytes
* In Python 3 ``u'...'`` is only for compatibility with Python 2

.. code-block:: python

    u'zażółć gęślą jaźń'

Bytes literals
--------------
* Used while reading from low level devices and drivers
* Used in sockets and HTTP connections
* ``bytes`` is a sequence of octets (integers between 0 and 255)
* ``bytes.decode()`` conversion to unicode ``str``
* ``str.encode()`` conversion to ``bytes``

.. code-block:: python

    b'this is bytes literals'

Raw String
----------
*  Escapes does not matters

.. code-block:: python

    r'(?P<foo>)\n'

.. code-block:: python

    path = r'C:\Users\Admin\file.txt'

    print(path)
    # C:\Users\Admin\file.txt

.. code-block:: python

    path = 'C:\Users\Admin\file.txt'

    print(path)
    # SyntaxError: (unicode error) 'unicodeescape'
    #   codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

* Problem: ``\Users``
* after ``\U...`` python expects Unicode codepoint in hex
* ``s`` is invalid hexadecimal character


Getting text from user
======================
* ``input()`` returns ``str``
* Space at the end of prompt

.. code-block:: python

    name = input('Type your name: ')
    # User inputs: Pan Twardowski

    print(name)     # 'Pan Twardowski'
    type(name)      # <class 'str'>

.. code-block:: python

    age = input('Type your age: ')
    # User inputs: 42

    print(age)      # '42'
    type(age)       # <class 'str'>


Assignments
===========

Emot print
----------
#. Wczytaj od użytkownika imię
#. Wyświetl ``hello IMIE EMOTICON``, gdzie:

    - IMIE to imie wprowadzone przez usera
    - EMOTICON to Unicode Codepoint "U+1F642"

Variables and types
-------------------
#. Wczytaj od użytkownika imię
#. Za pomocą f-string formatting wyświetl na ekranie:

    .. code-block:: text

        '''My name... "José Jiménez".
	    	I'm an """astronaut!"""'''

#. Uwaga! Druga linijka zaczyna się od tabulacji
#. Gdzie wartość w podwójnym cudzysłowiu to ciąg od użytkownika (w przykładzie użytkownik wpisał ``José Jiménez``)
#. Zwróć uwagę na znaki apostrofów, cudzysłowów, tabulacji i nowych linii
#. W ciągu do wyświetlenia nie używaj spacji ani enterów - użyj ``\n`` i ``\t``
#. Nie korzystaj z dodawania stringów (``str + str``)

:About:
    * Filename: ``types_str_input.py``
    * Lines of code to write: 4 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika
