class Astronaut:
    agency = 'NASA'

    def __init__(self, name):
        self.name = name


# Objects - Instances
ivan = Astronaut(name='Иван Иванович')
jose = Astronaut(name='José Jiménez')
matt = Astronaut(name='Matt Kowalski')

ivan.agency         # NASA
jose.agency         # NASA
matt.agency         # NASA
Astronaut.agency    # NASA

ivan.agency = 'Roscosmos'

ivan.agency         # Roscosmos
jose.agency         # NASA
matt.agency         # NASA
Astronaut.agency    # NASA

Astronaut.agency = 'ESA'

ivan.agency         # Roscosmos
jose.agency         # ESA
matt.agency         # ESA
Astronaut.agency    # ESA
