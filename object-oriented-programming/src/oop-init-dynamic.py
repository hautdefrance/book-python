class Astronaut:
    def __init__(self, last_name, **kwargs):
        self.last_name = last_name

        for key, value in kwargs.items():
            setattr(self, key, value)


ivan = Astronaut(first_name='Иван', last_name='Иванович', agency='Roscosmos')
jose = Astronaut(last_name='Jimenez', addresses=())

print(ivan.first_name)  # Иван
print(jose.last_name)   # Jimenez
print(jose.__dict__)    # {'last_name': 'Jimenez', 'addresses': ()}
print(ivan.__dict__)    # {'last_name': 'Иванович', 'first_name': 'Иван', 'agency': 'Roscosmos'}
