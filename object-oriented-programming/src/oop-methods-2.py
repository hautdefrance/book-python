class Astronaut:
    def say_hello(self):
        print(f'My name... {self.name}')


jose = Astronaut()
jose.name = 'José Jiménez'

jose.say_hello()         # My name... José Jiménez!
