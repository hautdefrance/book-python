class Contact:
    def __init__(self, name, addresses=()):
        self.name = name
        self.addresses = addresses if addresses else []


jose = Contact(name='Jose Jimenez')
jose.addresses.append('2101 E NASA Pkwy, Houston, TX')
print(jose.addresses)
# [2101 E NASA Pkwy, Houston, TX]

ivan = Contact(name='Ivan Ivanovich')
print(ivan.addresses)
# [2101 E NASA Pkwy, Houston, TX]
