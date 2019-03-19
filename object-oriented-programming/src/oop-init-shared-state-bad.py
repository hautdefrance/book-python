class Contact:
    def __init__(self, name, addresses=[]):
        self.name = name
        self.addresses = addresses


jose = Contact(name='Jose Jimenez')

jose.addresses.append('2101 E NASA Pkwy, Houston, TX')
print('Jose:', jose.addresses)
# [2101 E NASA Pkwy, Houston, TX]

ivan = Contact(name='Ivan Ivanovich')
print('Ivan:', ivan.addresses)
# [2101 E NASA Pkwy, Houston, TX]
