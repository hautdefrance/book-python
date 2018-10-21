class Kelvin:
    def __init__(self, value=None):
        self.value = value

    def __get__(self, parent, owner):
        print(locals())
        return self.value

    def __set__(self, parent, value):
        print(locals())
        self.value = value

    def __delete__(self, parent):
        print(locals())
        self.value = None


class Temperature:
    kelvin = Kelvin()


temp = Temperature()


temp.kelvin = 10
# will trigger __set__(), which prints:
# {
#   'self': <__main__.Kelvin object at 0x11b9f3470>,
#   'parent': <__main__.Temperature object at 0x11b9f34a8>,
#   'value': 10
# }

print(temp.kelvin)
# will trigger __get__(), which prints:
# {
#   'self': <__main__.Kelvin object at 0x11b9f3470>,
#   'parent': <__main__.Temperature object at 0x11b9f34a8>,
#   'owner': <class '__main__.Temperature'>
# }

del temp.kelvin
# will trigger __delete__()
# {
#   'self': <__main__.Kelvin object at 0x11b9f3470>,
#   'parent': <__main__.Temperature object at 0x11b9f34a8>
# }
