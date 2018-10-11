class Astronaut:
    name = 'José Jiménez'

    @staticmethod
    def say_hello():
        print('Hello')


jose = Astronaut()
jose.say_hello()        # Hello

Astronaut.say_hello()   # Hello
