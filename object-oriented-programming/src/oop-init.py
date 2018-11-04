class Astronaut:
    def __init__(self, first_name, last_name, agency='NASA'):
        self.first_name = first_name
        self.last_name = last_name
        self.agency = agency


jose = Astronaut(first_name='José', last_name='Jiménez')
ivan = Astronaut(first_name='Иван', last_name='Иванович', agency='Roscosmos')


print(jose.first_name)  # José
print(jose.last_name)   # Jiménez
print(ivan.agency)      # NASA

print(ivan.first_name)  # Иван
print(ivan.last_name)   # Иванович
print(ivan.agency)      # Roscosmos


