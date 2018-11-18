class Spaceman:
    agency = None

    def __init__(self, name):
        self.name = name

    def get_agency(self):
        return self.agency


class Astronaut(Spaceman):
    agency = 'NASA'


class Cosmonaut(Spaceman):
    agency = 'Roscosmos'


jose = Astronaut(name='José Jiménez')
ivan = Cosmonaut(name='Иван Иванович')


jose.get_agency()       # NASA
ivan.get_agency()       # Roscosmos
