***************
Basic Debugging
***************


Run in the console
==================
* Execute cell
* Run File in the console


``print``
=========
.. code-block:: python

    DATA = ['a', 'b', 'c', [1, 2, 3]]

    for element in DATA:
        print(element)
        # a
        # b
        # c
        # [1, 2, 3]


Case Study
----------

Good
^^^^
:settings.py:
    .. code-block:: python

        ADMIINSTRATORS = 'jose.jimenez@nasa.gov',

:main.py:
    .. code-block:: python

        from settings import ADMIINSTRATORS

        for config in MY_CONFIGURATION:
            print(config)

        # jose.jimenez@nasa.gov

Bad
^^^
:settings.py:
    .. code-block:: python

        ADMIINSTRATORS = 'jose.jimenez@nasa.gov'

:main.py:
    .. code-block:: python

        from settings import ADMIINSTRATORS

        for config in MY_CONFIGURATION:
            print(config)

        # j
        # o
        # s
        # e
        # .
        # j
        # ...
        # g
        # o
        # v


``pprint``
==========
.. code-block:: python

    from pprint import pprint

    pprint(...)

.. code-block:: python

    import json
    from pprint import pprint

    DANE = '{"contacts": [{"id": 1, "created": "2018-06-13T09:57:55.405Z", "modified": "2018-06-13T10:16:13.975Z", "reporter_id": 1, "is_deleted": false, "first_name": "José", "last_name": "Jiménez", "date_of_birth": "1969-07-24", "email": "jose.jimenez@nasa.gov", "bio": "", "image": "33950257662_d7561fb140_o.jpg", "status": null, "gender": null}, {"id": 2, "created": "2018-06-13T10:26:46.948Z", "modified": "2018-06-13T10:26:46.948Z", "reporter_id": 1, "is_deleted": false, "first_name": "Matt", "last_name": "Kowalski", "date_of_birth": null, "email": null, "bio": "", "image": "", "status": null, "gender": null}, {"id": 3, "created": "2018-06-13T10:26:55.820Z", "modified": "2018-06-13T10:26:55.820Z", "reporter_id": 1, "is_deleted": false, "first_name": "Иван", "last_name": "Иванович", "date_of_birth": null, "email": null, "bio": "", "image": "", "status": null, "gender": null}, {"id": 15, "created": "2018-06-13T14:34:42.353Z", "modified": "2018-06-13T14:34:43.638Z", "reporter_id": null, "is_deleted": false, "first_name": "Mark", "last_name": "Watney", "date_of_birth": null, "email": null, "bio": null, "image": "", "status": null, "gender": null}]}'

    dane = json.loads(DANE)
    pprint(dane)

.. code-block:: python

    pprint(globals())

.. code-block:: python

    from pprint import pprint

    print(globals())
    pprint(globals())

    def hello(a, b, text='My name...'):
        first_name = 'José'
        last_name = 'Jiménez'
        pprint(locals())
        return locals()


    hello(1, 2)

``locals()``
============
.. code-block:: python

    def hello(a, b, text='My name...'):
        first_name = 'José'
        last_name = 'Jiménez'
        my_vars = locals()
        del my_vars['text']
        return my_vars


Using debugger in IDE
=====================

Setting Break Points
--------------------

Inspecting variable values
--------------------------

Resume Program
--------------
