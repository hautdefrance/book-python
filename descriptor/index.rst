**********
Descriptor
**********

 - They provide the developer with the ability to add managed attributes to objects
 - The methods needed to create a descriptor are ``__get__``, ``__set__`` and ``__delete__``
 - If you define any of these methods, then you have created a descriptor


The Descriptor Protocol
=======================
- ``__get__(self, obj, type=None) -> Any``
- ``__set__(self, obj, value) -> None``
- ``__delete__(self, obj) -> None``


Builtin Descriptor Object Examples
==================================
- classmethod
- staticmethod
- property
- functions in general


Example
=======
.. literalinclude:: src/descriptor-example-1.py
    :language: python
    :caption: Example

.. literalinclude:: src/descriptor-example-2.py
    :language: python
    :caption: Example


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
