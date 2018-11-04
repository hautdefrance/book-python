class Astronaut:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name... {self.name}'


jose = Astronaut(name='José Jiménez')

str(jose)       # My name... José Jiménez
print(jose)     # My name... José Jiménez
