class Pilot:
    current_job = 'Pilot'

    def __init__(self, name):
        self.name = name

    def say_hallo(self):
        print(f'My name... {self.name}')


class CosmonautPilot(Pilot):
    current_job = 'Cosmonaut'
    previous_job = 'Pilot'


class GieroyCosmonautPilot(CosmonautPilot):
    status = 'Gieroy'


ivan = GieroyCosmonautPilot(name='Иван Иванович')

ivan.say_hallo()        # Здравствуйте... Иван Иванович
ivan.current_job        # Cosmonaut
ivan.previous_job       # Pilot
ivan.status             # Gieroy
