class Address:
    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return str(self.address)


class Contact:
    def __init__(self, name, addresses=[]):
        self.name = name
        self.addresses = addresses


jose = Contact(name='Jose Jimenez')
jsc = Address('2101 E NASA Pkwy, Houston, TX')
jose.addresses.append(jsc)
print(jose.addresses)
# [2101 E NASA Pkwy, Houston, TX]

ivan = Contact(name='Ivan Ivanovich')
print(ivan.addresses)
# [2101 E NASA Pkwy, Houston, TX]
