import json


class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state


class Contact:
    def __init__(self, name, addresses=()):
        self.name = name
        self.addresses = addresses


DATA = [
    Contact(name='Jan Twardowski', addresses=(
        Address(city='Houston', state='Texas'),
        Address(city='Kennedy Space Center', state='Florida'),
        Address(city='Pasadena', state='California'),
        Address(city='Palmdale', state='California'),
    )),
    Contact(name='Mark Watney'),
    Contact(name='José Jiménez', addresses=()),
]


class JSONObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        result = obj.__dict__
        result['__type__'] = obj.__class__.__name__
        return result


output = json.dumps(DATA, cls=JSONObjectEncoder)

print(output)
# [
#    {"__type__":"Contact", "name":"Jan Twardowski", "addresses":[
#          {"__type__":"Address", "city":"Houston", "state":"Texas"},
#          {"__type__":"Address", "city":"Kennedy Space Center", "state":"Florida"},
#          {"__type__":"Address", "city":"Pasadena", "state":"California"},
#          {"__type__":"Address", "city":"Palmdale", "state":"California"}]},
#    {"__type__":"Contact", "name":"Mark Watney", "addresses":[]},
#    {"__type__":"Contact", "name":"Jos\u00e9 Jim\u00e9nez", "addresses":[]}
# ]




# class Person:
#     def __init__(self, name=None, *args, **kwargs):
#         self.name = name
#
#
# class ABC(Person):
#     def __init__(self, wiek=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.wiek = wiek
#         print(locals())
#
# ABC(1, name='Jan', x=18)
#
#
#
# def wyswietl(a, b, c=0):
#
#     x = 1000
#     y = 190123
#     o = 'asdas'
#     print(lambda: print(x)())
#
# wyswietl(1, 2, 3)
