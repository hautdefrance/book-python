from dataclasses import dataclass
from typing import List


@dataclass
class Address:
    location: str
    city: str = None

    def __post_init__(self):
        self.city = self.location

    def __repr__(self):
        d = {'city': self.city}
        return f'{d}'


@dataclass
class Contact:
    name: str
    addresses: List[Address]

    def __iadd__(self, other):
        self.addresses.append(other)
        return self

    def __contains__(self, item):
        if item in self.addresses:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.__dict__}'


contact = Contact(name='José Jiménez', addresses=[Address(location='JPL')])
contact += Address(location='Houston')
contact += Address(location='KSC')

print(contact)
# {'name': 'José Jiménez', 'addresses': [
#       {'location': 'JPL'},
#       {'location': 'Houston'},
#       {'location': 'KSC'}
# ]}

if Address(location='Bajkonur') in contact:
    print(True)
else:
    print(False)
# False
