class Astronaut:

    def say_text(self, text='Ehlo World!'):
        print(text)


jose = Astronaut()

jose.say_text()         # Ehlo World!
jose.say_text('Hello')  # Hello
