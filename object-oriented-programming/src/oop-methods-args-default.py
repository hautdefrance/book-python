class Astronaut:
    def say_hello(self, text='Ehlo World!'):
        print(text)


jose = Astronaut()

jose.say_hello(text='Privyet')     # Privyet
jose.say_hello('Hello')            # Hello
jose.say_hello()                   # Ehlo World!
