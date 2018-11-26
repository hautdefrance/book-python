.. _Character Types:

***************
Character Types
***************


``str``
=======

Defining ``str``
----------------
* ``"`` and ``'`` works the same
* Unicode characters (UTF-16 or UTF-32, depending on how Python was compiled)

.. code-block:: python

    name = ''
    name = ""

.. code-block:: python

    name = 'José'       # 'José'
    name = "José"       # 'José'

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

        my_str = 'it\'s José\'s book'
        my_str = "it's José's book"


When use single quotes?
-----------------------
* HTML and XML uses double quotes

.. code-block:: python

    my_str = '<a href="http://python.astrotech.io">Python and Machine Learning</a>'


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
    🚀


Characters before strings
=========================
* Format string: since Python 3.6
* In Python 3 ``str`` is Unicode
* In Python 2 ``str`` is Bytes
* In Python 2 to make unicode ``str``, you need to use ``u'...'`` prefix
* In Python 3 ``u'...'`` is only for compatibility with Python 2
* ``bytes`` is a sequence of octets (integers between 0 and 255)

.. csv-table:: String modifiers
    :header-rows: 1
    :widths: 15, 30, 55
    :file: data/str-modifiers.csv

.. code-block:: python

    name = 'José Jiménez'

    f'My name... {name}'
    u'zażółć gęślą jaźń'
    b'this is bytes literals'
    r'(?P<foo>)\n'
    r'C:\Users\Admin\file.txt'

.. code-block:: python

    print('C:\Users\Admin\file.txt')
    # SyntaxError: (unicode error) 'unicodeescape'
    #   codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

* Problem: ``\Users``
* after ``\U...`` python expects Unicode codepoint in hex
* ``s`` is invalid hexadecimal character


String methods
==============

String immutability
-------------------
* ``str`` is immutable
* ``str`` methods create a new modified ``str``

.. code-block:: python

    a = 'Python'
    a.replace('P', 'J')

    print(a)            # Python

.. code-block:: python

    a = 'Python'
    b = a.replace('P', 'J')

    print(a)            # Python
    print(b)            # Jython

Multiplication
--------------
.. code-block:: python

    'José' * 3          # JoséJoséJosé
    '-' * 10            # ----------

``str.title()``, ``str.lower()``, ``str.upper()``
-------------------------------------------------
* Unify data format before analysis

    .. code-block:: python

        name = 'joSé jiMénEz III'

        name.upper()    # 'JOSÉ JIMÉNEZ III'
        name.lower()    # 'josé jiménez iii'
        name.title()    # 'José Jiménez Iii'

``str.replace()``
-----------------
.. code-block:: python

    name = 'José Jiménez Iii'
    name.replace('Iii', 'III')  # 'José Jiménez III'

``strip()``, ``lstrip()``, ``rstrip()``
---------------------------------------
.. code-block:: python

    name = '\tMark Watney    \n'

    name.strip()        # 'Mark Watney'
    name.rstrip()       # '\tMark Watney'
    name.lstrip()       # 'Mark Watney    \n'

``str.startswith()`` and ``str.endswith()``
-------------------------------------------
* Understand this as "starts with" and "ends with"

.. code-block:: python

    name = 'José Jiménez'

    name.startswith('José')
    # True

    name.endswith(';')
    # False

``str.split()``
---------------
.. code-block:: python

    text = 'José Jiménez'

    text.split()
    # ['José', 'Jiménez']

.. code-block:: python

    text = 'jimenez:x:0:0:José Jiménez:/home/jimenez:/bin/bash'

    text.split(':')
    # ['jimenez', 'x', '0', '0', 'José Jiménez', '/home/jimenez', '/bin/bash']

``str.join()``
--------------
.. code-block:: python

    names = ['jimenez', 'x', '0', '0', 'José Jiménez', '/home/jimenez', '/bin/bash']

    ':'.join(names)
    # 'jimenez:x:0:0:José Jiménez:/home/jimenez:/bin/bash'

``str.isspace()``
-----------------
.. code-block:: python

    ''.isspace()    # False
    ' '.isspace()   # True
    '\t'.isspace()  # True
    '\n'.isspace()  # True

``str.isnumeric()``, ``str.isdigit()``, ``str.isdecimal()``
-----------------------------------------------------------
* Only numbers are numeric, digit or decimal
* Dot ``.`` is not!

.. code-block:: python

    '10'.isnumeric()    # True
    '10.5'.isnumeric()  # False

    '10'.isdigit()      # True
    '10.5'.isdigit()    # False

    '10'.isdecimal()    # True
    '10.5'.isdecimal()  # False

