class Astronaut:
    agency = 'NASA'

    def __init__(self, name):
        self.name = name


ivan = Astronaut(name='Иван Иванович')
jose = Astronaut(name='José Jiménez')
mark = Astronaut(name='Mark Watney')


# Check value of field agency
ivan.agency         # NASA
jose.agency         # NASA
mark.agency         # NASA
Astronaut.agency    # NASA


# Let's change Agency of ``ivan``
ivan.agency = 'Roscosmos'

ivan.agency         # Roscosmos
jose.agency         # NASA
mark.agency         # NASA
Astronaut.agency    # NASA


# Let's change agency of ``Astronaut`` class
Astronaut.agency = 'ESA'

ivan.agency         # Roscosmos
jose.agency         # ESA
mark.agency         # ESA
Astronaut.agency    # ESA
