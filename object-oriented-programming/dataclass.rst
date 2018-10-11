*********
Dataclass
*********

Old style classes
=================
.. code-block:: python

    class Astronaut:
        def __init__(self, first_name, last_name, agency='NASA'):
            self.first_name = first_name
            self.last_name = last_name
            self.agency = agency

New style dataclasses
=====================
.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Astronaut:
        first_name: str
        last_name: str
        agency: str = 'NASA'

``__init__`` vs. ``__post_init__``
==================================
.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Kelvin:
        value: float = 0.0

        def __post_init__(self):
            if self.value < 0.0:
                raise ValueError('Temperature must be greater than 0')


    temp = Kelvin(-300)



More advanced options
=====================
.. code-block:: python

    @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)

.. csv-table:: More advanced options
    :header-rows: 1
    :file: data/dataclass-options.csv

Under the hood
==============

Write
-----
.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class InventoryItem:
        name: str
        unit_price: float
        quantity_on_hand: int = 0

        def total_cost(self) -> float:
            return self.unit_price * self.quantity_on_hand

Dataclass will add
------------------
.. code-block:: python

    class InventoryItem:

        def total_cost(self) -> float:
            return self.unit_price * self.quantity_on_hand

        def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0) -> None:
            self.name = name
            self.unit_price = unit_price
            self.quantity_on_hand = quantity_on_hand

        def __repr__(self):
            return f'InventoryItem(name={self.name!r}, unit_price={self.unit_price!r}, quantity_on_hand={self.quantity_on_hand!r})'

        def __eq__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity_on_hand) == (other.name, other.unit_price, other.quantity_on_hand)
            return NotImplemented

        def __ne__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity_on_hand) != (other.name, other.unit_price, other.quantity_on_hand)
            return NotImplemented

        def __lt__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity_on_hand) < (other.name, other.unit_price, other.quantity_on_hand)
            return NotImplemented

        def __le__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity_on_hand) <= (other.name, other.unit_price, other.quantity_on_hand)
            return NotImplemented

        def __gt__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity_on_hand) > (other.name, other.unit_price, other.quantity_on_hand)
            return NotImplemented

        def __ge__(self, other):
            if other.__class__ is self.__class__:
                return (self.name, self.unit_price, self.quantity_on_hand) >= (other.name, other.unit_price, other.quantity_on_hand)
            return NotImplemented

Assignments
===========

Address Book (dataclass)
------------------------
#. Zmień kod książki adresowej z listingu :numref:`listing-oop-dataclass-addressbook` na wykorzystujący mechanizm ``dataclass``

.. literalinclude:: assignment/dataclass_addressbook.py
    :name: listing-oop-dataclass-addressbook
    :language: python
    :caption: Easy object implementation of Address Book

:About:
    * Filename: ``oop_dataclass_addressbook.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 10 min
