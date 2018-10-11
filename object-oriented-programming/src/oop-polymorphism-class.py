class Astronaut:
    agency = None

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        raise NotImplementedError


class NASAAstronaut(Astronaut):
    agency = 'NASA'

    def say_hello(self):
        print(f'Howdy from {self.agency}')


class ESAAstronaut(Astronaut):
    agency = 'ESA'

    def say_hello(self):
        print(f'Guten Tag aus {self.agency}')


class RoscosmosAstronaut(Astronaut):
    agency = 'Roscosmos'

    def say_hello(self):
        print(f'Privyet z {self.agency}')


crew = [
    NASAAstronaut('José Jiménez'),
    RoscosmosAstronaut('Ivan Иванович'),
    ESAAstronaut('Alex Vogel'),
    NASAAstronaut('Mark Watney'),
]

for astronaut in crew:
    astronaut.say_hello()
    # Howdy from NASA
    # Privyet z Roscosmos
    # Guten Tag aus ESA
    # Howdy from NASA
