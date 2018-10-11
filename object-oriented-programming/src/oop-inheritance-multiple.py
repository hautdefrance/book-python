class Cosmonaut:
    agency = 'Roscosmos'


class Gieroy:
    status = 'gieroy'


class GeroySovietskogoSoyuza(Cosmonaut, Gieroy):
    def __init__(self, name):
        self.name = name

    def say_hallo(self):
        print(f'Здравствуйте... {self.name}')


ivan = GeroySovietskogoSoyuza(name='Иван Иванович')
ivan.say_hallo()        # Здравствуйте... Иван Иванович
ivan.status             # gieroy
ivan.agency             # Roscosmos
