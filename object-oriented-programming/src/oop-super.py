class Astronaut:
    def say_hello(self):
        print('I am an astronaut')


class FictionalAstronaut(Astronaut):
    def say_hello(self):
        print(f'My name... José Jiménez')
        super().say_hello()


jose = FictionalAstronaut()
jose.say_hello()
# My name... José Jiménez
# I am an astronaut
