class JSONSerializable:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class PickleSerializable:
    def to_pickle(self):
        import pickle
        return pickle.dumps(self)


class User(JSONSerializable, PickleSerializable):
    def __init__(self, first_name, last_name, address=()):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


user = User(
    first_name='Jan',
    last_name='Twardowski',
    address='Copernicus Crater, Moon'
)

print(user.to_json())
# {"first_name": "Jan", "last_name": "Twardowski", "address": "Copernicus Crater, Moon"}

print(user.to_pickle())
# b'\x80\x03c__main__\nUser\nq\x00)\x81q\x01}q\x02(X\n\x00\x00\x00first_nameq\x03X\x03\x00\x00\x00Janq\x04X\t\x00\x00\x00last_nameq\x05X\n\x00\x00\x00Twardowskiq\x06X\x07\x00\x00\x00addressq\x07X\x17\x00\x00\x00Copernicus Crater, Moonq\x08ub.'
