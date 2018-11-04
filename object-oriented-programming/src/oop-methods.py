class Astronaut:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f'My name... {self.name}')

    def say_text(self, text='Ehlo World!'):
        print(text)


jose = Astronaut(name='José Jiménez')

jose.say_name()         # My name... José Jiménez!
jose.say_text()         # Ehlo World!
jose.say_text('Hello')  # Hello

