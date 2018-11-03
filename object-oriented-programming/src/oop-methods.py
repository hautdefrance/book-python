class Astronaut:
    def __init__(self, name):
        self.name = name

    def say_my_name(self):
        print(f'My name... {self.name}')

    def say_hello(self, text='Ehlo World!'):
        print(text)


jose = Astronaut(name='José Jiménez')

jose.say_my_name()
# My name... José Jiménez!

jose.say_hello()
# Ehlo World!

jose.say_hello('Hello')
# Hello
