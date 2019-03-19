class JSONMixin:
    def to_json(self):
        return ...

    @classmethod
    def from_json(cls, data):
        return ...


class CSVMixin:
    def to_csv(self):
        return ...

    @classmethod
    def from_csv(cls, data):
        return ...


class User(JSONMixin, CSVMixin):
    def __init__(self, first_name, last_name):
        ...
