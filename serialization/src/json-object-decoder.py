import json
import sys
from dataclasses import dataclass


DATA = """[{"first_name": "Pan", "last_name": "Twardowski", "addresses": [{"street": "2101 E NASA Pkwy", "city": "Houston", "state": "Texas", "zipcode": "77058", "country": "USA", "__type__": "Address"}, {"street": "Florida", "city": "Kennedy Space Center", "state": "", "zipcode": "32899", "country": "USA", "__type__": "Address"}, {"street": "4800 Oak Grove Dr", "city": "Pasadena", "state": "California", "zipcode": "91109", "country": "USA", "__type__": "Address"}, {"street": "2825 E Ave P", "city": "Palmdale", "state": "California", "zipcode": "93550", "country": "USA", "__type__": "Address"}], "__type__": "Contact"}, {"first_name": "Jos\u00e9", "last_name": "Jim\u00e9nez", "addresses": [], "__type__": "Contact"}, {"first_name": "\u0418\u0432\u0430\u043d", "last_name": "\u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447", "addresses": [], "__type__": "Contact"}]"""


@dataclass
class Address:
    street: str
    city: str
    state: str
    zipcode: str
    country: str


@dataclass
class Contact:
    first_name: str
    last_name: str
    addresses: tuple = ()


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
#   Contact(first_name='Pan', last_name='Twardowski', addresses=[
#       Address(street='2101 E NASA Pkwy', city='Houston', state='Texas', zipcode='77058', country='USA'),
#       Address(street='', city='Kennedy Space Center', state='Florida', zipcode='32899', country='USA'),
#       Address(street='4800 Oak Grove Dr', city='Pasadena', state='California', zipcode='91109', country='USA'),
#       Address(street='2825 E Ave P', city='Palmdale', state='California', zipcode='93550', country='USA')]),
#   Contact(first_name='José', last_name='Jiménez', addresses=[]),
#   Contact(first_name='Иван', last_name='Иванович', addresses=[])
# ]
