.. _Metaclass:

*********
Metaclass
*********

    "Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don’t (the people who actually need them know with certainty that they need them, and don’t need an explanation about why)." -- Tim Peters


Metaclass mechanism
===================

What are Metaclasses?
---------------------
* Class is an instance of a Metaclass
* Class defines how an instance of the class behaves
* Metaclass defines how a class behaves

.. figure:: img/metaclass-instances.png
    :scale: 75%
    :align: center

    Class is an instance of a metaclass.

How Metaclasses works?
----------------------
* Instances are created by calling the class
* Python creates a new class (when it executes the 'class' statement) by calling the metaclass
* Combined with the normal ``__init__`` and ``__new__`` methods
* Metaclasses allow you to do 'extra things' when creating a class

Example use of Metaclasses
--------------------------
* Allow customization of class instantiation
* Most commonly used as a class-factory
* Registering the new class with some registry
* Replace the class with something else entirely


Type and objects
================
.. code-block:: python

    type(int)       # <class 'type'>
    type(float)     # <class 'type'>
    type(dict)      # <class 'type'>
    type(list)      # <class 'type'>
    type(tuple)     # <class 'type'>

.. code-block:: python

    type(type)      # <class 'type'>

.. figure:: img/metaclass-class-chain.png
    :scale: 75%
    :align: center

    Class is an instance of a metaclass.


.. code-block:: python
    :caption: Metaclass

    class Iris:
        pass

    flower = Iris()

    isinstance(flower, Iris)    # True
    isinstance(flower, object)  # True

    Iris.__mro__
    # (<class '__main__.Iris'>, <class 'object'>)


Example
=======
.. code-block:: python

    class Iris:
        pass

    def new(cls):
        obj = object.__new__(cls)
        obj.kingdom = 'Plantae'
        return obj

    Iris.__new__ = new

    setosa = Iris()
    versicolor = Iris()

    setosa.kingdom      # Plantae
    versicolor.kingdom  # Plantae

.. code-block:: python
    :caption: Spoiler alert:  This doesn't work!

    def new(cls):
        obj = type.__new__(cls)
        obj.kingdom = 'Plantae'
        return obj

    type.__new__ = new
    # TypeError: can't set attributes of built-in/extension type 'type'

.. code-block:: python

    class Iris(type):
        def __new__(cls, *args, **kwargs):
            obj = super().__new__(cls, *args, **kwargs)
            obj.kingdom = 'Plantae'
            return obj

    class Setosa(metaclass=Iris):
        pass

    class Virginica(metaclass=Iris):
        pass

    class Versicolor(metaclass=Iris):
        pass


    Setosa.kingdom         # Plantae
    Virginica.kingdom      # Plantae
    Versicolor.kingdom     # Plantae

Factories
=========

Object factory
--------------
.. code-block:: python
    :caption: Object factory

    class Iris:
        def __init__(self):
            self.kingdom = 'Plantae'


    setosa = Iris()
    versicolor = Iris()
    virginica = Iris()

    setosa.kingdom          # Plantae
    versicolor.kingdom      # Plantae
    virginica.kingdom       # Plantae

Class Factory
-------------
.. code-block:: python
    :caption: Class Factory

    class Iris(type):
        def __init__(cls, *args, **kwargs):
            cls.kingdom = 'Plantae'


     class Setosa(metaclass=Iris):
        pass

    class Virginica(metaclass=Iris):
        pass

    class Versicolor(metaclass=Iris):
        pass


    Setosa.kingdom         # Plantae
    Virginica.kingdom      # Plantae
    Versicolor.kingdom     # Plantae


Metaclass replacements
======================
* Effectively accomplish the same thing

Inheritance
-----------
.. code-block:: python

    class Iris:
        kingdom = 'Plantae'

    class Setosa(Iris):
        pass

    Setosa.kingdom
    # Plantae

Class Decorator
---------------
.. code-block:: python

    def add_kingdom(cls):
        class NewIris(cls):
            kingdom = 'Plantae'
        return NewIris

    @add_kingdom
    class Iris:
        pass

    Iris.kingdom
    # Plantae
