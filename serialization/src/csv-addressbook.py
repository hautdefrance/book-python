class Contact:
    def __init__(self, first_name, last_name, addresses=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses


class Address:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


addressbook = [
    Contact(first_name='Jan', last_name='Twardowski', addresses=[
        Address(street='2101 E NASA Pkwy', city='Houston', state='Texas', code='77058', country='USA'),
        Address(street=None, city='Kennedy Space Center', code='32899', country='USA'),
        Address(street='4800 Oak Grove Dr', city='Pasadena', code='91109', country='USA'),
        Address(street='2825 E Ave P', city='Palmdale', state='California', code='93550', country='USA', data_urodzenia=None),
    ]),
    Contact(first_name='José', last_name='Jiménez'),
    Contact(first_name='Иван', last_name='Иванович', addresses=[]),
]
