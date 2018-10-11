class Astronaut:
    def __init__(self, name, agency='NASA'):
        self.name = name
        self.agency = agency

    def __str__(self):
        return f'My name... {self.name}'

    def __repr__(self):
        return f'Astronaut(name="{self.name}", agency="{self.agency}")'


jose = Astronaut(name='José Jiménez', agency='NASA')
print(jose)
# My name... José Jiménez

crew = [
    Astronaut(name='José Jimenéz', agency='NASA'),
    Astronaut(name='Matt Kowalski', agency='NASA'),
    Astronaut(name='Иван Иванович', agency='Roscosmos'),
    Astronaut(name='Alex Vogel', agency='ESA'),
]

print(crew)
# Astronaut(name='José Jiménez', agency='NASA')
# Astronaut(name='Matt Kowalski', agency='NASA')
# Astronaut(name='Ivan Иванович', agency='Roscosmos')
# Astronaut(name='Alex Vogel', agency='ESA')
