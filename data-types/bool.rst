********
``bool``
********


Defining ``bool``
=================
* ``True`` - Positive value
* ``False`` - Negative value
* First letter capitalized, other are lower cased

.. code-block:: python

    my_var = True
    my_var = False


Converting to ``bool``
======================
* Also known as "type casting"
* ``float()`` converts argument to ``float``

.. code-block:: python

    bool(1)                     # True
    bool(0)                     # False

.. code-block:: python

    bool(1.0)                   # True
    bool(0.0)                   # False

.. code-block:: python

    bool('José')                # True
    bool('')                    # False

Negative values
===============
* ``False``
* ``0``
* ``0.0``
* ``()`` - empty ``tuple``
* ``{}`` - empty ``dict``
* ``[]`` - empty ``list``
* ``''`` - empty ``str``
* ``set()`` - empty ``set``
* ``None``


Boolean logic
=============

Using ``and``
-------------
.. code-block:: python

    True and True               # True
    True and False              # False
    False and True              # False
    False and False             # False

.. code-block:: python

    1 and 1                     # True
    1 and 0                     # False
    0 and 1                     # False
    0 and 0                     # False

.. code-block:: python

    'José' and 'Иван'           # True
    'José' and ''               # False
    '' and 'José'               # False
    '' and ''                   # False

Using ``or``
------------
.. code-block:: python

    True or True                # True
    True or False               # True
    False or True               # True
    False or False              # False

.. code-block:: python

    1 or 1                      # True
    1 or 0                      # True
    0 or 1                      # True
    0 or 0                      # False

.. code-block:: python

    'José' or 'Иван'            # True
    'José' or ''                # True
    '' or 'José'                # True
    '' or ''                    # False

Using both: ``or`` and ``and``
------------------------------
.. code-block:: python

    True and True or False      # True
    True and False or False     # False
    False and False or True     # True


Logic operators
===============
.. csv-table:: Logic operators
    :header-rows: 1
    :widths: 15, 25, 60

    "Operand", "Example", "Description"
    "``x < y``", "``x < 18``", "value of ``x`` is less than ``y``"
    "``x <= y``", "``x <= 18``", "value of ``x`` is less or equal ``y``"
    "``x > y``", "``x > 18``", "value of ``x`` is greater than ``y``"
    "``x >= y``", "``x >= 18``", "value of ``x`` is greater or equal than ``y``"
    "``x == y``", "``x == 18``", "value of ``x`` is equal to ``y``"
    "``x != y``", "``x != 18``", "value of ``x`` is not equal to ``y``"


Assignments
===========

To ``bool`` or not to ``bool``
------------------------------
* Filename: ``types_bool_imple.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min

#. Wprowadzono zmienne:

    .. code-block:: python

        a = bool(False)
        b = bool(True)

        c = bool('a')
        d = bool('.')
        e = bool('0')
        f = bool('0.0')
        g = bool('')
        h = bool(' ')

        i = bool(0)
        j = bool(0.0)
        k = bool(-0)
        l = bool(-0.0+0.0j)
        l = bool('-0.0+0.0j')

        m = bool(int('0'))
        n = bool(float('-0'))

#. Które zmienne mają wartość ``True``, ``False``?

:The whys and wherefores:
    * Definiowanie zmiennych
    * Konwersja typów
    * Typy logiczne

``True`` of ``False``
---------------------
* Filename: ``types_bool.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min

#. Co należy podstawić do zmiennych aby wyrażenia poniżej zgadzały się z wartością oczekiwaną?

    .. code-block:: python

        a = bool(...) == True                   # True
        b = bool(...) == False                  # True
        c = ... == True                         # True
        d = ... != False                        # True
        e = ... or ...                          # True
        f = ... and ...                         # False
        g = bool(bool(...) == False) or False   # True
        h = bool(...) is not bool(...)          # False

        print(a)                                # True
        print(b)                                # True
        print(c)                                # True
        print(d)                                # True
        print(e)                                # True
        print(f)                                # False
        print(g)                                # True
        print(i)                                # False

:The whys and wherefores:
    * Definiowanie zmiennych
    * Konwersja typów
    * Typy logiczne
