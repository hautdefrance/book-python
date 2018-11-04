class Astronaut:
    def __init__(self, first_name, last_name, agency='NASA'):
        self.first_name = first_name
        self.last_name = last_name
        self.agency = agency


ivan = Astronaut(first_name='Иван', last_name='Иванович', agency='Roscosmos')
jose = Astronaut(first_name='José', last_name='Jiménez')

print(ivan.first_name)  # Иван
print(jose.last_name)   # Jiménez

print(jose.__dict__)    # {'first_name': 'José', 'last_name': 'Jiménez', 'agency': 'NASA'}
print(ivan.__dict__)    # {'first_name': 'Иван', 'last_name': 'Иванович', 'agency': 'Roscosmos'}
