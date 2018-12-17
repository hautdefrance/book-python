**************
String methods
**************


String immutability
===================
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

.. code-block:: python

    c = '\u00B2'        # ²
    c.isdecimal()       # False
    c.isdigit()         # True

.. code-block:: python

    c = '\u00BD'        # ½
    c.isdecimal()       # False
    c.isdigit()         # False
    c.isnumeric()       # True

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

String cleaning
---------------
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

:About:
    * Filename: ``types_str_cleaning.py``
    * Lines of code to write: 11 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika
