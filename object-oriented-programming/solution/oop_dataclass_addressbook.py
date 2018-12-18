from dataclasses import dataclass


@dataclass
class Address:
    street: str = None
    city: str = None


@dataclass
class Contact:
    first_name: str
    last_name: str
    addresses: list = ()


@dataclass
class AddressBook:
    contacts: list


addresses = AddressBook(contacts=[
    Contact(first_name='José', last_name='Jiménez'),
    Contact(first_name='Иван', last_name='Иванович', addresses=[]),
    Contact(first_name='Pan', last_name='Twardowski', addresses=[
        Address(street='2101 E NASA Pkwy', city='Houston'),
        Address(city='Kennedy Space Center'),
        Address(street='4800 Oak Grove Dr', city='Pasadena'),
        Address(street='2825 E Ave P', city='Palmdale'),
    ])
])
