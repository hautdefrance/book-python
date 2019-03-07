class AddressBook:
    def __init__(self, contacts=()):
        self.contacts = contacts


class Address:
    def __init__(self, street=None, city=None):
        self.street = street
        self.city = city


class Contact:
    def __init__(self, first_name, last_name, addresses=()):
        self.first_name = first_name
        self.last_name = last_name
        self.address = addresses


AddressBook([
    Contact(first_name='José', last_name='Jiménez'),
    Contact(first_name='Иван', last_name='Иванович', addresses=[]),
    Contact(first_name='Jan', last_name='Twardowski', addresses=[
        Address(street='2101 E NASA Pkwy', city='Houston'),
        Address(city='Kennedy Space Center'),
        Address(street='4800 Oak Grove Dr', city='Pasadena'),
        Address(street='2825 E Ave P', city='Palmdale'),
    ])
])

