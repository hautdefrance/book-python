class Astronaut:
    first_name = ''     # public
    last_name = ''      # public
    _agency = None      # private

    def print_(self):   # avoid name collision with print
        print(self.__str__())

    def __str__(self):  # system function
        return f'My name... {self.name}'
