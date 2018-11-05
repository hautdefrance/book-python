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
    :caption: Serializing to JSON


Deserializing from JSON
-----------------------
.. literalinclude:: src/json-simple-loads.py
    :language: python
    :caption: Deserializing from JSON


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
    :caption: Simple loading returns ``str`` not ``datetime`` or ``date``

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

Deserialize
-----------
#. Po API dostajesz JSONa tak jak na listingu poniżej
#. Iterując po rekordach twórz obiekty klasy ``Astronaut``
#. Sparsuj ``user_permissions`` i przedstaw je za pomocą listy klas
#. Nazwa klasy to klucz w słowniku
#. Są zawsze cztery pola: ``"add", "modify", "view", "delete"``
#. Jeżeli jakieś pole jest wymienione, to ma wartość ``True``, jeżeli nie to ``False``

.. code-block:: text

    [{"model":"authorization.user","pk":1,"fields":{"password":"pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"commander","first_name":"Иван","last_name":"Иванович","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":2,"fields":{"password":"pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=","last_login":null,"is_superuser":false,"username":"executive-officer","first_name":"José","last_name":"Jiménez","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":3,"fields":{"password":"pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"crew-medical-officer","first_name":"Melissa","last_name":"Lewis","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":4,"fields":{"password":"pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=","last_login":null,"is_superuser":false,"username":"science-data-officer","first_name":"Mark","last_name":"Watney","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":5,"fields":{"password":"pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=","last_login":null,"is_superuser":false,"username":"communication-officer","first_name":"Matt","last_name":"Kowalski","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":6,"fields":{"password":"pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=","last_login":null,"is_superuser":false,"username":"eclss-officer","first_name":"Harry","last_name":"Stamper","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"eclss":["add","modify","view"]},{"science":["add","modify","view"]}]}}]

:About:
    * Filename: ``json_deserialize_classes.py``
    * Lines of code to write: 30 lines
    * Estimated time of completion: 30 min

:The whys and wherefores:
    * Deserializacja danych
    * Korzystanie z biblioteki JSON
    * Deserializacja zagnieżdżonych obiektów
    * Reprezentacja klas na podstawie danych otrzymanych przez API
