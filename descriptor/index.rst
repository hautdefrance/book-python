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

    class Quantity(object):
        __index = 0

        def __init__(self):
            self.__index = self.__class__.__index
            self._storage_name = f"quantity: {self.__index}"
            self.__class__.__index += 1

        def __set__(self, instance, value):
            if value > 0:
                setattr(instance, self._storage_name, value)
            else:
               raise ValueError('value should be >0')

       def __get__(self, instance, owner):
            return getattr(instance, self._storage_name)

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
    f.bar = 10
    print f.bar
    del f.bar

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
        """
        >>> oven = Temperature()

        >>> oven.fahrenheit = 450
        >>> oven.celsius
        232.22222222222223

        >>> oven.celsius = 175
        >>> oven.fahrenheit
        347.0
        """
        celsius = Celsius()
        fahrenheit = Fahrenheit()


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

Temperatura
-----------
#. Stwórz klasę ``KelvinTemperature``
#. Temperatura musi być dodatnia, sprawdzaj to przy zapisie do pola ``value``
#. Usunięcie temperatury nie usunie wartości, ale ustawi ją na ``None``