``str.isalpha()``
-----------------
.. code-block:: python

    'hello'.isalpha()   # True
    'hello1'.isalpha()  # False

``str`` in ``str``
------------------
.. code-block:: python

    'th' in 'Python'     # True
    'hello' in 'Python'    # False

``len()``
---------
.. code-block:: python

    len('Python')   # 6
    len('')         # 0

Multiple statements in one line
-------------------------------
.. code-block:: python

    a = 'Python'
    b = a.upper().replace('P', 'C').title()

    print(a)            # Python
    print(b)            # Cython

.. code-block:: python

    a = 'Python'

    b = a.upper().startswith('P').replace('P', 'C')
    # AttributeError: 'bool' object has no attribute 'replace'


Handling user input
===================

Getting user input
------------------
* ``input()`` returns ``str``
* Space at the end of prompt

.. code-block:: python

    name = input('Type your name: ')    # User inputs: Jose

    type(name)
    # <class 'str'>

.. code-block:: python

    age = input('Type your age: ')      # User inputs: 42

    type(age)
    # <class 'str'>

Cleaning data
-------------
* 80% of machine learning and data science is cleaning data
* This is a dump of distinct records of a single address
* Is this the same address?:

    .. code-block:: text

        'ul. Jana III Sobieskiego'
        'ul Jana III Sobieskiego'
        'ul.Jana III Sobieskiego'
        'ulicaJana III Sobieskiego'
        'Ul. Jana III Sobieskiego'
        'UL. Jana III Sobieskiego'
        'ulica Jana III Sobieskiego'
        'Ulica. Jana III Sobieskiego'

        'os. Jana III Sobieskiego'

        'Jana 3 Sobieskiego'
        'Jana 3ego Sobieskiego'
        'Jana III Sobieskiego'
        'Jana Iii Sobieskiego'
        'Jana IIi Sobieskiego'
        'Jana lll Sobieskiego'  # three small letters 'L'

* Which one of the above is a true address?
* Other examples:

    .. code-block:: text

        'ul '
        'ul. '
        'ul.'
        'ulica'
        'Ul. '
        'UL. '
        'ulica '
        'Ulica. '
        'os. '
        'ośedle'
        'osiedle'
        'os'
        'plac '
        'pl '
        'al '
        'al. '
        'aleja '
        'alei '
        'aleia'
        'aleii'
        'aleji'

    .. code-block:: text

        '1/2'
        '1 / 2'
        '1/ 2'
        '1 /2'

        '1 m. 2'
        '1 m 2'
        '1 apt 2'
        '1 apt. 2'

        '1f/108f'
        '1f/108'
        '1/108f'


Assignments
===========

String cleaning
---------------
#. Dane poniżej przeczyść, tak aby zmienne miały wartość ``'Jana III Sobieskiego'``
#. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące do wszystkich?

.. code-block:: python

    a = '  Jana III Sobieskiego 1 apt 2'
    b = 'ul Jana III SobIESkiego 1/2'
    c = '\tul. Jana trzeciego Sobieskiego 1/2'
    d = 'ul.Jana III Sob\n\nieskiego 1/2'
    e = 'ulicaJana III Sobieskiego 1/2'
    f = 'UL. JA\tNA 3 SOBIES\tKIEGO 1/2'
    g = 'UL. III SOBiesKIEGO 1/2'
    h = 'ULICA JANA III SOBIESKIEGO 1 /2  '
    i = 'ULICA. JANA III SOBI'
    j = ' Jana 3 Sobieskiego 1/2 '
    k = 'Jana III Sobieskiego 1 m. 2'


    expected = 'Jana III Sobieskiego'
    print(f'a: {a == expected}')
    print(f'b: {b == expected}')
    print(f'c: {c == expected}')
    print(f'd: {d == expected}')
    print(f'e: {e == expected}')
    print(f'f: {f == expected}')
    print(f'g: {g == expected}')
    print(f'h: {h == expected}')
    print(f'i: {i == expected}')
    print(f'j: {j == expected}')
    print(f'k: {k == expected}')

:About:
    * Filename: ``types_str_cleaning.py``
    * Lines of code to write: 11 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika

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
#. Tekst wyświetlony na ekranie ma mieć zamienione wszystkie spacje na ``_``
#. Tekst wyświetlony na ekranie ma być w UPPERCASE
#. Nie korzystaj z dodawania stringów (``str + str``)
#. Następnie znów wyświetl na ekranie wynik, tym razem z podmienionymi spacjami:

    .. code-block:: text

        '''MY_NAME_"JOSÉ_JIMÉNEZ".
        _I'M_AN_"""ASTRONAUT!"""'''

:About:
    * Filename: ``types_str_input.py``
    * Lines of code to write: 4 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika
