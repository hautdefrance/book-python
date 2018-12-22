**************
Dates and Time
**************

.. warning:: If you're thinking about implementing your own time calculator or system, watch Computerophile Time & Time Zones https://www.youtube.com/watch?v=-5wpm-gesOY


Creating ``date`` objects
=========================

Create ``date``
---------------
.. literalinclude:: src/date-custom.py
    :language: python
    :caption: Create ``date``

Current ``date``
----------------
.. literalinclude:: src/date-current.py
    :language: python
    :caption: Current ``date``


Creating ``time`` objects
=========================

Create ``time``
---------------
.. literalinclude:: src/time-custom.py
    :language: python
    :caption: Create ``time``

Create empty ``time`` (midnight)
--------------------------------
.. literalinclude:: src/time-midnight.py
    :language: python
    :caption: Create empty ``time`` - midnight


Creating ``datetime`` objects
=============================

Create ``datetime``
-------------------
.. literalinclude:: src/datetime-custom.py
    :language: python
    :caption: Create ``datetime``

Create ``datetime`` with empty time (midnight)
----------------------------------------------
.. literalinclude:: src/datetime-midnight.py
    :language: python
    :caption: Create ``datetime`` with empty time

Create ``datetime`` from ``date`` and ``time`` objects
------------------------------------------------------
.. literalinclude:: src/datetime-compose.py
    :language: python
    :caption: Create ``datetime`` from ``date`` and ``time`` objects

Current ``datetime`` in local time
----------------------------------
.. literalinclude:: src/datetime-current-local.py
    :language: python
    :caption: Current ``datetime`` in local timezone


``datetime`` methods
====================
.. literalinclude:: src/datetime-methods.py
    :language: python
    :caption: ``datetime`` methods


Assignments
===========

Create ``date``, ``time`` and ``datetime`` objects
--------------------------------------------------
* Filename: ``datetime_create_custom.py``
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min

#. Stwórz obiekt ``date`` z datą Twojego urodzenia
#. Stwórz obiekt ``time`` z czasem Twojego urodzenia
#. Stwórz obiekt ``datetime`` z datą i czasem Twojego urodzenia

Create current ``date`` and ``datetime`` objects
------------------------------------------------
* Filename: ``datetime_create_current.py``
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min

#. Stwórz obiekt ``date`` z obecną datą
#. Stwórz obiekt ``datetime`` z datą i czasem
#. Jak stworzyć obiekt ``time`` obecnym czasem?

Create ``datetime`` object
--------------------------
* Filename: ``datetime_create.py``
* Lines of code to write: 1 lines
* Estimated time of completion: 5 min

#. Stwórz obiekt ``datetime`` z datą "1970-01-01T00:00:00.000000+0000"
#. Co to za data?
