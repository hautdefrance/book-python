class Astronaut:
    def say_hello(self, text):
        print(text)


jose = Astronaut()

jose.say_hello(text='Privyet')     # Privyet
jose.say_hello('Hello')            # Hello
jose.say_hello()                   # TypeError: say_text() missing 1 required positional argument: 'text'
