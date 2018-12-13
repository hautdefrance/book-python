*****************
Keywords in loops
*****************


``break`` - exits loop
======================
.. code-block:: python

    while True:
        number = input('Type number: ')

        # if user hit enter, without typing number
        if not number:
            break


``continue`` - skips iteration
==============================
.. code-block:: python

    for i in range(0, 10):
        if i % 2 == 0:
            continue

        print(i)

    # 1
    # 3
    # 5
    # 7
    # 9

``else`` in loop
================
* ``else`` is executed at the end of the loop:

    .. code-block:: python

        i = 0

        while i < 5:
            print(i)
            i += 1
        else:
            print('Finished!')

        # 0
        # 1
        # 2
        # 3
        # 4
        # Finished!

    .. code-block:: python

        for i in range(0, 5):
            print(i)
        else:
            print('Finished!')

        # 0
        # 1
        # 2
        # 3
        # 4
        # Finished!

* ``else`` is not executed when loop exited with ``break``:

    .. code-block:: python

        i = 0

        while i < 5:
            print(i)
            i += 1
            if i % 2 == 0:
                break
        else:
            print('Finished!')

        # 0
        # 1

    .. code-block:: python

        for i in range(1, 5):
            print(i)
            if i % 2 == 0:
                break
        else:
            print('Finished!')

        # 0
        # 1
