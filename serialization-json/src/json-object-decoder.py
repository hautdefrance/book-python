import json
from dataclasses import dataclass



DATA = """[{"first_name": "Matt", "last_name": "Kowalski", "addresses": [{"street": "2101 E NASA Pkwy", "city": "Houston", "state": "Texas", "zipcode": "77058", "country": "USA", "__type__": "Address"}, {"street": "", "city": "Kennedy Space Center", "state": "", "zipcode": "32899", "country": "USA", "__type__": "Address"}, {"street": "4800 Oak Grove Dr", "city": "Pasadena", "state": "", "zipcode": "91109", "country": "USA", "__type__": "Address"}, {"street": "2825 E Ave P", "city": "Palmdale", "state": "California", "zipcode": "93550", "country": "USA", "__type__": "Address"}], "__type__": "Contact"}, {"first_name": "Jos\u00e9", "last_name": "Jim\u00e9nez", "addresses": [], "__type__": "Contact"}, {"first_name": "\u0418\u0432\u0430\u043d", "last_name": "\u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447", "addresses": [], "__type__": "Contact"}]"""


@dataclass
class Address:
    street: str = ''
    city: str = ''
    state: str = ''
    zipcode: str = ''
    country: str = ''


@dataclass
class Contact:
    first_name: str = ''
    last_name: str = ''
    addresses: tuple = ()


class JSONDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.default)

    def default(self, obj):
        what = obj.pop('__type__')

        if not what:
            return None

        if what == 'Address':
            return Address(**obj)
        elif what == 'Contact':
            return Contact(**obj)


output = json.loads(DATA, cls=JSONDecoder)

print(output)
# [
#   Contact(first_name='Matt', last_name='Kowalski', addresses=[
#       Address(street='2101 E NASA Pkwy', city='Houston', state='Texas', zipcode='77058', country='USA'),
#       Address(street='', city='Kennedy Space Center', state='', zipcode='32899', country='USA'),
#       Address(street='4800 Oak Grove Dr', city='Pasadena', state='', zipcode='91109', country='USA'),
#       Address(street='2825 E Ave P', city='Palmdale', state='California', zipcode='93550', country='USA')]),
#   Contact(first_name='José', last_name='Jiménez', addresses=[]),
#   Contact(first_name='Иван', last_name='Иванович', addresses=[])
# ]
