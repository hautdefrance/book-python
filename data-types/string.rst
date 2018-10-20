.. _Character Types:

***************
Character Types
***************


``str``
=======

Creating empty string
---------------------
* ``"`` and ``'`` works the same
* Unicode characters (UTF-16 or UTF-32, depending on how Python was compiled)

.. code-block:: python

    name = ''
    name = ""

    name: str = ''
    name: str = ""

Creating string
---------------
.. code-block:: python

    name = 'José'       # 'José'
    name = "José"       # 'José'

    name: str = 'José'  # 'José'
    name: str = "José"  # 'José'

Multiline ``str``
-----------------
.. code-block:: python

    names = """
        We choose to go to the Moon!
    We choose to go to the Moon in this decade and do the other things, not because they are easy, but because they are hard.
    """

    print(names)
    # '\n    We choose to go to the Moon!\nWe choose to go to the Moon in this decade and do the other things, not because they are easy, but because they are hard.'

Type casting to ``str``
-----------------------
.. code-block:: python

    str(1969)           # '1969'
    str(13.37)          # '13.37'


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
.. csv-table::
    :header-rows: 1

    "Escape sequence", "Description"

    "``\\``", "Backslash ``\``"
    "``\'``", "Single quote ``'``"
    "``\"``", "Double quote ``"``"
    "``\a``", "ASCII Bell (BEL)"
    "``\b``", "ASCII Backspace (BS)"
    "``\f``", "ASCII Formfeed (FF)"
    "``\n``", "ASCII Linefeed (LF)"
    "``\r``", "ASCII Carriage Return (CR)"
    "``\t``", "ASCII Horizontal Tab (TAB)"
    "``\uxxxx``", "Character with 16-bit hex value XXXX"
    "``\Uxxxxxxxx``", "Character with 32-bit hex value XXXXXXXX"
    "``\v``", "ASCII Vertical Tab (VT)"
    "``\ooo``", "ASCII character with octal value ooo"
    "``\xhh...``", "ASCII character with hex value hh..."

.. code-block:: text

    \x1F680     # after \x goes hexadecimal number
    \U0001F680  # after \u goes four hexadecimal numbers
    🚀


Characters before strings
=========================
* Format string: since Python 3.6
* ``str`` is a unicode
* In Python3 ``u'..'`` = ``'...'``
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
    # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

    # Problem: ``\Users``
    #          ``s`` is invalid hexadecimal character
    #          after ``\U...`` python expects unicode codepoint


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

.. code-block:: python

    a = 'Python'
    b = a.upper().replace('P', 'C').title()

    print(a)            # Python
    print(b)            # Cython


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

        name.title()    # 'José Jiménez Iii'
        name.upper()    # 'JOSÉ JIMÉNEZ III'
        name.lower()    # 'josé jiménez iii'

``str.replace()``
-----------------
.. code-block:: python

    name = 'José Jiménez Iii'
    name.replace('Iii', 'III')  # 'José Jiménez III'

``strip()``, ``lstrip()``, ``rstrip()``
---------------------------------------
.. code-block:: python

    name = '\tMark Watney    \n'

    name.rstrip()       # '\tMark Watney'
    name.lstrip()       # 'Mark Watney    \n'
    name.strip()        # 'Mark Watney'

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
    text.split()        # ['José', 'Jiménez']

    text = 'jimenez:x:0:0:José Jiménez:/home/jimenez:/bin/bash'
    text.split(':')     # ['jimenez', 'x', '0', '0', 'José Jiménez', '/home/jimenez', '/bin/bash']

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
    len()           # TypeError: len() takes exactly one argument (0 given)

Handling user input
===================
* ``input()`` returns ``str``
* Space at the end of prompt

.. code-block:: python

    name = input('Type your name: ')

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

    .. code-block:: text

        '1/2'
        '1 / 2'
        '1 m. 2'
        '1 apt 2'
        '1 apt. 2'


* Which one is a true address?

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
        l = ' 1/2'

:About:
    * Filename: ``types_cleaning.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 10 min

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
    * Filename: ``types_input.py``
    * Lines of code to write: 4 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika
