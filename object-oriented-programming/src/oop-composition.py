class JSONSerializable:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class PickleSerializable:
    def to_pickle(self):
        import pickle
        return pickle.dumps(self)


class Connection(JSONSerializable, PickleSerializable):
    def __init__(self, host, user, password=None):
        self.host = host
        self.user = user
        self.password = password


connection = Connection(
    host='localhost',
    user='admin',
    password='admin'
)

connection.to_json()
# {"host": "localhost", "user": "admin", "password": "admin"}

connection.to_pickle()
# b'\x80\x03c__main__\nServer\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00hostq\x03X\t\x00\x00\x00localhostq\x04X\x04\x00\x00\x00userq\x05X\x05\x00\x00\x00adminq\x06X\x08\x00\x00\x00passwordq\x07h\x06ub.'
