.. _Character Types:

*******
``str``
*******


Defining ``str``
================
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
=======================
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

    "Escape sequence", "Description"
    "``\\``", "Backslash ``\``"
    "``\'``", "Single quote ``'``"
    "``\""``", "Double quote ``""``"
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


String methods
==============

String immutability
-------------------
* ``str`` is immutable
* ``str`` methods create a new modified ``str``

.. code-block:: python

    a = 'Python'
    a.replace('P', 'J')

    print(a)  # Python

.. code-block:: python

    a = 'Python'
    b = a.replace('P', 'J')

    print(a)  # Python
    print(b)  # Jython

String Arithmetic
-----------------
.. code-block:: python

    first_name = 'Pan'
    last_name = 'Twardowski'

    name = first_name + last_name
    # Pan Twardowski

.. code-block:: python

    'José' * 3          # JoséJoséJosé
    '-' * 10            # ----------

``str.title()``, ``str.lower()``, ``str.upper()``
-------------------------------------------------
* Unify data format before analysis

.. code-block:: python

    name = 'pAn TwARDowSKi III'

    name.upper()       # 'PAN TWARDOWSKI III'
    name.lower()       # 'pan twardowski iii'
    name.title()       # 'Pan Twardowski Iii'
    name.capitalize()  # 'Pan twardowski iii'

``str.replace()``
-----------------
.. code-block:: python

    name = 'Pan Twardowski Iii'

    name.replace('Iii', 'III')
    # 'Pan Twardowski III'

``str.strip()``, ``str.lstrip()``, ``str.rstrip()``
---------------------------------------------------
.. code-block:: python

    name = '\tPan Twardowski    \n'

    name.strip()        # 'Pan Twardowski'
    name.rstrip()       # '\tPan Twardowski'
    name.lstrip()       # 'Pan Twardowski    \n'

``str.startswith()`` and ``str.endswith()``
-------------------------------------------
* Understand this as "starts with" and "ends with"

.. code-block:: python

    name = 'Pan Twardowski'

    name.startswith('Pan')  # True
    name.endswith(';')      # False

``str.split()``
---------------
.. code-block:: python

    text = 'We choose to go to the Moon'

    text.split()
    # ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

.. code-block:: python

    text = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

    text.split(' ')
    # ['10.13.37.1', '', '', '', '', '', 'nasa.gov', 'esa.int', 'roscosmos.ru']

    text.split()
    # ['10.13.37.1', 'nasa.gov', 'esa.int', 'roscosmos.ru']

.. code-block:: python

    setosa = '5.1,3.5,1.4,0.2,setosa'

    setosa.split(',')
    # ['5.1', '3.5', '1.4', '0.2', 'setosa']

``str.join()``
--------------
.. code-block:: python

    text = ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

    ' '.join(text)
    # 'We choose to go to the Moon'

.. code-block:: python

    setosa = [5.1, 3.5, 1.4, 0.2, 'setosa']

    ','.join(setosa)
    # '5.1,3.5,1.4,0.2,setosa'

``str.isspace()``
-----------------
.. code-block:: python

    ''.isspace()        # False
    ' '.isspace()       # True
    '\t'.isspace()      # True
    '\n'.isspace()      # True

``str.isalpha()``
-----------------
.. code-block:: python

    'hello'.isalpha()   # True
    'hello1'.isalpha()  # False

``str`` in ``str``
------------------
.. code-block:: python

    'th' in 'Python'     # True
    'hello' in 'Python'  # False

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


Cleaning ``str`` from user input
================================
* 80% of machine learning and data science is cleaning data

Is this the same address?
-------------------------
* This is a dump of distinct records of a single address
* Which one of the below is a true address?

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

Different way of spelling and abbreviating
------------------------------------------
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

House number and apartment
--------------------------
.. code-block:: text

    '1/2'
    '1 / 2'
    '1/ 2'
    '1 /2'
    '3/5/7'

    '1 m. 2'
    '1 m 2'
    '1 apt 2'
    '1 apt. 2'

    '180f/8f'
    '180f/8'
    '180/8f'

    '13d bud. A'


Assignments
===========

Emot print
----------
* Filename: ``types_emoticon.py``
* Lines of code to write: 4 lines
* Estimated time of completion: 10 min

#. Wczytaj od użytkownika imię
#. Wyświetl ``hello IMIE EMOTICON``, gdzie:

    - IMIE to imie wprowadzone przez usera
    - EMOTICON to Unicode Codepoint "U+1F642"

:The whys and wherefores:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika

Variables and types
-------------------
* Filename: ``types_str_input.py``
* Lines of code to write: 4 lines
* Estimated time of completion: 10 min

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

:The whys and wherefores:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika

String cleaning
---------------
* Filename: ``types_str_cleaning.py``
* Lines of code to write: 11 lines
* Estimated time of completion: 15 min

#. Dane poniżej przeczyść, tak aby zmienne miały wartość ``'Jana III Sobieskiego'``
#. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące do wszystkich? (Implementacja rozwiązania będzie w rozdziale :ref:`Function Basics`)

.. code-block:: python

    expected = 'Jana III Sobieskiego'

    a = '  Jana III Sobieskiego '
    b = 'ul Jana III SobIESkiego'
    c = '\tul. Jana trzeciego Sobieskiego'
    d = 'ulicaJana III Sobieskiego'
    e = 'UL. JA\tNA 3 SOBIES\tKIEGO'
    f = 'UL. jana III SOBiesKIEGO'
    g = 'ULICA JANA III SOBIESKIEGO  '
    h = 'ULICA. JANA III SOBIeskieGO'
    i = ' Jana 3 Sobieskiego  '
    j = 'Jana III\tSobieskiego '
    k = 'ul.Jana III Sob\n\nieskiego\n'

    print(f'{a == expected}\t a: "{a}"')
    print(f'{b == expected}\t b: "{b}"')
    print(f'{c == expected}\t c: "{c}"')
    print(f'{d == expected}\t d: "{d}"')
    print(f'{e == expected}\t e: "{e}"')
    print(f'{f == expected}\t f: "{f}"')
    print(f'{g == expected}\t g: "{g}"')
    print(f'{h == expected}\t h: "{h}"')
    print(f'{i == expected}\t i: "{i}"')
    print(f'{j == expected}\t j: "{j}"')
    print(f'{k == expected}\t k: "{k}"')

:The whys and wherefores:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika
