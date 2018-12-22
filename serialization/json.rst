******************
JSON Serialization
******************


JSON syntax
===========
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


Pretty Printing JSON
====================
.. code-block:: console

    $ DATA='[{"sepalLength":5.1,"sepalWidth":3.5,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.9,"sepalWidth":3,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"}]'

    $ echo $DATA | python -m json.tool
    [
        {
            "sepalLength": 5.1,
            "sepalWidth": 3.5,
            "petalLength": 1.4,
            "petalWidth": 0.2,
            "species": "setosa"
        },
        {
            "sepalLength": 4.9,
            "sepalWidth": 3,
            "petalLength": 1.4,
            "petalWidth": 0.2,
            "species": "setosa"
        }
    ]

.. code-block:: console

    $ echo '{"sepalLength":5.1,"sepalWidth":3.5,}' | python -m json.tool
    Expecting property name enclosed in double quotes: line 1 column 37 (char 36)

.. code-block:: console

    $ URL='https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.json'
    $ curl $URL |python -m json.tool

Alternatywy:

- https://stedolan.github.io/jq/


Assignments
===========

Iris Serialize
--------------
* Filename: ``json_iris_serialize.py``
* Lines of code to write: 30 lines
* Estimated time of completion: 20 min

#. Dane z listingu poniżej zapisz do pliku ``iris.json`` w formacie JSON

    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:The whys and wherefores:
    * Serializacja danych
    * Korzystanie z biblioteki JSON
    * Konwersja typów
    * Praca z plikami

Iris deserialize
----------------
* Filename: ``json_iris_deserialize.py``
* Lines of code to write: 30 lines
* Estimated time of completion: 20 min
* Input data: :ref:`listing-json-iris`

#. Dane z listingu poniżej skopiuj do pliku "iris.json"

    .. literalinclude:: data/iris.json
        :name: listing-json-iris
        :language: python
        :caption: Iris dataset in JSON

#. Odczytaj dane z pliku, i wyświetl je w formacie ``List[tuple]``
#. Pierwsza linijka ma zawierać nagłówek
#. Kolejne linie mają mieć dane

:The whys and wherefores:
    * Deserializacja danych
    * Korzystanie z biblioteki JSON
    * Konwersja typów
    * Praca z plikami

Date serialization
------------------
* Filename: ``json_datetimes.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min

#. Skopiuj do swojego pliku strukturę danych :numref:`listing-json-assignment-datetime`
#. Zapisz ją do pliku JSON
#. Wczytaj ją z pliku JSON jako obiekty Pythona (ten sam efekt co na listingu)

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
* Filename: ``json_objects.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min

#. Skopiuj do pliku ``iris.json`` dane z listingu :numref:`listing-json-assignment-objects`
#. Stwórz klasy ``Setosa``, ``Virginica``, ``Versicolor``
#. Czytając dane z pliku twórz obiekty powyższych klas w zależności od wyniku pomiaru (pole "species")

:The whys and wherefores:
    * Serializacja danych
    * Korzystanie z biblioteki JSON
    * Serializowanie zagnieżdżonych obiektów

.. literalinclude:: src/json-assignment-objects.py
    :name: listing-json-assignment-objects
    :language: python
    :caption: Sample Python data JSON

Deserialize data from GITHub
----------------------------
* Filename: ``json_deserialize_github.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min

#. Za pomocą biblioteki ``requests`` pobierz dane z https://api.github.com/users
#. Iterując po rekordach twórz obiekty klasy ``User``

:The whys and wherefores:
    * Deserializacja danych
    * Korzystanie z biblioteki JSON
    * Deserializacja zagnieżdżonych obiektów
    * Reprezentacja klas na podstawie danych otrzymanych przez API

Deserialize
-----------
* Filename: ``json_deserialize_classes.py``
* Lines of code to write: 30 lines
* Estimated time of completion: 30 min

#. Po API dostajesz JSONa tak jak na listingu poniżej
#. Iterując po rekordach twórz obiekty klasy ``Astronaut``
#. Sparsuj ``user_permissions`` i przedstaw je za pomocą listy klas
#. Nazwa klasy to klucz w słowniku
#. Są zawsze cztery pola: ``"add", "modify", "view", "delete"``
#. Jeżeli jakieś pole jest wymienione, to ma wartość ``True``, jeżeli nie to ``False``

:The whys and wherefores:
    * Deserializacja danych
    * Korzystanie z biblioteki JSON
    * Deserializacja zagnieżdżonych obiektów
    * Reprezentacja klas na podstawie danych otrzymanych przez API

.. code-block:: text

    [{"model":"authorization.user","pk":1,"fields":{"password":"pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"commander","first_name":"Иван","last_name":"Иванович","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":2,"fields":{"password":"pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=","last_login":null,"is_superuser":false,"username":"executive-officer","first_name":"José","last_name":"Jiménez","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":3,"fields":{"password":"pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"crew-medical-officer","first_name":"Melissa","last_name":"Lewis","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":4,"fields":{"password":"pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=","last_login":null,"is_superuser":false,"username":"science-data-officer","first_name":"Mark","last_name":"Watney","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":5,"fields":{"password":"pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=","last_login":null,"is_superuser":false,"username":"communication-officer","first_name":"Pan","last_name":"Twardowski","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":6,"fields":{"password":"pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=","last_login":null,"is_superuser":false,"username":"eclss-officer","first_name":"Harry","last_name":"Stamper","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"eclss":["add","modify","view"]},{"science":["add","modify","view"]}]}}]
