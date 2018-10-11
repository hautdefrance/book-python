***********
Collections
***********

* https://docs.python.org/3/library/collections.html

It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.

This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.

    ================  ====================================================================
    Name              Description
    ----------------  --------------------------------------------------------------------
    ``namedtuple()``  factory function for creating tuple subclasses with named fields
    ``deque``         list-like container with fast appends and pops on either end
    ``ChainMap``      dict-like class for creating a single view of multiple mappings
    ``Counter``       dict subclass for counting hashable objects
    ``OrderedDict``   dict subclass that remembers the order entries were added
    ``defaultdict``   dict subclass that calls a factory function to supply missing values
    ``UserDict``      wrapper around dictionary objects for easier dict subclassing
    ``UserList``      wrapper around list objects for easier list subclassing
    ``UserString``    wrapper around string objects for easier string subclassing
    ================  ====================================================================

.. code-block:: python

    jose = {'first_name': 'José', 'last_name': 'Jiménez', 'agency': 'NASA'}

    print(jose)
    # {'first_name': 'José', 'last_name': 'Jiménez', 'agency': 'NASA'}

    print(jose['first_name'], jose['last_name'], jose['agency'])
    # José Jiménez NASA

``OrderedDict``
===============
.. code-block:: python

    from collections import OrderedDict

    jose = OrderedDict(first_name='José', last_name='Jiménez', agency='NASA')
    print(jose)
    # OrderedDict([('first_name', 'José'), ('last_name', 'Jiménez'), ('agency', 'NASA')])

``namedtuple``
==============
.. code-block:: python

    from collections import namedtuple

    Astronaut = namedtuple('Astronaut', ['first_name', 'last_name', 'agency'])
    jose = Astronaut(first_name='José', last_name='Jiménez', agency='NASA')

    print(jose)
    # Astronaut(first_name='José', last_name='Jiménez', agency='NASA')

    print(jose.first_name, jose.last_name, jose.agency)
    # José Jiménez NASA
