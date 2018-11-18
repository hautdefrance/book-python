class Astronaut:

    def get_name(self):
        return 'José Jiménez'

    def say_name(self):
        name = self.get_name()
        print(f'My name... {name}')


jose = Astronaut()

jose.get_name()         # 'José Jiménez!'
jose.say_name()         # My name... José Jiménez!
