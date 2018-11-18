class Astronaut:

    def say_name(self):
        print(f'My name... {self.name}')


jose = Astronaut()
jose.name = 'José Jiménez'

jose.say_name()         # My name... José Jiménez!
