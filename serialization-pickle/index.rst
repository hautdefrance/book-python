********************
Pickle serialization
********************

* What is ``pickle``?
* ``pickle`` vs. ``cPickle``
* Extension ``pkl``


Serializing objects
===================

To string
---------
.. literalinclude:: src/pickle-dumps.py
    :language: python
    :caption: Serializing objects to string

To file
-------
.. literalinclude:: src/pickle-dump.py
    :language: python
    :caption: Serializing objects to file


Deserializing objects
=====================

From string
-----------
.. literalinclude:: src/pickle-loads.py
    :language: python
    :caption: Deserializing objects from string

From file
---------
.. literalinclude:: src/pickle-load.py
    :language: python
    :caption: Deserializing objects from file


Assignments
===========

Pickle serialization
--------------------
#. Użyj obiektu książki adresowej stworzonego w zadaniu z serializacją
#. Za pomocą ``pickle`` zapisz kontakty z książki adresowej w pliku
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku

.. literalinclude:: assignment/pickle_addressbook.py
    :language: python
    :caption: Serializacja obiektów do Pickle
