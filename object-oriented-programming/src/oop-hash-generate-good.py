from collections import OrderedDict


class Astronaut:
    def __init__(self, first_name, last_name, agency='NASA'):
        self.first_name = first_name
        self.last_name = last_name
        self.agency = agency

    def __hash__(self):
        d = OrderedDict(self.__dict__)
        return hash(d)

    def __eq__(self, other):
        if self.__dict__ == other.__dict__:
            return True
        else:
            return False
