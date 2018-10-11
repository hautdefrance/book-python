class Astronaut:
    def __init__(self, name):
        self.name = name

    def say_hallo(self):
        print(f'My name... {self.name}')


class MaleAstronaut(Astronaut):
    gender = 'male'


class Gieroj(MaleAstronaut):
    status = 'hero'


ivan = Gieroj(name='Иван Иванович')
ivan.say_hallo()        # My name... Иван Иванович
ivan.status             # hero
ivan.gender             # male
