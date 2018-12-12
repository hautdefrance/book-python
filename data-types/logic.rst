.. _Logical Types:

*************
Logical Types
*************


``bool``
========
* ``True`` - Positive value
* ``False`` - Negative value
* First letter capitalized, other are lower cased

Defining ``bool``
-----------------
.. code-block:: python

    my_var = True
    my_var = False

Converting to ``bool``
----------------------
* Also known as "type casting"
* ``float()`` converts argument to ``float``

.. code-block:: python

    bool(1)               # True
    bool(0)               # False

.. code-block:: python

    bool(1.0)             # True
    bool(0.0)             # False

.. code-block:: python

    bool('José')          # True
    bool('')              # False

Negative values
---------------
* ``False``
* ``0``
* ``0.0``
* ``()`` - empty ``tuple``
* ``{}`` - empty ``dict``
* ``[]`` - empty ``list``
* ``''`` - empty ``str``
* ``set()`` - empty ``set``
* ``None``

Using ``and``
-------------
.. code-block:: python

    1 and 1               # True
    1 and 0               # False
    0 and 0               # False

.. code-block:: python

    'José' and 'Иван'     # True
    'José' and ''         # False
    '' and ''             # False

Using ``or``
------------
.. code-block:: python

    1 or 1                # True
    1 or 0                # True
    0 or 0                # False

.. code-block:: python

    'José' or 'Иван'      # True
    'José' or ''          # True
    '' or ''              # False


``None``
========
* First letter capitalized, other are lower cased
* Empty value (null)
* It is not ``False`` value
* With ``if`` statements behaves like negative values
* Used for unknown (unset) values

Defining ``None``
-----------------
.. code-block:: python

    my_var = None


Logic operators
===============
.. csv-table:: Logic operators
    :header-rows: 1
    :widths: 15, 25, 60
    :file: data/operators-logic.csv


Assignments
===========

To ``bool`` or not to ``bool``
------------------------------
#. Wprowadzono zmienne:

    .. code-block:: python

        a = False
        b = True
        c = None

        c = 'a'
        d = '.'
        e = '0'
        f = '0.0'
        g = ''
        h = ' '

        j = 0
        k = 0.0
        l = -0
        m = -0.0+0.0j

        n = int('0')
        o = float('-0')

#. Które zmienne mają wartość ``True``, ``None``, ``False``?
#. Czym się różni ``None`` od ``False``?

:About:
    * Filename: ``types_bool.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Konwersja typów
    * Typy logiczne

``True`` of ``False``
---------------------
#. Co należy podstawić do zmiennych aby wyrażenia poniżej zgadzały się z wartością oczekiwaną?

    .. code-block:: python

        a = bool(...) == True                          # True
        b = bool(...) == False                         # True
        c = ... == True                                # True
        d = ... != False                               # True
        e = ... or ...                                 # True
        f = ... and ...                                # False
        g = bool(bool(...) == False) or False          # True
        h = ... is None                                # True
        i = ... is not None                            # False
        j = bool(...) is not bool(...)                 # False

        print(a)  # True
        print(b)  # True
        print(c)  # True
        print(d)  # True
        print(e)  # True
        print(f)  # False
        print(g)  # True
        print(h)  # True
        print(i)  # False
        print(j)  # False

#. Zadanie dla chętnych:

    .. code-block:: python

        k = bool(bool(...) is not bool(...)) == False  # True
        l = (bool(bool(...) is not bool(...)) == False and bool(...))   # False
        m = (bool(bool(...) is not bool(...)) == False and bool(...)) and (... is not None)   # False

        print(k)  # True
        print(l)  # False
        print(m)  # False

:About:
    * Filename: ``types_bool_or_none.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 5 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Konwersja typów
    * Typy logiczne

