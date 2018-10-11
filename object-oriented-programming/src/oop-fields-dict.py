class Astronaut:
    def __init__(self, name, agency='NASA'):
        self.name = name
        self.agency = agency


jose = Astronaut(name='José Jiménez')
ivan = Astronaut(name='Иван Иванович', agency='Roscosmos')

jose.__dict__    # {'name': 'José Jiménez', 'agency': 'NASA'}
ivan.__dict__    # {'name': 'Иван Иванович', 'agency': 'Roscosmos'}
