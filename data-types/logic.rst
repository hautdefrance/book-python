.. _Logical Types:

*************
Logical Types
*************


``bool``
========
* First letter capitalized, other are lower cased
* Positive value - ``True``
* Negative values - ``False``
* Defining ``bool``:

    .. code-block:: python

        my_var = True
        my_var = False

        my_var: bool = True
        my_var: bool = False

* Negative values:

    * ``False``
    * ``0``
    * ``()`` - empty ``tuple``
    * ``{}`` - empty ``dict``
    * ``[]`` - empty ``list``
    * ``''`` - empty ``str``
    * ``None``

* ``bool()`` converts argument to ``bool``:

    .. code-block:: python

        bool('José')          # True
        bool('')              # False

* Using ``and``:

    .. code-block:: python

        'José' and ''         # False
        'José' and 'Иван'     # True

* Using ``or``:

    .. code-block:: python

        'José' or ''          # True
        'José' or 'Иван'      # True


``None``
========
* First letter capitalized, other are lower cased
* Empty value (null)
* It is not ``False`` value, although in ``if`` it behaves like ``False``
* With ``if`` statements behaves like negative values
* Used for unknown (unset) values:

    .. code-block:: python

        my_var = None


Assignments
===========

Bool
----
#. Wprowadzono zmienne:

    .. code-block:: python

        a = False
        b = True
        c = None
        d = ''
        e = ' '
        f = 'a'
        g = '.'
        h = 0
        i = 0.0
        j = '0'
        k = '0.0'
        l = -0
        m = -0.0+0.0j
        n = int('0')
        o = float('0')

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
