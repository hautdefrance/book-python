**********
Time Utils
**********


Sleep
=====
.. literalinclude:: src/time-sleep.py
    :language: python
    :caption: Time sleep function


``calendar``
============
.. literalinclude:: src/calendar-html.py
    :language: python
    :caption: HTML Calendar


.. _timeit:

``timeit`` - Microbenchmarks
============================

``timeit`` from Python script
-----------------------------
.. literalinclude:: src/timeit_simple.py
    :language: python
    :caption: Timeit simple statement

.. literalinclude:: src/timeit_multiple.py
    :language: python
    :caption: Timeit multiple statements with setup code

.. literalinclude:: src/timeit_globals.py
    :language: python
    :caption: Timeit with ``globals()``

``timeit`` from terminal
------------------------
.. literalinclude:: src/timeit.sh
    :language: console
    :caption: Timeit

.. code-block:: text

    -n N, --number=N
    how many times to execute ‘statement’

    -r N, --repeat=N
    how many times to repeat the timer (default 5)

    -s S, --setup=S
    statement to be executed once initially (default pass)

    -p, --process
    measure process time, not wallclock time, using time.process_time() instead of time.perf_counter(), which is the default

    -u, --unit=U
    specify a time unit for timer output; can select nsec, usec, msec, or sec

    -v, --verbose
    print raw timing results; repeat for more digits precision

    -h, --help
    print a short usage message and exit
