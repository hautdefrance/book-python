********************
Composite statements
********************


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


``and`` and ``or``
------------------
* Use parenthesis for explicit order

.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if (first_name == 'José' and last_name == 'Jiménez')
            or (first_name == 'Mark' and last_name == 'Watney'):
        print('Your name is José Jiménez or Mark Watney')
    else:
        print('Your name is different')


Control Statements
==================

``in`` with ``tuple``, ``dict``, ``list``, ``set``
--------------------------------------------------
* ``in`` checks whether value is in collection
* works with ``tuple``, ``dict``, ``list``, ``set``

.. code-block:: python

    usernames = {'José Jiménez', 'Pan Twardowski', 'Mark Watney'}

    if 'José Jiménez' in usernames:
        print(True)
    else:
        print(False)

``in`` with ``str``
-------------------
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


Assignments
===========

Classification of blood pressure in adults
------------------------------------------
#. Poniższa tabelka przedstawia klasyfikację ciśnienia krwi, wg. American Heart Association
#. Użytkownik wprowadza ciśnienie w formacie ``XXX/YY``, gdzie:

    - ``XXX`` to wartość ciśnienia skurczowego (ang. *systolic*)
    - ``YY`` to wartość ciśnienia rozkurczowego (ang. *diastolic*)

#. Daj informację użytkownikowi o klasyfikacji ciśnienia
#. W przypadku gdy wartości ciśnienia skurczowego i ciśnienia rozkurczowego należą do różnych kategorii, należy przyjąć kategorię wyższą

.. csv-table:: Classification of blood pressure in adults :cite:`AHA2018`
    :header-rows: 1

    "Blood Pressure Category", "Systolic [mm Hg]", "Operator", "Diastolic [mm Hg]"
    "Normal", "Less than 120", "and", "Less than 80"
    "Elevated", "120-129", "and", "Less than 80"
    "Hypertension stage 1", "130-139", "or", "80-89"
    "Hypertension stage 2", "140 or higher", "or", "90 or higher"
    "Hypertensive Crisis", "Higher than 180", "and/or", "Higher than 120"


:About:
    * Filename: ``ifelse_blood_pressure.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Wczytywanie ciągu znaków od użytkownika
    * Rzutowanie i konwersja typów
    * Instrukcje warunkowe
    * Złożone instrukcje warunkowe
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Definiowanie zmiennych i stałych w programie
