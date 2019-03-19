class Contact:
    def __init__(self, name, addresses=()):
        self.name = name
        self.addresses = list(addresses)


jose = Contact(name='Jose Jimenez')
jose.addresses.append('2101 E NASA Pkwy, Houston, TX')
print(jose.addresses)
# [2101 E NASA Pkwy, Houston, TX]

ivan = Contact(name='Ivan Ivanovich')
print(ivan.addresses)
# []
