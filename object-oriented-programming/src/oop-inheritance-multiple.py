class Cosmonaut:
    job = 'Cosmonaut'
    agency = 'Roscosmos'


class Pilot:
    job = 'Pilot'


class Gieroy:
    status = 'Gieroy'


class GeroySovietskogoSoyuza(Gieroy, Cosmonaut, Pilot):
    def __init__(self, name):
        self.name = name


ivan = GeroySovietskogoSoyuza(name='Иван Иванович')

ivan.job        # 'Cosmonaut'
ivan.status     # 'Gieroy'
ivan.agency     # 'Roscosmos'
