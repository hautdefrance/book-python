class Astronaut:
    name = 'José Jiménez'

    def say_hello(self, text='My name...'):
        print(f'{text} {self.name}!')


jose = Astronaut()

jose.say_hello()
# My name... José Jiménez!

jose.say_hello('¡Hola')
# ¡Hola José Jiménez!
