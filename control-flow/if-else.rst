.. _Control Flow Statements:

***********************
Control Flow Statements
***********************


Conditional Statements
======================

``if``
------
* Simple syntax:

    .. code-block:: python

        if True:
            print('First line of the true statement')

* Multiline blocks:

    .. code-block:: python

        if True:
            print('First line of the true statement')
            print('Second line of the true statement')
            print('Third line of the true statement')

* Negative values:

    * ``False``
    * ``0``
    * ``()`` - empty ``tuple``
    * ``{}`` - empty ``dict``
    * ``[]`` - empty ``list``
    * ``''`` - empty ``str``
    * ``set()`` - empty ``set``
    * ``None``

* Positive values: any other values
* Checking for simple value

    .. code-block:: python

        name = 'José Jiménez'

        if name == 'José Jiménez':
            print('My name... José Jiménez')

* Checking if value is in range

    .. code-block:: python

        age = 7

        if 0 <= age < 18:
            print('Age is between [0, 18)')

``else``
--------
* Optional
* Executed when condition is not met
* Checking if variable is certain value:

    .. code-block:: python

        name = 'José Jiménez'

        if name == 'José Jiménez':
            print('My name... José Jiménez')
        else:
            print('My name is other')

* Multiline blocks:

    .. code-block:: python

        if True:
            print('First line of the true statement')
            print('Second line of the true statement')
            print('Third line of the true statement')
        else:
            print('First line of the false statement')
            print('Second line of the false statement')
            print('Third line of the false statement')

* Checking if variable has any value

    .. code-block:: python

        name = 'José Jiménez'

        if name:
            print('Name is defined')
        else:
            print('Name is not defined')

``elif``
--------
* Used to check for additional condition if first is not met
* In other languages is known as ``else if``

.. code-block:: python

    name = 'José Jiménez'

    if name == 'José Jiménez':
        print('My name... José Jiménez')
    elif name == 'Alex Vogel':
        print('Guten tag!')
    else:
        print("You're not José nor Alex")

Checking if has value
---------------------
.. code-block:: python

    name = None

    if name:
        print(name)
    else:
        print('Name is not defined')

Inline ``if``
-------------
.. code-block:: python

    ip = '127.0.0.1'

    if '.' in ip:
        protocol = 'IPv4'
    else:
        protocol = 'IPv6'

.. code-block:: python

    ip = '127.0.0.1'

    protocol = 'IPv4' if '.' in ip else 'IPv6'


Complex expressions
===================

``and``
-------
.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if first_name == 'José' and last_name == 'Jiménez':
        print('My name... José Jiménez')
    else:
        print('Your name is different')


``or``
------
.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if first_name == 'José' or first_name == 'Max':
        print('Your name is José or Max')
    else:
        print('Your name is different')


mixed
-----
* Use parenthesis for explicit order

    .. code-block:: python

        first_name = 'José'
        last_name = 'Jiménez'

        if (first_name == 'José' and last_name == 'Jiménez')
                or (first_name == 'Matt' and last_name == 'Kowalski'):
            print('Your name is José Jiménez or Matt Kowalski')
        else:
            print('Your name is different')


Control Statements
==================

``in``
------
* works with ``tuple``, ``dict``, ``list``, ``set`` and ``str``
* ``in`` checks whether value is in other collection

    .. code-block:: python

        usernames = {'José Jiménez', 'Matt Kowalski', 'Mark Watney'}

        if 'José Jiménez' in usernames:
            print(True)
        else:
            print(False)

* ``in`` checks whether ``str`` is a part of another ``str``

    .. code-block:: python

        text = 'My name... José Jiménez'

        if 'José' in text:
            print(True)
        else:
            print(False)

``not``
-------
* ``not`` negates (logically inverts) condition

.. code-block:: python

    name = None

    if not name:
        print('Name is not defined')

.. code-block:: python

    usernames = {'José', 'Max', 'Иван'}

    if 'José' not in usernames:
        print('Not found')

``is``
------
.. code-block:: python

    name = None

    if name is None:
        print('Name is not defined')

.. code-block:: python

    name = None

    if name is not None:
        print(name)

No ``switch`` statement?!
=========================
* ``switch`` in Object Oriented Programming is considered a bad practise
* `PEP 275 <https://www.python.org/dev/peps/pep-0275/>`_

.. code-block:: python

    if name == 'José Jiménez':
        print('My name... José Jiménez')
    elif name == 'Иван Иванович':
        print('Your name is Иван Иванович')
    elif name == 'Mark Watney':
        print('Your name is Mark Watney')
    else:
         print('Your name is other')

.. code-block:: python

    switch = {
        'English': 'Hello',
        'Russian': 'Здравствуйте',
        'German': 'Guten Tag',
        'Polish': 'Witaj',
    }

    what = 'French'
    switch.get(what, "Sorry, I don't know")
    # "Sorry, I don't know"

.. code-block:: python

    def switch(key):
        return {
            'English': 'Hello',
            'Russian': 'Здравствуйте',
            'German': 'Guten Tag',
            'Polish': 'Witaj',
        }.get(key, "Sorry, I don't know")

    switch('Russian')       # 'Здравствуйте'
    switch('French')        # "Sorry, I don't know"


Assignments
===========

Conditioning on user input
--------------------------
#. Napisz program, który poprosi użytkownika o wiek
#. Użytkownik będzie podawał tylko i wyłącznie ``int`` lub ``float``
#. Następnie sprawdzi pełnoletność i wyświetli informację czy osoba jest "dorosła" czy "niepełnoletnia"

:About:
    * Filename: ``control_input.py``
    * Lines of code to write: 6 lines
    * Estimated time of completion: 5 min

:The whys and wherefores:
    * Wczytywanie ciągu znaków od użytkownika
    * Rzutowanie i konwersja typów
    * Instrukcje warunkowe
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Definiowanie zmiennych i stałych w programie
    * Magic Number

