*********
Dataclass
*********


Example 1
=========

Old style classes
-----------------
.. code-block:: python

    class Astronaut:
        def __init__(self, first_name, last_name, agency='NASA'):
            self.first_name = first_name
            self.last_name = last_name
            self.agency = agency

Dataclasses
-----------
.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Astronaut:
        first_name: str
        last_name: str
        agency: str = 'NASA'


Field Factory
=============
.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class C:
        x: int
        y: int = field(repr=False)
        z: int = field(repr=False, default=10)
        t: int = 20

.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class C:
        mylist: List[int] = field(default_factory=list)

    c = C()
    c.mylist += [1, 2, 3]

Why?
----
* :ref:`Initial arguments mutability and shared state`

.. code-block:: python

    class Contact:
        def __init__(self, name, addresses=[]):
            self.name = name
            self.addresses = addresses


    jose = Contact(name='Jose Jimenez')
    jose.addresses.append('2101 E NASA Pkwy, Houston, TX')
    print(jose.addresses)
    # [2101 E NASA Pkwy, Houston, TX]

    ivan = Contact(name='Ivan Ivanovich')
    print(ivan.addresses)
    # [2101 E NASA Pkwy, Houston, TX]

So what?
--------
* ``field()`` creates new empty ``list`` for each object
* It does not reuse pointer


``__init__`` vs. ``__post_init__``
==================================

Old style classes
-----------------
.. code-block:: python

    class Kelvin:
        def __init__(self, value):
            if self.value < 0.0:
                raise ValueError('Temperature must be greater than 0')
            else:
                self.value = value


    temp = Kelvin(-300)

Dataclasses
-----------
.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class Kelvin:
        value: float = 0.0

        def __post_init__(self):
            if self.value < 0.0:
                raise ValueError('Temperature must be greater than 0')


    temp = Kelvin(-300)


Case Study
==========

Old style classes
-----------------
.. code-block:: python

    class StarWarsMovie:

        def __init__(self, title: str, episode_id: int, opening_crawl: str,
                     director: str, producer: str, release_date: datetime,
                     characters: List[str], planets: List[str], starships: List[str],
                     vehicles: List[str], species: List[str], created: datetime,
                     edited: datetime, url: str):

            self.title = title
            self.episode_id = episode_id
            self.opening_crawl= opening_crawl
            self.director = director
            self.producer = producer
            self.release_date = release_date
            self.characters = characters
            self.planets = planets
            self.starships = starships
            self.vehicles = vehicles
            self.species = species
            self.created = created
            self.edited = edited
            self.url = url

            if type(self.release_date) is str:
                self.release_date = dateutil.parser.parse(self.release_date)

            if type(self.created) is str:
                self.created = dateutil.parser.parse(self.created)

            if type(self.edited) is str:
                self.edited = dateutil.parser.parse(self.edited)

Dataclasses
-----------
.. code-block:: python

    from dataclasses import dataclass


    @dataclass
    class StarWarsMovie:
        title: str
        episode_id: int
        opening_crawl: str
        director: str
        producer: str
        release_date: datetime
        characters: List[str]
        planets: List[str]
        starships: List[str]
        vehicles: List[str]
        species: List[str]
        created: datetime
        edited: datetime
        url: str

        def __post_init__(self):
            if type(self.release_date) is str:
                self.release_date = dateutil.parser.parse(self.release_date)

            if type(self.created) is str:
                self.created = dateutil.parser.parse(self.created)

            if type(self.edited) is str:
                self.edited = dateutil.parser.parse(self.edited)



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
* Filename: ``oop_dataclass_addressbook.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Input data: :numref:`listing-dataclass_addressbook.json`

#. Stwórz klasy wykorzystujące mechanizm ``dataclass``

.. literalinclude:: assignment/dataclass_addressbook.json
    :name: listing-dataclass_addressbook.json
    :language: json
    :caption: Data for AddressBook
