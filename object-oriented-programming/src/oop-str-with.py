class Astronaut:
    name = 'José Jiménez'

    def __str__(self):
        return f'My name... {self.name}'


jose = Astronaut()

str(jose)
# My name... José Jiménez

print(jose)
# My name... José Jiménez
