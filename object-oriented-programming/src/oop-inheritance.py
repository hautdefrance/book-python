class Spaceman:
    agency = None

    def __init__(self, name):
        self.name = name

    def what_is_your_agency(self):
        return self.agency


class Astronaut(Spaceman):
    agency = 'NASA'


class Cosmonaut(Spaceman):
    agency = 'Roscosmos'



jose = Astronaut(name='José Jiménez')
jose.what_is_your_agency()       # NASA

ivan = Cosmonaut(name='Иван Иванович')
ivan.what_is_your_agency()       # Roscosmos
