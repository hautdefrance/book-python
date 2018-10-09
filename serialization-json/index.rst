******************
JSON Serialization
******************


Format JSON jest podobny do zapisu dict w Python, ale różni się:

    * nie może być przecinka po ostatnim elemencie list
    * zawsze są stosowane podwójne cudzysłowia
    * ``true`` i ``false`` jest pisane małymi literami
    * zamiast ``None`` jest ``null``


JSON Serialization of simple objects
====================================

Serializing to JSON
-------------------
.. literalinclude:: src/json-simple-dumps.py
    :language: python
    :caption: Zapis danych do formatu JSON


Deserializing from JSON
-----------------------
.. literalinclude:: src/json-simple-loads.py
    :language: python
    :caption: Odczyt danych z formatu JSON


Serializing ``datetime`` and ``date``
=====================================

Encoding ``datetime`` and ``date``
----------------------------------
.. literalinclude:: src/json-datetime-dumps.py
    :language: python
    :caption: Exception during encoding datetime

.. literalinclude:: src/json-datetime-encoder.py
    :language: python
    :caption: Encoding ``datetime`` and ``date``

Decoding ``datetime`` and ``date``
----------------------------------
.. literalinclude:: src/json-datetime-loads.py
    :language: python
    :caption: Simple loading ``datetime`` and ``date`` from JSON is not working

.. literalinclude:: src/json-datetime-decoder.py
    :language: python
    :caption: Decoding ``datetime`` and ``date``


Serializing objects
===================

Encoding objects
----------------
.. literalinclude:: src/json-object-encoder.py
    :language: python
    :caption: Encoding objects to JSON

Decoding objects
----------------
.. literalinclude:: src/json-object-decoder.py
    :language: python
    :caption: Decoding objects from JSON


Class based encoders and decoders
=================================

Class based encoder
-------------------
.. literalinclude:: src/json-class-encoder.py
    :language: python
    :caption: Class based encoder

Class based decoder
-------------------
.. literalinclude:: src/json-class-decoder.py
    :language: python
    :caption: Class based decoder


Assignments
===========

Date serialization
------------------
#. Skopiuj do swojego pliku strukturę danych :numref:`listing-json-assignment-datetime`
#. Zapisz ją do pliku json
#. Wczytaj ją z pliku json jako obiekty Pythona (ten sam efekt co na listingu)

:About:
    * Filename: ``json_datetimes.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Serializacja danych
    * Korzystanie z biblioteki JSON
    * Serializowanie zagnieżdżonych dat i dat z czasem

.. literalinclude:: src/json-assignment-datetime.py
    :name: listing-json-assignment-datetime
    :language: python
    :caption: Sample Python data JSON

Serializing custom class to JSON
--------------------------------
#. Skopiuj do pliku ``iris.json`` dane z listingu :numref:`listing-json-assignment-objects`
#. Stwórz klasy ``Setosa``, ``Virginica``, ``Versicolor``
#. Czytając dane z pliku twórz obiekty powyższych klas w zależności od wyniku pomiaru (pole "species")

:About:
    * Filename: ``json_objects.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 20 min

:The whys and wherefores:
    * Serializacja danych
    * Korzystanie z biblioteki JSON
    * Serializowanie zagnieżdżonych obiektów

.. literalinclude:: src/json-assignment-objects.py
    :name: listing-json-assignment-objects
    :language: python
    :caption: Sample Python data JSON
