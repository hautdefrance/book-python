**********
Descriptor
**********

 - They provide the developer with the ability to add managed attributes to objects
 - The methods needed to create a descriptor are ``__get__``, ``__set__`` and ``__delete__``
 - If you define any of these methods, then you have created a descriptor

Builtin Descriptor Object Examples
----------------------------------
- classmethod
- staticmethod
- property
- functions in general

The Descriptor Protocol
=======================
- ``__get__(self, obj, type=None) -> Any``
- ``__set__(self, obj, value) -> None``
- ``__delete__(self, obj) -> None``

Example
=======
.. code-block:: python

    class Bar:
        def __init__(self):
            self.value = ''

        def __get__(self, instance, owner):
            print "returned from descriptor object"
            return self.value

        def __set__(self, instance, value):
            print "set in descriptor object"
            self.value = value

        def __delete__(self, instance):
            print "deleted in descriptor object"
            del self.value

    class Foo:
        bar = Bar()

    f = Foo()

    f.bar = 10      # will trigger __set__()
    print(f.bar)    # will trigger __get__()
    del f.bar       # will trigger __delete__()

.. code-block:: python

    class Celsius:
        def __init__(self, value=0.0):
            self.value = float(value)

        def __get__(self, instance, owner):
            return self.value

        def __set__(self, instance, value):
            self.value = float(value)


    class Fahrenheit:
        def __get__(self, instance, owner):
            return instance.celsius * 9 / 5 + 32

        def __set__(self, instance, value):
            instance.celsius = (float(value)-32) * 5 / 9


    class Temperature:
        celsius = Celsius()
        fahrenheit = Fahrenheit()


    temp = Temperature()

    temp.fahrenheit = 450
    temp.celsius
    # 232.22222222222223

    temp.celsius = 175
    temp.fahrenheit
    # 347.0

Accessors
=========

``__delattr__()``
-----------------
.. code-block:: python

    class Point:
        x = 10
        y = -5
        z = 0

    delattr(Point, 'z')
    del Point.y

``__getattribute__()``
----------------------
.. code-block:: python

    class Point:
        x = 10
        y = -5
        z = 0

    x = getattr(Point, 'x')
    # 10

``__setattr__()``
-----------------
.. code-block:: python

    class Kelvin:
        def __init__(self, initial_temperature):
            self.temperature = initial_temperature

        def __setattr__(self, name, new_value):
            if name == 'value' and new_value < 0.0:
                raise ValueError('Temperature cannot be negative')
            else:
                super().__setattr__(name, new_value)


    temp = Kelvin(273)

    temp.value = 20
    print(temp.value)   # 20

    temp.value = -10
    print(temp.value)   # ValueError: Temperature cannot be negative


Assignments
===========

Longtitude and Latitude
-----------------------
#. Stwórz klasę ``GeographicCoordinate``
#. Klasa ma mieć pola:

    * ``latitude`` - min: -180.0; max: 180.0
    * ``longitude`` - min: -90.0; max 90.0
    * ``elevation`` - min: -10,994; max: 8,848 m

#. Wykorzystując deskryptory dodaj mechanizm sprawdzania wartości
#. Przy kasowaniu (``del``) wartości, nie usuwaj jej, a ustaw na ``None``
#. Zablokuj całkowicie modyfikację pola ``elevation``

:About:
    * Filename: ``descriptor_geographic.py``
    * Lines of code to write: 25 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Wykorzystanie deskryptorów
    * Walidacja danych


Temperatura
-----------
#. Stwórz klasę ``KelvinTemperature``
#. Temperatura musi być dodatnia, sprawdzaj to przy zapisie do pola ``value``
#. Usunięcie temperatury nie usunie wartości, ale ustawi ją na ``None``

:About:
    * Filename: ``descriptor_temperature.py``
    * Lines of code to write: 25 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Wykorzystanie deskryptorów
    * Walidacja danych
