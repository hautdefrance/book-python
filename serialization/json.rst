******************
JSON Serialization
******************


JSON syntax
===========
Format *JSON* jest podobny do zapisu ``dict`` w *Python*, ale różni się:

    * nie może być przecinka po ostatnim elemencie ``list``
    * zawsze stosowany jest podwójny cudzysłów
    * ``true`` i ``false`` jest pisane małymi literami
    * zamiast ``None`` jest ``null``
    * konwencją jest stosowanie ``camelCase`` a nie ``snake_case``, ale oba są poprawne

Example
-------
.. code-block:: json

    [
        {"sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
        {"sepalLength": 4.9, "sepalWidth": 3.0, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
        {"sepalLength": false, "sepalWidth": true, "petalLength": null, "petalWidth": 0.2, "species": null}
    ]


JSON Serialization of simple objects
====================================
* ``json.dump(DATA, file)``
* ``json.dumps(DATA)``
* ``json.load(DATA, file)``
* ``json.loads(DATA)``

Serialize to JSON
-----------------
.. code-block:: python
    :caption: Serializing to JSON

    import json


    DATA = {
        'first_name': 'Jan',
        'last_name': 'Twardowski'
    }

    output = json.dumps(DATA)
    print(output)
    # '{"first_name": "Jan", "last_name": "Twardowski"}'


Deserialize from JSON
---------------------
.. code-block:: python
    :caption: Deserialize from JSON

    import json


    DATA = '{"first_name": "Jan", "last_name": "Twardowski"}'

    output = json.loads(DATA)
    print(output)
    # {
    #     'first_name': 'Jan',
    #     'last_name': 'Twardowski'
    # }


Serializing ``datetime`` and ``date``
=====================================

Encoding ``datetime`` and ``date``
----------------------------------
* Encoder will be used, when standard procedure fails

.. code-block:: python
    :caption: Exception during encoding datetime

    from datetime import datetime, date
    import json


    DATA = {
        'name': 'Pan Twardowski',
        'date': date(1961, 4, 12),
        'datetime': datetime(1969, 7, 21, 14, 56, 15),
    }

    output = json.dumps(DATA)
    # TypeError: Object of type date is not JSON serializable

.. code-block:: python
    :caption: Encoding ``datetime`` and ``date``

    from datetime import datetime, date
    import json


    DATA = {
        'name': 'Pan Twardowski',
        'date': date(1961, 4, 12),
        'datetime': datetime(1969, 7, 21, 14, 56, 15),
    }


    class JSONDatetimeEncoder(json.JSONEncoder):
        def default(self, value):

            if isinstance(value, datetime):
                return value.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            elif isinstance(value, date):
                return value.strftime('%Y-%m-%d')


    output = json.dumps(DATA, cls=JSONDatetimeEncoder)
    print(output)
    # '{"name": "Pan Twardowski", "date": "1961-04-12", "datetime": "1969-07-21T14:56:15.000Z"}'


Decoding ``datetime`` and ``date``
----------------------------------
.. code-block:: python
    :caption: Simple loading returns ``str`` not ``datetime`` or ``date``

    import json


    DATA = '{"name": "Pan Twardowski", "date": "1961-04-12", "datetime": "1969-07-21T14:56:15.000Z"}'

    output = json.loads(DATA)
    print(output)
    # {
    #     'name': 'Pan Twardowski',
    #     'date': '1961-04-12',
    #     'datetime': '1969-07-21T14:56:15.000Z',
    # }

.. code-block:: python
    :caption: Decoding ``datetime`` and ``date``

    from datetime import datetime, timezone
    import json


    DATA = '{"name": "Pan Twardowski", "date": "1961-04-12", "datetime": "1969-07-21T14:56:15.000Z"}'


    class JSONDatetimeDecoder(json.JSONDecoder):
        def __init__(self):
            super().__init__(object_hook=self.default)

        def default(self, obj):
            for key, value in obj.items():

                if key == 'datetime':
                    dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
                    obj['datetime'] = dt.replace(tzinfo=timezone.utc)

                elif key == 'date':
                    dt = datetime.strptime(value, '%Y-%m-%d')
                    obj['date'] = dt.replace(tzinfo=timezone.utc).date()

            return obj


    output = json.loads(DATA, cls=JSONDatetimeDecoder)
    print(output)
    # {
    #     'name': 'Pan Twardowski',
    #     'date': date(1961, 4, 12),
    #     'datetime': datetime(1969, 7, 21, 14, 56, 15, tzinfo=datetime.timezone.utc),
    # }


Serializing objects
===================

Encoding objects
----------------
* Encoder will be used, when standard procedure fails

.. code-block:: python
    :caption: Encoding objects to JSON

    import json


    class Address:
        def __init__(self, city, state):
            self.city = city
            self.state = state


    class Contact:
        def __init__(self, name, addresses=()):
            self.name = name
            self.addresses = addresses


    DATA = [
        Contact(name='Jan Twardowski', addresses=(
            Address(city='Houston', state='Texas'),
            Address(city='Kennedy Space Center', state='Florida'),
            Address(city='Pasadena', state='California'),
            Address(city='Palmdale', state='California'),
        )),
        Contact(name='Mark Watney'),
        Contact(name='José Jiménez', addresses=()),
    ]


    class JSONObjectEncoder(json.JSONEncoder):
        def default(self, obj):
            result = obj.__dict__
            result['__type__'] = obj.__class__.__name__
            return result


    output = json.dumps(DATA, cls=JSONObjectEncoder)

    print(output)
    # [
    #    {"__type__":"Contact", "name":"Jan Twardowski", "addresses":[
    #          {"__type__":"Address", "city":"Houston", "state":"Texas"},
    #          {"__type__":"Address", "city":"Kennedy Space Center", "state":"Florida"},
    #          {"__type__":"Address", "city":"Pasadena", "state":"California"},
    #          {"__type__":"Address", "city":"Palmdale", "state":"California"}]},
    #    {"__type__":"Contact", "name":"Mark Watney", "addresses":[]},
    #    {"__type__":"Contact", "name":"Jos\u00e9 Jim\u00e9nez", "addresses":[]}
    # ]

Decoding objects
----------------
.. code-block:: python
    :caption: Decoding objects from JSON

    import json
    import sys


    DATA = """
    [
       {"__type__":"Contact", "name":"Jan Twardowski", "addresses":[
             {"__type__":"Address", "city":"Houston", "state":"Texas"},
             {"__type__":"Address", "city":"Kennedy Space Center", "state":"Florida"},
             {"__type__":"Address", "city":"Pasadena", "state":"California"},
             {"__type__":"Address", "city":"Palmdale", "state":"California"}]},
       {"__type__":"Contact", "name":"Mark Watney", "addresses":[]},
       {"__type__":"Contact", "name":"Jos\u00e9 Jim\u00e9nez", "addresses":[]}
    ]"""


    class Address:
        def __init__(self, city, state):
            self.city = city
            self.state = state


    class Contact:
        def __init__(self, name, addresses=()):
            self.name = name
            self.addresses = addresses


    class JSONObjectDecoder(json.JSONDecoder):
        def __init__(self):
            super().__init__(object_hook=self.default)

        def default(self, obj):
            type = obj.pop('__type__')
            cls = getattr(sys.modules[__name__], type)
            return cls(**obj)


    output = json.loads(DATA, cls=JSONObjectDecoder)
    print(output)
    # [
    #     Contact(name='Jan Twardowski', addresses=(
    #         Address(city='Houston', state='Texas'),
    #         Address(city='Kennedy Space Center', state='Florida'),
    #         Address(city='Pasadena', state='California'),
    #         Address(city='Palmdale', state='California'),
    #     )),
    #     Contact(name='Mark Watney'),
    #     Contact(name='José Jiménez', addresses=()),
    # ]


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
    $ curl $URL

    [{"sepalLength":5.1,"sepalWidth":3.5,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.9,"sepalWidth":3,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.7,"sepalWidth":3.2,"petalLength":1.3,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.6,"sepalWidth":3.1,"petalLength":1.5,"petalWidth":0.2,"species":"setosa"},{"sepalLength":5,"sepalWidth":3.6,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":5.4,"sepalWidth":3.9,"petalLength":1.7,"petalWidth":0.4,"species":"setosa"},{"sepalLength":4.6,"sepalWidth":3.4,"petalLength":1.4,"petalWidth":0.3,"species":"setosa"},{"sepalLength":5,"sepalWidth":3.4,"petalLength":1.5,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.4,"sepalWidth":2.9,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.9,"sepalWidth":3.1,"petalLength":1.5,"petalWidth":0.1,"species":"setosa"},{"sepalLength":7,"sepalWidth":3.2,"petalLength":4.7,"petalWidth":1.4,"species":"versicolor"},{"sepalLength":6.4,"sepalWidth":3.2,"petalLength":4.5,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":6.9,"sepalWidth":3.1,"petalLength":4.9,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":5.5,"sepalWidth":2.3,"petalLength":4,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":6.5,"sepalWidth":2.8,"petalLength":4.6,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":5.7,"sepalWidth":2.8,"petalLength":4.5,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":6.3,"sepalWidth":3.3,"petalLength":4.7,"petalWidth":1.6,"species":"versicolor"},{"sepalLength":4.9,"sepalWidth":2.4,"petalLength":3.3,"petalWidth":1,"species":"versicolor"},{"sepalLength":6.6,"sepalWidth":2.9,"petalLength":4.6,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":5.2,"sepalWidth":2.7,"petalLength":3.9,"petalWidth":1.4,"species":"versicolor"},{"sepalLength":6.3,"sepalWidth":3.3,"petalLength":6,"petalWidth":2.5,"species":"virginica"},{"sepalLength":5.8,"sepalWidth":2.7,"petalLength":5.1,"petalWidth":1.9,"species":"virginica"},{"sepalLength":7.1,"sepalWidth":3,"petalLength":5.9,"petalWidth":2.1,"species":"virginica"},{"sepalLength":6.3,"sepalWidth":2.9,"petalLength":5.6,"petalWidth":1.8,"species":"virginica"},{"sepalLength":6.5,"sepalWidth":3,"petalLength":5.8,"petalWidth":2.2,"species":"virginica"},{"sepalLength":7.6,"sepalWidth":3,"petalLength":6.6,"petalWidth":2.1,"species":"virginica"},{"sepalLength":4.9,"sepalWidth":2.5,"petalLength":4.5,"petalWidth":1.7,"species":"virginica"},{"sepalLength":7.3,"sepalWidth":2.9,"petalLength":6.3,"petalWidth":1.8,"species":"virginica"},{"sepalLength":6.7,"sepalWidth":2.5,"petalLength":5.8,"petalWidth":1.8,"species":"virginica"},{"sepalLength":7.2,"sepalWidth":3.6,"petalLength":6.1,"petalWidth":2.5,"species":"virginica"}]

.. code-block:: console

    $ URL='https://raw.githubusercontent.com/AstroMatt/book-python/master/serialization/data/iris.json'
    $ curl $URL |python -m json.tool
    [
        {
            "petalLength": 1.4,
            "petalWidth": 0.2,
            "sepalLength": 5.1,
            "sepalWidth": 3.5,
            "species": "setosa"
        },
        {
            "petalLength": 1.4,
            "petalWidth": 0.2,
            "sepalLength": 4.9,
            "sepalWidth": 3,
            "species": "setosa"
        },
        {
            "petalLength": 1.3,
            "petalWidth": 0.2,
            "sepalLength": 4.7,
            "sepalWidth": 3.2,
            "species": "setosa"
        },
    ...


Assignments
===========

Iris Serialize
--------------
* Filename: ``json_iris_serialize.py``
* Lines of code to write: 30 lines
* Estimated time of completion: 20 min
* Input data: :numref:`listing-json-serialize`

#. Z danych wydziel nagłówek i pomiary
#. Na podstawie nagłówka przekonwertuj na ``List[dict]``

    - klucz: nazwa z nagłówka
    - wartość: obserwacje

    .. code-block:: python

        DATA = [
            {'Sepal length': 5.8, 'Sepal width': 2.7, ...},
            {'Sepal length': 5.1, 'Sepal width': 3.5, ...},
            {'Sepal length': 5.7, 'Sepal width': 2.8, ...},
            ...
        ]

#. Zapisz do pliku ``iris.json`` w formacie JSON

.. code-block:: python
    :name: listing-json-serialize
    :caption: Iris Serialize

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
* Input data: :numref:`listing-json-iris`

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
* Filename: ``json_datetime.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min

#. Skopiuj do swojego pliku strukturę danych :numref:`listing-json-assignment-datetime`
#. Zapisz ją do pliku JSON
#. Wczytaj ją z pliku JSON jako obiekty Pythona (ten sam efekt co na listingu)

:The whys and wherefores:
    * Serializacja danych
    * Korzystanie z biblioteki JSON
    * Serializowanie zagnieżdżonych dat i dat z czasem

.. literalinclude:: assignment/json-datetime.py
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

.. literalinclude:: assignment/json-objects.py
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

    [{"model":"authorization.user","pk":1,"fields":{"password":"pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"commander","first_name":"Иван","last_name":"Иванович","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":2,"fields":{"password":"pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=","last_login":null,"is_superuser":false,"username":"executive-officer","first_name":"José","last_name":"Jiménez","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":3,"fields":{"password":"pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"crew-medical-officer","first_name":"Melissa","last_name":"Lewis","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":4,"fields":{"password":"pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=","last_login":null,"is_superuser":false,"username":"science-data-officer","first_name":"Mark","last_name":"Watney","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":5,"fields":{"password":"pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=","last_login":null,"is_superuser":false,"username":"communication-officer","first_name":"Jan","last_name":"Twardowski","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":6,"fields":{"password":"pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=","last_login":null,"is_superuser":false,"username":"eclss-officer","first_name":"Harry","last_name":"Stamper","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"eclss":["add","modify","view"]},{"science":["add","modify","view"]}]}}]
