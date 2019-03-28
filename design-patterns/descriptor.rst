**********
Descriptor
**********


The Descriptor Protocol
=======================
* They provide the developer with the ability to add managed attributes to objects
* ``__get__(self, obj, type=None) -> self``
* ``__set__(self, obj, value) -> None``
* ``__delete__(self, obj) -> None``


Builtin Descriptor Object Examples
==================================
* classmethod
* staticmethod
* property
* functions in general


Example
=======
.. literalinclude:: src/descriptor-example-1.py
    :language: python
    :caption: Example

.. literalinclude:: src/descriptor-example-2.py
    :language: python
    :caption: Example

.. todo:: dorobić przykład z konwersją stref czasowych i bazowym czasie w UTC


Accessors
=========

``__setattr__()``
-----------------
.. literalinclude:: src/accessor-setattr.py
    :language: python
    :caption: Example ``__setattr__()``

``__getattribute__()``
----------------------
.. literalinclude:: src/accessor-getattribute.py
    :language: python
    :caption: Example ``__getattribute__()``

``__delattr__()``
-----------------
.. literalinclude:: src/accessor-delattr.py
    :language: python
    :caption: Example ``__delattr__()``


setter, getter, deleter
=======================

``@property``
-------------
* ``@property`` - for defining getters
* Przykład użycia:

    * Blokowanie możliwości edycji pola klasy
    * Dodawanie logowania przy ustawianiu wartości

.. code-block:: python
    :caption: Using ``@property`` as a getter

    class Temperature:
        def __init__(self, kelvin: float = 0.0):
            self.kelvin = kelvin

        @property
        def celsius(self):
            temp = self.kelvin - 273.15
            return round(temp, 2)


    temp = Temperature(kelvin=309.75)

    print(temp.celsius)
    # 36.6

``@x.setter``
-------------
* ``@x.setter`` - for defining setter for field ``x``
* Require field to be ``@property``

.. code-block:: python
    :caption: ``@x.setter``

    class Temperature:
        def __init__(self, kelvin: float = 0.0):
            self.kelvin = kelvin

        @property
        def celsius(self):
            temp = self.kelvin - 273.15
            return round(temp, 2)

        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError('Temperature below -273.15 is not possible')
            else:
                self.kelvin = value + 273.15

    temp = Temperature()

    print(temp.kelvin)
    # 0.0

    temp.celsius = 36.60
    print(temp.kelvin)
    # 309.75

    temp.celsius = -1000
    # ValueError: Temperature below -273.15 is not possible

``@x.deleter``
--------------
* ``@x.deleter`` - for defining deleter for field ``x``
* Require field to be ``@property``

.. code-block:: python
    :caption: ``@x.deleter``

    class Temperature:
        def __init__(self, kelvin: float = 0.0):
            self.kelvin = kelvin

        @property
        def celsius(self):
            temp = self.kelvin - 273.15
            return round(temp, 2)

        @celsius.deleter
        def celsius(self):
            self.kelvin = 0.0

    temp = Temperature(kelvin=100)

    print(temp.celsius)
    # -173.15

    del temp.celsius

    print(temp.celsius)
    # -273.15


Assignments
===========

Longitude and Latitude
----------------------
* Filename: ``descriptor_geographic.py``
* Lines of code to write: 25 lines
* Estimated time of completion: 15 min

#. Stwórz klasę ``GeographicCoordinate``
#. Klasa ma mieć pola:

    * ``latitude`` - min: -180.0; max: 180.0
    * ``longitude`` - min: -90.0; max 90.0
    * ``elevation`` - min: -10,994; max: 8,848 m

#. Wykorzystując deskryptory dodaj mechanizm sprawdzania wartości
#. Przy kasowaniu (``del``) wartości, nie usuwaj jej, a ustaw na ``None``
#. Zablokuj całkowicie modyfikację pola ``elevation``

:The whys and wherefores:
    * Wykorzystanie deskryptorów
    * Walidacja danych

Temperatura
-----------
* Filename: ``descriptor_temperature.py``
* Lines of code to write: 25 lines
* Estimated time of completion: 15 min

#. Stwórz klasę ``KelvinTemperature``
#. Temperatura musi być dodatnia, sprawdzaj to przy zapisie do pola ``value``
#. Usunięcie temperatury nie usunie wartości, ale ustawi ją na ``None``

:The whys and wherefores:
    * Wykorzystanie deskryptorów
    * Walidacja danych
