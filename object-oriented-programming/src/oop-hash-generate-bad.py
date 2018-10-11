class Astronaut:
    def __init__(self, first_name, last_name, agency='NASA'):
        self.first_name = first_name
        self.last_name = last_name
        self.agency = agency

    def __hash__(self, *args, **kwargs):
        """
        __hash__ should return the same value for objects that are equal.
        It also shouldn't change over the lifetime of the object;
        generally you only implement it for immutable objects.
        """
        return hash(self.first_name) + hash(self.last_name) + hash(self.agency)

    def __eq__(self, other):
        if self.first_name == other.first_name and \
                self.last_name == other.last_name and \
                self.agency == other.agency:
            return True
        else:
            return False
