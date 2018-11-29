class Astronaut:
    def say_hello(self):
        name = self.get_name()
        print(f'My name... {name}')

    def get_name(self):
        return 'José Jiménez'


jose = Astronaut()

jose.get_name()         # 'José Jiménez!'
jose.say_hello()         # My name... José Jiménez!
