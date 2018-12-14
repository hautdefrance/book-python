import json
from dataclasses import dataclass


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


addressbook = [
    Contact(first_name='Matt', last_name='Kowalski', addresses=(
        Address(street='2101 E NASA Pkwy', city='Houston', state='Texas', zipcode='77058', country='USA'),
        Address(street='', city='Kennedy Space Center', zipcode='32899', state='Florida', country='USA'),
        Address(street='4800 Oak Grove Dr', city='Pasadena', zipcode='91109', state='California', country='USA'),
        Address(street='2825 E Ave P', city='Palmdale', state='California', zipcode='93550', country='USA'),
    )),
    Contact(first_name='José', last_name='Jiménez'),
    Contact(first_name='Иван', last_name='Иванович', addresses=()),
]


def encoder(self, obj):
    result = obj.__dict__
    result['__type__'] = obj.__class__.__name__
    return result


json.JSONEncoder.default = encoder

output = json.dumps(addressbook)
print(output)
# [{"first_name": "Matt", "last_name": "Kowalski", "addresses": [{"street": "2101 E NASA Pkwy", "city": "Houston", "state": "Texas", "zipcode": "77058", "country": "USA", "__type__": "Address"}, {"street": "", "city": "Kennedy Space Center", "state": "Florida", "zipcode": "32899", "country": "USA", "__type__": "Address"}, {"street": "4800 Oak Grove Dr", "city": "Pasadena", "state": "California", "zipcode": "91109", "country": "USA", "__type__": "Address"}, {"street": "2825 E Ave P", "city": "Palmdale", "state": "California", "zipcode": "93550", "country": "USA", "__type__": "Address"}], "__type__": "Contact"}, {"first_name": "Jos\u00e9", "last_name": "Jim\u00e9nez", "addresses": [], "__type__": "Contact"}, {"first_name": "\u0418\u0432\u0430\u043d", "last_name": "\u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447", "addresses": [], "__type__": "Contact"}]
