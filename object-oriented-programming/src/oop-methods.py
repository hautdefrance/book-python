class Astronaut:

    def say_text(self, text='Ehlo World!'):
        print(text)

    def get_name(self):
        return 'José Jiménez'

    def say_name(self):
        print(f'My name... {self.get_name()}')


jose = Astronaut(name='José Jiménez')

jose.get_name()         # 'José Jiménez!'
jose.say_name()         # My name... José Jiménez!
jose.say_text()         # Ehlo World!
jose.say_text('Hello')  # Hello

